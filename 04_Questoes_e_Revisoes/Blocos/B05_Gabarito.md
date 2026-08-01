# B05 — Gabarito comentado

Abra somente depois de responder às [questões B05](B05_Questoes.md) e registrar
a confiança.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B05-01 | B | 3.1 |
| B05-02 | C | 3.1 |
| B05-03 | C | 3.1 |
| B05-04 | A | 1.3 |
| B05-05 | D | 3.1 |
| B05-06 | B | 2.2 |
| B05-07 | B | 3.1 |
| B05-08 | A | 3.1 |
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

## B05-03 — Resposta C

- **Requisito central:** avaliar gravação concorrente segura em EBS
  Multi-Attach.
- **Palavras decisivas:** *simultaneamente*, *filesystem comum*, *mesma AZ*.
- **A:** o EBS não fornece locking ou coordenação para qualquer filesystem.
- **B:** Multi-Attach não transforma o volume em recurso cross-AZ.
- **C:** correta; aplicação e filesystem cluster-aware devem coordenar I/O para
  evitar corrupção.
- **D:** o volume continua oferecendo block storage, não NFS.
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

- **Requisito central:** recover EBS data in a different Availability Zone.
- **Palavras decisivas:** *volume in 1a*, *instance in 1b*.
- **A:** an EBS volume cannot attach to an instance in another AZ.
- **B:** correct; create a regional snapshot and restore a new zonal volume in
  `us-east-1b`.
- **C:** EBS cannot be converted into host-local instance store.
- **D:** an Elastic IP is network addressing and cannot attach to a volume.
- **Regra reutilizável:** EBS across AZs → snapshot → new volume in target AZ.
- **Variação:** cross-Region recovery first requires copying the snapshot or a
  different replication mechanism.
- **Aulas:** 63.
- **Referência:** [Create an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html).

## B05-08 — Answer A

- **Requisito central:** choose EFS throughput for unpredictable, spiky load.
- **Palavras decisivas:** *unknown in advance*, *highly spiky*.
- **A:** correct; Elastic throughput automatically scales throughput with
  workload activity.
- **B:** Provisioned IOPS is an EBS dimension, not an EFS throughput mode.
- **C:** Max I/O is not mandatory; current guidance favors General Purpose for
  lower per-operation latency.
- **D:** S3 Transfer Acceleration does not configure EFS NFS throughput.
- **Regra reutilizável:** unpredictable EFS throughput → start with Elastic.
- **Variação:** known sustained requirements can justify Provisioned; Bursting
  ties throughput to data stored in Standard.
- **Aulas:** 66–68.
- **Referência:** [EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html).

## B05-09 — Answer D

- **Requisito central:** find independent storage that still bills after EC2
  termination.
- **Palavras decisivas:** *terminated*, *block storage bill remains*.
- **A:** listener rules are not block volumes.
- **B:** releasing a private IPv4 does not create retained block-storage cost.
- **C:** instance store ends with the underlying instance/host lifecycle.
- **D:** correct; an available data volume or retained snapshot is billed
  independently of the instance.
- **Regra reutilizável:** EC2 cleanup must separately audit EBS volumes,
  snapshots and snapshots behind AMIs.
- **Variação:** `DeleteOnTermination=false` intentionally preserves a volume
  and therefore its cost.
- **Aulas:** 61 e 69.
- **Referência:** [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html).

## B05-10 — Answer B

- **Requisito central:** identify the ELB component accepting a protocol/port.
- **Palavras decisivas:** *accepts client connections*, *protocol and port*.
- **A:** a snapshot is a storage recovery point.
- **B:** correct; the listener checks for connection requests on its configured
  protocol and port.
- **C:** a mount target provides EFS network access.
- **D:** a KMS grant delegates cryptographic-key permissions.
- **Regra reutilizável:** ELB front door → listener; destinations → target
  group; target availability → health check.
- **Variação:** an ALB listener rule can select different target groups by L7
  conditions.
- **Aulas:** 70–71.
- **Referência:** [How Elastic Load Balancing works](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html).

## Ação após a correção

No [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), registre toda resposta
errada e todo acerto com confiança baixa. Inclua palavra decisiva, regra
reutilizável e datas D+2/D+7.
