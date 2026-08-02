# B11 — Gabarito comentado

Abra depois das [questões B11](B11_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B11-01 | B | 1.1 |
| B11-02 | C | 2.2 |
| B11-03 | A,C | 2.2 |
| B11-04 | D | 4.1 |
| B11-05 | B | 3.1 |
| B11-06 | C | 4.1 |
| B11-07 | A | 3.5 |
| B11-08 | A,D | 4.1 |
| B11-09 | B | 3.1 |
| B11-10 | C | 3.1 |

## B11-01 — Resposta B

- **Requisito central:** conceder acesso mínimo a um prefixo mantendo bucket
  privado.
- **Palavras decisivas:** *role*, *somente tenant-a*, *privado*.
- **A:** policy pública e BPA desligado violam menor privilégio.
- **B:** correta; `ListBucket` usa bucket ARN/condition e `GetObject` usa object
  ARN do prefixo.
- **C:** website exige outro modelo de acesso e não limita a role.
- **D:** ACL pública expõe dados e é desnecessária com bucket owner enforced.
- **Regra reutilizável:** separar actions de bucket e object ARNs; principal
  específico, sem acesso público.
- **Variação:** Block Public Access, um SCP ou um `Deny` explícito aplicável
  ainda podem bloquear o request apesar de um `Allow`.
- **Aulas:** 130–131.
- **Referência:** [Policy actions/resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html).

## B11-02 — Resposta C

- **Requisito central:** recuperar uma key escondida por delete marker.
- **Palavras decisivas:** *versionado*, *DELETE sem version ID*, *recuperar*.
- **A:** EBS não contém versions S3.
- **B:** suspensão não remove marker nem restaura automaticamente.
- **C:** correta; remover o marker current revela a versão anterior.
- **D:** Requester Pays altera cobrança de requests, não version history.
- **Regra reutilizável:** delete comum em bucket versionado → marker; remova o
  marker correto para undelete.
- **Variação:** excluir uma version ID de dados é permanente e requer cautela.
- **Aulas:** 134–135.
- **Referência:** [Delete markers](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html).

## B11-03 — Resposta A,C

- **Requisito central:** replicar objetos existentes antes da regra live.
- **Palavras decisivas:** *cinco anos anteriores*, *CRR hoje*.
- **A:** correta; a regra live processa novos objetos elegíveis.
- **B:** live replication não copia retroativamente todo o histórico por padrão.
- **C:** correta; Batch Replication processa os objetos existentes elegíveis.
- **D:** EFS muda a interface de armazenamento e não executa CRR.
- **E:** DNS Alias não copia objetos.
- **Regra reutilizável:** new objects → replication rule; existing → Batch
  Replication.
- **Variação:** source/destination versioning, IAM role e KMS permissions ainda
  são necessários.
- **Aulas:** 136–138 e 148.
- **Referência:** [Replicating existing objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-for-existing-objects.html).

## B11-04 — Resposta D

- **Requisito central:** arquivo raro, ms e resiliência à perda de AZ.
- **Palavras decisivas:** *única cópia*, *poucas vezes*, *milissegundos*.
- **A:** One Zone-IA aceita failure domain de uma AZ.
- **B:** Express é single-AZ e otimiza performance, não arquivo regulatório.
- **C:** instance store é efêmero e ligado ao host.
- **D:** correta; Glacier Instant Retrieval oferece acesso em ms e design
  Multi-AZ, considerando minimum duration/retrieval.
- **Regra reutilizável:** rare archive + immediate access → Glacier Instant;
  valide custo e retenção.
- **Variação:** Flexible/Deep Archive reduzem custo, mas exigem restore em
  minutos/horas.
- **Aulas:** 139–140.
- **Referência:** [S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html).

## B11-05 — Answer B

- **Requisito central:** highest-performance object access in one accepted AZ.
- **Palavras decisivas:** *single-digit milliseconds*, *accepts single AZ*.
- **A:** Deep Archive has hours-scale restore workflows.
- **B:** correct; Express One Zone uses directory buckets for latency-sensitive
  high-request workloads.
- **C:** Standard-IA is for infrequent access, not the highest-performance tier.
- **D:** snapshot archive is EBS recovery storage, not an S3 serving class.
- **Regra reutilizável:** extreme S3 performance + zonal placement accepted →
  Express One Zone.
- **Variação:** validate directory-bucket API, naming, endpoint and feature
  differences before migration.
- **Aulas:** 141.
- **Referência:** [S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-one-zone.html).

## B11-06 — Answer C

- **Requisito central:** stop retained versions/multipart from growing cost.
- **Palavras decisivas:** *versioned*, *current expires*, *old versions remain*.
- **A:** public ACL adds exposure and does not delete history.
- **B:** MX is a DNS mail record.
- **C:** correct; noncurrent expiration and multipart cleanup address residues.
- **D:** load-balancer draining has no effect on S3 versions.
- **Regra reutilizável:** versioned lifecycle must separately cover current,
  noncurrent, markers and multipart.
- **Variação:** retention/compliance and minimum storage duration must be checked
  before aggressive expiration.
- **Aulas:** 142–143.
- **Referência:** [Lifecycle and versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-and-other-bucket-config.html).

## B11-07 — Answer A

- **Requisito central:** achieve business-level exactly-once effects over
  at-least-once notification delivery.
- **Palavras decisivas:** *duplicate event*, *second ledger entry*, *commit*,
  *visibility timeout*, *dead-letter path*.
- **A:** correct; a conditional write on a stable idempotency key prevents a
  repeated business side effect, acknowledgement after commit avoids message
  loss, and visibility/DLQ settings handle worker and poison-message failures.
- **B:** FIFO ordering or transport deduplication alone does not make an
  unconditional downstream database side effect exactly once across every
  retry and failure boundary.
- **C:** a visibility timeout shorter than processing makes concurrent redelivery
  more likely before the first worker commits.
- **D:** deleting the message before the transaction creates an
  acknowledgement-before-commit loss window; S3 versioning does not replay that
  deleted queue message automatically.
- **Regra reutilizável:** at-least-once event → durable idempotency key + commit
  side effect before acknowledgement + retry/DLQ policy.
- **Variação:** an outbox or transactional workflow can coordinate additional
  downstream effects after the idempotent ledger commit.
- **Aulas:** 145–146.
- **Referência:** [S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html).

## B11-08 — Answer A,D

- **Requisito central:** allocate private cross-account dataset access costs to
  authenticated consumers without changing ownership or authorization.
- **Palavras decisivas:** *approved principals*, *consumer account pays requests
  and transfer*, *owner pays stored capacity*, *anonymous prohibited*.
- **A:** correct; acknowledgement on an authenticated applicable request lets S3
  assign requester-borne charges to the requester account.
- **B:** anonymous access cannot identify an authenticated requester account and
  is not a supported way to allocate Requester Pays charges.
- **C:** Requester Pays neither transfers bucket ownership nor moves the owner's
  storage-capacity charges.
- **D:** correct; applicable request and transfer charges shift to the requester,
  while storage remains charged to the bucket owner.
- **E:** IAM and bucket authorization are still evaluated; Requester Pays is a
  billing feature, not an access grant.
- **Regra reutilizável:** Requester Pays transfers eligible access cost, not
  ownership, storage cost, or authorization responsibility.
- **Variação:** a data exchange requiring subscription, entitlement, or product
  publication should be evaluated separately from this S3 billing control.
- **Aulas:** 144.
- **Referência:** [Requester Pays](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html).

## B11-09 — Answer B

- **Requisito central:** execute an auditable, least-privilege mutation over a
  reviewed inventory of billions of objects without a workstation dependency.
- **Palavras decisivas:** *S3 Inventory*, *reviewed manifest*, *managed retries*,
  *progress*, *completion report*.
- **A:** a custom Distributed Map can be engineered to call the tagging API, but
  the team must build and operate status, throttling, retry, and audit-report
  behavior that S3 Batch Operations provides for this native bulk action.
- **B:** correct; Batch Operations consumes the manifest, assumes a scoped IAM
  role, tracks the managed job, and can write a completion report.
- **C:** a custom ECS fleet is technically capable of calling the tagging API,
  but it adds bespoke sharding, checkpointing, retry, throttling, and reporting
  operations despite the purpose-built managed service requirement.
- **D:** Batch Replication copies eligible objects; it does not apply an
  arbitrary compliance tag in place to the selected source objects.
- **Regra reutilizável:** governed bulk action over a massive object set →
  reviewed manifest + scoped role + S3 Batch Operations job/report.
- **Variação:** require confirmation before a destructive operation and retain
  the source manifest and completion report as change evidence.
- **Aulas:** 148.
- **Referência:** [S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html).

## B11-10 — Answer C

- **Requisito central:** centralize organization-level S3 usage, activity,
  version, and optimization metrics without inspecting object payloads.
- **Palavras decisivas:** *Organizations*, *aggregated visibility*, *noncurrent
  versions*, *managed dashboards*, *without object contents*.
- **A:** Instance Connect is an EC2 access mechanism and cannot aggregate S3
  storage governance metrics.
- **B:** RDS Proxy pools relational database connections; it is not placed in
  front of S3 buckets.
- **C:** correct; Storage Lens provides managed dashboards and metrics at
  configured scopes and tiers, including organization-wide administration when
  configured appropriately.
- **D:** Gateway Load Balancer distributes network appliances and would not
  provide the requested S3 storage analytics.
- **Regra reutilizável:** S3 organization/account storage visibility and
  recommendations → Storage Lens with the required scope, tier, and delegation.
- **Variação:** advanced metrics, recommendations, and metrics exports can add
  cost; evaluate them separately from standard metrics.
- **Aulas:** 149.
- **Referência:** [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html).

## Ação após a correção

Classifique erros em access, versions, replication, class/lifecycle, events ou
operations. Registre no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md) a
palavra decisiva, a regra e como o cleanup mudaria em bucket versionado.
