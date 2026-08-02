# B25 — Gabarito comentado

Volte às [questões B25](B25_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B25-01 | A | 2.2 |
| B25-02 | B | 2.2 |
| B25-03 | A | 1.1 |
| B25-04 | A,D | 1.2 |
| B25-05 | C | 3.2 |
| B25-06 | B | 4.2 |
| B25-07 | A | 4.2 |
| B25-08 | B | 2.2 |
| B25-09 | A,C,E | 4.2 |
| B25-10 | A | 2.2 |

## B25-01 — Answer A

- **Central requirement:** The operations team must review proposed changes before execution.
- **Decisive words:** review proposed changes, before execution, replace
- **Why the correct answer works:** A change set compares the proposed template and parameters with the current stack and previews actions such as replacement.
- **A:** This is correct.
- **B:** Flow Logs provide network metadata.
- **C:** An SCP does not grant and does not preview stack changes.
- **D:** Cost monitoring does not preview infrastructure updates.
- **Reusable rule:** Preview a CloudFormation update with a change set.
- **Cost/operation:** The change set itself is not the resource cost; created or replaced resources are.
- **Variation:** A change set does not guarantee that execution is risk-free.
- **Lessons:** 368–370
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html)

## B25-02 — Answer B

- **Central requirement:** The team needs to compare the actual configuration with the expected template configuration.
- **Decisive words:** manual change, actual versus expected template
- **Why the correct answer works:** Drift detection compares actual supported resource properties with the stack template expectation.
- **A:** CloudTrail can show an API caller but does not perform the requested template comparison.
- **B:** This is correct.
- **C:** Shield is DDoS protection.
- **D:** SES sends email.
- **Reusable rule:** Detect out-of-band changes with CloudFormation drift detection.
- **Cost/operation:** Drift does not remove or recreate resources automatically.
- **Variation:** Not every resource type and property supports drift detection.
- **Lessons:** 368–370
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)

## B25-03 — Answer A

- **Central requirement:** Administrators must prevent users from passing an overly privileged role to CloudFormation.
- **Decisive words:** service role, pass, overly privileged
- **Why the correct answer works:** iam:PassRole controls whether a principal can pass a service role for CloudFormation to assume.
- **A:** This is correct.
- **B:** S3 read alone is not the pass control.
- **C:** Metrics read is unrelated.
- **D:** DNS listing is unrelated.
- **Reusable rule:** Passing a role to an AWS service requires tightly controlled iam:PassRole.
- **Cost/operation:** An overprivileged role expands blast radius even without direct service-role credentials.
- **Variation:** Once associated, stack operations can use the role permissions.
- **Lessons:** 370
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html)

## B25-04 — Answer A,D

- **Central requirement:** administer isolated instances through IAM-authorized, logged sessions without inbound ports or internet egress.
- **Decisive words:** *no SSH*, *no public IP*, *no general internet*, *IAM*, *auditable*.
- **A:** correct; Session Manager provides managed interactive access and supports session logging when prerequisites are configured.
- **B:** incorrect; opening SSH and sharing keys violates every access constraint.
- **C:** incorrect; CloudFront is a CDN and does not provide operating-system sessions.
- **D:** correct; Systems Manager interface endpoints and private DNS provide private service reachability from the isolated VPC.
- **E:** incorrect; WAF authorizes and filters supported web requests, not shell commands.
- **Reusable rule:** private Session Manager requires both the management plane capability and an IAM/network path from the managed node.
- **Lessons:** 373–374.
- **Official reference:** [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) and [Systems Manager VPC endpoints](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html).

## B25-05 — Answer C

- **Central requirement:** schedule dependent, prioritized container jobs onto elastic compute with workload-specific capacity/cost choices.
- **Decisive words:** dependencies, queue priorities, retry, GPU, Spot, may wait
- **Why the correct answer works:** AWS Batch supplies job definitions/queues/scheduling and orchestrates supported managed compute environments for batch demand.
- **A:** ECS workers plus SQS can form a valid custom batch platform, but the option requires building the dependencies, priority scheduling, retries, placement, and scaling logic AWS Batch already supplies.
- **B:** Step Functions can orchestrate ECS tasks and Distributed Map can fan out work, but recreating fair job queues and heterogeneous compute scheduling adds complexity for this batch-compute requirement.
- **C:** correct; queues and policies express scheduling, definitions express resources/retries, and compute-environment choices balance compatibility, interruption, and cost.
- **D:** EKS Jobs can run the workloads and specialized schedulers exist, but the proposal adds Kubernetes control/data-plane operations without a Kubernetes constraint.
- **Reusable rule:** queued finite container jobs with dependencies and elastic compute point to AWS Batch; continuous records and stateful windows point to streaming services.
- **Cost/operation:** The service orchestrates compute, and the underlying compute and storage are billed.
- **Variation:** Validate whether each job can tolerate interruption before using Spot and whether its resource shape is supported by the chosen compute environment.
- **Lessons:** 367–381
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)

## B25-06 — Answer B

- **Central requirement:** run supported AWS compute and storage inside the
  customer facility for local latency/processing while AWS manages the local
  infrastructure.
- **Decisive words:** *inside the facility*, *local latency*, *AWS-managed*,
  *finite capacity planned*, *service link*.
- **Why the correct answer works:** Outposts extends supported AWS
  infrastructure, services, APIs, and tools to the customer site and integrates
  Outpost subnets with the parent VPC/Region.
- **A:** Local Zones place resources in AWS-operated metropolitan locations;
  they are not installed in the customer's facility.
- **B:** correct; it meets local execution and AWS-management requirements, but
  requires site readiness, capacity planning, and resilient Region connectivity.
- **C:** Direct Connect provides private connectivity to AWS; it does not put EC2
  or EBS hardware at the customer site.
- **D:** customer-owned infrastructure can satisfy locality, but the customer
  remains responsible for the hardware/platform and does not receive the
  requested Outposts operating model.
- **Reusable rule:** choose Outposts for AWS-managed compute at the customer
  site; choose Local Zones for nearby AWS placement; choose Direct Connect for
  connectivity to a Region.
- **Cost/operation:** installed capacity is finite and can be idle; size for
  growth, maintenance/failure headroom, facility needs, and connectivity.
- **Variation:** if no local-execution requirement exists, a Region connected by
  Direct Connect is usually simpler and more elastic.
- **Lessons:** 377
- **Official reference:** [What is AWS Outposts?](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html)

## B25-07 — Answer A

- **Central requirement:** detect model-based spend deviations, notify owners, preserve attribution analysis, and keep explicit threshold budgets separate.
- **Decisive words:** learned patterns, service-level deviation, attribute, separate forecast threshold, not stop resources
- **Why the correct answer works:** Cost Anomaly Detection models expected spend and uses subscriptions for alerts; Cost Explorer/cost data supports investigation, while Budgets covers configured thresholds.
- **A:** correct; each capability has a distinct role and none is misrepresented as automatic resource shutdown.
- **B:** Budgets is correct for explicit thresholds and forecasts, but it is not the requested learned-pattern anomaly detector.
- **C:** custom Cost Explorer analytics could be built, but the team would own statistical modeling, seasonality, state, and alert quality already provided by the managed capability.
- **D:** a static billing alarm lacks learned service-level patterns and the richer monitor/subscription dimensions requested.
- **Reusable rule:** anomaly model → Cost Anomaly Detection; explicit actual/forecast threshold → Budgets; interactive attribution → Cost Explorer or detailed cost data.
- **Cost/operation:** Alerts do not stop resources; investigation and cleanup remain necessary.
- **Variation:** Notifications require ownership and a remediation runbook because cost alerts themselves do not stop resources.
- **Lessons:** 375–376
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)

## B25-08 — Answer B

- **Central requirement:** evaluate cross-pillar trade-offs with the complete framework and record an improvement plan without automatic production changes.
- **Decisive words:** single-AZ, reliability versus cost/sustainability, automation, documented improvement, not silently changes
- **Why the correct answer works:** the six pillars are simultaneous decision dimensions, and the Well-Architected Tool records workloads, risks, and improvement items for human-governed remediation.
- **A:** these services provide valuable signals, but automated checks cannot replace workload-specific pillar trade-offs, business context, and an owned improvement plan.
- **B:** correct; it uses the complete current pillar set and correctly limits the Tool's role to review/documentation rather than autonomous remediation.
- **C:** the Tool is appropriate, but omitting Sustainability means the review is not using the complete current framework requested.
- **D:** recording improvements does not authorize untested automatic production mutations; owners must prioritize, test, and implement changes through governance.
- **Reusable rule:** Well-Architected is a trade-off framework across six pillars; the Tool records review state and improvement plans but does not redesign workloads automatically.
- **Cost/operation:** Cost Optimization is one pillar and must be balanced with the other five.
- **Variation:** Revisit reviews after material workload or business changes; a risk accepted today may need a different trade-off later.
- **Lessons:** 382–385
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html)

## B25-09 — Answer A,C,E

- **Central requirement:** deliver detailed cost data, utilization-based rightsizing, and learned-pattern anomaly alerts.
- **Decisive words:** *line-item*, *SQL analysis*, *rightsizing*, *deviates from learned patterns*.
- **A:** correct; Cost and Usage Reports deliver detailed billing and usage records to S3.
- **B:** incorrect; Artifact provides compliance reports and agreements, not rightsizing.
- **C:** correct; Compute Optimizer analyzes utilization for supported resource recommendations.
- **D:** incorrect; Inspector assesses security vulnerabilities, not billing allocation.
- **E:** correct; Cost Anomaly Detection learns patterns and sends alerts for anomalous spend.
- **F:** incorrect; CloudTrail is an API audit source, not the authoritative line-item billing dataset.
- **Reusable rule:** CUR is detailed cost evidence, Compute Optimizer is rightsizing, and Cost Anomaly Detection is behavioral spend alerting.
- **Lessons:** 375–384.
- **Official reference:** [Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html), [Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html), and [Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html).

## B25-10 — Answer A

- **Central requirement:** preserve recoverable database state on both stack deletion and update-driven replacement.
- **Decisive words:** *stack deleted*, *update replaces*, *snapshot*, *stateful resource only*.
- **A:** correct; `DeletionPolicy` governs stack deletion while `UpdateReplacePolicy` governs the old physical resource during replacement.
- **B:** incorrect; stack events are metadata and cannot restore deleted database contents.
- **C:** incorrect; outputs expose values but do not change resource lifecycle behavior.
- **D:** incorrect; a change set previews changes but does not automatically snapshot a replacement.
- **Reusable rule:** use `DeletionPolicy` for deletion behavior and `UpdateReplacePolicy` for replacement behavior; set both explicitly for stateful resources.
- **Lessons:** 368–396.
- **Official reference:** [DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html) and [UpdateReplacePolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatereplacepolicy.html).
