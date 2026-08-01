# B06 — ALB, NLB, GWLB, target groups e cross-zone

**Data planejada:** 31/07/2026<br>
**Comece pelas aulas:** [roteiro B06 — aulas 072–079](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b06); não há quiz neste bloco<br>
**Domínios:** 2 — Resilient Architectures; 3 — High-Performing Architectures; 4 — Cost-Optimized Architectures<br>
**Tarefa principal:** 3.4 — Determine high-performing and/or scalable network architectures<br>
**Secundárias:** 3.2, 2.2 e 4.2<br>
**Pré-requisito:** [B05 — storage e fundamentos de HA](B05_EBS_Instance_Store_EFS_e_Fundamentos_de_HA.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá escolher ALB, NLB ou GWLB; explicar listener, rule, target group e health check; projetar roteamento por host/path; prever preservação de source IP; avaliar stickiness e cross-zone; e identificar custo/cleanup.

Mais especificamente, você deverá conseguir:

1. separar a conexão front-end da conexão com o target;
2. selecionar o tipo de load balancer pelo protocolo e pela semântica;
3. desenhar listener, regras e target groups sem confundir responsabilidades;
4. criar health check que represente a capacidade real do serviço;
5. localizar o endereço do cliente em cada arquitetura;
6. prever a distribuição com e sem cross-zone;
7. explicar afinidade e externalização de estado;
8. projetar drenagem e cleanup de recursos independentes.

## 2. Como estudar as aulas

| Aulas | Foco |
|---|---|
| 72–74 | ALB, listeners, rules e target groups |
| 75–76 | NLB, desempenho L4 e IPs estáticos |
| 77 | GWLB e appliances transparentes |
| 78 | sticky sessions e estado |
| 79 | distribuição cross-zone e defaults atuais |

## 3. Modelo mental

```text
cliente → DNS do load balancer → listener → regra → target group → target saudável
                                                        └→ health check
```

O load balancer é regional e usa subnets/AZs habilitadas. O listener aceita conexões em protocolo/porta. No ALB, regras avaliam host, path, headers, método, source IP e outros critérios. O target group define tipo de target, protocolo/porta e health check. Um target só recebe tráfego quando registrado, em AZ habilitada e considerado saudável.

## 4. Tabela de decisão

| Requisito | ALB | NLB | GWLB |
|---|---|---|---|
| Camada | L7 | L4 | L3 gateway |
| Protocolos típicos | HTTP, HTTPS, gRPC | TCP, TLS, UDP, TCP_UDP | todo tráfego IP; GENEVE 6081 com appliances |
| Roteamento por host/path | sim | não | não |
| IP estático por AZ | não como regra de decisão clássica | sim; pode usar EIP em internet-facing | endpoint/rotas, não endpoint web |
| Source IP no target | normalmente em `X-Forwarded-For` | preservação depende do tipo/configuração; caso clássico: source IP | fluxo transparente para appliance |
| Uso | microservices/web | latência extrema, TCP/UDP, IP fixo | firewalls, IDS/IPS, inspeção |
| Security group | suportado | suportado em NLBs criados com SG; associação não pode ser adicionada depois se criado sem SG | appliances/endpoints exigem projeto de rede |

Não escolha apenas por “mais rápido”. Protocolo, roteamento, IP, observabilidade e appliance são palavras decisivas.

## 5. ALB

- precisa de pelo menos duas subnets em AZs diferentes para criação padrão;
- uma regra default sempre existe; regras adicionais têm prioridade;
- target groups podem usar instâncias, IPs ou Lambda, respeitando compatibilidade;
- uma instância pode participar de vários target groups;
- HTTP→HTTPS pode ser redirect; autenticação também pode ocorrer em regras suportadas;
- para o IP do cliente, a aplicação usa headers encaminhados pelo ALB, não o IP da conexão direta ao target.

### Cenário resolvido 1 — três serviços, um endpoint

`shop.example.com/api/*`, `/images/*` e `admin.example.com/*` usam serviços diferentes. **Decisão:** ALB com listener HTTPS, certificado, regras por host/path e três target groups. NLB não interpreta HTTP. Três load balancers funcionariam, mas aumentariam custo e operação sem requisito.

## 6. NLB

NLB opera por conexão/fluxo em L4 e atende cargas TCP/UDP/TLS de altíssimo desempenho. Pode expor IP por AZ e Elastic IP em load balancer internet-facing. Health checks podem ser TCP, HTTP ou HTTPS conforme target group.

TLS pode terminar no NLB com certificado, ou passar TCP criptografado ao target quando a terminação precisa ocorrer no backend. Targets IP permitem integração com endereços privados compatíveis, inclusive fora da VPC por conectividade privada e regras documentadas.

### Cenário resolvido 2 — allowlist e protocolo proprietário

Um parceiro envia TCP na porta 9000 e exige IPs públicos estáticos. **Decisão:** internet-facing NLB com EIP por subnet/AZ habilitada, listener TCP:9000 e target group apropriado. ALB não atende protocolo arbitrário; GWLB é para inserir appliances no caminho.

## 7. GWLB

GWLB combina gateway transparente e distribuição de appliances virtuais. Ele opera na camada de rede e troca tráfego com appliances por GENEVE porta 6081. GWLB endpoints, route tables e simetria de fluxo são parte do desenho.

Use para firewall, IDS/IPS ou deep packet inspection em escala. Não use como substituto de ALB para URLs nem como NLB genérico para publicar um servidor.

## 8. Health checks, deregistration e stickiness

- health check do load balancer é diferente do health check interno da aplicação; escolha um endpoint barato e representativo;
- thresholds evitam oscilação; intervalos menores detectam antes, mas geram mais carga;
- **deregistration delay** permite que requests/conexões em andamento terminem ao remover target;
- sticky session prende temporariamente um cliente ao target e pode usar cookie do load balancer ou aplicação no ALB;
- stickiness é útil para legado, mas cria desequilíbrio e não substitui estado externo. Prefira sessão em DynamoDB, ElastiCache ou outro store apropriado quando possível.

## 9. Cross-zone sem memorização antiga

Com cross-zone, cada nó distribui para targets nas AZs habilitadas; sem ele, distribui apenas aos targets de sua AZ.

- **ALB:** ligado no nível do load balancer; no target group pode ser explicitamente desligado. Stickiness de target não é suportada quando cross-zone está desligado.
- **NLB e GWLB:** desligado por padrão; pode ser habilitado.
- Avalie distribuição desigual, isolamento zonal e possíveis cobranças de processamento/transferência conforme serviço e fluxo; consulte preço atual.

Exemplo: dois targets na AZ A e oito na B, com metade do tráfego chegando a cada nó. Com cross-zone, cada target tende a 10%; sem ele, os dois da A recebem cerca de 25% cada e os oito da B, 6,25% cada.

## 10. Fluxo de diagnóstico

Quando um target não recebe tráfego, percorra o caminho em ordem:

```text
DNS resolve?
  → listener aceita protocolo/porta?
    → regra seleciona o target group esperado?
      → target está registrado e na AZ habilitada?
        → health check alcança porta/path e recebe success code?
          → SG/NACL/rotas permitem ida e retorno?
            → aplicação está ouvindo na interface correta?
```

Não comece recriando a instância. A propriedade `running` só confirma o estado
de compute; não confirma listener da aplicação, dependências ou resposta do
health check.

## 11. Mais cenários resolvidos

### Cenário resolvido 3 — sessão de aplicação legada

Um portal guarda sessão em memória e precisa de mudança mínima imediata.
Habilite stickiness no target group como ponte de migração, com duração curta e
monitoramento de desequilíbrio. Planeje mover a sessão para um store externo.
Somente stickiness não recupera a sessão quando o target falha.

### Cenário resolvido 4 — targets desiguais por AZ

Há dois targets na AZ A e oito na B. Se o objetivo é carga uniforme por target,
habilite ou mantenha cross-zone conforme o tipo e nível suportado. Se o objetivo
for isolamento zonal, desabilitar pode ser consciente, mas cada zona precisa de
capacidade proporcional ao tráfego que recebe.

## 12. Comparações que eliminam distratores

| Frase da questão | Recurso correto | Distrator comum |
|---|---|---|
| vários paths/hosts | ALB | NLB por ser “mais rápido” |
| UDP ou TCP arbitrário | NLB | ALB com regra de path |
| firewall transparente | GWLB | NLB publicando o firewall |
| endpoint saudável | health check/TG | EC2 apenas `running` |
| terminar conexões com segurança | deregistration delay | sticky session |
| preservar estado do usuário | store externo; stickiness como compatibilidade | cross-zone |

## 13. Segurança por camada

- internet-facing ou internal define exposição do load balancer;
- SG do load balancer limita clientes e portas;
- SG do target deve referenciar o SG do ALB quando aplicável, evitando abrir a
  aplicação à internet;
- TLS protege transporte, mas certificados e policies serão aprofundados no
  B07;
- AWS WAF integra-se ao ALB para regras L7, não substitui SG/NACL;
- access logs e métricas ajudam auditoria, com storage/custo associados;
- GWLB exige confiança no appliance e desenho de rotas simétricas.

## 14. Custos e armadilhas

Load balancers cobram tempo e unidades/capacidade processada conforme tipo; também podem existir IPv4 público, transferência, certificados importados ou appliances licenciados. Um load balancer vazio continua cobrando. No laboratório, não crie recursos.

Armadilhas:

- Route 53 multivalue não é substituto completo de ELB;
- healthy no EC2 não significa healthy no target group;
- SG do ALB deve alcançar SG dos targets na porta do serviço/health check;
- NACL é stateless e precisa do retorno;
- stickiness não replica sessão;
- GWLB endpoint e GWLB são componentes diferentes;
- zonal health e cross-zone são decisões distintas.

## 15. Checklist e recuperação ativa

- [ ] Escolho ALB/NLB/GWLB por requisito, não por slogan.
- [ ] Desenho listener → rule → target group → health check.
- [ ] Sei onde procurar o IP original no ALB.
- [ ] Explico deregistration delay e stickiness.
- [ ] Conheço os defaults atuais de cross-zone.

Sem consulta: escolha o balanceador para gRPC com paths, UDP de baixa latência, firewall transparente e TCP com EIP. Depois explique o caminho de um target unhealthy.

Perguntas finais:

1. Por que um NLB não substitui o ALB em roteamento por path?
2. Onde um appliance recebe e devolve tráfego no desenho GWLB?
3. Por que um target pode estar `running` e `unhealthy`?
4. Quando a afinidade prejudica distribuição?
5. O que muda na matemática 2/8 ao desligar cross-zone?
6. Que recurso independente precisa ser auditado após excluir um NLB?

## 16. Ligações e referências oficiais

- [LAB B06](../../05_Laboratorios/LAB_B06_Projeto_ALB_NLB_GWLB_Multi_AZ.md)
- [Questões B06](../../04_Questoes_e_Revisoes/Blocos/B06_Questoes.md)
- [Gabarito B06](../../04_Questoes_e_Revisoes/Blocos/B06_Gabarito.md)
- [Checklist B06](../../06_Progresso/B06_Checklist_e_Revisoes.md)
- [B07 — TLS e Auto Scaling](B07_TLS_ACM_Deregistration_e_Auto_Scaling.md)
- [How Elastic Load Balancing works](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html)
- [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
- [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
- [Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html)
- [ALB target-group attributes](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html)
