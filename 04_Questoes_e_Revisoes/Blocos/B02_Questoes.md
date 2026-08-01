# B02 — Questões: IAM aplicado, CLI, EC2 e security groups

**Quantidade:** 10 questões autorais  
**Idioma:** 6 em português e 4 em inglês  
**Formato:** questões single-answer e multi-answer; siga a instrução de cada questão<br>
**Tempo sugerido:** 15 minutos; registre sua confiança antes de corrigir  
**Gabarito:** [arquivo separado](B02_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B02-01 | 1.1 | CLI e credenciais temporárias | single | fundamental | básica | Português |
| B02-02 | 1.2 | Role para EC2 | single | fundamental | básica | Português |
| B02-03 | 1.1 | Auditoria IAM | multi-2 | fundamental | intermediária | Português |
| B02-04 | 1.1 | IAM best practices | single | situacional | intermediária | Português |
| B02-05 | 4.2 | AWS Budgets | single | situacional | intermediária | Português |
| B02-06 | 3.2 | EC2 user data | single | situacional | intermediária | Português |
| B02-07 | 3.2 | Instance families | single | situacional | intermediária | Inglês |
| B02-08 | 1.2 | Security group e portas | multi-2 | integrada | avançada | Inglês |
| B02-09 | 1.2 | Stateful security group | single | situacional | intermediária | Inglês |
| B02-10 | 3.2 | Componentes de EC2 | single | situacional | intermediária | Inglês |

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

Quais ferramentas atendem aos requisitos?

**Choose TWO.**

- A. Gerar o IAM credential report para verificar senha, MFA, access keys e
  idade das credenciais dos IAM users.
- B. Consultar last accessed information/Access Advisor para identificar
  serviços sem uso recente pela IAM role.
- C. Usar security groups para inventariar senhas e MFA dos IAM users.
- D. Usar o Cost and Usage Report para determinar quais permissões IAM foram
  utilizadas.
- E. Usar o AWS Budgets para listar access keys e sua última rotação.

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

A public Application Load Balancer terminates HTTPS and forwards requests on
TCP port 8080 to Linux instances in private subnets. The instances must accept
application traffic only from the load balancer; administrators use Systems
Manager Session Manager, so no inbound SSH rule is required.

Which inbound security group rules meet these requirements?

**Choose TWO.**

- A. On the load balancer security group, allow TCP 443 from `0.0.0.0/0`.
- B. On the instance security group, allow TCP 8080 from `0.0.0.0/0`.
- C. On the instance security group, allow TCP 8080 with the load balancer
  security group as the source.
- D. On the load balancer security group, allow TCP 8080 with the instance
  security group as the source.
- E. On the instance security group, allow all ephemeral TCP ports from
  `0.0.0.0/0` for response traffic.

### B02-09

An EC2 workload in a private subnet initiates HTTPS connections through the
approved egress path to an external API. Its security group permits outbound TCP
443. The subnet network ACL, which is stateless, explicitly permits outbound TCP
443 and the corresponding inbound ephemeral response ports. The team now asks
whether the stateful instance control also needs a broad inbound ephemeral-port
rule.

What additional inbound security group rule is required for the response
traffic?

- A. An inbound rule allowing all ephemeral ports from `0.0.0.0/0`.
- B. No additional inbound rule, because security groups are stateful and allow
  response traffic for an established connection.
- C. An inbound TCP 443 rule from the EC2 instance's own private IP address.
- D. An explicit security group deny rule followed by an allow rule for the
  external service.

### B02-10

A company is standardizing a repeatable EC2 web tier. Every replacement instance
must boot with the approved operating system, receive enough CPU and memory for
the workload, accept HTTPS only from the Application Load Balancer, and install
the current application package automatically at first boot. The design must
keep image, capacity, network authorization, and bootstrap responsibilities
separate so each can change independently.

Which launch design meets all requirements?

- A. Put the firewall rules in the AMI, and use the instance type to select the
  operating system.
- B. Use a security group to install the package, and use user data to select CPU
  and memory.
- C. Use an approved AMI for the system image, an appropriate instance type for
  capacity, a security group that permits HTTPS from the load balancer security
  group, and user data for boot-time package installation.
- D. Use a key pair to select the deployment Region, and use AWS Budgets to
  attach the persistent application volume.

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
