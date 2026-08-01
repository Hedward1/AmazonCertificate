# B16 — Gabarito comentado

Abra somente depois das [questões B16](B16_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B16-01 | A | 3.2 |
| B16-02 | C | 3.2 |
| B16-03 | B | 3.2 |
| B16-04 | D | 3.2 |
| B16-05 | A | 3.2 |
| B16-06 | C | 3.2 |
| B16-07 | B | 3.2 |
| B16-08 | D | 3.2 |
| B16-09 | A | 1.2 |
| B16-10 | C | 4.2 |

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

## B16-04 — Answer D

- **Central requirement:** prevent Lambda scale from exhausting database connections.
- **Decisive words:** *80 connections*, *bursts*, *far beyond*.
- **A:** memory may change speed but does not directly cap concurrency.
- **B:** a public URL adds exposure and no connection protection.
- **C:** cache behaviors do not cap Lambda database use in this scenario.
- **D:** correct; cap concurrency, buffer bursts, and pool through RDS Proxy where suitable.
- **Reusable rule:** fragile downstream → bound concurrency and decouple/buffer.
- **Lessons:** 213–214.
- **Reference:** [Reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html).
- **Common trap:** using provisioned concurrency as a maximum.

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

## B16-07 — Answer B

- **Central requirement:** extremely lightweight viewer-request manipulation without network access.
- **Decisive words:** *URL rewrite*, *header*, *no network call*.
- **A:** MQ is a broker.
- **B:** correct; CloudFront Functions is optimized for lightweight viewer logic.
- **C:** ECS is unnecessary and not executed at CloudFront edge events.
- **D:** regional Lambda with NAT adds cost and latency and is not the direct edge option.
- **Reusable rule:** simple high-scale viewer logic → CloudFront Functions.
- **Lessons:** 216.
- **Reference:** [Edge functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions.html).
- **Common trap:** choosing Lambda@Edge for a simple rewrite.

## B16-08 — Answer D

- **Central requirement:** a managed Kubernetes control plane.
- **Decisive words:** *Kubernetes APIs*, *tooling*, *managed control plane*.
- **A:** ECS is AWS container orchestration without Kubernetes API.
- **B:** Lambda is function compute.
- **C:** ECR is an image registry.
- **D:** correct; EKS provides managed Kubernetes.
- **Reusable rule:** explicit Kubernetes requirement → EKS.
- **Lessons:** 206–207.
- **Reference:** [What is EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html).
- **Common trap:** forgetting control-plane and worker cost.

## B16-09 — Answer A

- **Central requirement:** reference immutable tested image content.
- **Decisive words:** *exact*, *even if tag is moved*.
- **A:** correct; a digest identifies the content and immutable-tag controls reduce accidents.
- **B:** `latest` is mutable and ambiguous.
- **C:** registry credentials must not be embedded in deployments.
- **D:** a console URL is not an image reference.
- **Reusable rule:** reproducible release → image digest/immutable versioning.
- **Lessons:** 205.
- **Reference:** [ECR image details](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-detail.html).
- **Common trap:** treating a mutable tag as content identity.

## B16-10 — Answer C

- **Central requirement:** complete cleanup after deleting a function.
- **Decisive words:** *deleted*, *remains*, *separate cleanup*.
- **A:** a Region cannot be deleted.
- **B:** the managed runtime is not a customer resource.
- **C:** correct; log groups, roles, event mappings and related resources can remain.
- **D:** the service control plane is AWS-managed.
- **Reusable rule:** resource deletion does not imply dependency/log deletion; inventory explicitly.
- **Lessons:** 203–214.
- **Reference:** [Lambda monitoring](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html).
- **Common trap:** checking only the Lambda console after cleanup.

## Ação após a correção

Registre todo erro ou acerto de baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), com cálculo ou regra reutilizável.
