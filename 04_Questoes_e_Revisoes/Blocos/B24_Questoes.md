# B24 — Questões: Custos de rede, disaster recovery, migração e arquiteturas integradas

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione uma resposta<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B24_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B24-01 | 2.2 | RTO and RPO | Situacional | Basic | Inglês |
| B24-02 | 2.2 | Backup and restore | Situacional | Intermediate | Inglês |
| B24-03 | 2.2 | Warm standby | Situacional | Intermediate | Inglês |
| B24-04 | 2.2 | Elastic Disaster Recovery | Situacional | Basic | Inglês |
| B24-05 | 3.5 | Application Migration Service | Situacional | Basic | Inglês |
| B24-06 | 3.5 | DMS full load and CDC | Situacional | Intermediate | Inglês |
| B24-07 | 2.2 | AWS Backup | Situacional | Intermediate | Inglês |
| B24-08 | 3.5 | Large data transfer | Situacional | Intermediate | Inglês |
| B24-09 | 4.4 | Network cost optimization | Situacional | Intermediate | Inglês |
| B24-10 | 2.2 | EC2 high availability | Situacional | Advanced | Inglês |

## Questões

### B24-01

**Context:** A business can tolerate four hours of data loss and must restore service within eight hours after a disaster.

**Requirement:** The architect must translate the two limits correctly.

**Question:** Which statement is correct?

- A. RTO is four hours and RPO is eight hours.
- B. RPO is four hours and RTO is eight hours.
- C. Both values are RTO.
- D. Both values are RPO.

**Before moving on:** record decisive words and confidence.

### B24-02

**Context:** A noncritical application accepts an RTO of many hours and an RPO of several hours.

**Requirement:** The company wants the lowest-cost multi-Region DR strategy.

**Question:** Which strategy is most appropriate?

- A. Multi-site active-active.
- B. Warm standby.
- C. Backup and restore with tested infrastructure automation.
- D. Full-size hot standby.

**Before moving on:** record decisive words and confidence.

### B24-03

**Context:** A recovery Region must already run a complete version of an application at reduced capacity and accept a small amount of traffic.

**Requirement:** During failover, the team should primarily scale the environment.

**Question:** Which DR strategy is described?

- A. Warm standby.
- B. Pilot light.
- C. Backup and restore.
- D. Tape archive only.

**Before moving on:** record decisive words and confidence.

### B24-04

**Context:** A company needs continuous block-level replication of servers to a low-cost staging area and orchestrated recovery instances.

**Requirement:** The primary goal is server disaster recovery.

**Question:** Which service should be used?

- A. AWS Database Migration Service.
- B. AWS Application Migration Service only for one-time cutover.
- C. AWS Elastic Disaster Recovery.
- D. Amazon Quick Sight.

**Before moving on:** record decisive words and confidence.

### B24-05

**Context:** A company wants to lift and shift physical and virtual servers into Amazon EC2 with continuous replication before cutover.

**Requirement:** The project is a server migration rather than an ongoing DR program.

**Question:** Which service is the best fit?

- A. AWS Application Migration Service.
- B. AWS Backup.
- C. Amazon Macie.
- D. AWS WAF.

**Before moving on:** record decisive words and confidence.

### B24-06

**Context:** A database must move to AWS while the source continues processing transactions.

**Requirement:** The team wants an initial copy followed by ongoing changes until a short cutover.

**Question:** Which AWS DMS migration mode should be used?

- A. CDC only with no initial state.
- B. Full load only and ignore later writes.
- C. Full load plus change data capture.
- D. AWS MGN block replication.

**Before moving on:** record decisive words and confidence.

### B24-07

**Context:** A company needs centrally managed backup schedules, retention, vaults, and cross-account copies for supported resources.

**Requirement:** The service must govern backups rather than migrate servers.

**Question:** Which service should be selected?

- A. AWS Backup.
- B. AWS DMS.
- C. AWS Direct Connect.
- D. Amazon EventBridge only.

**Before moving on:** record decisive words and confidence.

### B24-08

**Context:** An existing AWS Snowball Edge customer must move petabytes to AWS before commercial support ends on December 31, 2026, but its network cannot finish the transfer within the deadline.

**Requirement:** The account is still eligible to order the rugged AWS physical appliance during the remaining support window.

**Question:** Which service fits this explicitly qualified legacy scenario?

- A. Amazon CloudFront.
- B. AWS Snowball Edge.
- C. AWS WAF.
- D. AWS IAM Identity Center.

**Before moving on:** record decisive words and confidence.

### B24-09

**Context:** Private instances send large amounts of data to Amazon S3 through a NAT Gateway.

**Requirement:** The company wants to reduce NAT data processing cost while keeping S3 access private.

**Question:** What should the company do?

- A. Create an S3 gateway endpoint and update the private route tables.
- B. Add more public IPv4 addresses.
- C. Send traffic through a second NAT Gateway in another Region.
- D. Create a CloudHSM cluster.

**Before moving on:** record decisive words and confidence.

### B24-10

**Context:** A stateless web tier runs on one EC2 instance in one Availability Zone and stores sessions on the instance.

**Requirement:** The company needs resilient scaling across Availability Zones.

**Question:** Which redesign best meets the requirement?

- A. Use a larger single instance and a static Elastic IP.
- B. Place instances in a cluster placement group in one AZ.
- C. Deploy an ALB and Auto Scaling group across multiple AZs and externalize session state.
- D. Create a single NAT instance.

**Before moving on:** record decisive words and confidence.

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
