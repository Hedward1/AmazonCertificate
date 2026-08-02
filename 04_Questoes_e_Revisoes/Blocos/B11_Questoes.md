# B11 — Questões: Amazon S3 básico e avançado

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 4 em português e 6 em inglês<br>
**Formato:** questões single-answer e multi-answer; siga a instrução de cada questão<br>
**Tempo:** 15 minutos<br>
**Gabarito:** [arquivo separado](B11_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B11-01 | 1.1 | Bucket policy/BPA | single | fundamental | básica | Português |
| B11-02 | 2.2 | Versioning | single | fundamental | básica | Português |
| B11-03 | 2.2 | Replication existente | multi-2 | integrada | avançada | Português |
| B11-04 | 4.1 | Storage classes | single | situacional | intermediária | Português |
| B11-05 | 3.1 | Express One Zone | single | situacional | intermediária | Inglês |
| B11-06 | 4.1 | Lifecycle versioned | single | situacional | intermediária | Inglês |
| B11-07 | 3.5 | Event notification | single | integrada | avançada | Inglês |
| B11-08 | 4.1 | Requester Pays | multi-2 | integrada | avançada | Inglês |
| B11-09 | 3.1 | Batch Operations | single | integrada | avançada | Inglês |
| B11-10 | 3.1 | Storage Lens | single | situacional | intermediária | Inglês |

## Questões

### B11-01

Uma role deve listar somente `tenant-a/` e ler objetos desse prefixo. O bucket
deve permanecer privado.

- A. Desabilitar Block Public Access e permitir `Principal:*`.
- B. Conceder `ListBucket` no bucket condicionado ao prefix e `GetObject` em
  `bucket/tenant-a/*` à role.
- C. Criar website público.
- D. Usar apenas uma ACL pública.

### B11-02

Em bucket versionado, um usuário executa DELETE sem version ID. O objeto deixa de
aparecer em GET normal, mas precisa ser recuperado.

- A. Restaurar EBS snapshot.
- B. Suspender versioning e recriar o bucket.
- C. Listar versions/delete markers e excluir o delete marker atual correto.
- D. Habilitar Requester Pays.

### B11-03

CRR foi habilitado hoje, mas cinco anos de objetos anteriores também precisam ser
replicados.

Quais ações atendem ao requisito?

**Choose TWO.**

- A. Manter uma regra de replicação live para os novos objetos elegíveis.
- B. Esperar que a nova regra live copie retroativamente todo o histórico sem
  outro processo.
- C. Usar S3 Batch Replication para processar os objetos existentes elegíveis.
- D. Converter o bucket em EFS para iniciar automaticamente a CRR.
- E. Criar um Alias record para copiar os objetos anteriores.

### B11-04

Uma única cópia de documentos regulatórios deve sobreviver à perda de uma AZ e é
acessada poucas vezes ao ano com recuperação em milissegundos.

- A. S3 One Zone-IA.
- B. S3 Express One Zone.
- C. Instance store.
- D. S3 Glacier Instant Retrieval, considerando duração/retrieval e preço.

### B11-05

A latency-sensitive analytics workload runs in one AZ and requires the highest
performance S3 object access with single-digit millisecond latency. It accepts
the single-AZ failure domain.

- A. S3 Glacier Deep Archive.
- B. S3 Express One Zone using a directory bucket.
- C. S3 Standard-IA is always faster.
- D. EBS snapshot archive.

### B11-06

A versioned bucket expires current objects, but storage cost keeps growing
because old versions remain. What should be added?

- A. A public-read ACL.
- B. An MX record.
- C. Lifecycle actions for noncurrent versions and incomplete multipart uploads,
  with retention requirements considered.
- D. A shorter ALB deregistration delay.

### B11-07

S3 `ObjectCreated` events are sent to an SQS queue. A retry or duplicate event
must not create a second invoice-ledger entry, and a failed worker must not lose
the event before the database commit. The queue requires a dead-letter path for
repeated failures.

Which design meets the requirements?

- A. Use the object key plus version or another business idempotency key in a
  conditional database write, delete the SQS message only after the transaction
  succeeds, and configure an appropriate visibility timeout and DLQ.
- B. Route events through EventBridge to an SQS FIFO queue as the only duplicate
  control and perform an unconditional ledger insert for every delivered
  message.
- C. Set the visibility timeout shorter than normal processing time so another
  worker receives the message before the first database transaction commits.
- D. Delete each SQS message before starting the ledger transaction, then rely
  on S3 versioning to recreate any event lost during worker failure.

### B11-08

A research organization owns a private S3 dataset that is shared with approved
principals in several AWS accounts. The owner will continue paying for stored
capacity, but each consumer account must pay applicable request and data-transfer
charges. Existing bucket policies and IAM authorization must remain in force,
and anonymous access is prohibited.

Which actions and billing effects are part of the correct design?

**Choose TWO.**

- A. Enable Requester Pays and require each authenticated consumer to acknowledge
  Requester Pays on applicable requests so AWS can identify the requester account.
- B. Permit anonymous downloads because S3 can infer the payer from the source IP
  address.
- C. Transfer bucket ownership and all stored-capacity charges to the requester
  automatically after its first request.
- D. Bill applicable request and data-transfer charges to the requester while the
  bucket owner continues paying the storage charges.
- E. Use Requester Pays as a replacement for bucket policies because it grants
  object access automatically.

### B11-09

A company must apply a compliance tag to two billion existing S3 objects selected
by an S3 Inventory report. The operation needs a reviewed manifest, least-
privilege execution role, managed retries, progress visibility, and a completion
report that auditors can retain. A workstation must not become the orchestration
or checkpointing dependency.

Which design meets the requirements with the least operational overhead?

- A. Build a Step Functions Distributed Map that invokes custom Lambda tagging
  code for every manifest row and implement separate status, retry, and audit-
  report stores.
- B. Create an S3 Batch Operations job from the reviewed manifest, assign an IAM
  role limited to the tagging action and selected objects, and enable the job
  completion report.
- C. Run a custom sharded ECS tagging fleet over the Inventory report and build
  its own throttling, checkpoint, retry, progress, and completion-report logic.
- D. Use S3 Batch Replication to copy the objects to another bucket and assume
  that replication applies the required tag to the existing source objects.

### B11-10

An AWS Organizations storage team needs aggregated visibility across approved
accounts and S3 buckets. It must identify growth in noncurrent versions, activity
patterns, and cost-optimization opportunities without opening or indexing object
contents. The team wants managed dashboards and metrics at the organization or
account scope instead of collecting per-object application logs itself.

Which design best meets the requirements?

- A. Use EC2 Instance Connect to log in to every application instance and sum the
  object sizes found in local configuration files.
- B. Put RDS Proxy in front of every bucket to aggregate S3 request and version
  metrics.
- C. Configure Amazon S3 Storage Lens at the appropriate organization/account
  scope and metrics tier, with delegated administration or export controls as
  required.
- D. Insert a Gateway Load Balancer in every S3 request path and inspect object
  payloads to calculate storage recommendations.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B11-01 | | | |
| B11-02 | | | |
| B11-03 | | | |
| B11-04 | | | |
| B11-05 | | | |
| B11-06 | | | |
| B11-07 | | | |
| B11-08 | | | |
| B11-09 | | | |
| B11-10 | | | |
