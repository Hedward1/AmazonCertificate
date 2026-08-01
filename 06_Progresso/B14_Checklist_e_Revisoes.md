# B14 — Checklist e revisões D+2/D+7

**Estudo inicial:** 10/08/2026<br>
**D+2:** 12/08/2026<br>
**D+7:** 17/08/2026<br>
**Conteúdo:** SQS Standard/FIFO, visibility, long polling, DLQ, SNS e fan-out

## 1. Conclusão inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b14) | concluir 182–190; quiz fica no B15 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B14_SQS_SNS_Desacoplamento_e_Fanout.md) | explicar decisões sem consulta | [ ] |
| [Laboratório](../05_Laboratorios/LAB_B14_SQS_SNS_Fanout_e_DLQ.md) | fan-out, redelivery, DLQ e cleanup | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B14_Questoes.md) | responder 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B14_Gabarito.md) | justificar A–D | [ ] |
| Correção | justificar A–D | [ ] |
| Caderno de Erros | registrar erros e baixa confiança | [ ] |

### Resultado inicial

- **Questões:** ____ / 10
- **Confiança baixa:** ____
- **Tempo:** ____ min
- **Fan-out observado:** sim / não / diagrama
- **DLQ observada:** sim / não / diagrama
- **Recursos residuais:** zero / investigar
- **Regra mais fraca:**

### Evidência do LAB

- [ ] duas filas receberam cópias independentes;
- [ ] receive foi diferenciado de delete;
- [ ] visibility e redelivery foram observados;
- [ ] `ApproximateReceiveCount` foi interpretado;
- [ ] DLQ e redrive foram explicados;
- [ ] chave idempotente foi definida;
- [ ] backlog por worker foi calculado;
- [ ] topic, subscriptions e filas foram excluídos.

## 2. D+2 — 12/08/2026

Sem consultar, em até 10 minutos:

1. Compare SQS Standard, FIFO e SNS.
2. Desenhe receive → visibility → delete → redelivery.
3. Diferencie delay, visibility, retention e receive wait time.
4. Explique idempotência com um exemplo de cobrança.
5. Desenhe SNS com três filas e suas policies.
6. Escolha métricas para Auto Scaling de workers.

| Item | Correto? | Confiança | Correção |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

- **Resultado:** ____ / 6
- **Erros reabertos:**

## 3. D+7 — 17/08/2026

### Cenário

Pedidos chegam em picos. Billing, analytics e audit precisam de cada evento.
Billing demora até seis minutos; algumas mensagens falham sempre. Eventos do
mesmo cliente precisam de ordem, mas clientes distintos podem executar juntos.

Responda:

1. Como fazer fan-out durável para os três sistemas?
2. Que fila e message group atendem à ordem?
3. Por que ainda é preciso idempotência?
4. Como configurar visibility para billing?
5. Onde colocar poison messages e como observá-las?
6. Qual policy limita cada fila ao tópico esperado?
7. Que métricas comandam scaling?
8. Quais recursos devem ser removidos?

- **Corretos:** ____ / 8
- **Tempo:** ____ min
- **Confiança:** alta / média / baixa
- **Próxima ação:**

## 4. Critério de encerramento

- questões ≥ 8/10;
- D+2 ≥ 5/6 e D+7 ≥ 7/8;
- Standard/FIFO/SNS escolhidos por requisito;
- idempotência, visibility e DLQ explicados sem consulta;
- fan-out não confundido com competing consumers;
- inventário AWS sem recursos B14.
