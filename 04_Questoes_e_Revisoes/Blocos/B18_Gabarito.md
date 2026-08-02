# B18 — Gabarito comentado

Abra após responder às [questões B18](B18_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B18-01 | A | 3.3 |
| B18-02 | B | 3.5 |
| B18-03 | C | 3.3 |
| B18-04 | B,D | 3.3 |
| B18-05 | D | 3.3 |
| B18-06 | B | 4.3 |
| B18-07 | A,C | 3.5 |
| B18-08 | A | 3.5 |
| B18-09 | A,C,E | 3.5 |
| B18-10 | C | 2.1 |

## B18-01 — Resposta A

- **Requisito central:** engine relacional com joins, constraints e transações SQL.
- **Palavras decisivas:** *joins*, *foreign keys*, *transações complexas*.
- **A:** correta; RDS/Aurora são serviços relacionais gerenciados.
- **B:** Neptune é graph database.
- **C:** Glacier Deep Archive é armazenamento de objetos arquivados.
- **D:** OpenSearch fornece busca/indexação, não integridade relacional.
- **Regra reutilizável:** SQL OLTP com joins/ACID → RDS ou Aurora.
- **Aulas:** 230–232.
- **Referência:** [Choosing a database](https://docs.aws.amazon.com/databases-on-aws-how-to-choose/).
- **Erro comum:** escolher NoSQL apenas porque o workload pode crescer.

## B18-02 — Resposta B

- **Requisito central:** SQL ad hoc em Parquet S3 sem cluster.
- **Palavras decisivas:** *esporádicas*, *S3*, *sem manter cluster*.
- **A:** RDS exigiria carga/movimentação e capacidade de banco.
- **B:** correta; Athena consulta o S3 de forma serverless.
- **C:** Amazon MQ é broker.
- **D:** ECS exige código e compute gerenciado pelo cliente.
- **Regra reutilizável:** ad hoc SQL diretamente no S3 → Athena.
- **Aulas:** 240–241.
- **Referência:** [When to use Athena](https://docs.aws.amazon.com/athena/latest/ug/when-should-i-use-ate.html).
- **Erro comum:** escolher Redshift para poucas queries esporádicas no lake.

## B18-03 — Answer C

- **Central requirement:** add read scaling while retaining high availability.
- **Decisive words:** *also offload*, *growing read workload*.
- **A:** a traditional standby primarily supports failover and is not the read target.
- **B:** DNS TTL does not create read capacity.
- **C:** correct; suitable read replicas/readers scale reads alongside the HA design.
- **D:** instance store is ephemeral and not a managed read replica.
- **Reusable rule:** Multi-AZ for HA; read replicas/readers for read scaling.
- **Lessons:** 231–232.
- **Reference:** [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).
- **Common trap:** assuming every standby can serve application reads.

## B18-04 — Answer B,D

- **Central requirement:** use purpose-built stores for graph traversal and relational ACID transactions.
- **Decisive words:** *graph traversals*, *relationships*, *relational constraints*, *ACID SQL*.
- **A:** incorrect; a cache is not the durable system of record for either requirement.
- **B:** correct; Neptune is purpose-built for graph relationships and traversals.
- **C:** incorrect; DocumentDB does not provide relational foreign-key semantics.
- **D:** correct; Aurora provides relational SQL transactions and constraints.
- **E:** incorrect; OpenSearch is a search/analytics engine, not an account-balance ledger.
- **Reusable rule:** polyglot persistence chooses the database model from each dominant access pattern and consistency requirement.
- **Lessons:** 230–239.
- **Reference:** [AWS purpose-built databases](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html).

## B18-05 — Answer D

- **Central requirement:** store/query telemetry organized by time.
- **Decisive words:** *new AWS customer*, *timestamp*, *time-window*, *retention*.
- **A:** DocumentDB stores JSON-like documents.
- **B:** LiveAnalytics is purpose-built, but it has not accepted new customers since June 20, 2025.
- **C:** Neptune handles graph relationships.
- **D:** correct; Timestream for InfluxDB is the current Timestream option a new customer should evaluate.
- **Reusable rule:** IoT/metrics with time-window analytics → time-series engine; for a new account, validate availability before selecting the historical LiveAnalytics answer.
- **Lessons:** 239.
- **Reference:** [Timestream for LiveAnalytics availability change](https://docs.aws.amazon.com/timestream/latest/developerguide/AmazonTimestreamForLiveAnalytics-availability-change.html).
- **Common trap:** applying the historical LiveAnalytics answer to a new customer without checking availability.

## B18-06 — Answer B

- **Central requirement:** reduce Athena bytes scanned and query cost.
- **Decisive words:** *years of CSV*, *bytes scanned*.
- **A:** usage plans govern APIs, not lake scans.
- **B:** correct; columnar compressed data plus partition pruning reads less.
- **C:** Lambda memory is unrelated to Athena scan size.
- **D:** SQS ordering is unrelated.
- **Reusable rule:** Athena optimization → columnar, compressed, partitioned, selective queries.
- **Lessons:** 240–241.
- **Reference:** [Optimize Athena data](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html).
- **Common trap:** partitioning by a field never used in predicates.

## B18-07 — Answer A,C

- **Central requirement:** serve repeated warehouse OLAP and occasional serverless S3 SQL without idle clusters.
- **Decisive words:** *repeated OLAP joins*, *raw Parquet*, *ad hoc*, *no permanently provisioned cluster*.
- **A:** correct; Redshift Serverless provides managed warehouse capacity for repeated analytical workloads.
- **B:** incorrect; Route 53 does not execute or federate SQL.
- **C:** correct; Athena performs serverless SQL directly over S3 and charges by scanned data.
- **D:** incorrect; instance store is ephemeral and would add data movement and host operations.
- **E:** incorrect; SQS is messaging, not a BI semantic or SQL engine.
- **Reusable rule:** separate warehouse-shaped repeated analytics from occasional data-lake queries; serverless options can remove idle cluster management.
- **Lessons:** 240–242.
- **Reference:** [Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-whatis.html) and [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html).

## B18-08 — Answer A

- **Central requirement:** provide one scalable, low-latency managed indexed-search layer for products and logs without consuming transactional capacity or replacing the system of record.
- **Decisive words:** *high search traffic*, *must not consume database capacity*, *one managed indexed-search platform*, *predictable low latency*, *asynchronous indexing*.
- **A:** correct; OpenSearch supplies the required managed indexed-search layer for product relevance and log exploration, while pipelines populate its indexes and the transactional database remains authoritative.
- **B:** native database search plus Logs Insights separates the two query experiences and places customer search load on the transactional database, directly violating the unified-layer, capacity-isolation, and scale requirements.
- **C:** DynamoDB serves key-value/document access patterns, but scans/filter expressions do not supply typo-tolerant relevance search and would be inefficient.
- **D:** Athena is valuable for ad hoc SQL over S3, but per-request scans are not a low-latency relevance index for interactive search.
- **Reusable rule:** use a transactional store for correctness and a separately populated OpenSearch index for search-oriented access patterns.
- **Lessons:** 243.
- **Reference:** [OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html).
- **Common trap:** dual-writing without a replayable, monitored synchronization path between the source and the index.

## B18-09 — Answer A,C,E

- **Central requirement:** combine Spark processing, shared metadata, and centralized fine-grained lake governance.
- **Decisive words:** *Apache Spark*, *shared catalog*, *fine-grained permissions*, *across accounts*.
- **A:** correct; EMR options run managed Apache Spark workloads over S3.
- **B:** incorrect; Route 53 zones contain DNS records, not analytics table metadata.
- **C:** correct; Glue Data Catalog provides table and schema metadata used by analytics engines.
- **D:** incorrect; SES policies do not grant table, row, column, or lake access.
- **E:** correct; Lake Formation centrally governs supported data lake permissions and sharing.
- **F:** incorrect; EBS is block storage and is not a cross-account S3 data lake.
- **Reusable rule:** a governed analytics lake separates compute, catalog metadata, and authorization into purpose-built layers.
- **Lessons:** 240–244.
- **Reference:** [Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html).

## B18-10 — Answer C

- **Central requirement:** deliver large private/versioned objects globally with edge caching and optional viewer authorization, without proxy compute.
- **Decisive words:** *multi-gigabyte*, *horizontal/vertical compute scaling*, *private origin*, *time-limited*, *edge caching*.
- **A:** presigned S3 URLs remove Lambda and preserve time-limited origin access, but clients still fetch from the regional origin and repeated downloads do not benefit from CloudFront caching.
- **B:** CloudFront supplies edge caching, but a public website origin and absent viewer authorization violate the private-origin/customer-access controls.
- **C:** correct; S3 provides durable versioned objects, OAC keeps the origin private, CloudFront reduces latency/origin transfer, and signed access limits viewers.
- **D:** Global Accelerator improves network paths for supported endpoints but is not a content cache; retaining Lambda byte proxying leaves the compute scaling and cost problem.
- **Reusable rule:** choose component scaling strategies by bottleneck: static bytes scale through durable object storage and CDN caches, not horizontal concurrency or vertical memory in application compute.
- **Lessons:** 226–229.
- **Reference:** [CloudFront with S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html).
- **Common trap:** securing the S3 origin but leaving CloudFront viewer access unrestricted when the files are customer-specific.

## Ação após a correção

Registre erro ou baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), nomeando o modelo de dados ou tipo de análise que decidiu a resposta.
