# B15 — Checklist e revisões D+2/D+7

**Estudo inicial:** 11/08/2026<br>
**D+2:** 13/08/2026<br>
**D+7:** 18/08/2026<br>
**Conteúdo:** Kinesis, Data Firehose, Amazon MQ, containers e ECS

## 1. Conclusão inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b15) | 191–202 e Q14 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B15_Streaming_Amazon_MQ_e_ECS.md) | explicar tabela de decisão | [ ] |
| [LAB](../05_Laboratorios/LAB_B15_Streaming_e_Inspecao_ECS.md) | diagrama + inspeção read-only | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B15_Questoes.md) | 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B15_Gabarito.md) | justificar A–D | [ ] |
| Caderno de Erros | registrar erro/baixa confiança | [ ] |
| Auditoria | zero recursos criados | [ ] |

- **Q14:** ____%
- **Questões:** ____ / 10
- **Tempo:** ____ min
- **Maior confusão:**
- **Inventário final igual:** sim / não

### Evidência

- [ ] SQS/SNS/KDS/Firehose/MQ comparados;
- [ ] hot shard corrigido por partition key;
- [ ] replay e fan-out diferenciados;
- [ ] task definition interpretada;
- [ ] task role e execution role diferenciadas;
- [ ] Fargate e ECS on EC2 comparados;
- [ ] service scaling e capacity scaling separados;
- [ ] nenhum ARN/segredo salvo.

## 2. D+2 — 13/08/2026

Sem consulta:

1. Reconstrua a matriz dos cinco serviços.
2. Explique partition key, shard, order e hot shard.
3. Compare shared consumer e enhanced fan-out.
4. Compare KDS e Firehose por retention/replay/buffer.
5. Desenhe cluster → service → task → container.
6. Compare Fargate e EC2; task role e execution role.

| Item | Correto? | Confiança | Correção |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

**Resultado:** ____ / 6

## 3. D+7 — 18/08/2026

Uma empresa recebe transações para dois consumers com replay, entrega logs ao
S3, mantém uma integração JMS e executa APIs containerizadas sem querer
gerenciar hosts. Responda:

1. Serviço para transações e replay?
2. Como manter ordem por cliente e evitar hot shard?
3. Quando usar enhanced fan-out?
4. Serviço para logs no S3 sem consumer?
5. Serviço para JMS compatível?
6. Opção de compute dos containers?
7. Role do código e role de pull/logs?
8. Quais recursos/custos seriam removidos após uma PoC?

- **Corretos:** ____ / 8
- **Tempo:** ____ min
- **Confiança:** alta / média / baixa
- **Próxima ação:**

## 4. Critério de encerramento

- questões ≥ 8/10;
- D+2 ≥ 5/6 e D+7 ≥ 7/8;
- streaming escolhido por replay, consumers, protocolo e destino;
- componentes ECS e roles explicados sem consulta;
- nenhum recurso caro criado no LAB.
