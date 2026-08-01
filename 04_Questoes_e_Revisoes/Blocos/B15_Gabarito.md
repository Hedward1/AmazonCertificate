# B15 — Gabarito comentado

Abra após responder às [questões B15](B15_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B15-01 | A | 3.5 |
| B15-02 | B | 3.5 |
| B15-03 | C | 3.5 |
| B15-04 | D | 2.1 |
| B15-05 | A | 3.2 |
| B15-06 | C | 3.2 |
| B15-07 | B | 3.2 |
| B15-08 | D | 3.2 |
| B15-09 | A | 3.5 |
| B15-10 | B | 1.2 |

## B15-01 — Resposta A

- **Requisito central:** múltiplos consumers independentes, ordem por cliente e replay.
- **Palavras decisivas:** *mesmo fluxo*, *reler*, *ordem por cliente*.
- **A:** correta; KDS é um log retido e a partition key cria a unidade de ordenação.
- **B:** uma fila SQS distribui trabalho e não oferece o replay multi-consumer descrito.
- **C:** SNS entrega notificações, mas não é o log retido solicitado.
- **D:** Firehose entrega a destinos e não expõe consumers gerais com replay.
- **Regra reutilizável:** event log + retention/replay → Kinesis Data Streams.
- **Aulas:** 192–193.
- **Referência:** [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html).
- **Erro comum:** escolher SQS por qualquer requisito assíncrono.

## B15-02 — Resposta B

- **Requisito central:** entrega gerenciada, comprimida e near-real-time no S3.
- **Palavras decisivas:** *sem consumers*, *sem shards*, *S3*.
- **A:** Amazon MQ é um broker de compatibilidade.
- **B:** correta; Data Firehose gerencia buffer, compressão e entrega.
- **C:** SQS FIFO não cria arquivos otimizados no S3.
- **D:** ECS adiciona código e operação desnecessários.
- **Regra reutilizável:** ingestão contínua diretamente a destino suportado → Firehose.
- **Aulas:** 194–196.
- **Referência:** [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html).
- **Erro comum:** exigir latência de milissegundos apesar do buffering.

## B15-03 — Answer C

- **Central requirement:** remove a partition-key write hot spot.
- **Decisive words:** *same partition key*, *one shard throttles*.
- **A:** SQS consumers do not change Kinesis write distribution.
- **B:** a Firehose buffer cannot redistribute KDS writes.
- **C:** correct; a higher-cardinality key spreads records while preserving only required order.
- **D:** retention changes storage duration, not write throughput distribution.
- **Reusable rule:** uneven shard traffic → inspect and redesign partition keys first.
- **Lessons:** 192–193.
- **Reference:** [Kinesis partition keys](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html).
- **Common trap:** adding shards while a single low-cardinality key remains hot.

## B15-04 — Answer D

- **Central requirement:** migrate JMS/ActiveMQ behavior with minimal code changes.
- **Decisive words:** *JMS*, *ActiveMQ-specific*, *managed broker*.
- **A:** SQS has its own API and semantics.
- **B:** SNS is managed pub/sub, not an ActiveMQ-compatible broker.
- **C:** KDS is a streaming log rather than JMS middleware.
- **D:** correct; Amazon MQ for ActiveMQ preserves supported broker protocols/APIs.
- **Reusable rule:** legacy broker protocol compatibility → Amazon MQ.
- **Lessons:** 197.
- **Reference:** [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).
- **Common trap:** selecting MQ for a new cloud-native queue without compatibility needs.

## B15-05 — Answer A

- **Central requirement:** run containers without managing EC2 hosts.
- **Decisive words:** *small*, *variable*, *without patching hosts*.
- **A:** correct; Fargate provides serverless compute capacity for ECS tasks.
- **B:** Dedicated Hosts maximize host responsibility.
- **C:** Lambda@Edge is event code at CloudFront, not arbitrary ECS container hosting.
- **D:** Amazon MQ is a message broker.
- **Reusable rule:** ECS containers + no host management → Fargate.
- **Lessons:** 198–201.
- **Reference:** [ECS on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html).
- **Common trap:** calling Fargate an orchestrator separate from ECS.

## B15-06 — Answer C

- **Central requirement:** grant application code narrowly scoped S3 access.
- **Decisive words:** *code inside task*, *one S3 prefix*.
- **A:** an instance profile is broader and is not applicable to every launch type.
- **B:** the service-linked role lets ECS call AWS services for control-plane operations.
- **C:** correct; the task role supplies credentials to application containers.
- **D:** execution role supports image pull/logs/secrets at startup, not normal app access.
- **Reusable rule:** application AWS API permission → task role.
- **Lessons:** 199–201.
- **Reference:** [ECS task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).
- **Common trap:** adding every permission to the execution role.

## B15-07 — Answer B

- **Central requirement:** provide compute capacity for additional ECS tasks on EC2.
- **Decisive words:** *desired count increased*, *PENDING*, *no free CPU*.
- **A:** caching is unrelated to cluster slots.
- **B:** correct; the capacity provider/ASG must add suitable EC2 capacity.
- **C:** stream retention is unrelated.
- **D:** a revision number cannot create CPU.
- **Reusable rule:** ECS on EC2 has service scaling and cluster capacity scaling layers.
- **Lessons:** 199–202.
- **Reference:** [ECS capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-capacity-providers.html).
- **Common trap:** assuming desired tasks automatically create hosts.

## B15-08 — Answer D

- **Central requirement:** identify the declarative, versioned ECS blueprint.
- **Decisive words:** *images*, *CPU*, *roles*, *versioned blueprint*.
- **A:** cluster groups tasks and capacity.
- **B:** service maintains a desired task count and deployments.
- **C:** a running task is an instantiation.
- **D:** correct; a task definition revision declares these settings.
- **Reusable rule:** blueprint → task definition; instance → task; controller → service.
- **Lessons:** 199–201.
- **Reference:** [Task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html).
- **Common trap:** treating a service as the container specification.

## B15-09 — Answer A

- **Central requirement:** dedicated Kinesis read throughput per low-latency consumer.
- **Decisive words:** *same shards*, *without sharing*, *low latency*.
- **A:** correct; enhanced fan-out provides registered consumers dedicated throughput per shard.
- **B:** short polling is an SQS receive mode.
- **C:** Firehose buffering increases delivery efficiency but is not consumer read capacity.
- **D:** bin packing places containers.
- **Reusable rule:** multiple KDS consumers contending for reads → evaluate enhanced fan-out.
- **Lessons:** 192–193.
- **Reference:** [Enhanced fan-out](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html).
- **Common trap:** ignoring the additional cost.

## B15-10 — Answer B

- **Central requirement:** remove plaintext secrets from a container image.
- **Decisive words:** *password*, *embedded in image*.
- **A:** publishing makes exposure worse.
- **B:** correct; reference a secrets service and grant least-privilege retrieval.
- **C:** a container name is metadata and not secret storage.
- **D:** memory does not protect the credential.
- **Reusable rule:** runtime secret → secrets service reference, role, rotation, and no logging.
- **Lessons:** 199–202.
- **Reference:** [Pass secrets to ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html).
- **Common trap:** using plain environment variables committed in task JSON or image layers.

## Ação após a correção

Registre erro ou baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md) e escreva a regra sem nomes das alternativas.
