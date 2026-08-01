# B13 — Gabarito comentado

Corrija somente após responder às [questões B13](B13_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B13-01 | D | 3.1 |
| B13-02 | A | 3.1 |
| B13-03 | C | 3.5 |
| B13-04 | B | 3.5 |
| B13-05 | C | 3.1 |
| B13-06 | A | 3.5 |
| B13-07 | B | 3.1 |
| B13-08 | B | 3.1 |
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

## B13-03 — Resposta C

- **Requisito central:** copiar arquivos online com agendamento, automação e verificação.
- **Palavras decisivas:** *milhões de arquivos*, *NFS*, *agendamento*, *verificação*.
- **A:** Direct Connect fornece conectividade, mas não é o motor de cópia.
- **B:** S3 File Gateway mantém uma interface híbrida em vez de ser apenas uma tarefa de migração.
- **C:** correta; DataSync executa, agenda, verifica e monitora transferências.
- **D:** SNS é pub/sub e não copia arquivos.
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

## B13-08 — Answer B

- **Central requirement:** preserve NetApp ONTAP and multiprotocol features.
- **Decisive words:** *NetApp*, *NFS/SMB/iSCSI*, *snapshots*, *clones*.
- **A:** EFS supplies NFS but not the requested ONTAP capabilities.
- **B:** correct; FSx for NetApp ONTAP is purpose-built for these requirements.
- **C:** FSx for Lustre targets parallel compute and HPC.
- **D:** S3 is object storage rather than a multiprotocol ONTAP filesystem.
- **Reusable rule:** NetApp migration or ONTAP features → FSx for NetApp ONTAP.
- **Lessons:** 175–176.
- **Reference:** [FSx for ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html).
- **Common trap:** choosing an FSx family without matching its engine and protocol.

## B13-09 — Answer A

- **Central requirement:** shared elastic NFS for Linux across Availability Zones.
- **Decisive words:** *Linux*, *NFS*, *multi-AZ*, *no specialized engine*.
- **A:** correct; EFS is the general-purpose regional NFS option.
- **B:** EBS is Availability Zone-scoped block storage.
- **C:** Glacier Flexible Retrieval is an object archival class.
- **D:** Transfer Family is a managed transfer endpoint, not a mounted NFS share.
- **Reusable rule:** shared elastic regional NFS → Amazon EFS.
- **Lessons:** 181.
- **Reference:** [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html).
- **Common trap:** choosing FSx when no specialized filesystem is required.

## B13-10 — Answer B

- **Central requirement:** distinguish data movement from an ongoing hybrid interface.
- **Decisive words:** *automates transfer tasks*, *exposes interface*.
- **A:** this reverses the roles of the two services.
- **B:** correct; DataSync moves data, while Storage Gateway presents hybrid storage protocols.
- **C:** neither service generally requires a Snow device.
- **D:** SFTP endpoints are supplied by Transfer Family, not Storage Gateway.
- **Reusable rule:** copy/migrate → DataSync; preserve legacy storage protocol → Storage Gateway.
- **Lessons:** 177–180.
- **Reference:** [DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) and [Storage Gateway](https://docs.aws.amazon.com/storagegateway/).
- **Common trap:** selecting by service name instead of interface and duration.

## Ação após a correção

Registre todo erro ou acerto de baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), com a palavra decisiva e a regra reutilizável.
