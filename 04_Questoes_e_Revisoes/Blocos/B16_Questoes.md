# B16 — Questões

**Formato:** questões de resposta única e múltipla, conforme indicado<br>
**Idioma:** 2 Português + 8 Inglês<br>
**Aulas:** 203–216<br>
**Tarefas:** 1.2, 3.2 e 4.2

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma | Formato | Tipo | Dificuldade |
|---|---:|---:|---|---|---|---|---|
| B16-01 | 3 | 3.2 | 206–207 | Português | single | fundamental | básica |
| B16-02 | 3 | 3.2 | 210–214 | Português | single | situacional | intermediária |
| B16-03 | 3 | 3.2 | 210–212 | Inglês | single | situacional | intermediária |
| B16-04 | 3 | 3.2 | 213–214 | Inglês | multi-2 | integrada | avançada |
| B16-05 | 3 | 3.2 | 213–215 | Inglês | single | situacional | intermediária |
| B16-06 | 3 | 3.2 | 215 | Inglês | single | situacional | intermediária |
| B16-07 | 3 | 3.2 | 216 | Inglês | multi-2 | integrada | avançada |
| B16-08 | 3 | 3.2 | 203–207 | Inglês | single | situacional | intermediária |
| B16-09 | 1 | 1.2 | 205 | Inglês | multi-3 | integrada | avançada |
| B16-10 | 2 | 2.2 | 210–214 | Inglês | single | integrada | avançada |

### B16-01

Uma equipe quer executar uma API em containers sem gerenciar hosts. Não existe
requisito de Kubernetes. Qual opção tem menor sobrecarga operacional?

- A. Amazon ECS com AWS Fargate
- B. Amazon EKS com nodes self-managed
- C. EC2 Dedicated Hosts sem Auto Scaling
- D. Lambda@Edge para iniciar containers

### B16-02

Uma função recebe 100 requests/s e cada invocação dura em média 2 segundos.
Qual concurrency aproximada é necessária em regime estável?

- A. 50
- B. 100
- C. 200
- D. 1.000

### B16-03

A job runs for 40 minutes and cannot be divided or checkpointed. Which compute
choice is appropriate instead of a standard Lambda Function?

- A. Increase the standard Lambda Function timeout to 40 minutes
- B. Use ECS/Fargate, AWS Batch, or EC2 rather than a standard Lambda Function
- C. Use CloudFront Functions
- D. Put the job in the Lambda `/tmp` directory

### B16-04

A bursty Lambda API writes to an RDS database that accepts at most 80 concurrent
connections. The design must protect the database, reuse connections, and avoid
unbounded function scaling. **Choose TWO.**

- A. Increase the Lambda timeout to 15 minutes
- B. Place Amazon RDS Proxy between the functions and the database
- C. Put the functions in public subnets so each receives a public IP address
- D. Set reserved concurrency to a limit the downstream system can safely absorb
- E. Increase API Gateway cache TTL without limiting Lambda concurrency

### B16-05

A synchronous API needs predictable low initialization latency at all hours and
uses a runtime that might not support SnapStart. What should be evaluated first?

- A. Provisioned concurrency
- B. Reserved concurrency only
- C. A longer SQS retention period
- D. ECR lifecycle expiration

### B16-06

Which statement best describes Lambda SnapStart?

- A. It increases the maximum invocation timeout
- B. It creates an EKS cluster snapshot
- C. It snapshots an initialized compatible function version and restores environments from it
- D. It guarantees that all external sockets remain valid after restore

### B16-07

A global application needs a submillisecond URL rewrite on every viewer request
and separate origin-request logic that uses AWS SDK calls and has longer execution
requirements. Which edge options should be assigned to the two tasks? **Choose TWO.**

- A. Use CloudFront Functions for the lightweight viewer-request rewrite
- B. Use an EC2 Auto Scaling group for every viewer-request rewrite
- C. Use Step Functions Express Workflows as a CloudFront event handler
- D. Use Lambda@Edge for the origin-request logic that exceeds CloudFront Functions capabilities
- E. Use an SQS FIFO consumer for synchronous header normalization

### B16-08

A platform team already operates Helm charts, Kubernetes admission policies,
and controllers across environments. It wants AWS to manage control-plane
availability and upgrades while retaining Kubernetes APIs, choosing EC2 or
Fargate worker capacity per workload, and integrating pods with AWS IAM. Which
platform best satisfies these constraints with the least application rewrite?

- A. Self-manage Kubernetes control-plane and worker nodes on EC2 to preserve every API and assume all upgrade/availability work
- B. Migrate to Amazon ECS on Fargate and rewrite Helm charts, admission policies, and controllers into AWS-native deployment mechanisms
- C. Keep Kubernetes outside AWS and use Amazon ECR only for images, accepting an independently operated control plane and network integration
- D. Amazon EKS with managed control plane, appropriate data-plane options, and pod-level AWS access controls

### B16-09

A regulated ECS deployment pulls images from private ECR. It must deploy exactly
the tested bytes, identify vulnerable packages, and access ECR from private
subnets without routing image pulls through a NAT gateway. Which controls meet
the requirements? **Select THREE.**

- A. Reference the mutable `latest` tag in the task definition
- B. Reference the tested image by digest
- C. Enable ECR enhanced scanning with Amazon Inspector
- D. Store the image only in a developer workstation cache
- E. Configure the required ECR interface endpoints and an S3 gateway endpoint
- F. Give the task role unrestricted administrator access

### B16-10

EventBridge invokes a Lambda order handler asynchronously. A partner outage can
cause repeated failures; the company must bound retry age, preserve exhausted
events for later recovery, alert operators, and retain function logs for only
30 days. Which design meets the reliability and operations requirements without
custom polling code?

- A. Rely on an EventBridge archive for manual replay, disable Lambda retries, and keep failed-event discovery only in logs
- B. Replace EventBridge with an SQS queue and redrive policy, but omit idempotency, alarms, maximum retention analysis, and the required 30-day log lifecycle
- C. Configure asynchronous retry/maximum event age with an on-failure destination or DLQ, alarm on failures, and set the CloudWatch Logs retention policy to 30 days
- D. Configure an SNS email notification for each error, leave native retry age unbounded by design, and retain logs indefinitely

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B16-01 |  |  |  |
| B16-02 |  |  |  |
| B16-03 |  |  |  |
| B16-04 |  |  |  |
| B16-05 |  |  |  |
| B16-06 |  |  |  |
| B16-07 |  |  |  |
| B16-08 |  |  |  |
| B16-09 |  |  |  |
| B16-10 |  |  |  |

Abra o [gabarito](B16_Gabarito.md) somente após registrar tudo.

Na correção, verbalize o limite e o trade-off que eliminaram cada distrator.
Não use apenas a memória do nome do serviço.
