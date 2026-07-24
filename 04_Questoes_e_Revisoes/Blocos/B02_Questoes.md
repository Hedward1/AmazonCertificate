# B02 — Questões: IAM aplicado, CLI, EC2 e security groups

**Quantidade:** 10 questões autorais  
**Idioma:** 6 em português e 4 em inglês  
**Regra:** selecione uma resposta em cada questão  
**Tempo sugerido:** 15 minutos; registre sua confiança antes de corrigir  
**Gabarito:** [arquivo separado](B02_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B02-01 | 1.1 | CLI e credenciais temporárias | Situacional | Básica | Português |
| B02-02 | 1.2 | Role para EC2 | Situacional | Básica | Português |
| B02-03 | 1.1 | Auditoria IAM | Situacional | Intermediária | Português |
| B02-04 | 1.1 | IAM best practices | Fundamental | Básica | Português |
| B02-05 | 4.2 | AWS Budgets | Situacional | Básica | Português |
| B02-06 | 3.2 | EC2 user data | Situacional | Básica | Português |
| B02-07 | 3.2 | Instance families | Situacional | Básica | Inglês |
| B02-08 | 1.2 | Security group e portas | Situacional | Intermediária | Inglês |
| B02-09 | 1.2 | Stateful security group | Fundamental | Intermediária | Inglês |
| B02-10 | 3.2 | Componentes de EC2 | Fundamental | Básica | Inglês |

## Questões

### B02-01

Um estudante utiliza AWS CLI 2.32 ou posterior em seu computador. Ele possui uma
identidade IAM não root com acesso ao console e a permissão
`SignInLocalDevelopmentAccess`. Ele quer evitar access keys permanentes
armazenadas localmente.

Qual é a abordagem mais adequada?

- A. Executar `aws configure` usando access keys do root user.
- B. Executar `aws login --profile estudos`, concluir a autenticação no navegador
  e usar as credenciais temporárias gerenciadas pela CLI.
- C. Salvar access key e secret access key em variáveis permanentes do sistema.
- D. Criar outro IAM user com `AdministratorAccess` e versionar suas chaves em um
  repositório privado.

### B02-02

Uma aplicação executada em uma instância EC2 precisa apenas ler objetos de um
bucket S3 específico.

Qual solução segue melhor as práticas de segurança da AWS?

- A. Armazenar a senha de um IAM user em um arquivo dentro da instância.
- B. Inserir access keys permanentes no código e criar uma AMI com esse código.
- C. Associar à instância um instance profile que contenha uma IAM role com
  `s3:GetObject` somente nos objetos necessários.
- D. Tornar o bucket público para que a instância não precise de credenciais.

### B02-03

Uma empresa precisa:

1. identificar, para cada IAM user, se há senha, MFA e access keys, além da idade
   dessas credenciais;
2. descobrir quais serviços permitidos por uma IAM role não apresentam uso
   recente, para ajudar a reduzir suas permissões.

Qual combinação atende melhor aos requisitos?

- A. IAM credential report para a primeira verificação e last accessed
  information/Access Advisor para a segunda.
- B. CloudTrail Event history para a primeira e security groups para a segunda.
- C. AWS Budgets para a primeira e AWS Config para a segunda.
- D. IAM Access Analyzer para a primeira e Cost and Usage Report para a segunda.

### B02-04

Qual estratégia está mais alinhada às práticas de segurança atuais do IAM?

- A. Usar root diariamente, desde que ele tenha MFA.
- B. Criar access keys permanentes para cada administrador e não exigir MFA para
  não dificultar a automação.
- C. Compartilhar um único IAM user entre todos os administradores.
- D. Usar federação ou IAM Identity Center com credenciais temporárias para
  pessoas, roles para workloads, MFA e least privilege, reservando root para
  situações excepcionais.

### B02-05

Um estudante possui um pequeno orçamento mensal para laboratórios com EC2 e quer
ser avisado antes de ultrapassá-lo.

Qual solução é a mais apropriada?

- A. Criar um alarme de CPU no CloudWatch e considerar que isso impede qualquer
  cobrança adicional.
- B. Criar um cost budget mensal no AWS Budgets, configurar alertas de custo real
  e previsto e continuar monitorando e encerrando recursos.
- C. Configurar uma Service Quota com o valor do orçamento em dólares.
- D. Ativar Cost Explorer, que encerrará automaticamente todos os recursos
  quando o valor for atingido.

### B02-06

Uma empresa quer que, no primeiro boot de cada nova instância EC2 Linux, um
servidor web seja instalado e iniciado automaticamente.

Qual abordagem atende melhor ao requisito?

- A. Escolher uma instância com mais memória, pois instance types executam
  comandos de instalação durante o boot.
- B. Adicionar somente uma inbound rule TCP 80 ao security group.
- C. Fornecer um shell script em EC2 user data e configurar separadamente o
  security group para permitir o tráfego web necessário.
- D. Armazenar o script na private key do EC2 key pair.

### B02-07

A company runs a CPU-intensive batch processing workload. The workload uses
relatively little memory but requires sustained processor performance.

Which EC2 instance family category is the best starting point?

- A. Compute optimized, such as a C family instance.
- B. Memory optimized, such as an R family instance.
- C. Storage optimized, such as an I family instance.
- D. General purpose burstable, such as a T family instance, regardless of
  CPU-credit behavior.

### B02-08

A public Linux web server must accept HTTPS connections from internet users.
Administrators must connect through SSH only from the corporate public IPv4
address `203.0.113.10`.

Which inbound security group configuration best meets these requirements?

- A. Allow TCP 443 and TCP 22 from `0.0.0.0/0`.
- B. Allow TCP 443 from `203.0.113.10/32` and TCP 22 from `0.0.0.0/0`.
- C. Allow TCP 80 from `0.0.0.0/0` and TCP 3389 from
  `203.0.113.10/32`.
- D. Allow TCP 443 from `0.0.0.0/0` and TCP 22 from
  `203.0.113.10/32`.

### B02-09

An EC2 instance has a security group that permits outbound TCP 443 traffic. It
initiates an HTTPS request to an external service. Assume that the network ACL
permits the traffic.

What inbound security group rule is required for the response?

- A. An inbound rule allowing all ephemeral ports from `0.0.0.0/0`.
- B. No additional inbound rule, because security groups are stateful and allow
  response traffic for an established connection.
- C. An inbound TCP 443 rule from the EC2 instance's own private IP address.
- D. An explicit security group deny rule followed by an allow rule for the
  external service.

### B02-10

Which statement correctly describes the main purpose of common EC2 launch
components?

- A. An AMI defines firewall rules, while the instance type defines the
  operating system.
- B. A security group installs software, while user data selects CPU and memory.
- C. An AMI provides the system image, the instance type determines hardware
  capacity, a security group controls allowed network traffic, and user data can
  automate boot-time configuration.
- D. A key pair selects the AWS Region, while AWS Budgets attaches persistent
  storage.

## Registro antes de corrigir

| ID | Resposta | Confiança (alta/média/baixa) | Palavra decisiva |
|---|---|---|---|
| B02-01 |  |  |  |
| B02-02 |  |  |  |
| B02-03 |  |  |  |
| B02-04 |  |  |  |
| B02-05 |  |  |  |
| B02-06 |  |  |  |
| B02-07 |  |  |  |
| B02-08 |  |  |  |
| B02-09 |  |  |  |
| B02-10 |  |  |  |
