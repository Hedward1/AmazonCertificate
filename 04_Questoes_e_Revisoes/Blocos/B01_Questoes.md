# B01 — Questões: infraestrutura global, responsabilidade e IAM

**Quantidade:** 10 questões autorais  
**Idioma:** 6 em português e 4 em inglês  
**Regra:** selecione uma resposta em cada questão  
**Tempo sugerido:** 15 minutos para resolver; depois registre sua confiança antes
de abrir o gabarito  
**Gabarito:** [arquivo separado](B01_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B01-01 | 2.2 | Region e AZ | Situacional | Básica | Português |
| B01-02 | 2.1/3.4 | Edge locations | Situacional | Básica | Português |
| B01-03 | 1.1 | Shared responsibility/EC2 | Fundamental | Básica | Português |
| B01-04 | 1.1 | Shared responsibility/S3 | Situacional | Intermediária | Português |
| B01-05 | 1.1 | Root user e MFA | Situacional | Intermediária | Português |
| B01-06 | 1.1 | Groups e least privilege | Situacional | Intermediária | Português |
| B01-07 | 1.1 | Role para EC2 | Situacional | Intermediária | Inglês |
| B01-08 | 1.1 | Cross-account role | Integrada | Avançada | Inglês |
| B01-09 | 1.1 | Least-privilege policy | Situacional | Avançada | Inglês |
| B01-10 | 1.1 | Workforce access | Integrada | Avançada | Inglês |

## Questões

### B01-01

Uma aplicação precisa continuar disponível caso uma localização física isolada
apresente falha. A comunicação entre os componentes deve permanecer com baixa
latência, e não existe requisito de recuperação em outra Region.

Qual arquitetura atende melhor aos requisitos?

- A. Executar todas as instâncias em subnets diferentes de uma única
  Availability Zone.
- B. Distribuir as instâncias entre pelo menos duas Availability Zones da mesma
  Region e encaminhar o tráfego apenas aos componentes saudáveis.
- C. Executar todas as instâncias em uma Region e manter backups em uma edge
  location.
- D. Executar uma única instância maior em uma Local Zone.

### B01-02

Uma empresa hospeda imagens e arquivos estáticos em uma origem nos Estados
Unidos. Usuários de vários países reclamam de latência. A empresa quer armazenar
cópias em cache próximas aos usuários, sem implantar uma origem completa em cada
país.

Qual solução é mais adequada?

- A. Criar mais subnets na Availability Zone da origem.
- B. Replicar manualmente a origem para todas as AWS Regions.
- C. Usar o Amazon CloudFront para entregar o conteúdo por edge locations.
- D. Mover a origem para uma única Local Zone.

### B01-03

Uma empresa executa uma aplicação em instâncias Amazon EC2.

Segundo o modelo de responsabilidade compartilhada, qual atividade é
responsabilidade do cliente?

- A. Substituir discos físicos com defeito no data center.
- B. Aplicar patches de segurança ao sistema operacional convidado das
  instâncias.
- C. Manter a camada de virtualização utilizada pelo Amazon EC2.
- D. Controlar o acesso físico às instalações da AWS.

### B01-04

Uma empresa armazena documentos confidenciais no Amazon S3.

Qual responsabilidade permanece com o cliente?

- A. Aplicar patches ao sistema operacional dos servidores que executam o
  Amazon S3.
- B. Substituir equipamentos físicos de armazenamento com defeito.
- C. Proteger fisicamente os data centers que armazenam os objetos.
- D. Classificar os dados e configurar corretamente as permissões e opções de
  criptografia do bucket.

### B01-05

Uma empresa acabou de criar uma conta AWS independente. Qual conjunto de ações
representa a prática operacional mais segura?

- A. Habilitar MFA para o root user, não criar access keys para ele, proteger
  suas credenciais e usar outra identidade administrativa nas atividades
  diárias.
- B. Usar o root user diariamente porque ele já possui todas as permissões
  necessárias.
- C. Compartilhar a senha do root user entre os administradores e controlar o
  uso em uma planilha.
- D. Criar access keys do root user para cada administrador e fazer rotação
  mensal.

### B01-06

Por limitação de um sistema legado, uma empresa ainda precisa usar IAM users.
Todos os analistas devem apenas ler objetos do prefixo
`s3://relatorios/financeiro/`, e a composição da equipe muda frequentemente.

Qual solução exige menor esforço operacional e segue o princípio de least
privilege?

- A. Anexar `AdministratorAccess` individualmente a cada IAM user.
- B. Adicionar os IAM users a uma IAM role usada como grupo e anexar uma policy
  à role.
- C. Criar um IAM user group para os analistas, anexar ao grupo uma customer
  managed policy somente com as ações e os recursos necessários e adicionar ou
  remover usuários do grupo.
- D. Informar o IAM user group como `Principal` na bucket policy, sem conceder
  permissões aos usuários.

### B01-07

An application running on Amazon EC2 must read objects from one S3 bucket. The
company must avoid storing long-term credentials on the instance.

Which solution best meets these requirements?

- A. Create root user access keys and store them in EC2 user data.
- B. Attach an IAM role to the EC2 instance through an instance profile, grant
  only the required S3 permissions, and let the AWS SDK retrieve temporary
  credentials.
- C. Create an IAM user, embed its access keys in the AMI, and rotate the AMI
  every 90 days.
- D. Make the S3 bucket public so the application does not need credentials.

### B01-08

Developers in a development AWS account occasionally need limited access to a
deployment bucket in a production account. The company wants temporary access
and does not want to create duplicate user credentials in production.

Which solution should a solutions architect recommend?

- A. Create IAM users with long-term access keys in the production account for
  every developer.
- B. Attach an S3 policy only to the developers in the development account; no
  production configuration is required.
- C. Store the production account root user credentials in AWS Secrets Manager
  in the development account.
- D. Create a role in production whose trust policy trusts the authorized
  development principal, attach a least-privilege permissions policy to the
  role, and allow the developers to call `sts:AssumeRole`.

### B01-09

A reporting application must download known objects only from the `quarterly/`
prefix of the `reports-bucket` S3 bucket. It does not need to list, upload,
modify, or delete objects.

Which permission statement best follows the principle of least privilege?

- A. `Allow` `s3:GetObject` on
  `arn:aws:s3:::reports-bucket/quarterly/*`.
- B. `Allow` `s3:*` on `*`.
- C. `Allow` `s3:GetObject` on `arn:aws:s3:::reports-bucket`.
- D. `Allow` `s3:ListBucket` on `arn:aws:s3:::reports-bucket`.

### B01-10

A company has multiple AWS accounts and an existing corporate identity
provider. It needs centralized workforce access, MFA, least-privilege
assignments, and temporary credentials for console and CLI access.

Which solution best aligns with AWS security best practices?

- A. Share the root user of each account and protect each password with MFA.
- B. Create one IAM user with long-term access keys for every employee in every
  account.
- C. Connect the identity provider to AWS IAM Identity Center, assign permission
  sets to users or groups, enforce MFA, and use the resulting temporary role
  credentials.
- D. Create a single IAM group in one account and use it directly as the
  principal in every other account.

## Registro antes de corrigir

| ID | Resposta | Confiança (alta/média/baixa) | Palavra decisiva |
|---|---|---|---|
| B01-01 |  |  |  |
| B01-02 |  |  |  |
| B01-03 |  |  |  |
| B01-04 |  |  |  |
| B01-05 |  |  |  |
| B01-06 |  |  |  |
| B01-07 |  |  |  |
| B01-08 |  |  |  |
| B01-09 |  |  |  |
| B01-10 |  |  |  |
