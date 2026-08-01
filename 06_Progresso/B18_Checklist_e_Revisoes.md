# B18 — Checklist e revisões D+2/D+7

**Estudo inicial:** 14/08/2026<br>
**D+2:** 16/08/2026 cairia no domingo; revisão transferida para **17/08/2026**<br>
**D+7:** 21/08/2026<br>
**Conteúdo:** serverless architectures, bancos e analytics

## 1. Conclusão inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b18) | 226–244 e Q17–Q18 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B18_Arquiteturas_Serverless_Bancos_e_Analytics.md) | reconstruir matriz | [ ] |
| [LAB](../05_Laboratorios/LAB_B18_Arquitetura_Serverless_e_Matriz_de_Bancos.md) | diagrama e zero clusters | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B18_Questoes.md) | 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B18_Gabarito.md) | justificar A–D | [ ] |
| Caderno de Erros | registrar erro/baixa confiança | [ ] |

- **Q17:** ____% — **Q18:** ____%
- **Questões:** ____ / 10
- **Tempo:** ____ min
- **Clusters criados:** zero / investigar
- **Serviço mais confundido:**

### Evidência

- [ ] arquitetura mobile/web desenhada;
- [ ] RDS/Aurora/Multi-AZ/readers diferenciados;
- [ ] DynamoDB/ElastiCache/S3 comparados;
- [ ] quatro purpose-built databases reconhecidos;
- [ ] disponibilidade atual de Timestream for LiveAnalytics registrada;
- [ ] Athena/Redshift/OpenSearch/EMR comparados;
- [ ] custo por scan e formato colunar explicado;
- [ ] inventário final igual ao inicial.

## 2. D+2 transferido — 17/08/2026

1. Reconstrua a matriz de 12 stores/analytics.
2. Diferencie Multi-AZ e read replica.
3. Escolha bancos para document, graph, Cassandra e time series; no último,
   diferencie uma conta nova de um cliente elegível ao LiveAnalytics.
4. Compare Athena e Redshift.
5. Explique OpenSearch e EMR.
6. Desenhe website serverless seguro.

| Item | Correto? | Confiança | Correção |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

**Resultado:** ____ / 6

## 3. D+7 — 21/08/2026

Uma loja precisa pedidos relacionais, carrinho key-value, cache, recomendação em
graph, telemetry, pesquisa textual, SQL ad hoc no S3, BI warehouse e Spark.

1. Store para pedidos?
2. Store para carrinho e cache?
3. Stores para graph e telemetry de uma conta nova em 2026?
4. Serviço para search?
5. Serviço para ad hoc S3?
6. Serviço para warehouse?
7. Serviço para Spark?
8. Quais otimizações reduzem Athena scan?

- **Corretos:** ____ / 8
- **Tempo:** ____ min
- **Confiança:** alta / média / baixa
- **Próxima ação:**

## 4. Critério de encerramento

- questões ≥ 8/10;
- D+2 ≥ 5/6 e D+7 ≥ 7/8;
- store escolhido por modelo e access pattern;
- escolha time-series respeita a disponibilidade para novos clientes;
- OLTP/OLAP e quatro analytics diferenciados;
- zero cluster/recurso B18 residual.
