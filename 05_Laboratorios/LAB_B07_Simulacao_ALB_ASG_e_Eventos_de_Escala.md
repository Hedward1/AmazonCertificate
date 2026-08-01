# LAB B07 — Simulação ALB + ASG e eventos de escala

**Tempo:** 30 min · **Aulas:** 80–86 · **Modo:** diagrama/read-only · **Custo:** USD 0,00<br>
**Capítulo:** [B07](../03_Guia_do_Estudante/Capitulos/B07_TLS_ACM_Deregistration_e_Auto_Scaling.md)

## 1. Resultado esperado

Ao terminar, você deverá ter:

- arquitetura ALB + ASG em duas AZs;
- listener HTTPS associado conceitualmente ao ACM;
- launch template versionado;
- tabela min/desired/max para cinco eventos;
- decisões sobre warmup, grace period e deregistration;
- plano de instance refresh e rollback;
- inventário inicial e final idêntico.

## 2. Conexão com o exame

| Decisão | Tarefa |
|---|---|
| compute elástico | 3.2 |
| load balancing/TLS | 3.4 |
| falha e substituição | 2.2 |
| capacidade versus custo | 4.2 |

## 3. Preflight (3 min)

Confirme identidade não root, Region e inventário de ALB/ASG/launch templates. Não crie nem altere recursos. Consulte [preços do ELB](https://aws.amazon.com/elasticloadbalancing/pricing/) e [EC2](https://aws.amazon.com/ec2/pricing/) para reconhecer por que o exercício é simulado.

## 4. Arquitetura (7 min)

Desenhe ALB HTTPS com certificado ACM, duas subnets/AZs, target group HTTP:80 e ASG com `min=2`, `desired=2`, `max=8`, launch template versionado e default warmup de 300 s. SG do target aceita 80 somente do SG do ALB. Estado de sessão fica fora das instâncias.

## 5. Simulações (15 min)

Preencha capacidade e ações:

1. **CPU sobe imprevisivelmente:** target tracking 50%; duas instâncias em warmup; explique por que não devem induzir scale-in.
2. **Pico conhecido às 09:00:** scheduled action às 08:50 eleva min/desired para 4; target tracking continua ativo.
3. **Deploy:** nova versão do template, instance refresh; target entra draining por 120 s antes de terminar.
4. **Uma AZ falha:** ALB usa targets saudáveis da outra AZ; ASG tenta restaurar capacidade conforme subnets/quota.
5. **Aplicação responde 500 em `/health`:** ELB marca target unhealthy; com ELB health check no ASG, ocorre substituição após grace period/configuração.

### Tabela de evidência

| Evento | Antes | Ação | Durante warmup/draining | Depois |
|---|---:|---|---|---:|
| CPU alta | 2 | | | |
| pico agendado | 2 | | | |
| deploy | 4 | | | |
| falha de AZ | 4 | | | |
| health 500 | 2 | | | |

### Cartão do certificado

- hostname: `app.example.test`;
- Region: a mesma do ALB;
- validação: DNS conceitual;
- listener: HTTPS 443;
- policy TLS: versão atual aprovada;
- backend: HTTP ou HTTPS, com justificativa;
- renovação: condições que precisam permanecer válidas.

### Teste de limites

1. Tente propor `desired=10` com `max=8`: explique a rejeição/limitação.
2. Faça scale-in até 1 com `min=2`: explique por que o grupo restaura o piso.
3. Faça o boot durar 8 min com warmup 1 min: descreva a métrica enganosa.
4. Faça shutdown imediato com draining 120 s: identifique o conflito.
5. Mude o template sem refresh: diga quais instâncias usam a nova versão.

No walkthrough do console, localize campos de listener/certificate, min/desired/max, health check, warmup e policies; cancele todas as telas.

## 6. Validação e cleanup (5 min)

- [ ] cada evento mostra desired antes/depois e limite max;
- [ ] warmup, health-check grace period e deregistration não foram confundidos;
- [ ] certificado está na mesma Region do ALB;
- [ ] nenhum recurso foi criado; inventário final = inicial.

Se algo foi criado acidentalmente, pare; identifique somente tags B07 e dependências. Remova ASG antes do launch template, depois ALB/listeners/TGs e certificados de teste somente se não usados. Audite EC2, EBS, EIP e CloudWatch. Nunca exclua recurso sem ownership confirmado.

## 7. Solução de problemas

| Sintoma | Hipótese a validar |
|---|---|
| escala repetida durante boot | warmup curto ou métrica inadequada |
| instância boa é substituída | health path/grace period |
| request interrompido no deploy | shutdown antes do deregistration delay |
| certificado warning | hostname, cadeia, listener ou validação |
| AMI nova não aparece | template mudou sem instance refresh |
| custo após desired=0 | ALB, EBS, EIP ou métrica continuam |

## 8. Referências oficiais

- [ASG concepts](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)
- [Target tracking](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)
- [Instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html)
- [ASG health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html)
- [ACM managed renewal](https://docs.aws.amazon.com/acm/latest/userguide/managed-renewal.html)
