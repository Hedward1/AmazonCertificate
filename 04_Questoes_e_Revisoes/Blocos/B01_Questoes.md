# B01 — Questões: infraestrutura global, responsabilidade e IAM

**Quantidade:** 10 questões autorais  
**Idioma:** 6 em português e 4 em inglês  
**Formato:** questões single-answer e multi-answer; siga a instrução de cada questão<br>
**Tempo sugerido:** 15 minutos para resolver; depois registre sua confiança antes
de abrir o gabarito  
**Gabarito:** [arquivo separado](B01_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B01-01 | 2.2 | Region e AZ | single | fundamental | básica | Português |
| B01-02 | 2.1/3.4 | Edge locations | single | fundamental | básica | Português |
| B01-03 | 1.1 | Shared responsibility/EC2 | multi-2 | fundamental | intermediária | Português |
| B01-04 | 1.1 | Shared responsibility/S3 | single | situacional | intermediária | Português |
| B01-05 | 1.1 | Root user e MFA | single | situacional | intermediária | Português |
| B01-06 | 1.1 | Groups e least privilege | single | situacional | intermediária | Português |
| B01-07 | 1.1 | Role para EC2 | single | situacional | intermediária | Inglês |
| B01-08 | 1.1 | Cross-account role | multi-2 | integrada | avançada | Inglês |
| B01-09 | 1.1 | Least-privilege policy | single | situacional | intermediária | Inglês |
| B01-10 | 1.1 | Workforce access | single | situacional | intermediária | Inglês |

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

Segundo o modelo de responsabilidade compartilhada, quais atividades são
responsabilidade do cliente?

**Choose TWO.**

- A. Substituir discos físicos com defeito no data center.
- B. Aplicar patches de segurança ao sistema operacional convidado das
  instâncias.
- C. Manter a camada de virtualização utilizada pelo Amazon EC2.
- D. Controlar o acesso físico às instalações da AWS.
- E. Configurar security groups, permissões IAM e a proteção dos dados da
  aplicação.

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

Which configurations should a solutions architect implement?

**Choose TWO.**

- A. Create a role in production and attach a permissions policy that limits
  access to the required deployment bucket actions and resources.
- B. Configure the production role trust policy for the authorized development
  principal, and allow that principal to call `sts:AssumeRole`.
- C. Create IAM users with long-term access keys in the production account for
  every developer.
- D. Store the production account root user credentials in AWS Secrets Manager
  in the development account.
- E. Make the deployment bucket public and distribute its URL to the
  developers.

### B01-09

A reporting workload assumes an IAM role and receives exact object keys from an
approved manifest. It must download only objects under the `quarterly/` prefix
of `reports-bucket`; it never discovers keys by listing and must not upload,
modify, or delete data. The bucket separately enforces TLS, and any required KMS
permission is scoped in another policy statement.

Which S3 permission statement should be included in the role to preserve least
privilege?

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
