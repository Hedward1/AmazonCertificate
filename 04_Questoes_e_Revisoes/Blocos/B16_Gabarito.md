# B16 — Gabarito comentado

Abra somente depois das [questões B16](B16_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B16-01 | A | 3.2 |
| B16-02 | C | 3.2 |
| B16-03 | B | 3.2 |
| B16-04 | B,D | 3.2 |
| B16-05 | A | 3.2 |
| B16-06 | C | 3.2 |
| B16-07 | A,D | 3.2 |
| B16-08 | D | 3.2 |
| B16-09 | B,C,E | 1.2 |
| B16-10 | C | 2.2 |

## B16-01 — Resposta A

- **Requisito central:** containers sem hosts e sem requisito Kubernetes.
- **Palavras decisivas:** *sem gerenciar hosts*, *não existe Kubernetes*.
- **A:** correta; ECS/Fargate executa tasks sem o cliente administrar EC2.
- **B:** EKS self-managed adiciona Kubernetes e gestão de nodes.
- **C:** Dedicated Hosts aumentam administração e capacidade ociosa.
- **D:** Lambda@Edge executa funções ligadas ao CloudFront, não containers gerais.
- **Regra reutilizável:** container AWS-native sem hosts/K8s → ECS on Fargate.
- **Aulas:** 203–207.
- **Referência:** [ECS on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html).
- **Erro comum:** escolher EKS apenas porque há containers.

## B16-02 — Resposta C

- **Requisito central:** estimar invocações simultâneas em regime estável.
- **Palavras decisivas:** *100 requests/s*, *2 segundos*.
- **A:** 50 seria taxa dividida por duração.
- **B:** 100 ignora que cada request ocupa dois segundos.
- **C:** correta; `100 × 2 = 200` execuções concorrentes.
- **D:** 1.000 não resulta dos valores fornecidos.
- **Regra reutilizável:** concurrency ≈ taxa por segundo × duração média.
- **Aulas:** 213–214.
- **Referência:** [Lambda concurrency](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html).
- **Erro comum:** confundir requests por segundo com concurrency.

## B16-03 — Answer B

- **Central requirement:** run one indivisible 40-minute job.
- **Decisive words:** *40 minutes*, *cannot be divided*.
- **A:** a standard Lambda Function invocation has a 15-minute maximum; the newer Durable Functions and MicroVMs are different execution models, not a 40-minute timeout setting.
- **B:** correct; container/batch/instance compute supports a longer process.
- **C:** CloudFront Functions are extremely short edge functions.
- **D:** `/tmp` storage does not extend execution time.
- **Reusable rule:** indivisible work beyond 15 minutes → not a standard Lambda Function; evaluate the exact current compute primitive.
- **Lessons:** 209–212.
- **Reference:** [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
- **Common trap:** treating timeout as an adjustable quota beyond the maximum.

## B16-04 — Answer B,D

- **Central requirement:** pool database connections and cap Lambda pressure below the database limit.
- **Decisive words:** *80 concurrent connections*, *reuse connections*, *avoid unbounded scaling*.
- **A:** incorrect; execution duration does not pool connections or cap concurrency.
- **B:** correct; RDS Proxy pools and reuses database connections across invocations.
- **C:** incorrect; VPC-connected Lambda functions do not receive public IPs, and public placement would not protect the database.
- **D:** correct; reserved concurrency limits how many invocations can pressure the downstream database.
- **E:** incorrect; caching might reduce some calls but does not enforce a safe concurrency ceiling.
- **Reusable rule:** protect relational databases from serverless bursts with connection pooling plus an explicit concurrency budget.
- **Lessons:** 210–214.
- **Reference:** [Using Lambda with RDS databases](https://docs.aws.amazon.com/lambda/latest/dg/services-rds.html).

## B16-05 — Answer A

- **Central requirement:** predictable low initialization latency regardless of SnapStart support.
- **Decisive words:** *predictable*, *all hours*, *might not support SnapStart*.
- **A:** correct; provisioned concurrency prepares a configured number of environments.
- **B:** reserved concurrency reserves/limits quota but does not pre-initialize environments.
- **C:** SQS retention is unrelated to synchronous cold start.
- **D:** ECR lifecycle manages images.
- **Reusable rule:** consistently warm Lambda capacity → provisioned concurrency.
- **Lessons:** 213–215.
- **Reference:** [Provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html).
- **Common trap:** ignoring its ongoing cost.

## B16-06 — Answer C

- **Central requirement:** identify SnapStart's actual mechanism.
- **Decisive words:** *best describes*.
- **A:** it does not change the 15-minute standard-function invocation timeout.
- **B:** it is unrelated to EKS cluster backups.
- **C:** correct; Lambda snapshots initialized compatible versions and restores environments.
- **D:** code must handle uniqueness, secrets, and connections after restore.
- **Reusable rule:** SnapStart optimizes initialization; validate runtime and restore safety.
- **Lessons:** 215.
- **Reference:** [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).
- **Common trap:** assuming every runtime and Region is supported.

## B16-07 — Answer A,D

- **Central requirement:** match lightweight viewer logic and more capable origin logic to the appropriate edge runtime.
- **Decisive words:** *submillisecond rewrite*, *every viewer request*, *AWS SDK calls*, *longer execution*.
- **A:** correct; CloudFront Functions is optimized for high-scale, short viewer event transformations.
- **B:** incorrect; EC2 adds latency and operations and is not a CloudFront viewer-event runtime.
- **C:** incorrect; Step Functions cannot be attached as a CloudFront event function.
- **D:** correct; Lambda@Edge supports the more capable origin-event code beyond CloudFront Functions limits.
- **E:** incorrect; an asynchronous queue consumer cannot synchronously modify a viewer request.
- **Reusable rule:** use CloudFront Functions for very short viewer transformations and Lambda@Edge when richer runtime capabilities are required.
- **Lessons:** 216.
- **Reference:** [Choosing between CloudFront Functions and Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-choosing.html).

## B16-08 — Answer D

- **Central requirement:** preserve the Kubernetes operating model while outsourcing control-plane availability and retaining flexible worker choices and AWS identity integration.
- **Decisive words:** *Helm*, *admission policies*, *controllers*, *least rewrite*, *EC2 or Fargate*.
- **A:** self-managed Kubernetes preserves compatibility but contradicts the requirement to outsource control-plane availability and upgrades.
- **B:** ECS on Fargate reduces orchestration/node operations, but the stated Kubernetes APIs and controllers would require a material rewrite.
- **C:** retaining an external control plane is technically possible and ECR can store images, but it does not meet the AWS-managed control-plane requirement.
- **D:** correct; EKS preserves Kubernetes APIs, manages the control plane, supports multiple data-plane choices, and integrates workload identities with AWS permissions.
- **Reusable rule:** choose EKS when Kubernetes compatibility is a hard constraint; choose ECS when AWS-native orchestration and lower Kubernetes operational complexity are acceptable.
- **Lessons:** 206–207.
- **Reference:** [What is EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html).
- **Common trap:** choosing EKS only because containers are present, without an actual Kubernetes compatibility requirement.

## B16-09 — Answer B,C,E

- **Central requirement:** immutable deployment identity, vulnerability visibility, and private ECR access without NAT.
- **Decisive words:** *exactly the tested bytes*, *vulnerable packages*, *private subnets*, *without NAT*.
- **A:** incorrect; a mutable tag can later resolve to different bytes.
- **B:** correct; the image digest identifies immutable image content.
- **C:** correct; enhanced ECR scanning integrates Amazon Inspector findings for packages and supported languages.
- **D:** incorrect; a workstation cache is neither a managed registry nor a deployable control.
- **E:** correct; ECR API/DKR interface endpoints plus the S3 gateway endpoint support private image pulls.
- **F:** incorrect; administrator access violates least privilege and does not solve the three requirements.
- **Reusable rule:** secure private image delivery combines digest pinning, managed scanning, and the service endpoints used by the pull path.
- **Lessons:** 203–205.
- **Reference:** [Amazon ECR VPC endpoints](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html).

## B16-10 — Answer C

- **Central requirement:** bound asynchronous failure handling, retain recoverable failed events, create operational visibility, and enforce log retention.
- **Decisive words:** *asynchronously*, *bound retry age*, *preserve exhausted events*, *30 days*.
- **A:** EventBridge archives can aid replay, but disabling retries and relying on log discovery leaves no automatic durable terminal-failure route or prompt alert.
- **B:** an SQS buffer can be a valid alternative architecture, but the proposed incomplete design omits stated correctness, observability, retention, and log-lifecycle requirements.
- **C:** correct; native asynchronous controls bound attempts and age, a destination or DLQ preserves failures, alarms expose the condition, and log retention controls storage duration.
- **D:** email per error is not a durable failed-event store, and indefinite retries/log retention fail the bounded-age and lifecycle requirements.
- **Reusable rule:** asynchronous Lambda reliability combines retry/age limits, durable failure routing, alarms, idempotency, and explicit log retention.
- **Lessons:** 203–214.
- **Reference:** [Handling errors for asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-error-handling.html) and [CloudWatch Logs retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html).
- **Common trap:** assuming Lambda retries provide indefinite durable storage or operational alerting by themselves.

## Ação após a correção

Registre todo erro ou acerto de baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), com cálculo ou regra reutilizável.
