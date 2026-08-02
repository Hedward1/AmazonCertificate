# SIM-B — Commented answer key

**Navigation:** [Questions](Questoes.md) | [Commented answer key](Gabarito.md) | [Result report](Relatorio.md)

Open this file only after completing the timed attempt.

## Quick answer table

| ID | Answer | Domain | Task |
|---|---|---:|---:|
| SIM-B-01 | C | 1 | 1.1 |
| SIM-B-02 | A | 1 | 1.1 |
| SIM-B-03 | C | 1 | 1.1 |
| SIM-B-04 | A,B | 1 | 1.1 |
| SIM-B-05 | A | 1 | 1.1 |
| SIM-B-06 | B | 1 | 1.1 |
| SIM-B-07 | D | 1 | 1.1 |
| SIM-B-08 | C,D | 1 | 1.2 |
| SIM-B-09 | B | 1 | 1.2 |
| SIM-B-10 | C | 1 | 1.2 |
| SIM-B-11 | D | 1 | 1.2 |
| SIM-B-12 | A,E | 1 | 1.2 |
| SIM-B-13 | B | 1 | 1.2 |
| SIM-B-14 | D | 1 | 1.2 |
| SIM-B-15 | B | 1 | 1.3 |
| SIM-B-16 | B,C | 1 | 1.3 |
| SIM-B-17 | A | 1 | 1.3 |
| SIM-B-18 | A | 1 | 1.3 |
| SIM-B-19 | B | 1 | 1.3 |
| SIM-B-20 | D,E | 1 | 1.3 |
| SIM-B-21 | C | 2 | 2.1 |
| SIM-B-22 | B | 2 | 2.1 |
| SIM-B-23 | A | 2 | 2.1 |
| SIM-B-24 | A,C | 2 | 2.1 |
| SIM-B-25 | D | 2 | 2.1 |
| SIM-B-26 | B | 2 | 2.1 |
| SIM-B-27 | A | 2 | 2.1 |
| SIM-B-28 | B,D | 2 | 2.1 |
| SIM-B-29 | C | 2 | 2.1 |
| SIM-B-30 | D | 2 | 2.2 |
| SIM-B-31 | A | 2 | 2.2 |
| SIM-B-32 | C,E | 2 | 2.2 |
| SIM-B-33 | C | 2 | 2.2 |
| SIM-B-34 | A | 2 | 2.2 |
| SIM-B-35 | D | 2 | 2.2 |
| SIM-B-36 | A,D | 2 | 2.2 |
| SIM-B-37 | C | 2 | 2.2 |
| SIM-B-38 | B | 3 | 3.1 |
| SIM-B-39 | D | 3 | 3.1 |
| SIM-B-40 | B,E | 3 | 3.1 |
| SIM-B-41 | A | 3 | 3.2 |
| SIM-B-42 | B | 3 | 3.2 |
| SIM-B-43 | A | 3 | 3.2 |
| SIM-B-44 | A,B | 3 | 3.3 |
| SIM-B-45 | C | 3 | 3.3 |
| SIM-B-46 | A | 3 | 3.3 |
| SIM-B-47 | D | 3 | 3.4 |
| SIM-B-48 | C,D | 3 | 3.4 |
| SIM-B-49 | C | 3 | 3.4 |
| SIM-B-50 | D | 3 | 3.5 |
| SIM-B-51 | C | 3 | 3.5 |
| SIM-B-52 | A,B,C | 3 | 3.5 |
| SIM-B-53 | B | 4 | 4.1 |
| SIM-B-54 | D | 4 | 4.1 |
| SIM-B-55 | C | 4 | 4.1 |
| SIM-B-56 | A,D,F | 4 | 4.1 |
| SIM-B-57 | D | 4 | 4.2 |
| SIM-B-58 | B | 4 | 4.2 |
| SIM-B-59 | A | 4 | 4.2 |
| SIM-B-60 | B,C,E | 4 | 4.3 |
| SIM-B-61 | C | 4 | 4.3 |
| SIM-B-62 | B | 4 | 4.3 |
| SIM-B-63 | D | 4 | 4.4 |
| SIM-B-64 | D,E,F | 4 | 4.4 |
| SIM-B-65 | A | 4 | 4.4 |

## SIM-B-01 — Answer C

- **Central requirement:** Centralized federated workforce access across multiple AWS accounts.
- **Decisive words:** corporate identity provider, several accounts, short-lived credentials
- **A:** Duplicated IAM users create long-term credentials and significant lifecycle overhead across accounts.
- **B:** Secrets Manager can protect application secrets, but shared administrator keys are not an appropriate workforce identity model.
- **C:** IAM Identity Center provides centralized workforce access, federation, and account-specific permission sets with temporary credentials.
- **D:** Cognito user pools authenticate application users; they do not provide workforce account assignments or reusable permission sets for administering multiple AWS accounts.
- **Reusable rule:** Use IAM Identity Center and permission sets for centrally managed workforce access to multiple AWS accounts.
- **Official reference:** [AWS](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

## SIM-B-02 — Answer A

- **Central requirement:** Secure third-party cross-account access without long-lived credentials or confused deputy exposure.
- **Decisive words:** consulting company, temporary credentials, confused deputy
- **A:** A cross-account role supplies temporary credentials, and a customer-specific external ID mitigates the confused deputy risk.
- **B:** Root access keys are long-lived, excessively privileged, and must not be distributed to an external party.
- **C:** Independent customer accounts cannot be placed into multiple unrelated organizations, and OU membership is not a third-party authorization mechanism.
- **D:** AWS RAM does not replace role-based authorization for a third party reading CloudWatch metrics.
- **Reusable rule:** For third-party role assumption, use a cross-account role and a unique external ID supplied by the customer.
- **Official reference:** [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html)

## SIM-B-03 — Answer C

- **Central requirement:** Directory-driven, least-privilege workforce authorization across many accounts and environments.
- **Decisive words:** external SAML, reusable job functions, automatic removal
- **A:** Local users duplicate identities and require manual deprovisioning, which conflicts with directory-driven lifecycle management.
- **B:** A shared credential removes individual accountability and makes least-privilege separation between environments impractical.
- **C:** Identity Center maps federated groups to reusable permission sets and account assignments, enabling centralized deprovisioning and environment separation.
- **D:** Cognito identity pools are intended for application identities; separate pools do not provide centralized multi-account workforce lifecycle and permission-set governance.
- **Reusable rule:** Map external directory groups to IAM Identity Center permission sets and scope account assignments by job function and environment.
- **Official reference:** [AWS](https://docs.aws.amazon.com/singlesignon/latest/userguide/external-idps.html)

## SIM-B-04 — Answer A,B

- **Central requirement:** Managed, federated remote access with group-specific network authorization.
- **Decisive words:** individual engineers, SAML, different groups, no VPN appliances
- **A:** Client VPN is the managed, client-based remote-access service and supports SAML federated authentication.
- **B:** A reachable destination needs both a route and an explicit authorization rule; authentication alone does not grant network access.
- **C:** Site-to-Site VPN connects networks through IPsec and is not provisioned separately for each roaming laptop.
- **D:** An internet gateway would not provide user authentication and would unnecessarily expose routing for private application subnets.
- **E:** Direct Connect is dedicated site connectivity and is not a per-user remote-access mechanism.
- **Reusable rule:** Client VPN designs require an authenticated endpoint plus routes and explicit authorization rules for every allowed destination.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html), [AWS](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html)

## SIM-B-05 — Answer A

- **Central requirement:** Enforce a preventive organization guardrail without treating the guardrail as a permission grant.
- **Decisive words:** organization-wide, even administrators, still receive permissions
- **A:** An explicit deny SCP limits the maximum permissions in member accounts, while IAM roles still grant the actions users can perform.
- **B:** SCPs do not grant permissions, so removing IAM policies would leave principals without the required application permissions.
- **C:** Permissions boundaries apply to IAM principals, not to the root user as an organization-wide account guardrail.
- **D:** AWS RAM shares supported resources and does not enforce an organization-wide deny on CloudTrail API operations.
- **Reusable rule:** SCPs set the permission ceiling for member accounts; IAM identity or resource policies must still grant allowed actions.
- **Official reference:** [AWS](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

## SIM-B-06 — Answer B

- **Central requirement:** Temporary AWS credentials for an EC2 workload without embedded access keys.
- **Decisive words:** EC2 application, prohibits long-term keys, automatically rotated
- **A:** User data can be retrieved from the instance and would expose long-term credentials that require manual rotation.
- **B:** An instance profile delivers temporary role credentials to EC2 and the platform rotates them automatically.
- **C:** Root credentials must not be used by an application, even when the storage volume is encrypted.
- **D:** Cognito user pools authenticate application users; mapping local users would not provide an EC2 workload role or automatically rotated credentials.
- **Reusable rule:** Assign an IAM role to an AWS compute service so workloads obtain temporary credentials instead of stored access keys.
- **Official reference:** [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

## SIM-B-07 — Answer D

- **Central requirement:** A recoverable but tightly protected break-glass identity for root-only account operations.
- **Decisive words:** break-glass, root-required tasks, minimize exposure
- **A:** Root access keys create a powerful long-term credential and are unnecessary for a console break-glass process.
- **B:** The account root user cannot simply be deleted and remains necessary for a small set of account tasks.
- **C:** Routine root use expands exposure and weakens the individual accountability provided by federated roles.
- **D:** MFA, protected recovery factors, no root access keys, and rare use align with AWS root user security guidance.
- **Reusable rule:** Secure root credentials and recovery factors with MFA, create no root access keys, and use federated roles for routine work.
- **Official reference:** [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)

## SIM-B-08 — Answer C,D

- **Central requirement:** Organization-wide managed detection plus centralized correlation and prioritization of security findings.
- **Decisive words:** 70 accounts, managed threat detection, correlate multiple services
- **A:** Independent manual administration creates drift and does not provide the requested organization-level operating model.
- **B:** A self-managed log host neither enables GuardDuty detectors nor provides managed cross-service finding correlation.
- **C:** GuardDuty organization administration provides scalable, centrally governed threat detection across member accounts.
- **D:** Security Hub centrally correlates and prioritizes security findings and supports delegated multi-account administration.
- **E:** Artifact supplies AWS compliance reports and agreements; it is not a security finding aggregation service.
- **Reusable rule:** Use delegated administrators for organization-wide security services, and use Security Hub to centralize correlated findings.
- **Official reference:** [AWS](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html), [AWS](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html)

## SIM-B-09 — Answer B

- **Central requirement:** Inline Layer 7 filtering of malicious HTTP request patterns.
- **Decisive words:** SQL injection, cross-site scripting, inspect HTTP
- **A:** A network ACL filters IP protocols and ports but cannot understand or filter HTTP request content.
- **B:** AWS WAF inspects Layer 7 web requests and can block SQL injection and cross-site scripting patterns.
- **C:** GuardDuty detects suspicious activity; it does not serve inline as an HTTP request filter for an ALB.
- **D:** Shield mitigates distributed denial-of-service attacks and does not define SQL injection inspection rules.
- **Reusable rule:** Use AWS WAF on a supported web entry point when the threat is expressed in HTTP headers, paths, or bodies.
- **Official reference:** [AWS](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)

## SIM-B-10 — Answer C

- **Central requirement:** Private, audited administration and patch management without internet traversal or a bastion.
- **Decisive words:** private subnets, no NAT, audited shell, least overhead
- **A:** A bastion adds patching, key management, public exposure, and inbound administration that the requirement seeks to avoid.
- **B:** An internet gateway route changes exposure but does not provide audited managed sessions or Systems Manager connectivity by itself.
- **C:** Session Manager and Patch Manager can operate through private interface endpoints when the agent, IAM role, and endpoint access are configured.
- **D:** A VPN can provide a network path, but it does not make a server a Systems Manager managed node or enable Patch Manager.
- **Reusable rule:** For private Systems Manager access, combine managed-node prerequisites with interface VPC endpoints instead of opening inbound administration.
- **Official reference:** [AWS](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-privatelink.html)

## SIM-B-11 — Answer D

- **Central requirement:** Stateful tier-to-tier filtering based on workload group membership rather than IP addresses.
- **Decisive words:** stateful, application tier, reference control
- **A:** Internet gateways provide connectivity and do not contain workload-level allow rules.
- **B:** Network ACLs are stateless subnet controls and cannot reference a security group or another network ACL.
- **C:** Route tables select network paths and cannot use a security group as a route target.
- **D:** Security groups are stateful and can reference another security group as the source of permitted traffic.
- **Reusable rule:** Use security group references for stateful access between workload tiers that belong to known security groups.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)

## SIM-B-12 — Answer A,E

- **Central requirement:** Workload-specific authorization and managed rotation for an EKS application secret.
- **Decisive words:** one service account, managed rotation, not image or ConfigMap
- **A:** A workload-specific role limits AWS API permissions to pods using the intended Kubernetes service account.
- **B:** A wildcard node role allows unrelated pods on the nodes to inherit excessive secret access.
- **C:** A plaintext ConfigMap does not provide the requested managed rotation and exposes the value through deployment configuration.
- **D:** Image-embedded credentials are long-lived, broadly exposed, and cannot be safely rotated without rebuilding the image.
- **E:** Secrets Manager provides controlled retrieval and managed rotation without embedding the password in deployment artifacts.
- **Reusable rule:** Give each Kubernetes workload its own AWS role and retrieve rotating secrets from Secrets Manager at runtime.
- **Official reference:** [AWS](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html), [AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_csi_driver.html)

## SIM-B-13 — Answer B

- **Central requirement:** Centralized stateful inspection with symmetric routing for multi-VPC and hybrid transit traffic.
- **Decisive words:** dozens of spokes, Transit Gateway, stateful, same endpoints
- **A:** AWS WAF inspects supported HTTP entry points and cannot be attached to Transit Gateway as a packet firewall.
- **B:** A centralized inspection VPC with Network Firewall and symmetric Transit Gateway routing supports stateful inspection across many attachments.
- **C:** GuardDuty is a detection service and does not become an inline transit packet filter.
- **D:** Network ACLs are attached to subnets, remain stateless, and are not a centralized Transit Gateway inspection plane.
- **Reusable rule:** Centralized stateful inspection requires an inspection VPC, an inline firewall, and symmetric routing through the same appliance path.
- **Official reference:** [AWS](https://docs.aws.amazon.com/network-firewall/latest/developerguide/architectures.html)

## SIM-B-14 — Answer D

- **Central requirement:** Enhanced managed DDoS response and cost protection beyond the standard baseline.
- **Decisive words:** DDoS Response Team, cost protection, revenue-critical
- **A:** Shield Standard is automatic baseline protection and does not provide the requested advanced response and cost-protection features.
- **B:** GuardDuty detects suspicious activity in AWS data sources but is not the enhanced managed DDoS protection subscription.
- **C:** Firewall Manager centralizes policies but, without Shield Advanced, does not supply enhanced detection, DDoS Response Team access, or cost protection.
- **D:** Shield Advanced adds enhanced detection, DDoS Response Team support, and eligible DDoS cost protection.
- **Reusable rule:** Choose Shield Advanced when the requirement explicitly includes enhanced DDoS response, visibility, or eligible cost protection.
- **Official reference:** [AWS](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)

## SIM-B-15 — Answer B

- **Central requirement:** Complete cross-account authorization for decrypting with a centrally owned KMS key.
- **Decisive words:** separate account, IAM allow exists, requests denied
- **A:** S3 object accessibility does not bypass KMS authorization and public access would violate the security requirement.
- **B:** Cross-account KMS use requires authorization in the key policy and an IAM permission for the external principal.
- **C:** An SCP sets a permissions boundary for accounts and cannot grant access that the KMS key policy omits.
- **D:** A KMS alias is only a friendly identifier and does not delegate cryptographic access to another account.
- **Reusable rule:** Cross-account KMS access normally needs both an owning-account key policy authorization and a consuming-principal IAM allow.
- **Official reference:** [AWS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html)

## SIM-B-16 — Answer B,C

- **Central requirement:** Enforce TLS in transit and customer managed KMS encryption at rest for S3.
- **Decisive words:** requires TLS, specified customer managed key, enforce
- **A:** S3 website endpoints do not support HTTPS and therefore cannot meet the mandatory TLS requirement.
- **B:** The aws:SecureTransport condition can explicitly deny bucket requests that do not use TLS.
- **C:** Default SSE-KMS applies the named KMS key to new objects, while a policy can reject noncompliant encryption choices.
- **D:** A public ACL expands data exposure and does not enforce transport or at-rest encryption.
- **E:** AWS physical security does not replace the customer's responsibility to configure logical encryption controls.
- **Reusable rule:** Use an explicit transport-policy deny for non-TLS requests and bucket encryption controls for the required at-rest key.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html), [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/specifying-kms-encryption.html)

## SIM-B-17 — Answer A

- **Central requirement:** Encrypted runtime retrieval and managed rotation of an RDS database credential.
- **Decisive words:** retrieved at runtime, IAM control, rotated automatically
- **A:** Secrets Manager stores encrypted secrets, controls retrieval with IAM, and supports managed rotation patterns for RDS credentials.
- **B:** A plaintext template parameter can expose the password and does not provide automatic secret rotation.
- **C:** User data is not an appropriate secret store and a permanent embedded password cannot meet managed rotation.
- **D:** Transfer Acceleration improves S3 transfer paths and has no role in rotating database credentials.
- **Reusable rule:** Use Secrets Manager when a secret lifecycle includes controlled retrieval and managed rotation, especially for supported databases.
- **Official reference:** [AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

## SIM-B-18 — Answer A

- **Central requirement:** Centralized, automated sensitive-data discovery in S3 across an AWS Organization.
- **Decisive words:** PII, hundreds of buckets, multiple accounts, no copying
- **A:** Macie discovers and classifies sensitive data in S3 and supports centralized multi-account administration through Organizations.
- **B:** Inspector evaluates supported workloads for vulnerabilities and does not classify the contents of S3 objects for PII.
- **C:** Artifact provides AWS compliance documents and agreements, not a customer S3 sensitive-data inventory.
- **D:** Detective investigates security activity and does not perform bulk object content classification or rewriting.
- **Reusable rule:** Use Macie for managed sensitive-data discovery in S3 and delegate administration for organization-wide coverage.
- **Official reference:** [AWS](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)

## SIM-B-19 — Answer B

- **Central requirement:** Immutable backup retention that administrators cannot weaken after a grace period.
- **Decisive words:** no user, cannot delete, immutable, grace period
- **A:** Budgets actions react to cost thresholds and do not make backup retention immutable.
- **B:** Vault Lock compliance mode enforces write-once-read-many controls that cannot be changed after the grace time expires.
- **C:** Immediate expiration contradicts the required retention and does not provide protected backup governance.
- **D:** Security groups do not govern AWS Backup deletion APIs or retention settings.
- **Reusable rule:** Use AWS Backup Vault Lock compliance mode when retention must remain immutable even from account administrators.
- **Official reference:** [AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html)

## SIM-B-20 — Answer D,E

- **Central requirement:** Encrypt a hybrid DataSync migration both in transit and at rest with the approved KMS key.
- **Decisive words:** DataSync, confidential, crosses network, customer managed KMS
- **A:** Publicly exposing NFS creates an unnecessary attack path and does not satisfy encrypted transport.
- **B:** Encryption at rest does not make public object access acceptable or satisfy least privilege.
- **C:** Broad KMS permissions increase risk, and disabling rotation is unrelated to enabling the required transfer encryption.
- **D:** DataSync encrypts data in transit between its agent, service, and supported AWS storage destinations.
- **E:** SSE-KMS with the approved key provides the required at-rest control when the transfer role can use that key.
- **Reusable rule:** Evaluate hybrid transfers in two planes: encrypted transport for movement and an authorized destination key for at-rest protection.
- **Official reference:** [AWS](https://docs.aws.amazon.com/datasync/latest/userguide/data-encryption.html), [AWS](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html)

## SIM-B-21 — Answer C

- **Central requirement:** Durable buffering and independent scaling between a request producer and consumer.
- **Decisive words:** faster than worker, durably buffered, scale independently
- **A:** A Direct Connect gateway supports network connectivity and is not an application message queue.
- **B:** Route 53 Resolver endpoints support hybrid DNS resolution and do not buffer application work.
- **C:** SQS provides durable message buffering so producers and consumers can operate and scale independently.
- **D:** A Dedicated Host changes EC2 tenancy but does not decouple the API from its workers.
- **Reusable rule:** Place a durable queue between components when producers and consumers must absorb different rates or failures independently.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

## SIM-B-22 — Answer B

- **Central requirement:** Fan out every event to isolated consumers with independent buffering and retries.
- **Decisive words:** each receive a copy, one backlog must not delay others
- **A:** A load balancer distributes requests among targets rather than giving every independent consumer its own event copy.
- **B:** SNS fanout delivers a copy to each SQS queue, while separate queues isolate consumer retries and backlogs.
- **C:** Local instance storage creates a single point of failure and tightly couples every consumer to one host.
- **D:** Competing consumers on one queue normally divide messages, so each system would not receive every event.
- **Reusable rule:** Use pub/sub fanout to separate queues when every consumer needs each event and independent failure isolation.
- **Official reference:** [AWS](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)

## SIM-B-23 — Answer A

- **Central requirement:** Ordered and deduplicated processing per order while retaining concurrency across orders.
- **Decisive words:** same order in sequence, duplicate submissions, different orders concurrently
- **A:** A FIFO queue preserves order within each message group, deduplicates messages, and permits concurrency across different groups.
- **B:** A standard queue provides at-least-once delivery and best-effort ordering, which does not meet per-order sequencing.
- **C:** A topic without a durable subscriber does not provide the required queueing, ordering, and recovery behavior.
- **D:** A single self-managed broker creates an avoidable failure and operational bottleneck for the migrated service.
- **Reusable rule:** Use a FIFO message group for each independent ordering key so ordering is preserved per entity without serializing all entities.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-understanding-logic.html)

## SIM-B-24 — Answer A,C

- **Central requirement:** Multi-AZ HTTP distribution combined with automatic horizontal EC2 scaling.
- **Decisive words:** healthy instances, multiple Availability Zones, automatically add or remove
- **A:** An ALB distributes Layer 7 requests to healthy targets across enabled Availability Zones.
- **B:** One fixed instance cannot provide horizontal elasticity or survive an Availability Zone failure.
- **C:** An Auto Scaling group adjusts instance capacity and can maintain targets across multiple Availability Zones.
- **D:** Tape Gateway provides virtual tape backup integration and does not route web application traffic.
- **E:** A NAT instance provides outbound translation and is neither a scalable web load balancer nor a suitable public endpoint.
- **Reusable rule:** Pair a load balancer with a multi-AZ Auto Scaling group for a horizontally scalable stateless EC2 tier.
- **Official reference:** [AWS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)

## SIM-B-25 — Answer D

- **Central requirement:** Pool bursty Lambda database connections and improve failover handling with minimal application change.
- **Decisive words:** thousands of concurrent functions, connection limit, pooling
- **A:** S3 Transfer Acceleration applies to object transfers and cannot proxy Aurora connections.
- **B:** An internet gateway does not pool connections and would be inappropriate for private database connectivity.
- **C:** SQS visibility controls message redelivery and has no effect on relational database connection limits.
- **D:** RDS Proxy pools and reuses database connections and can reduce application disruption during failovers.
- **Reusable rule:** Use RDS Proxy when serverless or highly concurrent clients would otherwise create excessive direct relational database connections.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)

## SIM-B-26 — Answer B

- **Central requirement:** Remove local session affinity so a web tier can scale horizontally.
- **Decisive words:** local disk, add and remove freely, without losing sessions
- **A:** More local disk preserves the coupling between a session and one instance and does not enable safe scale-in.
- **B:** External shared session storage makes the compute tier stateless so any healthy instance can serve a request.
- **C:** Per-user public addresses do not provide durable shared application state and create unnecessary networking complexity.
- **D:** Disabling health checks retains failed capacity and does not solve session loss during scaling or replacement.
- **Reusable rule:** Externalize mutable session state from a horizontally scaled compute tier so instances remain disposable and interchangeable.
- **Official reference:** [AWS](https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/data-store-offloading.html)

## SIM-B-27 — Answer A

- **Central requirement:** Cross-account, content-based event routing with producer and consumer decoupling.
- **Decisive words:** separate accounts, event content, producers must not know consumers
- **A:** EventBridge supports content-based routing and cross-account event delivery without coupling producers to consumer endpoints.
- **B:** Direct Connect supplies network connectivity and does not provide application event routing or event-bus authorization.
- **C:** EBS Multi-Attach is block storage for supported instances and is not a multi-account event integration mechanism.
- **D:** Private CA issues certificates but does not route or filter business events.
- **Reusable rule:** Use EventBridge when managed event buses and rules must route events by content across services or AWS accounts.
- **Official reference:** [AWS](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cross-account.html)

## SIM-B-28 — Answer B,D

- **Central requirement:** Durably absorb bursts, retry transient failures, and isolate poison documents.
- **Decisive words:** irregular bursts, limited rate, retried, isolate failing work
- **A:** Synchronous client retries tightly couple uploads to OCR availability and can amplify failures during a backlog.
- **B:** SQS absorbs burst traffic and permits consumers to process documents at a controlled, independently scalable rate.
- **C:** Instance store is ephemeral and creates a single-host dependency for durable pipeline state.
- **D:** A dead-letter queue isolates messages that exceed the configured retry threshold for later diagnosis and redrive.
- **E:** An inadequate visibility timeout causes concurrent duplicate processing instead of controlled retry behavior.
- **Reusable rule:** Use a queue for rate decoupling and a dead-letter queue for bounded retries and poison-message isolation.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

## SIM-B-29 — Answer C

- **Central requirement:** Asynchronous acceptance and scalable processing of jobs longer than an HTTP request lifecycle.
- **Decisive words:** 25 minutes, immediate acknowledgement, scale based on queued work
- **A:** Route 53 health checks monitor endpoints and are not a general-purpose long-running job processor.
- **B:** A long synchronous request is fragile; API Gateway integrations and Lambda's 15-minute maximum cannot support a 25-minute execution.
- **C:** An asynchronous queue accepts the request quickly, decouples processing time, and provides a metric for worker scaling.
- **D:** Load balancer cookies provide session affinity and cannot durably represent queued conversion work.
- **Reusable rule:** For long-running API work, return an identifier promptly and process the durable queued job asynchronously.
- **Official reference:** [AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/asynchronous-request-reply.html)

## SIM-B-30 — Answer D

- **Central requirement:** Cross-Region relational recovery with seconds-level RPO and minutes-level RTO.
- **Decisive words:** regional disaster, few seconds data loss, writable within minutes
- **A:** Application logs are not a transactionally consistent database replica and manual reconstruction cannot meet a minutes-level RTO.
- **B:** Monthly snapshots can lose weeks of data and require a lengthy restore, violating both RPO and RTO.
- **C:** An in-Region replica improves Availability Zone resilience but cannot survive loss of the entire Region.
- **D:** Aurora global databases provide low-latency cross-Region replication and support promotion of a secondary cluster for regional recovery.
- **Reusable rule:** For stringent Aurora regional DR, use a global database and rehearse the promotion and application-routing procedure.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

## SIM-B-31 — Answer A

- **Central requirement:** Correctly distinguish recovery time from acceptable data-loss time.
- **Decisive words:** unavailable for four hours, lose fifteen minutes
- **A:** RTO measures acceptable recovery duration, while RPO measures acceptable data loss expressed as time.
- **B:** This reverses the two definitions and would lead to an incorrect recovery design.
- **C:** The availability tolerance and data-loss tolerance are explicitly different in the scenario.
- **D:** Only the data-loss window is fifteen minutes; the allowed outage is four hours.
- **Reusable rule:** RTO answers how long recovery may take; RPO answers how much recent data may be lost.
- **Official reference:** [AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/recovery-time-objective-rto-and-recovery-point-objective-rpo.html)

## SIM-B-32 — Answer C,E

- **Central requirement:** Separate backup failure domains and continuously verify restorability.
- **Decisive words:** outside production account, evidence, actually restored
- **A:** A same-account, same-Region-only strategy retains common failure and administrative boundaries.
- **B:** Backup completion does not validate application dependencies, restore permissions, quotas, or restoration time.
- **C:** A protected copy outside the production failure or administrative boundary improves recoverability from account or regional incidents.
- **D:** Premature deletion reduces recovery choices and does not demonstrate that a restore succeeds.
- **E:** Restore testing creates scheduled recovery exercises and evidence instead of assuming that stored backups are usable.
- **Reusable rule:** A resilient backup strategy needs protected copies plus tested restores; a successful backup alone is insufficient.
- **Official reference:** [AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html), [AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-cross-account-backup.html)

## SIM-B-33 — Answer C

- **Central requirement:** Low-impact continuous disaster recovery for servers that cannot be rearchitected.
- **Decisive words:** VMware and physical servers, block-level replication, recovery instances
- **A:** AppFlow transfers data between supported SaaS applications and AWS services, not entire server operating environments.
- **B:** Database Migration Service moves database data and changes; it does not replicate complete server disks for disaster recovery.
- **C:** Elastic Disaster Recovery continuously replicates supported source servers to staging and orchestrates recovery launches on AWS.
- **D:** Transfer Family exposes managed file-transfer protocol endpoints and does not provide continuous server recovery.
- **Reusable rule:** Use Elastic Disaster Recovery for continuous server replication and recovery when legacy workloads cannot first be redesigned.
- **Official reference:** [AWS](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)

## SIM-B-34 — Answer A

- **Central requirement:** Automatic asynchronous S3 object replication to a bucket in another Region.
- **Decisive words:** automatic copies, second Region, continue source writes
- **A:** S3 replication requires versioning and a replication configuration and role to copy qualifying objects asynchronously across Regions.
- **B:** EBS snapshot policies manage block volumes and cannot create copies of S3 objects.
- **C:** S3 buckets are not attached to security groups, and a security group would not replicate data.
- **D:** A gateway endpoint creates a private access path and does not produce a second-Region object copy.
- **Reusable rule:** Use S3 Cross-Region Replication with versioning and an authorized role when objects need asynchronous regional copies.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

## SIM-B-35 — Answer D

- **Central requirement:** Dynamically fail over hybrid connectivity to an independent path after a Direct Connect circuit failure.
- **Decisive words:** one physical circuit, must not isolate, emergency path
- **A:** Changing the VLAN or bandwidth on the same circuit cannot survive failure of that circuit.
- **B:** Two virtual interfaces on one physical circuit retain the same circuit and location failure domain.
- **C:** An internet gateway does not terminate a customer IPsec or private BGP connection from the data center.
- **D:** An internet VPN supplies an independent connectivity path, while BGP can prefer Direct Connect and converge to the backup.
- **Reusable rule:** Hybrid resilience requires physically or logically independent paths; a VPN can back up Direct Connect when reduced failover performance is acceptable.
- **Official reference:** [AWS](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-site-to-site-vpn.html)

## SIM-B-36 — Answer A,D

- **Central requirement:** Distinguish database high availability from read-scaling replication.
- **Decisive words:** Multi-AZ, read replicas, primary purposes
- **A:** The classic RDS Multi-AZ DB instance uses synchronous replication to a standby and provides managed failover.
- **B:** The standby in a classic Multi-AZ DB instance is not exposed as a read-scaling endpoint.
- **C:** Read replica behavior varies by engine and topology and should not be treated as automatic synchronous HA.
- **D:** Read replicas address read scaling, whereas a Multi-AZ standby primarily improves database availability.
- **E:** Both designs create additional database copies for their different purposes.
- **Reusable rule:** Use Multi-AZ for managed availability and read replicas for read scaling unless a specific engine feature states otherwise.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html), [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

## SIM-B-37 — Answer C

- **Central requirement:** Managed multi-active DynamoDB operation and regional continuity for a global application.
- **Decisive words:** nearby Region, read and write, Region unavailable
- **A:** A VPC endpoint changes network access but does not create a second-Region copy or active endpoint.
- **B:** A local secondary index changes query access patterns inside one Region and provides no regional failover.
- **C:** Global tables provide managed multi-active replication so applications can read and write in multiple Regions.
- **D:** Exports support offline data use and recovery workflows, not live multi-Region application requests.
- **Reusable rule:** Use DynamoDB global tables when a key-value workload needs managed multi-Region active-active data access.
- **Official reference:** [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)

## SIM-B-38 — Answer B

- **Central requirement:** Managed, highly available Windows SMB storage with AD and Windows ACL compatibility.
- **Decisive words:** SMB, Active Directory, Windows ACLs, multiple Availability Zones
- **A:** EFS provides NFS file access and is not a native SMB Windows file system.
- **B:** FSx for Windows provides managed SMB file systems, Active Directory integration, Windows ACLs, and Multi-AZ options.
- **C:** S3 is object storage and does not directly expose NTFS or standard SMB file-system semantics.
- **D:** Instance store is ephemeral, local to one host, and cannot be shared as a managed Multi-AZ file system.
- **Reusable rule:** Choose FSx for Windows File Server when a Windows workload requires native SMB, AD integration, and Windows file semantics.
- **Official reference:** [AWS](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)

## SIM-B-39 — Answer D

- **Central requirement:** Accelerate long-distance uploads to a centralized S3 bucket through AWS edge networking.
- **Decisive words:** worldwide, far Region, edge network, no regional servers
- **A:** DAX accelerates DynamoDB reads and has no effect on transferring S3 objects.
- **B:** Glacier Deep Archive is a cold storage class and does not accelerate object uploads.
- **C:** S3 buckets do not attach EBS volumes, and EBS performance cannot change the client's internet path.
- **D:** Transfer Acceleration uses globally distributed edge locations and the AWS network to optimize long-distance S3 transfers.
- **Reusable rule:** Consider S3 Transfer Acceleration for geographically distant clients transferring objects to a centralized S3 bucket.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)

## SIM-B-40 — Answer B,E

- **Central requirement:** High-throughput shared POSIX scratch storage integrated with durable S3 datasets.
- **Decisive words:** HPC, thousands of cores, shared POSIX, deleted after results
- **A:** S3 is object storage and does not provide shared in-place POSIX file semantics for compute processes.
- **B:** FSx for Lustre provides a high-performance parallel POSIX file system and can integrate with an S3 data repository.
- **C:** EBS volumes are Availability Zone scoped, and a single volume is not a cross-AZ HPC shared file system.
- **D:** EFS serves general NFS workloads, but selecting One Zone without performance analysis does not meet the explicit parallel HPC requirement.
- **E:** Compute nodes can use the parallel file system during processing and return durable outputs to S3 before deleting temporary capacity.
- **Reusable rule:** Use FSx for Lustre as the parallel processing tier and S3 as the durable data repository for HPC pipelines.
- **Official reference:** [AWS](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-data-repositories.html)

## SIM-B-41 — Answer A

- **Central requirement:** Managed scheduling and compute for a container job that exceeds Lambda's standard duration.
- **Decisive words:** 40 minutes, containerized job, managed job queues
- **A:** AWS Batch schedules containerized jobs onto managed compute environments and supports workloads longer than the Lambda invocation limit.
- **B:** Route 53 provides DNS and health-check functions and cannot execute a containerized scientific job.
- **C:** Certificate Manager provisions and manages certificates but does not supply compute or job scheduling.
- **D:** Cognito provides application identity features and is unrelated to batch compute.
- **Reusable rule:** Use AWS Batch for queued container jobs requiring batch scheduling or execution beyond a standard Lambda invocation.
- **Official reference:** [AWS](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html), [AWS](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)

## SIM-B-42 — Answer B

- **Central requirement:** Elastic container execution without managing the underlying server fleet.
- **Decisive words:** containerized, variable traffic, no EC2 worker management
- **A:** A permanent Dedicated Host requires instance and host capacity management and does not match variable horizontal demand.
- **B:** Fargate supplies serverless container compute so the team scales tasks without administering the underlying EC2 fleet.
- **C:** A single self-managed server retains patching, scaling, and availability responsibilities.
- **D:** S3 stores objects and Route 53 resolves names; neither executes a container image.
- **Reusable rule:** Choose Fargate when containers are required but managing and patching the worker-node infrastructure is not.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)

## SIM-B-43 — Answer A

- **Central requirement:** AWS-consistent compute physically on premises for local latency and intermittent connectivity.
- **Decisive words:** inside facility, production equipment, WAN disruption, AWS-managed
- **A:** Outposts extends AWS infrastructure and services on premises for low-latency local processing while integrating with a home Region.
- **B:** S3 is object storage in a Region and cannot run the latency-sensitive factory control workload.
- **C:** CloudFront caches and delivers content at edge locations and is not an on-premises general compute operating environment.
- **D:** Object replication improves data-copy placement but does not execute control logic at the factory.
- **Reusable rule:** Choose Outposts when workloads require AWS infrastructure at an on-premises site for local latency or data residency.
- **Official reference:** [AWS](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html)

## SIM-B-44 — Answer A,B

- **Central requirement:** Scale repeated relational reads without moving writes away from the primary system of record.
- **Decisive words:** 90% reads, repeated popular queries, writes to primary
- **A:** Read replicas offload eligible read queries from the primary and can scale read capacity.
- **B:** ElastiCache can serve repeated hot reads at low latency when cache freshness and invalidation are designed correctly.
- **C:** Keeping all traffic on one primary preserves the existing bottleneck and adds no read capacity.
- **D:** An internet gateway provides a network path and cannot scale or accelerate relational queries.
- **E:** Instance store is ephemeral and is not a durable, managed location for the database system of record.
- **Reusable rule:** Scale relational reads with replicas and reduce repeated database work with a carefully invalidated cache.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html), [AWS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)

## SIM-B-45 — Answer C

- **Central requirement:** High-performance traversal of a very large and frequently changing relationship graph.
- **Decisive words:** billions of relationships, multi-hop paths, purpose-built
- **A:** Timestream is purpose-built for time-series data rather than general graph traversal across connected entities.
- **B:** Memcached is an ephemeral cache and is not a durable graph database for multi-hop relationship queries.
- **C:** Neptune is a managed graph database designed for relationship traversal and supported graph query models.
- **D:** Encoding every relationship in text prevents efficient graph traversal and ignores the purpose-built database requirement.
- **Reusable rule:** Select a graph database such as Neptune when relationship traversal is the dominant access pattern.
- **Official reference:** [AWS](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)

## SIM-B-46 — Answer A

- **Central requirement:** Choose a DynamoDB partition key that supports even high-volume traffic distribution.
- **Decisive words:** very high request rate, distribute evenly, partition key
- **A:** High-cardinality, well-distributed partition-key values help spread requests and storage across DynamoDB partitions.
- **B:** One constant value creates a hot partition and prevents effective traffic distribution.
- **C:** A shared monthly value can concentrate current traffic into a small number of hot keys.
- **D:** Only two possible values provide very low cardinality and poor distribution for a high-rate table.
- **Reusable rule:** Prefer high-cardinality DynamoDB partition keys with request activity spread across many values; avoid hot keys.
- **Official reference:** [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html)

## SIM-B-47 — Answer D

- **Central requirement:** Scalable private service consumption across accounts without internet exposure or network-mesh connectivity.
- **Decisive words:** service VPC, customer accounts, private IPs, no peering mesh
- **A:** Gateway endpoints support S3 and DynamoDB service access and cannot publish an arbitrary provider TCP service.
- **B:** VPC peering is not transitive, and a many-customer mesh increases route and address-overlap complexity.
- **C:** Public addresses violate the private-connectivity requirement and expand exposure and address cost.
- **D:** PrivateLink exposes a provider service through private interface endpoints without requiring internet access or full network peering.
- **Reusable rule:** Use AWS PrivateLink when consumers need private access to a provider service without joining entire VPC networks.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html)

## SIM-B-48 — Answer C,D

- **Central requirement:** Dedicated hybrid connectivity combined with IPsec encryption.
- **Decisive words:** mainframe on premises, dedicated path, predictable, IPsec
- **A:** CloudFront accelerates content delivery to edge locations and does not provide private mainframe-to-VPC connectivity.
- **B:** Client VPN is designed for individual client devices, not a mainframe network integration.
- **C:** Direct Connect supplies the dedicated connectivity and predictable network path required by the bank.
- **D:** A supported Site-to-Site VPN design adds IPsec encryption to traffic using Direct Connect connectivity.
- **E:** S3 Transfer Acceleration optimizes object transfers and does not create an encrypted hybrid application network.
- **Reusable rule:** Direct Connect provides a dedicated path; combine it with a supported VPN design when IPsec encryption is also mandatory.
- **Official reference:** [AWS](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-site-to-site-vpn.html)

## SIM-B-49 — Answer C

- **Central requirement:** Static anycast entry points and healthy multi-Region routing for a global TCP service.
- **Decisive words:** TCP, static anycast IP, two Regions, AWS global network
- **A:** A private hosted zone is not reachable by public gaming clients and does not provide the requested anycast addresses.
- **B:** CloudFront focuses on HTTP content delivery and signed cookies do not provide static anycast IPs for arbitrary TCP endpoints.
- **C:** Global Accelerator provides static anycast IP addresses and routes TCP or UDP traffic over the AWS network to healthy endpoints.
- **D:** A gateway endpoint creates private VPC routing to S3 and cannot accelerate public TCP services.
- **Reusable rule:** Use Global Accelerator for global TCP or UDP applications that need static anycast IPs and health-based regional routing.
- **Official reference:** [AWS](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

## SIM-B-50 — Answer D

- **Central requirement:** Heterogeneous database conversion with low-downtime initial load and ongoing change replication.
- **Decisive words:** Oracle to PostgreSQL, remain online, CDC, incompatible schema
- **A:** DNS routing selects endpoints and does not replicate or convert relational database contents.
- **B:** DataSync copies supported storage data but does not perform a transactional heterogeneous database migration into Aurora.
- **C:** S3 lifecycle rules transition or expire objects and cannot translate database schemas or stored code.
- **D:** Schema Conversion Tool addresses heterogeneous schema conversion, while DMS full load and CDC move initial and ongoing data.
- **Reusable rule:** For heterogeneous migrations, combine schema conversion with DMS full load and CDC; data movement alone does not convert application schema code.
- **Official reference:** [AWS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html), [AWS](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)

## SIM-B-51 — Answer C

- **Central requirement:** Managed, scheduled, verified online file transfer from on-premises NFS to S3.
- **Decisive words:** recurring, incremental, NFS, scheduling, verification
- **A:** Kinesis Data Streams ingests event records and does not copy an NFS file hierarchy with metadata verification.
- **B:** Volume Gateway presents hybrid block storage and is not the primary service for scheduled NFS-to-S3 migration tasks.
- **C:** DataSync is designed for managed online movement between supported on-premises storage and AWS storage with scheduling and verification.
- **D:** DMS migrates supported databases and data stores rather than general NFS file systems.
- **Reusable rule:** Use DataSync for accelerated and verifiable online transfers between supported file or object storage systems and AWS storage.
- **Official reference:** [AWS](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)

## SIM-B-52 — Answer A,B,C

- **Central requirement:** Replayable ingestion, stateful stream transformation, and buffered analytics delivery to S3.
- **Decisive words:** retained for replay, stateful windows, continuous buffered delivery
- **A:** Kinesis Data Streams supplies partitioned ordered ingestion and retains records so consumers can replay them.
- **B:** Managed Service for Apache Flink performs stateful event-time and windowed transformations on streaming data.
- **C:** Data Firehose buffers streaming records and can deliver compressed, converted output to S3.
- **D:** SQS FIFO provides ordered messaging but is not itself a stateful windowed stream analytics engine.
- **E:** RDS Proxy pools relational database connections and does not serialize or transform streaming events.
- **F:** DMS replicates databases and is not the intended public ingestion endpoint for application click events.
- **Reusable rule:** Separate streaming pipelines into an ingest log, a stateful processing layer, and a managed delivery sink.
- **Official reference:** [AWS](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [AWS](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html), [AWS](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

## SIM-B-53 — Answer B

- **Central requirement:** Automatically optimize unpredictable S3 access patterns while retaining immediate object access.
- **Decisive words:** unpredictable, change over time, millisecond, automatic
- **A:** Deep Archive requires asynchronous restoration and therefore cannot satisfy the millisecond-access requirement for all objects.
- **B:** Intelligent-Tiering monitors access and automatically moves objects among eligible tiers while its immediate-access tiers retain millisecond access.
- **C:** One Zone-IA stores data in one Availability Zone and is unsuitable as the sole copy of irreplaceable enterprise data.
- **D:** Provisioned block volumes on a permanent server add capacity management and are not cost-effective at this object scale.
- **Reusable rule:** Use S3 Intelligent-Tiering when access patterns are unknown or changing and automatic tiering is worth the monitoring charge.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)

## SIM-B-54 — Answer D

- **Central requirement:** Lower general-purpose block cost while provisioning capacity, IOPS, and throughput independently.
- **Decisive words:** large only for IOPS, independently, reduce cost
- **A:** S3 Glacier is object archival storage and cannot be mounted as an EC2 boot block volume.
- **B:** io2 is intended for demanding, high-durability and high-IOPS workloads and may add unnecessary cost here.
- **C:** Instance store is ephemeral and cannot replace durable EBS volumes for persistent application data.
- **D:** gp3 separates volume size from provisioned IOPS and throughput and is the cost-focused general-purpose SSD generation.
- **Reusable rule:** Evaluate gp3 when gp2 volumes are oversized merely to obtain performance tied to capacity.
- **Official reference:** [AWS](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html)

## SIM-B-55 — Answer C

- **Central requirement:** Automatically lower the cost of inactive EFS files without changing application file access.
- **Decisive words:** rarely opened, same NFS namespace, least effort
- **A:** More throughput can increase cost and does not move cold files to a lower-cost storage tier.
- **B:** Instance store is ephemeral and host-local; the manual copy and redirect catalog also violate the requirements for unchanged applications and minimal operations.
- **C:** EFS lifecycle management moves inactive files to lower-cost EFS storage while preserving transparent file-system access.
- **D:** EBS is not a cross-Region shared NFS file system and does not preserve the existing EFS namespace.
- **Reusable rule:** Use EFS lifecycle management when files become inactive but applications must retain transparent access through EFS.
- **Official reference:** [AWS](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

## SIM-B-56 — Answer A,D,F

- **Central requirement:** Recognize storage-class pricing and retrieval trade-offs before selecting a lower-cost tier.
- **Decisive words:** cost, availability characteristics, influence choice
- **A:** Standard-IA trades lower storage price for retrieval and minimum-duration considerations, which matter for short-lived or frequently read data.
- **B:** Intelligent-Tiering automatically moves eligible objects based on observed access; manual prediction is not required for automatic tiers.
- **C:** Some transitions and storage classes have minimum object-size or duration charging considerations that must be evaluated.
- **D:** One Zone-IA uses one Availability Zone and therefore suits data that can be recreated or has another durable copy.
- **E:** EBS snapshots are durable incremental backups stored independently of whether the source volume remains attached.
- **F:** The archive storage classes use asynchronous retrieval workflows rather than immediate access to archived object data.
- **Reusable rule:** Storage cost decisions must include retrieval fees, minimum durations, restore latency, and failure-domain requirements, not price per GB alone.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

## SIM-B-57 — Answer D

- **Central requirement:** Discount a stable compute baseline while retaining family, Region, and compute-service flexibility.
- **Decisive words:** three years, change families and Regions, EC2 Fargate Lambda
- **A:** Lambda does not run on customer-purchased Dedicated Hosts, and this would not provide the requested cross-service flexibility.
- **B:** EC2 Instance Savings Plans can offer discounts but provide less flexibility because they are tied to a family in a Region.
- **C:** Spot capacity can be interrupted and should not be treated as a guaranteed baseline for all production workloads.
- **D:** Compute Savings Plans can apply across EC2 instance families and Regions and to eligible Fargate and Lambda usage.
- **Reusable rule:** Choose Compute Savings Plans for broad compute flexibility; choose narrower commitments only when their constraints are acceptable.
- **Official reference:** [AWS](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)

## SIM-B-58 — Answer B

- **Central requirement:** Maintain a reliable compute baseline and use low-cost interruptible capacity for resilient bursts.
- **Decisive words:** checkpointed, small always available, lowest-cost burst, several families
- **A:** Keeping peak On-Demand capacity running wastes spend during lower-demand periods.
- **B:** A mixed instances policy preserves a baseline while diversified Spot capacity reduces cost for interruption-tolerant burst work.
- **C:** Idle Dedicated Hosts impose high fixed cost and are unnecessary for a flexible rendering workload.
- **D:** One large instance creates a scaling and failure bottleneck and does not exploit the workload's checkpoint tolerance.
- **Reusable rule:** Blend an On-Demand baseline with diversified Spot capacity when queued or checkpointed work can tolerate interruptions.
- **Official reference:** [AWS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html)

## SIM-B-59 — Answer A

- **Central requirement:** Evidence-based rightsizing recommendations that preserve workload performance.
- **Decisive words:** overprovisioned, utilization metrics, projected candidate sizes
- **A:** Compute Optimizer analyzes configuration and utilization to produce rightsizing findings, recommendations, and projected utilization.
- **B:** Artifact supplies AWS compliance documents and agreements, not resource utilization recommendations.
- **C:** Route 53 Resolver provides DNS resolution features and does not analyze compute sizing.
- **D:** CloudHSM provides dedicated cryptographic hardware and has no compute-rightsizing function.
- **Reusable rule:** Use Compute Optimizer for utilization-based rightsizing guidance, then validate the recommendation before changing production capacity.
- **Official reference:** [AWS](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

## SIM-B-60 — Answer B,C,E

- **Central requirement:** Reduce a stable RDS workload's cost while preserving required Multi-AZ availability.
- **Decisive words:** steady, Multi-AZ must remain, low utilization, three years
- **A:** Unused replicas add database and storage cost without satisfying a stated performance or resilience need.
- **B:** Rightsizing can remove excess capacity, but the team must evaluate more than average CPU before reducing the class.
- **C:** Compatible Graviton classes can improve price performance when application and engine behavior are validated.
- **D:** Removing Multi-AZ violates the explicit availability requirement and is not an acceptable cost optimization.
- **E:** A Reserved DB Instance can discount a predictable long-running RDS baseline without requiring Multi-AZ removal.
- **F:** A database-type migration without access-pattern and schema analysis is high risk and not an automatic cost reduction.
- **Reusable rule:** Cost-optimize stable databases through evidence-based rightsizing, price-performance classes, and commitments without violating availability requirements.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html), [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.Types.html)

## SIM-B-61 — Answer C

- **Central requirement:** Cost and scale a new DynamoDB workload with unpredictable request volume and no capacity planning.
- **Decisive words:** new, unknown traffic, sudden peaks, pay per request
- **A:** RDS reservations apply to eligible relational database instances and cannot purchase DynamoDB table throughput.
- **B:** A permanently minimal provisioned setting would throttle peaks and requires capacity planning or auto scaling.
- **C:** On-demand mode automatically accommodates changing request rates and charges per request without throughput capacity planning.
- **D:** DynamoDB is managed and does not expose table partitions as customer EC2 Spot capacity.
- **Reusable rule:** Start with DynamoDB on-demand for unpredictable traffic; evaluate provisioned capacity when usage becomes sufficiently stable.
- **Official reference:** [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html)

## SIM-B-62 — Answer B

- **Central requirement:** Reduce and stabilize the database cost of a consistently I/O-intensive Aurora workload.
- **Decisive words:** highly I/O intensive, large consistent I/O charges, no per-operation
- **A:** Unused replicas add compute and storage cost and do not eliminate Standard configuration I/O charges.
- **B:** Aurora I/O-Optimized removes read and write I/O charges and is intended for I/O-intensive workloads where that pricing is beneficial.
- **C:** Glacier Deep Archive is object archival storage and cannot serve as Aurora's live transactional storage.
- **D:** Aurora manages its distributed storage layer and cannot use a customer-attached instance store volume.
- **Reusable rule:** Compare Aurora I/O-Optimized with Standard using the workload's measured I/O share; do not select it by name alone.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-storage-type.html)

## SIM-B-63 — Answer D

- **Central requirement:** Remove high-volume same-Region S3 traffic from an expensive NAT gateway path.
- **Decisive words:** most NAT processing, EC2 to S3, same Region
- **A:** Public addresses add exposure and public IPv4 cost and are unnecessary for private S3 service access.
- **B:** Another NAT gateway preserves or increases NAT processing cost instead of removing S3 traffic from the NAT path.
- **C:** Cross-Region transit adds unnecessary processing and transfer cost and does not optimize same-Region S3 access.
- **D:** An S3 gateway endpoint routes service traffic privately without NAT gateway hourly or data-processing charges for that path.
- **Reusable rule:** Inspect dominant NAT destinations and use gateway endpoints for S3 or DynamoDB when those private service paths fit.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [AWS](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html)

## SIM-B-64 — Answer D,E,F

- **Central requirement:** Reduce NAT, repeated origin-delivery, and avoidable cross-AZ network charges.
- **Decisive words:** S3 through NAT, cacheable downloads, unnecessary cross-AZ
- **A:** A distant single NAT can add cross-AZ charges and a failure dependency; cost cannot be evaluated without resilience and topology.
- **B:** Direct Connect connects sites or networks and is not provisioned separately for public internet consumers.
- **C:** An extra Region adds latency and inter-Region transfer cost without addressing the identified patterns.
- **D:** Gateway endpoints remove eligible S3 traffic from NAT processing while preserving a private service path.
- **E:** CloudFront serves cache hits near users and reduces repeated origin processing and data transfer from the regional origin.
- **F:** Zonal cache placement and locality-aware routing can avoid unnecessary cross-AZ bytes for chatty application-cache traffic.
- **Reusable rule:** Optimize network cost hop by hop: remove avoidable NAT processing, cache repeated delivery, and preserve zonal locality where appropriate.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html), [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

## SIM-B-65 — Answer A

- **Central requirement:** Cost-effective, predictable long-term hybrid connectivity for sustained high data volume.
- **Decisive words:** terabytes daily, five years, steady, carrier provisioning
- **A:** Direct Connect is designed for sustained dedicated hybrid connectivity and can provide predictable performance and different transfer pricing.
- **B:** Client VPN is a user remote-access service and is not an efficient foundation for steady data-center-scale transfer.
- **C:** Transfer Acceleration applies to S3 object transfers and does not create a general private hybrid application network.
- **D:** Public addresses do not provide dedicated performance and would expand exposure and address cost.
- **Reusable rule:** Evaluate Direct Connect for sustained high-volume hybrid traffic when provisioning lead time and fixed connectivity commitments are acceptable.
- **Official reference:** [AWS](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
