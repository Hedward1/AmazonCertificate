# B07 — Checklist e revisões D+2/D+7

**Inicial:** 01/08/2026 · **D+2:** 03/08/2026 · **D+7:** 08/08/2026

## Inicial

- [ ] [aulas 80–86 e Q05](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b07);
- [ ] [capítulo](../03_Guia_do_Estudante/Capitulos/B07_TLS_ACM_Deregistration_e_Auto_Scaling.md);
- [ ] [LAB](../05_Laboratorios/LAB_B07_Simulacao_ALB_ASG_e_Eventos_de_Escala.md) com zero recursos;
- [ ] [questões](../04_Questoes_e_Revisoes/Blocos/B07_Questoes.md) antes do [gabarito](../04_Questoes_e_Revisoes/Blocos/B07_Gabarito.md);
- [ ] mini-simulado semanal B01–B07 e três lacunas no Caderno de Erros.

**Q05:** ____%; **autorais:** ____/10; **mini-simulado:** ____/____; **tempo:** ____; **lacunas:** ____________________.

### Evidência mínima

- [ ] listener HTTPS, hostname e Region do certificado registrados;
- [ ] duas AZs no ASG;
- [ ] min, desired e max coerentes;
- [ ] launch template versionado;
- [ ] target tracking e scheduled usados nos eventos corretos;
- [ ] default warmup ligado ao tempo de bootstrap;
- [ ] grace period separado do warmup;
- [ ] deregistration alinhado ao shutdown;
- [ ] plano de refresh e rollback;
- [ ] inventário final sem recursos B07.

## D+2 — 03/08/2026

Sem consulta: desenhe os dois trechos TLS; explique Region do certificado; compare warmup, grace period e deregistration; escolha target/step/scheduled/predictive para quatro frases; resolva min=2, desired=3, max=6 após scale-out +2.<br>
**Resultado:** ____/7.

| Item | Correto? | Confiança | Correção |
|---|---|---|---|
| dois trechos TLS | | | |
| Region/SAN | | | |
| três temporizadores | | | |
| target tracking | | | |
| step/scheduled/predictive | | | |
| limites ASG | | | |
| cleanup | | | |

## D+7 — 08/08/2026

Projete API stateless Multi-AZ com TLS, ALB e ASG para pico semanal previsível e variação imprevisível. Inclua métricas, valores min/desired/max, warmup, health check, deployment e custos residuais.<br>
**Resultado:** ____/8; **tempo:** ____.

### Registro D+7

- Métrica e target:
- Capacidade antes/depois:
- Tempo de bootstrap:
- Health check:
- Estratégia de deploy:
- Custo residual:
- Palavra decisiva:
- Erro enviado ao Caderno:

## Critério de encerramento

- [ ] ≥8/10, D+2 ≥6/7, D+7 ≥7/8;
- [ ] escolho políticas sem consulta;
- [ ] não confundo warmup com draining;
- [ ] estado externo e cleanup estão claros;
- [ ] zero recurso B07.

### Autoexplicação final

- [ ] explico a cadeia TLS sem consulta;
- [ ] calculo min/desired/max em três eventos;
- [ ] escolho métrica proporcional à capacidade;
- [ ] associo cada temporizador ao evento correto;
- [ ] descrevo refresh e rollback;
- [ ] encontro custos restantes após desired zero.

Se falhar, revise somente a política ou o temporizador que causou a decisão
errada. Repita o cenário em papel depois de 24 horas; não provisionar ALB/ASG é
parte do controle de custo deste bloco.
