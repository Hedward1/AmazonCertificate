# B22 — Questões: Segredos, proteção de aplicações e fundamentos de VPC

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione a quantidade indicada em cada questão<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B22_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B22-01 | 1.2 | Secrets Manager | single | fundamental | básica | Inglês |
| B22-02 | 1.3 | ACM | single | situacional | intermediária | Inglês |
| B22-03 | 1.3 | CloudHSM | single | situacional | intermediária | Inglês |
| B22-04 | 1.2 | WAF and Firewall Manager | multi-2 | integrada | avançada | Inglês |
| B22-05 | 1.2 | Central security policy | single | situacional | intermediária | Inglês |
| B22-06 | 1.2 | GuardDuty | single | integrada | avançada | Inglês |
| B22-07 | 1.2 | Detective and Inspector | multi-2 | integrada | avançada | Inglês |
| B22-08 | 3.4 | Subnet design | single | situacional | intermediária | Inglês |
| B22-09 | 1.2 | Layered application and network defense | multi-3 | integrada | avançada | Inglês |
| B22-10 | 1.2 | Security group and NACL | single | integrada | avançada | Inglês |

## Questões

### B22-01

**Context:** An application uses an Amazon RDS database password.

**Requirement:** The credential must be stored securely and rotated automatically on a schedule.

**Question:** Which service is the best fit?

- A. AWS Secrets Manager.
- B. AWS Systems Manager Parameter Store String.
- C. Amazon S3 object tags.
- D. AWS CloudFormation Outputs.

### B22-02

**Context:** A public Application Load Balancer must terminate TLS by using a managed public certificate.

**Requirement:** The certificate should be provisioned and renewed with minimal operations.

**Question:** Which service should be used?

- A. AWS KMS.
- B. AWS Certificate Manager.
- C. AWS CloudHSM.
- D. Amazon Inspector.

### B22-03

**Context:** A regulated workload requires single-tenant hardware security modules and direct control over keys and cryptographic operations.

**Requirement:** A standard multi-tenant managed key service does not satisfy the requirement.

**Question:** Which service should be selected?

- A. AWS Shield Standard.
- B. Amazon Macie.
- C. AWS CloudHSM.
- D. Amazon EventBridge.

### B22-04

**Context:** Web applications behind ALBs in many organization accounts receive SQL injection attempts. Security requires HTTP inspection and centrally enforced, consistently updated policy.

**Requirement:** Choose the application-layer control and the multi-account policy manager. **Choose TWO.**

- A. Use security group deny rules to inspect SQL syntax.
- B. Associate AWS WAF web ACLs with the protected ALBs.
- C. Use AWS Shield Standard as the SQL parser.
- D. Use AWS Firewall Manager to deploy and govern WAF policies across organization accounts.
- E. Use a route table to block malicious HTTP request bodies.

### B22-05

**Context:** A security team must deploy consistent WAF policies across resources in many AWS accounts in an organization.

**Requirement:** Administration and compliance must be centralized.

**Question:** Which service best addresses the requirement?

- A. AWS Firewall Manager.
- B. Amazon Inspector.
- C. AWS Certificate Manager.
- D. VPC Flow Logs.

### B22-06

**Context:** A security team manages many AWS accounts. It needs managed threat
detection from supported account, DNS, and VPC network signals, centralized
enablement for new organization accounts, and a common findings view alongside
other security products. It does not want to build a detection pipeline.

**Requirement:** Separate the detector from the cross-service findings
aggregation layer.

**Question:** Which design best meets the requirement after pricing review?

- A. Enable Amazon Macie organization-wide and send its sensitive-data findings to a central dashboard, treating it as the detector for all credential and network threats.
- B. Enable GuardDuty with organization-wide delegated administration for threat detection and integrate findings into Security Hub CSPM for centralized correlation.
- C. Enable Security Hub CSPM organization-wide without any integrated threat-detection service and assume aggregation creates the missing network findings.
- D. Enable Amazon Detective as the only service, expecting its investigation graphs to generate every initial threat finding from raw organization signals.

### B22-07

**Context:** GuardDuty reports possible credential misuse linked to several resources. The team must investigate related entities and historical activity, while separately scanning supported compute workloads for software vulnerabilities.

**Requirement:** Use specialized managed services for investigation and vulnerability management. **Choose TWO.**

- A. Use Amazon Detective to analyze relationships and activity associated with the finding.
- B. Use Amazon Macie to patch vulnerable packages on EC2 instances.
- C. Use AWS Artifact to build the investigation graph.
- D. Use AWS WAF to inventory package CVEs.
- E. Use Amazon Inspector to continuously assess supported workloads for software vulnerabilities.

### B22-08

**Context:** A private application subnet is `10.22.2.0/28`. A planned scale-out
requires 12 additional ENIs for instances and interface endpoints, before
allowing headroom for replacements. The architect must account for AWS-reserved
IPv4 addresses and avoid a deployment that fails from address exhaustion.

**Requirement:** Determine whether the current CIDR can support even the stated
12-ENI requirement.

**Question:** Which conclusion is correct?

- A. The subnet has 16 usable addresses, so it has four addresses of headroom.
- B. The subnet has 14 usable addresses because only network and broadcast addresses are unavailable.
- C. The subnet has 13 usable addresses, so exactly one replacement can launch.
- D. The subnet has only 11 usable addresses; it cannot support 12 ENIs and must be redesigned with a larger nonoverlapping CIDR or redistributed capacity.

### B22-09

**Context:** A public web application must block SQL injection, improve response to sophisticated DDoS attacks, and ensure application instances accept traffic only from the ALB tier.

**Requirement:** Implement layered application and network protection. **Select THREE.**

- A. Associate an AWS WAF web ACL with the ALB.
- B. Give every application instance an unrestricted public security group.
- C. Evaluate AWS Shield Advanced for enhanced DDoS detection, response, and cost protection.
- D. Replace the ALB with a NAT Gateway for inbound HTTP inspection.
- E. Use a network ACL as the only stateful application-tier control.
- F. Allow the application security group to receive the application port only from the ALB security group.

### B22-10

**Context:** Application ENIs should accept HTTPS only from an ALB security
group. At the subnet boundary, the team also needs an ordered emergency deny
for a hostile CIDR and understands that return traffic may require explicit
ephemeral-port rules.

**Requirement:** Apply least privilege at the interface and a stateless subnet
guardrail without confusing evaluation behavior.

**Question:** Which mapping is correct?

- A. Allow the ALB's changing public CIDRs directly in the application security group and add only an inbound NACL deny, with no return-path rules.
- B. Use a stateful security group on application ENIs with an ALB-SG source rule, and an ordered stateless NACL with explicit allow/deny plus required return-path rules.
- C. Use AWS Network Firewall for the hostile CIDR but allow application HTTPS from the entire VPC CIDR, omitting the required ALB-to-application least privilege.
- D. Reference the ALB security group correctly on the application ENIs, but configure the stateless NACL only for inbound HTTPS and omit ephemeral return traffic.

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
