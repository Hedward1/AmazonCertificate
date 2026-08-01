# B20 — Gabarito comentado

Volte às [questões B20](B20_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B20-01 | B | 2.2 |
| B20-02 | A | 2.2 |
| B20-03 | C | 2.1 |
| B20-04 | D | 1.2 |
| B20-05 | A | 1.2 |
| B20-06 | B | 1.2 |
| B20-07 | C | 1.2 |
| B20-08 | D | 1.2 |
| B20-09 | A | 2.1 |
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

## B20-04 — Answer D

- **Central requirement:** Only recent management activity is needed, and no trail has been configured.
- **Decisive words:** who, recently, management activity, no trail
- **Why the correct answer works:** Event history provides searchable recent management events without requiring a trail.
- **A:** BI is unrelated.
- **B:** CPU metrics do not show API authorship.
- **C:** A conformance pack evaluates configuration.
- **D:** Event history is correct.
- **Reusable rule:** Recent API authorship points to CloudTrail Event history.
- **Cost/operation:** Event history itself does not require creating a trail.
- **Variation:** A trail is needed for continuous delivery and longer retention.
- **Lessons:** 276–281
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)

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

## B20-07 — Answer C

- **Central requirement:** It needs operational impact, API authorship, and the resulting configuration.
- **Decisive words:** impact, authorship, resulting configuration
- **Why the correct answer works:** Each service answers a distinct part of the investigation.
- **A:** The roles are incorrect.
- **B:** The roles are reversed.
- **C:** The mapping is correct.
- **D:** Organizations does not provide these three signals.
- **Reusable rule:** CloudWatch observes behavior; CloudTrail audits actions; Config tracks resource state.
- **Cost/operation:** Using all services improves evidence but adds ingestion, retention, and evaluation costs.
- **Variation:** EventBridge can automate a response from the audit event.
- **Lessons:** 264–281
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/pdfs/decision-guides/latest/cloudtrail-or-cloudwatch/cloudtrail-or-cloudwatch.pdf)

## B20-08 — Answer D

- **Central requirement:** The events are high volume and must be selected intentionally.
- **Decisive words:** object-level, GetObject, PutObject, high volume
- **Why the correct answer works:** S3 object-level operations are CloudTrail data events and require deliberate selection.
- **A:** Config CPU is unrelated.
- **B:** Event history management events do not provide the requested object activity.
- **C:** EC2 monitoring is unrelated.
- **D:** Selected data events are correct.
- **Reusable rule:** Operations inside a resource often map to CloudTrail data events.
- **Cost/operation:** Data event volume can create substantial CloudTrail and storage charges.
- **Variation:** Apply selectors narrowly to required resources and actions.
- **Lessons:** 276–281
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html)

## B20-09 — Answer A

- **Central requirement:** The design needs retries and a place for events that exhaust retries.
- **Decisive words:** temporarily fail, cannot lose, exhaust retries
- **Why the correct answer works:** EventBridge target retry policy and DLQ provide controlled handling of failed delivery.
- **A:** Retry and DLQ are correct.
- **B:** Storage on EC2 is unrelated.
- **C:** SCP never grants permissions.
- **D:** A dashboard does not preserve failed events.
- **Reusable rule:** Asynchronous delivery needs idempotency, retries, and DLQ.
- **Cost/operation:** SQS DLQ, target invocations, and logging can incur charges.
- **Variation:** The consumer should remain idempotent because retries can repeat delivery.
- **Lessons:** 273–275
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-dlq.html)

## B20-10 — Answer B

- **Central requirement:** The solution must organize accounts into logical units.
- **Decisive words:** accounts, consolidated billing, hierarchy
- **Why the correct answer works:** Organizations manages multiple accounts and OUs group accounts for governance.
- **A:** Log groups organize logs.
- **B:** Organizations and OUs are correct.
- **C:** Config does not create account hierarchy.
- **D:** Subnets organize networks.
- **Reusable rule:** Multi-account hierarchy and consolidated billing point to Organizations and OUs.
- **Cost/operation:** Creating an organization changes governance even when the service has no direct usage fee.
- **Variation:** SCP behavior is covered in B21.
- **Lessons:** 282
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
