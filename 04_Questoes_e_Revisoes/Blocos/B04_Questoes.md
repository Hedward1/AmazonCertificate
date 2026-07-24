# B04 — Questões: endereçamento, placement, ENI, EBS e AMI

**Quantidade:** 10 questões autorais  
**Idioma:** 6 em português e 4 em inglês  
**Regra:** selecione uma resposta em cada questão  
**Tempo sugerido:** 15 minutos; registre sua confiança antes de corrigir  
**Gabarito:** [arquivo separado](B04_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B04-01 | 3.4 | Private, public e Elastic IP | Situacional | Básica | Português |
| B04-02 | 3.4 | Elastic Network Interface | Situacional | Intermediária | Português |
| B04-03 | 3.2 | Cluster placement group | Situacional | Básica | Português |
| B04-04 | 2.2 | Partition placement group | Situacional | Intermediária | Português |
| B04-05 | 2.2 | Spread placement group | Situacional | Intermediária | Português |
| B04-06 | 4.2 | EC2 Hibernate | Situacional | Intermediária | Português |
| B04-07 | 3.1 | Persistência de volumes EBS | Fundamental | Intermediária | Inglês |
| B04-08 | 2.2 | Snapshots incrementais | Fundamental | Intermediária | Inglês |
| B04-09 | 2.2 | AMI entre Regions | Situacional | Intermediária | Inglês |
| B04-10 | 2.2 | Restauração EBS entre AZs | Situacional | Intermediária | Inglês |

## Questões

### B04-01

Uma aplicação legada é executada em uma instância EC2 EBS-backed que é
interrompida durante a noite e iniciada novamente pela manhã. Um parceiro
externo precisa adicionar o endereço IPv4 público da aplicação à allowlist do
firewall.

Qual solução atende ao requisito com a menor mudança?

- A. Fornecer ao parceiro o endereço IPv4 privado primário da instância.
- B. Alocar um Elastic IP e associá-lo à instância ou à sua interface de rede.
- C. Continuar usando o endereço IPv4 público atribuído automaticamente, pois
  ele permanece igual depois de qualquer ciclo de stop/start.
- D. Adicionar um segundo endereço IPv4 privado à interface de rede.

### B04-02

Duas instâncias EC2 de um appliance virtual estão na mesma Availability Zone.
Somente uma fica ativa por vez. Durante o failover, a empresa precisa transferir
rapidamente para a instância reserva o endereço IPv4 privado, os security groups
e a identidade de rede usados pelo appliance.

Qual solução é a mais apropriada?

- A. Criar um snapshot do root volume da instância ativa e restaurá-lo na
  instância reserva durante cada failover.
- B. Mover a interface de rede primária da instância ativa para uma instância em
  outra Availability Zone.
- C. Converter o endereço IPv4 privado em um endereço público atribuído
  automaticamente.
- D. Usar uma ENI secundária com a configuração necessária e, durante o
  failover, desanexá-la da instância ativa e anexá-la à reserva na mesma
  Availability Zone.

### B04-03

Uma aplicação de high-performance computing possui dezenas de nós EC2 em uma
única Availability Zone. A maior parte do tráfego ocorre entre os nós, e o
requisito principal é obter baixa latência e alta taxa de transferência na
rede.

Qual estratégia de placement group é a mais apropriada?

- A. Cluster placement group.
- B. Spread placement group.
- C. Partition placement group.
- D. Nenhum placement group, distribuindo obrigatoriamente os nós entre várias
  Regions.

### B04-04

Uma empresa executará um grande cluster Apache Kafka. A aplicação conhece a
topologia das réplicas e precisa distribuir grupos de instâncias entre conjuntos
de racks distintos. Uma falha no hardware de uma partição não deve afetar as
instâncias de outras partições.

Qual estratégia atende melhor ao requisito?

- A. Spread placement group para todas as instâncias, independentemente da
  quantidade por Availability Zone.
- B. Cluster placement group.
- C. Partition placement group.
- D. Dedicated Host único para todo o cluster.

### B04-05

Uma empresa possui quatro instâncias EC2 críticas e independentes. Para reduzir
o risco de uma falha de hardware afetar mais de uma delas, cada instância deve
ser colocada em hardware subjacente distinto. A quantidade de instâncias
permanecerá pequena.

Qual estratégia de placement group deve ser usada?

- A. Cluster.
- B. Spread.
- C. Partition com todas as instâncias na mesma partição.
- D. Precision time.

### B04-06

Uma aplicação demora vários minutos para inicializar e reconstruir seu estado
em memória. A instância e o sistema operacional são compatíveis, e a hibernação
foi habilitada corretamente durante o lançamento. A empresa quer suspender a
instância e posteriormente continuar os processos do ponto em que estavam.

Qual afirmação descreve corretamente a solução?

- A. Um stop normal preserva automaticamente o conteúdo da RAM e retoma todos
  os processos.
- B. A hibernação grava a RAM em instance store e exclui os volumes EBS.
- C. A empresa deve terminar a instância e lançá-la novamente pela mesma AMI
  para recuperar a RAM.
- D. A hibernação grava a RAM no EBS root volume; ao iniciar, o conteúdo é
  restaurado e os processos continuam. Durante o estado stopped não há cobrança
  de compute, mas os volumes EBS continuam cobrados.

### B04-07

An EBS-backed EC2 instance has:

- a root EBS volume with `DeleteOnTermination=true`;
- a secondary data EBS volume with `DeleteOnTermination=false`.

What happens when the instance is stopped and later when it is terminated?

- A. Stopping deletes both volumes; terminating restores them from snapshots.
- B. Stopping preserves only the root volume; terminating preserves the root
  and deletes the data volume.
- C. Stopping preserves both volumes. On termination, the root volume is
  deleted and the secondary data volume persists.
- D. Both volumes are always deleted by either a stop or a termination because
  they are attached to the instance.

### B04-08

A 100-GiB EBS volume has an initial snapshot. After only 5 GiB of blocks change,
a second snapshot is created. The company later deletes the first snapshot.

Which statement is correct?

- A. EBS snapshots are incremental, but each snapshot can restore the volume to
  its own point in time. Deleting the first snapshot does not invalidate the
  second because referenced data is retained.
- B. Every standard-tier snapshot stores and bills another complete 100-GiB
  physical copy.
- C. The second snapshot becomes unusable as soon as the first snapshot is
  deleted.
- D. EBS snapshots are tied to one Availability Zone and cannot restore a
  volume in another AZ.

### B04-09

A company creates a customized EBS-backed AMI in `eu-west-1`. It must launch
instances with the same operating system and software configuration in
`us-east-1`.

What should the company do?

- A. Use the `eu-west-1` AMI ID directly when launching in `us-east-1`.
- B. Change the Region attribute of the running source instance.
- C. Detach the source root EBS volume and attach it directly to an instance in
  `us-east-1`.
- D. Copy the AMI to `us-east-1` and launch instances from the copied AMI.

### B04-10

An application stores data on an EBS volume in `us-east-1a`. The company has a
recent snapshot and needs to recover the data on an EC2 instance in
`us-east-1b`.

Which solution meets the requirement?

- A. Attach the existing `us-east-1a` EBS volume directly to the instance in
  `us-east-1b`.
- B. Create a new EBS volume from the snapshot in `us-east-1b`, and attach the
  new volume to the recovery instance.
- C. Copy the snapshot to another Region before creating the volume in
  `us-east-1b`.
- D. Associate an Elastic IP with the EBS volume to make it available in both
  Availability Zones.

## Registro antes de corrigir

| ID | Resposta | Confiança (alta/média/baixa) | Palavra decisiva |
|---|---|---|---|
| B04-01 |  |  |  |
| B04-02 |  |  |  |
| B04-03 |  |  |  |
| B04-04 |  |  |  |
| B04-05 |  |  |  |
| B04-06 |  |  |  |
| B04-07 |  |  |  |
| B04-08 |  |  |  |
| B04-09 |  |  |  |
| B04-10 |  |  |  |
