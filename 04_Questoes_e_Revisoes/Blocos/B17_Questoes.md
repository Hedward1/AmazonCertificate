# B17 — Questões

**Formato:** questões de resposta única e múltipla, conforme indicado<br>
**Idioma:** 2 Português + 8 Inglês<br>
**Aulas:** 217–225<br>
**Tarefas:** 1.2, 2.1, 3.2 e 3.3

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma | Formato | Tipo | Dificuldade |
|---|---:|---:|---|---|---|---|---|
| B17-01 | 3 | 3.2 | 217 | Português | single | fundamental | básica |
| B17-02 | 3 | 3.3 | 219–221 | Português | single | situacional | intermediária |
| B17-03 | 3 | 3.3 | 219–221 | Inglês | single | situacional | intermediária |
| B17-04 | 3 | 3.3 | 219–221 | Inglês | multi-2 | situacional | avançada |
| B17-05 | 2 | 2.1 | 222–223 | Inglês | single | situacional | intermediária |
| B17-06 | 1 | 1.2 | 222–225 | Inglês | single | situacional | intermediária |
| B17-07 | 2 | 2.1 | 224 | Inglês | multi-2 | integrada | avançada |
| B17-08 | 1 | 1.2 | 225 | Inglês | single | integrada | avançada |
| B17-09 | 1 | 1.2 | 225 | Inglês | multi-3 | integrada | avançada |
| B17-10 | 3 | 3.5 | 218–221 | Inglês | single | integrada | avançada |

### B17-01

Uma função precisa acessar RDS privado e também uma API pública. Qual desenho de
rede é adequado?

- A. Public subnet, pois a função recebe public IP automaticamente
- B. Private subnets/SG para RDS e rota de saída por NAT para a API pública
- C. Apenas CORS no banco
- D. Elastic IP associado diretamente à função

### B17-02

Uma tabela DynamoDB sofre throttling porque todos os writes usam a mesma
partition key `ALL`. Qual é a primeira correção arquitetural?

- A. Usar uma partition key de alta cardinalidade que distribua o workload
- B. Substituir Query por Scan
- C. Criar uma única LSI com a mesma key
- D. Reduzir a capacidade da tabela

### B17-03

An application needs unpredictable key-value traffic and wants no capacity
planning during launch. Which DynamoDB capacity mode is the simplest choice?

- A. Provisioned capacity with no Auto Scaling
- B. One EC2 instance running a database
- C. On-demand capacity mode
- D. DAX as the primary persistent database

### B17-04

An existing DynamoDB table needs a new query using a different partition key.
The application accepts eventually consistent reads for this access pattern and
must add the index without recreating the table. **Choose TWO.**

- A. Add a local secondary index after table creation
- B. Add a global secondary index with the alternate partition key
- C. Require strongly consistent reads from the new index
- D. Scan the base table for every request to preserve low latency at scale
- E. Project the attributes required by the query into the global secondary index

### B17-05

A low-cost API needs simple HTTP routes, JWT authorization, and Lambda
integration. It does not need REST API caching or usage plans. What should it use?

- A. API Gateway HTTP API
- B. API Gateway WebSocket API
- C. Amazon MQ
- D. An S3 Glacier vault

### B17-06

Which statement about API Gateway API keys is correct?

- A. They are a complete user authentication mechanism by themselves
- B. They replace TLS
- C. They are primarily for usage metering/throttling, not user authentication
- D. They grant AWS credentials to a browser

### B17-07

A mobile commerce application needs a managed GraphQL endpoint with real-time
subscriptions. After checkout, an order workflow must coordinate Lambda tasks,
branch on payment status, retry with backoff, and run compensation. **Choose TWO.**

- A. Use AWS AppSync for the GraphQL API and subscriptions
- B. Use Amazon Route 53 as the workflow state machine
- C. Use an SQS message group as the GraphQL schema
- D. Use AWS Step Functions to orchestrate the order workflow
- E. Use AWS WAF to implement compensation steps

### B17-08

A mobile application needs self-service sign-up, MFA, social federation, and
JWTs for an API. Authenticated users must also upload objects directly to only
their own S3 prefix by using short-lived AWS credentials; no long-lived access
keys may be stored on devices. Which Cognito design meets both identity layers?

- A. Use a user pool for authentication and have an API backend generate presigned S3 uploads, without issuing the explicitly required temporary AWS credentials to the client
- B. Federate an external identity provider directly to an identity pool for AWS credentials, but provide no user directory for the required self-service sign-up and MFA controls
- C. Use a user pool for JWTs and embed one IAM user's access keys in the application for direct S3 uploads
- D. Use a user pool for authentication/JWTs and an identity pool with scoped IAM roles for temporary S3 credentials

### B17-09

A mobile application requires user sign-in and MFA, temporary scoped AWS
credentials for direct S3 uploads, and a managed GraphQL API with subscriptions.
Which services or components complete the design? **Select THREE.**

- A. An Amazon Cognito user pool for sign-in, MFA, and tokens
- B. A long-lived IAM access key embedded in the application
- C. An Amazon Cognito identity pool with roles scoped to each user's S3 prefix
- D. A public S3 bucket that accepts anonymous uploads
- E. AWS AppSync for GraphQL queries, mutations, and subscriptions
- F. A NAT Gateway as the identity provider

### B17-10

A team must stream committed order-row changes from RDS to a downstream data
store with low downtime during migration. It also needs separate alerts when
the DB instance fails over or enters a maintenance state. Which design correctly
separates data-plane changes from operational events?

- A. Use RDS event notifications for both row changes and failovers, then order notifications by timestamp in the consumer
- B. Use a CDC mechanism such as AWS DMS for row changes, and RDS event notifications/EventBridge or SNS for operational resource events
- C. Use DMS full load on a schedule for row changes and infer failover from replication-task restarts, without CDC or RDS operational events
- D. Export database logs to CloudWatch Logs and parse every engine log line as guaranteed committed-row CDC and maintenance telemetry

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B17-01 |  |  |  |
| B17-02 |  |  |  |
| B17-03 |  |  |  |
| B17-04 |  |  |  |
| B17-05 |  |  |  |
| B17-06 |  |  |  |
| B17-07 |  |  |  |
| B17-08 |  |  |  |
| B17-09 |  |  |  |
| B17-10 |  |  |  |

Depois consulte [B17 — Gabarito](B17_Gabarito.md).

Na correção, reconstrua o access pattern, o fluxo de rede ou a cadeia de
autorização que sustentou cada resposta.
