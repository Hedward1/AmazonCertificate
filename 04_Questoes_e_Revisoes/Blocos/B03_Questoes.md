# B03 — Questões: conexões EC2, instance roles e opções de compra

**Quantidade:** 10 questões autorais  
**Idioma:** 6 em português e 4 em inglês  
**Regra:** selecione uma resposta em cada questão  
**Tempo sugerido:** 15 minutos; registre sua confiança antes de corrigir  
**Gabarito:** [arquivo separado](B03_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B03-01 | 1.2 | SSH e security group | Situacional | Básica | Português |
| B03-02 | 1.2 | EC2 Instance Connect | Fundamental | Intermediária | Português |
| B03-03 | 1.2 | Session Manager | Situacional | Intermediária | Português |
| B03-04 | 1.1 | EC2 instance role | Situacional | Básica | Português |
| B03-05 | 4.2 | On-Demand Instances | Situacional | Básica | Português |
| B03-06 | 4.2 | Compute Savings Plans | Situacional | Intermediária | Português |
| B03-07 | 4.2 | Spot e EC2 Fleet | Situacional | Intermediária | Inglês |
| B03-08 | 4.2 | Zonal Reserved Instance | Situacional | Avançada | Inglês |
| B03-09 | 4.2 | Dedicated Hosts | Situacional | Intermediária | Inglês |
| B03-10 | 4.2 | Dedicated Instances | Situacional | Intermediária | Inglês |

## Questões

### B03-01

Uma instância EC2 Linux tem um endereço IPv4 público. A tabela de rotas e a
network ACL estão corretas, mas o administrador não consegue estabelecer uma
conexão SSH. O security group permite somente HTTPS, e o endereço IPv4 público
do administrador é `198.51.100.20`.

O administrador precisa restaurar o acesso SSH convencional usando o key pair
existente. Qual solução é a mais segura?

- A. Permitir TCP 22 de `0.0.0.0/0` e conectar-se como `root`.
- B. Permitir TCP 3389 de `198.51.100.20/32`.
- C. Permitir TCP 22 de `198.51.100.20/32` e verificar o arquivo de chave
  privada e o nome de usuário correspondente à AMI.
- D. Adicionar somente uma regra de saída TCP 22 ao security group.

### B03-02

Uma empresa quer permitir que administradores autorizados usem EC2 Instance
Connect para acessar instâncias Linux, sem distribuir permanentemente uma chave
SSH privada comum a toda a equipe.

Qual afirmação descreve corretamente o funcionamento do serviço?

- A. Uma chamada autorizada pelo IAM envia uma chave SSH pública para os
  metadados da instância por 60 segundos; ainda é necessário existir um caminho
  de rede para a conexão SSH.
- B. O serviço grava uma chave privada permanente na AMI da instância.
- C. EC2 Instance Connect não utiliza SSH e, portanto, uma conexão direta nunca
  precisa alcançar a porta 22.
- D. O serviço é destinado somente a instâncias Windows que utilizam RDP.

### B03-03

Uma instância EC2 Linux está em uma subnet privada, sem endereço IP público. A
política de segurança proíbe portas administrativas de entrada e o uso de
bastion hosts. Os administradores precisam obter um shell interativo com
controle de acesso pelo IAM.

Qual solução atende melhor aos requisitos?

- A. Usar EC2 Instance Connect diretamente pela internet, sem um EC2 Instance
  Connect Endpoint.
- B. Adicionar uma regra de entrada SSH de `0.0.0.0/0` e associar um Elastic IP.
- C. Migrar a instância para um Dedicated Host, pois isso cria automaticamente
  um canal administrativo.
- D. Usar AWS Systems Manager Session Manager, com SSM Agent, uma instance role
  adequada e conectividade de saída aos endpoints do Systems Manager.

### B03-04

Uma aplicação executada em uma instância EC2 precisa gravar itens em uma tabela
específica do DynamoDB. A equipe quer evitar o armazenamento e a rotação manual
de access keys.

Qual abordagem é a mais apropriada?

- A. Salvar as access keys do root user em `/etc/environment`.
- B. Associar uma IAM role por meio de um instance profile, conceder somente as
  ações necessárias na tabela e permitir que o SDK obtenha credenciais
  temporárias pelo Instance Metadata Service.
- C. Inserir access keys permanentes no EC2 user data.
- D. Usar a chave privada do EC2 key pair para assinar as requisições ao
  DynamoDB.

### B03-05

Uma empresa executará um teste de migração que utilizará aproximadamente 20
instâncias EC2 durante dez dias. A duração e o número exato de instâncias ainda
podem mudar. A execução não pode sofrer interrupções e a empresa não quer
assumir um compromisso de um ou três anos.

Qual opção de compra é a mais apropriada?

- A. Standard Reserved Instances com compromisso de três anos.
- B. Spot Instances em um único capacity pool.
- C. On-Demand Instances.
- D. Dedicated Hosts reservados por três anos.

### B03-06

Uma empresa possui uso de computação estável e consegue assumir um compromisso
de gasto em USD por hora durante três anos. Entretanto, durante esse período, a
aplicação poderá mudar:

- entre famílias de instâncias EC2;
- entre AWS Regions;
- de EC2 para AWS Fargate ou AWS Lambda.

Qual modelo oferece o melhor alinhamento entre desconto por compromisso e
flexibilidade?

- A. Standard Reserved Instance para uma configuração EC2 específica.
- B. Compute Savings Plan.
- C. On-Demand Instances sem nenhum compromisso.
- D. EC2 Instance Savings Plan para uma família específica em uma única Region.

### B03-07

A company runs a large batch-processing job. Each task stores checkpoints in
durable storage and can be retried on another instance. Start and completion
times are flexible. The company wants to minimize EC2 cost while reducing the
likelihood that many workers are interrupted together.

Which solution is the best fit?

- A. Run all workers as On-Demand Instances in one Availability Zone.
- B. Allocate Dedicated Hosts and place every worker on the same host.
- C. Request one Spot instance type in one Availability Zone using the
  lowest-price-only strategy, without processing interruption notices.
- D. Use Spot capacity through EC2 Fleet or an Auto Scaling group, allow
  multiple instance types and Availability Zones, use the
  price-capacity-optimized strategy, and handle interruption notifications.

### B03-08

A non-interruptible EC2 workload will use the same instance type, platform, and
tenancy in a specific Availability Zone for three years. The company requires
both a committed-use discount and reserved capacity in that Availability Zone.

Which option best meets the requirements?

- A. Purchase a matching Zonal Reserved Instance.
- B. Purchase a Compute Savings Plan only.
- C. Purchase a Regional Reserved Instance.
- D. Continue using On-Demand Instances without a Capacity Reservation.

### B03-09

A company is migrating a commercial database whose existing license is tied to
physical processor sockets and cores. The company must identify the physical
host and control instance placement for license compliance.

Which EC2 tenancy option should the solutions architect choose?

- A. Dedicated Instances.
- B. Shared-tenancy On-Demand Instances.
- C. Dedicated Hosts.
- D. Spot Instances in a placement group.

### B03-10

A regulatory requirement states that a company's EC2 instances must not share
physical host hardware with instances from other AWS accounts. The company does
not need socket visibility, host affinity, targeted host placement, or
per-core BYOL support. It prefers per-instance billing.

Which option is the best fit?

- A. A cluster placement group on shared-tenancy instances.
- B. Dedicated Instances.
- C. Dedicated Hosts.
- D. A Compute Savings Plan on shared-tenancy instances.

## Registro antes de corrigir

| ID | Resposta | Confiança (alta/média/baixa) | Palavra decisiva |
|---|---|---|---|
| B03-01 |  |  |  |
| B03-02 |  |  |  |
| B03-03 |  |  |  |
| B03-04 |  |  |  |
| B03-05 |  |  |  |
| B03-06 |  |  |  |
| B03-07 |  |  |  |
| B03-08 |  |  |  |
| B03-09 |  |  |  |
| B03-10 |  |  |  |
