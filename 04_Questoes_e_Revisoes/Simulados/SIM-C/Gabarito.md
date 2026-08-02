# SIM-C — Commented answer key

**Navigation:** [Questions](Questoes.md) | [Commented answer key](Gabarito.md) | [Result report](Relatorio.md)

Open this file only after completing the timed attempt.

## Quick answer table

| ID | Answer | Domain | Task |
|---|---|---:|---:|
| SIM-C-01 | A | 1 | 1.1 |
| SIM-C-02 | B | 1 | 1.1 |
| SIM-C-03 | C | 1 | 1.1 |
| SIM-C-04 | A,B | 1 | 1.1 |
| SIM-C-05 | D | 1 | 1.1 |
| SIM-C-06 | A | 1 | 1.1 |
| SIM-C-07 | B | 1 | 1.1 |
| SIM-C-08 | A,C | 1 | 1.2 |
| SIM-C-09 | C | 1 | 1.2 |
| SIM-C-10 | D | 1 | 1.2 |
| SIM-C-11 | A | 1 | 1.2 |
| SIM-C-12 | A,D | 1 | 1.2 |
| SIM-C-13 | B | 1 | 1.2 |
| SIM-C-14 | C | 1 | 1.2 |
| SIM-C-15 | D | 1 | 1.3 |
| SIM-C-16 | A,E | 1 | 1.3 |
| SIM-C-17 | A | 1 | 1.3 |
| SIM-C-18 | B | 1 | 1.3 |
| SIM-C-19 | C | 1 | 1.3 |
| SIM-C-20 | B,C | 1 | 1.3 |
| SIM-C-21 | D | 2 | 2.1 |
| SIM-C-22 | A | 2 | 2.1 |
| SIM-C-23 | B | 2 | 2.1 |
| SIM-C-24 | B,D | 2 | 2.1 |
| SIM-C-25 | C | 2 | 2.1 |
| SIM-C-26 | D | 2 | 2.1 |
| SIM-C-27 | A | 2 | 2.1 |
| SIM-C-28 | B,E | 2 | 2.1 |
| SIM-C-29 | B | 2 | 2.1 |
| SIM-C-30 | C | 2 | 2.2 |
| SIM-C-31 | D | 2 | 2.2 |
| SIM-C-32 | C,D | 2 | 2.2 |
| SIM-C-33 | A | 2 | 2.2 |
| SIM-C-34 | B | 2 | 2.2 |
| SIM-C-35 | C | 2 | 2.2 |
| SIM-C-36 | C,E | 2 | 2.2 |
| SIM-C-37 | D | 2 | 2.2 |
| SIM-C-38 | A | 3 | 3.1 |
| SIM-C-39 | B | 3 | 3.1 |
| SIM-C-40 | D,E | 3 | 3.1 |
| SIM-C-41 | C | 3 | 3.2 |
| SIM-C-42 | D | 3 | 3.2 |
| SIM-C-43 | A | 3 | 3.2 |
| SIM-C-44 | A,B | 3 | 3.3 |
| SIM-C-45 | B | 3 | 3.3 |
| SIM-C-46 | C | 3 | 3.3 |
| SIM-C-47 | D | 3 | 3.4 |
| SIM-C-48 | C,D | 3 | 3.4 |
| SIM-C-49 | A | 3 | 3.4 |
| SIM-C-50 | B | 3 | 3.5 |
| SIM-C-51 | C | 3 | 3.5 |
| SIM-C-52 | A,B,C | 3 | 3.5 |
| SIM-C-53 | D | 4 | 4.1 |
| SIM-C-54 | A | 4 | 4.1 |
| SIM-C-55 | B | 4 | 4.1 |
| SIM-C-56 | A,D,E | 4 | 4.1 |
| SIM-C-57 | C | 4 | 4.2 |
| SIM-C-58 | D | 4 | 4.2 |
| SIM-C-59 | A | 4 | 4.2 |
| SIM-C-60 | B,D,F | 4 | 4.3 |
| SIM-C-61 | B | 4 | 4.3 |
| SIM-C-62 | C | 4 | 4.3 |
| SIM-C-63 | D | 4 | 4.4 |
| SIM-C-64 | C,E,F | 4 | 4.4 |
| SIM-C-65 | A | 4 | 4.4 |

## SIM-C-01 — Answer A

- **Central requirement:** Determine the effect of an applicable explicit deny during IAM policy evaluation.
- **Decisive words:** identity allow, bucket explicit deny, authorization result
- **A:** Correct. An explicit deny in any applicable policy overrides identity-based allows during authorization evaluation.
- **B:** Incorrect. Identity policies do not override an applicable explicit deny in a resource policy.
- **C:** Incorrect. The encryption method does not change the explicit-deny result for the S3 API authorization.
- **D:** Incorrect. IAM policy evaluation is synchronous and does not retry denied application requests.
- **Reusable rule:** An applicable explicit deny wins over any allow; boundaries and SCPs can further limit but never grant permissions.
- **Official reference:** [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)

## SIM-C-02 — Answer B

- **Central requirement:** Provide temporary cross-account incident access controlled by the destination account.
- **Decisive words:** two hours, no IAM users, workload account controls entry
- **A:** Incorrect. Root credentials must not be distributed, and storage in Secrets Manager does not make them temporary or least privilege.
- **B:** Correct. The destination trust policy and temporary STS session satisfy cross-account control without long-lived credentials.
- **C:** Incorrect. Public sharing violates the security requirement and names do not provide authorization.
- **D:** Incorrect. An SCP sets permission guardrails and cannot grant cross-account resource access.
- **Reusable rule:** For cross-account operations, use a destination role trust policy plus caller permission to assume the role and short STS sessions.
- **Official reference:** [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html)

## SIM-C-03 — Answer C

- **Central requirement:** Centralize routine workforce access while preserving a constrained and audited emergency path.
- **Decisive words:** Identity Center, central revocation, emergency role, short sessions
- **A:** Incorrect. Cognito user pools authenticate application users and do not replace workforce AWS account permission sets.
- **B:** Incorrect. Distributed long-lived administrator keys increase attack surface and make centralized revocation difficult.
- **C:** Correct. This separates routine centralized access from a constrained, auditable emergency path with temporary credentials.
- **D:** Incorrect. Removing accounts from governance weakens centralized response and does not create a safe break-glass design.
- **Reusable rule:** Use Identity Center permission sets for workforce access and design break-glass roles as exceptional, temporary, MFA-protected, and heavily monitored.
- **Official reference:** [AWS](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

## SIM-C-04 — Answer A,B

- **Central requirement:** Prevent privilege escalation while permitting delegated role creation under a fixed ceiling.
- **Decisive words:** compromised deployment role, create roles, approved ceiling
- **A:** Correct. A permissions boundary limits the maximum permissions an identity policy can produce for each created role.
- **B:** Correct. Conditional IAM permissions can require and constrain the boundary used during role creation.
- **C:** Incorrect. Resource names do not make administrator permissions safe and this enables privilege escalation.
- **D:** Incorrect. Encryption protects storage but does not reduce the permissions or escalation path.
- **E:** Incorrect. A dashboard is observational and cannot enforce IAM authorization limits.
- **Reusable rule:** Delegated IAM administration requires both a permissions boundary on created identities and caller permissions that enforce the approved boundary.
- **Official reference:** [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)

## SIM-C-05 — Answer D

- **Central requirement:** Create a single protected global edge while preventing clients from bypassing private origins.
- **Decisive words:** global storefront, private S3, direct URLs, centralized Layer 7
- **A:** Incorrect. Direct origin routing violates the single-edge and private-origin requirements and provides no centralized WAF point.
- **B:** Incorrect. Public bucket access bypasses CloudFront and security groups cannot inspect application payloads for SQL injection.
- **C:** Incorrect. NAT Gateways provide egress translation, and network ACLs cannot inspect URL or HTTP payload content.
- **D:** Correct. OAC keeps the bucket private, CloudFront becomes the public edge, and WAF filters supported web requests centrally.
- **Reusable rule:** For private global delivery, make CloudFront the public entry point, authorize origin access explicitly, and attach WAF at the shared edge.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

## SIM-C-06 — Answer A

- **Central requirement:** Identify the credential model that automatically expires and avoids long-lived keys.
- **Decisive words:** one hour, command-line, expire automatically
- **A:** Correct. STS credentials include an expiration and avoid permanent IAM user access keys.
- **B:** Incorrect. Encryption at rest does not make an IAM user key temporary or automatically expiring.
- **C:** Incorrect. Root access keys are long lived and must not be used for routine command-line access.
- **D:** Incorrect. A presigned URL authorizes a specific request and is not a general AWS credential set.
- **Reusable rule:** Use role-based STS sessions for human and workload access whenever permanent access keys are unnecessary.
- **Official reference:** [AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

## SIM-C-07 — Answer B

- **Central requirement:** Authenticate consumer users and issue temporary, prefix-scoped AWS credentials for direct uploads.
- **Decisive words:** social identities, MFA, direct S3, user-specific prefix
- **A:** Incorrect. Millions of IAM users and long-lived keys are unsafe and create excessive credential operations.
- **B:** Correct. User pools handle customer authentication while identity pools vend temporary AWS credentials governed by role policies.
- **C:** Incorrect. A public bucket does not enforce authenticated user-to-prefix isolation.
- **D:** Incorrect. Identity Center targets workforce access to AWS accounts, not high-scale customer application authentication.
- **Reusable rule:** Use Cognito user pools for application authentication and identity pools when clients also need temporary scoped AWS credentials.
- **Official reference:** [AWS](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html)

## SIM-C-08 — Answer A,C

- **Central requirement:** Manage rotating database credentials and absorb serverless connection bursts.
- **Decisive words:** Lambda bursts, RDS password rotation, connection storms
- **A:** Correct. Secrets Manager supports managed rotation and controlled programmatic retrieval of the current credential.
- **B:** Incorrect. Embedded duplicate credentials increase exposure and require deployment coordination instead of managed rotation.
- **C:** Correct. RDS Proxy pools connections and can obtain database credentials from Secrets Manager.
- **D:** Incorrect. Longer function timeouts do not pool connections or coordinate credential rotation.
- **E:** Incorrect. Public subnet placement does not grant Lambda public IPs and does not solve database connection pressure.
- **Reusable rule:** For Lambda-to-RDS workloads, combine Secrets Manager rotation with RDS Proxy connection pooling when supported.
- **Official reference:** [AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)

## SIM-C-09 — Answer C

- **Central requirement:** Add a principal- and resource-aware control at the private service endpoint.
- **Decisive words:** interface endpoint, one role, selected secrets, additional policy
- **A:** Incorrect. Network ACLs filter IP protocol fields and cannot evaluate IAM principal ARNs.
- **B:** Incorrect. Route tables cannot filter API principals or secret ARNs, and an internet path weakens the stated design.
- **C:** Correct. Endpoint policies can constrain which principals and resources may use the private endpoint in addition to normal authorization.
- **D:** Incorrect. Secrets Manager requires secure API access, and removing TLS would not create principal-aware authorization.
- **Reusable rule:** VPC endpoint policies are defense in depth; they narrow endpoint use but do not replace IAM and resource-policy authorization.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html)

## SIM-C-10 — Answer D

- **Central requirement:** Combine centralized security findings, event-driven containment, and contextual investigation.
- **Decisive words:** GuardDuty high severity, centralized, automatic isolation, related entities
- **A:** Incorrect. CPU is not a reliable credential-exfiltration signal and broad termination is unsafe remediation.
- **B:** Incorrect. Config state snapshots are not a timely threat-finding or automated response pipeline.
- **C:** Incorrect. Artifact distributes compliance documents, while Macie discovers sensitive data in S3 rather than isolating compute.
- **D:** Correct. The services cover centralized findings, event-driven response, and contextual investigation as separate managed capabilities.
- **Reusable rule:** Use purpose-built stages: detection and aggregation, EventBridge-driven idempotent response, then Detective investigation of linked activity.
- **Official reference:** [AWS](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)

## SIM-C-11 — Answer A

- **Central requirement:** Identify the stateful return-traffic behavior of EC2 security groups.
- **Decisive words:** inbound HTTPS allowed, response packets, outbound rule
- **A:** Correct. State tracking permits return traffic for an established allowed flow regardless of a matching outbound rule.
- **B:** Incorrect. That describes network ACL behavior rather than security-group connection tracking.
- **C:** Incorrect. Security groups contain allow rules and do not use ordered explicit deny entries.
- **D:** Incorrect. Security groups filter connection properties and do not inspect HTTP methods.
- **Reusable rule:** Security groups are stateful allow lists; network ACLs are stateless ordered subnet filters.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)

## SIM-C-12 — Answer A,D

- **Central requirement:** Enforce a private API network path and resource-level caller restrictions.
- **Decisive words:** private REST API, one VPC endpoint, approved organization accounts
- **A:** Correct. A private API is reached through an execute-api VPC endpoint rather than a public endpoint type.
- **B:** Incorrect. NAT provides outbound internet reachability and would not eliminate the public invocation path.
- **C:** Incorrect. API keys identify usage and are not authorization controls for private principals.
- **D:** Correct. The resource policy can deny calls outside the expected private endpoint and principal boundary.
- **E:** Incorrect. S3 gateway endpoints are service-specific and cannot carry API Gateway execute-api traffic.
- **Reusable rule:** A private API design requires the private endpoint type plus a resource policy that constrains endpoint and principal context.
- **Official reference:** [AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)

## SIM-C-13 — Answer B

- **Central requirement:** Centrally enforce Layer 7 controls across accounts and add enhanced DDoS protection where justified.
- **Decisive words:** fifty accounts, zero-day pattern, within minutes, DDoS response
- **A:** Incorrect. Security groups cannot inspect HTTP content and decentralized manual updates will not meet the time objective.
- **B:** Correct. Firewall Manager centralizes supported policies across accounts, while Shield Advanced provides enhanced DDoS capabilities for protected resources.
- **C:** Incorrect. NAT Gateways do not proxy inbound traffic and network ACLs cannot inspect request bodies.
- **D:** Incorrect. Inspector detects workload vulnerabilities and is not an inline Layer 7 request control.
- **Reusable rule:** At organization scale, centralize WAF policy with Firewall Manager and separately evaluate Shield Advanced for high-value DDoS requirements.
- **Official reference:** [AWS](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-firewall-manager.html)

## SIM-C-14 — Answer C

- **Central requirement:** Map API authorship, resource state, and application impact to the correct evidence sources.
- **Decisive words:** who changed, configuration over time, error metrics
- **A:** Incorrect. Artifact supplies compliance documents and Access Analyzer reasons about external or unused access, not latency.
- **B:** Incorrect. These assignments reverse service responsibilities and Config does not capture packet payloads.
- **C:** Correct. Each service supplies the audit, state, and behavior evidence requested by the incident review.
- **D:** Incorrect. Flow Logs provide network metadata, not management API identity or full configuration history.
- **Reusable rule:** CloudTrail answers who called an API, Config answers how a resource was configured, and CloudWatch answers how the system behaved.
- **Official reference:** [AWS](https://docs.aws.amazon.com/pdfs/decision-guides/latest/cloudtrail-or-cloudwatch/cloudtrail-or-cloudwatch.pdf)

## SIM-C-15 — Answer D

- **Central requirement:** Enforce administrator-resistant fixed retention for regulated S3 object versions.
- **Decisive words:** seven years, administrators unable to shorten, immutability
- **A:** Incorrect. An unversioned public destination is neither immutable nor appropriately secured.
- **B:** Incorrect. Lifecycle controls transition or expiration but does not provide immutable compliance retention against administrators.
- **C:** Incorrect. MFA Delete adds a deletion control but does not enforce an unshortenable fixed retention period.
- **D:** Correct. Compliance mode prevents protected object versions from deletion or retention shortening, including by the root user, during the retention period.
- **Reusable rule:** For WORM compliance that no user can shorten, use S3 Object Lock compliance mode on a versioned bucket and protect the surrounding lifecycle.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)

## SIM-C-16 — Answer A,E

- **Central requirement:** Identify the data-key generation and storage steps in envelope encryption.
- **Decisive words:** large files, KMS protects key material, client-side
- **A:** Correct. The plaintext data key performs efficient bulk encryption outside KMS.
- **B:** Incorrect. KMS cryptographic APIs are not designed for bulk payload encryption and impose size limits.
- **C:** Incorrect. Persisting plaintext key material exposes the protected data and defeats envelope encryption.
- **D:** Incorrect. An SCP is an authorization guardrail and is not cryptographic key material.
- **E:** Correct. The encrypted data key is safe to retain for later KMS decryption while plaintext key material should be removed.
- **Reusable rule:** Envelope encryption uses a plaintext data key briefly for bulk data and stores only its KMS-encrypted copy with the ciphertext.
- **Official reference:** [AWS](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping)

## SIM-C-17 — Answer A

- **Central requirement:** Protect both independent network hops with the appropriate certificate mechanisms.
- **Decisive words:** ALB client TLS, managed renewal, RDS encrypted sessions, validate CA
- **A:** Correct. ACM manages the public edge certificate while database TLS and CA validation protect the separate backend connection.
- **B:** Incorrect. A VPC boundary does not satisfy the explicit encryption requirement for the database hop.
- **C:** Incorrect. Disabling validation permits impersonation and creates unnecessary certificate operations.
- **D:** Incorrect. Presigned URLs authorize S3 requests and do not provide TLS certificates for ALB or RDS.
- **Reusable rule:** Treat each termination point as a separate TLS hop: ACM for supported public endpoints and validated database TLS for the backend.
- **Official reference:** [AWS](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)

## SIM-C-18 — Answer B

- **Central requirement:** Enable local regional decryption with related key material and independently governed policies.
- **Decisive words:** regional outage, decrypt locally, equivalent key identifiers, independent policies
- **A:** Incorrect. Single-Region keys cannot be used through another Region's KMS endpoint and create the prohibited dependency.
- **B:** Correct. Related multi-Region keys share key material and key ID while retaining independent regional policies and service endpoints.
- **C:** Incorrect. AWS managed keys do not accept customer imports, and exporting protected key material this way is unsupported.
- **D:** Incorrect. Removing encryption violates the stated protection requirement.
- **Reusable rule:** Use KMS multi-Region keys only when interoperable regional key material is required; policies and grants remain regional.
- **Official reference:** [AWS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html)

## SIM-C-19 — Answer C

- **Central requirement:** Discover sensitive S3 data with controlled classification scope and recurring cost.
- **Decisive words:** S3 objects, personal data, new high-risk prefixes, cost
- **A:** Incorrect. GuardDuty detects threats from security signals and does not perform content classification of S3 objects.
- **B:** Incorrect. Inspector assesses supported compute and code workloads for vulnerabilities, not personal-data content in S3.
- **C:** Correct. Macie is purpose-built for sensitive-data discovery in S3 and supports scoped classification jobs to control coverage and cost.
- **D:** Incorrect. Manual exfiltration is insecure, operationally unscalable, and inconsistent with recurring managed discovery.
- **Reusable rule:** Use Macie for S3 sensitive-data discovery and narrow job scope or sampling to the risk and cost objective.
- **Official reference:** [AWS](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)

## SIM-C-20 — Answer B,C

- **Central requirement:** Authorize and configure cross-account, cross-Region replication of SSE-KMS objects.
- **Decisive words:** encrypted objects fail, replication role, destination key
- **A:** Incorrect. AWS managed keys cannot generally be shared and administered for this cross-account replication design.
- **B:** Correct. The replication principal needs cryptographic authorization on both sides of the encrypted transfer.
- **C:** Correct. SSE-KMS replication must be explicitly selected and a valid destination encryption key configured.
- **D:** Incorrect. Public bucket access does not grant KMS permissions and creates severe exposure.
- **E:** Incorrect. A NAT Gateway changes network translation and cannot authorize S3 or KMS operations.
- **Reusable rule:** SSE-KMS replication requires rule opt-in, a destination key, and role/key-policy permissions to decrypt source and encrypt destination.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-config-for-kms-objects.html)

## SIM-C-21 — Answer D

- **Central requirement:** Recognize the delivery behavior that explains redelivery after processing but before delete.
- **Decisive words:** SQS Standard, crash before delete, delivered again
- **A:** Incorrect. Standard queues provide best-effort ordering and do not guarantee one global order.
- **B:** Incorrect. SQS does not atomically coordinate arbitrary database commits with message deletion.
- **C:** Incorrect. A repeated delivery is consistent with Standard queue behavior rather than corruption.
- **D:** Correct. Standard queues can redeliver a message, so business effects must tolerate repeated processing.
- **Reusable rule:** Treat Standard queue consumers as idempotent because acknowledgement and external business commits are not one atomic transaction.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html)

## SIM-C-22 — Answer A

- **Central requirement:** Route heterogeneous events to independently operated consumers without producer endpoint coupling.
- **Decisive words:** different JSON shapes, filtered subsets, independent retry, producers unaware
- **A:** Correct. EventBridge decouples producers, routes by event content, and lets each target have independent retry and DLQ configuration.
- **B:** Incorrect. A shared host and file create a single point of failure, polling, and tight operational coupling.
- **C:** Incorrect. Synchronous fan-out couples producer latency and availability to every consumer.
- **D:** Incorrect. Competing consumers on one queue divide messages rather than give each consumer an independent copy.
- **Reusable rule:** Use an event bus and content rules for many-to-many event routing; give each consumer its own target or durable buffer.
- **Official reference:** [AWS](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)

## SIM-C-23 — Answer B

- **Central requirement:** Orchestrate a durable multi-step serverless transaction with waits and compensation.
- **Decisive words:** bursts, five-minute wait, compensation, audit trail
- **A:** Incorrect. A synchronous client request is fragile and does not provide durable orchestration or compensation state.
- **B:** Correct. Standard workflows durably track long-running state transitions and model wait, retry, and compensation logic explicitly.
- **C:** Incorrect. SNS distributes messages but does not maintain per-reservation workflow state or branching.
- **D:** Incorrect. Lambda execution environments are ephemeral and cannot provide durable cross-invocation state.
- **Reusable rule:** Use Step Functions Standard for durable, auditable workflows with long waits, retries, branching, and compensation.
- **Official reference:** [AWS](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

## SIM-C-24 — Answer B,D

- **Central requirement:** Bound target delivery retries and retain exhausted events for controlled recovery.
- **Decisive words:** target throttles, bounded retry, preserved, replay
- **A:** Incorrect. EC2 block storage has no role in EventBridge target delivery reliability.
- **B:** Correct. The target retry policy bounds how long and how often EventBridge retries retryable delivery failures.
- **C:** Incorrect. Disabling retries increases event loss risk and does not meet the preservation requirement.
- **D:** Correct. The target DLQ preserves events that cannot be delivered after the retry policy is exhausted.
- **E:** Incorrect. A dashboard visualizes metrics and does not durably store undelivered event payloads.
- **Reusable rule:** For EventBridge target reliability, configure a retry policy and an authorized SQS DLQ; keep consumers idempotent.
- **Official reference:** [AWS](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-dlq.html)

## SIM-C-25 — Answer C

- **Central requirement:** Absorb bursts, protect a constrained dependency, handle duplicates, and isolate poison work.
- **Decisive words:** unpredictable uploads, duplicate events, 50 concurrent, poison images
- **A:** Incorrect. Unbounded concurrency can overload the API, while object deletion loses recoverable evidence.
- **B:** Incorrect. Client-side synchronous retries tightly couple uploads to the dependency and provide no durable poison-message handling.
- **C:** Correct. The queue buffers bursts, concurrency protects the dependency, idempotency handles duplicates, and redrive isolates poison work.
- **D:** Incorrect. The design has a single failure domain, high delay, and ephemeral checkpoint state.
- **Reusable rule:** Buffer asynchronous serverless work in SQS, bound consumer concurrency, make effects idempotent, and design an observable redrive path.
- **Official reference:** [AWS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)

## SIM-C-26 — Answer D

- **Central requirement:** Choose the FIFO message-group scope that preserves only required ordering.
- **Decisive words:** same customer ordered, different customers concurrent
- **A:** Incorrect. The queue URL identifies the queue and does not define independent ordered message groups.
- **B:** Incorrect. One global group serializes all messages and removes the desired cross-customer concurrency.
- **C:** Incorrect. Random groups permit same-customer orders to be processed concurrently and lose required ordering.
- **D:** Correct. FIFO ordering is enforced within each message group, so per-customer groups preserve the required scope of ordering.
- **Reusable rule:** Set MessageGroupId to the smallest business entity that requires ordering; excessive grouping reduces FIFO parallelism.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html)

## SIM-C-27 — Answer A

- **Central requirement:** Provide high-throughput ordered stream retention and independent consumer replay.
- **Decisive words:** hundreds of thousands, ordered records, independent checkpoints, replay
- **A:** Correct. Kinesis provides an ordered retained log per shard and supports multiple consumers with independent positions.
- **B:** Incorrect. Competing consumers divide messages, so each analytics application would not receive the complete record stream.
- **C:** Incorrect. SNS alone does not provide the retained replay log and per-consumer checkpoints requested.
- **D:** Incorrect. Instance store is ephemeral, host-bound, and not a scalable multi-consumer streaming backbone.
- **Reusable rule:** Choose a retained stream such as Kinesis when multiple consumers need ordered partitions and independent replay positions.
- **Official reference:** [AWS](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

## SIM-C-28 — Answer B,E

- **Central requirement:** Fan out DynamoDB changes to consumers with independent durability and retry behavior.
- **Decisive words:** three independent consumers, retry without blocking, item changes
- **A:** Incorrect. Sequential synchronous fan-out couples failure and latency across independent consumers.
- **B:** Correct. DynamoDB Streams records item-level changes and preserves order for modifications to the same item.
- **C:** Incorrect. Public access is unnecessary and polling partitions is inefficient and insecure.
- **D:** Incorrect. Lambda temporary storage is execution-environment local and cannot provide a durable shared event history.
- **E:** Correct. Independent queues give each consumer its own backlog, retry pace, and failure isolation.
- **Reusable rule:** Use DynamoDB Streams as the change source, then fan out into one durable buffer per independent consumer when failure isolation matters.
- **Official reference:** [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html)

## SIM-C-29 — Answer B

- **Central requirement:** Decouple long-running processing from the client request and provide durable status.
- **Decisive words:** forty minutes, immediate ID, client disconnect, queryable status
- **A:** Incorrect. Long synchronous waits exceed common integration limits and couple completion to client connectivity.
- **B:** Correct. An asynchronous job pattern decouples client lifetime from processing and provides durable status tracking.
- **C:** Incorrect. Standard Lambda functions have a maximum execution duration below forty minutes.
- **D:** Incorrect. Client-local state is not durable server-side work and can cause duplicate uncontrolled submissions.
- **Reusable rule:** For long asynchronous work, acknowledge quickly, queue durably, process independently, and expose persisted job status.
- **Official reference:** [AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/async-request-reply.html)

## SIM-C-30 — Answer C

- **Central requirement:** Meet aggressive regional RPO/RTO for a serverless API without unsafe write behavior.
- **Decisive words:** regional outage, seconds RPO, under five minutes, conflict-safe
- **A:** Incorrect. Multi-AZ improves Availability Zone resilience within one Region and is not cross-Region recovery.
- **B:** Incorrect. Nightly backups and manual changes cannot meet seconds of RPO or a five-minute RTO.
- **C:** Correct. Global tables replicate with low latency, while dual deployments and health routing meet rapid regional recovery when write semantics are designed safely.
- **D:** Incorrect. Uncoordinated dual writes create partial failure and conflict risks and shift recovery complexity to clients.
- **Reusable rule:** Global active-active data requires both replication technology and an application data model that tolerates concurrent regional writes.
- **Official reference:** [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)

## SIM-C-31 — Answer D

- **Central requirement:** Identify the metric that represents maximum acceptable data loss in time.
- **Decisive words:** lose data, fifteen minutes, disaster
- **A:** Incorrect. Release cadence does not define disaster-recovery data-loss tolerance.
- **B:** Incorrect. RTO measures how long service restoration may take, not how much committed data may be lost.
- **C:** Incorrect. MTBF describes reliability frequency and does not set an acceptable recovery data point.
- **D:** Correct. RPO measures the maximum acceptable amount of data loss expressed as time before the disruption.
- **Reusable rule:** RPO answers how much data can be lost; RTO answers how long the service can remain unavailable.
- **Official reference:** [AWS](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html)

## SIM-C-32 — Answer C,D

- **Central requirement:** Provide zonal redundancy and application-aware instance replacement.
- **Decisive words:** Availability Zone fails, ALB, application health checks
- **A:** Incorrect. One subnet belongs to one Availability Zone and leaves a zonal single point of failure.
- **B:** Incorrect. EC2 checks detect infrastructure health but do not validate the application's target response.
- **C:** Correct. Multi-AZ placement preserves load-balancer and compute capacity after a zonal failure.
- **D:** Correct. ELB health integration lets Auto Scaling replace instances that fail application target health.
- **E:** Incorrect. A single registered target undermines the availability and scaling requirements.
- **Reusable rule:** For resilient EC2 fleets, distribute load balancer and Auto Scaling capacity across AZs and feed target health into replacement decisions.
- **Official reference:** [AWS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html)

## SIM-C-33 — Answer A

- **Central requirement:** Provide low-lag cross-Region relational replication, local reads, and rapid managed promotion.
- **Decisive words:** Aurora, second Region reads, low lag, managed promotion
- **A:** Correct. Aurora global databases provide cross-Region storage replication, local secondary reads, and managed promotion workflows.
- **B:** Incorrect. Post-incident snapshot copying and restore cannot meet low-lag replication or rapid recovery.
- **C:** Incorrect. Multi-AZ protects against zonal failures and does not create a readable cross-Region cluster.
- **D:** Incorrect. Log delivery is not a supported relational replication or promotion mechanism.
- **Reusable rule:** Choose Aurora global database when relational workloads require cross-Region read locality and low-RPO regional recovery, then test promotion and routing.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

## SIM-C-34 — Answer B

- **Central requirement:** Automatically create cross-account, cross-Region copies of newly uploaded S3 objects.
- **Decisive words:** S3 originals, regional outage, recovery account, asynchronous
- **A:** Incorrect. Lifecycle transition changes storage class and does not create a cross-Region recovery copy.
- **B:** Correct. CRR asynchronously copies eligible new object versions across Regions and can target another account with the required permissions.
- **C:** Incorrect. EBS Multi-Attach is regional block storage behavior and cannot mount or replicate an S3 bucket.
- **D:** Incorrect. DNS routing cannot make unavailable regional object data exist in another Region.
- **Reusable rule:** Use S3 replication for asynchronous object copies, and remember versioning, role permissions, ownership, and KMS settings when applicable.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

## SIM-C-35 — Answer C

- **Central requirement:** Select a DR strategy that meets tight recovery objectives without full duplicate capacity.
- **Decisive words:** ten-minute RTO, under one-minute RPO, reduced capacity, cost
- **A:** Incorrect. A pilot-light-like control plane without required core data and services would miss the aggressive recovery objectives.
- **B:** Incorrect. Weekly backups and restore provisioning cannot meet the stated RPO or ten-minute RTO.
- **C:** Correct. Warm standby keeps a functional reduced environment and can scale quickly, fitting tighter objectives at lower cost than full active-active.
- **D:** Incorrect. Active-active may meet recovery goals but conflicts with the requirement to avoid full duplicate capacity.
- **Reusable rule:** Warm standby is a functional scaled-down regional copy; match strategy cost to measured RTO/RPO and rehearse scaling and routing.
- **Official reference:** [AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

## SIM-C-36 — Answer C,E

- **Central requirement:** Identify the DNS record roles and health signal needed for automated failover.
- **Decisive words:** Route 53, primary, secondary, automatic failover
- **A:** Incorrect. Simple routing does not define primary and secondary failover roles.
- **B:** Incorrect. A network ACL filters subnet traffic and does not provide Route 53 endpoint health evaluation.
- **C:** Correct. The paired record roles tell Route 53 which answer is primary and which is the failover destination.
- **D:** Incorrect. TTL affects resolver caching but cannot detect that the primary endpoint is unhealthy.
- **E:** Correct. Route 53 needs health information to stop returning an unhealthy primary endpoint automatically.
- **Reusable rule:** DNS failover requires explicit failover records plus trustworthy health evaluation; TTL tunes convergence but does not detect failure.
- **Official reference:** [AWS](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html)

## SIM-C-37 — Answer D

- **Central requirement:** Centralize protected backup retention outside compromised workload administration.
- **Decisive words:** ransomware, member accounts, immutable vault, cross-account
- **A:** Incorrect. Termination protection does not create recovery points and can be disabled by authorized principals.
- **B:** Incorrect. Manual same-account snapshots lack centralized enforcement and remain exposed to compromised workload administrators.
- **C:** Incorrect. CloudTrail records API activity and does not contain recoverable database or volume data.
- **D:** Correct. AWS Backup centralizes supported resource policies and vault governance while cross-account copies reduce compromise of the workload account.
- **Reusable rule:** For cyber-resilient backups, separate backup administration and copies from workload accounts, enforce retention, and regularly test restores.
- **Official reference:** [AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

## SIM-C-38 — Answer A

- **Central requirement:** Optimize tightly coupled HPC compute, network fabric, and parallel storage together.
- **Decisive words:** MPI, low latency, high bandwidth, shared parallel file
- **A:** Correct. Cluster placement, EFA, and a parallel file system address tightly coupled network latency and high-throughput shared storage.
- **B:** Incorrect. Cross-Region distance and archival retrieval latency conflict with tightly coupled computation.
- **C:** Incorrect. Lambda and API Gateway do not provide the required low-latency tightly coupled network fabric.
- **D:** Incorrect. Spread placement prioritizes failure isolation rather than the lowest inter-node latency, and file storage is not the MPI network.
- **Reusable rule:** For tightly coupled HPC, co-design instance type, cluster placement, EFA networking, and a high-throughput parallel file system.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html)

## SIM-C-39 — Answer B

- **Central requirement:** Handle both predictable and unpredictable demand without permanent peak capacity.
- **Decisive words:** weekday 09:00, promotions, ready before, automatic response
- **A:** Incorrect. Permanent peak capacity wastes cost and still lacks policy-driven adaptation.
- **B:** Correct. Scheduled actions pre-position capacity, while target tracking adapts to unplanned changes around the baseline.
- **C:** Incorrect. Scale-in protection prevents selected termination and does not add capacity during demand.
- **D:** Incorrect. IAM user count is unrelated to real-time web request demand.
- **Reusable rule:** Combine proactive scheduled or predictive capacity for known patterns with dynamic policies tied to a workload-relevant metric.
- **Official reference:** [AWS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)

## SIM-C-40 — Answer D,E

- **Central requirement:** Provide static global entry addresses and health-aware routing to regional ALBs.
- **Decisive words:** worldwide uploads, static anycast, AWS network, healthy Regions
- **A:** Incorrect. Signed cookies authorize CloudFront content access and do not provide the required static anycast TCP entry design by themselves.
- **B:** Incorrect. ALB node addresses can change and are not stable anycast client endpoints.
- **C:** Incorrect. Gateway endpoints are VPC route-table targets and are not public global entry points for end users.
- **D:** Correct. Global Accelerator provides static anycast IP addresses and routes traffic over the AWS global network to healthy endpoints.
- **E:** Correct. Endpoint groups control regional distribution and use endpoint health to avoid unhealthy destinations.
- **Reusable rule:** Use Global Accelerator when clients need static anycast IPs and optimized health-aware routing for supported regional endpoints.
- **Official reference:** [AWS](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

## SIM-C-41 — Answer C

- **Central requirement:** Estimate steady-state Lambda concurrency from request rate and duration.
- **Decisive words:** 120 requests per second, 2 seconds, concurrency
- **A:** Incorrect. Concurrency depends on both arrival rate and how long each invocation remains active.
- **B:** Incorrect. Dividing the request rate by duration understates the number of overlapping invocations.
- **C:** Correct. Concurrency is request rate multiplied by average duration: 120 invocations per second times 2 seconds.
- **D:** Incorrect. Execution duration alone does not determine the number of overlapping requests.
- **Reusable rule:** For a steady stream, concurrency is approximately requests per second multiplied by average execution duration in seconds.
- **Official reference:** [AWS](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html)

## SIM-C-42 — Answer D

- **Central requirement:** Run bursty containers without Kubernetes or EC2 host administration.
- **Decisive words:** spiky, scale to zero tasks, no Kubernetes, no host patching
- **A:** Incorrect. Manual instance launches are slow, operationally heavy, and do not provide a managed service scaling model.
- **B:** Incorrect. A fixed peak fleet creates idle cost and requires host lifecycle management.
- **C:** Incorrect. EKS adds Kubernetes control and operational concepts despite no Kubernetes requirement.
- **D:** Correct. Fargate removes host provisioning and patching while retaining ECS task and service controls.
- **Reusable rule:** Choose Fargate when ECS container semantics are needed but managing the underlying EC2 capacity is not a requirement.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)

## SIM-C-43 — Answer A

- **Central requirement:** Reduce global public-read latency and personalized compute/data latency without unsafe caching.
- **Decisive words:** cacheable public reads, personalized endpoint, cold starts, repeated DynamoDB reads
- **A:** Correct. The design separates safe edge caching, initialization latency control, and database read acceleration instead of applying one cache to private data.
- **B:** Incorrect. A shared key can leak personalized data and ignores authorization-specific cache variation.
- **C:** Incorrect. Ephemeral storage does not remove cold starts or repeated database reads, and DynamoDB requires a primary key.
- **D:** Incorrect. A single ephemeral host reduces global resilience and creates operational and durability risks.
- **Reusable rule:** Optimize each latency layer independently: edge-cache shareable data, control Lambda initialization, and accelerate only proven database read patterns.
- **Official reference:** [AWS](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)

## SIM-C-44 — Answer A,B

- **Central requirement:** Remove a hot DynamoDB key and support an alternate severity-time query.
- **Decisive words:** 40 percent gateway, throttling, query by severity, recent
- **A:** Correct. Write sharding spreads a dominant logical key across physical partitions so provisioned or on-demand capacity can be used.
- **B:** Correct. A GSI supplies the alternate query key without scanning the base table.
- **C:** Incorrect. LSIs must be created with the table and retain the base table partition key.
- **D:** Incorrect. Larger items consume more capacity and do not remove concentration on one logical partition key.
- **E:** Incorrect. Scans consume broad capacity and do not create the scalable severity access pattern.
- **Reusable rule:** Design DynamoDB keys from traffic distribution and access patterns; shard hot writes and use a GSI for a new alternate partition key.
- **Official reference:** [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-sharding.html)

## SIM-C-45 — Answer B

- **Central requirement:** Combine relational consistency, elastic capacity, read scaling, and safe Lambda connectivity.
- **Decisive words:** PostgreSQL, unpredictable bursts, transactions, read scaling, Lambda
- **A:** Incorrect. This abandons the required relational model and moves consistency logic into untrusted clients.
- **B:** Correct. The combination preserves PostgreSQL transactions, scales compute incrementally, adds read capacity, and protects connections from serverless bursts.
- **C:** Incorrect. Spot interruption and ephemeral storage conflict with durability, availability, and managed scaling requirements.
- **D:** Incorrect. Cluster lifecycle time and cost make per-request database provisioning impractical.
- **Reusable rule:** For bursty relational serverless access, separate database capacity scaling, read scaling, and connection pooling rather than treating them as one control.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html)

## SIM-C-46 — Answer C

- **Central requirement:** Select the database feature intended to offload asynchronous read traffic.
- **Decisive words:** read-only reporting, accepts lag, no automatic standby
- **A:** Incorrect. Backups are recovery artifacts and cannot serve live reporting SQL traffic.
- **B:** Incorrect. A traditional Multi-AZ standby is maintained for failover and is not a general read-scaling target.
- **C:** Correct. A read replica asynchronously copies data and can offload read-only traffic from the primary.
- **D:** Incorrect. Event subscriptions report service events and do not execute or scale database reads.
- **Reusable rule:** Use read replicas for read scaling; use Multi-AZ deployments primarily for availability and failover unless the specific cluster architecture says otherwise.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

## SIM-C-47 — Answer D

- **Central requirement:** Remove high-volume DynamoDB traffic from NAT while preserving private AWS connectivity.
- **Decisive words:** private subnets, DynamoDB, NAT charges, no SDK change
- **A:** Incorrect. Self-peering is not a DynamoDB service path and does not remove the NAT dependency.
- **B:** Incorrect. Public addressing increases exposure and does not meet the private-path requirement.
- **C:** Incorrect. VPC endpoints are service-specific and cannot proxy arbitrary AWS service traffic.
- **D:** Correct. The gateway endpoint changes the route for DynamoDB traffic, requires no NAT, and has no hourly endpoint charge.
- **Reusable rule:** For S3 and DynamoDB from a VPC, evaluate no-additional-charge gateway endpoints before paying for NAT processing.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html)

## SIM-C-48 — Answer C,D

- **Central requirement:** Build an IPsec-encrypted dedicated primary path while recognizing the need for separate backup connectivity.
- **Decisive words:** dedicated path, predictable, IPsec, backup
- **A:** Incorrect. A NAT Gateway is a VPC egress service and cannot terminate the on-premises VPN or dedicated circuit.
- **B:** Incorrect. This is a useful backup, but the question asks for two components forming the encrypted dedicated primary; selecting it would omit one primary requirement.
- **C:** Correct. Direct Connect provides the dedicated network path and more consistent performance than internet-only connectivity.
- **D:** Correct. VPN over Direct Connect combines the dedicated transport with IPsec encryption when designed with the supported routing model.
- **E:** Incorrect. VPC peering connects VPCs and does not provide on-premises physical connectivity.
- **Reusable rule:** Direct Connect supplies dedicated transport; VPN can add IPsec, and a truly independent backup should avoid the same physical failure domain.
- **Official reference:** [AWS](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-plus-vpn.html)

## SIM-C-49 — Answer A

- **Central requirement:** Centralize transitive hybrid and VPC routing while preserving environment segmentation.
- **Decisive words:** eighty VPCs, VPNs, transitive hub, separate routing domains
- **A:** Correct. Transit Gateway provides regional transitive routing and route-table segmentation for hub-and-spoke connectivity.
- **B:** Incorrect. VPC peering is non-transitive, and a full mesh creates substantial route and connection operations.
- **C:** Incorrect. Internet Gateways provide internet connectivity and are not private multi-VPC transit hubs.
- **D:** Incorrect. NAT Gateways translate egress traffic, security groups do not route, and neither supplies transitive segmentation.
- **Reusable rule:** Use Transit Gateway route-table associations and propagations as explicit segmentation controls; connectivity does not imply universal reachability.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)

## SIM-C-50 — Answer B

- **Central requirement:** Combine low-latency stateful streaming, replay, and durable queryable raw storage.
- **Decisive words:** subsecond aggregates, raw S3, schema, independent replay
- **A:** Incorrect. Archive retrieval and annual batch processing cannot meet subsecond anomaly detection.
- **B:** Correct. The retained stream supports replay, Flink supplies stateful low-latency computation, and Firehose plus S3 and Glue serve durable analytics.
- **C:** Incorrect. Competing SQS consumers divide work and do not provide the retained multi-consumer stream model.
- **D:** Incorrect. Synchronous relational writes create coupling and do not naturally provide independent stream replay or scalable window processing.
- **Reusable rule:** Use a retained stream for replay, a stateful stream processor for windows, and a separate delivery path for durable lake storage and cataloging.
- **Official reference:** [AWS](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)

## SIM-C-51 — Answer C

- **Central requirement:** Identify the serverless query service for SQL directly over S3 data.
- **Decisive words:** occasional SQL, Parquet, S3, no cluster
- **A:** Incorrect. ElastiCache is an in-memory cache and does not provide serverless SQL over S3 files.
- **B:** Incorrect. A provisioned relational database adds administration and unnecessary ingestion for occasional lake queries.
- **C:** Correct. Athena is serverless SQL over data in S3 and avoids provisioning a persistent database cluster.
- **D:** Incorrect. SNS routes notifications and is not an analytical SQL query engine.
- **Reusable rule:** Use Athena for ad hoc serverless SQL over S3; optimize cost with columnar formats, compression, and useful partition pruning.
- **Official reference:** [AWS](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)

## SIM-C-52 — Answer A,B,C

- **Central requirement:** Transform heterogeneous inputs, catalog the lake, and govern fine-grained cross-account access.
- **Decisive words:** CSV and JSON, Parquet, shared catalog, fine-grained permissions
- **A:** Correct. Glue provides managed data integration and Spark-based transformation without self-managing a cluster.
- **B:** Correct. The shared catalog stores technical metadata that Athena and other analytics services can use.
- **C:** Correct. Lake Formation centralizes fine-grained data-lake permissions on cataloged resources.
- **D:** Incorrect. DNS records do not store analytical schemas or partition metadata.
- **E:** Incorrect. Block-storage snapshots neither govern S3 tables nor provide column-level permissions.
- **F:** Incorrect. Polly performs text-to-speech and is unrelated to data format transformation.
- **Reusable rule:** A governed lake separates transformation, metadata catalog, and authorization into Glue processing, Glue Data Catalog, and Lake Formation.
- **Official reference:** [AWS](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)

## SIM-C-53 — Answer D

- **Central requirement:** Align automatic storage transitions and expiration with a known access and retention timeline.
- **Decisive words:** first month active, six years rare, hours acceptable, delete year seven
- **A:** Incorrect. One Zone-IA stores data in one AZ and is inappropriate when the archive cannot be recreated after a zonal loss.
- **B:** Incorrect. S3 storage classes are designed for different access patterns and retain documented durability; Standard wastes cost for cold data.
- **C:** Incorrect. Instance store is ephemeral, host-bound, and unsuitable for a seven-year compliance archive.
- **D:** Correct. Lifecycle automation aligns storage class with access age and performs expiration without manual object-by-object operations.
- **Reusable rule:** When object age predicts access, use S3 Lifecycle transitions and expiration; validate minimum storage duration and retrieval requirements.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

## SIM-C-54 — Answer A

- **Central requirement:** Reduce EBS overprovisioning while retaining measured IOPS and throughput.
- **Decisive words:** gp2 sized for IOPS, unused capacity, 6000 IOPS, 250 MiB/s
- **A:** Correct. gp3 decouples performance settings from volume size, allowing lower capacity while meeting measured IOPS and throughput.
- **B:** Incorrect. Increasing unused capacity raises cost and ignores a volume type that decouples performance from size.
- **C:** Incorrect. Instance store is ephemeral and would endanger database durability after stop, termination, or host failure.
- **D:** Incorrect. Snapshots are point-in-time backups and cannot directly serve as the attached live filesystem.
- **Reusable rule:** Use gp3 when independent capacity, IOPS, and throughput sizing avoids paying for unused gp2 storage.
- **Official reference:** [AWS](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html)

## SIM-C-55 — Answer B

- **Central requirement:** Optimize unpredictable S3 access automatically without per-object analysis.
- **Decisive words:** unpredictable access, changes, automatic savings, no retrieval fees
- **A:** Incorrect. Deep Archive has long retrieval times and minimum-duration considerations that conflict with unpredictable weekly reads.
- **B:** Correct. Intelligent-Tiering moves objects among access tiers based on observed activity without retrieval fees for the automatic frequent and infrequent tiers.
- **C:** Incorrect. This preserves performance but fails the automatic savings and low-operations requirements.
- **D:** Incorrect. Instance store is ephemeral and is not durable managed object storage.
- **Reusable rule:** Use Intelligent-Tiering when access patterns are unknown or changing; evaluate monitoring charges, object size, and optional archive retrieval times.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html)

## SIM-C-56 — Answer A,D,E

- **Central requirement:** Recognize the storage model and durability role of EBS, EFS, and S3 archival classes.
- **Decisive words:** block, shared file, archival object, optimization
- **A:** Correct. EBS is durable block storage scoped to an Availability Zone and supports snapshots for backup or migration.
- **B:** Incorrect. Instance store data is ephemeral and can be lost on stop, termination, or host failure.
- **C:** Incorrect. NAT Gateways translate network egress and do not expose file-system semantics.
- **D:** Correct. EFS is a regional managed NFS file service designed for concurrent client access.
- **E:** Correct. Glacier classes reduce storage cost for cold objects while introducing retrieval and duration considerations.
- **F:** Incorrect. CloudFront caches delivered content and is not an EBS backup or block-storage service.
- **Reusable rule:** Choose storage by access protocol, scope, durability, and retrieval profile before comparing price; caches and ephemeral disks are not backups.
- **Official reference:** [AWS](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html)

## SIM-C-57 — Answer C

- **Central requirement:** Discount a stable compute baseline while retaining family, Region, and service flexibility.
- **Decisive words:** steady EC2 and Fargate, families may change, three-year commitment
- **A:** Incorrect. Spot discounts require interruption-tolerant workloads and do not represent a guaranteed baseline commitment.
- **B:** Incorrect. Standard RIs are less flexible and do not provide the requested cross-service Fargate coverage.
- **C:** Correct. Compute Savings Plans apply across eligible EC2 families, Regions, operating systems, and supported Fargate or Lambda usage.
- **D:** Incorrect. Savings Plans apply to eligible compute usage, not NAT Gateway charges.
- **Reusable rule:** Buy flexible commitments only for a conservative usage baseline; keep variable or interruption-tolerant demand on appropriate on-demand or Spot capacity.
- **Official reference:** [AWS](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)

## SIM-C-58 — Answer D

- **Central requirement:** Blend reliable baseline compute with discounted interruption-tolerant burst capacity.
- **Decisive words:** steady queue, overnight bursts, checkpoint, retry, lowest cost
- **A:** Incorrect. An archival object tier is not a compute-capacity or queue-scaling mechanism.
- **B:** Incorrect. Single-pool Spot capacity is fragile, and lack of checkpoint or interruption response wastes work.
- **C:** Incorrect. Permanent peak capacity meets performance but wastes substantial idle compute cost.
- **D:** Correct. Stable capacity protects deadlines while diversified Spot handles interruption-tolerant bursts at lower cost.
- **Reusable rule:** Use stable capacity for the noninterruptible baseline and diversified Spot for elastic fault-tolerant work, with checkpointing and rebalance handling.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

## SIM-C-59 — Answer A

- **Central requirement:** Optimize Lambda memory and duration using measured total cost rather than one dimension.
- **Decisive words:** 512 MB 12 seconds, 1536 MB 3 seconds, cost-performance
- **A:** Correct. Lambda allocates CPU with memory and bills duration, so higher memory can reduce total cost when execution time falls enough.
- **B:** Incorrect. Billing depends on both memory and duration, and more memory also changes available CPU performance.
- **C:** Incorrect. Higher memory has a higher per-duration rate and must be evaluated against the measured speedup.
- **D:** Incorrect. Subnet selection does not change the Lambda compute billing formula and does not automatically provide a public IP.
- **Reusable rule:** Benchmark representative Lambda memory sizes because CPU scales with memory and the cheapest configuration depends on memory-duration product and workload behavior.
- **Official reference:** [AWS](https://docs.aws.amazon.com/lambda/latest/operatorguide/computing-power.html)

## SIM-C-60 — Answer B,D,F

- **Central requirement:** Reduce database cost through commitments, pricing-model analysis, and idle-environment scheduling.
- **Decisive words:** predictable RDS, Aurora I/O charges, development idle
- **A:** Incorrect. Removing required recovery points violates resilience and may create unacceptable business risk.
- **B:** Correct. Reserved DB Instance pricing can discount eligible steady database instance usage when the commitment matches the workload.
- **C:** Incorrect. Oversizing raises cost and may not improve bottlenecks unrelated to CPU or memory.
- **D:** Correct. I/O-Optimized can reduce total cost for I/O-intensive Aurora workloads but is not automatically cheaper for every cluster.
- **E:** Incorrect. A cache is not a durable relational system of record and cannot replace required SQL semantics.
- **F:** Correct. Stopping eligible development databases avoids instance charges during planned idle periods while storage charges continue.
- **Reusable rule:** Optimize database cost only after separating steady commitments, measured I/O economics, idle schedules, and mandatory resilience requirements.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)

## SIM-C-61 — Answer B

- **Central requirement:** Choose a DynamoDB mode that removes initial capacity forecasting for variable demand.
- **Decisive words:** new application, unknown variable traffic, avoid forecasting
- **A:** Incorrect. A tiny fixed allocation risks throttling and directly conflicts with unknown variable demand.
- **B:** Correct. On-demand automatically accommodates variable traffic within service behavior and charges per request without initial capacity planning.
- **C:** Incorrect. DynamoDB is managed and does not expose partitions as EC2 instances for customers to scale.
- **D:** Incorrect. S3 storage tiers do not control DynamoDB request capacity.
- **Reusable rule:** Start unpredictable DynamoDB workloads on on-demand capacity, then evaluate provisioned plus auto scaling when traffic becomes stable and savings justify it.
- **Official reference:** [AWS](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html)

## SIM-C-62 — Answer C

- **Central requirement:** Evaluate Aurora pricing configuration from the workload's measured I/O cost profile.
- **Decisive words:** I/O charges exceed instances, tuned workload, preserve throughput
- **A:** Incorrect. Lambda temporary storage is ephemeral, not shared, and cannot replace a transactional database.
- **B:** Incorrect. Disabling recovery protections violates durability and is not an appropriate cost optimization.
- **C:** Correct. I/O-Optimized removes per-I/O charges in exchange for different compute and storage pricing, benefiting sufficiently I/O-intensive workloads.
- **D:** Incorrect. Additional replicas add cost and replication I/O and do not automatically reduce the workload's write volume.
- **Reusable rule:** Compare Aurora Standard and I/O-Optimized with real compute, storage, and I/O usage; choose by total cost, not one line item.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-storage-iopt.html)

## SIM-C-63 — Answer D

- **Central requirement:** Reduce repeated content delivery, NAT processing, and cross-AZ egress dependency together.
- **Decisive words:** global downloads, repeated origin, S3 through NAT, centralized NAT
- **A:** Incorrect. A single block-storage origin is operationally fragile and cannot match global object caching.
- **B:** Incorrect. Public exposure is not a safe cost optimization and creates ongoing IPv4 charges.
- **C:** Incorrect. NAT Gateways are regional resources, and cross-Region centralization would add latency, transfer cost, and failure risk.
- **D:** Correct. Caching reduces repeated origin delivery, the endpoint removes S3 from NAT, and same-AZ NAT paths avoid cross-AZ dependency and transfer.
- **Reusable rule:** Optimize network cost by changing traffic paths: edge caching for repeated content, service endpoints for AWS APIs, and zonally resilient egress for the remainder.
- **Official reference:** [AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

## SIM-C-64 — Answer C,E,F

- **Central requirement:** Reduce recurring service-path, origin-delivery, and unnecessary endpoint charges.
- **Decisive words:** terabytes to S3, static global, interface versus gateway endpoints
- **A:** Incorrect. This retains NAT processing and adds cross-AZ transfer and a zonal dependency.
- **B:** Incorrect. Larger payloads generally increase transfer rather than reduce it.
- **C:** Correct. S3 gateway endpoints avoid NAT processing and have no additional endpoint hourly charge.
- **D:** Incorrect. Public addresses add cost and exposure and do not provide an appropriate private service path.
- **E:** Correct. A higher cache-hit ratio reduces repeated origin requests and data transfer from the origin path.
- **F:** Correct. Interface endpoints incur hourly and data-processing charges, so architecture and AZ placement should match actual needs.
- **Reusable rule:** Network cost optimization starts with flow visibility, then replaces expensive paths with gateway endpoints, caching, compression, or right-sized private endpoints.
- **Official reference:** [AWS](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html)

## SIM-C-65 — Answer A

- **Central requirement:** Evaluate predictable private hybrid connectivity for sustained outbound data volume.
- **Decisive words:** 8 TB monthly, same facility, inconsistent internet, predictable private
- **A:** Correct. Direct Connect can provide more consistent private connectivity and different transfer economics for sustained hybrid traffic.
- **B:** Incorrect. A NAT Gateway is internet egress translation and does not create a private dedicated on-premises circuit.
- **C:** Incorrect. Gateway endpoints cannot be extended from on-premises through VPN, Direct Connect, peering, or Transit Gateway.
- **D:** Incorrect. Resolver endpoints forward DNS queries, not bulk analytics data.
- **Reusable rule:** For steady high-volume hybrid transfer, compare Direct Connect port, provider, redundancy, and data-transfer economics with internet or VPN alternatives.
- **Official reference:** [AWS](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
