# B05 — Questões: EBS, instance store, EFS e HA

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 6 em português e 4 em inglês<br>
**Formato:** questões single-answer e multi-answer; siga a instrução de cada questão<br>
**Tempo sugerido:** 15 minutos<br>
**Gabarito:** [arquivo separado](B05_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B05-01 | 3.1 | Instance store | single | fundamental | básica | Português |
| B05-02 | 3.1 | EBS volume types | single | fundamental | básica | Português |
| B05-03 | 3.1 | EBS Multi-Attach | multi-2 | fundamental | intermediária | Português |
| B05-04 | 1.3 | EBS encryption | single | situacional | intermediária | Português |
| B05-05 | 3.1 | EFS Regional | single | situacional | intermediária | Português |
| B05-06 | 2.2 | HA e escalabilidade | single | situacional | intermediária | Português |
| B05-07 | 3.1 | EBS scope | single | situacional | intermediária | Inglês |
| B05-08 | 3.1 | EFS throughput | multi-2 | situacional | intermediária | Inglês |
| B05-09 | 4.1 | EBS sizing and cost | single | integrada | avançada | Inglês |
| B05-10 | 3.4 | ELB fundamentals | single | situacional | intermediária | Inglês |

## Questões

### B05-01
Uma frota de processamento pode repetir qualquer tarefa a partir dos objetos originais no S3. Ela precisa do menor tempo de acesso possível para arquivos temporários, e a perda desses arquivos quando uma instância é interrompida é aceitável. Qual armazenamento usar?<br>
- A. EFS Regional.
- B. Instance store.
- C. Snapshot EBS.
- D. S3 Glacier Deep Archive.

### B05-02
Um banco em EC2 exige IOPS provisionadas e latência consistente para transações críticas. Qual escolha inicial é mais adequada?<br>
- A. `sc1`.
- B. `st1`.
- C. `io2`.
- D. Instance store sem réplica.

### B05-03
Duas instâncias precisam gravar simultaneamente no mesmo volume EBS. Quais
afirmações descrevem corretamente uma arquitetura com EBS Multi-Attach?<br>

**Choose TWO.**

- A. O volume e todas as instâncias anexadas devem permanecer na mesma
  Availability Zone.
- B. Multi-Attach permite anexar o mesmo volume simultaneamente a instâncias em
  Availability Zones diferentes.
- C. A aplicação ou o filesystem cluster-aware deve coordenar o I/O concorrente
  para evitar corrupção.
- D. Multi-Attach converte o volume de block storage em um compartilhamento NFS.
- E. O EBS serializa automaticamente as gravações de qualquer filesystem comum.

### B05-04
Uma empresa precisa controlar e auditar quem pode usar a chave que protege volumes EBS. Qual solução atende melhor?<br>
- A. Chave KMS gerenciada pelo cliente com política e grants adequados.
- B. Security group no volume.
- C. Bucket policy no snapshot.
- D. Elastic IP criptografado.

### B05-05
Instâncias Linux em três AZs devem compartilhar o mesmo filesystem e continuar acessando dados após a perda de uma AZ. Qual solução?<br>
- A. Um volume EBS `gp3` em Multi-Attach.
- B. Instance store replicado por reboot.
- C. EFS One Zone.
- D. EFS Regional com conectividade e mount targets apropriados.

### B05-06
Qual afirmação distingue corretamente alta disponibilidade de escalabilidade horizontal?<br>
- A. São sinônimos.
- B. HA visa continuidade diante de falhas; escala horizontal adiciona/remove
  nós e pode ajudar, mas não garante HA sozinha.
- C. HA significa apenas usar uma instância maior.
- D. Escala horizontal elimina a necessidade de health checks.

### B05-07
A latency-sensitive database runs on one EC2 instance and requires persistent
block storage with sustained high IOPS, sub-millisecond average latency, and
independent provisioning of capacity and performance. The instance family can
use the Nitro System and must support the selected volume's requested
performance. The data must survive an instance stop or replacement, and the
application does not require a shared POSIX file system.<br>

Which storage design is the best fit?<br>

- A. Store the database only on instance store and rely on an Elastic IP for
  durability.
- B. Attach an Amazon EBS `io2 Block Express` volume to a compatible Nitro-based
  EC2 instance, provision capacity and IOPS for the workload, and protect the
  volume with the required snapshot or replication policy.
- C. Convert an Amazon EFS file system into an EC2 root block device.
- D. Put the database files in an S3 Glacier Flexible Retrieval vault and mount
  the vault as a low-latency disk.

### B05-08
An EFS workload is unpredictable and highly spiky. The team does not know the
throughput requirement in advance. Which statements support the best starting
configuration?<br>

**Choose TWO.**

- A. Select Elastic throughput so throughput scales automatically with workload
  activity.
- B. Configure Provisioned IOPS, which is the EFS throughput mode for unknown
  demand.
- C. Select Max I/O because it is mandatory whenever Elastic throughput is
  enabled.
- D. Elastic throughput is designed for workloads whose throughput needs are
  difficult to forecast or vary significantly.
- E. Enable S3 Transfer Acceleration to scale EFS NFS throughput.

### B05-09
A database currently uses `1,200 GiB` on an EBS volume. Measurements show
growth of `80 GiB` per month, and the team will review capacity again in six
months. The approved headroom is 20% above projected usage. The workload needs
`8,000` sustained IOPS and `400 MiB/s`; single-digit millisecond latency is
acceptable, and the EC2 instance supports these EBS requirements. The company
wants the lowest-cost design that meets capacity and performance.<br>

Which sizing decision is the best fit?<br>

- A. Keep `1,200 GiB` until it is full and use EBS snapshots as writable
  overflow capacity during the next six months.
- B. Provision `8,000 GiB` because a `gp3` volume requires one GiB of capacity
  for every provisioned IOPS.
- C. Provision `2,100 GiB` of `io2 Block Express` at its maximum IOPS, although
  the workload does not require sub-millisecond latency or its added durability.
- D. Project `1,680 GiB`, apply headroom to obtain `2,016 GiB`, round up to
  approximately `2,100 GiB` of `gp3`, and provision `8,000 IOPS` and
  `400 MiB/s` independently while validating instance limits and regional
  pricing.

### B05-10
An Application Load Balancer must accept public HTTPS on port 443 with an ACM
certificate. Host-based rules then forward requests to separate target groups,
whose targets listen on internal application ports and have independent health
checks.<br>

Which component owns the front-end protocol, port, certificate, and evaluation
of those forwarding rules?<br>

- A. An EBS snapshot.
- B. The load balancer listener.
- C. An EFS mount target.
- D. A KMS grant.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B05-01 | | | |
| B05-02 | | | |
| B05-03 | | | |
| B05-04 | | | |
| B05-05 | | | |
| B05-06 | | | |
| B05-07 | | | |
| B05-08 | | | |
| B05-09 | | | |
| B05-10 | | | |
