# B18 — Gabarito comentado

Abra após responder às [questões B18](B18_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B18-01 | A | 3.3 |
| B18-02 | B | 3.5 |
| B18-03 | C | 3.3 |
| B18-04 | A | 3.3 |
| B18-05 | D | 3.3 |
| B18-06 | B | 4.3 |
| B18-07 | C | 3.5 |
| B18-08 | A | 3.5 |
| B18-09 | B | 3.5 |
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

## B18-04 — Answer A

- **Central requirement:** efficiently traverse a highly connected fraud network.
- **Decisive words:** *relationships*, *traverse*, *accounts/devices/IPs*.
- **A:** correct; Neptune is purpose-built for graph traversal.
- **B:** Keyspaces is a Cassandra-compatible wide-column database.
- **C:** Timestream is time series.
- **D:** Memcached is an in-memory cache.
- **Reusable rule:** relationship traversal/path queries → Neptune.
- **Lessons:** 237.
- **Reference:** [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html).
- **Common trap:** choosing a document store because nodes can be encoded as JSON.

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

## B18-07 — Answer C

- **Central requirement:** managed warehouse for repeated OLAP and BI joins.
- **Decisive words:** *data warehouse*, *OLAP*, *BI*.
- **A:** DAX caches DynamoDB reads.
- **B:** Object Lock enforces object retention.
- **C:** correct; Redshift is the AWS data warehouse service.
- **D:** Identity Pools broker AWS credentials.
- **Reusable rule:** structured warehouse analytics/BI → Redshift.
- **Lessons:** 242.
- **Reference:** [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html).
- **Common trap:** using Redshift as the transactional order database.

## B18-08 — Answer A

- **Central requirement:** full-text search, relevance, and log analytics.
- **Decisive words:** *full-text*, *relevance scoring*, *indexed*.
- **A:** correct; OpenSearch is designed for search and log analytics.
- **B:** EBS is block storage.
- **C:** Storage Gateway exposes hybrid storage interfaces.
- **D:** RDS events are operational notifications.
- **Reusable rule:** full-text/indexed search → OpenSearch Service.
- **Lessons:** 243.
- **Reference:** [OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html).
- **Common trap:** treating a search index as the source of truth for transactions.

## B18-09 — Answer B

- **Central requirement:** execute custom Apache Spark on a large data lake.
- **Decisive words:** *custom Spark jobs*, *large data lake*.
- **A:** SNS is pub/sub notification.
- **B:** correct; EMR runs managed big-data frameworks including Spark.
- **C:** Cognito handles identities.
- **D:** Global Accelerator routes network traffic.
- **Reusable rule:** Hadoop/Spark/custom distributed framework → EMR.
- **Lessons:** 244.
- **Reference:** [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html).
- **Common trap:** choosing EMR for one simple ad hoc SQL query.

## B18-10 — Answer C

- **Central requirement:** distribute immutable binaries globally without Lambda proxying bytes.
- **Decisive words:** *large*, *worldwide*, *reduce compute/origin load*.
- **A:** longer Lambda execution wastes compute and does not create a CDN.
- **B:** cache alone is not durable global object delivery.
- **C:** correct; S3 stores versioned objects and CloudFront caches via a private OAC origin.
- **D:** SQS is not for large binary distribution.
- **Reusable rule:** static/download content → object storage + CDN, not application compute.
- **Lessons:** 226–229.
- **Reference:** [CloudFront with S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html).
- **Common trap:** routing static bytes through Lambda/API Gateway.

## Ação após a correção

Registre erro ou baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), nomeando o modelo de dados ou tipo de análise que decidiu a resposta.
