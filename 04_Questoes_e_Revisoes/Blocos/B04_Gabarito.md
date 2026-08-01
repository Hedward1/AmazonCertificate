# B04 — Gabarito comentado

Abra este arquivo somente depois de responder e registrar a confiança em todas
as [questões B04](B04_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B04-01 | B | 3.4 |
| B04-02 | D | 3.4 |
| B04-03 | A,D | 3.2 |
| B04-04 | C | 2.2 |
| B04-05 | B | 2.2 |
| B04-06 | D | 4.2 |
| B04-07 | C | 3.1 |
| B04-08 | A,C,E | 2.2 |
| B04-09 | D | 2.2 |
| B04-10 | B | 2.2 |

## B04-01 — Resposta B

- **Requisito central:** manter um IPv4 público previsível apesar de ciclos de
  stop/start.
- **Palavras decisivas:** *allowlist*, *IPv4 público*, *stop/start*.
- **A:** um endereço privado não é diretamente alcançável pela internet e não
  atende à allowlist pública do parceiro.
- **B:** correta; um Elastic IP é um IPv4 público estático alocado à conta. Ele
  permanece sob controle da empresa até ser liberado e pode ser remapeado.
- **C:** uma instância normalmente recebe outro IPv4 público automático quando
  volta a ser iniciada.
- **D:** outro IPv4 privado não cria um endereço público estável.
- **Regra reutilizável:** necessidade explícita de IPv4 público fixo → Elastic
  IP; para comunicação interna, prefira IP privado ou DNS.
- **Variação:** Elastic IP é regional e endereços IPv4 públicos geram cobrança,
  inclusive quando estão ociosos.
- **Aulas:** 47–48.
- **Referências:** [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) e [stop and start EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html).

## B04-02 — Resposta D

- **Requisito central:** mover a identidade de rede durante failover dentro da
  mesma AZ.
- **Palavras decisivas:** *mesma Availability Zone*, *private IP*, *security
  groups*, *failover*.
- **A:** um snapshot recupera armazenamento, não transfere imediatamente a
  identidade de rede.
- **B:** uma interface de rede pertence a uma subnet e Availability Zone. A
  interface primária também não pode ser tratada como uma ENI secundária
  destacável para esse failover.
- **C:** um endereço público automático não preserva a configuração privada nem
  os security groups solicitados.
- **D:** correta; uma ENI secundária mantém seus atributos ao ser desanexada e
  anexada a outra instância na mesma Availability Zone.
- **Regra reutilizável:** failover de identidade de rede em uma AZ → mover uma
  ENI secundária.
- **Variação:** para failover entre AZs, use mecanismos de nível superior, como
  load balancer, DNS ou outra arquitetura, pois a ENI não atravessa AZs.
- **Aulas:** 51–53.
- **Referência:** [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html).

## B04-03 — Resposta A,D

- **Requisito central:** maximizar desempenho de rede entre nós estreitamente
  acoplados.
- **Palavras decisivas:** *HPC*, *single AZ*, *low latency*, *high throughput*.
- **A:** correta; cluster placement aproxima as instâncias dentro de uma AZ para
  workloads com comunicação intensa entre nós.
- **B:** spread prioriza separar um pequeno número de instâncias para reduzir
  falhas correlacionadas, não aproximá-las.
- **C:** partition separa grupos de instâncias em conjuntos de hardware
  distintos para grandes sistemas distribuídos que conhecem a topologia.
- **D:** correta; nós na mesma AZ e tipos compatíveis com enhanced networking
  complementam o cluster placement para baixa latência e alto throughput.
- **E:** distribuir os nós entre Regions aumentaria a latência e não atenderia à
  comunicação tightly coupled.
- **Regra reutilizável:** HPC ou comunicação intensa entre nós na mesma AZ →
  cluster placement group.
- **Variação:** lançar as instâncias em uma única solicitação e usar tipos
  homogêneos melhora a chance de obter capacidade.
- **Aulas:** 49–50.
- **Referência:** [Placement strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html).

## B04-04 — Resposta C

- **Requisito central:** isolar grupos de nós de um sistema distribuído em
  conjuntos de racks.
- **Palavras decisivas:** *Kafka*, *topologia das réplicas*, *partições*, *falha
  não deve afetar outras partições*.
- **A:** spread oferece separação estrita, mas em uma Region aceita no máximo
  sete instâncias por AZ em cada placement group. Não é a escolha para um grande
  cluster.
- **B:** cluster concentra as instâncias para desempenho de rede e aumenta a
  possibilidade de impacto correlacionado.
- **C:** correta; partition placement cria partições lógicas que não compartilham
  o hardware subjacente entre si e expõe a topologia à aplicação.
- **D:** colocar todo o cluster em um host concentra o risco e não separa as
  partições.
- **Regra reutilizável:** Hadoop, Cassandra, Kafka e grandes clusters
  topology-aware → partition placement group.
- **Variação:** um partition placement group regional pode ter até sete
  partições por Availability Zone.
- **Aulas:** 49–50.
- **Referência:** [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

## B04-05 — Resposta B

- **Requisito central:** separar estritamente um pequeno número de instâncias
  críticas.
- **Palavras decisivas:** *quatro*, *independentes*, *hardware distinto*.
- **A:** cluster aproxima as instâncias e favorece desempenho, não isolamento de
  falhas.
- **B:** correta; spread placement coloca cada instância em hardware distinto
  para reduzir falhas correlacionadas.
- **C:** instâncias na mesma partição podem compartilhar o conjunto de hardware
  daquela partição.
- **D:** precision time fornece acesso a fontes de tempo de alta precisão; não é
  a estratégia principal para isolar falhas.
- **Regra reutilizável:** pequeno conjunto de instâncias críticas que precisam
  ficar separadas → spread.
- **Variação:** rack-level spread em uma Region suporta no máximo sete instâncias
  em execução por Availability Zone em cada grupo.
- **Aulas:** 49–50.
- **Referência:** [Placement strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html).

## B04-06 — Resposta D

- **Requisito central:** preservar o estado em memória e retomar processos.
- **Palavras decisivas:** *estado em memória*, *continuar do ponto em que
  estavam*, *hibernação habilitada*.
- **A:** um stop comum preserva volumes EBS, mas não preserva a RAM nem retoma os
  processos.
- **B:** a RAM é gravada no EBS root volume. Dados em instance store não são a
  base da hibernação e podem ser perdidos.
- **C:** uma AMI preserva configuração de disco, não uma sessão RAM em execução.
- **D:** correta; hibernate realiza suspend-to-disk no root EBS. Ao reiniciar, a
  RAM e os processos são restaurados. Compute não é cobrado enquanto stopped,
  mas o armazenamento EBS permanece cobrado.
- **Regra reutilizável:** preservar memória e acelerar retomada → hibernate;
  preservar apenas discos → stop.
- **Variação:** a hibernação precisa ser habilitada e depende de AMI, tipo de
  instância, sistema operacional, RAM e root volume compatíveis.
- **Aulas:** 54–55.
- **Referência:** [Hibernate an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html).

## B04-07 — Answer C

- **Central requirement:** distinguish stopping from termination and apply the
  two `DeleteOnTermination` settings.
- **Keywords:** *EBS-backed*, *root true*, *data false*.
- **A:** stopping an EBS-backed instance does not delete its attached EBS
  volumes.
- **B:** this reverses the configured termination behavior.
- **C:** correct; both volumes survive stop/start. On termination, the root
  volume is deleted because its flag is true, while the secondary volume
  persists because its flag is false.
- **D:** volume behavior on termination is configurable, and stopping is not the
  same as deleting an instance.
- **Reusable rule:** stop preserves attached EBS; termination follows each
  volume's `DeleteOnTermination` value.
- **Variation:** by default, an EBS root volume is deleted on termination, while
  additional volumes created at launch normally persist unless configured
  otherwise.
- **Lessons:** 56–57.
- **Reference:** [Amazon EBS data persistence](https://docs.aws.amazon.com/ebs/latest/userguide/EBSFeatures.html).

## B04-08 — Answer A,C,E

- **Central requirement:** understand incremental storage without confusing it
  with restore dependency.
- **Keywords:** *only 5 GiB changed*, *deletes the first snapshot*.
- **A:** correct; after the initial snapshot, EBS stores new and changed blocks
  incrementally.
- **B:** standard snapshots do not independently duplicate every unchanged block
  for billing.
- **C:** correct; every snapshot remains a complete logical recovery point for
  its own point in time.
- **D:** snapshots are regional and their data is replicated across the Region;
  they can create volumes in any AZ in that Region.
- **E:** correct; snapshot deletion removes only data no longer referenced by
  another snapshot, so the second recovery point remains usable.
- **F:** deleting an earlier recovery point does not break a user-managed
  incremental chain.
- **Reusable rule:** incremental storage, independent restore point.
- **Variation:** deleting a snapshot might not reduce cost if later snapshots
  still reference its blocks.
- **Lessons:** 58–59.
- **Reference:** [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html).

## B04-09 — Answer D

- **Central requirement:** make an encrypted, approved machine image independently
  launchable by the recovery account in another Region.
- **Keywords:** *regional disaster recovery*, *customer managed KMS key*,
  *recovery account*, *no source-Region dependency*.
- **A:** sharing changes account authorization but not Region scope; an AMI ID
  from `eu-west-1` cannot be launched by a `us-east-1` template.
- **B:** rebuilding from current packages during the incident does not guarantee
  the same preapproved image, adds recovery-time work, and lacks pre-disaster
  validation.
- **C:** a copy encrypted with the default AWS managed EBS key cannot be shared
  for cross-account use; the destination copy needs an authorized customer
  managed key and the corresponding permissions.
- **D:** correct; copying creates a destination AMI and snapshots, and the
  destination KMS and sharing permissions make that image usable by the recovery
  account and Auto Scaling group.
- **Reusable rule:** cross-Region AMI recovery = regional copy + destination
  encryption authorization + launch-template reference to the copied AMI.
- **Variation:** an automated image pipeline can refresh and test the destination
  AMI regularly instead of copying it only during an incident.
- **Lessons:** 60.
- **References:** [Copy an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html) and [share encrypted AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html#sharingamis-explicit-encrypted).

## B04-10 — Answer B

- **Central requirement:** recover an encrypted zonal block volume from a
  Regional snapshot after the source Availability Zone is unavailable.
- **Keywords:** *source AZ unavailable*, *encrypted snapshot*, *recovery role has
  KMS access*, *same Region*, *us-east-1b*.
- **A:** the original EBS volume remains scoped to its Availability Zone and
  cannot attach across AZs, regardless of the role's encryption permissions.
- **B:** correct; the authorized recovery path restores a new encrypted zonal
  volume from the Regional snapshot in `us-east-1b` and attaches it there.
- **C:** both Availability Zones are in `us-east-1`, so a cross-Region copy adds
  unnecessary delay and is not required by the runbook.
- **D:** an Elastic IP is network addressing and cannot change EBS scope or be
  associated with a volume.
- **Reusable rule:** zonal EBS failure recovery = usable snapshot + KMS
  authorization when encrypted + restore in target AZ + attach there.
- **Variation:** cross-Region recovery would first require a snapshot copy or
  another replication mechanism.
- **Lessons:** 58–59.
- **References:** [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) and [restore an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-restoring-volume.html).

## Ação após a correção

Registre no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md):

- toda resposta errada;
- toda resposta correta com confiança baixa;
- a palavra decisiva;
- a regra de decisão;
- as datas D+2 e D+7.
