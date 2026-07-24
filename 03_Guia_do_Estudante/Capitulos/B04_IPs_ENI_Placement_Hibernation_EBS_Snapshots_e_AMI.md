# B04 — IPs, ENIs, placement groups, hibernação, EBS, snapshots e AMIs

**Data planejada:** 29/07/2026  
**Nível:** iniciante absoluto  
**Comece pelas aulas da Udemy:** [roteiro B04 — aulas
047–060](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b04);
assista `047–060` antes deste capítulo  
**Domínios oficiais:** 2 — Design Resilient Architectures; 3 — Design
High-Performing Architectures; 4 — Design Cost-Optimized Architectures  
**Tarefas principais:** 2.2 — Design highly available and/or fault-tolerant
architectures; 3.1 — Determine high-performing and/or scalable storage
solutions; 3.2 — Design high-performing and elastic compute solutions; 3.4 —
Determine high-performing and/or scalable network architectures; 4.2 — Design
cost-optimized compute solutions  
**Tarefas secundárias:** 1.3 — Determine appropriate data security controls;
4.1 — Design cost-optimized storage solutions; 4.4 — Design cost-optimized
network architectures  
**Pré-requisito:** [B03 — conexão ao EC2, roles e modelos de
compra](B03_Conexao_EC2_Roles_e_Modelos_de_Compra.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá conseguir:

1. diferenciar private IPv4, public IPv4 automático e Elastic IP;
2. prever o que acontece com cada endereço em reboot, stop, hibernate e
   terminate;
3. explicar por que um endereço público não substitui rota, security group ou
   internet gateway;
4. identificar os atributos que pertencem a uma Elastic Network Interface;
5. usar uma ENI secundária como identidade de rede móvel dentro de uma
   Availability Zone;
6. escolher entre cluster, partition e spread placement groups;
7. distinguir reboot, stop, hibernate e terminate;
8. explicar o escopo zonal e a persistência de um volume EBS;
9. aplicar corretamente `DeleteOnTermination`;
10. explicar por que snapshots são incrementais sem formar uma cadeia frágil de
    restauração;
11. restaurar conceitualmente dados EBS em outra AZ ou Region;
12. explicar a relação entre uma AMI EBS-backed e seus snapshots;
13. prever custos residuais de EBS, snapshots, AMIs e IPv4 público;
14. resolver cenários que combinem rede, compute, storage e recuperação.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 47 — Private vs Public vs Elastic IP | estudar integralmente |
| 48 — Private vs Public vs Elastic IP Hands On | acompanhar e reproduzir a tabela de ciclo de vida |
| 49 — EC2 Placement Groups | alta prioridade para decisões de arquitetura |
| 50 — EC2 Placement Groups Hands On | fazer o walkthrough sem criar recursos |
| 51 — Elastic Network Interfaces (ENI) — Overview | estudar integralmente |
| 52 — Elastic Network Interfaces (ENI) — Hands On | substituir criação por inventário read-only |
| 53 — ENI — Extra Reading | ler o resumo deste capítulo e usar como consulta |
| 54 — EC2 Hibernate | estudar integralmente |
| 55 — EC2 Hibernate — Hands On | usar o filtro de compatibilidade, sem lançar instância |
| 56 — EBS Overview | estudar integralmente |
| 57 — EBS Hands On | observar o ciclo; a prática de criação ficará no B05 |
| 58 — EBS Snapshots | estudar integralmente |
| 59 — EBS Snapshots — Hands On | fazer em diagrama; criação e exclusão ficarão no B05 |
| 60 — AMI Overview | estudar integralmente |

O LAB B04 é intencionalmente read-only. O B03 já demonstrou o ciclo de vida de
uma instância, e o B05 criará um volume e um snapshot de forma controlada. Criar
recursos intermediários somente para repetir os cliques das aulas aumentaria o
risco de cobrança sem melhorar a sequência didática.

### Atualizações importantes em 2026

- Todos os public IPv4 fornecidos pela AWS são cobrados, inclusive os
  associados a instâncias em execução e os Elastic IPs.
- A documentação atual apresenta também **precision time placement groups**.
  Eles atendem aplicações que precisam de fontes locais de tempo com precisão
  de microssegundos. Não substituem cluster, partition ou spread e não fazem
  parte das aulas 47–60.
- A hibernação precisa ser habilitada durante o lançamento. A documentação
  vigente limita a permanência contínua em hibernação a 60 dias.
- Amazon Linux 2023 é a referência atual dos laboratórios. Amazon Linux 2
  encerrou o suporte em 30/06/2026.
- Ao desregistrar uma AMI, os snapshots associados não desaparecem
  necessariamente. Eles devem participar da auditoria de custos.

## 3. Vocabulário essencial

| Inglês | Significado no cenário |
|---|---|
| private IPv4 address | endereço da faixa da subnet, usado dentro da rede |
| public IPv4 address | endereço público temporário fornecido pelo pool da AWS |
| Elastic IP address | IPv4 público estático alocado à conta em uma Region |
| allowlist | lista de endereços autorizados |
| network interface / ENI | placa de rede virtual dentro de uma VPC |
| primary ENI | interface índice 0, não destacável da instância |
| secondary ENI | interface adicional que pode ser movida na mesma AZ |
| source/destination check | valida se a instância é origem ou destino do tráfego |
| placement group | controle lógico de posicionamento de instâncias |
| tightly coupled | nós com comunicação intensa e sensível à latência |
| correlated failure | falha que afeta componentes colocados próximos |
| suspend-to-disk | gravação do estado da memória em disco |
| root volume | volume de inicialização do sistema operacional |
| data volume | volume adicional usado para dados |
| point-in-time snapshot | cópia lógica de blocos em um instante |
| crash-consistent | estado semelhante ao de uma queda súbita de energia |
| incremental | armazena somente blocos novos ou alterados após a primeira cópia |
| restore | criação de um novo volume a partir de um snapshot |
| Amazon Machine Image (AMI) | modelo regional para lançar instâncias |
| deregister | remover o registro de uma AMI |
| Delete on termination | excluir ou preservar um volume quando a instância termina |

Palavras decisivas:

```text
fixed public IPv4 / firewall allowlist       -> Elastic IP
move private IP + security groups in one AZ  -> secondary ENI
low latency + high throughput + one AZ       -> cluster
large topology-aware distributed system      -> partition
few critical instances on distinct hardware  -> spread
resume RAM and processes                     -> hibernate
block storage that survives stop             -> EBS
recover in another AZ                        -> snapshot -> new volume
same customized image in another Region      -> copy AMI
```

## 4. O mapa mental: recurso, escopo e persistência

Antes de decorar comportamentos, descubra a qual recurso cada atributo pertence:

```text
Region
├── Elastic IP allocation
├── AMI
├── EBS snapshot
└── placement group
    ├── cluster: uma AZ
    ├── partition: uma ou mais AZs
    └── spread: uma ou mais AZs

Availability Zone
├── subnet
├── ENI
└── EBS volume

EC2 instance
├── primary ENI
├── EBS root/data volumes
└── RAM e processos
```

Consequências:

- uma ENI não atravessa AZs;
- um volume EBS não é anexado diretamente em outra AZ;
- um snapshot regional pode criar um novo volume na AZ desejada;
- uma AMI precisa ser copiada para ser usada em outra Region;
- um Elastic IP pertence à Region, não ao sistema operacional da instância.

## 5. Private IPv4, public IPv4 e Elastic IP

### 5.1 Private IPv4

Ao lançar uma instância em uma subnet IPv4 ou dual-stack, a ENI primária recebe
um private IPv4 da faixa da subnet.

- Ele não é diretamente alcançável pela internet.
- Permanece associado à ENI em reboot, stop/start e hibernate/start.
- É liberado quando a ENI é excluída, normalmente com a terminação da
  instância.
- Endereços privados secundários podem ser atribuídos e reatribuídos, conforme
  os limites da interface e do instance type.

“Privado” descreve endereçamento, não segurança completa. Uma rota por VPN,
Direct Connect, Transit Gateway, peering ou outra conexão privada ainda pode
tornar o endereço alcançável a partir de outras redes. Security groups, NACLs e
políticas continuam necessários.

### 5.2 Public IPv4 automático

Um public IPv4 automático vem do pool da AWS e **não** fica alocado à sua conta.

- Pode ser atribuído no lançamento, conforme a configuração da subnet e da
  interface.
- É liberado em stop, hibernate ou terminate.
- Um novo endereço normalmente é atribuído no próximo start.
- Não pode ser recuperado depois que volta ao pool.
- O public DNS associado também pode mudar com o endereço.

Na comunicação IPv4, a instância normalmente enxerga seu private IPv4. A
infraestrutura da AWS mantém o mapeamento 1:1 entre o public IPv4 e o private
IPv4 primário. Configurar manualmente o public IPv4 dentro do sistema
operacional é um erro.

Ter public IPv4 também não basta para acesso:

```text
public IPv4
   + rota 0.0.0.0/0 para internet gateway
   + subnet e VPC compatíveis
   + security group
   + network ACL
   + serviço ouvindo
   = caminho potencial de comunicação
```

### 5.3 Elastic IP

Um Elastic IP (EIP) é um public IPv4 estático:

- é alocado à conta em uma Region;
- permanece sob controle da conta até ser liberado;
- pode ser associado a uma instância ou a um private IPv4 de uma ENI;
- pode ser remapeado para outro destino compatível;
- atende integrações que exigem IP público fixo, como uma allowlist externa.

O EIP não torna uma arquitetura altamente disponível sozinho. Se estiver
associado a uma única instância, a aplicação ainda depende dessa instância e,
normalmente, de uma única AZ. Para aplicações web escaláveis, um load balancer,
DNS ou Global Accelerator pode ser mais apropriado que expor instâncias
individualmente.

Todos os public IPv4 fornecidos pela AWS geram cobrança segundo a tabela
vigente. Na data de verificação, o preço era **USD 0,005 por endereço/hora**,
equivalente a cerca de USD 3,60 em 720 horas. Um EIP ocioso continua sendo um
recurso alocado e cobrado; sempre confira a página de preços antes de estimar
um laboratório.

### 5.4 Tabela do ciclo de vida dos endereços

| Evento | Private IPv4 | Public IPv4 automático | Elastic IP associado | IPv6 da ENI |
|---|---|---|---|---|
| reboot | permanece | permanece | permanece | permanece |
| stop/start | permanece | liberado; normalmente recebe outro | permanece associado | permanece |
| hibernate/start | permanece | liberado; normalmente recebe outro | permanece associado | permanece |
| terminate | liberado com a ENI | liberado | desassociado, mas continua alocado até você liberar | liberado com a ENI |

Pegadinha: **desassociar** e **liberar** um Elastic IP são operações diferentes.
Desassociar remove o vínculo; liberar devolve o endereço à AWS.

### Cenário resolvido 1 — Parceiro exige IP fixo

1. **Cenário:** uma instância EBS-backed é parada toda noite.
2. **Requisito:** o firewall do parceiro aceita apenas um IPv4 público fixo.
3. **Palavras decisivas:** *allowlist*, *fixed public IP*, *stop/start*.
4. **Decisão:** associar um Elastic IP, se a integração realmente precisar de
   uma instância com IP público.
5. **Por que não public IPv4 automático:** ele é liberado no stop.
6. **Por que não private IPv4:** não atende uma allowlist da internet.
7. **Trade-off:** cobrança do public IPv4 e dependência de um destino.
8. **Variação:** se houver vários backends e necessidade de alta
   disponibilidade, usar um endpoint de nível superior pode ser melhor.

## 6. Elastic Network Interfaces

Uma ENI é uma placa de rede virtual e um recurso da VPC. Ela pertence a uma
subnet e, portanto, a uma Availability Zone.

Uma ENI pode carregar:

- private IPv4 primário;
- private IPv4 secundários;
- endereços IPv6;
- public IPv4 automático, conforme o caso;
- associações de Elastic IP;
- security groups;
- endereço MAC;
- descrição;
- flag de source/destination check.

Quando uma ENI secundária é destacada e anexada a outra instância, seus atributos
de rede a acompanham. Isso permite mover uma identidade de rede sem reconfigurar
cada atributo separadamente.

### 6.1 Primária versus secundária

| Característica | ENI primária | ENI secundária |
|---|---|---|
| device index | 0 | 1 ou maior |
| existe em toda instância | sim | opcional |
| pode ser destacada durante a vida da instância | não | sim |
| pode ser movida para outra instância | não diretamente | sim, na mesma AZ |
| quantidade | uma | limitada pelo instance type |

Uma ENI secundária só pode ser anexada a uma instância na mesma AZ. Mesmo que
duas AZs estejam na mesma Region e as subnets pertençam à mesma VPC, a ENI não
atravessa a fronteira zonal.

### 6.2 Security groups pertencem à ENI

Na prática, o security group é associado à interface, não ao endereço individual
nem ao volume. Todos os endereços daquela ENI ficam sujeitos aos grupos
associados a ela.

Isso explica por que mover uma ENI secundária também move:

- seus private IPs;
- associações de EIP;
- MAC address;
- security groups.

### 6.3 Source/destination check

Por padrão, a AWS verifica se uma instância é origem ou destino do tráfego que
recebe. Uma instância que atua como roteador, firewall ou NAT precisa encaminhar
pacotes de terceiros; nesse caso, o source/destination check deve ser
desabilitado na ENI apropriada.

Não desabilite esse controle em uma instância comum. A mudança existe para um
caso de rede explícito.

### Cenário resolvido 2 — Failover de appliance na mesma AZ

1. **Cenário:** duas instâncias executam um appliance virtual, uma ativa e outra
   reserva.
2. **Requisito:** mover private IP, MAC e security groups rapidamente.
3. **Restrição:** as instâncias estão na mesma AZ.
4. **Decisão:** usar uma ENI secundária para a identidade do serviço; no
   failover, destacar da instância ativa e anexar à reserva.
5. **Por que não snapshot:** snapshot transfere dados de bloco, não identidade
   de rede.
6. **Por que não ENI primária:** ela não pode ser destacada da instância.
7. **Variação:** entre AZs, usar load balancer, DNS, Global Accelerator ou outro
   mecanismo de failover; a ENI não atravessa AZs.

## 7. Placement groups

Placement groups influenciam onde o EC2 tenta posicionar instâncias. Eles não
alteram o instance type, não fazem replicação de dados e não substituem uma
arquitetura Multi-AZ.

### 7.1 Cluster

```text
uma Availability Zone

[instância][instância][instância][instância]
          proximidade de rede
```

Escolha cluster quando o requisito dominante for:

- baixa latência entre instâncias;
- alta taxa de pacotes ou throughput;
- HPC;
- workload tightly coupled;
- a maior parte do tráfego ocorrer entre os membros.

Trade-offs:

- fica em uma única AZ;
- a proximidade pode aumentar o impacto de falhas correlacionadas;
- pode ocorrer `insufficient capacity`;
- a AWS recomenda lançar as instâncias juntas e usar o mesmo instance type para
  aumentar a chance de posicionamento bem-sucedido;
- após stop/start, o start pode falhar se não houver capacidade compatível.

Cluster não significa “todas no mesmo rack”. Significa proximidade em um
segmento de rede de alta largura de banda.

### 7.2 Partition

```text
partition 1       partition 2       partition 3
[nó][nó][nó]      [nó][nó][nó]      [nó][nó][nó]
 racks próprios    racks próprios    racks próprios
```

Escolha partition para grandes sistemas distribuídos e topology-aware:

- HDFS/Hadoop;
- HBase;
- Cassandra;
- Kafka;
- aplicações que posicionam réplicas conhecendo a partição física.

Cada partição usa um conjunto de racks que não é compartilhado com outra
partição do mesmo grupo. Instâncias **dentro da mesma partição** ainda podem
compartilhar racks.

Características:

- pode abranger várias AZs da mesma Region;
- suporta até sete partições por AZ;
- a quantidade de instâncias é limitada pelas quotas da conta, não pela regra
  de sete do spread;
- a aplicação pode consultar a identificação da partição;
- o EC2 tenta distribuir instâncias, mas não garante distribuição perfeitamente
  uniforme.

### 7.3 Spread

```text
rack A          rack B          rack C          rack D
[crítica 1]     [crítica 2]     [crítica 3]     [crítica 4]
```

Escolha spread para um **pequeno número** de instâncias críticas que precisam
ficar em hardware distinto.

Características do rack-level spread em uma Region:

- pode abranger várias AZs;
- cada instância é colocada em rack distinto dentro do grupo;
- no máximo sete instâncias em execução por AZ por placement group;
- é adequado para poucos componentes independentes;
- capacidade pode não estar disponível ao iniciar uma nova instância.

Não use spread para um cluster de centenas de nós. Use partition quando o
sistema distribuído precisa separar grupos de réplicas em conjuntos de racks.

### 7.4 Precision time — atualização, não foco do bloco

A documentação vigente também apresenta precision time placement groups. Eles
colocam tipos compatíveis em hardware com acesso a fontes locais aprimoradas do
Amazon Time Sync Service, atendendo requisitos de sincronização de relógio com
precisão de microssegundos.

Use a seguinte regra:

```text
latência/throughput entre nós -> cluster
isolamento de partições       -> partition
separação de poucas instâncias -> spread
relógio local de alta precisão -> precision time
```

As questões deste bloco priorizam as três estratégias ensinadas nas aulas.

### 7.5 Comparação

| Estratégia | Prioridade | Escopo | Escala típica | Caso clássico |
|---|---|---|---|---|
| cluster | desempenho de rede | uma AZ | vários nós próximos | HPC |
| partition | isolar grupos de racks | uma ou mais AZs | grande cluster | Kafka/Cassandra/Hadoop |
| spread | separar cada instância | uma ou mais AZs | até 7/AZ/grupo | poucos nós críticos |
| precision time | relógio de alta precisão | hardware compatível | requisito especializado | timestamps e ordenação |

### Cenário resolvido 3 — Escolha de placement strategy

Uma empresa apresenta três workloads:

1. simulação HPC com tráfego intenso entre 40 nós na mesma AZ;
2. Kafka com centenas de brokers e réplicas conscientes da topologia;
3. quatro servidores de controle independentes que não podem compartilhar
   hardware.

Decisões:

- HPC → cluster;
- Kafka → partition;
- quatro servidores críticos → spread.

O requisito determina a resposta. “Alta disponibilidade” sozinho não torna
spread a escolha universal, e “alto desempenho” sozinho não torna cluster
adequado quando a aplicação precisa sobreviver à falha de uma AZ.

## 8. Reboot, stop, hibernate e terminate

| Operação | RAM/processos | EBS | Instance store | Private IP | Public IP automático | Compute |
|---|---|---|---|---|---|---|
| reboot | reiniciados | permanece | permanece | permanece | permanece | cobrado |
| stop/start | perdidos | permanece | dados perdidos | permanece | muda | não cobrado enquanto stopped |
| hibernate/start | salvos e restaurados | permanece, incluindo RAM no root | dados perdidos | permanece | muda | não cobrado enquanto stopped |
| terminate | perdidos | segue `DeleteOnTermination` | perdido | liberado | liberado | encerrado |

“Compute não cobrado” não significa custo zero. Enquanto a instância está
stopped ou hibernated, continuam possíveis:

- cobrança dos volumes EBS;
- cobrança dos snapshots;
- cobrança do Elastic IP ou outro public IPv4 alocado;
- compromissos de Savings Plans ou Reserved Instances.

## 9. EC2 Hibernate

Hibernar é executar suspend-to-disk:

1. o EC2 sinaliza o sistema operacional;
2. processos são congelados;
3. a RAM é gravada no EBS root volume;
4. a instância é desligada e entra em `stopped`;
5. no start, o sistema lê a RAM salva;
6. os processos continuam do ponto em que estavam.

Casos adequados:

- aplicação demora muito para aquecer cache em memória;
- ambiente de desenvolvimento possui estado complexo;
- processo precisa continuar sem reconstruir todo o contexto;
- boot comum é mais lento que restaurar o estado salvo.

Hibernar não é backup. Uma falha, corrupção lógica ou exclusão ainda exige
snapshot, AMI, replicação ou outra estratégia de proteção.

### 9.1 Pré-requisitos

- habilitar hibernação **durante o lançamento**;
- AMI HVM compatível;
- instance type e Region compatíveis;
- EBS como root volume;
- root volume criptografado;
- espaço no root suficiente para sistema, aplicação e conteúdo da RAM;
- tipo de volume root compatível, como `gp2`, `gp3`, `io1` ou `io2`;
- respeitar limites vigentes de RAM e sistema operacional.

Não é possível habilitar hibernação depois que a instância já existe. Além
disso, uma instância hibernada possui mais restrições de modificação que uma
instância apenas parada. Hibernação também não é suportada para uma instância
que integra um Auto Scaling group ou é usada pelo Amazon ECS. Criar snapshot ou
AMI de uma instância hibernada — ou habilitada para hibernação — pode produzir
uma imagem da qual não seja possível conectar corretamente; não combine esses
experimentos no mesmo recurso.

### 9.2 Comportamento que costuma cair

- EBS permanece.
- Conteúdo de instance store é perdido.
- Private IPv4 e IPv6 permanecem.
- Public IPv4 automático é liberado e muda no start.
- Elastic IP permanece associado e cobrado.
- A AWS não cobra compute enquanto a instância está em `stopped`.
- O espaço EBS usado para guardar a RAM continua cobrado.
- A permanência contínua em hibernação é limitada a 60 dias na documentação
  vigente.

## 10. Amazon EBS: armazenamento de bloco zonal

Amazon Elastic Block Store oferece volumes de bloco independentes do host da
instância.

```text
Availability Zone A
├── EC2 instance
└── EBS volume ── attach ── EC2

Availability Zone B
└── o volume da AZ A não pode ser anexado diretamente aqui
```

Características:

- o volume pertence a uma AZ;
- é replicado dentro dessa AZ pela infraestrutura do serviço;
- pode ser anexado somente a instâncias compatíveis na mesma AZ;
- persiste em stop/start;
- pode persistir depois de terminate;
- pode ser destacado e anexado a outra instância na mesma AZ;
- continua cobrado até ser excluído, mesmo em estado `available`.

EBS é armazenamento de bloco, como um disco virtual. Depois de anexá-lo, o
sistema operacional ainda precisa reconhecer o device, criar filesystem quando
necessário e montá-lo. “Attached” no console não significa “arquivo já visível”.

Os tipos de volume, IOPS, throughput, Multi-Attach e criptografia serão
aprofundados no B05.

### 10.1 Root versus data volume

| Volume | Default comum no lançamento | Efeito do terminate |
|---|---|---|
| EBS root | `DeleteOnTermination=true` | excluído |
| EBS adicional criado no lançamento | `DeleteOnTermination=false` | preservado |
| EBS anexado depois | não depende do ciclo da instância | preservado |

Esses defaults podem ser alterados. Leia a configuração real do block device
mapping em vez de confiar apenas na regra geral.

Stop não consulta `DeleteOnTermination`: ambos os volumes permanecem. A flag é
avaliada quando a instância é terminada.

### Cenário resolvido 4 — Terminação com dois volumes

Uma instância possui:

- root: `DeleteOnTermination=true`;
- data: `DeleteOnTermination=false`.

Ao parar, os dois volumes permanecem. Ao terminar, o root é excluído e o data
continua em estado `available`, gerando cobrança até ser reutilizado ou excluído.

Se o enunciado exige preservar o sistema inteiro, confirme a flag do root ou
faça snapshot/AMI antes da terminação. Se exige cleanup completo, procure também
volumes adicionais que sobreviveram.

## 11. EBS snapshots

Um snapshot EBS é um backup point-in-time dos blocos de um volume.

- O primeiro snapshot armazena os blocos existentes.
- Snapshots seguintes armazenam somente blocos novos ou alterados.
- Cada snapshot continua sendo um ponto lógico completo de restauração.
- O serviço armazena os dados em Amazon S3, mas não em um bucket visível ou
  administrado pelo cliente.
- O snapshot é regional.
- A partir dele, é possível criar um novo volume em qualquer AZ da Region.
- Para outra Region, copie o snapshot ou a AMI que o utiliza.

### 11.1 Incremental não significa dependência frágil

Considere:

```text
S1: blocos A B C D
S2: mudou C
S3: mudou D
```

Excluir S1 não quebra S2 nem S3. A AWS remove somente blocos que não são mais
referenciados. Os dados necessários a snapshots posteriores são preservados.

Por isso:

- um snapshot posterior continua restaurável;
- excluir um snapshot antigo pode liberar menos espaço que o esperado;
- não se deve estimar economia apenas pelo tamanho lógico do volume.

### 11.2 Consistência

É possível solicitar um snapshot enquanto o volume está em uso, mas o snapshot
captura blocos gravados até aquele momento. Dados ainda em memória ou em buffers
da aplicação podem não estar incluídos.

Para maior consistência:

1. pause gravações;
2. faça flush dos buffers;
3. congele ou desmonte o filesystem, quando apropriado;
4. para root volume, considere parar a instância;
5. em aplicações com vários volumes, use um processo coordenado ou snapshots
   multi-volume crash-consistent.

Um snapshot `pending` já foi aceito pelo serviço, mas a cópia de blocos ainda
está em andamento. Não o trate como concluído até o estado `completed`.

### 11.3 Relações de ciclo de vida

| Operação | O outro recurso é excluído? |
|---|---|
| excluir volume | snapshots existentes permanecem |
| excluir snapshot | volume original permanece |
| criar volume do snapshot | snapshot permanece |
| terminar instância | snapshots permanecem |

Snapshots continuam cobrados até serem excluídos ou arquivados conforme uma
política consciente. Nunca exclua snapshots apenas pelo tamanho ou pela idade;
confirme owner, tags, dependências de AMIs e política de retenção.

### Cenário resolvido 5 — Recuperar em outra AZ

1. **Cenário:** o volume está na AZ A e a instância de recuperação na AZ B.
2. **Requisito:** recuperar os dados na mesma Region.
3. **Restrição:** EBS volume é zonal.
4. **Decisão:** usar um snapshot e criar um **novo volume** na AZ B.
5. **Por que não attach direto:** um volume da AZ A não atravessa AZ.
6. **Por que não copiar para outra Region:** as duas AZs já pertencem à mesma
   Region.
7. **Variação:** recuperação em outra Region exige copiar snapshot, AMI ou usar
   replicação apropriada.

## 12. Amazon Machine Images

Uma AMI é um modelo regional usado para lançar instâncias. Em uma AMI
EBS-backed, o conjunto inclui:

- permissões de lançamento;
- block device mapping;
- snapshot do root volume;
- snapshots de volumes EBS adicionais incluídos;
- metadados de registro.

```text
instância configurada
      │ Create image
      ▼
AMI regional
├── metadados
├── root snapshot
└── snapshots adicionais
      │ Run instances
      ▼
novas instâncias
```

Uma AMI é útil para:

- padronizar sistemas operacionais e software;
- acelerar lançamentos repetidos;
- criar uma golden image controlada;
- reproduzir uma configuração;
- apoiar recuperação e implantação em outra Region após cópia.

### 12.1 Criação e consistência

Ao criar uma AMI EBS-backed pelo processo padrão, o EC2 reinicia a instância
para garantir um estado consistente dos volumes antes dos snapshots. A opção de
não reiniciar reduz indisponibilidade, mas aumenta o risco de inconsistência de
filesystem ou aplicação.

Uma AMI não é substituto automático para:

- backup frequente de dados;
- configuração reproduzível por código;
- patching contínuo;
- replicação de banco;
- estratégia Multi-AZ.

Ela captura uma imagem em um momento específico.

### 12.2 Escopo regional

AMI IDs são regionais. Uma AMI criada em `eu-west-1` não pode ser usada
diretamente em `us-east-1`.

Processo:

```text
AMI origem em Region A
     │ Copy AMI
     ▼
nova AMI + novos snapshots em Region B
     │
     ▼
lançar instâncias em Region B
```

A cópia pode gerar cobrança de transferência e armazenamento de snapshots.
Criptografia e permissões de KMS também precisam ser compatíveis.

### 12.3 Deregister não é cleanup completo

Desregistrar uma AMI:

- impede novos lançamentos por aquela AMI;
- não termina instâncias que já foram lançadas;
- não exclui automaticamente todos os snapshots em todos os fluxos;
- não remove cópias da AMI em outras Regions;
- pode deixar cobrança de snapshots.

O console e as APIs atuais oferecem opções de exclusão associada em alguns
fluxos, mas a auditoria continua obrigatória. Um cleanup seguro verifica
separadamente:

1. AMIs próprias;
2. snapshots próprios;
3. cópias em outras Regions;
4. permissões e chaves KMS, se aplicável.

Snapshots que sustentam uma AMI registrada normalmente não podem ser excluídos
até a AMI ser desregistrada.

### Cenário resolvido 6 — Imagem customizada em outra Region

1. **Cenário:** uma AMI customizada existe em `eu-west-1`.
2. **Requisito:** lançar a mesma base em `us-east-1`.
3. **Palavras decisivas:** *AMI*, *another Region*.
4. **Decisão:** copiar a AMI para `us-east-1` e lançar pela nova AMI regional.
5. **Por que não usar o mesmo AMI ID:** IDs e recursos são regionais.
6. **Por que não mover o volume:** EBS é zonal e não atravessa Regions.
7. **Trade-off:** novos snapshots, transferência, armazenamento e governança da
   imagem copiada.

## 13. Tabela de decisão consolidada

| Requisito | Melhor ponto de partida | Limite ou trade-off |
|---|---|---|
| comunicação interna estável | private IPv4/DNS privado | exige caminho de rede |
| IPv4 público temporário | public IPv4 automático | muda em stop/hibernate |
| IPv4 público fixo para allowlist | Elastic IP | custo e dependência de endpoint |
| mover identidade de rede na mesma AZ | ENI secundária | não atravessa AZ |
| baixa latência entre nós | cluster placement group | uma AZ e risco correlacionado |
| grande cluster topology-aware | partition placement group | aplicação deve usar a topologia |
| poucos nós em hardware distinto | spread placement group | máximo 7/AZ/grupo |
| retomar RAM e processos | hibernate | compatibilidade, EBS e limite temporal |
| disco persistente de uma instância | EBS | volume é zonal |
| recuperar EBS em outra AZ | snapshot → novo volume | tempo e cobrança de storage |
| replicar imagem em outra Region | copy AMI | novos snapshots e custo |
| apagar imagem sem resíduos | deregister + auditar snapshots | cuidado com dependências |

## 14. Armadilhas de prova

1. Private IPv4 permanece em stop/start; public IPv4 automático normalmente
   muda.
2. Reboot não libera o public IPv4.
3. Elastic IP é estático, mas não é gratuito por estar associado.
4. Desassociar EIP não é liberá-lo.
5. Public IP não substitui internet gateway, rota ou security group.
6. O sistema operacional não configura diretamente o public IPv4 mapeado.
7. ENI pertence à subnet e à AZ.
8. A ENI primária não pode ser destacada.
9. Uma ENI secundária move IPs e security groups na mesma AZ.
10. Security group é associado à ENI, não ao volume.
11. Source/destination check só deve ser desabilitado para encaminhamento de
    tráfego.
12. Cluster prioriza desempenho, não isolamento.
13. Cluster não atravessa AZs.
14. Partition separa grupos de racks; membros da mesma partição ainda podem
    compartilhar hardware.
15. Spread é para poucos nós críticos e possui limite de sete por AZ por grupo.
16. Placement group não replica dados.
17. Stop preserva EBS, mas não preserva RAM.
18. Hibernate preserva RAM no EBS root, não em instance store.
19. Hibernação deve ser habilitada no lançamento.
20. Instância stopped/hibernated não cobra compute, mas storage e IPv4 podem
    continuar cobrados.
21. `DeleteOnTermination` atua em terminate, não em stop.
22. Root EBS costuma ser apagado por default; data volume costuma permanecer.
23. EBS volume não atravessa AZs.
24. Snapshot é regional e pode criar volume em qualquer AZ da Region.
25. Snapshot incremental continua sendo um ponto lógico completo.
26. Excluir o primeiro snapshot não invalida snapshots posteriores.
27. Excluir volume não exclui snapshots.
28. AMI é regional; para outra Region, copie.
29. Deregister de AMI não afeta instâncias existentes.
30. Deregister não deve ser tratado como prova de que os snapshots sumiram.

## 15. Custos e cleanup

Itens que podem cobrar sem uma instância em execução:

- EBS volumes, inclusive `available`;
- EBS snapshots;
- snapshots mantidos por AMIs próprias;
- public IPv4 e Elastic IP;
- cópias em outras Regions;
- compromissos financeiros já adquiridos.

O LAB B04 não cria recursos. Ele apenas lê o inventário da Region, observa
configurações e produz um diagrama. Não exclua recursos preexistentes durante
esse exercício.

No B05, quando houver volume e snapshot controlados, o cleanup exigirá IDs e
tags exatos. Nunca exclua um volume, ENI, snapshot ou AMI apenas porque “parece
ser do laboratório”.

## 16. Checklist de domínio

- [ ] Prevejo os endereços depois de reboot, stop, hibernate e terminate.
- [ ] Sei quando um Elastic IP é necessário e quando é uma solução frágil.
- [ ] Explico ENI primária versus secundária.
- [ ] Sei por que uma ENI não pode atravessar AZ.
- [ ] Escolho cluster, partition ou spread pelas palavras decisivas.
- [ ] Reconheço precision time sem confundi-lo com as três estratégias do curso.
- [ ] Distingo reboot, stop, hibernate e terminate.
- [ ] Explico os pré-requisitos da hibernação.
- [ ] Sei que EBS volume é zonal e snapshot é regional.
- [ ] Aplico `DeleteOnTermination` ao volume correto.
- [ ] Explico incremental storage versus restore point completo.
- [ ] Recupero conceitualmente EBS em outra AZ.
- [ ] Copio uma AMI antes de usá-la em outra Region.
- [ ] Audito snapshots depois de desregistrar uma AMI.

## 17. Recuperação ativa

Responda sem consultar:

1. O que acontece com cada tipo de endereço em stop/start?
2. Por que o public IPv4 automático não serve para uma allowlist permanente?
3. Quais quatro componentes, além do IP, permitem acesso pela internet?
4. Quais atributos acompanham uma ENI secundária?
5. Por que a ENI primária não resolve o failover proposto entre duas instâncias?
6. Qual placement group atende HPC tightly coupled?
7. Qual atende Kafka topology-aware e por quê?
8. Qual atende quatro instâncias críticas e qual é seu limite clássico?
9. O que precision time resolve?
10. Quais dados hibernate preserva e perde?
11. Por que o root volume precisa de espaço adicional e criptografia?
12. O que continua cobrando durante `stopped`?
13. Qual a diferença de escopo entre EBS volume e snapshot?
14. O que `DeleteOnTermination=false` faz em stop e terminate?
15. Por que excluir o primeiro snapshot não quebra o segundo?
16. Como recuperar um volume em outra AZ?
17. Quais elementos compõem uma AMI EBS-backed?
18. Como usar uma AMI em outra Region?
19. Por que deregister não encerra o cleanup?

## 18. Ligações deste bloco

- [Laboratório B04](../../05_Laboratorios/LAB_B04_Inventario_EC2_ENI_EBS_e_AMI.md)
- [Questões B04](../../04_Questoes_e_Revisoes/Blocos/B04_Questoes.md)
- [Gabarito B04](../../04_Questoes_e_Revisoes/Blocos/B04_Gabarito.md)
- [Revisões B04](../../06_Progresso/B04_Checklist_e_Revisoes.md)

## 19. Referências oficiais

- [EC2 instance IP addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html)
- [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
- [Public IPv4 pricing](https://aws.amazon.com/vpc/pricing/)
- [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)
- [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
- [Placement strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html)
- [Stop and start EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)
- [How stop and start work](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html)
- [Hibernate an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html)
- [How hibernation works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-hibernate-overview.html)
- [Hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html)
- [Amazon EBS features](https://docs.aws.amazon.com/ebs/latest/userguide/EBSFeatures.html)
- [EBS volume lifecycle](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-lifecycle.html)
- [Attach an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-attaching-volume.html)
- [How EBS snapshots work](https://docs.aws.amazon.com/ebs/latest/userguide/how_snapshots_work.html)
- [Create an EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-snapshot.html)
- [Delete an EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-snapshot.html)
- [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [Create an EBS-backed AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html)
- [Copy an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html)
- [Deregister an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html)

**Referências verificadas em:** 24/07/2026.
