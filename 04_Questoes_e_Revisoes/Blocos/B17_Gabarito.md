# B17 — Gabarito comentado

Abra após responder às [questões B17](B17_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B17-01 | B | 3.2 |
| B17-02 | A | 3.3 |
| B17-03 | C | 3.3 |
| B17-04 | D | 3.3 |
| B17-05 | A | 2.1 |
| B17-06 | C | 1.2 |
| B17-07 | B | 2.1 |
| B17-08 | D | 1.2 |
| B17-09 | A | 1.2 |
| B17-10 | B | 3.3 |

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

## B17-04 — Answer D

- **Central requirement:** add a new access pattern with a different partition key.
- **Decisive words:** *different partition key*, *existing table*.
- **A:** an LSI keeps the base partition key and must be defined at table creation.
- **B:** S3 has no DynamoDB index type.
- **C:** CloudFront caching is unrelated.
- **D:** correct; a GSI can use different keys and be added later.
- **Reusable rule:** alternate partition key added after creation → GSI.
- **Lessons:** 219–221.
- **Reference:** [DynamoDB secondary indexes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html).
- **Common trap:** reversing GSI and LSI creation constraints.

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

## B17-07 — Answer B

- **Central requirement:** orchestrate sequence, branches, retries and compensation.
- **Decisive words:** *sequential*, *branching*, *backoff*, *compensation*.
- **A:** S3 Lifecycle manages objects.
- **B:** correct; Step Functions models state and error handling explicitly.
- **C:** Route 53 Resolver handles DNS.
- **D:** EBS Multi-Attach is block storage.
- **Reusable rule:** multi-step workflow with state/error paths → Step Functions.
- **Lessons:** 224.
- **Reference:** [Step Functions concepts](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html).
- **Common trap:** implementing orchestration by Lambda calling Lambda.

## B17-08 — Answer D

- **Central requirement:** authenticate app users and issue JWTs.
- **Decisive words:** *sign-up*, *MFA*, *federation*, *JWT*.
- **A:** an identity pool brokers temporary AWS credentials.
- **B:** Streams captures DynamoDB item changes.
- **C:** usage plans meter API clients.
- **D:** correct; a user pool is the user directory/authentication component.
- **Reusable rule:** application user authentication → Cognito User Pool.
- **Lessons:** 225.
- **Reference:** [Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html).
- **Common trap:** swapping user and identity pools.

## B17-09 — Answer A

- **Central requirement:** issue temporary scoped AWS credentials to a mobile user.
- **Decisive words:** *temporary*, *AWS credentials*, *one S3 prefix*.
- **A:** correct; Identity Pool maps identity to least-privilege IAM roles.
- **B:** hard-coded long-lived keys are unsafe.
- **C:** a User Pool token is not itself permanent AWS access credentials.
- **D:** public policy violates scoped access.
- **Reusable rule:** client needs temporary AWS credentials → Cognito Identity Pool.
- **Lessons:** 225.
- **Reference:** [Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html).
- **Common trap:** embedding IAM user keys in mobile binaries.

## B17-10 — Answer B

- **Central requirement:** distinguish operational RDS events from data changes.
- **Decisive words:** *every row update*, *event notifications*.
- **A:** RDS events do not require DynamoDB.
- **B:** correct; subscriptions describe operational resource events, not general row CDC.
- **C:** SNS/EventBridge integrations are relevant; Glacier is not required.
- **D:** database public access is not a prerequisite.
- **Reusable rule:** row-level change stream → CDC/engine mechanism, not RDS event subscription.
- **Lessons:** 218.
- **Reference:** [RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html).
- **Common trap:** treating control-plane events as database records.

## Ação após a correção

Registre erros e baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), incluindo o access pattern ou fluxo de autorização correto.
