# B13 — Questões

**Formato:** 10 questões autorais, com itens single-answer e multi-answer; siga a instrução de cada questão<br>
**Idioma:** 4 em português e 6 em inglês<br>
**Aulas:** 172–181<br>
**Tarefas:** 3.1 e 3.5

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Formato | Tipo | Dificuldade | Idioma |
|---|---:|---:|---|---|---|---|---|
| B13-01 | 3 | 3.1 | 175–176 | single | fundamental | básica | Português |
| B13-02 | 3 | 3.1 | 175–176 | single | fundamental | básica | Português |
| B13-03 | 3 | 3.5 | 180 | multi-2 | integrada | avançada | Português |
| B13-04 | 3 | 3.5 | 172–174 | single | situacional | intermediária | Português |
| B13-05 | 3 | 3.1 | 177–178 | single | situacional | intermediária | Inglês |
| B13-06 | 3 | 3.5 | 179 | single | situacional | intermediária | Inglês |
| B13-07 | 3 | 3.1 | 177–178 | single | situacional | intermediária | Inglês |
| B13-08 | 3 | 3.1 | 175–176 | multi-2 | integrada | avançada | Inglês |
| B13-09 | 3 | 3.1 | 181 | single | situacional | intermediária | Inglês |
| B13-10 | 3 | 3.5 | 177–180 | single | situacional | intermediária | Inglês |

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
rede, com agendamento, verificação e automação. Quais componentes devem ser
configurados?

**Choose TWO.**

- A. Usar apenas AWS Direct Connect, sem um serviço de transferência.
- B. Configurar um AWS DataSync agent com acesso ao NFS on-premises e criar as
  locations de origem e destino.
- C. Usar S3 File Gateway como uma tarefa única que verifica toda a migração.
- D. Criar uma DataSync task com agendamento, opções de verificação e a IAM role
  necessária para o destino S3.
- E. Publicar os caminhos dos arquivos em um tópico do Amazon SNS.

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

**Choose TWO.**

- A. Amazon EFS One Zone supplies the requested ONTAP administration model and
  iSCSI.
- B. Amazon FSx for NetApp ONTAP supports NFS, SMB, and iSCSI access.
- C. Amazon FSx for Lustre scratch preserves ONTAP volumes and multiprotocol
  access.
- D. FSx for ONTAP provides familiar ONTAP features such as snapshots and
  clones.
- E. Amazon S3 Standard exposes the required ONTAP block and file protocols.

### B13-09

A fleet of Linux EC2 instances scales across three Availability Zones and must
mount the same POSIX file hierarchy. Instances are replaced frequently, capacity
must grow and shrink without pre-provisioning, and the team does not need Lustre,
ONTAP, OpenZFS, SMB, or application changes to an object API.

Which storage design is the simplest operational fit?

- A. Mount a Regional Amazon EFS file system from the instances in each
  Availability Zone, using appropriate mount targets and network controls.
- B. Attach one zonal Amazon EBS volume simultaneously to arbitrary instances in
  all three Availability Zones as a general-purpose NFS service.
- C. Mount S3 Glacier Flexible Retrieval directly as a low-latency POSIX file
  system for active application writes.
- D. Use AWS Transfer Family as the shared kernel-mounted NFS storage layer for
  the EC2 fleet.

### B13-10

A company has two hybrid requirements. First, it must perform scheduled,
verified transfers of millions of files from on premises to Amazon S3 with
incremental runs and managed task reporting. Second, a legacy application must
continue using a familiar NFS or iSCSI interface while data is integrated with
AWS storage. The architect must select different services according to movement
versus persistent interface semantics.

Which statement maps the services correctly?

- A. AWS DataSync provides the persistent iSCSI application interface, while
  Storage Gateway only performs one-time file-copy tasks.
- B. AWS DataSync automates and verifies data-transfer tasks, while AWS Storage
  Gateway exposes supported hybrid storage interfaces to applications.
- C. Both services require a physical Snow device to operate, even when the
  network path has sufficient capacity.
- D. Storage Gateway is only an SFTP partner endpoint and cannot expose file or
  volume storage interfaces.

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
