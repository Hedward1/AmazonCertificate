# B11 — Questões: Amazon S3 básico e avançado

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 4 em português e 6 em inglês<br>
**Tempo:** 15 minutos<br>
**Gabarito:** [arquivo separado](B11_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B11-01 | 1.1 | Bucket policy/BPA | Situacional | Intermediária | Português |
| B11-02 | 2.2 | Versioning | Situacional | Básica | Português |
| B11-03 | 2.2 | Replication existente | Situacional | Intermediária | Português |
| B11-04 | 4.1 | Storage classes | Situacional | Intermediária | Português |
| B11-05 | 3.1 | Express One Zone | Situacional | Intermediária | Inglês |
| B11-06 | 4.1 | Lifecycle versioned | Situacional | Avançada | Inglês |
| B11-07 | 3.5 | Event notification | Situacional | Intermediária | Inglês |
| B11-08 | 4.1 | Requester Pays | Fundamental | Intermediária | Inglês |
| B11-09 | 3.1 | Batch Operations | Situacional | Básica | Inglês |
| B11-10 | 3.1 | Storage Lens | Situacional | Básica | Inglês |

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

- A. Usar S3 Batch Replication para objetos existentes, além da regra live.
- B. Esperar a regra copiar retroativamente todo histórico.
- C. Converter o bucket em EFS.
- D. Criar Alias record.

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

S3 event notifications can occasionally deliver duplicates. A worker processes
uploaded invoices exactly once from a business perspective.

- A. Make processing idempotent using object/version/event identity and store
  completion state; use queue/DLQ as required.
- B. Assume every notification is unique and ordered.
- C. Disable versioning to guarantee delivery.
- D. Open the bucket publicly.

### B11-08

Which statement describes S3 Requester Pays?

- A. The requester pays bucket storage and owns the bucket.
- B. Anonymous users can download without identifying a payer.
- C. The bucket owner pays every request forever.
- D. An authenticated requester acknowledges payment for applicable requests
  and transfer, while the bucket owner still pays storage.

### B11-09

A company must apply tags to two billion existing S3 objects using a managed job,
manifest, progress tracking and completion report.

- A. Run a single workstation loop without checkpointing.
- B. Use S3 Batch Operations with the required manifest and IAM role.
- C. Use Route 53 weighted routing.
- D. Attach the bucket as EBS Multi-Attach.

### B11-10

An organization wants account-wide visibility into storage usage, activity,
noncurrent versions and cost-optimization opportunities without reading object
contents.

- A. EC2 Instance Connect.
- B. RDS Proxy.
- C. S3 Storage Lens dashboards/metrics at the appropriate scope and tier.
- D. A Gateway Load Balancer.

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
