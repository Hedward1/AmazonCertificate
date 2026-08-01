# B06 — Checklist e revisões D+2/D+7

**Inicial:** 31/07/2026<br>
**D+2 nominal:** 02/08/2026 — domingo, sem estudo<br>
**D+2 executado:** 03/08/2026 (atrasado conforme cronograma)<br>
**D+7:** 07/08/2026

## Estudo inicial

- [ ] assistir [aulas 72–79](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b06);
- [ ] concluir [capítulo](../03_Guia_do_Estudante/Capitulos/B06_ALB_NLB_GWLB_Target_Groups_e_Cross_Zone.md);
- [ ] entregar [LAB](../05_Laboratorios/LAB_B06_Projeto_ALB_NLB_GWLB_Multi_AZ.md) sem criar recursos;
- [ ] responder [10 questões](../04_Questoes_e_Revisoes/Blocos/B06_Questoes.md) antes do [gabarito](../04_Questoes_e_Revisoes/Blocos/B06_Gabarito.md);
- [ ] registrar erros e confirmar inventário inalterado.

**Resultado:** ____/10; confiança baixa ____; tempo ____; recurso criado: zero/____.

### Evidência mínima

- [ ] ALB com listener, duas regras e dois target groups;
- [ ] NLB com protocolo e IP por AZ justificados;
- [ ] GWLB com endpoint, rotas e GENEVE;
- [ ] health check representativo em cada ficha;
- [ ] SG de cliente/load balancer/target separado;
- [ ] source IP explicado por tipo;
- [ ] stickiness tratada como compatibilidade, não durabilidade;
- [ ] distribuição 2/8 calculada com/sem cross-zone;
- [ ] inventários inicial e final iguais;
- [ ] nenhuma tela de criação concluída.

## D+2 — 03/08/2026

Em 10 minutos, sem consulta: desenhe listener/rule/TG/health check; escolha ALB/NLB/GWLB em quatro cenários; explique source IP no ALB, stickiness, deregistration e cross-zone.<br>
**Resultado:** ____/7. **Ponto fraco:** ____________________.

| Item | Correto? | Confiança | Correção |
|---:|---|---|---|
| fluxo listener/TG | | | |
| ALB | | | |
| NLB | | | |
| GWLB | | | |
| source IP | | | |
| stickiness/draining | | | |
| cross-zone | | | |

## D+7 — 07/08/2026

Projete um endpoint web por host/path, um serviço UDP com IP fixo e uma camada de inspeção. Para cada um, escolha balanceador, health check, duas AZs, SG/rotas, cross-zone e cleanup.<br>
**Resultado:** ____/8. **Tempo:** ____ min.

Registre no D+7:

- política/camada escolhida para cada endpoint;
- caminho do health check;
- comportamento durante falha de AZ;
- custo que continuaria mesmo sem tráfego;
- palavra em inglês que atrasou a decisão;
- regra enviada ao Caderno de Erros.

## Critério de encerramento

- [ ] autorais ≥ 8/10; D+2 ≥ 6/7; D+7 ≥ 7/8;
- [ ] nenhuma troca entre L7, L4 e appliance;
- [ ] defaults atuais de cross-zone recuperados sem consulta;
- [ ] zero recurso B06.

### Autoexplicação final

- [ ] consigo explicar ALB em 60 segundos;
- [ ] consigo explicar NLB em 60 segundos;
- [ ] consigo explicar GWLB em 60 segundos;
- [ ] desenho health check sem consultar;
- [ ] calculo distribuição cross-zone sem decorar exemplo;
- [ ] reconheço custo de recurso ocioso.

Se falhar, revise somente o tipo de balanceador ou atributo que causou o erro e
refaça o cenário depois de 24 horas. Não crie um ELB pago para corrigir uma
lacuna de vocabulário.
