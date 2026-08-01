# B15 — Questões

**Formato:** questões de resposta única e múltipla, conforme indicado<br>
**Idioma:** 2 Português + 8 Inglês<br>
**Aulas:** 191–202<br>
**Tarefas:** 1.2, 2.1, 3.2 e 3.5

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma | Formato | Tipo | Dificuldade |
|---|---:|---:|---|---|---|---|---|
| B15-01 | 3 | 3.5 | 192–193 | Português | single | fundamental | básica |
| B15-02 | 3 | 3.5 | 194–196 | Português | single | fundamental | básica |
| B15-03 | 3 | 3.5 | 192–193 | Inglês | single | situacional | intermediária |
| B15-04 | 2 | 2.1 | 197 | Inglês | multi-2 | situacional | avançada |
| B15-05 | 3 | 3.2 | 198–201 | Inglês | single | situacional | intermediária |
| B15-06 | 3 | 3.2 | 199–201 | Inglês | single | situacional | intermediária |
| B15-07 | 3 | 3.2 | 199–202 | Inglês | multi-2 | integrada | avançada |
| B15-08 | 2 | 2.1 | 199–201 | Inglês | single | integrada | avançada |
| B15-09 | 3 | 3.5 | 192–196 | Inglês | multi-3 | integrada | avançada |
| B15-10 | 1 | 1.2 | 199–202 | Inglês | single | integrada | avançada |

### B15-01

Fraude e analytics precisam consumir independentemente o mesmo fluxo, manter
ordem por cliente e reler eventos após correções. Qual serviço atende melhor?

- A. Amazon Kinesis Data Streams com `customer-id` como partition key
- B. Uma única fila SQS Standard
- C. Amazon SNS com email subscribers
- D. Amazon Data Firehose sem stream de origem

### B15-02

Sensores enviam logs que devem ser comprimidos e entregues ao S3 em poucos
minutos, sem consumers customizados nem shards gerenciados. Qual escolha?

- A. Amazon MQ
- B. Amazon Data Firehose
- C. SQS FIFO com um único group
- D. ECS service em instâncias EC2

### B15-03

A provisioned Kinesis stream has four shards, but almost all writes use the
same partition key and one shard throttles. What should be changed first?

- A. Add more SQS consumers
- B. Increase the Firehose buffer interval
- C. Use a higher-cardinality partition-key strategy that preserves required ordering
- D. Decrease stream retention

### B15-04

A Java application depends on JMS and ActiveMQ-specific features. The company
wants minimal code changes and broker availability across Availability Zones,
without administering broker hosts. **Choose TWO.**

- A. Use Amazon MQ for ActiveMQ to preserve the compatible broker APIs
- B. Replace the broker with Amazon SQS FIFO without testing application semantics
- C. Run a single self-managed ActiveMQ broker on an EC2 Spot Instance
- D. Deploy an active/standby Amazon MQ broker configuration with multi-AZ storage
- E. Send JMS frames directly to an Amazon SNS topic

### B15-05

A small, variable ECS workload must run containers without managing or patching
EC2 hosts. Which compute option best fits?

- A. AWS Fargate
- B. EC2 Dedicated Hosts managed manually
- C. Lambda@Edge for every container
- D. Amazon MQ

### B15-06

Application code inside an ECS task needs permission to read one S3 prefix. To
which role should that permission be granted?

- A. The EC2 instance profile in every case
- B. The ECS service-linked role
- C. The task role referenced by the task definition
- D. The task execution role only

### B15-07

An ECS service on EC2 scales desired tasks from queue depth, but tasks remain
`PENDING` when the cluster runs out of CPU. The team wants ECS to add instances
and remove empty capacity with minimal custom automation. **Choose TWO.**

- A. Increase the number of ECR repositories
- B. Associate the service with an Auto Scaling group capacity provider
- C. Grant the task execution role permission to launch EC2 instances
- D. Enable capacity provider managed scaling for the backing Auto Scaling group
- E. Scale the number of Route 53 hosted zones with desired task count

### B15-08

A stateful API on EC2 stores sessions and uploads on the instance, reads
configuration from a local file, and uses long-term IAM access keys. The company
wants to migrate it to containers with minimal host management, scale across
Availability Zones, and retain a tested rollback path. The team has no
Kubernetes requirement.

Which migration plan best meets the requirements?

- A. Rehost the unchanged VM with AWS Application Migration Service and call the
  resulting EC2 instance a container deployment.
- B. Package the application and its local state in one image, run one ECS task
  on an EC2 host with a bind mount, and retain the IAM access keys in environment
  variables.
- C. Deploy one pod on Amazon EKS with a hostPath volume and a `latest` image;
  replace the pod manually during cutover to minimize migration planning.
- D. Assess dependencies, externalize sessions/uploads and configuration,
  publish a scanned immutable image to ECR, use an ECS/Fargate service with task
  roles and health checks, and shift traffic with a tested rollback strategy.

### B15-09

A Kinesis Data Streams workload has several low-latency independent consumers,
must retain records for replay during incident recovery, and is throttled by a
hot shard caused by a low-cardinality partition key. Which changes address the
requirements? **Select THREE.**

- A. Register consumers for enhanced fan-out
- B. Replace the stream with one SQS queue shared by all consumers
- C. Choose a higher-cardinality partition key and split or reshard capacity as needed
- D. Deliver records only through Firehose and disable stream retention
- E. Increase the stream retention period to cover the required replay window
- F. Use EBS Multi-Attach for consumer checkpoints

### B15-10

An ECS service runs immutable images in several environments. A database
password is currently baked into an image layer; security requires independent
rotation, no plaintext in task-definition environment fields, and
least-privilege retrieval by only this workload. Assume native ECS secret
injection is supported. Which design best meets the requirements?

- A. Encrypt a password file during the image build, place the ciphertext in the image, and give every task broad KMS decrypt access
- B. Store the value in Secrets Manager or encrypted Parameter Store, reference it from the task definition, grant only this workload's ECS task execution role permission to retrieve it (and decrypt its customer managed KMS key, if used), and replace tasks after rotation
- C. Put the plaintext value in the task definition environment section and restrict only who can update the service
- D. Store one encrypted configuration file in S3 and let a shared cluster role read the entire configuration bucket at startup

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B15-01 |  |  |  |
| B15-02 |  |  |  |
| B15-03 |  |  |  |
| B15-04 |  |  |  |
| B15-05 |  |  |  |
| B15-06 |  |  |  |
| B15-07 |  |  |  |
| B15-08 |  |  |  |
| B15-09 |  |  |  |
| B15-10 |  |  |  |

Abra o [gabarito](B15_Gabarito.md) somente após registrar todas.
