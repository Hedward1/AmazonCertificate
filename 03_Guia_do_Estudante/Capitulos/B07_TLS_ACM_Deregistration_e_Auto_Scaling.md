# B07 — TLS/ACM, deregistration e EC2 Auto Scaling

**Data:** 01/08/2026 · **Aulas:** [080–086 + Q05](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b07)<br>
**Domínios:** 2, 3 e 4 · **Tarefa principal:** 3.2 — Design high-performing and elastic compute solutions · **Secundárias:** 3.4, 2.2 e 4.2<br>
**Pré-requisito:** [B06 — load balancers](B06_ALB_NLB_GWLB_Target_Groups_e_Cross_Zone.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá terminar TLS no balanceador com ACM; diferenciar front-end e back-end encryption; explicar deregistration delay; construir launch template e ASG Multi-AZ; escolher target tracking, step, simple, scheduled ou predictive scaling; e aplicar warmup, health checks e termination policies.

Você também deverá conseguir:

1. verificar Region, hostname e validação de um certificado;
2. separar TLS termination de recriptografia ao backend;
3. relacionar `min`, `desired` e `max` sem somá-los;
4. selecionar métrica proporcional à capacidade;
5. distinguir warmup, health-check grace period, cooldown e draining;
6. explicar como uma instância nova recebe configuração;
7. planejar rollout e rollback por versão do launch template;
8. encontrar custos que o ASG não remove automaticamente.

## 2. Como estudar as aulas

| Aulas | Foco |
|---|---|
| 80–81 | certificados TLS e ACM |
| 82 | connection draining/deregistration delay |
| 83–84 | ASG, launch template, min/desired/max, integração ELB |
| 85–86 | políticas, métricas, cooldown e warmup |
| Q05 | quiz após as aulas |

## 3. TLS e ACM

```text
cliente ==TLS/certificado público==> ALB/NLB
                                   └== HTTP ou HTTPS ==> target
```

TLS autentica o endpoint e protege dados em trânsito. O certificado deve cobrir o hostname usado pelo cliente e formar cadeia confiável. No ALB, um listener HTTPS termina TLS e pode encaminhar HTTP ou HTTPS ao target. Recriptografar o trecho interno atende defesa em profundidade/compliance, mas exige certificado e configuração no backend.

AWS Certificate Manager provisiona e renova certificados públicos elegíveis quando os requisitos de validação e associação continuam atendidos. Certificados ACM são **regionais**: use certificado na mesma Region do ALB; CloudFront é uma exceção importante, usando certificado em `us-east-1`. Certificados públicos exportáveis e privados têm regras/custos próprios; valide a opção atual.

SNI permite múltiplos certificados no mesmo listener. Um default certificate atende quando nenhum certificado adicional corresponde. DNS validation costuma ser preferida porque facilita renovação automática.

## 4. Deregistration delay

Ao desregistrar ou substituir target, ELB deixa de enviar novas requisições e permite conclusão das existentes até o delay. Um valor muito curto pode interromper requests; muito longo atrasa deploy e scale-in. Long-lived connections e WebSockets merecem medida real. “Draining” não significa que o processo pode ser morto imediatamente.

## 5. Auto Scaling Group

```text
Launch template → ASG {min, desired, max; subnets AZ-a/AZ-b}
                        ├→ EC2 → target group → ALB
CloudWatch metric → scaling policy ─┘
```

- **launch template:** AMI, instance type, SG, role, user data e opções de disco; versione mudanças;
- **min:** piso; **desired:** capacidade buscada agora; **max:** teto de escala;
- ASG substitui instâncias consideradas unhealthy e equilibra capacidade entre AZs;
- com ELB health checks habilitados, falha da aplicação pode disparar substituição, não só falha de status EC2;
- lifecycle hooks pausam launch/terminate para bootstrap, registro, coleta ou drenagem;
- instance refresh realiza rollout de nova versão do launch template;
- termination policy define qual instância sai, mas proteção contra scale-in pode preservar membros críticos.

## 6. Políticas de escala

| Sinal/requisito | Política | Decisão |
|---|---|---|
| manter métrica perto de alvo | target tracking | “termostato”; AWS gerencia alarms |
| reagir em degraus à gravidade | step scaling | ajustes diferentes por faixa do alarm |
| um único ajuste e cooldown | simple scaling | menos flexível; raramente primeira opção |
| pico previsível por calendário | scheduled | altera desired/min/max no horário |
| histórico recorrente e previsão | predictive | antecipa capacidade; combine com dinâmica |

Uma boa métrica de target tracking deve variar proporcionalmente à capacidade. `ALBRequestCountPerTarget` é útil quando requests por instância refletem carga. Backlog por instância pode ser métrica customizada. Total de requests sem normalização pode não diminuir após scale-out.

**Default instance warmup** impede que métricas de instâncias ainda inicializando distorçam decisões e bloqueia scale-in dinâmico durante o aquecimento. Cooldown clássico e warmup não são sinônimos; prefira configurar default instance warmup e entender a política usada.

## 7. Cenários resolvidos

### Cenário resolvido 1 — tráfego imprevisível

Uma API stateless tem CPU proporcional ao volume e precisa manter cerca de 50% com margem. **Decisão:** ASG em duas AZs, ALB, target tracking de `ASGAverageCPUUtilization`, min 2, max baseado em quota/orçamento e warmup equivalente ao bootstrap. Scheduled não reage ao imprevisível; step seria possível, mas exige thresholds.

### Cenário resolvido 2 — abertura semanal

Toda segunda às 08:00 há pico imediato; inicialização leva 12 minutos. **Decisão:** scheduled action antes do pico para elevar min/desired, mais target tracking para variações. Escalar somente após CPU subir chegaria tarde.

### Cenário resolvido 3 — deployment seguro

Nova AMI deve substituir gradualmente instâncias sem cortar downloads. **Decisão:** nova versão do launch template, instance refresh com capacidade saudável, health checks representativos e deregistration delay medido. TLS permanece no ALB com ACM.

## 8. Tabela de decisão e trade-offs

| Decisão | Benefício | Custo/risco |
|---|---|---|
| min 2 em duas AZs | tolera falha individual/zonal no tier | compute ocioso em baixa carga |
| target tracking | simples e adaptativo | métrica/target ruins causam sobre/subprovisão |
| warmup correto | evita reação a bootstrap | valor longo desacelera scale-in |
| Spot no ASG mixed instances | reduz custo | interrupção; diversidade e On-Demand base necessárias |
| TLS no ALB | gestão central e offload | trecho interno não cifrado se encaminhar HTTP |

## 9. Três temporizadores que não são iguais

| Temporizador | Início/objetivo | Erro comum |
|---|---|---|
| default instance warmup | após nova capacidade entrar; protege métricas de scaling | tratá-lo como tempo de desligamento |
| health-check grace period | após launch; evita substituição durante bootstrap | deixá-lo esconder falha real por tempo excessivo |
| deregistration delay | ao remover target; permite concluir requests | matar o processo antes do draining |

Cooldown ainda aparece em políticas e comportamento legado. Descubra qual
política usa qual parâmetro; não responda “aumente o cooldown” a qualquer
oscilação.

## 10. Saúde em camadas

```text
EC2 status checks
  └→ sistema operacional/host
ELB target health
  └→ porta/path/success codes da aplicação
Custom health
  └→ sinal operacional enviado ao ASG
```

Uma verificação profunda demais pode derrubar toda a frota quando uma dependência
compartilhada falha. Uma verificação rasa demais mantém targets incapazes de
servir. O endpoint deve provar capacidade de atender sem criar carga excessiva.

## 11. Novos cenários resolvidos

### Cenário resolvido 4 — fila como sinal

Workers consomem uma fila e cada instância processa 100 mensagens dentro do
SLA. Use backlog por instância como métrica customizada de target tracking ou
step scaling. Tamanho total da fila sozinho não é proporcional quando a
capacidade muda.

### Cenário resolvido 5 — certificado não renova

Um certificado público ACM associado ao ALB se aproxima do vencimento. Antes de
substituí-lo manualmente, valide se o DNS de validação permanece publicado, se
o certificado está associado a serviço compatível e se o domínio ainda está
sob controle. Renovação gerenciada depende dessas condições.

## 12. Deploy e proteção de capacidade

Instance refresh deve definir quanto da frota pode ficar indisponível e quando
uma instância é considerada pronta. Misturar Spot e On-Demand pode reduzir
custo, mas exige diversification, base On-Demand coerente e tolerância a
interrupção. Capacity Rebalancing pode iniciar substituição ao receber sinais de
risco Spot; não elimina a necessidade de idempotência e drenagem.

Lifecycle hooks podem:

- pausar launch para instalar/agrupar configuração;
- pausar terminate para coletar logs ou drenar um worker;
- publicar eventos para automação;
- expirar ou continuar conforme heartbeat/resultado.

Não use um hook para manter estado permanente dentro da instância. A frota deve
continuar substituível.

## 13. Custos, cleanup e armadilhas

ASG não tem cobrança separada, mas EC2, EBS, ELB, IPv4, CloudWatch custom metrics e tráfego cobram. `desired=0` não remove ALB nem volumes/snapshots externos. Delete ASG, load balancer, target groups, launch templates de teste e resíduos explicitamente.

Armadilhas: ASG não escala banco automaticamente; AMI nova no template não atualiza instâncias existentes sem rollout; target tracking gerencia seus alarms; scale-out costuma priorizar disponibilidade, scale-in é conservador; certificado vencido/hostname incorreto falha antes da aplicação; session state local dificulta scale-in; health check raso pode declarar uma instância “saudável” sem dependências essenciais.

## 14. Checklist e recuperação ativa

- [ ] desenho certificado→listener→target e ASG→TG;
- [ ] seleciono a política para imprevisível, degraus, calendário e previsão;
- [ ] explico warmup versus deregistration;
- [ ] prevejo o que acontece quando desired excede max (não permitido) ou cai abaixo de min.

- [ ] associo cada temporizador ao evento correto;
- [ ] explico por que target tracking cria e gerencia alarms;
- [ ] sei como publicar uma AMI nova em instâncias existentes;
- [ ] diferencio certificado regional do requisito especial do CloudFront;

Sem consultar, desenhe dois eventos completos: scale-out por CPU e scale-in
durante um download. Marque métrica, alarm, desired, warmup, target health,
draining e encerramento.

## 15. Ligações

- [LAB B07](../../05_Laboratorios/LAB_B07_Simulacao_ALB_ASG_e_Eventos_de_Escala.md)
- [Questões B07](../../04_Questoes_e_Revisoes/Blocos/B07_Questoes.md)
- [Gabarito B07](../../04_Questoes_e_Revisoes/Blocos/B07_Gabarito.md)
- [Checklist B07](../../06_Progresso/B07_Checklist_e_Revisoes.md)
- Próximo: [B08](B08_RDS_Aurora_RDS_Proxy_e_ElastiCache.md)

## 16. Referências oficiais

- [ACM concepts](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html)
- [HTTPS listeners for ALB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)
- [Deregistration delay](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#modify-target-group-health-settings)
- [EC2 Auto Scaling concepts](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)
- [Target tracking](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)
- [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)
- [Default instance warmup](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html)
