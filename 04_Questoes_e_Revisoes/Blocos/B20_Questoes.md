# B20 — Questões: CloudWatch, EventBridge, CloudTrail, Config e Organizations

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione uma resposta<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B20_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B20-01 | 2.2 | CloudWatch agent | Situacional | Basic | Inglês |
| B20-02 | 2.2 | CloudWatch alarm | Situacional | Intermediate | Inglês |
| B20-03 | 2.1 | EventBridge | Situacional | Basic | Inglês |
| B20-04 | 1.2 | CloudTrail Event history | Situacional | Basic | Inglês |
| B20-05 | 1.2 | CloudTrail trail | Situacional | Intermediate | Inglês |
| B20-06 | 1.2 | AWS Config | Situacional | Intermediate | Inglês |
| B20-07 | 1.2 | CloudWatch versus CloudTrail versus Config | Situacional | Intermediate | Inglês |
| B20-08 | 1.2 | CloudTrail data events | Situacional | Intermediate | Inglês |
| B20-09 | 2.1 | EventBridge reliability | Situacional | Intermediate | Inglês |
| B20-10 | 1.1 | AWS Organizations | Situacional | Basic | Inglês |

## Questões

### B20-01

**Context:** An EC2 operations team can see CPU and network metrics but cannot see memory utilization.

**Requirement:** It needs guest operating system memory metrics in CloudWatch.

**Question:** What should the team do?

- A. Enable a CloudTrail trail.
- B. Install and configure the CloudWatch agent with an IAM role.
- C. Create an AWS Config rule.
- D. Create an EventBridge scheduled rule only.

**Before moving on:** record decisive words and confidence.

### B20-02

**Context:** A service must notify operators only when average CPU exceeds 80 percent for three consecutive five-minute periods.

**Requirement:** The evaluation window and notification must be explicit.

**Question:** Which solution meets the requirement?

- A. A CloudWatch alarm configured with the metric, period, evaluation periods, threshold, and notification action.
- B. A CloudTrail Event history filter.
- C. An AWS Config recorder.
- D. A VPC Flow Log.

**Before moving on:** record decisive words and confidence.

### B20-03

**Context:** A Lambda function must run whenever an EC2 instance changes to the stopped state.

**Requirement:** The solution should react to the event without polling.

**Question:** Which service should route the event?

- A. Amazon CloudWatch Logs storage only.
- B. AWS Config only.
- C. Amazon EventBridge.
- D. AWS Organizations.

**Before moving on:** record decisive words and confidence.

### B20-04

**Context:** An administrator needs to find who recently deleted an IAM role in the current Region.

**Requirement:** Only recent management activity is needed, and no trail has been configured.

**Question:** What should the administrator use first?

- A. Amazon Quick Sight.
- B. CloudWatch CPU metrics.
- C. AWS Config conformance pack.
- D. CloudTrail Event history.

**Before moving on:** record decisive words and confidence.

### B20-05

**Context:** A security team must retain selected account API activity in an S3 bucket for multiple years.

**Requirement:** Events must be delivered continuously rather than relying on the recent console history.

**Question:** Which resource should the team configure?

- A. A CloudTrail trail.
- B. A CloudWatch dashboard.
- C. A Config rule with no recorder.
- D. An EventBridge archive only.

**Before moving on:** record decisive words and confidence.

### B20-06

**Context:** Auditors need a timeline of how an EC2 security group was configured and whether it violated an approved rule.

**Requirement:** The solution must track configuration and evaluate compliance.

**Question:** Which service meets the requirement?

- A. CloudWatch Metrics.
- B. AWS Config.
- C. Amazon Inspector.
- D. AWS Shield.

**Before moving on:** record decisive words and confidence.

### B20-07

**Context:** A team investigates a security group change that caused application errors.

**Requirement:** It needs operational impact, API authorship, and the resulting configuration.

**Question:** Which mapping is correct?

- A. CloudTrail for CPU, Config for logs, and CloudWatch for caller.
- B. Config for CPU, CloudWatch for caller, and CloudTrail for compliance.
- C. CloudWatch for impact, CloudTrail for caller, and Config for configuration.
- D. Organizations for all three.

**Before moving on:** record decisive words and confidence.

### B20-08

**Context:** A company must audit object-level GetObject and PutObject operations in a sensitive S3 bucket.

**Requirement:** The events are high volume and must be selected intentionally.

**Question:** What should be enabled?

- A. A Config rule for CPU.
- B. Only the default Event history management events.
- C. Only EC2 detailed monitoring.
- D. CloudTrail data events for the selected bucket.

**Before moving on:** record decisive words and confidence.

### B20-09

**Context:** An EventBridge target can temporarily fail, and the business cannot silently lose matched events.

**Requirement:** The design needs retries and a place for events that exhaust retries.

**Question:** What should be configured?

- A. A retry policy and a dead-letter queue for the target.
- B. A larger EC2 root volume.
- C. An SCP that grants EventBridge access.
- D. A CloudWatch dashboard only.

**Before moving on:** record decisive words and confidence.

### B20-10

**Context:** A company wants consolidated billing and a hierarchy that groups AWS accounts for centralized governance.

**Requirement:** The solution must organize accounts into logical units.

**Question:** Which service and construct should be used?

- A. CloudWatch with log groups.
- B. AWS Organizations with organizational units.
- C. AWS Config with conformance packs only.
- D. Amazon VPC with subnets.

**Before moving on:** record decisive words and confidence.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B20-01 |  |  |  |
| B20-02 |  |  |  |
| B20-03 |  |  |  |
| B20-04 |  |  |  |
| B20-05 |  |  |  |
| B20-06 |  |  |  |
| B20-07 |  |  |  |
| B20-08 |  |  |  |
| B20-09 |  |  |  |
| B20-10 |  |  |  |
