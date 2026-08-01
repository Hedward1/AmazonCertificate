# B24 — Gabarito comentado

Volte às [questões B24](B24_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B24-01 | B | 2.2 |
| B24-02 | C | 2.2 |
| B24-03 | A | 2.2 |
| B24-04 | A,C | 2.2 |
| B24-05 | A | 3.5 |
| B24-06 | C | 3.5 |
| B24-07 | A | 2.2 |
| B24-08 | B | 3.5 |
| B24-09 | B,D,F | 4.4 |
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

## B24-04 — Answer A,C

- **Central requirement:** continuously replicate whole servers and validate orchestrated DR without disrupting production.
- **Decisive words:** *block-level replication*, *staging area*, *point in time*, *non-disruptive drills*.
- **A:** correct; Elastic Disaster Recovery supplies ongoing block replication and recovery orchestration.
- **B:** incorrect; DMS migrates database data and changes, not complete server disks and boot recovery.
- **C:** correct; DRS drill launches validate recovery while source workloads and replication continue.
- **D:** incorrect; Application Migration Service is optimized for migration/cutover, not the ongoing DR requirement.
- **E:** incorrect; Quick Sight is BI and cannot launch recovery instances.
- **Reusable rule:** MGN is server migration; DRS is continuous server disaster recovery with drills and failover.
- **Lessons:** 352.
- **Official reference:** [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html).

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

- **Central requirement:** convert a heterogeneous schema and keep data synchronized through a controlled low-downtime cutover.
- **Decisive words:** different engine, source keeps writing, initial copy, delta, validation
- **Why the correct answer works:** schema assessment/conversion addresses engine differences, while DMS full load plus CDC establishes the baseline and applies ongoing changes until cutover.
- **A:** CDC without a consistent initial state and prepared target schema leaves missing historical data and objects.
- **B:** full load alone loses all changes written after the copy begins; DNS does not reconcile data.
- **C:** correct; it includes conversion, baseline, ongoing replication, lag/validation evidence, and an explicit quiesce/cutover step.
- **D:** MGN performs server block-level replication and does not convert database schema or provide logical table CDC for this heterogeneous migration.
- **Reusable rule:** heterogeneous database migration separates schema/code conversion from DMS data movement; low downtime generally requires full load plus CDC and measured cutover readiness.
- **Cost/operation:** Replication capacity, logs, transfer, and endpoints can charge.
- **Variation:** Engine-native tools may be preferable for some homogeneous migrations; always validate supported types, LOB behavior, and source logging prerequisites.
- **Lessons:** 353–355
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html)

## B24-07 — Answer A

- **Central requirement:** enforce organization-scale backup policy, copy
  recovery points across accounts, make destination retention immutable after a
  reviewed cooling-off period with AWS Backup Vault Lock in compliance mode,
  and prove restorability without custom schedulers in every account.
- **Decisive words:** many accounts, cross-account copy, compliance mode,
  premature deletion, restore-tested
- **Why the correct answer works:** AWS Backup centralizes plans and organization
  policies, cross-account copies isolate recovery points in the security
  account, Vault Lock compliance mode makes the lock immutable after its
  cooling-off period, and restore testing provides recovery evidence for
  supported resources.
- **A:** correct; it combines centralized backup governance, cross-account
  isolation, explicit compliance-mode Vault Lock protection, and scheduled
  restore verification.
- **B:** custom snapshot automation can work, but recreating policy, inventory, lifecycle, copies, immutability, and restore testing across accounts adds substantial operations.
- **C:** Data Lifecycle Manager is useful for supported EBS snapshot/EBS-backed AMI lifecycles, but it is not the broad cross-service backup-governance layer requested.
- **D:** local AWS Backup plans cover part of the problem, but co-located recovery points and absent restore tests fail the isolation and evidence requirements.
- **Reusable rule:** AWS Backup governs supported backup lifecycles;
  cross-account copies reduce account blast radius, Vault Lock compliance mode
  becomes immutable after its cooling-off period, and restore tests validate
  recoverability.
- **Cost/operation:** Recovery points can persist and continue charging after original resources are removed.
- **Variation:** Use governance mode only when authorized administrators must
  retain the ability to remove the lock. It does not meet a requirement for an
  immutable lock after the cooling-off period; verify service/Region support,
  destination KMS permissions, retention ranges, and cross-account copy behavior.
- **Lessons:** 357–358
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

## B24-08 — Answer B

- **Central requirement:** complete a qualified legacy offline baseline before end of support while synchronizing and validating the changing delta online.
- **Decisive words:** existing eligible customer, petabyte baseline, support deadline, delta, cutover
- **Why the correct answer works:** Snowball Edge can serve the physical baseline only for the explicitly eligible existing customer; DataSync or another supported online method handles later changes and cutover validation.
- **A:** Direct Connect plus DataSync can be a strong online design, but the scenario explicitly states that the available network path cannot complete the baseline by the deadline.
- **B:** correct; it respects the time-limited eligibility, assigns physical and online tools to distinct phases, and avoids pretending shipping provides continuous replication.
- **C:** Data Transfer Terminal is a current physical-site option for eligible Enterprise customers using their own supported equipment, but those prerequisites are absent and it is not a shipped AWS appliance.
- **D:** physical baseline-only transfer leaves all writes during shipping unsynchronized and provides no evidence for a safe short cutover.
- **Reusable rule:** offline seeding still needs discovery, encryption/chain-of-custody, target validation, and a delta/cutover path; in 2026, Snowball Edge is a legacy exception rather than a new-customer default.
- **Cost/operation:** Include device jobs, shipping, target storage, transfer, encryption, and the final delta synchronization.
- **Variation:** Snowball Edge is unavailable to new customers since November 7, 2025, and AWS has announced end of support in commercial Regions after December 31, 2026. For a new design, evaluate DataSync or Direct Connect online, and Data Transfer Terminal eligibility or an AWS Partner solution offline.
- **Lessons:** 360
- **Official reference:** [Snowball Edge availability change](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html), [Snowball end-of-support notice](https://aws.amazon.com/snowball/), and [AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html)

## B24-09 — Answer B,D,F

- **Central requirement:** reduce S3 NAT processing, cross-AZ NAT dependency, and repeated origin transfer without sacrificing multi-AZ design.
- **Decisive words:** *high-volume S3*, *one NAT across AZs*, *large static downloads*, *preserving resilience*.
- **A:** incorrect; public IPv4 addresses increase exposure and do not optimize the private S3 path.
- **B:** correct; an S3 gateway endpoint removes supported S3 traffic from the NAT path without an hourly endpoint charge.
- **C:** incorrect; centralizing all AZ routes adds cross-AZ transfer and a zonal dependency.
- **D:** correct; CloudFront caches objects near users and reduces repeat origin traffic.
- **E:** incorrect; EBS is not a scalable regional object-download replacement.
- **F:** correct; same-AZ NAT routing removes cross-AZ NAT dependency and transfer for remaining internet egress, justified here by high volume and resilience.
- **Reusable rule:** optimize network cost by changing the path: endpoints for AWS services, caching for repeated delivery, and zonally aligned egress.
- **Lessons:** 349 plus 333–334.
- **Official reference:** [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html) and [NAT Gateway architecture](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html).

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
