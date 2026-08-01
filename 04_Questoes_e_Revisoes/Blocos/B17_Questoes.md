# B17 — Questões

**Formato:** 10 questões autorais; uma resposta correta<br>
**Idioma:** 2 Português + 8 Inglês<br>
**Aulas:** 217–225<br>
**Tarefas:** 1.2, 2.1, 3.2 e 3.3

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma |
|---|---:|---:|---|---|
| B17-01 | 3 | 3.2 | 217 | Português |
| B17-02 | 3 | 3.3 | 219–221 | Português |
| B17-03 | 3 | 3.3 | 219–221 | Inglês |
| B17-04 | 3 | 3.3 | 219–221 | Inglês |
| B17-05 | 2 | 2.1 | 222–223 | Inglês |
| B17-06 | 1 | 1.2 | 222–225 | Inglês |
| B17-07 | 2 | 2.1 | 224 | Inglês |
| B17-08 | 1 | 1.2 | 225 | Inglês |
| B17-09 | 1 | 1.2 | 225 | Inglês |
| B17-10 | 3 | 3.3 | 218–221 | Inglês |

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

An access pattern requires a different partition key and must be added to an
existing DynamoDB table. Which index type fits?

- A. Local secondary index created after launch
- B. S3 index
- C. CloudFront cache behavior
- D. Global secondary index

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

An order process has sequential steps, branching, retries with backoff, and a
compensation path. Which service is the best orchestrator?

- A. S3 Lifecycle
- B. AWS Step Functions
- C. Route 53 Resolver
- D. EBS Multi-Attach

### B17-08

A mobile application needs sign-up, sign-in, MFA, federation, and JWT tokens.
Which Cognito component provides these capabilities?

- A. Cognito identity pool only
- B. DynamoDB Streams
- C. API Gateway usage plan
- D. Cognito user pool

### B17-09

Authenticated mobile users need temporary, scoped AWS credentials to upload
directly to one S3 prefix. Which Cognito component is relevant?

- A. Cognito identity pool mapped to least-privilege IAM roles
- B. A hard-coded IAM user access key
- C. Cognito user pool alone as permanent AWS credentials
- D. A public bucket policy

### B17-10

A team enables RDS event notifications and expects one event for every row
update. What is wrong with this assumption?

- A. RDS event notifications require DynamoDB
- B. They represent operational DB-instance events, not general row-level CDC
- C. They can only be delivered to S3 Glacier
- D. They require a public database

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
