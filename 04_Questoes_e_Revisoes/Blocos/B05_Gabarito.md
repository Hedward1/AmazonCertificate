# B05 — Gabarito comentado

Abra somente depois de responder às [questões B05](B05_Questoes.md) e registrar
a confiança.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B05-01 | B | 3.1 |
| B05-02 | C | 3.1 |
| B05-03 | A,C | 3.1 |
| B05-04 | A | 1.3 |
| B05-05 | D | 3.1 |
| B05-06 | B | 2.2 |
| B05-07 | B | 3.1 |
| B05-08 | A,D | 3.1 |
| B05-09 | D | 4.1 |
| B05-10 | B | 3.4 |

## B05-01 — Resposta B

- **Requisito central:** obter scratch de baixa latência quando perder os dados
  é aceitável.
- **Palavras decisivas:** *temporário*, *reconstruível*, *menor tempo de acesso*.
- **A:** EFS oferece persistência e compartilhamento por rede que o cenário não
  pede.
- **B:** correta; instance store usa discos ligados ao host e atende dados
  efêmeros reconstruíveis.
- **C:** snapshot é um recovery point, não um device montável para scratch.
- **D:** Glacier Deep Archive prioriza arquivo de baixo custo, com restauração
  incompatível com acesso imediato.
- **Regra reutilizável:** scratch, cache ou buffer reconstruível → instance
  store; mantenha original e resultado em storage durável.
- **Variação:** instance store normalmente sobrevive a reboot, mas não a stop,
  hibernate, terminate ou falha do host.
- **Aulas:** 62.
- **Referência:** [EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html).

## B05-02 — Resposta C

- **Requisito central:** fornecer IOPS provisionadas e consistentes a um banco
  transacional crítico.
- **Palavras decisivas:** *banco*, *IOPS provisionadas*, *latência consistente*.
- **A:** `sc1` é HDD para dados frios e sequenciais.
- **B:** `st1` é HDD otimizado para throughput sequencial.
- **C:** correta; `io2` é SSD de IOPS provisionadas e maior durabilidade.
- **D:** instance store sozinho perde dados em eventos do host/ciclo de vida.
- **Regra reutilizável:** OLTP crítico com IOPS consistentes → avaliar `io2` e o
  limite de EBS do instance type.
- **Variação:** `gp3` pode ser mais econômico quando seus limites satisfazem o
  workload.
- **Aulas:** 63.
- **Referência:** [EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html).

## B05-03 — Resposta A,C

- **Requisito central:** avaliar gravação concorrente segura em EBS
  Multi-Attach.
- **Palavras decisivas:** *simultaneamente*, *filesystem comum*, *mesma AZ*.
- **A:** correta; um volume Multi-Attach só pode ser anexado a instâncias na
  mesma Availability Zone.
- **B:** Multi-Attach não transforma o volume em recurso cross-AZ.
- **C:** correta; aplicação e filesystem cluster-aware devem coordenar I/O para
  evitar corrupção.
- **D:** o volume continua oferecendo block storage, não NFS.
- **E:** o EBS não fornece locking nem serialização para qualquer filesystem
  comum.
- **Regra reutilizável:** Multi-Attach fornece acesso ao bloco; consistência
  concorrente é responsabilidade do software.
- **Variação:** para filesystem Linux compartilhado entre AZs, EFS costuma ser
  a resposta administrada.
- **Aulas:** 64.
- **Referência:** [EBS Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html).

## B05-04 — Resposta A

- **Requisito central:** controlar e auditar o uso da chave de criptografia.
- **Palavras decisivas:** *controlar*, *auditar*, *chave*.
- **A:** correta; customer managed KMS key permite política, grants, rotação e
  auditoria sob controle do cliente.
- **B:** security group controla tráfego de rede, não criptografia de EBS.
- **C:** snapshots EBS não usam bucket policy S3 do cliente.
- **D:** endereço IP não é mecanismo de criptografia de bloco.
- **Regra reutilizável:** necessidade de governança própria da chave → customer
  managed KMS key e menor privilégio.
- **Variação:** negar ou excluir a chave pode impedir acesso a volumes e
  snapshots; proteção da key faz parte da disponibilidade.
- **Aulas:** 65.
- **Referência:** [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html).

## B05-05 — Resposta D

- **Requisito central:** compartilhar filesystem entre três AZs e sobreviver à
  perda de uma delas.
- **Palavras decisivas:** *Linux*, *mesmo filesystem*, *três AZs*.
- **A:** EBS Multi-Attach é zonal e não oferece uma interface NFS.
- **B:** reboot não replica instance store e perda do host destrói os dados.
- **C:** EFS One Zone não atende resiliência à perda completa da AZ.
- **D:** correta; EFS Regional oferece filesystem NFS regional com acesso pelas
  AZs configuradas.
- **Regra reutilizável:** NFS compartilhado e Multi-AZ → EFS Regional.
- **Variação:** mount targets, SG, TCP 2049 e permissões POSIX ainda precisam
  ser configurados.
- **Aulas:** 66–68.
- **Referência:** [Amazon EFS features](https://docs.aws.amazon.com/efs/latest/ug/features.html).

## B05-06 — Resposta B

- **Requisito central:** diferenciar objetivo de capacidade do objetivo de
  continuidade.
- **Palavras decisivas:** *alta disponibilidade*, *escala horizontal*.
- **A:** os conceitos se apoiam, mas não são sinônimos.
- **B:** correta; HA trata continuidade diante de falhas, enquanto scale-out
  altera número de nós.
- **C:** instância maior é escala vertical, não definição de HA.
- **D:** novas instâncias ainda exigem health checks.
- **Regra reutilizável:** scaling responde a carga; redundância e failover
  respondem a falha.
- **Variação:** um ASG com min=1 pode escalar e ainda sofrer interrupção durante
  reposição.
- **Aulas:** 70–71.
- **Referência:** [Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

## B05-07 — Answer B

- **Requisito central:** choose persistent, high-performance block storage for a
  database while decoupling the data lifecycle from the EC2 instance.
- **Palavras decisivas:** *persistent block storage*, *sustained high IOPS*,
  *sub-millisecond average latency*, *Nitro*, *survive instance replacement*.
- **A:** instance store is host-local ephemeral storage; an Elastic IP provides
  network addressing and cannot make the data durable.
- **B:** correct; `io2 Block Express` on a compatible Nitro-based instance
  provides provisioned-IOPS EBS block storage for I/O-intensive,
  latency-sensitive workloads. Instance and volume limits must support the
  requested performance, while snapshots or replication address recovery.
- **C:** EFS is a managed shared file system and cannot be converted into an EC2
  block-device root volume.
- **D:** S3 Glacier Flexible Retrieval is archival object storage, not a
  mountable low-latency database volume.
- **Regra reutilizável:** persistent single-instance block I/O with explicit
  sub-millisecond and IOPS requirements points to `io2 Block Express` plus a
  compatible Nitro instance; add a separate recovery mechanism for the failure
  scope.
- **Variação:** a shared Linux file workload across instances would change the
  comparison toward EFS rather than EBS.
- **Aulas:** 63.
- **Referência:** [Provisioned IOPS SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html).

## B05-08 — Answer A,D

- **Requisito central:** choose EFS throughput for unpredictable, spiky load.
- **Palavras decisivas:** *unknown in advance*, *highly spiky*.
- **A:** correct; Elastic throughput automatically scales throughput with
  workload activity.
- **B:** Provisioned IOPS is an EBS dimension, not an EFS throughput mode.
- **C:** Max I/O is not mandatory; current guidance favors General Purpose for
  lower per-operation latency.
- **D:** correct; Elastic throughput is intended for varying or
  difficult-to-forecast throughput needs.
- **E:** S3 Transfer Acceleration does not configure EFS NFS throughput.
- **Regra reutilizável:** unpredictable EFS throughput → start with Elastic.
- **Variação:** known sustained requirements can justify Provisioned; Bursting
  ties throughput to data stored in Standard.
- **Aulas:** 66–68.
- **Referência:** [EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html).

## B05-09 — Answer D

- **Requisito central:** meet forecast capacity and measured performance without
  paying for unrelated storage or a premium volume class.
- **Palavras decisivas:** *growth per month*, *review in six months*, *20%
  headroom*, *8,000 IOPS*, *400 MiB/s*, *lowest cost*.
- **A:** a snapshot is a point-in-time backup, not writable overflow for an
  attached volume; waiting until the filesystem is full also violates the
  approved capacity margin.
- **B:** `gp3` separates capacity, IOPS and throughput within documented ratios
  and limits. Capacity does not need to equal the IOPS count.
- **C:** the proposed capacity is reasonable, but maximum `io2 Block Express`
  performance and its premium characteristics are unnecessary for the stated
  latency, IOPS and cost requirements.
- **D:** correct; `1,200 + (80 × 6) = 1,680 GiB`, and
  `1,680 × 1.20 = 2,016 GiB`. Rounding up provides the approved margin, while
  `gp3` permits the required IOPS and throughput to be provisioned separately.
- **Regra reutilizável:** forecast capacity through the next review, add
  justified headroom, then size IOPS and throughput from measurements and price
  the dimensions separately.
- **Variação:** if the workload required sub-millisecond latency, materially
  higher durability, or performance beyond `gp3`, compare `io2 Block Express`
  and a compatible Nitro instance.
- **Aulas:** 63 e 69.
- **Referências:** [`gp3` volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html) e [right-size resources](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/select-the-correct-resource-type-size-and-number.html).

## B05-10 — Answer B

- **Requisito central:** map TLS termination and front-end connection handling to
  the correct component while keeping routing destinations and health separate.
- **Palavras decisivas:** *public HTTPS 443*, *ACM certificate*, *host-based
  rules*, *target groups use internal ports*.
- **A:** a snapshot is a storage recovery point and cannot accept network
  connections or evaluate routing rules.
- **B:** correct; the listener owns the front-end protocol and port, can use the
  certificate for HTTPS, and evaluates its rules before forwarding.
- **C:** a mount target provides network access to an EFS file system, not to an
  ALB front end.
- **D:** a KMS grant delegates cryptographic-key permissions and is not a
  load-balancer connection component.
- **Regra reutilizável:** ELB front door/TLS → listener; request selection →
  listener rule; destinations → target group; target availability → health check.
- **Variação:** an ALB listener rule can select different target groups by L7
  conditions.
- **Aulas:** 70–71.
- **Referência:** [How Elastic Load Balancing works](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html).

## Ação após a correção

No [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), registre toda resposta
errada e todo acerto com confiança baixa. Inclua palavra decisiva, regra
reutilizável e datas D+2/D+7.
