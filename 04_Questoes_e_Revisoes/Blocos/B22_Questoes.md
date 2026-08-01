# B22 — Questões: Segredos, proteção de aplicações e fundamentos de VPC

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione uma resposta<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B22_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B22-01 | 1.2 | Secrets Manager | Situacional | Basic | Inglês |
| B22-02 | 1.3 | ACM | Situacional | Basic | Inglês |
| B22-03 | 1.3 | CloudHSM | Situacional | Intermediate | Inglês |
| B22-04 | 1.2 | AWS WAF | Situacional | Basic | Inglês |
| B22-05 | 1.2 | Firewall Manager | Situacional | Intermediate | Inglês |
| B22-06 | 1.2 | GuardDuty | Situacional | Basic | Inglês |
| B22-07 | 1.2 | Inspector and Macie | Situacional | Intermediate | Inglês |
| B22-08 | 3.4 | Subnet CIDR | Situacional | Intermediate | Inglês |
| B22-09 | 3.4 | Public subnet | Situacional | Intermediate | Inglês |
| B22-10 | 3.4 | Security group and NACL | Situacional | Intermediate | Inglês |

## Questões

### B22-01

**Context:** An application uses an Amazon RDS database password.

**Requirement:** The credential must be stored securely and rotated automatically on a schedule.

**Question:** Which service is the best fit?

- A. AWS Secrets Manager.
- B. AWS Systems Manager Parameter Store String.
- C. Amazon S3 object tags.
- D. AWS CloudFormation Outputs.

**Before moving on:** record decisive words and confidence.

### B22-02

**Context:** A public Application Load Balancer must terminate TLS by using a managed public certificate.

**Requirement:** The certificate should be provisioned and renewed with minimal operations.

**Question:** Which service should be used?

- A. AWS KMS.
- B. AWS Certificate Manager.
- C. AWS CloudHSM.
- D. Amazon Inspector.

**Before moving on:** record decisive words and confidence.

### B22-03

**Context:** A regulated workload requires single-tenant hardware security modules and direct control over keys and cryptographic operations.

**Requirement:** A standard multi-tenant managed key service does not satisfy the requirement.

**Question:** Which service should be selected?

- A. AWS Shield Standard.
- B. Amazon Macie.
- C. AWS CloudHSM.
- D. Amazon EventBridge.

**Before moving on:** record decisive words and confidence.

### B22-04

**Context:** A web application behind an Application Load Balancer is receiving SQL injection attempts.

**Requirement:** The solution must inspect HTTP requests and block matching patterns.

**Question:** Which service should be used?

- A. A security group deny rule.
- B. A network ACL only.
- C. AWS Shield Standard only.
- D. AWS WAF web ACL.

**Before moving on:** record decisive words and confidence.

### B22-05

**Context:** A security team must deploy consistent WAF policies across resources in many AWS accounts in an organization.

**Requirement:** Administration and compliance must be centralized.

**Question:** Which service best addresses the requirement?

- A. AWS Firewall Manager.
- B. Amazon Inspector.
- C. AWS Certificate Manager.
- D. VPC Flow Logs.

**Before moving on:** record decisive words and confidence.

### B22-06

**Context:** A company wants managed threat detection based on account activity, DNS, and VPC network signals.

**Requirement:** It does not want to build its own detection pipeline.

**Question:** Which service should it enable after reviewing pricing?

- A. Amazon Macie.
- B. Amazon GuardDuty.
- C. Amazon Textract.
- D. AWS Batch.

**Before moving on:** record decisive words and confidence.

### B22-07

**Context:** A team must identify software vulnerabilities in supported compute workloads and discover sensitive data in S3.

**Requirement:** Each requirement should use the specialized managed service.

**Question:** Which pairing is correct?

- A. Macie for vulnerabilities and Inspector for PII.
- B. GuardDuty for both tasks.
- C. Inspector for vulnerabilities and Macie for sensitive S3 data.
- D. ACM for vulnerabilities and WAF for PII.

**Before moving on:** record decisive words and confidence.

### B22-08

**Context:** A VPC designer creates an IPv4 subnet with CIDR 10.22.2.0/28.

**Requirement:** The designer must account for addresses reserved by AWS.

**Question:** How many IPv4 addresses are available for use in the subnet?

- A. 16.
- B. 14.
- C. 13.
- D. 11.

**Before moving on:** record decisive words and confidence.

### B22-09

**Context:** An EC2 instance is in a subnet whose route table sends 0.0.0.0/0 to an Internet Gateway.

**Requirement:** The instance must receive inbound IPv4 traffic from the internet.

**Question:** What additional condition is required?

- A. A public IPv4 or Elastic IP plus permissive security controls and a listening service.
- B. Only a private IPv4 address.
- C. A NAT Gateway in the same subnet.
- D. A gateway endpoint for DynamoDB.

**Before moving on:** record decisive words and confidence.

### B22-10

**Context:** A network design needs stateful allow rules at the interface and an ordered subnet guardrail that can explicitly deny a CIDR.

**Requirement:** Both controls must be mapped correctly.

**Question:** Which mapping is correct?

- A. NACL is stateful; security group is stateless.
- B. Security group is stateful; NACL is stateless with allow and deny rules.
- C. Both are stateful and support deny.
- D. Both operate only at the VPC level.

**Before moving on:** record decisive words and confidence.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B22-01 |  |  |  |
| B22-02 |  |  |  |
| B22-03 |  |  |  |
| B22-04 |  |  |  |
| B22-05 |  |  |  |
| B22-06 |  |  |  |
| B22-07 |  |  |  |
| B22-08 |  |  |  |
| B22-09 |  |  |  |
| B22-10 |  |  |  |
