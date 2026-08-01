# LAB B18 — Arquitetura serverless e matriz de bancos

**Timebox:** 25 minutos<br>
**Modo:** diagrama e tabela; Athena opcional somente após conferir preço<br>
**Custo esperado:** zero no modo principal<br>
**Objetivo:** escolher stores/analytics por access pattern sem criar clusters<br>
**Capítulo:** [B18 — Bancos e analytics](../03_Guia_do_Estudante/Capitulos/B18_Arquiteturas_Serverless_Bancos_e_Analytics.md)

## 1. Restrições

Não crie RDS/Aurora, ElastiCache, DocumentDB, Neptune, Keyspaces, Timestream,
Redshift, OpenSearch ou EMR. Não crie NAT Gateway. O custo/hora e o cleanup não
cabem no timebox.

Athena real é opcional: use somente um arquivo fictício minúsculo, workgroup com
limite e bucket de resultados descartável. O objetivo é modelagem, não query.

## 2. Preflight — 3 min

- [ ] Identidade não root confirmada se abrir o console.
- [ ] Region e página de preços conferidas.
- [ ] Inventário inicial de clusters/domains/workgroups registrado read-only.
- [ ] Nenhum dado real, account ID ou endpoint será salvo.
- [ ] Budget/alerta permanece ativo.

```text
Clusters/domains criados antes: ______
Athena workgroups de laboratório antes: ______
Buckets de query result antes: ______
```

## 3. Requisitos — 3 min

Uma loja global que é **nova cliente AWS em 2026** precisa:

- usuários mobile e web;
- assets e downloads globais;
- pedidos com transações/joins;
- carrinho key-value de escala imprevisível;
- catálogo lido repetidamente;
- recomendação por relações usuário-produto;
- telemetry IoT por timestamp;
- pesquisa textual de produtos;
- SQL ad hoc em cinco anos de logs no S3;
- BI com joins repetitivos;
- Spark customizado mensal.

## 4. Diagrama serverless — 5 min

Complete os serviços:

```text
viewer -> __________ -> S3 privado (assets)
       -> __________ -> Lambda -> __________ (carrinho)
auth  -> __________
orders -> __________/Aurora
events -> SQS/EventBridge -> consumers
```

Marque:

- authorization e encryption;
- retries/idempotência;
- cache e source of truth;
- Multi-AZ/backup;
- logs e tracing;
- cada recurso com custo ocioso.

## 5. Matriz de bancos — 7 min

Preencha sem consultar; depois confira o capítulo:

| Access pattern | Modelo | Serviço | HA/escala | Custo dominante |
|---|---|---|---|---|
| pedido com joins/ACID |  |  |  |  |
| carrinho por customer ID |  |  |  |  |
| cache do catálogo |  |  |  |  |
| assets/data lake |  |  |  |  |
| documento JSON |  |  |  |  |
| graph recommendation |  |  |  |  |
| Cassandra workload |  |  |  |  |
| telemetry por tempo |  |  |  |  |

Na linha de telemetry, não escreva apenas “Timestream”. Para este novo cliente,
avalie Timestream for InfluxDB e registre que Timestream for LiveAnalytics não
aceita novos clientes desde 20/06/2025.

Para o relacional, escreva separadamente:

```text
Multi-AZ resolve: ____________________
Read replica resolve: _______________
RDS Proxy resolve: __________________
```

## 6. Matriz de analytics — 4 min

| Requisito | Athena | Redshift | OpenSearch | EMR | Escolha |
|---|---|---|---|---|---|
| SQL ad hoc em Parquet S3 |  |  |  |  |  |
| warehouse e BI repetitivo |  |  |  |  |  |
| full-text/log search |  |  |  |  |  |
| Spark customizado |  |  |  |  |  |

Para Athena, estime bytes examinados antes/depois de Parquet, compression e
partition pruning. Não multiplique tamanho total do bucket quando a query lê
somente partitions selecionadas.

## 7. Testes de mudança — 2 min

Troque um requisito por vez:

1. relatório ad hoc vira dashboard constante com joins → __________
2. consulta por ID vira graph traversal de seis saltos → __________
3. cache precisa ser system of record durável → rever __________
4. database tem HA, mas precisa escalar leitura → adicionar __________
5. mobile precisa AWS credentials temporárias → __________

## 8. Segurança/custo — 1 min

- [ ] stores privados e least privilege;
- [ ] secrets fora do código;
- [ ] PITR/backups e restore testados;
- [ ] Athena workgroup/scan limits;
- [ ] clusters e replicas identificados como custo contínuo;
- [ ] cross-AZ/Region e logs lembrados.

## 9. Cleanup e validação — 3 min

Modo principal: inventário final deve ser idêntico ao inicial.

Se executou Athena opcional:

1. delete table/database de catálogo criada;
2. delete query results e versões no S3;
3. delete bucket descartável;
4. delete workgroup se exclusivo;
5. confirme zero arquivo e zero query agendada.

```text
Clusters/domains novos: zero / investigar
Objetos de query: zero / investigar
Workgroups novos: zero / investigar
Inventário final igual: sim / não
```

## Resultado esperado

Um diagrama serverless, oito escolhas de store e quatro escolhas de analytics,
todas justificadas por modelo/access pattern, com zero cluster provisionado.

## Conexão com o exame

Traduza: *joins/transactions* → RDS/Aurora; *key-value at scale* → DynamoDB;
*cache* → ElastiCache; *graph* → Neptune; *ad hoc SQL on S3* → Athena;
*warehouse* → Redshift; *search* → OpenSearch; *Spark* → EMR.

## Referências oficiais

- [Choosing a database](https://docs.aws.amazon.com/databases-on-aws-how-to-choose/)
- [When to use Athena](https://docs.aws.amazon.com/athena/latest/ug/when-should-i-use-ate.html)
- [Athena cost optimization](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html)
- [Timestream for LiveAnalytics availability change](https://docs.aws.amazon.com/timestream/latest/developerguide/AmazonTimestreamForLiveAnalytics-availability-change.html)
