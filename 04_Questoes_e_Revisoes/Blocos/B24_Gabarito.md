# B24 — Gabarito comentado

Volte às [questões B24](B24_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B24-01 | B | 2.2 |
| B24-02 | C | 2.2 |
| B24-03 | A | 2.2 |
| B24-04 | C | 2.2 |
| B24-05 | A | 3.5 |
| B24-06 | C | 3.5 |
| B24-07 | A | 2.2 |
| B24-08 | B | 3.5 |
| B24-09 | A | 4.4 |
| B24-10 | C | 2.2 |

## B24-01 — Answer B

- **Central requirement:** The architect must translate the two limits correctly.
- **Decisive words:** data loss, restore service
- **Why the correct answer works:** RPO is acceptable data loss measured in time; RTO is acceptable recovery duration.
- **A:** The values are reversed.
- **B:** This is correct.
- **C:** Data loss is not RTO.
- **D:** Restore duration is not RPO.
- **Reusable rule:** RPO measures lost time of data; RTO measures time to restore.
- **Cost/operation:** More aggressive objectives usually require more replication and capacity.
- **Variation:** Measure actual recovery in game days rather than assuming targets are met.
- **Lessons:** 351–352
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-impact-analysis.html)

## B24-02 — Answer C

- **Central requirement:** The company wants the lowest-cost multi-Region DR strategy.
- **Decisive words:** many hours, lowest cost
- **Why the correct answer works:** Backup and restore offers the lowest ongoing cost when recovery objectives are relaxed.
- **A:** Active-active has the highest ongoing cost.
- **B:** Warm standby maintains a functional copy.
- **C:** This is correct.
- **D:** Hot standby keeps significant capacity.
- **Reusable rule:** Relaxed RTO and RPO plus cost priority points to backup and restore.
- **Cost/operation:** Backups, cross-Region copies, storage, and tests still cost.
- **Variation:** IaC and tested runbooks can reduce RTO without standby compute.
- **Lessons:** 351–352
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

## B24-03 — Answer A

- **Central requirement:** During failover, the team should primarily scale the environment.
- **Decisive words:** complete, reduced capacity, already accepts traffic, scale
- **Why the correct answer works:** Warm standby maintains a complete, functional, scaled-down environment.
- **A:** This is correct.
- **B:** Pilot light needs additional components turned on or deployed.
- **C:** Backup restore has no functional stack ready.
- **D:** Tape alone does not describe the running environment.
- **Reusable rule:** Functional but scaled-down copy is warm standby.
- **Cost/operation:** The always-running secondary stack creates ongoing cost.
- **Variation:** Active-active serves normal production traffic from multiple sites.
- **Lessons:** 351–352
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

## B24-04 — Answer C

- **Central requirement:** The primary goal is server disaster recovery.
- **Decisive words:** continuous server replication, staging, recovery
- **Why the correct answer works:** AWS DRS continuously replicates servers and orchestrates recovery from a staging area.
- **A:** DMS moves database data.
- **B:** MGN focuses on migration to AWS.
- **C:** This is correct.
- **D:** BI is unrelated.
- **Reusable rule:** Continuous server DR points to AWS Elastic Disaster Recovery.
- **Cost/operation:** Staging storage, replication, tests, and launched recovery resources can charge.
- **Variation:** Test recovery regularly without disrupting replication.
- **Lessons:** 352
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)

## B24-05 — Answer A

- **Central requirement:** The project is a server migration rather than an ongoing DR program.
- **Decisive words:** lift and shift, servers, EC2, cutover
- **Why the correct answer works:** AWS MGN is designed for lift-and-shift server migration to AWS.
- **A:** This is correct.
- **B:** Backup does not orchestrate lift-and-shift cutover.
- **C:** Macie classifies S3 data.
- **D:** WAF filters HTTP.
- **Reusable rule:** Server migration to EC2 points to MGN; ongoing server DR points to DRS.
- **Cost/operation:** Replication, staging, test, and cutover resources can charge.
- **Variation:** Use launch settings and testing before cutover.
- **Lessons:** 359
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)

## B24-06 — Answer C

- **Central requirement:** The team wants an initial copy followed by ongoing changes until a short cutover.
- **Decisive words:** initial copy, ongoing changes, short cutover
- **Why the correct answer works:** Full load copies the initial data, and CDC applies ongoing source changes.
- **A:** CDC alone lacks the requested initial load in this design.
- **B:** Full load alone misses later writes.
- **C:** This is correct.
- **D:** MGN migrates servers rather than logical database changes.
- **Reusable rule:** Initial state plus continuing writes maps to DMS full load and CDC.
- **Cost/operation:** Replication capacity, logs, transfer, and endpoints can charge.
- **Variation:** Changing engines also requires schema and code assessment.
- **Lessons:** 353–355
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html)

## B24-07 — Answer A

- **Central requirement:** The service must govern backups rather than migrate servers.
- **Decisive words:** backup schedules, retention, vaults, cross-account
- **Why the correct answer works:** AWS Backup centrally manages plans, vaults, retention, and copies for supported resources.
- **A:** This is correct.
- **B:** DMS migrates and replicates data stores.
- **C:** Direct Connect is networking.
- **D:** EventBridge alone is not the backup service.
- **Reusable rule:** Central backup governance points to AWS Backup.
- **Cost/operation:** Recovery points can persist and continue charging after original resources are removed.
- **Variation:** A completed backup must still be restore-tested.
- **Lessons:** 357–358
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

## B24-08 — Answer B

- **Central requirement:** The scenario explicitly describes an existing customer that remains eligible to order Snowball Edge within the final support window.
- **Decisive words:** existing customer, before December 31, 2026, petabytes, physical appliance
- **Why the correct answer works:** For this narrowly qualified legacy scenario, Snowball Edge still supports physical, large-scale data transfer while the existing customer's service remains supported.
- **A:** CloudFront distributes content.
- **B:** This is correct.
- **C:** WAF is web filtering.
- **D:** Identity Center is workforce access.
- **Reusable rule:** Treat Snowball Edge as a historical exam pattern, not a default for a new design in 2026.
- **Cost/operation:** Include device jobs, shipping, target storage, transfer, encryption, and the final delta synchronization.
- **Variation:** Snowball Edge is unavailable to new customers since November 7, 2025, and AWS has announced end of support in commercial Regions after December 31, 2026. For a new design, evaluate DataSync or Direct Connect online, and Data Transfer Terminal eligibility or an AWS Partner solution offline.
- **Lessons:** 360
- **Official reference:** [Snowball Edge availability change](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html), [Snowball end-of-support notice](https://aws.amazon.com/snowball/), and [AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html)

## B24-09 — Answer A

- **Central requirement:** The company wants to reduce NAT data processing cost while keeping S3 access private.
- **Decisive words:** S3, NAT processing cost, private
- **Why the correct answer works:** An S3 gateway endpoint routes S3 traffic privately without sending it through the NAT Gateway.
- **A:** This is correct.
- **B:** Public IPv4 does not reduce NAT processing safely.
- **C:** Cross-Region NAT adds complexity and cost.
- **D:** CloudHSM is unrelated.
- **Reusable rule:** S3 or DynamoDB traffic through NAT is a clue for a gateway endpoint.
- **Cost/operation:** Gateway endpoints have no hourly endpoint charge, though normal service and transfer pricing applies.
- **Variation:** Interface endpoints have hourly and data charges.
- **Lessons:** 349 plus 333–334
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html)

## B24-10 — Answer C

- **Central requirement:** The company needs resilient scaling across Availability Zones.
- **Decisive words:** stateless web tier, multiple AZs, resilient scaling
- **Why the correct answer works:** An ALB and multi-AZ Auto Scaling group remove the single instance and AZ dependency; external state allows replacement.
- **A:** A larger instance remains a single point of failure.
- **B:** Cluster placement stays in one AZ and targets network performance.
- **C:** This is correct.
- **D:** NAT does not provide application HA.
- **Reusable rule:** EC2 web HA points to load balancing, Auto Scaling across AZs, and external state.
- **Cost/operation:** Multi-AZ capacity costs more but is required by the resilience objective.
- **Variation:** CloudFront can add edge caching but does not replace origin HA.
- **Lessons:** 362–366
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html)
