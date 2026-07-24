# B03 — Conexão ao EC2, instance roles e modelos de compra

**Data planejada:** 28/07/2026  
**Nível:** iniciante absoluto  
**Aulas relacionadas:** 36–46  
**Domínios oficiais:** 1 — Design Secure Architectures; 3 — Design
High-Performing Architectures; 4 — Design Cost-Optimized Architectures  
**Tarefas principais:** 1.1 — Design secure access to AWS resources; 1.2 —
Design secure workloads and applications; 3.2 — Design high-performing and
elastic compute solutions; 4.2 — Design cost-optimized compute solutions  
**Pré-requisito:** [B02 — IAM aplicado, AWS CLI, EC2 e security
groups](B02_IAM_Aplicado_CLI_EC2_e_Security_Groups.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá conseguir:

1. separar autenticação no sistema operacional de autorização nas APIs da AWS;
2. diagnosticar uma falha de SSH em uma sequência lógica;
3. explicar como EC2 Instance Connect combina IAM, uma chave temporária e SSH;
4. escolher entre SSH, EC2 Instance Connect e Session Manager;
5. explicar como uma aplicação em EC2 recebe credenciais temporárias de uma
   instance role;
6. distinguir On-Demand, Savings Plans, Reserved Instances e Spot;
7. diferenciar desconto de preço de reserva de capacidade;
8. escolher entre Dedicated Host e Dedicated Instance;
9. reconhecer workloads adequados e inadequados para Spot;
10. lançar e terminar uma instância de laboratório sem deixar recursos
    residuais.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 36 — Security Groups Hands On | executar no LAB B03 |
| 37 — SSH Overview | estudar integralmente |
| 38 — SSH no Linux/macOS | acelerar os comandos específicos da plataforma |
| 39–40 — SSH no Windows | estudar; Windows é o ambiente deste projeto |
| 41 — SSH Troubleshooting | usar como checklist de diagnóstico |
| 42 — EC2 Instance Connect | estudar e comparar com Session Manager |
| 43 — EC2 Instance Roles Demo | estudar integralmente |
| 44 — EC2 purchasing options | alta prioridade para a prova |
| 45 — Spot Instances e Spot Fleet | estudar Spot; aplicar a atualização de 2026 |
| 46 — Launch Types Hands On | acompanhar no console; não comprar compromissos |

As aulas de SSH para Linux, macOS e Windows repetem o mesmo modelo mental. Não é
necessário refazer o laboratório em três sistemas operacionais. Concentre-se em
rede, porta, usuário da AMI, chave e método de conexão.

### Atualizações importantes em 2026

- **Session Manager** deve entrar na comparação mesmo que a aula se concentre
  em SSH e EC2 Instance Connect. Ele permite administração controlada por IAM
  sem abrir portas de entrada e sem administrar SSH keys.
- **Spot Fleet usa uma API legada sem investimento planejado.** Em novos
  projetos, a AWS recomenda Amazon EC2 Auto Scaling para gerenciar o ciclo de
  vida ou EC2 Fleet quando o próprio cliente o gerencia.
- A própria documentação da AWS recomenda **Savings Plans** como opção mais
  simples e flexível que Reserved Instances para desconto de compute. Reserved
  Instances continuam relevantes para a prova, principalmente para entender
  escopo regional versus zonal.
- O laboratório usa **Amazon Linux 2023**, exige **IMDSv2**, não abre SSH e
  termina a instância no mesmo exercício.
- Um endereço IPv4 público é cobrado por segundo, com mínimo de 60 segundos. O
  LAB B03 o usa por pouco tempo e não cria Elastic IP.

## 3. Vocabulário essencial

| Inglês | Significado no cenário |
|---|---|
| key pair | par de chaves usado para acesso ao sistema operacional |
| private key | segredo mantido pelo administrador |
| public key | parte colocada ou enviada à instância |
| inbound rule | regra para tráfego que entra |
| source IP | endereço de origem permitido |
| instance profile | contêiner que entrega uma IAM role ao EC2 |
| temporary credentials | access key, secret key e token com expiração |
| no long-term commitment | sem compromisso de um ou três anos |
| steady-state usage | uso estável e previsível |
| fault-tolerant | tolera falha ou interrupção |
| interruption notice | aviso de interrupção de Spot |
| spare capacity | capacidade ociosa oferecida como Spot |
| single-tenant hardware | host físico não compartilhado com outras contas |
| host affinity | associação da instância a um host específico |
| bring your own license (BYOL) | uso de licença própria |

Palavras decisivas costumam selecionar a resposta antes dos detalhes:

```text
short-term + unpredictable + cannot be interrupted       -> On-Demand
steady commitment + flexibility                           -> Savings Plans
interruptible + stateless + checkpoint                    -> Spot
physical sockets/cores + BYOL + placement control         -> Dedicated Host
single-tenant + no host visibility needed                 -> Dedicated Instance
```

## 4. O acesso possui camadas independentes

Conseguir “entrar na instância” depende de mais de um controle:

```text
identidade do administrador
        │
        ├── IAM autoriza a operação do serviço?
        │
        ▼
método: SSH / EC2 Instance Connect / Session Manager
        │
        ├── existe caminho de rede?
        ├── security group e NACL permitem?
        ├── agente ou daemon está funcionando?
        └── usuário/chave estão corretos?
```

Essas camadas não se substituem:

- uma IAM policy não abre a porta 22;
- uma regra de security group não autoriza `ec2-instance-connect:SendSSHPublicKey`;
- um key pair não permite chamar APIs do DynamoDB;
- uma IAM role da instância não é a identidade humana que iniciou a conexão.

## 5. SSH convencional

### 5.1 O que acontece

SSH cria uma conexão criptografada entre um cliente e o daemon SSH da instância.
Para uma instância Linux pública, normalmente são necessários:

1. estado `running` e status checks aprovados;
2. public IPv4 ou IPv6 e caminho de rede compatível;
3. subnet pública com rota para um internet gateway, no caso de IPv4 público;
4. inbound TCP 22 somente da origem administrativa necessária;
5. network ACL e firewall do sistema operacional compatíveis;
6. chave privada correspondente à chave pública da instância;
7. nome de usuário correto para a AMI.

Usuários comuns:

| AMI | Usuário frequente |
|---|---|
| Amazon Linux 2023 | `ec2-user` |
| Ubuntu | `ubuntu` |
| Debian | `admin` em imagens compatíveis |
| RHEL | `ec2-user` ou `root`, conforme a imagem |

Sempre confirme a documentação da AMI. Tentar `administrator`, o e-mail da
conta AWS ou o nome do IAM user não autentica o sistema operacional Linux.

### 5.2 Key pair não é IAM

No lançamento, o EC2 coloca a chave pública na instância. A chave privada fica
com o administrador.

- A AWS não mantém uma cópia recuperável da chave privada criada para download.
- Perder a chave privada não é resolvido criando uma IAM policy.
- Compartilhar uma mesma chave privada reduz a responsabilização individual.
- Não envie `.pem` ou `.ppk` por chat, e-mail ou repositório.

O key pair autentica o login no sistema operacional. IAM autentica e autoriza
chamadas às APIs da AWS.

### 5.3 Windows atual

O Windows possui cliente OpenSSH opcional ou instalado por padrão em versões
recentes. Um comando conceitual seria:

```powershell
ssh -i C:\caminho\chave.pem ec2-user@NOME_DNS_OU_IP
```

Antes de executar:

- confirme que o arquivo é a chave do laboratório;
- não coloque a chave dentro desta pasta sincronizada pelo OneDrive;
- não exponha o caminho, IP ou DNS em evidências públicas;
- restrinja TCP 22 ao seu IPv4 público `/32`.

PuTTY e arquivos `.ppk` continuam possíveis, mas não são um requisito
arquitetural da prova. São apenas ferramentas do cliente.

### 5.4 Diagnóstico de SSH

Use esta ordem para não alterar controles ao acaso:

| Sintoma/verificação | Pergunta |
|---|---|
| estado e status checks | a instância terminou o boot e está saudável? |
| endereço | há IP público ou conectividade privada até o destino? |
| rota | a subnet possui o caminho esperado? |
| security group | TCP 22 permite exatamente a origem necessária? |
| network ACL | entrada e retorno estão permitidos? |
| firewall/daemon | `sshd` está ativo e ouvindo? |
| usuário | corresponde à AMI? |
| chave | é a chave privada correta e está protegida? |

Interpretação útil:

- **timeout:** normalmente aponta para caminho de rede, rota, security group,
  NACL, firewall ou serviço indisponível;
- **permission denied:** o caminho chegou ao SSH, mas usuário, chave ou
  configuração de autenticação não foram aceitos;
- **host key warning:** a identidade criptográfica do host mudou; investigue
  antes de ignorar o aviso.

Não “resolva” um timeout abrindo todas as portas para `0.0.0.0/0`.

## 6. EC2 Instance Connect

O EC2 Instance Connect evita distribuir uma chave SSH privada permanente entre
administradores.

Fluxo simplificado:

```text
administrador
   │ chamada autorizada por IAM
   ▼
EC2 Instance Connect envia chave pública temporária
   │ disponível por 60 segundos para iniciar o login
   ▼
instância Linux ── sessão SSH
```

Pontos obrigatórios:

- a chave enviada é **pública**, não privada;
- a autorização de envio usa IAM;
- a imagem precisa ter o EC2 Instance Connect instalado e configurado;
- a conexão estabelecida continua sendo SSH;
- ainda é necessário caminho de rede e inbound TCP 22;
- os 60 segundos limitam o período para iniciar a autenticação, não a duração
  da sessão já estabelecida.

### 6.1 Conexão pelo console com IP público

Para a experiência do console:

- a instância precisa de public IPv4 ou IPv6;
- o navegador alcança o proxy regional do serviço;
- o security group deve permitir TCP 22 a partir da **AWS-managed prefix list**
  do EC2 Instance Connect da Region.

O tráfego não se origina simplesmente do IP do navegador. Essa é uma diferença
importante em relação ao cliente SSH executado diretamente no computador.

### 6.2 Instância somente privada

Uma instância sem endereço público ainda precisa de caminho privado. As opções
incluem:

- conectividade corporativa por VPN ou Direct Connect;
- um EC2 Instance Connect Endpoint;
- Session Manager.

Criar um EC2 Instance Connect Endpoint não torna a instância pública. Ele
fornece um caminho controlado para a conexão privada e exige configuração de
IAM, endpoint e security groups.

## 7. AWS Systems Manager Session Manager

Session Manager é uma alternativa moderna para shell administrativo:

- não requer inbound 22 ou 3389;
- não exige bastion host;
- não exige distribuir SSH keys;
- usa IAM para controlar quem inicia a sessão;
- permite terminal pelo console ou pela CLI;
- pode integrar logs e auditoria, conforme a configuração.

Pré-requisitos típicos:

1. SSM Agent instalado e em execução;
2. instance profile com permissões, como
   `AmazonSSMManagedInstanceCore`;
3. conectividade HTTPS de saída para os endpoints necessários, diretamente,
   via NAT ou por VPC endpoints;
4. permissões IAM para o operador iniciar e encerrar sessões.

Uma subnet privada não significa “sem conectividade”. O agente ainda precisa
alcançar os serviços do Systems Manager. Se o requisito proíbe internet, use os
VPC endpoints necessários em vez de abrir uma porta de entrada.

`ssm:StartSession` concede acesso interativo ao sistema operacional e deve ser
restrito por identidade e recurso. O fato de não existir uma porta inbound não
torna essa permissão inofensiva.

### 7.1 Comparação de métodos

| Método | Inbound administrativo | Key pair | IAM | Componente na instância |
|---|---|---|---|---|
| SSH direto | TCP 22 | sim | não para o login | `sshd` |
| EC2 Instance Connect | TCP 22 | chave pública temporária | sim | EIC + `sshd` |
| Session Manager | nenhum | não | sim | SSM Agent + instance role |
| RDP direto, Windows | TCP 3389 | pode participar da senha inicial | não para a conexão | RDP |

Escolha:

- ambiente pessoal simples e temporário: SSH restrito ou Instance Connect;
- empresa que quer acesso centralizado sem portas inbound: Session Manager;
- instância privada com requisito de SSH: EIC Endpoint ou conectividade privada;
- nenhuma necessidade de shell: não habilite acesso administrativo.

## 8. Instance roles dentro do EC2

### 8.1 Duas identidades no mesmo exercício

Não confunda:

```text
Identidade humana
  └── pode lançar, conectar ou terminar a instância

Instance role
  └── autoriza o software executado dentro da instância
```

O operador pode ter permissão para `ec2:RunInstances`, enquanto a aplicação
possui somente `s3:GetObject` ou as operações do Systems Manager. Uma não herda
automaticamente as permissões da outra.

### 8.2 Como a role chega à instância

1. Uma trust policy permite que `ec2.amazonaws.com` assuma a role.
2. Permissions policies definem o que a sessão da role pode fazer.
3. Um instance profile contém a role.
4. O instance profile é associado ao EC2.
5. Credenciais temporárias ficam disponíveis pelo Instance Metadata Service.
6. SDKs e AWS CLI atualizados descobrem e renovam essas credenciais
   automaticamente.

Não execute `aws configure` dentro do EC2 para gravar access keys. Não coloque
chaves em user data, variáveis permanentes, AMIs ou arquivos da aplicação.

Uma instância pode ter somente uma role associada por vez, embora a mesma role
possa ser usada por várias instâncias. Se a aplicação precisa de mais ações,
refine as policies da role em vez de criar credenciais paralelas.

A identidade que lança a instância com esse instance profile também precisa de
`iam:PassRole` sobre a role aprovada. Essa permissão deixa o operador entregar a
role ao serviço EC2; ela não faz o operador assumir automaticamente a role.

### 8.3 IMDSv2

O Instance Metadata Service fornece dados locais da instância. IMDSv2 exige um
token de sessão e adiciona proteção contra certas classes de ataques que
exploram requisições indevidas a metadados.

No laboratório, configure:

```text
Metadata accessible: Enabled
Metadata version: V2 only / token required
```

É seguro verificar o nome da role ou o instance ID durante um laboratório. Não
copie nem publique o documento que contém as credenciais da role.

Exemplo que consulta apenas o nome da role:

```bash
TOKEN=$(curl -sS -X PUT \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 300" \
  http://169.254.169.254/latest/api/token)

curl -sS \
  -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/iam/security-credentials/

unset TOKEN
```

Não acrescente o nome da role ao final da URL durante o material de estudo, pois
essa consulta retornaria access key temporária, secret key e session token.

### Cenário resolvido 1 — Administração sem SSH aberto

1. **Cenário:** centenas de instâncias privadas precisam de shell administrativo.
2. **Requisitos:** sem bastion, sem key pair compartilhado, sem inbound 22.
3. **Palavras decisivas:** *no inbound ports*, *IAM-controlled access*,
   *interactive shell*.
4. **Decisão:** Systems Manager Session Manager.
5. **Dependências:** SSM Agent, instance role, endpoints e permissão do operador.
6. **Por que não Instance Connect direto:** continua sendo SSH e precisa de
   caminho à porta 22.
7. **Variação:** se a organização exige protocolo SSH e possui EIC Endpoint, o
   EC2 Instance Connect pode ser a escolha.

## 9. Modelos de compra: separe preço de capacidade

O mesmo instance type pode ser executado sob modelos diferentes. A aplicação
não fica mais rápida só porque a cobrança mudou.

| Necessidade | Opção inicial |
|---|---|
| uso curto, novo ou imprevisível | On-Demand |
| uso estável com compromisso em USD/h | Savings Plans |
| configuração EC2 estável e desconto correspondente | Reserved Instance |
| workload tolerante a interrupção | Spot |
| host físico e licenciamento por socket/core | Dedicated Host |
| hardware de um único cliente sem controle do host | Dedicated Instance |
| capacidade garantida em uma AZ, sem foco em desconto | Capacity Reservation |

## 10. On-Demand Instances

Características:

- sem compromisso de um ou três anos;
- pagamento pelo tempo executado segundo a oferta;
- capacidade sujeita às quotas e à disponibilidade;
- não pode ser interrompida pela AWS pelo simples mecanismo de recuperação de
  capacidade Spot;
- maior flexibilidade e, normalmente, maior preço unitário que opções com
  compromisso.

Casos:

- aplicação nova sem histórico;
- teste de poucos dias;
- tráfego irregular que não aceita interrupção;
- parte de uma frota mantida como base confiável.

On-Demand não significa “capacidade garantida em qualquer AZ”. Para garantia
específica, avalie Capacity Reservation.

## 11. Savings Plans

Savings Plans trocam um compromisso de uso, medido em **USD por hora**, por
preços reduzidos durante um ou três anos.

### 11.1 Compute Savings Plans

Oferecem a maior flexibilidade:

- famílias e tamanhos de EC2;
- Regions;
- sistema operacional;
- tenancy;
- AWS Fargate;
- AWS Lambda.

São adequados quando o gasto de compute é previsível, mas a tecnologia ou a
localização pode mudar.

### 11.2 EC2 Instance Savings Plans

Aplicam-se a:

- uma família de instâncias;
- uma Region escolhida;
- diferentes tamanhos, sistemas operacionais e tenancy compatíveis com o plano.

Têm menos flexibilidade e podem oferecer desconto maior que Compute Savings
Plans.

### 11.3 O compromisso continua sendo cobrado

O benefício se aplica automaticamente ao uso elegível, mas o compromisso não
desaparece se o recurso for terminado. Não compre um Savings Plan em um
laboratório.

As formas de pagamento podem ser:

- no upfront;
- partial upfront;
- all upfront.

O pagamento antecipado pode aumentar o desconto, mas não reduz o prazo do
compromisso.

## 12. Reserved Instances

Uma **Reserved Instance (RI)** não é um servidor pré-criado. É principalmente um
benefício de cobrança aplicado automaticamente a instâncias On-Demand que
correspondam aos atributos da reserva.

Características:

- prazo de um ou três anos;
- atributos como instance type, Region, plataforma e tenancy;
- cobrança do compromisso mesmo sem uso correspondente;
- Standard ou Convertible;
- escopo regional ou zonal.

### 12.1 Standard versus Convertible

| Tipo | Desconto relativo | Flexibilidade |
|---|---|---|
| Standard RI | normalmente maior | pode ser modificada em condições específicas; não pode ser trocada |
| Convertible RI | normalmente menor | pode ser trocada por outra Convertible RI com atributos diferentes |

### 12.2 Regional versus zonal

| Escopo | Desconto | Reserva capacidade | Flexibilidade |
|---|---|---|---|
| Regional RI | na Region | não | qualquer AZ da Region; size flexibility em casos compatíveis |
| Zonal RI | na AZ escolhida | sim | precisa corresponder à AZ e aos atributos |

Pegadinha central:

> uma Regional RI oferece desconto, mas não reserva capacidade; uma Zonal RI
> correspondente também reserva capacidade naquela AZ.

A documentação atual recomenda Savings Plans como caminho mais fácil e flexível
para desconto. RIs ainda aparecem em ambientes existentes e em requisitos
específicos.

### Cenário resolvido 2 — Desconto flexível por três anos

1. **Cenário:** gasto estável, mas a aplicação pode mudar de EC2 para Fargate ou
   Lambda e entre Regions.
2. **Requisito:** desconto com compromisso de três anos.
3. **Palavras decisivas:** *consistent USD/hour*, *across Regions*, *Fargate and
   Lambda*.
4. **Decisão:** Compute Savings Plan.
5. **Por que não EC2 Instance Savings Plan:** restringe família e Region.
6. **Por que não RI:** não acompanha a migração para Fargate ou Lambda.
7. **Variação:** família EC2 e Region totalmente estáveis podem favorecer EC2
   Instance Savings Plan.

## 13. Spot Instances

Spot usa capacidade ociosa do EC2 com grande desconto em relação a On-Demand.
Em troca, a AWS pode recuperar a capacidade.

### 13.1 Workloads adequados

- batch;
- renderização;
- processamento distribuído;
- CI/CD;
- workers stateless;
- workloads com checkpoint;
- capacidade adicional em uma frota diversificada.

### 13.2 Workloads inadequados

- banco stateful único;
- processo que perde todo o trabalho quando interrompido;
- aplicação rigidamente ligada a uma única instância;
- workload que precisa começar imediatamente em um único capacity pool;
- sistema que não tolera períodos de capacidade reduzida.

Quando o EC2 interrompe Spot, pode terminar, parar ou hibernar conforme a
configuração compatível. O aviso de interrupção é entregue em regime best effort
e normalmente oferece **dois minutos**. Um rebalance recommendation pode
aparecer antes, mas não é garantido.

Use o intervalo para:

- parar de aceitar novo trabalho;
- gravar checkpoint em armazenamento durável;
- remover o nó do balanceamento;
- encerrar com segurança.

### 13.3 Diversificação

Um Spot capacity pool combina instance type e Availability Zone. Depender de um
único pool aumenta o risco de indisponibilidade simultânea.

Boas práticas:

- permitir vários instance types;
- usar várias AZs;
- manter estado fora da instância;
- usar EC2 Auto Scaling ou EC2 Fleet;
- preferir a estratégia `price-capacity-optimized`;
- processar interruption notices e rebalance recommendations;
- testar a aplicação para interrupção.

`lowest-price` considera preço sem priorizar a disponibilidade de capacidade e
pode aumentar interrupções. O menor preço instantâneo não é automaticamente o
menor custo do sistema quando reiniciar trabalho é caro.

O modelo atual não deve ser estudado como uma guerra de lances. Definir um preço
máximo maior não cria capacidade e não impede que a AWS interrompa a instância.
Além disso, terminar manualmente uma instância controlada por uma solicitação
persistente, frota ou Auto Scaling pode provocar sua substituição; no cleanup,
remova primeiro o controlador responsável pela capacidade.

### 13.4 Atualização sobre Spot Fleet

O curso demonstra Spot Fleet, mas a documentação atual o classifica como API
legada sem investimento planejado:

- **Amazon EC2 Auto Scaling:** recomendado quando a AWS deve manter e substituir
  a capacidade da frota;
- **EC2 Fleet:** indicado quando o cliente quer solicitar combinações de
  On-Demand e Spot e gerenciar o ciclo de vida;
- **Spot Fleet:** reconhecer em arquiteturas legadas, não escolher como padrão
  para projeto novo.

### Cenário resolvido 3 — Batch com menor custo

1. **Cenário:** dez mil tarefas independentes, cada uma grava checkpoint no S3.
2. **Requisitos:** menor custo; prazo flexível; falhas podem ser repetidas.
3. **Palavras decisivas:** *fault-tolerant*, *flexible*, *checkpoint*.
4. **Decisão:** Spot em Auto Scaling ou EC2 Fleet, com vários tipos e AZs.
5. **Estratégia:** `price-capacity-optimized`.
6. **Por que não somente On-Demand:** funciona, mas não atende à otimização
   principal.
7. **Variação:** se nenhuma interrupção for aceita, use On-Demand ou um
   compromisso adequado ao padrão.

## 14. Dedicated Hosts e Dedicated Instances

Ambas as opções usam hardware que não é compartilhado com instâncias de outras
contas, mas o controle é diferente.

| Característica | Dedicated Host | Dedicated Instance |
|---|---|---|
| cobrança principal | por host | por instância, além das regras vigentes |
| host ID, sockets e cores visíveis | sim | não |
| targeted placement | sim | não |
| host affinity | sim | não |
| BYOL ligado a socket/core | opção apropriada | suporte limitado |
| caso central | licenciamento e controle do host | isolamento físico sem controle do host |

Dedicated não é sinônimo de maior desempenho. A decisão costuma nascer de
compliance, isolamento ou licenciamento.

Dedicated Instances podem incluir uma taxa regional além da cobrança das
instâncias. Dedicated Hosts são cobrados enquanto o host permanece alocado,
mesmo que sua capacidade esteja vazia. Confirme sempre a tabela vigente.

Não crie Dedicated Host em laboratório: não participa do Free Tier e pode gerar
custo alto mesmo sem uma carga útil relevante.

### Capacity Reservation

Uma On-Demand Capacity Reservation:

- reserva capacidade para atributos específicos em uma AZ;
- pode ser criada sem compromisso de longo prazo na modalidade imediata;
- cobra a capacidade reservada, usada ou não;
- não oferece desconto por si só;
- pode receber desconto correspondente de Savings Plans ou Regional RI.

Separe as perguntas:

```text
Quero preço menor?       -> Savings Plans / RI / Spot, conforme o workload
Quero garantir capacidade? -> Zonal RI ou Capacity Reservation
```

### Cenário resolvido 4 — Licença por socket

1. **Cenário:** licença existente depende do número de sockets e cores físicos.
2. **Requisitos:** identificar o host e controlar o posicionamento.
3. **Palavras decisivas:** *socket-based license*, *host ID*, *host affinity*.
4. **Decisão:** Dedicated Host.
5. **Por que não Dedicated Instance:** não expõe sockets, cores ou placement.
6. **Por que não Savings Plan:** altera preço, não a visibilidade do host.
7. **Variação:** se o requisito for somente hardware de um único cliente,
   Dedicated Instance pode bastar.

## 15. Tabela de decisão consolidada

| Requisito | Melhor ponto de partida | Trade-off |
|---|---|---|
| acesso Linux tradicional, rede pública controlada | SSH com origem `/32` | gestão de keys e porta 22 |
| SSH temporário governado por IAM | EC2 Instance Connect | ainda precisa de SSH e rede |
| administração sem inbound e sem keys | Session Manager | exige agente, role e endpoints |
| aplicação EC2 chama API AWS | instance role | policy deve aplicar least privilege |
| demanda nova por poucos dias | On-Demand | preço unitário maior |
| compromisso flexível entre serviços/Regions | Compute Savings Plan | compromisso financeiro |
| família EC2 estável em uma Region | EC2 Instance Savings Plan | menos flexível |
| configuração EC2 fixa e legado de RI | Reserved Instance | correspondência de atributos |
| batch tolerante a interrupção | Spot diversificado | capacidade e duração não garantidas |
| desconto e capacidade em uma AZ | Zonal RI | compromisso e baixa flexibilidade |
| capacidade em AZ sem compromisso de desconto | Capacity Reservation | paga mesmo ociosa |
| licença por socket/core | Dedicated Host | custo e gestão do host |
| isolamento single-tenant sem controle de host | Dedicated Instance | menos visibilidade e BYOL limitado |

## 16. Armadilhas de prova

1. Security group aberto não corrige usuário ou chave errados.
2. IAM permission não abre uma porta de rede.
3. Key pair do EC2 não é access key do IAM.
4. `ec2-user` é usuário do sistema operacional, não IAM user.
5. SSH direto não exige IAM para o handshake.
6. EC2 Instance Connect usa IAM, mas continua usando SSH.
7. A chave pública do Instance Connect fica disponível por 60 segundos; uma
   sessão estabelecida não dura somente 60 segundos.
8. Session Manager não exige inbound 22/3389.
9. Session Manager ainda exige agente, instance role e conectividade aos
   endpoints.
10. A role da instância não é a identidade do administrador.
11. Instance profile entrega a role ao EC2.
12. Não se devem copiar credenciais recuperadas do IMDS.
13. IMDSv2 usa token de sessão.
14. On-Demand não significa capacidade garantida.
15. Savings Plan é compromisso em USD/h, não compra de uma instância.
16. Terminar uma instância não cancela um Savings Plan ou RI.
17. Reserved Instance é benefício de cobrança, não servidor pré-lançado.
18. Regional RI não reserva capacidade.
19. Zonal RI correspondente reserva capacidade na AZ.
20. Spot pode ser interrompida; não use para workload intolerante.
21. Diversificar Spot reduz dependência de um capacity pool, mas não elimina
    interrupções.
22. Spot Fleet é legado para novos projetos.
23. Dedicated Instance não oferece visibilidade de sockets/cores.
24. Dedicated Host é a resposta típica para BYOL ligado ao servidor.
25. Dedicated não implica automaticamente maior desempenho.

## 17. Custos e cleanup do LAB B03

O primeiro laboratório com EC2 pode consumir créditos ou gerar alguns centavos:

- compute enquanto a instância estiver `running`;
- root volume EBS até ser excluído;
- endereço IPv4 público enquanto estiver associado;
- pequena transferência de dados, se ultrapassar ofertas aplicáveis.

Controles obrigatórios:

1. lançar exatamente uma instância;
2. usar AMI oficial Amazon Linux 2023;
3. selecionar o menor tipo marcado **Free tier eligible** no console;
4. manter um root volume `gp3` pequeno e com delete on termination;
5. usar On-Demand, sem comprar RI ou Savings Plan;
6. não criar Spot, Dedicated Host, NAT gateway, load balancer ou Elastic IP;
7. não colocar dados sensíveis no site HTTP;
8. terminar em até 60 minutos;
9. conferir Volumes, Elastic IPs, Snapshots, AMIs e EC2 Global View;
10. excluir a role e o security group específicos do laboratório.

Se a conta não tiver default VPC, não crie uma arquitetura de rede improvisada
nem um NAT gateway. Faça o exercício em diagrama e retome quando uma rede segura
e seu custo tiverem sido definidos.

## 18. Checklist de domínio

- [ ] Explico key pair versus IAM access key.
- [ ] Diagnostico SSH sem abrir `0.0.0.0/0`.
- [ ] Explico os 60 segundos do EC2 Instance Connect.
- [ ] Sei por que Instance Connect ainda depende da porta 22.
- [ ] Escolho Session Manager quando não pode haver inbound administrativo.
- [ ] Explico a cadeia role → instance profile → IMDS → credencial temporária.
- [ ] Escolho On-Demand para demanda curta e incerta.
- [ ] Comparo Compute e EC2 Instance Savings Plans.
- [ ] Explico Regional RI versus Zonal RI.
- [ ] Identifico workloads adequados para Spot.
- [ ] Escolho Dedicated Host para BYOL por socket/core.
- [ ] Sei que Capacity Reservation e desconto são dimensões diferentes.
- [ ] Consigo provar que o cleanup do laboratório foi concluído.

## 19. Recuperação ativa

Responda sem consultar:

1. Quais sete verificações formam o diagnóstico básico de SSH?
2. Qual a diferença entre uma key pair do EC2 e uma access key do IAM?
3. O que o EC2 Instance Connect envia à instância?
4. Os 60 segundos encerram uma sessão SSH já conectada?
5. Qual método oferece shell sem porta inbound?
6. Quais quatro pré-requisitos típicos do Session Manager?
7. Quem usa a instance role: o administrador ou o software no EC2?
8. Por que não se executa `aws configure` com access key dentro da instância?
9. Qual é a função do IMDSv2?
10. Qual modelo atende um teste imprevisível de dez dias sem interrupção?
11. Quando escolher Compute Savings Plan?
12. Uma Regional RI garante capacidade?
13. Qual oferta combina desconto e capacidade em uma AZ?
14. Quais características tornam um workload adequado para Spot?
15. Qual estratégia atual substitui Spot Fleet em um projeto novo?
16. Dedicated Host e Dedicated Instance oferecem o mesmo controle?
17. Capacity Reservation reduz o preço por si só?

## 20. Ligações deste bloco

- [Laboratório B03](../../05_Laboratorios/LAB_B03_EC2_Web_Role_e_Cleanup.md)
- [Questões B03](../../04_Questoes_e_Revisoes/Blocos/B03_Questoes.md)
- [Gabarito B03](../../04_Questoes_e_Revisoes/Blocos/B03_Gabarito.md)
- [Revisões B03](../../06_Progresso/B03_Checklist_e_Revisoes.md)

## 21. Referências oficiais

- [Connect to an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html)
- [Connect to Linux using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html)
- [EC2 Instance Connect methods](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html)
- [EC2 Instance Connect prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-prerequisites.html)
- [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
- [Connect using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-with-systems-manager-session-manager.html)
- [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
- [Retrieve temporary role credentials](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-security-credentials.html)
- [Use IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)
- [Configure IMDS options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html)
- [EC2 billing and purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)
- [Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html)
- [Reserved Instances overview](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)
- [Regional and zonal Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-scope.html)
- [Spot best practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html)
- [Spot interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
- [Choose a fleet method](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/which-fleet-method-to-use.html)
- [Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html)
- [Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html)
- [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html)
- [EC2 Free Tier usage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-free-tier-usage.html)
- [Public IPv4 pricing](https://aws.amazon.com/vpc/pricing/)
- [Terminate EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html)

**Referências verificadas em:** 24/07/2026.
