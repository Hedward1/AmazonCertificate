# LAB B06 — Projeto ALB, NLB e GWLB Multi-AZ

**Tempo:** 50 minutos<br>
**Aulas:** 72–79<br>
**Capítulo:** [B06](../03_Guia_do_Estudante/Capitulos/B06_ALB_NLB_GWLB_Target_Groups_e_Cross_Zone.md)<br>
**Modo:** console read-only + diagrama; **não criar load balancer**<br>
**Custo esperado:** USD 0,00 causado pelo laboratório

## 1. Resultado esperado

Ao terminar, você deverá ter três diagramas comparáveis, uma ficha de listener e
target group para o ALB, uma ficha de conectividade para o NLB e uma tabela de
rotas conceitual para o GWLB. O inventário da conta deve permanecer inalterado.

Evidências:

- escolha do balanceador justificada pelo protocolo;
- duas AZs e targets saudáveis no desenho;
- tráfego do cliente separado do tráfego ao target;
- health check, SG e retorno representados;
- decisão explícita sobre stickiness e cross-zone;
- zero recurso criado.

## 2. Conexão com o exame

| Elemento | Tarefa |
|---|---|
| protocolo e load balancer | 3.4 |
| falha de target/AZ | 2.2 |
| distribuição e elasticidade | 3.2 |
| consolidação/capacidade | 4.2 |

## 3. Preflight (5 min)

- confirme identidade não root, Region e inventário de ELB/target groups;
- não altere recursos existentes;
- consulte [preços do ELB](https://aws.amazon.com/elasticloadbalancing/pricing/) e identifique cobrança por hora e capacidade;
- se houver recurso preexistente, use somente metadados não sensíveis e não copie DNS, ARN, account ID ou IP.

## 4. Desafio (30 min)

Desenhe uma aplicação em duas AZs:

```text
Internet → ALB HTTPS
             ├─ host api.example.test + /v1/* → TG-api → EC2 AZ-a/AZ-b
             └─ /static/*                    → TG-static → EC2 AZ-a/AZ-b

Partner TCP:9000 → NLB + IP estático por AZ → TG-tcp

VPC workload → GWLB endpoint → GWLB → firewall AZ-a/AZ-b → retorno simétrico
```

Para o ALB, preencha:

1. duas subnets públicas, SG aceitando 443 do cliente;
2. listener 443, certificado fictício, redirect opcional 80→443;
3. duas regras e prioridades sem colisão;
4. target types, portas e health paths `/health`;
5. SG dos targets aceitando somente do SG do ALB;
6. deregistration delay e decisão fundamentada sobre stickiness;
7. efeito de um target unhealthy em uma AZ.

Para NLB, indique protocolo, EIP por AZ, target type, preservação de source IP a validar e health check. Para GWLB, desenhe endpoints, route tables, GENEVE 6081, appliances e caminho de ida/volta.

### Ficha de decisão

| Campo | ALB | NLB | GWLB |
|---|---|---|---|
| requisito central | | | |
| protocolo/camada | | | |
| listener | | | |
| target type | | | |
| health check | | | |
| source IP | | | |
| cross-zone | | | |
| principal custo | | | |
| risco operacional | | | |

### Testes de mesa

1. Remova o target da AZ A: para onde vai o tráfego?
2. Faça `/health` responder 500: qual componente muda de estado?
3. Desative cross-zone com frota 2/8: calcule a fração por target.
4. Faça um request durar mais que o deregistration delay: o que pode ocorrer?
5. Que rota deve mudar para inserir/remover o GWLB endpoint?

## 5. Walkthrough read-only (10 min)

No console, abra **EC2 → Load Balancers → Create** e avance sem concluir. Localize: scheme, IP address type, VPC/subnets, SG, listener e target group. Repita até a tela de NLB e GWLB. Cancele em todas. Confirme no inventário que nada surgiu.

## 6. Validação e cleanup (5 min)

- [ ] cada decisão tem requisito associado;
- [ ] ALB usa regras L7, NLB não;
- [ ] GWLB usa rota e endpoint, não URL pública;
- [ ] há targets em duas AZs;
- [ ] cross-zone default foi anotado por tipo;
- [ ] inventário inicial = final e nenhum recurso foi criado.

Cleanup é encerrar o walkthrough e a sessão. Não exclua recursos preexistentes. Se algo foi criado acidentalmente com tag B06, confirme o identificador e remova listener/load balancer, target groups e EIPs alocados exclusivamente para o exercício; audite a fatura.

## 7. Solução de problemas conceitual

| Sintoma | Próxima verificação |
|---|---|
| DNS responde, conexão recusa | listener e SG do load balancer |
| regra errada | prioridade e condições L7 |
| target unhealthy | path, porta, success code, SG e aplicação |
| IP original ausente no ALB | headers encaminhados e trusted proxies |
| appliance quebra o retorno | simetria das rotas/endpoints |
| uma AZ sobrecarrega | quantidade de targets e cross-zone |

## 8. Referências oficiais

- [How ELB works](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html)
- [ALB listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)
- [NLB listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html)
- [GWLB getting started](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started.html)
- [Target health](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html)
