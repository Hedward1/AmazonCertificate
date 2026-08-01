# B11 — Gabarito comentado

Abra depois das [questões B11](B11_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B11-01 | B | 1.1 |
| B11-02 | C | 2.2 |
| B11-03 | A | 2.2 |
| B11-04 | D | 4.1 |
| B11-05 | B | 3.1 |
| B11-06 | C | 4.1 |
| B11-07 | A | 3.5 |
| B11-08 | D | 4.1 |
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

## B11-03 — Resposta A

- **Requisito central:** replicar objetos existentes antes da regra live.
- **Palavras decisivas:** *cinco anos anteriores*, *CRR hoje*.
- **A:** correta; Batch Replication processa inventory/history elegível.
- **B:** live replication não copia retroativamente tudo por padrão.
- **C:** EFS muda interface e não executa CRR.
- **D:** DNS Alias não copia objetos.
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
- **Palavras decisivas:** *duplicates*, *exactly once business perspective*.
- **A:** correct; idempotency state prevents repeated side effects and queue/DLQ
  improves buffering/recovery.
- **B:** notifications can duplicate and ordering is not universally guaranteed.
- **C:** versioning does not change delivery semantics.
- **D:** public access is unrelated and unsafe.
- **Regra reutilizável:** at-least-once event → idempotent consumer.
- **Variação:** filter input/output prefixes to prevent recursive Lambda loops.
- **Aulas:** 145–146.
- **Referência:** [S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html).

## B11-08 — Answer D

- **Requisito central:** allocate request/transfer charges to data consumers.
- **Palavras decisivas:** *Requester Pays*, *who pays storage*.
- **A:** bucket owner keeps paying storage.
- **B:** requester must authenticate and acknowledge payer behavior.
- **C:** applicable requester charges move when correctly requested.
- **D:** correct; requester pays requests/transfer while owner pays storage.
- **Regra reutilizável:** Requester Pays transfers access cost, not ownership or
  storage cost.
- **Variação:** bucket policies/permissions still apply; it is not public access.
- **Aulas:** 144.
- **Referência:** [Requester Pays](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html).

## B11-09 — Answer B

- **Requisito central:** execute one managed action over billions of objects.
- **Palavras decisivas:** *manifest*, *progress*, *completion report*.
- **A:** workstation loop lacks managed scale, retries and reporting.
- **B:** correct; Batch Operations creates tracked jobs over manifest objects.
- **C:** DNS routing cannot tag storage objects.
- **D:** S3 is not attached as an EBS volume.
- **Regra reutilizável:** bulk action over massive object set → S3 Batch
  Operations.
- **Variação:** review IAM role, manifest correctness, job report, priority and
  confirmation before running a mutating job.
- **Aulas:** 148.
- **Referência:** [S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html).

## B11-10 — Answer C

- **Requisito central:** gain aggregated storage usage/activity insights.
- **Palavras decisivas:** *account-wide*, *noncurrent versions*, *without content*.
- **A:** Instance Connect provides EC2 access.
- **B:** RDS Proxy pools database connections.
- **C:** correct; Storage Lens supplies storage metrics/dashboards by scope/tier.
- **D:** GWLB distributes virtual appliances.
- **Regra reutilizável:** S3 organization/account storage visibility → Storage
  Lens.
- **Variação:** advanced metrics/recommendations and exports may add cost; Lens
  does not inspect object contents.
- **Aulas:** 149.
- **Referência:** [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html).

## Ação após a correção

Classifique erros em access, versions, replication, class/lifecycle, events ou
operations. Registre no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md) a
palavra decisiva, a regra e como o cleanup mudaria em bucket versionado.
