# B25 — Gabarito comentado

Volte às [questões B25](B25_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B25-01 | A | 2.2 |
| B25-02 | B | 2.2 |
| B25-03 | A | 1.1 |
| B25-04 | B | 1.2 |
| B25-05 | C | 2.2 |
| B25-06 | B | 3.5 |
| B25-07 | A | 4.2 |
| B25-08 | B | 2.2 |
| B25-09 | A | 2.2 |
| B25-10 | C | 2.2 |

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

## B25-04 — Answer B

- **Central requirement:** Sessions must use managed identity and can be logged.
- **Decisive words:** private, no SSH, no public IP, logged sessions
- **Why the correct answer works:** Session Manager provides managed interactive access without opening inbound administrative ports when prerequisites are met.
- **A:** WAF filters web requests.
- **B:** This is correct.
- **C:** CloudFront is a CDN.
- **D:** Snowball Edge is a legacy data-transfer and edge-compute service approaching end of support; it is unrelated to managed administrative sessions.
- **Reusable rule:** Administrative access without inbound ports points to Session Manager.
- **Cost/operation:** Logs, VPC endpoints, and storage can incur charges.
- **Variation:** Nodes need SSM Agent, IAM permissions, and network connectivity.
- **Lessons:** 373–374
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)

## B25-05 — Answer C

- **Central requirement:** It does not need continuous stream processing.
- **Decisive words:** queued, containerized jobs, batch demand
- **Why the correct answer works:** AWS Batch schedules and runs containerized batch computing workloads on managed compute environments.
- **A:** Pinpoint is a legacy engagement service approaching end of support and is unrelated to batch compute.
- **B:** AppFlow transfers data between SaaS and AWS.
- **C:** This is correct.
- **D:** Lex builds conversational interfaces.
- **Reusable rule:** Queued containerized batch jobs point to AWS Batch.
- **Cost/operation:** The service orchestrates compute, and the underlying compute and storage are billed.
- **Variation:** Continuous event streams point to streaming services instead.
- **Lessons:** 367–381
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)

## B25-06 — Answer B

- **Central requirement:** The solution should use a managed data integration service.
- **Decisive words:** SaaS, S3, minimal code, managed flow
- **Why the correct answer works:** AppFlow provides managed data flows between supported SaaS applications and AWS services.
- **A:** Outposts runs AWS infrastructure on premises.
- **B:** This is correct.
- **C:** Inspector assesses vulnerabilities.
- **D:** Direct Connect supplies connectivity, not the SaaS integration flow.
- **Reusable rule:** Supported SaaS-to-AWS managed data flow points to AppFlow.
- **Cost/operation:** Flow runs, data processing, destinations, and transfer can incur charges.
- **Variation:** Glue is more appropriate for broader custom ETL requirements.
- **Lessons:** 379
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html)

## B25-07 — Answer A

- **Central requirement:** The feature should detect anomalies, not enforce a hard spending cap.
- **Decisive words:** unexpected spending, learned patterns, notifications
- **Why the correct answer works:** Cost Anomaly Detection uses models to identify unusual spending and sends notifications through subscriptions.
- **A:** This is correct.
- **B:** A security group controls network access.
- **C:** Drift compares stack configuration.
- **D:** ACM manages certificates.
- **Reusable rule:** Unusual cost pattern points to Cost Anomaly Detection; threshold planning points to Budgets.
- **Cost/operation:** Alerts do not stop resources; investigation and cleanup remain necessary.
- **Variation:** Use Cost Explorer to attribute the anomaly by service, account, or Region.
- **Lessons:** 375–376
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)

## B25-08 — Answer B

- **Central requirement:** The team wants the complete current set of Well-Architected pillars.
- **Decisive words:** complete, pillars, environmental impact
- **Why the correct answer works:** Those are the six pillars of the AWS Well-Architected Framework.
- **A:** This is a service-category list, not the pillars.
- **B:** This is correct.
- **C:** These are practices, not the official pillars.
- **D:** These are technical topics, not the pillars.
- **Reusable rule:** Memorize the six pillars as decision areas, not products.
- **Cost/operation:** Cost Optimization is one pillar and must be balanced with the other five.
- **Variation:** The Well-Architected Tool records reviews and improvement plans but does not change resources.
- **Lessons:** 382–385
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html)

## B25-09 — Answer A

- **Central requirement:** The architect must remember that coverage varies by support plan.
- **Decisive words:** checks, recommendations, support plan
- **Why the correct answer works:** Trusted Advisor analyzes the account and provides checks and recommendations, with access depending on support level.
- **A:** This is correct.
- **B:** Kendra is enterprise search.
- **C:** DMS migrates data.
- **D:** Textract extracts documents.
- **Reusable rule:** Account recommendations across operational categories point to Trusted Advisor.
- **Cost/operation:** Recommendations identify opportunities but do not automatically remove resources.
- **Variation:** Do not assume every check is available on every plan.
- **Lessons:** 384
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)

## B25-10 — Answer C

- **Central requirement:** Cleanup must be verified, and the practice exam must remain unseen until SIM B.
- **Decisive words:** Retain, remains, reserved practice exam
- **Why the correct answer works:** Retain deliberately preserves the resource, so cleanup requires explicit ownership verification; the study plan reserves the exam for SIM B.
- **A:** Both assumptions are wrong.
- **B:** Deleting unknown resources is unsafe.
- **C:** This is correct.
- **D:** Retained resources can continue charging.
- **Reusable rule:** Stack deletion is not proof of cleanup; preserve an unseen readiness measurement.
- **Cost/operation:** Retained databases, snapshots, logs, public IPs, and keys can continue to cost.
- **Variation:** Termination protection and stack policies solve different lifecycle risks.
- **Lessons:** 368–396; practice exam excluded
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html)
