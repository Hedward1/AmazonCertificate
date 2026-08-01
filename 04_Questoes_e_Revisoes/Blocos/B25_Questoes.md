# B25 — Questões: CloudFormation, operações, custos e Well-Architected

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione a quantidade indicada em cada questão<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B25_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B25-01 | 2.2 | CloudFormation change set | single | fundamental | básica | Inglês |
| B25-02 | 2.2 | CloudFormation drift | single | situacional | intermediária | Inglês |
| B25-03 | 1.1 | CloudFormation service role | single | situacional | intermediária | Inglês |
| B25-04 | 1.2 | Session Manager operations | multi-2 | integrada | avançada | Inglês |
| B25-05 | 3.2 | Managed compute integration | single | integrada | avançada | Inglês |
| B25-06 | 4.2 | AWS Outposts e compute híbrido | single | integrada | avançada | Inglês |
| B25-07 | 4.2 | Cost Anomaly Detection | single | integrada | avançada | Inglês |
| B25-08 | 2.2 | Well-Architected review | single | situacional | intermediária | Inglês |
| B25-09 | 4.2 | CUR and Compute Optimizer | multi-3 | integrada | avançada | Inglês |
| B25-10 | 2.2 | Retained state and resilient automation | single | integrada | avançada | Inglês |

## Questões

### B25-01

**Context:** A CloudFormation template update might replace a stateful database resource.

**Requirement:** The operations team must review proposed changes before execution.

**Question:** What should the team create?

- A. A change set.
- B. A VPC Flow Log.
- C. An SCP that grants database access.
- D. A Cost Anomaly monitor.

### B25-02

**Context:** An administrator manually changed a supported property of a resource that belongs to a CloudFormation stack.

**Requirement:** The team needs to compare the actual configuration with the expected template configuration.

**Question:** Which feature should be used?

- A. CloudTrail Event history only.
- B. CloudFormation drift detection.
- C. AWS Shield Advanced.
- D. Amazon SES.

### B25-03

**Context:** A stack uses a CloudFormation service role to create resources.

**Requirement:** Administrators must prevent users from passing an overly privileged role to CloudFormation.

**Question:** Which permission requires particular control?

- A. iam:PassRole.
- B. s3:GetObject only.
- C. cloudwatch:GetMetricData only.
- D. route53:ListHostedZones only.

### B25-04

**Context:** Private EC2 instances must be administered without inbound SSH, public IP addresses, a bastion, or general internet egress. Sessions must use IAM authorization and be auditable.

**Requirement:** Select the managed session capability and the private connectivity needed to reach it. **Choose TWO.**

- A. Use Systems Manager Session Manager with an appropriate instance profile and logging configuration.
- B. Open TCP 22 from the corporate internet and store shared SSH keys in user data.
- C. Use Amazon CloudFront as the interactive shell endpoint.
- D. Configure the required Systems Manager interface VPC endpoints and private DNS for the isolated VPC.
- E. Use AWS WAF rules to authorize operating-system commands.

### B25-05

**Context:** A research company runs containerized rendering and genomics jobs
with dependencies, queue priorities, retry rules, and highly variable CPU/GPU
demand. Jobs may wait for capacity, can use Spot where interruption is
acceptable, and do not require a continuously running stream processor.

**Requirement:** Use a managed scheduler that selects and scales compatible
compute environments while the company pays for underlying resources.

**Question:** Which design best fits?

- A. Run an Amazon ECS service whose long-lived workers poll SQS, and build custom dependency, priority, retry, GPU-placement, and scale-to-zero logic.
- B. Use Step Functions Distributed Map with ECS `RunTask` integrations for every job and implement queue fairness, capacity selection, retries, and large-scale scheduler behavior in workflows.
- C. Use AWS Batch job definitions, queues, scheduling policies/dependencies, and managed EC2/Fargate compute environments appropriate to each workload.
- D. Run Kubernetes Jobs on Amazon EKS with a separately operated queueing/scheduling stack and node autoscaling, retaining the Kubernetes operations the team has not requested.

### B25-06

**Context:** A factory control workload must process data inside the customer's
facility because equipment interactions require single-digit-millisecond local
latency and policy requires local processing. The company wants supported EC2,
EBS, and ECS interfaces, AWS-managed infrastructure, and VPC integration. The
site can provide rack space, power, networking, and resilient connectivity to
the parent Region, and the team can plan finite capacity in advance.

**Requirement:** Select the hybrid compute placement that satisfies the local
execution requirement with the least customer management of infrastructure.

**Question:** Which design is appropriate?

- A. Run the workload in an AWS Local Zone; a Local Zone is installed inside
  the customer's factory and uses the customer's power and racks.
- B. Deploy an appropriately sized AWS Outposts rack at the factory, design the
  service link and local connectivity for resilience, and run supported AWS
  resources in Outpost subnets.
- C. Use AWS Direct Connect to a Region and assume the circuit places EC2 and
  EBS capacity physically inside the factory.
- D. Operate customer-owned servers and Kubernetes on premises; this preserves
  local compute but does not satisfy the requirement for AWS-managed local
  infrastructure and supported AWS service interfaces.

### B25-07

**Context:** A company needs notifications when service-level daily spend
deviates from learned patterns, then needs analysts to attribute the change by
account, service, and Region. A separate forecast threshold is already managed
as a budget; neither mechanism should be described as automatically stopping
resources.

**Requirement:** Add model-based anomaly monitoring and a notification path
without replacing attribution or budget controls.

**Question:** Which design is correct?

- A. Configure AWS Cost Anomaly Detection monitors and alert subscriptions, investigate detections with Cost Explorer/cost data, and retain Budgets for explicit actual/forecast thresholds.
- B. Use AWS Budgets with actual/forecast thresholds as if fixed thresholds were a learned anomaly model, then skip service-level anomaly monitors.
- C. Schedule Cost Explorer queries and custom Lambda statistical rules, owning seasonality, false positives, notification state, and model maintenance.
- D. Use a CloudWatch billing alarm with one static account-level threshold and treat it as service-level learned-pattern detection.

### B25-08

**Context:** A team is reviewing a low-cost single-AZ design. Moving to multiple
AZs improves reliability but raises cost and embodied/operational resource use;
automation can reduce operational risk. The team needs a structured review,
documented improvement plan, and explicit trade-offs rather than a tool that
silently changes production.

**Requirement:** Use the complete current AWS Well-Architected decision model
and record findings without treating pillars as isolated service categories.

**Question:** Which approach is correct?

- A. Replace the workload review with outputs from Trusted Advisor, Security Hub CSPM, and Compute Optimizer, assuming automated checks cover every architectural trade-off and business context.
- B. Evaluate Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability together, and use the Well-Architected Tool to record risks and improvements rather than automatically remediate resources.
- C. Use the Well-Architected Tool but review only five historical pillars, omitting Sustainability from trade-offs and the improvement plan.
- D. Review all six pillars, then configure automation to apply every recorded improvement directly to production without owner approval or workload testing.

### B25-09

**Context:** A FinOps team needs line-item cost and usage data for SQL analysis, resource rightsizing recommendations based on utilization, and alerts when spending deviates from learned patterns.

**Requirement:** Use purpose-built AWS capabilities for detailed allocation, optimization, and anomaly notification. **Select THREE.**

- A. Deliver AWS Cost and Usage Reports to Amazon S3 for detailed cost records.
- B. Use AWS Artifact to recommend EC2 instance sizes.
- C. Use AWS Compute Optimizer for supported resource recommendations.
- D. Use Amazon Inspector as the cost allocation ledger.
- E. Configure AWS Cost Anomaly Detection monitors and alert subscriptions.
- F. Use CloudTrail Event history as the authoritative line-item billing dataset.

### B25-10

**Context:** An RDS database is managed by CloudFormation. The company must preserve a recoverable snapshot if the stack is deleted or if an update replaces the database, while allowing stateless resources to follow normal deletion behavior.

**Requirement:** Apply protection specifically to the stateful resource through infrastructure as code.

**Question:** Which design best meets the requirement?

- A. Set `DeletionPolicy: Snapshot` and `UpdateReplacePolicy: Snapshot` on the database resource.
- B. Set `DeletionPolicy: Delete` and rely on stack event history as the backup.
- C. Add a stack output containing the database endpoint; outputs prevent deletion and replacement.
- D. Use a CloudFormation change set only; a change set automatically snapshots replaced databases.

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
