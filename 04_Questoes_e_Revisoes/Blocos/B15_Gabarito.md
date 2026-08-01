# B15 — Gabarito comentado

Abra após responder às [questões B15](B15_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B15-01 | A | 3.5 |
| B15-02 | B | 3.5 |
| B15-03 | C | 3.5 |
| B15-04 | A,D | 2.1 |
| B15-05 | A | 3.2 |
| B15-06 | C | 3.2 |
| B15-07 | B,D | 3.2 |
| B15-08 | D | 2.1 |
| B15-09 | A,C,E | 3.5 |
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

## B15-04 — Answer A,D

- **Central requirement:** preserve ActiveMQ/JMS behavior with managed, multi-AZ broker availability.
- **Decisive words:** *ActiveMQ-specific*, *minimal code changes*, *across Availability Zones*.
- **A:** correct; Amazon MQ for ActiveMQ provides managed compatibility with the existing broker protocols and APIs.
- **B:** incorrect; SQS semantics are not a drop-in replacement for ActiveMQ/JMS-specific features.
- **C:** incorrect; one Spot-hosted broker is self-managed and interruption-prone.
- **D:** correct; active/standby deployment provides managed failover across Availability Zones.
- **E:** incorrect; SNS does not accept JMS frames as an ActiveMQ broker.
- **Reusable rule:** broker compatibility plus minimal refactoring points to Amazon MQ; add active/standby when broker HA is required.
- **Lessons:** 197.
- **Reference:** [Amazon MQ broker architecture](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-broker-architecture.html).

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

## B15-07 — Answer B,D

- **Central requirement:** scale both ECS tasks and the EC2 capacity that can place them, with managed coordination.
- **Decisive words:** *tasks remain PENDING*, *no free CPU*, *minimal custom automation*.
- **A:** incorrect; repository count does not create cluster CPU or memory.
- **B:** correct; the Auto Scaling group capacity provider connects ECS placement demand to EC2 capacity.
- **C:** incorrect; the task execution role pulls images and logs; it should not launch cluster instances.
- **D:** correct; managed scaling adjusts the backing Auto Scaling group from capacity-provider reservation signals.
- **E:** incorrect; DNS zones do not provide task placement capacity.
- **Reusable rule:** ECS-on-EC2 service scaling changes desired tasks; a capacity provider with managed scaling changes the underlying hosts.
- **Lessons:** 199–202.
- **Reference:** [ECS capacity provider managed scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-scaling-behavior.html).

## B15-08 — Answer D

- **Central requirement:** migrate an existing stateful application to a managed
  container runtime without carrying local state, static credentials, or a
  single-host dependency into the target architecture.
- **Decisive words:** *stateful API*, *minimal host management*, *multiple AZs*,
  *rollback*, *no Kubernetes requirement*.
- **A:** MGN is a valid rehost path when containerization is not yet justified,
  but the result remains an EC2 workload and does not satisfy this migration goal.
- **B:** ECS on EC2 is technically possible, but keeping state on one host and
  access keys in the task preserves the original availability and security risks.
- **C:** EKS can run the container, but it adds an unnecessary Kubernetes control
  model while hostPath, `latest`, and manual replacement undermine resilience
  and repeatable rollback.
- **D:** correct; it covers assessment, externalized state/configuration,
  short-lived task credentials, immutable image delivery, managed orchestration,
  health validation, multi-AZ scaling, cutover, and rollback.
- **Reusable rule:** container migration is a lifecycle—assess, externalize,
  build/test, select the orchestrator, deploy, observe, cut over, and retain a
  rollback—not a VM filesystem copied into an image.
- **Lessons:** 199–201.
- **Reference:** [Containerizing and migrating applications with AWS App2Container](https://docs.aws.amazon.com/prescriptive-guidance/latest/containerize-java-a2c/introduction.html).
- **Common trap:** assuming a container is automatically stateless, secure, or
  highly available.

## B15-09 — Answer A,C,E

- **Central requirement:** isolate consumer throughput, remove hot-shard pressure, and retain replay history.
- **Decisive words:** *independent consumers*, *replay*, *hot shard*, *low-cardinality partition key*.
- **A:** correct; enhanced fan-out gives registered consumers dedicated read throughput and low-latency delivery.
- **B:** incorrect; one competing-consumer SQS queue would not give every consumer the full ordered stream and replay model.
- **C:** correct; higher-cardinality keys distribute writes; resharding adds capacity where the key distribution can use it.
- **D:** incorrect; Firehose delivery does not replace independent stream consumption, and disabling retention violates replay.
- **E:** correct; retention must cover the incident recovery replay window.
- **F:** incorrect; EBS Multi-Attach is unrelated to Kinesis consumer throughput or checkpoints.
- **Reusable rule:** stream design separates write partitioning, per-consumer read capacity, and retention/replay requirements.
- **Lessons:** 192–196.
- **Reference:** [Kinesis enhanced fan-out](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html).

## B15-10 — Answer B

- **Central requirement:** decouple credential lifecycle from immutable images while using a dedicated ECS task execution role for least-privilege native secret injection and rotation.
- **Decisive words:** *image layer*, *independent rotation*, *no plaintext*, *only this workload*.
- **A:** embedding ciphertext avoids plaintext at rest in the layer but couples rotation to image delivery and broad KMS decrypt permission; native secret references provide cleaner lifecycle and scope.
- **B:** correct; for native ECS secret injection, the ECS task execution role retrieves the referenced value and needs `secretsmanager:GetSecretValue` or `ssm:GetParameters`, plus `kms:Decrypt` when a customer managed KMS key protects it. A new task launch consumes the rotated value.
- **C:** task definitions and `DescribeTaskDefinition` output can expose plain environment values; update permission alone is not confidentiality.
- **D:** encrypted S3 can be engineered, but a shared broad role and custom fetch/rotation logic violate least privilege and add operations compared with native integration.
- **Reusable rule:** for native ECS secret injection, scope retrieval and any KMS decrypt permissions on the task execution role; use the task role only for AWS API calls made by application code, avoid logs, and redeploy tasks after rotation.
- **Lessons:** 199–202.
- **Reference:** [Pass secrets to ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html).
- **Common trap:** using plain environment variables committed in task JSON or image layers.

## Ação após a correção

Registre erro ou baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md) e escreva a regra sem nomes das alternativas.
