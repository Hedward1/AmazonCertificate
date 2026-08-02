# B24 — Questões: Custos de rede, disaster recovery, migração e arquiteturas integradas

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione a quantidade indicada em cada questão<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B24_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B24-01 | 2.2 | RTO and RPO | single | fundamental | básica | Inglês |
| B24-02 | 2.2 | Backup and restore | single | situacional | intermediária | Inglês |
| B24-03 | 2.2 | Warm standby | single | situacional | intermediária | Inglês |
| B24-04 | 2.2 | Elastic Disaster Recovery | multi-2 | situacional | avançada | Inglês |
| B24-05 | 3.5 | Application Migration Service | single | situacional | intermediária | Inglês |
| B24-06 | 3.5 | DMS full load and CDC | single | integrada | avançada | Inglês |
| B24-07 | 2.2 | AWS Backup | single | integrada | avançada | Inglês |
| B24-08 | 3.5 | Large data transfer | single | integrada | avançada | Inglês |
| B24-09 | 4.4 | Network cost optimization | multi-3 | integrada | avançada | Inglês |
| B24-10 | 2.2 | EC2 high availability | single | integrada | avançada | Inglês |

## Questões

### B24-01

**Context:** A business can tolerate four hours of data loss and must restore service within eight hours after a disaster.

**Requirement:** The architect must translate the two limits correctly.

**Question:** Which statement is correct?

- A. RTO is four hours and RPO is eight hours.
- B. RPO is four hours and RTO is eight hours.
- C. Both values are RTO.
- D. Both values are RPO.

### B24-02

**Context:** A noncritical application accepts an RTO of many hours and an RPO of several hours.

**Requirement:** The company wants the lowest-cost multi-Region DR strategy.

**Question:** Which strategy is most appropriate?

- A. Multi-site active-active.
- B. Warm standby.
- C. Backup and restore with tested infrastructure automation.
- D. Full-size hot standby.

### B24-03

**Context:** A recovery Region must already run a complete version of an application at reduced capacity and accept a small amount of traffic.

**Requirement:** During failover, the team should primarily scale the environment.

**Question:** Which DR strategy is described?

- A. Warm standby.
- B. Pilot light.
- C. Backup and restore.
- D. Tape archive only.

### B24-04

**Context:** A company needs continuous block-level replication of servers to a low-cost staging area, orchestrated recovery instances, and non-disruptive recovery drills with point-in-time selection.

**Requirement:** Implement ongoing server disaster recovery rather than a one-time migration. **Choose TWO.**

- A. Use AWS Elastic Disaster Recovery for continuous replication and recovery orchestration.
- B. Use AWS Database Migration Service as the operating-system block replicator.
- C. Regularly launch drill instances through the service and validate recovery without affecting the source.
- D. Use AWS Application Migration Service only and treat cutover as the recurring DR test mechanism.
- E. Use Amazon Quick Sight to create recovery instances.

### B24-05

**Context:** A company wants to lift and shift physical and virtual servers into Amazon EC2 with continuous replication before cutover.

**Requirement:** The project is a server migration rather than an ongoing DR program.

**Question:** Which service is the best fit?

- A. AWS Application Migration Service.
- B. AWS Backup.
- C. Amazon Macie.
- D. AWS WAF.

### B24-06

**Context:** A self-managed commercial database must move to an AWS-managed
open-source engine. The source will continue taking writes for several days;
the team needs an initial copy, continuous delta replication, schema/code
assessment for the heterogeneous change, validation, and a short final cutover.

**Requirement:** Separate schema conversion work from low-downtime data
replication.

**Question:** Which migration plan best meets the requirement?

- A. Start CDC with no baseline copy or schema preparation, then create missing tables during cutover.
- B. Run a one-time full load, ignore later source writes, and use DNS TTL as the reconciliation mechanism.
- C. Assess/convert the heterogeneous schema as required, then use AWS DMS full load plus CDC, monitor validation/lag, quiesce writes, and cut over after the delta closes.
- D. Use AWS Application Migration Service block replication as logical row-level database conversion.

### B24-07

**Context:** An organization needs centrally governed backup schedules and
retention for supported resources in many accounts. Recovery points must be
copied to a security account, protected against premature deletion, and
periodically restore-tested. The design is for recoverability, not server
migration.

**Requirement:** Minimize account-by-account scheduling code while separating
backup policy, vault protection, copies, and restore verification.

**Question:** Which service should anchor the design?

- A. AWS Backup with organization backup policies/plans, cross-account copies
  to vaults in the security account, AWS Backup Vault Lock in compliance mode
  on the destination vaults with a reviewed cooling-off period, and scheduled
  restore testing for supported resources.
- B. Use EventBridge and Lambda in every account to schedule native snapshots, then maintain custom retention, copy, immutability, inventory, and restore-test code.
- C. Use Amazon Data Lifecycle Manager for every resource type and assume its narrower snapshot/AMI scope supplies organization-wide cross-service backup governance.
- D. Use AWS Backup plans in each workload account but keep every recovery point and KMS dependency inside the same account, with no protected cross-account copy or restore testing.

### B24-08

**Context:** An existing Snowball Edge customer remains eligible to order a
device and must seed petabytes into S3 before commercial support ends on
December 31, 2026. Its WAN cannot finish the baseline in time, but a smaller
delta must continue during shipping and be synchronized before cutover.

**Requirement:** Use the still-supported physical path only for this qualified
legacy baseline and include an online delta/cutover plan rather than treating
the appliance as continuous replication.

**Question:** Which plan fits?

- A. Use Direct Connect and DataSync for the entire baseline, despite the stated WAN/deadline constraint, and skip offline transfer.
- B. Order Snowball Edge while the existing account remains eligible, import the baseline, use an appropriate online synchronization method such as DataSync for the changing delta, validate, and cut over before the support deadline.
- C. Use Data Transfer Terminal without confirming Enterprise eligibility or a usable location, and assume AWS supplies/ships the customer's transfer equipment like Snowball.
- D. Ship only the Snowball Edge baseline and freeze no writes, run no online delta synchronization, and cut over without validating the imported target.

### B24-09

**Context:** Private instances in three Availability Zones send high-volume S3 traffic through one NAT Gateway, and customers download large static objects directly from the regional origin.

**Requirement:** Reduce NAT processing, avoid cross-AZ NAT dependency, and reduce repeated origin transfer while preserving resilience. **Select THREE.**

- A. Assign public IPv4 addresses to all private instances.
- B. Create an S3 gateway endpoint and associate it with the private route tables.
- C. Route every AZ through a single NAT Gateway in another AZ to consolidate hourly charges.
- D. Serve cacheable static objects through Amazon CloudFront.
- E. Replace S3 with EBS volumes attached to the web fleet.
- F. For remaining internet-bound traffic, deploy NAT Gateways per AZ and route each subnet to its same-AZ NAT Gateway.

### B24-10

**Context:** A stateless web tier runs on one EC2 instance in one Availability Zone and stores sessions on the instance.

**Requirement:** The company needs resilient scaling across Availability Zones.

**Question:** Which redesign best meets the requirement?

- A. Use a larger single instance and a static Elastic IP.
- B. Place instances in a cluster placement group in one AZ.
- C. Deploy an ALB and Auto Scaling group across multiple AZs and externalize session state.
- D. Create a single NAT instance.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B24-01 |  |  |  |
| B24-02 |  |  |  |
| B24-03 |  |  |  |
| B24-04 |  |  |  |
| B24-05 |  |  |  |
| B24-06 |  |  |  |
| B24-07 |  |  |  |
| B24-08 |  |  |  |
| B24-09 |  |  |  |
| B24-10 |  |  |  |
