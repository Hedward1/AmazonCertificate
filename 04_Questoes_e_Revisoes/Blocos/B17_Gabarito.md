# B17 — Gabarito comentado

Abra após responder às [questões B17](B17_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B17-01 | B | 3.2 |
| B17-02 | A | 3.3 |
| B17-03 | C | 3.3 |
| B17-04 | B,E | 3.3 |
| B17-05 | A | 2.1 |
| B17-06 | C | 1.2 |
| B17-07 | A,D | 2.1 |
| B17-08 | D | 1.2 |
| B17-09 | A,C,E | 1.2 |
| B17-10 | B | 3.5 |

## B17-01 — Resposta B

- **Requisito central:** alcançar RDS privado e uma API pública.
- **Palavras decisivas:** *privado*, *pública*, *Lambda*.
- **A:** Lambda não recebe public IP apenas por usar public subnet.
- **B:** correta; private subnets/SG alcançam RDS e NAT fornece saída pública.
- **C:** CORS é comportamento de browser, não roteamento de banco.
- **D:** não se associa Elastic IP diretamente a uma função Lambda.
- **Regra reutilizável:** Lambda VPC + internet IPv4 → private subnets e NAT/egress.
- **Aulas:** 217.
- **Referência:** [Lambda VPC internet access](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc-internet.html).
- **Erro comum:** confundir public subnet com public IP da função.

## B17-02 — Resposta A

- **Requisito central:** distribuir writes e remover hot partition.
- **Palavras decisivas:** *todos*, *mesma partition key*, *throttling*.
- **A:** correta; alta cardinalidade distribui o tráfego pelo hash.
- **B:** Scan aumenta leitura e não redistribui writes.
- **C:** LSI mantém a mesma partition key.
- **D:** reduzir capacity piora throttling.
- **Regra reutilizável:** hot partition → redesenhar key e access pattern.
- **Aulas:** 219–221.
- **Referência:** [DynamoDB partition key design](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html).
- **Erro comum:** escalar tabela sem remover uma key dominante.

## B17-03 — Answer C

- **Central requirement:** handle unpredictable key-value traffic without capacity planning.
- **Decisive words:** *unpredictable*, *no capacity planning*.
- **A:** fixed provisioned capacity needs planning and risks throttling/waste.
- **B:** self-managed EC2 adds operations and is not DynamoDB capacity mode.
- **C:** correct; on-demand charges per request and manages capacity automatically.
- **D:** DAX is a cache, not the primary durable database.
- **Reusable rule:** unpredictable DynamoDB demand → on-demand as the simple starting mode.
- **Lessons:** 219–221.
- **Reference:** [DynamoDB capacity modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html).
- **Common trap:** treating on-demand as always cheapest for steady predictable traffic.

## B17-04 — Answer B,E

- **Central requirement:** add an alternate partition-key query to an existing table with only required projected data.
- **Decisive words:** *different partition key*, *without recreating*, *eventually consistent*, *attributes required*.
- **A:** incorrect; an LSI uses the base partition key and must be created with the table.
- **B:** correct; a GSI can be added later and defines a different partition key.
- **C:** incorrect; GSI reads support eventual consistency, not strongly consistent reads.
- **D:** incorrect; repeated scans do not provide the scalable low-latency access pattern.
- **E:** correct; projecting query attributes supports the access path and avoids unnecessary base-table reads.
- **Reusable rule:** a new alternate partition key on an existing DynamoDB table points to a GSI; design its key and projection from the query.
- **Lessons:** 219–221.
- **Reference:** [DynamoDB global secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html).

## B17-05 — Answer A

- **Central requirement:** simple low-cost HTTP routes with JWT and Lambda.
- **Decisive words:** *simple*, *no caching*, *no usage plans*.
- **A:** correct; HTTP API provides the needed feature set with lower overhead.
- **B:** WebSocket is for persistent bidirectional connections.
- **C:** Amazon MQ is a broker.
- **D:** Glacier is archival storage.
- **Reusable rule:** simple proxy/JWT API → evaluate HTTP API first.
- **Lessons:** 222–223.
- **Reference:** [Choose HTTP or REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html).
- **Common trap:** choosing REST API without an advanced feature requirement.

## B17-06 — Answer C

- **Central requirement:** correctly classify API keys.
- **Decisive words:** *API keys*, *correct*.
- **A:** API keys are not standalone user identity/authentication.
- **B:** TLS remains required.
- **C:** correct; API keys support usage identification, metering and throttling.
- **D:** they do not issue AWS credentials.
- **Reusable rule:** usage plan/API key ≠ authentication; use IAM/JWT/Cognito/authorizer.
- **Lessons:** 222–225.
- **Reference:** [API keys and usage plans](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html).
- **Common trap:** securing private data with only an API key.

## B17-07 — Answer A,D

- **Central requirement:** provide managed GraphQL real-time access and reliable stateful business-process orchestration.
- **Decisive words:** *GraphQL*, *subscriptions*, *branch*, *retry with backoff*, *compensation*.
- **A:** correct; AppSync provides managed GraphQL APIs and real-time subscription capabilities.
- **B:** incorrect; Route 53 routes DNS and does not persist workflow state.
- **C:** incorrect; an SQS group orders messages but does not define a GraphQL API.
- **D:** correct; Step Functions models branching, retries, state, and compensation workflows.
- **E:** incorrect; WAF filters web requests and does not orchestrate transactions.
- **Reusable rule:** use AppSync for the client-facing GraphQL contract and Step Functions for multi-step stateful orchestration.
- **Lessons:** 222–224.
- **Reference:** [What is AWS AppSync?](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html).

## B17-08 — Answer D

- **Central requirement:** authenticate human users and separately exchange identity for least-privilege temporary AWS credentials.
- **Decisive words:** *JWTs for an API*, *own S3 prefix*, *short-lived*, *no long-lived keys*.
- **A:** presigned uploads can be a sound design, but this option does not meet the explicit requirement that clients receive scoped temporary AWS credentials.
- **B:** direct federation can issue temporary credentials, but it omits the required managed self-service user directory and MFA lifecycle.
- **C:** the user pool solves authentication, but embedded long-lived IAM credentials violate device security and per-user scope.
- **D:** correct; the user pool authenticates and issues JWTs, while the identity pool maps authenticated identities to scoped temporary-role credentials.
- **Reusable rule:** user pool answers “who is the app user?”; identity pool answers “which temporary AWS role may that identity assume?”.
- **Lessons:** 225.
- **Reference:** [Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html) and [Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html).
- **Common trap:** using a JWT directly as an AWS access key or giving all mobile users the same IAM identity.

## B17-09 — Answer A,C,E

- **Central requirement:** combine application authentication, temporary AWS authorization, and managed GraphQL real-time APIs.
- **Decisive words:** *sign-in and MFA*, *temporary scoped credentials*, *direct S3*, *GraphQL subscriptions*.
- **A:** correct; a user pool handles sign-up/sign-in, MFA, and application tokens.
- **B:** incorrect; embedded long-lived access keys are insecure and cannot be safely scoped per user lifecycle.
- **C:** correct; an identity pool exchanges identities for temporary IAM role credentials.
- **D:** incorrect; anonymous public writes violate authentication and least privilege.
- **E:** correct; AppSync supplies managed GraphQL queries, mutations, and subscriptions.
- **F:** incorrect; a NAT Gateway provides egress, not identity federation.
- **Reusable rule:** Cognito user pools authenticate users, identity pools vend scoped AWS credentials, and AppSync exposes GraphQL data APIs.
- **Lessons:** 225.
- **Reference:** [Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html) and [AppSync real-time data](https://docs.aws.amazon.com/appsync/latest/devguide/aws-appsync-real-time-data.html).

## B17-10 — Answer B

- **Central requirement:** capture committed row changes while preserving a distinct channel for DB-instance lifecycle and availability events.
- **Decisive words:** *order-row changes*, *low downtime*, *fails over*, *maintenance state*.
- **A:** RDS operational notifications do not expose every committed row, and consumer sorting cannot reconstruct missing transactional changes.
- **B:** correct; DMS CDC reads database change information for data replication, while RDS operational events are routed independently for notification and automation.
- **C:** repeated full loads are not continuous delta capture and task restarts are not a complete operational event channel.
- **D:** engine logs are useful diagnostics but are not a portable guarantee of complete committed-row CDC plus every RDS lifecycle event.
- **Reusable rule:** database records require CDC or engine-native change streams; control-plane/resource state requires operational event services.
- **Lessons:** 218.
- **Reference:** [RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html).
- **Common trap:** treating an RDS event subscription as a transactional outbox or logical replication stream.

## Ação após a correção

Registre erros e baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), incluindo o access pattern ou fluxo de autorização correto.
