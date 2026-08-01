# B18 — Questões

**Formato:** questões de resposta única e múltipla, conforme indicado<br>
**Idioma:** 2 Português + 8 Inglês<br>
**Aulas:** 226–244<br>
**Tarefas:** 2.1, 3.3, 3.5 e 4.3

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma | Formato | Tipo | Dificuldade |
|---|---:|---:|---|---|---|---|---|
| B18-01 | 3 | 3.3 | 230–239 | Português | single | fundamental | básica |
| B18-02 | 3 | 3.5 | 240–244 | Português | single | situacional | intermediária |
| B18-03 | 3 | 3.3 | 231–234 | Inglês | single | situacional | intermediária |
| B18-04 | 3 | 3.3 | 237 | Inglês | multi-2 | integrada | avançada |
| B18-05 | 3 | 3.3 | 239 | Inglês | single | situacional | intermediária |
| B18-06 | 4 | 4.3 | 240–241 | Inglês | single | situacional | intermediária |
| B18-07 | 3 | 3.5 | 242 | Inglês | multi-2 | integrada | avançada |
| B18-08 | 3 | 3.5 | 243 | Inglês | single | integrada | avançada |
| B18-09 | 3 | 3.5 | 244 | Inglês | multi-3 | integrada | avançada |
| B18-10 | 2 | 2.1 | 226–229 | Inglês | single | integrada | avançada |

### B18-01

Um sistema de pedidos exige joins, foreign keys e transações SQL complexas.
Qual família de serviço é a escolha inicial adequada?

- A. Amazon RDS ou Amazon Aurora
- B. Amazon Neptune
- C. Amazon S3 Glacier Deep Archive
- D. Amazon OpenSearch Service

### B18-02

Analistas fazem consultas SQL esporádicas diretamente em arquivos Parquet no
S3 e não querem manter cluster. Qual serviço usar?

- A. Amazon RDS Multi-AZ
- B. Amazon Athena
- C. Amazon MQ
- D. Amazon ECS on EC2

### B18-03

A highly available RDS deployment must also offload a growing read workload.
Which design addresses the read-scaling requirement?

- A. Rely only on a traditional Multi-AZ standby
- B. Increase DNS TTL
- C. Add appropriate read replicas/readers while retaining the HA design
- D. Store query results in instance store only

### B18-04

A financial platform needs millisecond graph traversals across accounts, devices,
and IP addresses for fraud detection, while its order ledger requires relational
constraints and ACID SQL transactions. **Choose TWO.**

- A. Store both workloads in Amazon ElastiCache and implement durability in clients
- B. Use Amazon Neptune for relationship traversal
- C. Use Amazon DocumentDB for foreign-key enforcement
- D. Use Amazon Aurora for the transactional order ledger
- E. Use Amazon OpenSearch Service as the system of record for account balances

### B18-05

In 2026, a new AWS customer needs to store measurements indexed by timestamp,
run time-window queries, and manage retention. Which current option should the
customer evaluate first?

- A. Amazon DocumentDB
- B. Amazon Timestream for LiveAnalytics
- C. Amazon Neptune
- D. Amazon Timestream for InfluxDB

### B18-06

Athena query cost is too high because each query scans years of CSV data. Which
change most directly reduces bytes scanned?

- A. Add an API Gateway usage plan
- B. Convert to compressed columnar files and partition for query predicates
- C. Increase Lambda memory
- D. Create an SQS FIFO queue

### B18-07

Analysts run repeated OLAP joins over curated structured data and occasional ad
hoc SQL against raw Parquet in S3. The team wants managed scaling and no
permanently provisioned cluster for either access pattern. **Choose TWO.**

- A. Use Amazon Redshift Serverless for repeated warehouse queries
- B. Use Amazon Route 53 for SQL federation
- C. Use Amazon Athena for ad hoc queries over Parquet in S3
- D. Load every raw object into an EC2 instance store volume
- E. Use Amazon SQS as the BI semantic layer

### B18-08

An ecommerce platform keeps authoritative product and inventory records in a
transactional database. Customer search traffic is high enough that it must not
consume transactional database capacity, and both customers and operators need
predictable low-latency queries through one managed indexed-search platform:
typo-tolerant product relevance for customers and near-real-time log exploration
for operators. The team accepts asynchronous indexing but cannot make the search
layer the source of truth. Which architecture best fits?

- A. Use Amazon OpenSearch Service as the managed search layer with product and log indexes, feed it from the systems of record, and keep transactional writes in the database
- B. Use the transactional database's native full-text features for product search and CloudWatch Logs Insights for logs, accepting separate query models and database search load
- C. Copy products and logs into DynamoDB and use filter expressions plus scans for typo tolerance and relevance ranking
- D. Store periodic product exports and logs in S3 and query them with Athena for every interactive search request

### B18-09

Data engineers need custom Apache Spark processing over an S3 data lake, a shared
technical catalog for Athena and the Spark jobs, and centrally governed
fine-grained data permissions across analytics accounts. Which components meet
the requirements? **Select THREE.**

- A. Amazon EMR or EMR Serverless for the Spark workloads
- B. Amazon Route 53 private hosted zones as the table catalog
- C. AWS Glue Data Catalog for shared table metadata
- D. Amazon SES identity policies for column permissions
- E. AWS Lake Formation for centralized data lake permissions
- F. Amazon EBS Multi-Attach as cross-account object storage

### B18-10

A software vendor proxies multi-gigabyte downloads through Lambda. It currently
uses horizontal concurrency scaling and vertical memory increases, but those
compute scaling strategies still proxy every byte. It needs global low latency,
private origin access, versioned releases, optional time-limited customer
authorization, and lower repeated origin transfer. Which redesign removes
Lambda from the data path while meeting the controls?

- A. Return time-limited S3 presigned URLs directly to viewers, keeping S3 private but accepting no edge cache for repeated global downloads
- B. Put CloudFront in front of a public S3 website endpoint and use long cache TTLs without OAC or viewer authorization
- C. Store versioned binaries in private S3, use CloudFront with OAC and caching, and apply signed URLs or cookies when viewer authorization is required
- D. Put Global Accelerator in front of the Lambda download proxy and continue horizontally scaling concurrency for every byte

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B18-01 |  |  |  |
| B18-02 |  |  |  |
| B18-03 |  |  |  |
| B18-04 |  |  |  |
| B18-05 |  |  |  |
| B18-06 |  |  |  |
| B18-07 |  |  |  |
| B18-08 |  |  |  |
| B18-09 |  |  |  |
| B18-10 |  |  |  |

Depois abra [B18 — Gabarito](B18_Gabarito.md).

Durante a correção, classifique primeiro o modelo de dados ou o tipo de análise.
Depois compare operação, escalabilidade, resiliência e custo das alternativas.
