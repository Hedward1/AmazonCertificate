# B25 — Questões: CloudFormation, operações, custos e Well-Architected

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione uma resposta<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B25_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B25-01 | 2.2 | CloudFormation change set | Situacional | Intermediate | Inglês |
| B25-02 | 2.2 | CloudFormation drift | Situacional | Intermediate | Inglês |
| B25-03 | 1.1 | CloudFormation service role | Situacional | Advanced | Inglês |
| B25-04 | 1.2 | Session Manager | Situacional | Intermediate | Inglês |
| B25-05 | 2.2 | Complementary services | Situacional | Basic | Inglês |
| B25-06 | 3.5 | Amazon AppFlow | Situacional | Basic | Inglês |
| B25-07 | 4.2 | Cost Anomaly Detection | Situacional | Intermediate | Inglês |
| B25-08 | 2.2 | Well-Architected pillars | Situacional | Basic | Inglês |
| B25-09 | 2.2 | Trusted Advisor | Situacional | Intermediate | Inglês |
| B25-10 | 2.2 | DeletionPolicy Retain and exam readiness | Situacional | Intermediate | Inglês |

## Questões

### B25-01

**Context:** A CloudFormation template update might replace a stateful database resource.

**Requirement:** The operations team must review proposed changes before execution.

**Question:** What should the team create?

- A. A change set.
- B. A VPC Flow Log.
- C. An SCP that grants database access.
- D. A Cost Anomaly monitor.

**Before moving on:** record decisive words and confidence.

### B25-02

**Context:** An administrator manually changed a supported property of a resource that belongs to a CloudFormation stack.

**Requirement:** The team needs to compare the actual configuration with the expected template configuration.

**Question:** Which feature should be used?

- A. CloudTrail Event history only.
- B. CloudFormation drift detection.
- C. AWS Shield Advanced.
- D. Amazon SES.

**Before moving on:** record decisive words and confidence.

### B25-03

**Context:** A stack uses a CloudFormation service role to create resources.

**Requirement:** Administrators must prevent users from passing an overly privileged role to CloudFormation.

**Question:** Which permission requires particular control?

- A. iam:PassRole.
- B. s3:GetObject only.
- C. cloudwatch:GetMetricData only.
- D. route53:ListHostedZones only.

**Before moving on:** record decisive words and confidence.

### B25-04

**Context:** Private EC2 instances must be administered without inbound SSH, public IP addresses, or a bastion host.

**Requirement:** Sessions must use managed identity and can be logged.

**Question:** Which service is the best fit?

- A. AWS WAF.
- B. Systems Manager Session Manager.
- C. Amazon CloudFront.
- D. AWS Snow Family.

**Before moving on:** record decisive words and confidence.

### B25-05

**Context:** A company needs to run queued containerized compute jobs that can scale according to batch demand.

**Requirement:** It does not need continuous stream processing.

**Question:** Which service should it use?

- A. Amazon Pinpoint.
- B. Amazon AppFlow.
- C. AWS Batch.
- D. Amazon Lex.

**Before moving on:** record decisive words and confidence.

### B25-06

**Context:** A business team must transfer data between a supported SaaS application and Amazon S3 with minimal custom integration code.

**Requirement:** The solution should use a managed data integration service.

**Question:** Which service is appropriate?

- A. AWS Outposts.
- B. Amazon AppFlow.
- C. Amazon Inspector.
- D. AWS Direct Connect only.

**Before moving on:** record decisive words and confidence.

### B25-07

**Context:** A company wants notifications when daily AWS spending deviates unexpectedly from learned patterns.

**Requirement:** The feature should detect anomalies, not enforce a hard spending cap.

**Question:** Which service capability should be configured?

- A. AWS Cost Anomaly Detection.
- B. A security group.
- C. CloudFormation drift detection.
- D. AWS Certificate Manager.

**Before moving on:** record decisive words and confidence.

### B25-08

**Context:** An architecture review evaluates operations, security, reliability, performance, cost, and environmental impact.

**Requirement:** The team wants the complete current set of Well-Architected pillars.

**Question:** Which list is correct?

- A. Security, networking, storage, database, compute, migration.
- B. Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.
- C. Audit, encryption, backup, scaling, caching, and billing.
- D. Identity, DNS, routing, logging, patching, and support.

**Before moving on:** record decisive words and confidence.

### B25-09

**Context:** An account owner wants automated checks and recommendations for areas such as cost, performance, security, fault tolerance, and service limits.

**Requirement:** The architect must remember that coverage varies by support plan.

**Question:** Which service provides these checks?

- A. AWS Trusted Advisor.
- B. Amazon Kendra.
- C. AWS DMS.
- D. Amazon Textract.

**Before moving on:** record decisive words and confidence.

### B25-10

**Context:** A course stack is deleted, but a database with DeletionPolicy Retain remains. The learner is tempted to open the reserved practice exam during B25.

**Requirement:** Cleanup must be verified, and the practice exam must remain unseen until SIM B.

**Question:** What should the learner do?

- A. Assume stack deletion removed every resource and open the exam.
- B. Delete every database in the account and open the exam.
- C. Verify the retained resource and its ownership, clean it up only if authorized, and keep the practice exam unopened.
- D. Ignore the retained database because retained resources are free.

**Before moving on:** record decisive words and confidence.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B25-01 |  |  |  |
| B25-02 |  |  |  |
| B25-03 |  |  |  |
| B25-04 |  |  |  |
| B25-05 |  |  |  |
| B25-06 |  |  |  |
| B25-07 |  |  |  |
| B25-08 |  |  |  |
| B25-09 |  |  |  |
| B25-10 |  |  |  |
