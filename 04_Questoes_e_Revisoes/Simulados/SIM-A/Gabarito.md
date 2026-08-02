# SIM-A — Commented answer key

**Navigation:** [Questions](Questoes.md) | [Commented answer key](Gabarito.md) | [Result report](Relatorio.md)

Open this file only after completing the timed attempt.

## Quick answer table

| ID | Answer | Domain | Task |
|---|---|---:|---:|
| SIM-A-01 | B | 1 | 1.1 |
| SIM-A-02 | C | 1 | 1.1 |
| SIM-A-03 | B | 1 | 1.1 |
| SIM-A-04 | A,B | 1 | 1.1 |
| SIM-A-05 | A | 1 | 1.1 |
| SIM-A-06 | C | 1 | 1.1 |
| SIM-A-07 | A | 1 | 1.1 |
| SIM-A-08 | A,C | 1 | 1.2 |
| SIM-A-09 | B | 1 | 1.2 |
| SIM-A-10 | D | 1 | 1.2 |
| SIM-A-11 | C | 1 | 1.2 |
| SIM-A-12 | A,D | 1 | 1.2 |
| SIM-A-13 | A | 1 | 1.2 |
| SIM-A-14 | B | 1 | 1.2 |
| SIM-A-15 | A | 1 | 1.3 |
| SIM-A-16 | A,E | 1 | 1.3 |
| SIM-A-17 | D | 1 | 1.3 |
| SIM-A-18 | C | 1 | 1.3 |
| SIM-A-19 | D | 1 | 1.3 |
| SIM-A-20 | B,C | 1 | 1.3 |
| SIM-A-21 | D | 2 | 2.1 |
| SIM-A-22 | B | 2 | 2.1 |
| SIM-A-23 | C | 2 | 2.1 |
| SIM-A-24 | B,D | 2 | 2.1 |
| SIM-A-25 | A | 2 | 2.1 |
| SIM-A-26 | D | 2 | 2.1 |
| SIM-A-27 | D | 2 | 2.1 |
| SIM-A-28 | B,E | 2 | 2.1 |
| SIM-A-29 | B | 2 | 2.1 |
| SIM-A-30 | A | 2 | 2.2 |
| SIM-A-31 | C | 2 | 2.2 |
| SIM-A-32 | C,D | 2 | 2.2 |
| SIM-A-33 | A | 2 | 2.2 |
| SIM-A-34 | D | 2 | 2.2 |
| SIM-A-35 | A | 2 | 2.2 |
| SIM-A-36 | C,E | 2 | 2.2 |
| SIM-A-37 | C | 2 | 2.2 |
| SIM-A-38 | D | 3 | 3.1 |
| SIM-A-39 | C | 3 | 3.1 |
| SIM-A-40 | D,E | 3 | 3.1 |
| SIM-A-41 | C | 3 | 3.2 |
| SIM-A-42 | A | 3 | 3.2 |
| SIM-A-43 | B | 3 | 3.2 |
| SIM-A-44 | A,B | 3 | 3.3 |
| SIM-A-45 | D | 3 | 3.3 |
| SIM-A-46 | A | 3 | 3.3 |
| SIM-A-47 | B | 3 | 3.4 |
| SIM-A-48 | C,D | 3 | 3.4 |
| SIM-A-49 | D | 3 | 3.4 |
| SIM-A-50 | C | 3 | 3.5 |
| SIM-A-51 | B | 3 | 3.5 |
| SIM-A-52 | A,B,C | 3 | 3.5 |
| SIM-A-53 | A | 4 | 4.1 |
| SIM-A-54 | C | 4 | 4.1 |
| SIM-A-55 | D | 4 | 4.1 |
| SIM-A-56 | D,E,F | 4 | 4.1 |
| SIM-A-57 | B | 4 | 4.2 |
| SIM-A-58 | C | 4 | 4.2 |
| SIM-A-59 | B | 4 | 4.2 |
| SIM-A-60 | A,D,F | 4 | 4.3 |
| SIM-A-61 | A | 4 | 4.3 |
| SIM-A-62 | D | 4 | 4.3 |
| SIM-A-63 | A | 4 | 4.4 |
| SIM-A-64 | B,C,E | 4 | 4.4 |
| SIM-A-65 | B | 4 | 4.4 |

## SIM-A-01 — Answer B

- **Central requirement:** Provide least-privilege S3 access to EC2 without long-term credentials.
- **Decisive words:** EC2 workload, private S3 bucket, no long-term access keys
- **A:** Root access keys must not be issued to an application and would violate least privilege.
- **B:** Correct. An instance profile supplies temporary role credentials without embedding reusable secrets.
- **C:** An IAM user key remains a long-term secret and user data is not an appropriate secret store.
- **D:** Public access removes authentication and does not satisfy the private-bucket security requirement.
- **Reusable rule:** Use an IAM role for an AWS compute workload that must call AWS APIs.
- **Official reference:** [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

## SIM-A-02 — Answer C

- **Central requirement:** Delegate temporary, scoped access from one AWS account to another.
- **Decisive words:** cross-account, three months, temporary sessions, no duplicate users
- **A:** A public copy violates the access requirement and introduces stale duplicated data.
- **B:** Duplicate IAM users and distributed access keys increase operational effort and credential risk.
- **C:** Correct. A trusted role provides temporary sessions and can restrict actions and resources to the required prefix.
- **D:** Root credentials are not a workforce delegation mechanism and must never be shared.
- **Reusable rule:** For cross-account delegation, combine a target-account role trust policy with least-privilege permissions.
- **Official reference:** [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html)

## SIM-A-03 — Answer B

- **Central requirement:** Centralize workforce access and enforce an organization-wide permission boundary.
- **Decisive words:** forty accounts, corporate IdP, console and CLI, prevent local administrators
- **A:** Per-account users multiply long-term credentials and broad administrator access does not enforce the required guardrail.
- **B:** Correct. Identity Center centralizes temporary workforce access, while an SCP establishes an organization-level permissions guardrail.
- **C:** Security groups filter network traffic and cannot restrict AWS control-plane API permissions.
- **D:** Root credential sharing is unsafe and federation into one account does not provide governed access to all member accounts.
- **Reusable rule:** Use IAM Identity Center for workforce sessions and SCPs for maximum-permission guardrails across accounts.
- **Official reference:** [AWS](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html), [AWS](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

## SIM-A-04 — Answer A,B

- **Central requirement:** Authorize an assumed cross-account role to decrypt with a customer managed KMS key.
- **Decisive words:** Account A role, Account B KMS key, cross-account decryption
- **A:** Correct. Cross-account KMS use also requires an IAM permission in the external principal account.
- **B:** Correct. The key policy in the key-owning account must permit the external principal or delegated account.
- **C:** Public S3 access neither grants KMS decrypt permission nor satisfies the security requirement.
- **D:** Automatic rotation changes key material over time but does not grant any principal access.
- **E:** Security groups control network flows and cannot authorize a principal to use a KMS key.
- **Reusable rule:** Cross-account KMS authorization requires permission on both the key-policy side and the external IAM side.
- **Official reference:** [AWS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html)

## SIM-A-05 — Answer A

- **Central requirement:** Protect private static and dynamic web origins while serving global clients efficiently.
- **Decisive words:** private S3, HTTPS, web exploits, edge, minimal origin load
- **A:** Correct. CloudFront secures the private S3 origin, handles HTTPS, routes to multiple origins, and integrates with AWS WAF at the edge.
- **B:** An S3 website endpoint requires public accessibility, while network ACLs cannot inspect application-layer attacks.
- **C:** A NAT gateway provides outbound translation and does not protect or publish an S3 origin.
- **D:** Route 53 is DNS, and S3 versioning recovers object versions rather than filtering malicious web requests.
- **Reusable rule:** For a global protected web tier, combine CloudFront origin controls, TLS, and AWS WAF according to each origin.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html), [AWS](https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html)

## SIM-A-06 — Answer C

- **Central requirement:** Recognize how stateful security group filtering affects an established connection.
- **Decisive words:** established HTTPS connection, rule removed, stateful
- **A:** Stateful tracking permits response traffic without a mirrored rule for the ephemeral client port.
- **B:** Security group changes do not create or modify rules in a network ACL.
- **C:** Correct. Security groups are stateful and automatically allow response traffic for tracked connections.
- **D:** Network ACLs are stateless, but security groups maintain connection state.
- **Reusable rule:** Security groups are stateful; network ACLs are stateless and require matching traffic-direction rules.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)

## SIM-A-07 — Answer A

- **Central requirement:** Provide managed application authentication without issuing direct AWS credentials.
- **Decisive words:** sign-up, password recovery, MFA, backend API tokens
- **A:** Correct. A Cognito user pool provides managed sign-up, recovery, MFA, and OIDC-compatible tokens.
- **B:** IAM users are intended for AWS identities and do not scale as a consumer application directory.
- **C:** AWS Organizations governs AWS accounts and is not an end-user authentication service.
- **D:** An identity pool brokers temporary AWS credentials and does not by itself provide the requested user-directory features.
- **Reusable rule:** Use a Cognito user pool for application authentication and an identity pool only when users need AWS credentials.
- **Official reference:** [AWS](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)

## SIM-A-08 — Answer A,C

- **Central requirement:** Terminate trusted TLS and filter application-layer attacks before payment API targets.
- **Decisive words:** managed certificates, automatic renewal, SQL injection, before targets
- **A:** Correct. ACM integrates with the load balancer listener and manages renewal for eligible certificates.
- **B:** Network ACLs filter stateless IP traffic and cannot inspect HTTP request bodies.
- **C:** Correct. AWS WAF inspects application-layer requests and managed rule groups can address common web exploit patterns.
- **D:** Self-signed target certificates do not provide a managed public client trust path and exposing targets bypasses the load balancer controls.
- **E:** Route 53 provides DNS routing and cannot terminate TLS with a certificate stored in S3.
- **Reusable rule:** Use ACM on an HTTPS listener for managed TLS and AWS WAF for Layer 7 request filtering.
- **Official reference:** [AWS](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html), [AWS](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)

## SIM-A-09 — Answer B

- **Central requirement:** Rotate and retrieve a database credential with minimal custom operations.
- **Decisive words:** database password, every thirty days, programmatic retrieval, least effort
- **A:** User data is not a secure secret distribution mechanism and instance replacement adds unnecessary work.
- **B:** Correct. Secrets Manager stores, retrieves, and rotates supported secrets through an integrated rotation workflow.
- **C:** Plain-text S3 storage does not meet secure credential handling and lifecycle expiration is not password rotation.
- **D:** Embedding credentials in immutable images spreads old secrets and makes every rotation a deployment task.
- **Reusable rule:** Choose Secrets Manager when a secret needs managed storage and an automated rotation workflow.
- **Official reference:** [AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)

## SIM-A-10 — Answer D

- **Central requirement:** Provide a REST API reachable only through approved private VPC connectivity.
- **Decisive words:** selected VPCs, no public invocation, interface endpoints, resource policy
- **A:** CloudFront is internet-facing and an unguessable DNS name is not a security boundary.
- **B:** Backend security groups do not make the API Gateway public endpoint private.
- **C:** An edge-optimized API is publicly reachable, and hiding a URL is not an access-control mechanism.
- **D:** Correct. A private REST API plus interface endpoints and a resource policy provides private network reachability and explicit endpoint authorization.
- **Reusable rule:** For private API Gateway access, combine a private REST API, execute-api interface endpoints, and a restrictive resource policy.
- **Official reference:** [AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)

## SIM-A-11 — Answer C

- **Central requirement:** Encrypt large application data while retaining centralized KMS access control.
- **Decisive words:** large files, KMS-controlled access, not sending entire files
- **A:** A KMS key ARN identifies a managed key but is not exportable plaintext key material.
- **B:** KMS cryptographic APIs have payload limits and are not designed to encrypt large application files directly.
- **C:** Correct. Envelope encryption uses a data key for bulk data and protects that data key under a KMS key.
- **D:** The plaintext data key must be removed from memory after use and must never be stored with ciphertext.
- **Reusable rule:** Use envelope encryption: a data key encrypts bulk data and a KMS key protects the data key.
- **Official reference:** [AWS](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping)

## SIM-A-12 — Answer A,D

- **Central requirement:** Provide private, cost-conscious access from subnets to S3 and Secrets Manager.
- **Decisive words:** no NAT, no internet gateway, private connectivity, lowest endpoint cost
- **A:** Correct. An S3 gateway endpoint provides private S3 routing without hourly endpoint charges.
- **B:** A NAT gateway would reintroduce public egress dependency and recurring processing charges.
- **C:** Secrets Manager supports interface endpoints, not gateway endpoints.
- **D:** Correct. Secrets Manager is reached privately through an AWS PrivateLink interface endpoint.
- **E:** An S3 interface endpoint can work, but the gateway endpoint is generally the lower-cost in-Region option for this requirement.
- **Reusable rule:** Use gateway endpoints for supported S3 or DynamoDB traffic and interface endpoints for other PrivateLink services.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html), [AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html)

## SIM-A-13 — Answer A

- **Central requirement:** Authorize a time-limited set of private downloads and protect both edge and origin.
- **Decisive words:** many files, one path, one hour, reject direct S3, rate limited
- **A:** Correct. Signed cookies cover multiple restricted files, origin access control blocks direct S3 access, and AWS WAF can rate limit viewers.
- **B:** Public object URLs bypass CloudFront authorization and expose the origin directly.
- **C:** Browser clients cannot use a VPC gateway endpoint, and network ACLs cannot count application requests.
- **D:** Public access and obscure names do not enforce subscriber authorization or request-rate controls.
- **Reusable rule:** Use signed cookies for multiple private CloudFront objects, secure the origin, and add WAF controls for viewer abuse.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.html), [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

## SIM-A-14 — Answer B

- **Central requirement:** Detect suspicious activity across accounts and centrally aggregate security findings.
- **Decisive words:** managed threat detection, across accounts, central security account, standards
- **A:** Audit Manager helps collect audit evidence and does not inspect network or API activity as a threat engine.
- **B:** Correct. GuardDuty detects threats from supported data sources, while Security Hub centralizes and prioritizes findings and standards.
- **C:** Inspector assesses software vulnerabilities and exposure but is not the general cross-service finding aggregator described.
- **D:** AWS Artifact provides compliance reports and agreements rather than runtime threat detection.
- **Reusable rule:** Use a purpose-built detector such as GuardDuty and centralize normalized findings and standards in Security Hub.
- **Official reference:** [AWS](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html), [AWS](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)

## SIM-A-15 — Answer A

- **Central requirement:** Combine immutable retention, customer-controlled encryption, and cross-Region recovery for regulated exports.
- **Decisive words:** undeletable, seven years, customer-controlled keys, second Region
- **A:** Correct. Compliance retention supplies WORM protection, while KMS and replication controls address encryption and regional recovery.
- **B:** A single EBS-based archive lacks the requested S3 controls and timely cross-Region resilience.
- **C:** Governance mode with broad bypass permission does not meet the requirement that no user can delete records.
- **D:** Early expiration contradicts seven-year retention, and a monthly copy does not provide continuous S3 replication.
- **Reusable rule:** When requirements span retention, encryption, and resilience, configure Object Lock, KMS authorization, and replication together.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html), [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-config-for-kms-objects.html)

## SIM-A-16 — Answer A,E

- **Central requirement:** Encrypt sensitive traffic from clients to the load balancer and from the application to RDS.
- **Decisive words:** data in transit, both network segments, ALB, RDS
- **A:** Correct. An HTTPS listener encrypts the client-to-load-balancer connection with TLS.
- **B:** Fast snapshot restore affects EBS volume initialization and not data in transit.
- **C:** S3 Versioning preserves object versions but does not encrypt either requested network segment.
- **D:** A health check monitors reachability but does not provide transport encryption.
- **E:** Correct. Engine TLS settings and certificates protect the application-to-database connection.
- **Reusable rule:** Protect each hop explicitly: terminate trusted TLS at the web entry point and use database TLS on the backend connection.
- **Official reference:** [AWS](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html), [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)

## SIM-A-17 — Answer D

- **Central requirement:** Share an encrypted RDS snapshot so another account can restore it.
- **Decisive words:** encrypted snapshot, default managed key, separate account, restore
- **A:** Public database access is not snapshot sharing and unnecessarily exposes a live data store.
- **B:** CloudWatch Logs cannot serve as an RDS snapshot restoration source.
- **C:** A snapshot encrypted with the default AWS managed key cannot be shared across accounts in this way.
- **D:** Correct. Cross-account sharing requires a snapshot encrypted under a customer managed key whose policy permits the recipient.
- **Reusable rule:** For cross-account encrypted snapshot sharing, copy under a customer managed KMS key and grant both snapshot and key access.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html)

## SIM-A-18 — Answer C

- **Central requirement:** Protect selected DynamoDB fields while adding recovery and auditable API activity.
- **Decisive words:** selected attributes, point-in-time recovery, attributable requests
- **A:** A public unencrypted bucket violates confidentiality, and DNS query logs do not audit database API access.
- **B:** EC2 disk encryption does not protect DynamoDB attributes, and flow logs do not record item-level API operations.
- **C:** Correct. Client-side attribute protection, PITR, and CloudTrail DynamoDB data events address cryptographic separation, recovery, and item-level API audit independently.
- **D:** Global tables replicate accidental writes and do not replace point-in-time recovery or audit logging.
- **Reusable rule:** Match each data-security requirement to its control: application encryption, managed recovery, and API audit logging.
- **Official reference:** [AWS](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.html), [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html), [AWS](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html)

## SIM-A-19 — Answer D

- **Central requirement:** Authorize cross-account reads of S3 objects protected by a customer managed KMS key.
- **Decisive words:** Account B role, Account A bucket, SSE-KMS, retain control
- **A:** Neither S3 objects nor KMS keys should be made public to solve controlled cross-account access.
- **B:** AWS managed KMS keys cannot be shared through an alias as a substitute for key and S3 policies.
- **C:** S3 authorization cannot override a KMS denial or missing key authorization.
- **D:** Correct. Cross-account reads of SSE-KMS objects require authorization for both the S3 object and the customer managed KMS key.
- **Reusable rule:** For SSE-KMS cross-account access, authorize the external principal at both the S3 resource and KMS key layers.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html), [AWS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html)

## SIM-A-20 — Answer B,C

- **Central requirement:** Replicate SSE-KMS S3 objects across Regions while re-encrypting them with the destination key.
- **Decisive words:** versioning already enabled, SSE-KMS, destination key, replication
- **A:** Public write access is unnecessary, unsafe, and does not replace IAM and KMS authorization.
- **B:** Correct. SSE-KMS objects require explicit replication configuration and a destination encryption key.
- **C:** Correct. The replication role needs cryptographic permissions for the source and destination portions of the workflow.
- **D:** S3 replication uses an IAM role with permissions; it does not operate as the root user.
- **E:** A destination in another Region or account needs an appropriate destination key and cannot rely on an unrelated source managed key.
- **Reusable rule:** Encrypted S3 replication requires both rule-level KMS configuration and role permissions for the source and destination keys.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-config-for-kms-objects.html)

## SIM-A-21 — Answer D

- **Central requirement:** Buffer work durably between producers and slower backend consumers.
- **Decisive words:** traffic bursts, decouple, retain work, worker
- **A:** Route 53 Resolver answers DNS queries and does not retain application work items.
- **B:** Amazon EBS provides block storage to compute instances and is not a managed message queue.
- **C:** AWS Certificate Manager provisions and manages certificates rather than application messages.
- **D:** Correct. Amazon SQS durably buffers messages and decouples producers from consumers.
- **Reusable rule:** Use a durable queue when producers and consumers must scale independently and work cannot be lost.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

## SIM-A-22 — Answer B

- **Central requirement:** Preserve user session state while allowing the web tier to scale horizontally.
- **Decisive words:** three Availability Zones, carts lost, scale in, no stickiness
- **A:** Instance store data is local and ephemeral, so it is unsuitable for shared durable cart state.
- **B:** Correct. External session storage lets any healthy web instance serve the user and survives scaling events.
- **C:** Preventing all termination defeats elasticity and still leaves state tied to individual instances.
- **D:** A NAT gateway is an outbound translation service and cannot distribute inbound web requests.
- **Reusable rule:** Keep scalable web instances stateless and place shared session data in a resilient external store.
- **Official reference:** [AWS](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_stateless.html)

## SIM-A-23 — Answer C

- **Central requirement:** Process bursty orders with per-customer order, duplicate safety, and failure isolation.
- **Decisive words:** unpredictable bursts, in sequence, duplicate charges, repeated attempts
- **A:** Standard SNS delivery does not promise global ordering or exactly-once application effects.
- **B:** Weekly polling creates excessive latency and does not directly provide ordered per-customer processing.
- **C:** Correct. FIFO message groups preserve per-customer ordering, idempotency handles redelivery, and a DLQ isolates poison messages.
- **D:** Synchronous coupling makes API availability depend on payment availability and discarding requests loses orders.
- **Reusable rule:** Use ordered queue groups for scoped ordering, design consumers to be idempotent, and route poison messages to a DLQ.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html), [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

## SIM-A-24 — Answer B,D

- **Central requirement:** Fan out one business event to isolated consumers with separate retry backlogs.
- **Decisive words:** independently, one failure must not delay the other, own backlog
- **A:** An in-memory buffer is not durable and couples both teams to one instance.
- **B:** Correct. Independent queues isolate backlog, retries, and scaling for each consumer.
- **C:** Competing consumers on one queue divide messages instead of giving each service its own copy.
- **D:** Correct. EventBridge can route the same matching event to independent targets without coupling their processing.
- **E:** A synchronous chain makes fulfillment availability and latency depend on billing execution.
- **Reusable rule:** Fan out events to a queue per consumer when every consumer needs a copy and independent failure handling.
- **Official reference:** [AWS](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html), [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-subscribe-queue-sns-topic.html)

## SIM-A-25 — Answer A

- **Central requirement:** Coordinate a long-running distributed checkout with compensation, history, and asynchronous work.
- **Decisive words:** different compensating steps, survives for days, execution history, asynchronous
- **A:** Correct. Standard Workflows provide durable orchestration and history, while SQS decouples retryable shipping work.
- **B:** Lambda has a bounded execution duration and in-memory state cannot survive multi-day failures.
- **C:** EC2 user data is initialization logic and does not provide durable workflow state or targeted retries.
- **D:** Route 53 performs DNS routing and cannot coordinate business transactions or compensation.
- **Reusable rule:** Use durable orchestration for multi-step business state and queues for independently retryable asynchronous activities.
- **Official reference:** [AWS](https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html)

## SIM-A-26 — Answer D

- **Central requirement:** Identify the managed publish-and-subscribe service for event fanout.
- **Decisive words:** one event, multiple subscribers, own copy, publish and subscribe
- **A:** Amazon EFS is a shared file system and does not implement event fanout.
- **B:** EC2 Auto Scaling adjusts compute capacity but does not distribute application events to subscribers.
- **C:** AWS Direct Connect supplies network connectivity and is not a notification broker.
- **D:** Correct. Amazon SNS publishes a message to multiple subscribed endpoints or services.
- **Reusable rule:** Use SNS when one publication must be pushed to multiple independent subscriptions.
- **Official reference:** [AWS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

## SIM-A-27 — Answer D

- **Central requirement:** Preserve per-device order while distributing stream load across devices.
- **Decisive words:** same device, arrival order, scale across many devices
- **A:** Random keys can send one device records to different shards and lose per-device ordering.
- **B:** Route 53 health checks do not provide stream partitioning or telemetry ingestion.
- **C:** One universal key creates a hot shard and prevents throughput from scaling across devices.
- **D:** Correct. A stable device partition key keeps that device on one shard while different devices can distribute across shards.
- **Reusable rule:** Choose a partition key for the scope that needs ordering, with enough key diversity and shard capacity for throughput.
- **Official reference:** [AWS](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html)

## SIM-A-28 — Answer B,E

- **Central requirement:** Absorb API bursts durably and process accepted requests without duplicate business effects.
- **Decisive words:** flash-sale bursts, asynchronous, no loss, retries, no duplicate records
- **A:** Disabling retries trades duplicate risk for data loss and does not satisfy reliable processing.
- **B:** Correct. SQS durably absorbs the burst and decouples the API acceptance rate from downstream processing.
- **C:** Longer synchronous timeouts do not buffer durable work and keep availability coupled to the downstream service.
- **D:** Lambda memory is ephemeral and cannot guarantee accepted-request durability.
- **E:** Correct. Queue-driven scaling restores throughput, while idempotency prevents redelivery from creating duplicate effects.
- **Reusable rule:** Buffer asynchronous work in a durable queue and make the business operation idempotent before scaling consumers.
- **Official reference:** [AWS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html), [AWS](https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/)

## SIM-A-29 — Answer B

- **Central requirement:** Provide shared low-latency Redis-compatible sessions for a stateless web fleet.
- **Decisive words:** submillisecond, short-lived sessions, automatic failover, Redis
- **A:** Instance store ties sessions to individual hosts and loses data when an instance stops.
- **B:** Correct. A replicated ElastiCache deployment provides low-latency shared sessions and regional automatic failover.
- **C:** Glacier Deep Archive has retrieval delays and is not an online session store.
- **D:** An RDS read replica cannot operate as a standalone writable session primary.
- **Reusable rule:** Use a replicated managed in-memory store for shared ephemeral state that must survive individual node failure.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html)

## SIM-A-30 — Answer A

- **Central requirement:** Provide low-RPO cross-Region relational recovery and route clients to the promoted writer.
- **Decisive words:** global reads, RPO seconds, managed promotion, active writer
- **A:** Correct. Aurora global database supplies low-lag cross-Region replication and managed switchover or failover capabilities; DNS completes client routing.
- **B:** A larger single instance remains a regional and instance-level single point of failure.
- **C:** Weekly snapshots have an excessive RPO and keeping them only in the primary Region does not address a regional outage.
- **D:** RDS Multi-AZ is a regional high-availability feature, not a cross-Region read and disaster-recovery topology.
- **Reusable rule:** For low-lag relational disaster recovery, pair cross-Region database replication with an explicit client endpoint failover plan.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html), [AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

## SIM-A-31 — Answer C

- **Central requirement:** Select the managed RDS feature for synchronous standby failover across Availability Zones.
- **Decisive words:** synchronously replicated standby, automatic failover, Availability Zone
- **A:** S3 lifecycle policies manage object storage classes and do not protect an RDS primary.
- **B:** A read replica is primarily for read scaling and normally requires a promotion decision rather than standard Multi-AZ failover.
- **C:** Correct. A Multi-AZ deployment maintains a synchronous standby and performs managed failover.
- **D:** A placement group controls EC2 placement and cannot create an RDS standby.
- **Reusable rule:** Use RDS Multi-AZ for regional database high availability; use read replicas primarily for read scaling.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html)

## SIM-A-32 — Answer C,D

- **Central requirement:** Keep a replaceable load-balanced EC2 web tier available through one zonal failure.
- **Decisive words:** loss of any one Availability Zone, replaceable, load balancer
- **A:** Health checks must evaluate the serving targets; an unrelated S3 bucket cannot represent application health.
- **B:** A single manually recovered instance does not meet the required automatic zonal availability.
- **C:** Correct. A load balancer enabled across zones routes traffic only to healthy registered targets.
- **D:** Correct. Multi-AZ subnets let Auto Scaling launch and replace capacity outside a failed zone.
- **E:** One subnet leaves the entire fleet dependent on a single Availability Zone.
- **Reusable rule:** Distribute both load-balancer nodes and scalable targets across multiple Availability Zones for zonal fault tolerance.
- **Official reference:** [AWS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-as-policies.html), [AWS](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html)

## SIM-A-33 — Answer A

- **Central requirement:** Protect critical S3 data from both a regional disruption and accidental overwrite propagation.
- **Decisive words:** two Regions, accidental overwrites, last known good copy
- **A:** Correct. Version history, regional replication, and retention or carefully scoped replication provide recovery from both regional and logical failures.
- **B:** An unversioned single bucket cannot recover overwritten content or provide a regional alternate.
- **C:** Instance store is ephemeral and keeping it in the primary Region does not satisfy regional resilience.
- **D:** Transfer Acceleration improves transfer paths but does not create a disaster-recovery copy or version history.
- **Reusable rule:** Combine regional redundancy with version retention controls; replication alone can propagate logical errors.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html), [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

## SIM-A-34 — Answer D

- **Central requirement:** Create centrally governed, isolated, deletion-resistant backups across accounts and Regions.
- **Decisive words:** RDS EBS DynamoDB, separate account and Region, resist deletion
- **A:** Passwords are not backups, and EC2 user data is not a cross-Region recovery mechanism.
- **B:** CloudFront origin failover serves HTTP content and cannot manage service backups.
- **C:** Custom functions and local state add operational risk and do not inherently provide immutable centralized retention.
- **D:** Correct. AWS Backup centralizes supported resource policies and copies, while Vault Lock strengthens retention against deletion.
- **Reusable rule:** Use AWS Backup for multi-service policy orchestration and isolate protected copies in a locked destination vault.
- **Official reference:** [AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-account-backup.html), [AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html)

## SIM-A-35 — Answer A

- **Central requirement:** Choose a cost-conscious regional DR pattern for one-hour RTO and fifteen-minute RPO.
- **Decisive words:** RTO one hour, RPO fifteen minutes, lower cost, continuously replicated
- **A:** Correct. Pilot light minimizes idle compute while continuous data replication and automation can satisfy the stated RPO and one-hour RTO when tested.
- **B:** A fully active design could improve recovery but has much higher steady-state cost than required.
- **C:** Larger primary instances do not provide recovery from a regional outage.
- **D:** A weekly backup exceeds the RPO, and manual provisioning makes the RTO unreliable.
- **Reusable rule:** Map RTO and RPO to a tested DR pattern; pilot light trades more recovery automation for lower idle compute cost.
- **Official reference:** [AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/pilot-light.html)

## SIM-A-36 — Answer C,E

- **Central requirement:** Identify the Availability Zone properties that enable regional fault tolerance.
- **Decisive words:** distinct locations, failure domains, redundant capacity
- **A:** Edge locations deliver edge services and do not host an RDS Multi-AZ standby as an Availability Zone.
- **B:** An Availability Zone belongs to one Region and does not span Regions.
- **C:** Correct. Redundant Multi-AZ capacity lets an application continue when one zone is unavailable.
- **D:** Multiple subnets in one Availability Zone still share that zone as a failure domain.
- **E:** Correct. Availability Zones are separate failure domains within an AWS Region.
- **Reusable rule:** For zonal resilience, place redundant resources in multiple Availability Zones rather than multiple subnets in one zone.
- **Official reference:** [AWS](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html)

## SIM-A-37 — Answer C

- **Central requirement:** Route DNS to a secondary regional endpoint only after primary health failure.
- **Decisive words:** primary and secondary, automatically, health check fails
- **A:** Equal weighted records distribute traffic rather than reserve one endpoint strictly for failure.
- **B:** Geolocation chooses by location and does not implement primary-secondary health failover by itself.
- **C:** Correct. Failover records designate primary and secondary resources and use health evaluation to select the secondary.
- **D:** Simple routing does not provide the requested primary health-based failover behavior.
- **Reusable rule:** Use Route 53 failover routing for active-passive DNS behavior and validate that the health check represents application health.
- **Official reference:** [AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

## SIM-A-38 — Answer D

- **Central requirement:** Combine high-throughput S3-backed file access with low-latency tightly coupled EC2 networking.
- **Decisive words:** multi-terabyte S3, HPC, POSIX, high throughput, inter-node latency
- **A:** S3 is object storage rather than an EBS boot volume, and cross-Region placement increases inter-node latency.
- **B:** EFS is not the purpose-built parallel Lustre file system for this HPC access pattern, and public routing is unnecessary.
- **C:** Manual copies create inconsistent data and cross-Region spread placement conflicts with low-latency coupling.
- **D:** Correct. FSx for Lustre provides parallel high-throughput file access and S3 integration, while cluster placement optimizes tightly coupled networking.
- **Reusable rule:** For S3-backed HPC, match a parallel file system to the data path and a cluster placement strategy to node communication.
- **Official reference:** [AWS](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html), [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html)

## SIM-A-39 — Answer C

- **Central requirement:** Provide durable, predictable high-IOPS block storage for a latency-sensitive EC2 database.
- **Decisive words:** sustained high IOPS, sub-millisecond, durable block storage
- **A:** Instance store can be fast but is ephemeral and does not satisfy independent durability.
- **B:** Glacier Deep Archive is object archival storage with retrieval delay, not a transactional block device.
- **C:** Correct. EBS io2 is durable block storage designed for high, provisioned IOPS and low-latency workloads.
- **D:** EFS archive classes are file storage tiers and do not provide the required database block semantics.
- **Reusable rule:** Choose provisioned IOPS EBS for durable EC2 block workloads whose IOPS and latency requirements are explicit.
- **Official reference:** [AWS](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html)

## SIM-A-40 — Answer D,E

- **Central requirement:** Improve reliability and global performance for direct transfers of very large S3 objects.
- **Decisive words:** multi-gigabyte, unreliable, retry failed portions, accelerated path
- **A:** An archive class does not improve upload reliability or establish an accelerated network path.
- **B:** Restarting the complete transfer wastes bandwidth and does not meet the failed-portion retry requirement.
- **C:** A self-managed NAT instance is not an inbound global S3 acceleration service and creates a bottleneck.
- **D:** Correct. Transfer Acceleration uses the AWS edge network to accelerate eligible long-distance S3 transfers.
- **E:** Correct. Multipart upload divides a large object into independently retryable parts and supports parallel transfer.
- **Reusable rule:** Use multipart transfer for large-object resilience and Transfer Acceleration when long-distance S3 network performance justifies it.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html), [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)

## SIM-A-41 — Answer C

- **Central requirement:** Increase compute resources available to a CPU-bound Lambda invocation.
- **Decisive words:** CPU-bound, execution time, does not run out of memory
- **A:** SQS visibility timeout is unrelated to an S3 invocation and does not allocate Lambda CPU.
- **B:** Lambda service availability is managed by AWS and CPU is not increased by selecting more Availability Zones.
- **C:** Correct. Lambda allocates CPU and other resources in proportion to the configured memory.
- **D:** Log retention changes storage duration for logs and not function compute capacity.
- **Reusable rule:** Lambda memory is also a compute-sizing control; benchmark memory settings because more memory can reduce duration.
- **Official reference:** [AWS](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html)

## SIM-A-42 — Answer A

- **Central requirement:** Choose an EC2 family that matches sustained CPU-intensive computation.
- **Decisive words:** heavy floating-point, little memory pressure, continuous, no interruption
- **A:** Correct. Compute optimized instances are designed for workloads with a high compute-to-memory ratio.
- **B:** A sustained CPU workload can exhaust burst credits and is not a natural fit for burstable instances.
- **C:** S3 Glacier retrieval is an object archive operation and cannot execute a simulation.
- **D:** Storage optimized instances target high local storage throughput rather than primarily floating-point CPU demand.
- **Reusable rule:** Match the dominant resource dimension first; compute optimized instances fit sustained CPU-bound workloads.
- **Official reference:** [AWS](https://docs.aws.amazon.com/ec2/latest/instancetypes/co.html)

## SIM-A-43 — Answer B

- **Central requirement:** Run bursty twenty-minute container jobs without managing hosts while decoupling API ingestion.
- **Decisive words:** containers, unpredictable bursts, twenty minutes, no EC2 hosts
- **A:** One fixed host creates a bottleneck and management burden and its local queue is not durable.
- **B:** Correct. SQS decouples ingestion, while Fargate runs long container jobs without customer-managed EC2 hosts.
- **C:** A standard Lambda invocation cannot exceed its maximum execution duration and therefore cannot run a twenty-minute job.
- **D:** Archive retrieval is unrelated to container execution and introduces unacceptable job delay.
- **Reusable rule:** For container jobs beyond Lambda duration, use a queue and autoscaled ECS on Fargate when host management is unwanted.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

## SIM-A-44 — Answer A,B

- **Central requirement:** Scale a read-heavy DynamoDB catalog while accelerating repeatedly accessed items.
- **Decisive words:** high traffic, repeated reads, small hot set, avoid hot partitions
- **A:** Correct. DAX can serve microsecond in-memory cached reads for compatible DynamoDB access patterns.
- **B:** Correct. A high-cardinality key distributes data and request load, reducing hot-partition risk.
- **C:** Forcing one partition and one proxy creates bottlenecks rather than scalable read performance.
- **D:** One constant key concentrates throughput and creates a hot partition.
- **E:** Full table scans consume more capacity and have less predictable performance than key-based access.
- **Reusable rule:** Design DynamoDB keys for even distribution and add DAX only when a compatible read pattern benefits from caching.
- **Official reference:** [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html), [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html)

## SIM-A-45 — Answer D

- **Central requirement:** Control serverless database connection storms and scale Aurora read traffic independently.
- **Decisive words:** thousands of Lambda functions, connection storms, read capacity, writes
- **A:** Longer Lambda timeouts do not pool connections or add read capacity, and one connection is not a scalable shared socket.
- **B:** A live database socket cannot be serialized to S3 and safely reused by independent Lambda environments.
- **C:** MX records describe mail exchangers and do not provide database pooling or query routing.
- **D:** Correct. RDS Proxy pools connections, while Aurora replicas and reader routing add read capacity without accepting application writes.
- **Reusable rule:** Use a managed connection proxy for bursty clients and database replicas or reader endpoints for read scaling.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html), [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html)

## SIM-A-46 — Answer A

- **Central requirement:** Identify the managed in-memory service for repeated low-latency database reads.
- **Decisive words:** same records, millions of reads, stale acceptable, microsecond
- **A:** Correct. ElastiCache provides managed in-memory data stores for low-latency caching.
- **B:** CloudFormation provisions infrastructure and does not serve application cache records.
- **C:** Glacier Deep Archive is for long-term object retention with delayed retrieval.
- **D:** Resolver DNS Firewall filters DNS queries and is not an application data cache.
- **Reusable rule:** Use an in-memory cache when repeated reads tolerate controlled staleness and database offload is valuable.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html)

## SIM-A-47 — Answer B

- **Central requirement:** Provide static global entry addresses and rapid regional failover for a TCP gaming API.
- **Decisive words:** static anycast IPs, AWS global network, two Regions, no DNS wait
- **A:** CloudFront is a content delivery service and an S3-only distribution does not front the regional gaming API described.
- **B:** Correct. Global Accelerator provides static anycast IPs, AWS backbone routing, health checks, and rapid endpoint failover.
- **C:** A private hosted zone is not resolvable by public gaming clients and does not provide anycast IPs.
- **D:** Internet gateways enable VPC internet connectivity but do not create global static anycast addresses or health-based regional routing.
- **Reusable rule:** Choose Global Accelerator for static anycast ingress and fast health-based routing of non-cacheable regional endpoints.
- **Official reference:** [AWS](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

## SIM-A-48 — Answer C,D

- **Central requirement:** Increase CloudFront cache reuse and collapse duplicate origin fetches for newly published objects.
- **Decisive words:** many edge locations, same object, query strings fragment cache, origin load
- **A:** Zero TTL values force frequent revalidation or origin requests and defeat the caching goal.
- **B:** Forwarding unnecessary request values creates many cache variants and lowers the hit ratio.
- **C:** Correct. A minimal cache key increases the probability that equivalent requests share cached objects.
- **D:** Correct. Origin Shield consolidates origin requests through an additional regional cache layer.
- **E:** Direct S3 access removes edge caching and increases origin traffic.
- **Reusable rule:** Keep the CloudFront cache key minimal and consider Origin Shield when global misses should be consolidated before one origin.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html), [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html)

## SIM-A-49 — Answer D

- **Central requirement:** Provide consistent high-throughput hybrid connectivity with an encrypted backup path.
- **Decisive words:** steady 2 Gbps, consistent, private network, encrypted backup
- **A:** CloudFront serves HTTP content and cannot replace hybrid network routing.
- **B:** A gateway endpoint privately reaches supported AWS services from a VPC and is not a physical hybrid link.
- **C:** An internet gateway does not terminate private data-center routing or create dedicated connectivity.
- **D:** Correct. Direct Connect provides dedicated connectivity characteristics, and a VPN can supply an encrypted alternate path.
- **Reusable rule:** Use Direct Connect for a dedicated hybrid path and design VPN or additional Direct Connect redundancy according to recovery needs.
- **Official reference:** [AWS](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html), [AWS](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

## SIM-A-50 — Answer C

- **Central requirement:** Serve a low-latency stream consumer and a batched S3 analytics destination from ordered clickstream ingestion.
- **Decisive words:** real time, fraud consumer, same stream to S3, per-session order
- **A:** DNS records are not a clickstream ingestion platform and do not provide controlled per-session ordering.
- **B:** Deep Archive does not support low-latency event consumption and daily scanning misses the real-time requirement.
- **C:** Correct. Data Streams provides ordered partitioned ingestion and multiple consumers, while Firehose batches and delivers to S3.
- **D:** Competing consumers on one SQS queue divide work instead of reliably giving both destinations each event.
- **Reusable rule:** Use a partitioned stream for ordered multi-consumer ingestion and Firehose when managed buffering and delivery to S3 are required.
- **Official reference:** [AWS](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [AWS](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)

## SIM-A-51 — Answer B

- **Central requirement:** Identify the managed catalog and serverless ETL service for S3 datasets.
- **Decisive words:** discover schemas, central catalog, serverless ETL
- **A:** Shield Advanced protects applications from distributed denial-of-service attacks and does not catalog data.
- **B:** Correct. AWS Glue provides crawlers, the Data Catalog, and managed serverless ETL capabilities.
- **C:** Route 53 provides DNS and health-check capabilities rather than ETL processing.
- **D:** Certificate Manager manages TLS certificates and does not discover schemas or transform datasets.
- **Reusable rule:** Use AWS Glue when a data lake needs crawlers, shared catalog metadata, and managed ETL jobs.
- **Official reference:** [AWS](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)

## SIM-A-52 — Answer A,B,C

- **Central requirement:** Preserve scoped order while scaling Kinesis shard capacity and independent consumer throughput.
- **Decisive words:** per-customer order, several consumers, dedicated throughput, uneven growth
- **A:** Correct. Resharding or a suitable capacity mode adapts stream capacity to changing traffic.
- **B:** Correct. A stable customer key keeps that customer's records on the same ordered shard sequence.
- **C:** Correct. Enhanced fan-out gives registered consumers dedicated throughput per shard and lower propagation delay.
- **D:** Glacier is archival object storage and cannot provide low-latency streaming consumption.
- **E:** Random keys can split one customer's records across shards and lose the required ordering scope.
- **F:** One global key creates a hot shard and prevents horizontal partition throughput.
- **Reusable rule:** Align partition keys with the ordering scope, scale shard capacity, and isolate demanding consumers with enhanced fan-out.
- **Official reference:** [AWS](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html), [AWS](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html)

## SIM-A-53 — Answer A

- **Central requirement:** Reduce S3 report storage cost over time while preserving millisecond retrieval and resilient storage.
- **Decisive words:** daily thirty days, monthly to ninety, rarely, milliseconds
- **A:** Correct. The transitions match declining known access while preserving millisecond access and multi-AZ durability, subject to class minimums.
- **B:** Deep Archive retrieval normally takes hours and therefore violates the millisecond access requirement.
- **C:** One Zone-IA stores data in one Availability Zone and is unsuitable when the only compliance copy needs multi-AZ resilience.
- **D:** Lifecycle transitions preserve object access semantics and can reduce storage cost as access declines.
- **Reusable rule:** Choose lifecycle classes from access frequency, retrieval-time, resilience, and minimum-duration requirements together.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html)

## SIM-A-54 — Answer C

- **Central requirement:** Stop overprovisioning EBS capacity solely to obtain general-purpose SSD performance.
- **Decisive words:** capacity increased for IOPS, known IOPS and throughput, no io2 need
- **A:** Previous-generation magnetic volumes do not provide equivalent general-purpose SSD performance.
- **B:** io2 can provide higher durability and IOPS but may add unnecessary cost for the stated requirements.
- **C:** Correct. gp3 separates performance settings from capacity, avoiding gp2 overprovisioning solely for IOPS.
- **D:** S3 Glacier is object archive storage and cannot be attached as an EBS block device.
- **Reusable rule:** Use gp3 when general-purpose block workloads benefit from sizing capacity and performance independently.
- **Official reference:** [AWS](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html)

## SIM-A-55 — Answer D

- **Central requirement:** Lower the cost of inactive shared files while preserving the EFS interface.
- **Decisive words:** active two weeks, untouched for months, occasional access
- **A:** Throughput mode affects performance billing and does not make active EFS storage cheaper in this manner.
- **B:** Instance store is ephemeral and not a shared durable replacement for EFS.
- **C:** An EBS root volume cannot be mounted as one shared cross-AZ file system by all instances.
- **D:** Correct. EFS lifecycle management transparently moves inactive files to lower-cost storage classes.
- **Reusable rule:** Use EFS lifecycle policies when file access cools over time and applications should retain the same file-system interface.
- **Official reference:** [AWS](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

## SIM-A-56 — Answer D,E,F

- **Central requirement:** Distinguish S3 storage-class cost, retrieval, and resilience characteristics.
- **Decisive words:** One Zone, retrieval time, archive, minimum duration
- **A:** The frequent and infrequent automatic access tiers do not impose the claimed universal retrieval charge behavior.
- **B:** S3 Standard is designed for multi-AZ resilience rather than single-zone placement.
- **C:** Standard-IA includes retrieval and minimum-duration considerations that must be included in cost analysis.
- **D:** Correct. Glacier Instant Retrieval combines archive pricing characteristics with millisecond access.
- **E:** Correct. One Zone-IA costs less by using one Availability Zone, so data must be reproducible or tolerate that risk.
- **F:** Correct. Deep Archive targets very infrequent long-term retention with retrieval measured in hours.
- **Reusable rule:** Select an S3 class only after matching access frequency, retrieval latency, resilience, and minimum-duration economics.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

## SIM-A-57 — Answer B

- **Central requirement:** Minimize EC2 cost for checkpointed independent jobs that tolerate interruption.
- **Decisive words:** fault-tolerant, checkpoint, resume, variable, no fixed family
- **A:** On-Demand capacity is flexible but does not provide the lowest cost for interruption-tolerant batch work.
- **B:** Correct. Diversified Spot capacity fits interruption-tolerant, checkpointed jobs and reduces cost without a long-term type commitment.
- **C:** Dedicated Hosts add cost and are intended for licensing or isolation needs not stated here.
- **D:** A specific zonal reservation reduces flexibility and is premature for highly variable, diversified demand.
- **Reusable rule:** Use diversified Spot capacity for interruption-tolerant work and design the worker to checkpoint and resume safely.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html), [AWS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html)

## SIM-A-58 — Answer C

- **Central requirement:** Optimize steady, critical burst, and retryable batch compute with different pricing models.
- **Decisive words:** steady baseline, peaks cannot interrupt, retryable batch, families and Regions change
- **A:** Committing to the full peak and one zone wastes capacity and reduces the flexibility explicitly required.
- **B:** Dedicated Hosts introduce substantial cost without a stated compliance or licensing benefit.
- **C:** Correct. Compute Savings Plans preserve compute flexibility, On-Demand handles uncertain critical peaks, and Spot discounts tolerant batch work.
- **D:** Spot interruption can remove customer-facing baseline capacity and discarding requests is unacceptable.
- **Reusable rule:** Apply commitments to the stable baseline, On-Demand to uncertain critical demand, and Spot to interruption-tolerant capacity.
- **Official reference:** [AWS](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html), [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

## SIM-A-59 — Answer B

- **Central requirement:** Avoid idle compute cost for a short, stateless, hourly task.
- **Decisive words:** one minute every hour, no state, avoid idle servers
- **A:** A continuously running EC2 instance incurs idle cost and operating work between hourly executions.
- **B:** Correct. Lambda bills for requests and execution duration and removes idle server management for this short periodic task.
- **C:** A Dedicated Host is far more capacity and cost than the tiny stateless workload requires.
- **D:** Unused container hosts create the same idle-capacity problem the company wants to avoid.
- **Reusable rule:** For short intermittent stateless execution, compare serverless duration billing before provisioning always-on hosts.
- **Official reference:** [AWS](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

## SIM-A-60 — Answer A,D,F

- **Central requirement:** Reduce cost for a steady production database and business-hours development databases.
- **Decisive words:** oversized production, one-year commitment, development business hours
- **A:** Correct. A reservation can reduce cost for the stable, measured production baseline after rightsizing.
- **B:** Idle development databases continue to incur compute cost and are not required for the stated production commitment.
- **C:** Committing to an oversized shape locks in avoidable waste and reverses the correct optimization order.
- **D:** Correct. Stopping eligible development instances reduces idle compute charges, with schedules designed around service restart limits.
- **E:** Unneeded replicas add database instance and storage cost without solving a performance requirement.
- **F:** Correct. Rightsizing removes persistent unused capacity before applying any commitment.
- **Reusable rule:** Right-size first, commit only the stable baseline, and schedule nonproduction databases when service constraints allow.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html), [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html)

## SIM-A-61 — Answer A

- **Central requirement:** Select DynamoDB billing and scaling for an unpredictable new workload.
- **Decisive words:** unpredictable, no forecast, automatically, request-based billing
- **A:** Correct. On-demand mode automatically accommodates traffic and bills for read and write requests without capacity planning.
- **B:** An EC2 proxy adds cost and does not replace DynamoDB capacity mode selection.
- **C:** A fixed provisioned configuration without scaling can throttle unpredictable traffic and still requires forecasting.
- **D:** Glacier retrieval capacity is unrelated to DynamoDB table request processing.
- **Reusable rule:** Start with on-demand for unknown spiky DynamoDB demand and revisit provisioned economics when usage becomes predictable.
- **Official reference:** [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html)

## SIM-A-62 — Answer D

- **Central requirement:** Discount a stable long-running ElastiCache footprint without changing its architecture.
- **Decisive words:** stable size, three years, billing discount, preserve availability
- **A:** Self-managed Spot nodes alter operations and availability and do not preserve the managed replication-group behavior.
- **B:** Deep Archive cannot provide in-memory cache latency.
- **C:** Artificially increasing capacity raises total cost even if the discount percentage appears larger.
- **D:** Correct. Reserved nodes provide a billing discount for predictable, sustained ElastiCache usage without changing runtime behavior.
- **Reusable rule:** Use service reservations for a measured stable baseline, not as a reason to provision unnecessary capacity.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.Reserved.html)

## SIM-A-63 — Answer A

- **Central requirement:** Reduce global S3 delivery cost and latency without weakening private-origin authorization.
- **Decisive words:** global audience, origin transfer cost, tracking parameters, signed authorization
- **A:** Correct. CloudFront reduces repeated origin transfer, an intentional cache key improves reuse, and origin access control keeps S3 private.
- **B:** Manual instance-store replicas are ephemeral, operationally expensive, and lack managed global caching.
- **C:** Public S3 weakens access control, and an overbroad cache key reduces hits and cost efficiency.
- **D:** NAT gateways are VPC egress resources and cannot be deployed in viewer networks as a CDN.
- **Reusable rule:** Use CloudFront for cacheable global delivery, minimize the cache key safely, and keep the origin private with explicit origin authorization.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html), [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

## SIM-A-64 — Answer B,C,E

- **Central requirement:** Reduce NAT charges for AWS service traffic while retaining resilient egress for remaining internet destinations.
- **Decisive words:** heavy S3 DynamoDB Secrets Manager, small internet traffic, no single zonal dependency
- **A:** The application still requires limited general internet egress, so removing every path breaks a stated requirement.
- **B:** Correct. Gateway endpoints remove supported S3 and DynamoDB traffic from NAT processing without hourly endpoint charges.
- **C:** Correct. A Secrets Manager interface endpoint keeps API calls private and avoids NAT for that service.
- **D:** Centralizing heavy service traffic through one NAT increases processing and cross-AZ exposure rather than reducing it.
- **E:** Correct. Per-AZ or otherwise resilient same-AZ NAT routing preserves zonal egress for traffic that truly needs internet translation.
- **F:** An Application Load Balancer cannot proxy arbitrary Secrets Manager control-plane calls and would expose unnecessary public infrastructure.
- **Reusable rule:** Use VPC endpoints for supported AWS services and reserve zonally resilient NAT capacity for destinations that actually require internet egress.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html), [AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html), [AWS](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html)

## SIM-A-65 — Answer B

- **Central requirement:** Reduce cross-AZ NAT cost and remove a single-zonal egress dependency.
- **Decisive words:** three Availability Zones, one NAT, cross-AZ charges, zonal dependency
- **A:** Concentrating all compute in one zone sacrifices application resilience and does not meet the multi-AZ design intent.
- **B:** Correct. Same-AZ NAT routing avoids unnecessary cross-AZ traversal and removes dependence on one zonal NAT gateway.
- **C:** An S3 website endpoint cannot perform general outbound network address translation.
- **D:** An internet gateway does not provide source translation for private instances without public addresses.
- **Reusable rule:** For resilient NAT gateway egress, deploy per Availability Zone and route private subnets to their local zonal gateway.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html), [AWS](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-basics.html)
