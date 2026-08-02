# B20 — Gabarito comentado

Volte às [questões B20](B20_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B20-01 | B | 2.2 |
| B20-02 | A | 2.2 |
| B20-03 | C | 2.1 |
| B20-04 | B,E | 1.2 |
| B20-05 | A | 1.2 |
| B20-06 | B | 1.2 |
| B20-07 | A,D | 2.2 |
| B20-08 | D | 1.2 |
| B20-09 | A,C,F | 1.2 |
| B20-10 | B | 1.1 |

## B20-01 — Answer B

- **Central requirement:** It needs guest operating system memory metrics in CloudWatch.
- **Decisive words:** EC2, memory, guest operating system
- **Why the correct answer works:** The CloudWatch agent collects guest operating system metrics such as memory.
- **A:** CloudTrail records API activity.
- **B:** The agent is correct.
- **C:** Config evaluates configuration.
- **D:** A schedule does not collect memory.
- **Reusable rule:** Hypervisor metrics are standard; guest OS memory and disk require an agent or custom publication.
- **Cost/operation:** Custom metrics and logs can incur charges.
- **Variation:** The agent can also collect log files.
- **Lessons:** 264–272
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

## B20-02 — Answer A

- **Central requirement:** The evaluation window and notification must be explicit.
- **Decisive words:** average CPU, three periods, notify
- **Why the correct answer works:** A CloudWatch alarm evaluates a metric across configured periods and can invoke a notification action.
- **A:** The alarm is correct.
- **B:** Event history tracks API activity.
- **C:** Config records configuration.
- **D:** Flow Logs record network metadata.
- **Reusable rule:** Threshold over time plus action maps to a CloudWatch alarm.
- **Cost/operation:** Alarms and notification targets may incur charges.
- **Variation:** Composite alarms can reduce noise across multiple alarms.
- **Lessons:** 265–271
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## B20-03 — Answer C

- **Central requirement:** The solution should react to the event without polling.
- **Decisive words:** whenever, state changes, without polling
- **Why the correct answer works:** EventBridge rules match state-change events and route them to targets such as Lambda.
- **A:** Log storage alone does not invoke the target.
- **B:** Config is not the event router in this requirement.
- **C:** EventBridge is correct.
- **D:** Organizations manages accounts.
- **Reusable rule:** Event source plus pattern plus target points to EventBridge.
- **Cost/operation:** Targets, retries, logs, and DLQs can incur downstream charges.
- **Variation:** For time-based execution, evaluate EventBridge Scheduler.
- **Lessons:** 273–275
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is-how-it-works-concepts.html)

## B20-04 — Answer B,E

- **Central requirement:** answer a recent caller investigation immediately and create durable future audit retention.
- **Decisive words:** *deleted yesterday*, *who*, *future investigations*, *multi-Region*.
- **A:** incorrect; CPU metrics do not record IAM API caller identity.
- **B:** correct; IAM is a global service, and its global service events are
  recorded in `us-east-1`. Event history there exposes the recent management
  event without requiring a pre-existing trail.
- **C:** incorrect; Config records resource configuration/compliance, not the complete API caller audit record.
- **D:** incorrect; Quick Sight is a BI service, not the source of CloudTrail events.
- **E:** correct; a multi-Region trail continuously delivers management events to durable S3 storage.
- **Reusable rule:** CloudTrail Event history is the quick recent lookup; for
  global IAM events, search `us-east-1`. A multi-Region trail is the durable,
  continuously delivered audit design.
- **Lessons:** 276–281.
- **Official reference:** [Viewing CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

## B20-05 — Answer A

- **Central requirement:** Events must be delivered continuously rather than relying on the recent console history.
- **Decisive words:** retain, S3, multiple years, continuously
- **Why the correct answer works:** A trail continuously delivers selected CloudTrail events to S3 and can integrate with logs and notifications.
- **A:** A trail is correct.
- **B:** A dashboard visualizes metrics.
- **C:** Config does not replace API audit logs.
- **D:** An EventBridge archive is not the primary CloudTrail retention mechanism.
- **Reusable rule:** Continuous CloudTrail delivery to S3 maps to a trail.
- **Cost/operation:** Trail event selection, S3, KMS, and CloudWatch Logs can incur charges.
- **Variation:** High-volume data events must be selected deliberately.
- **Lessons:** 276–281
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html)

## B20-06 — Answer B

- **Central requirement:** The solution must track configuration and evaluate compliance.
- **Decisive words:** timeline, configured, compliance
- **Why the correct answer works:** Config records supported resource configurations and evaluates them with Config rules.
- **A:** Metrics measure behavior.
- **B:** Config is correct.
- **C:** Inspector finds workload vulnerabilities.
- **D:** Shield provides DDoS protection.
- **Reusable rule:** Configuration history plus compliance points to AWS Config.
- **Cost/operation:** Recorded configuration items and rule evaluations can incur charges.
- **Variation:** CloudTrail complements Config by identifying the API caller.
- **Lessons:** 279–281
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html)

## B20-07 — Answer A,D

- **Central requirement:** identify slow distributed request segments and correlate traces with operational telemetry.
- **Decisive words:** *API Gateway, Lambda, DynamoDB*, *end-to-end latency*, *downstream segment*, *correlate*.
- **A:** correct; X-Ray trace context and segments expose the distributed request path and latency contributors.
- **B:** incorrect; CloudTrail data events audit resource API activity and are not application tracing spans.
- **C:** incorrect; Config snapshots track resource state, not individual request call graphs.
- **D:** correct; CloudWatch ServiceLens correlates traces with metrics and logs for supported resources.
- **E:** incorrect; consolidated billing provides cost aggregation, not a service latency map.
- **Reusable rule:** metrics show symptoms; distributed traces locate latency across service boundaries; correlate both for root cause.
- **Lessons:** 264–281.
- **Official reference:** [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) and [CloudWatch ServiceLens](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html).

## B20-08 — Answer D

- **Central requirement:** preserve centralized management and selected S3 object activity without logging every high-volume bucket.
- **Decisive words:** selected prefix, object operations, management changes, central retention
- **Why the correct answer works:** CloudTrail distinguishes management events from S3 data events and supports selectors plus delivery to a separately protected logging destination.
- **A:** Config and Inventory are useful for configuration and object listings, but neither is a complete record of the requested object API calls.
- **B:** CloudTrail Lake can retain/query selected events, but this design drops the required central S3 separation and management trail while logging excessive scope.
- **C:** server access logging can supplement analysis, but same-bucket placement and default Event history do not provide the requested protected, unified, narrowly selected CloudTrail design.
- **D:** correct; the trail retains control-plane visibility, targeted data selectors constrain volume, and a central destination improves separation and retention control.
- **Reusable rule:** CloudTrail management events cover control-plane actions; high-volume resource operations such as S3 object access require deliberately scoped data events.
- **Cost/operation:** Data event volume can create substantial CloudTrail and storage charges.
- **Variation:** Use advanced event selectors, lifecycle/immutability controls, and query tooling according to audit and cost requirements.
- **Lessons:** 276–281
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html)

## B20-09 — Answer A,C,F

- **Central requirement:** map finding aggregation, audit evidence collection, and AWS compliance documents to distinct managed services.
- **Decisive words:** *one view of findings*, *evidence mapped to controls*, *reports and agreements*.
- **A:** correct; Security Hub aggregates, normalizes, and prioritizes supported security findings.
- **B:** incorrect; Inspector assesses vulnerabilities and does not distribute AWS SOC reports.
- **C:** correct; Audit Manager automates evidence collection and assessment workflows.
- **D:** incorrect; dashboards visualize data but are not the authoritative compliance-agreement repository.
- **E:** incorrect; Artifact supplies documents and agreements, not runtime finding aggregation.
- **F:** correct; Artifact provides on-demand AWS compliance reports and agreements.
- **Reusable rule:** Security Hub is findings, Audit Manager is customer audit evidence, and Artifact is AWS compliance documentation.
- **Lessons:** 264–281.
- **Official reference:** [Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), [Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html), and [Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html).

## B20-10 — Answer B

- **Central requirement:** create a multi-account governance and billing hierarchy with policy inheritance and delegated operations.
- **Decisive words:** separate accounts, consolidated billing, policy boundaries, delegated administration
- **Why the correct answer works:** Organizations supplies the account hierarchy, OUs provide policy attachment boundaries, and supported services can use delegated administrators.
- **A:** tags, VPCs, and Resource Groups can organize resources but do not provide separate account blast radii, inherited account policies, or a multi-account billing hierarchy.
- **B:** correct; it separates blast radius while centralizing governance and leaves network topology as an independent design.
- **C:** a Config aggregator can centralize configuration visibility, but standalone accounts remain outside the required billing and preventive-policy hierarchy.
- **D:** multiple organizations fragment consolidated billing and delegated administration; management accounts cannot be nested into one OU hierarchy.
- **Reusable rule:** use accounts and Organizations/OUs for administrative and policy boundaries; use VPC/subnet structure for network boundaries.
- **Cost/operation:** Creating an organization changes governance even when the service has no direct usage fee.
- **Variation:** SCPs limit maximum available permissions; they do not grant permissions and should be tested before broad attachment.
- **Lessons:** 282
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
