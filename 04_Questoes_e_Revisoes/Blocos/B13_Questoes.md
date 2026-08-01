# B13 — Questões

**Formato:** 10 questões autorais, uma resposta correta<br>
**Idioma:** 4 em português e 6 em inglês<br>
**Aulas:** 172–181<br>
**Tarefas:** 3.1 e 3.5

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma |
|---|---:|---:|---|---|
| B13-01 | 3 | 3.1 | 175–176 | Português |
| B13-02 | 3 | 3.1 | 175–176 | Português |
| B13-03 | 3 | 3.5 | 180 | Português |
| B13-04 | 3 | 3.5 | 172–174 | Português |
| B13-05 | 3 | 3.1 | 177–178 | Inglês |
| B13-06 | 3 | 3.5 | 179 | Inglês |
| B13-07 | 3 | 3.1 | 177–178 | Inglês |
| B13-08 | 3 | 3.1 | 175–176 | Inglês |
| B13-09 | 3 | 3.1 | 181 | Inglês |
| B13-10 | 3 | 3.5 | 177–180 | Inglês |

### B13-01

Uma empresa executa aplicações Windows que exigem SMB, ACLs NTFS e integração
com Microsoft Active Directory. Qual storage gerenciado atende melhor?

- A. Amazon EFS
- B. Amazon S3 Glacier Deep Archive
- C. Amazon EC2 instance store
- D. Amazon FSx for Windows File Server

### B13-02

Uma aplicação de HPC precisa processar em paralelo um grande dataset no S3 e
gravar o resultado de volta com throughput muito alto. Qual escolha é adequada?

- A. FSx for Lustre ligado ao S3
- B. Tape Gateway
- C. Transfer Family com SFTP
- D. FSx for Windows com SMB

### B13-03

Uma empresa quer copiar milhões de arquivos de NFS on-premises para S3 pela
rede, com agendamento, verificação e automação. Qual serviço usar?

- A. AWS Direct Connect sem software de transferência
- B. S3 File Gateway como única tarefa de cópia
- C. AWS DataSync
- D. Amazon SNS

Considere que o link de rede já existe e que a empresa procura o serviço que
executa a movimentação, não apenas conectividade.

### B13-04

Um novo cliente AWS em 2026 planeja solicitar Snowball Edge para uma migração.
Qual fato deve mudar a avaliação?

- A. Snowball aceita apenas arquivos menores que 5 GB
- B. Nenhum dispositivo Snow Family está disponível para novos clientes
- C. Snowball funciona somente dentro de uma VPC
- D. Snowball exige FSx for Windows como destino

### B13-05

A backup application can write only to an iSCSI virtual tape library. The
company wants cloud-backed virtual tapes and archival storage. What should it
deploy?

- A. S3 File Gateway
- B. Volume Gateway cached mode
- C. Tape Gateway
- D. AWS Transfer Family

### B13-06

Business partners must continue using SFTP while uploaded files are stored in
Amazon S3. The company does not want to manage SFTP servers. Which service fits?

- A. AWS Transfer Family
- B. AWS DataSync
- C. Amazon FSx for Lustre
- D. Amazon EBS Multi-Attach

### B13-07

An on-premises application needs low-latency access to frequently used blocks
through iSCSI, while the primary data is stored in AWS. Which gateway mode is
appropriate?

- A. Stored Volume Gateway
- B. Cached Volume Gateway
- C. S3 File Gateway
- D. Tape Gateway

### B13-08

A company migrating NetApp workloads requires NFS, SMB, iSCSI, snapshots,
clones, and familiar ONTAP features. Which file system should it choose?

- A. Amazon EFS One Zone
- B. Amazon FSx for NetApp ONTAP
- C. Amazon FSx for Lustre scratch
- D. Amazon S3 Standard

### B13-09

An application needs a shared, elastic NFS file system for Linux instances
across multiple Availability Zones. It has no specialized Lustre or ZFS
requirements. Which service is the simplest fit?

- A. Amazon EFS
- B. Amazon EBS
- C. Amazon S3 Glacier Flexible Retrieval
- D. AWS Transfer Family

### B13-10

Which statement correctly distinguishes DataSync from Storage Gateway?

- A. DataSync provides a persistent iSCSI interface; Storage Gateway only copies files once.
- B. DataSync automates data transfer tasks; Storage Gateway exposes hybrid storage interfaces to applications.
- C. Both services require a physical Snow device.
- D. Storage Gateway is used only for SFTP partner endpoints.

## Registro

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B13-01 |  |  |  |
| B13-02 |  |  |  |
| B13-03 |  |  |  |
| B13-04 |  |  |  |
| B13-05 |  |  |  |
| B13-06 |  |  |  |
| B13-07 |  |  |  |
| B13-08 |  |  |  |
| B13-09 |  |  |  |
| B13-10 |  |  |  |

Depois consulte [B13 — Gabarito](B13_Gabarito.md).
