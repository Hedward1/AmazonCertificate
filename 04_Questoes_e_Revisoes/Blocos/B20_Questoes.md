# B20 — Questões: CloudWatch, EventBridge, CloudTrail, Config e Organizations

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione a quantidade indicada em cada questão<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B20_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B20-01 | 2.2 | CloudWatch agent | single | fundamental | básica | Inglês |
| B20-02 | 2.2 | CloudWatch alarm | single | situacional | intermediária | Inglês |
| B20-03 | 2.1 | EventBridge | single | situacional | intermediária | Inglês |
| B20-04 | 1.2 | CloudTrail investigation | multi-2 | integrada | avançada | Inglês |
| B20-05 | 1.2 | CloudTrail trail | single | situacional | intermediária | Inglês |
| B20-06 | 1.2 | AWS Config | single | situacional | intermediária | Inglês |
| B20-07 | 2.2 | X-Ray observability | multi-2 | integrada | avançada | Inglês |
| B20-08 | 1.2 | CloudTrail data events | single | integrada | avançada | Inglês |
| B20-09 | 1.2 | Security Hub, Audit Manager and Artifact | multi-3 | integrada | avançada | Inglês |
| B20-10 | 1.1 | Organizations and governance | single | situacional | intermediária | Inglês |

## Questões

### B20-01

**Context:** An EC2 operations team can see CPU and network metrics but cannot see memory utilization.

**Requirement:** It needs guest operating system memory metrics in CloudWatch.

**Question:** What should the team do?

- A. Enable a CloudTrail trail.
- B. Install and configure the CloudWatch agent with an IAM role.
- C. Create an AWS Config rule.
- D. Create an EventBridge scheduled rule only.

### B20-02

**Context:** A service must notify operators only when average CPU exceeds 80 percent for three consecutive five-minute periods.

**Requirement:** The evaluation window and notification must be explicit.

**Question:** Which solution meets the requirement?

- A. A CloudWatch alarm configured with the metric, period, evaluation periods, threshold, and notification action.
- B. A CloudTrail Event history filter.
- C. An AWS Config recorder.
- D. A VPC Flow Log.

### B20-03

**Context:** A Lambda function must run whenever an EC2 instance changes to the stopped state.

**Requirement:** The solution should react to the event without polling.

**Question:** Which service should route the event?

- A. Amazon CloudWatch Logs storage only.
- B. AWS Config only.
- C. Amazon EventBridge.
- D. AWS Organizations.

### B20-04

**Context:** An administrator must identify who deleted an IAM role yesterday. The company also needs durable multi-Region management-event records for future investigations.

**Requirement:** Provide the fastest answer for the recent event and establish long-term evidence. **Choose TWO.**

- A. Query CloudWatch CPU metrics for the role name.
- B. Search CloudTrail Event history in `us-east-1` for the recent global IAM management event.
- C. Enable only an AWS Config conformance pack; Config records the API caller identity.
- D. Use Amazon Quick Sight as the source of API audit records.
- E. Create a multi-Region CloudTrail trail that delivers management events to a protected S3 bucket.

### B20-05

**Context:** A security team must retain selected account API activity in an S3 bucket for multiple years.

**Requirement:** Events must be delivered continuously rather than relying on the recent console history.

**Question:** Which resource should the team configure?

- A. A CloudTrail trail.
- B. A CloudWatch dashboard.
- C. A Config rule with no recorder.
- D. An EventBridge archive only.

### B20-06

**Context:** Auditors need a timeline of how an EC2 security group was configured and whether it violated an approved rule.

**Requirement:** The solution must track configuration and evaluate compliance.

**Question:** Which service meets the requirement?

- A. CloudWatch Metrics.
- B. AWS Config.
- C. Amazon Inspector.
- D. AWS Shield.

### B20-07

**Context:** Requests traverse API Gateway, Lambda, and DynamoDB. Operators see elevated end-to-end latency but need to isolate which downstream segment is slow and correlate traces with service metrics.

**Requirement:** Add distributed tracing and a consolidated observability view with minimal custom correlation. **Choose TWO.**

- A. Enable AWS X-Ray tracing on supported components and propagate trace context.
- B. Use CloudTrail data events as application latency spans.
- C. Use AWS Config snapshots to reconstruct request-level call paths.
- D. Use CloudWatch ServiceLens to correlate traces, metrics, and logs.
- E. Use AWS Organizations consolidated billing as the service map.

### B20-08

**Context:** A regulated data lake must record `GetObject`, `PutObject`, and
`DeleteObject` for one sensitive S3 prefix, retain the audit trail separately
from the workload account, and avoid the cost/noise of logging object activity
for every bucket. Management changes to the bucket must remain auditable too.

**Requirement:** Capture both control-plane and narrowly selected object-level
activity with durable centralized retention.

**Question:** Which design best meets the requirement?

- A. Combine AWS Config history with S3 Inventory reports and treat configuration/object listings as complete API-access evidence.
- B. Put broad S3 data events in a CloudTrail Lake event data store in the workload account, disable the organization management trail, and omit the required central S3 retention boundary.
- C. Enable S3 server access logging into the same sensitive bucket and rely only on default CloudTrail Event history for management activity.
- D. Use a multi-Region CloudTrail trail for management events, add narrowly scoped S3 data-event selectors for the required prefix/actions, and deliver logs to a protected central S3 destination.

### B20-09

**Context:** A regulated organization needs one view of security findings, continuously collected audit evidence mapped to controls, and on-demand access to AWS compliance reports and agreements.

**Requirement:** Select the purpose-built managed service for each distinct outcome. **Select THREE.**

- A. Use AWS Security Hub to aggregate and prioritize findings from supported security services.
- B. Use Amazon Inspector to download AWS SOC reports and accept agreements.
- C. Use AWS Audit Manager to automate evidence collection and assessments.
- D. Use CloudWatch dashboards as the authoritative repository for compliance agreements.
- E. Use AWS Artifact to aggregate runtime GuardDuty findings.
- F. Use AWS Artifact to access AWS compliance documents and agreements.

### B20-10

**Context:** A company is separating production, development, security, and
log-archive workloads into AWS accounts. It needs consolidated billing,
hierarchical policy boundaries, delegated administration for security services,
and the ability to move accounts without redesigning their VPCs.

**Requirement:** Establish a scalable account-governance foundation rather
than a resource hierarchy inside one account.

**Question:** Which design should be used?

- A. Keep one payer account and represent production/development with Resource Groups, tags, and separate VPCs.
- B. Use AWS Organizations, place accounts in purpose-specific organizational units, apply guardrails such as SCPs at the appropriate level, and delegate supported services.
- C. Keep independently billed accounts outside an organization and use an AWS Config aggregator as the governance and billing hierarchy.
- D. Create a separate AWS Organization for each business unit and exchange cross-account roles between management accounts for every central service.

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
