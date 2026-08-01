# B15 — Questões

**Formato:** 10 questões autorais; uma resposta correta<br>
**Idioma:** 2 Português + 8 Inglês<br>
**Aulas:** 191–202<br>
**Tarefas:** 1.2, 2.1, 3.2 e 3.5

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma |
|---|---:|---:|---|---|
| B15-01 | 3 | 3.5 | 192–193 | Português |
| B15-02 | 3 | 3.5 | 194–196 | Português |
| B15-03 | 3 | 3.5 | 192–193 | Inglês |
| B15-04 | 2 | 2.1 | 197 | Inglês |
| B15-05 | 3 | 3.2 | 198–201 | Inglês |
| B15-06 | 3 | 3.2 | 199–201 | Inglês |
| B15-07 | 3 | 3.2 | 199–202 | Inglês |
| B15-08 | 3 | 3.2 | 199–201 | Inglês |
| B15-09 | 3 | 3.5 | 192–196 | Inglês |
| B15-10 | 1 | 1.2 | 199–202 | Inglês |

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

A Java application uses JMS and ActiveMQ-specific behavior. The company wants a
managed broker with minimal application changes. Which service should it use?

- A. Amazon SQS
- B. Amazon SNS
- C. Amazon Kinesis Data Streams
- D. Amazon MQ for ActiveMQ

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

An ECS service increases its desired task count on an EC2 capacity provider,
but new tasks remain `PENDING` because the cluster has no free CPU. What else
must scale?

- A. CloudFront cache behaviors
- B. The EC2 cluster capacity, typically through the capacity provider/ASG
- C. Kinesis retention
- D. The task definition revision number only

### B15-08

Which ECS object is the versioned blueprint that declares images, CPU, memory,
roles, ports, logging, and volumes?

- A. Cluster
- B. Service
- C. Running task
- D. Task definition

### B15-09

Several low-latency Kinesis consumers must read the same shards without sharing
read throughput. Which feature should be evaluated?

- A. Enhanced fan-out
- B. SQS short polling
- C. Firehose buffering
- D. ECS bin packing

### B15-10

A container image contains a plaintext database password in an environment
variable embedded in the image. What is the best improvement?

- A. Publish the image to a public ECR repository
- B. Reference Secrets Manager or Parameter Store and grant narrowly scoped access
- C. Put the password in the container name
- D. Increase task memory

Assume the task can use the native ECS secrets integration.

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
