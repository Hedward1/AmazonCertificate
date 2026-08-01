# B18 — Questões

**Formato:** 10 questões autorais; uma resposta correta<br>
**Idioma:** 2 Português + 8 Inglês<br>
**Aulas:** 226–244<br>
**Tarefas:** 2.1, 3.3, 3.5 e 4.3

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma |
|---|---:|---:|---|---|
| B18-01 | 3 | 3.3 | 230–239 | Português |
| B18-02 | 3 | 3.5 | 240–244 | Português |
| B18-03 | 3 | 3.3 | 231–234 | Inglês |
| B18-04 | 3 | 3.3 | 237 | Inglês |
| B18-05 | 3 | 3.3 | 239 | Inglês |
| B18-06 | 4 | 4.3 | 240–241 | Inglês |
| B18-07 | 3 | 3.5 | 242 | Inglês |
| B18-08 | 3 | 3.5 | 243 | Inglês |
| B18-09 | 3 | 3.5 | 244 | Inglês |
| B18-10 | 2 | 2.1 | 226–229 | Inglês |

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

A fraud system must efficiently traverse relationships among accounts, devices,
IP addresses, and merchants. Which database is purpose-built for this?

- A. Amazon Neptune
- B. Amazon Keyspaces
- C. Amazon Timestream
- D. Amazon ElastiCache Memcached

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

The business needs a managed data warehouse for repeated OLAP joins and BI over
large structured datasets. Which service is the best fit?

- A. DynamoDB Accelerator
- B. Amazon S3 Object Lock
- C. Amazon Redshift
- D. Cognito identity pools

### B18-08

Users need full-text search, relevance scoring, and log analytics over indexed
documents. Which service is designed for this?

- A. Amazon OpenSearch Service
- B. Amazon EBS
- C. AWS Storage Gateway
- D. Amazon RDS event subscriptions

### B18-09

Data engineers need to run custom Apache Spark jobs over a large data lake.
Which AWS service should they evaluate?

- A. Amazon SNS
- B. Amazon EMR
- C. Amazon Cognito
- D. AWS Global Accelerator

### B18-10

A website sends every large software binary through Lambda to users worldwide.
It must reduce compute work and origin load. Which redesign is best?

- A. Increase Lambda timeout for each download
- B. Put binaries in an ElastiCache node only
- C. Store versioned binaries in private S3 and distribute through CloudFront with OAC
- D. Send binaries in SQS messages

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
