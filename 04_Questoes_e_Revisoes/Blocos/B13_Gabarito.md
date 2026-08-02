# B13 — Gabarito comentado

Corrija somente após responder às [questões B13](B13_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B13-01 | D | 3.1 |
| B13-02 | A | 3.1 |
| B13-03 | B,D | 3.5 |
| B13-04 | B | 3.5 |
| B13-05 | C | 3.1 |
| B13-06 | A | 3.5 |
| B13-07 | B | 3.1 |
| B13-08 | B,D | 3.1 |
| B13-09 | A | 3.1 |
| B13-10 | B | 3.5 |

## B13-01 — Resposta D

- **Requisito central:** filesystem gerenciado com SMB, NTFS e Active Directory.
- **Palavras decisivas:** *Windows*, *SMB*, *ACLs NTFS*, *AD*.
- **A:** EFS oferece NFS para workloads Linux e não a semântica Windows solicitada.
- **B:** Glacier Deep Archive é uma classe de objetos para arquivo, não um share.
- **C:** instance store é efêmero e não é um filesystem compartilhado gerenciado.
- **D:** correta; FSx for Windows oferece SMB e integrações Windows/AD.
- **Regra reutilizável:** Windows file share + AD → FSx for Windows File Server.
- **Aulas:** 175–176.
- **Referência:** [FSx for Windows](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html).
- **Erro comum:** escolher EFS apenas porque ambos são “file storage”.

## B13-02 — Resposta A

- **Requisito central:** filesystem paralelo de alto throughput integrado ao S3.
- **Palavras decisivas:** *HPC*, *processar em paralelo*, *dataset S3*.
- **A:** correta; FSx for Lustre atende computação paralela e pode ligar datasets do S3.
- **B:** Tape Gateway emula fitas para software de backup.
- **C:** Transfer Family oferece endpoints de protocolos de transferência.
- **D:** FSx for Windows prioriza SMB e workloads Windows, não Lustre/HPC.
- **Regra reutilizável:** HPC/ML sobre dataset S3 → FSx for Lustre.
- **Aulas:** 175–176.
- **Referência:** [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html).
- **Erro comum:** escolher S3 sozinho quando a aplicação requer filesystem paralelo.

## B13-03 — Resposta B,D

- **Requisito central:** copiar arquivos online com agendamento, automação e verificação.
- **Palavras decisivas:** *milhões de arquivos*, *NFS*, *agendamento*, *verificação*.
- **A:** Direct Connect fornece conectividade, mas não é o motor de cópia.
- **B:** correta; o agent acessa o NFS on-premises, e as locations descrevem a
  origem e o destino S3.
- **C:** S3 File Gateway mantém uma interface híbrida em vez de ser uma tarefa
  de migração com verificação.
- **D:** correta; a DataSync task executa, agenda e verifica a transferência com
  as permissões necessárias.
- **E:** SNS é pub/sub e não copia arquivos.
- **Regra reutilizável:** transferência online recorrente ou planejada → DataSync.
- **Aulas:** 180.
- **Referência:** [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html).
- **Erro comum:** confundir o caminho de rede com a ferramenta que move os dados.

## B13-04 — Resposta B

- **Requisito central:** validar a disponibilidade para uma nova conta em 2026.
- **Palavras decisivas:** *novo cliente*, *2026*, *solicitar Snowball*.
- **A:** tamanho de arquivo não é a mudança comercial determinante.
- **B:** correta; novos clientes não podem solicitar dispositivos Snow Family.
- **C:** Snowball não é um recurso que funciona apenas dentro de uma VPC.
- **D:** não há requisito geral de FSx for Windows como destino.
- **Regra reutilizável:** novo cliente → DataSync online; para bulk físico, validar Terminal/parceiros atuais.
- **Aulas:** 172–174.
- **Referência:** [Snowball Edge availability change](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html).
- **Erro comum:** aplicar automaticamente uma recomendação histórica do curso.

## B13-05 — Answer C

- **Central requirement:** preserve an iSCSI virtual tape library workflow.
- **Decisive words:** *backup application*, *VTL*, *archive*.
- **A:** S3 File Gateway presents files over NFS or SMB.
- **B:** cached Volume Gateway presents block volumes, not tape devices.
- **C:** correct; Tape Gateway emulates a VTL and supports cloud-backed archival.
- **D:** Transfer Family exposes file-transfer protocols, not iSCSI tape drives.
- **Reusable rule:** legacy backup software + VTL → Tape Gateway.
- **Lessons:** 177–178.
- **Reference:** [Tape Gateway](https://docs.aws.amazon.com/storagegateway/latest/tgw/WhatIsStorageGateway.html).
- **Common trap:** selecting S3 directly although the backup software requires tape semantics.

## B13-06 — Answer A

- **Central requirement:** managed partner SFTP endpoints backed by S3.
- **Decisive words:** *partners*, *SFTP*, *no servers*.
- **A:** correct; Transfer Family provides managed protocol endpoints and AWS storage backends.
- **B:** DataSync moves datasets but is not a multiuser SFTP server.
- **C:** FSx for Lustre is a high-performance filesystem.
- **D:** EBS Multi-Attach is a block-storage attachment feature.
- **Reusable rule:** SFTP/FTPS/FTP/AS2 endpoint → AWS Transfer Family.
- **Lessons:** 179.
- **Reference:** [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html).
- **Common trap:** using DataSync whenever the word “transfer” appears.

## B13-07 — Answer B

- **Central requirement:** cloud-primary iSCSI block storage with a local working set.
- **Decisive words:** *primary in AWS*, *local cache*, *iSCSI*.
- **A:** stored mode retains the primary dataset on premises and backs it up to AWS.
- **B:** correct; cached volumes retain frequently accessed blocks locally while primary data is in AWS.
- **C:** S3 File Gateway exposes a file interface rather than block volumes.
- **D:** Tape Gateway exposes virtual tapes for backup applications.
- **Reusable rule:** cloud-primary block data + local cache → cached Volume Gateway.
- **Lessons:** 177–178.
- **Reference:** [Volume Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html).
- **Common trap:** reversing cached and stored modes.

## B13-08 — Answer B,D

- **Central requirement:** preserve NetApp ONTAP and multiprotocol features.
- **Decisive words:** *NetApp*, *NFS/SMB/iSCSI*, *snapshots*, *clones*.
- **A:** EFS supplies NFS but not the requested ONTAP capabilities.
- **B:** correct; FSx for NetApp ONTAP supports the requested NFS, SMB, and iSCSI
  access.
- **C:** FSx for Lustre targets parallel compute and HPC.
- **D:** correct; it preserves familiar ONTAP capabilities such as snapshots and
  clones.
- **E:** S3 is object storage rather than a multiprotocol ONTAP filesystem.
- **Reusable rule:** NetApp migration or ONTAP features → FSx for NetApp ONTAP.
- **Variation:** choose another FSx engine only when its workload and protocol
  model match the requirement.
- **Lessons:** 175–176.
- **Reference:** [FSx for ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html).
- **Common trap:** choosing an FSx family without matching its engine and protocol.

## B13-09 — Answer A

- **Central requirement:** provide one elastic POSIX namespace to disposable Linux
  instances across Availability Zones without a specialized file-system engine.
- **Decisive words:** *same POSIX hierarchy*, *three AZs*, *instances replaced*,
  *without pre-provisioning*, *no specialized engine*.
- **A:** correct; Regional EFS supplies managed, elastic NFS access through mount
  targets in the VPC Availability Zones and decouples files from instance life.
- **B:** EBS is zonal block storage and is not a general cross-AZ shared NFS
  namespace for an arbitrary fleet.
- **C:** Glacier Flexible Retrieval is an archival S3 storage class, not an active
  low-latency POSIX file system.
- **D:** Transfer Family exposes managed transfer endpoints; it does not become
  the EC2 fleet's shared kernel-mounted NFS storage layer.
- **Reusable rule:** shared elastic Regional NFS for a changing Linux fleet → EFS
  plus mount targets and network authorization in the required AZs.
- **Variation:** specialized protocol or workload requirements can shift the
  decision to the matching FSx engine.
- **Lessons:** 181.
- **Reference:** [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html).
- **Common trap:** choosing FSx when no specialized filesystem is required.

## B13-10 — Answer B

- **Central requirement:** satisfy both managed scheduled movement and a
  persistent legacy storage interface without treating them as the same problem.
- **Decisive words:** *scheduled verified transfers*, *incremental tasks and
  reports*, *legacy NFS or iSCSI interface*, *movement versus interface*.
- **A:** this reverses the services: DataSync is transfer-oriented, while Storage
  Gateway provides persistent supported hybrid storage interfaces.
- **B:** correct; DataSync schedules, moves, verifies, and reports transfer tasks,
  whereas Storage Gateway lets applications use supported file, volume, or tape
  interface patterns integrated with AWS storage.
- **C:** network-based deployments of both services do not generally require a
  physical Snow device.
- **D:** managed SFTP endpoints are a Transfer Family use case; Storage Gateway
  supports hybrid file, volume, and tape gateway patterns.
- **Reusable rule:** copy/migrate/synchronize data → DataSync; preserve a legacy
  storage interface during hybrid operation → the matching Storage Gateway mode.
- **Variation:** if the network cannot satisfy the migration window, evaluate an
  offline transfer service separately from either interface decision.
- **Lessons:** 177–180.
- **Reference:** [DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) and [Storage Gateway](https://docs.aws.amazon.com/storagegateway/).
- **Common trap:** selecting by service name instead of interface and duration.

## Ação após a correção

Registre todo erro ou acerto de baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), com a palavra decisiva e a regra reutilizável.
