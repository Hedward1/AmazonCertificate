# B16 — Questões

**Formato:** 10 questões autorais; uma resposta correta<br>
**Idioma:** 2 Português + 8 Inglês<br>
**Aulas:** 203–216<br>
**Tarefas:** 1.2, 3.2 e 4.2

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma |
|---|---:|---:|---|---|
| B16-01 | 3 | 3.2 | 206–207 | Português |
| B16-02 | 3 | 3.2 | 210–214 | Português |
| B16-03 | 3 | 3.2 | 210–212 | Inglês |
| B16-04 | 3 | 3.2 | 213–214 | Inglês |
| B16-05 | 3 | 3.2 | 213–215 | Inglês |
| B16-06 | 3 | 3.2 | 215 | Inglês |
| B16-07 | 3 | 3.2 | 216 | Inglês |
| B16-08 | 3 | 3.2 | 203–207 | Inglês |
| B16-09 | 1 | 1.2 | 205 | Inglês |
| B16-10 | 4 | 4.2 | 210–214 | Inglês |

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

A database accepts no more than 80 concurrent connections. A Lambda function
can scale far beyond that during bursts. Which control is most direct?

- A. Increase function memory only
- B. Enable a public Function URL
- C. Add more CloudFront cache behaviors
- D. Cap function/event-source concurrency and buffer bursts, while considering RDS Proxy

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

A CloudFront viewer request needs only a very fast URL rewrite and header
normalization, with no network call. Which option is preferred?

- A. Amazon MQ
- B. CloudFront Functions
- C. A long-running ECS task
- D. Lambda in a private subnet with NAT Gateway

### B16-08

An organization has standardized on Kubernetes APIs and tooling and requires a
managed Kubernetes control plane. Which service meets the requirement?

- A. Amazon ECS
- B. AWS Lambda
- C. Amazon ECR
- D. Amazon EKS

### B16-09

A production deployment must always reference the exact tested container image,
even if a tag is later moved. What should it reference?

- A. The image digest, with immutable-tag controls as appropriate
- B. The `latest` tag only
- C. A plaintext registry password
- D. The ECR console URL

### B16-10

A Lambda function is deleted after a lab, but charges/storage evidence remains.
Which resource commonly requires separate cleanup?

- A. The AWS Region
- B. The runtime itself
- C. The CloudWatch Logs log group and any exclusive role/triggers
- D. The Lambda service control plane

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
