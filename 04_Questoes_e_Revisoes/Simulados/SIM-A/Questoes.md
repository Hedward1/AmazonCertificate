# SIM-A — Questions

**Navigation:** [Simulators index](../README.md) | [Result report](Relatorio.md)

- **Time:** 130 minutes
- **Language:** English
- **Rules:** Closed book. Complete all 65 questions before opening the answer key.

## Question metadata

| ID | Domain | Task | Format | Type | Difficulty |
|---|---:|---:|---|---|---|
| SIM-A-01 | 1 | 1.1 | single | fundamental | basic |
| SIM-A-02 | 1 | 1.1 | single | situational | intermediate |
| SIM-A-03 | 1 | 1.1 | single | integrated | advanced |
| SIM-A-04 | 1 | 1.1 | multi-2 | situational | intermediate |
| SIM-A-05 | 1 | 1.1 | single | integrated | advanced |
| SIM-A-06 | 1 | 1.1 | single | fundamental | basic |
| SIM-A-07 | 1 | 1.1 | single | situational | intermediate |
| SIM-A-08 | 1 | 1.2 | multi-2 | integrated | advanced |
| SIM-A-09 | 1 | 1.2 | single | situational | intermediate |
| SIM-A-10 | 1 | 1.2 | single | integrated | advanced |
| SIM-A-11 | 1 | 1.2 | single | fundamental | basic |
| SIM-A-12 | 1 | 1.2 | multi-2 | situational | intermediate |
| SIM-A-13 | 1 | 1.2 | single | integrated | advanced |
| SIM-A-14 | 1 | 1.2 | single | situational | intermediate |
| SIM-A-15 | 1 | 1.3 | single | integrated | advanced |
| SIM-A-16 | 1 | 1.3 | multi-2 | fundamental | basic |
| SIM-A-17 | 1 | 1.3 | single | situational | intermediate |
| SIM-A-18 | 1 | 1.3 | single | integrated | advanced |
| SIM-A-19 | 1 | 1.3 | single | situational | intermediate |
| SIM-A-20 | 1 | 1.3 | multi-2 | integrated | advanced |
| SIM-A-21 | 2 | 2.1 | single | fundamental | basic |
| SIM-A-22 | 2 | 2.1 | single | situational | intermediate |
| SIM-A-23 | 2 | 2.1 | single | integrated | advanced |
| SIM-A-24 | 2 | 2.1 | multi-2 | situational | intermediate |
| SIM-A-25 | 2 | 2.1 | single | integrated | advanced |
| SIM-A-26 | 2 | 2.1 | single | fundamental | basic |
| SIM-A-27 | 2 | 2.1 | single | situational | intermediate |
| SIM-A-28 | 2 | 2.1 | multi-2 | integrated | advanced |
| SIM-A-29 | 2 | 2.1 | single | situational | intermediate |
| SIM-A-30 | 2 | 2.2 | single | integrated | advanced |
| SIM-A-31 | 2 | 2.2 | single | fundamental | basic |
| SIM-A-32 | 2 | 2.2 | multi-2 | situational | intermediate |
| SIM-A-33 | 2 | 2.2 | single | integrated | advanced |
| SIM-A-34 | 2 | 2.2 | single | situational | intermediate |
| SIM-A-35 | 2 | 2.2 | single | integrated | advanced |
| SIM-A-36 | 2 | 2.2 | multi-2 | fundamental | basic |
| SIM-A-37 | 2 | 2.2 | single | situational | intermediate |
| SIM-A-38 | 3 | 3.1 | single | integrated | advanced |
| SIM-A-39 | 3 | 3.1 | single | situational | intermediate |
| SIM-A-40 | 3 | 3.1 | multi-2 | integrated | advanced |
| SIM-A-41 | 3 | 3.2 | single | fundamental | basic |
| SIM-A-42 | 3 | 3.2 | single | situational | intermediate |
| SIM-A-43 | 3 | 3.2 | single | integrated | advanced |
| SIM-A-44 | 3 | 3.3 | multi-2 | situational | intermediate |
| SIM-A-45 | 3 | 3.3 | single | integrated | advanced |
| SIM-A-46 | 3 | 3.3 | single | fundamental | basic |
| SIM-A-47 | 3 | 3.4 | single | situational | intermediate |
| SIM-A-48 | 3 | 3.4 | multi-2 | integrated | advanced |
| SIM-A-49 | 3 | 3.4 | single | situational | intermediate |
| SIM-A-50 | 3 | 3.5 | single | integrated | advanced |
| SIM-A-51 | 3 | 3.5 | single | fundamental | intermediate |
| SIM-A-52 | 3 | 3.5 | multi-3 | situational | intermediate |
| SIM-A-53 | 4 | 4.1 | single | integrated | intermediate |
| SIM-A-54 | 4 | 4.1 | single | situational | intermediate |
| SIM-A-55 | 4 | 4.1 | single | situational | intermediate |
| SIM-A-56 | 4 | 4.1 | multi-3 | fundamental | intermediate |
| SIM-A-57 | 4 | 4.2 | single | situational | intermediate |
| SIM-A-58 | 4 | 4.2 | single | integrated | intermediate |
| SIM-A-59 | 4 | 4.2 | single | situational | intermediate |
| SIM-A-60 | 4 | 4.3 | multi-3 | situational | intermediate |
| SIM-A-61 | 4 | 4.3 | single | fundamental | intermediate |
| SIM-A-62 | 4 | 4.3 | single | situational | intermediate |
| SIM-A-63 | 4 | 4.4 | single | integrated | intermediate |
| SIM-A-64 | 4 | 4.4 | multi-3 | situational | intermediate |
| SIM-A-65 | 4 | 4.4 | single | situational | intermediate |

## SIM-A-01

**Choose ONE.**

An application on an Amazon EC2 instance must read objects from one private S3 bucket. The security team prohibits long-term access keys on the instance and requires least-privilege credentials that rotate automatically. Which solution meets these requirements?

- A. Store the root user access key in AWS Secrets Manager and retrieve it at boot.
- B. Attach an IAM role through an instance profile with only the required S3 permissions.
- C. Store an IAM user access key in EC2 user data, scope it to the bucket, and rotate it every ninety days.
- D. Make the S3 bucket public so that the instance does not require credentials.

## SIM-A-02

**Choose ONE.**

A reporting team in Account A needs read-only access to a specific S3 prefix in Account B for three months. The company wants temporary sessions, central revocation, and no duplicate IAM users in Account B. Which design is most appropriate?

- A. Copy the data to a public S3 bucket in Account A every night.
- B. Create IAM users in Account B and email their access keys to the reporting team.
- C. Create a cross-account role in Account B with a scoped permissions policy and trust the authorized principal from Account A.
- D. Share the Account B root credentials and require the team to use MFA.

## SIM-A-03

**Choose ONE.**

A company has forty AWS accounts and an existing corporate identity provider. Employees need centralized console and CLI access, while security administrators must prevent member accounts from disabling organization-wide logging even if a local administrator grants permission. Which architecture best meets both requirements?

- A. Create IAM users in every account and attach AdministratorAccess to simplify onboarding.
- B. Use IAM Identity Center with permission sets for workforce access, and apply an Organizations SCP that denies the prohibited logging actions.
- C. Use a security group in each account to deny API calls that modify logging.
- D. Federate only into the management account and share its root credentials for member-account work.

## SIM-A-04

**Choose TWO.**

A Lambda function in Account A assumes a role in Account B and must decrypt data with a customer managed KMS key owned by Account B. The role already has permission to read the encrypted S3 objects. Which additional configurations are required for cross-account decryption?

- A. Grant the assumed role an IAM permission for the required KMS decrypt operation.
- B. Allow the external role in the KMS key policy in Account B.
- C. Make the encrypted S3 objects public so that KMS authorization is bypassed.
- D. Enable automatic rotation on the KMS key because rotation grants cross-account access.
- E. Add a security group rule that allows the Lambda function to reach the KMS key ARN.

## SIM-A-05

**Choose ONE.**

A global web application serves static assets from S3 and dynamic requests through an Application Load Balancer. The S3 bucket must remain private, clients must use HTTPS, and common web exploits must be blocked at the edge with minimal origin load. Which design best satisfies the requirements?

- A. Use one CloudFront distribution with origin access control for S3, HTTPS viewer policies, the ALB as a second origin, and an AWS WAF web ACL.
- B. Expose the S3 website endpoint publicly and use network ACLs to inspect SQL injection payloads.
- C. Place a NAT gateway in front of S3 and terminate public TLS directly on each EC2 instance.
- D. Use Route 53 simple routing to the S3 REST endpoint and rely on S3 versioning for web attack protection.

## SIM-A-06

**Choose ONE.**

A security engineer removes an inbound security group rule after an HTTPS connection to an EC2 instance has already been established. Which statement correctly describes the stateful behavior of security groups for the connection?

- A. The return traffic is blocked unless an identical outbound rule is added for every client port.
- B. The security group change automatically creates a deny rule in the subnet network ACL.
- C. The established connection can continue because security groups track connection state.
- D. The security group behaves statelessly and immediately discards all response packets.

## SIM-A-07

**Choose ONE.**

A consumer web application needs user sign-up, password recovery, MFA, and standards-based tokens for its backend APIs. It does not need to give users temporary credentials for direct access to AWS services. Which service is the best fit?

- A. Use an Amazon Cognito user pool as the application user directory and token issuer.
- B. Create one IAM user for every consumer and distribute console passwords.
- C. Use AWS Organizations to register and authenticate individual consumers.
- D. Use an Amazon Cognito identity pool without a user directory, and federate it with an external identity provider.

## SIM-A-08

**Choose TWO.**

An internet-facing Application Load Balancer serves a payment API. The company requires managed TLS certificates with automatic renewal and protection against common SQL injection and cross-site scripting requests before they reach targets. Which configurations meet the requirements?

- A. Attach an ACM certificate to an HTTPS listener on the Application Load Balancer.
- B. Use a network ACL to inspect HTTP request bodies for SQL statements.
- C. Associate an AWS WAF web ACL with the Application Load Balancer and use appropriate managed rules.
- D. Install a self-signed certificate on every target and expose the targets directly to the internet.
- E. Store a certificate in an S3 bucket and configure Route 53 to perform TLS termination.

## SIM-A-09

**Choose ONE.**

An application uses a database password that must rotate every thirty days. Operations wants the application to retrieve the current value programmatically and wants rotation to occur without maintaining a custom credential server. Which solution requires the least operational effort?

- A. Place the password in an unencrypted EC2 user-data script and replace the instance monthly.
- B. Store the password in AWS Secrets Manager and configure managed or Lambda-based rotation for the database secret.
- C. Store the password as plain text in an S3 object with a lifecycle expiration rule.
- D. Embed the password in a container image and publish a replacement image through the deployment pipeline for every rotation.

## SIM-A-10

**Choose ONE.**

A company exposes a REST API only to workloads in selected VPCs. Requests must remain on the AWS network, public internet invocation must be impossible, and access must be restricted to approved interface endpoints. Which architecture best meets the requirements?

- A. Publish the API through CloudFront and use a long DNS name that external clients cannot guess.
- B. Create a public HTTP API and rely only on a security group attached to backend Lambda functions.
- C. Create an edge-optimized public API and hide its URL in Parameter Store.
- D. Create an API Gateway private REST API, invoke it through execute-api interface VPC endpoints, and restrict the API resource policy to approved endpoint or VPC conditions.

## SIM-A-11

**Choose ONE.**

An application encrypts large files before storing them in Amazon S3. The security team wants KMS-controlled key access without sending entire files to AWS KMS. Which statement describes the recommended envelope-encryption process?

- A. Use the KMS key ARN itself as plaintext symmetric key material inside the application.
- B. Send every complete file to the KMS Encrypt API because KMS accepts objects of any size.
- C. Use AWS KMS to generate a data key, encrypt the file locally with the plaintext data key, and store the encrypted data key with the ciphertext.
- D. Store the plaintext data key beside the encrypted file so that any reader can decrypt it.

## SIM-A-12

**Choose TWO.**

Instances in private subnets must access Amazon S3 and AWS Secrets Manager without a NAT gateway or internet gateway. The company wants private connectivity and the lowest practical endpoint cost. Which endpoints should be created?

- A. Create a gateway VPC endpoint for S3 and associate it with the private route tables.
- B. Create a public NAT gateway solely for calls to both services.
- C. Create a gateway VPC endpoint for Secrets Manager and add it to the route tables.
- D. Create an interface VPC endpoint for Secrets Manager with private DNS enabled.
- E. Create an interface VPC endpoint for S3 in every subnet as the only S3 access path.

## SIM-A-13

**Choose ONE.**

A subscription website serves thousands of private training files from S3 through CloudFront. After sign-in, a user may download many files under one path for one hour. The S3 bucket must reject direct access, and abusive requests must be rate limited. Which design best meets the requirements?

- A. Use CloudFront signed cookies for the authorized path, origin access control for the private S3 bucket, and an AWS WAF rate-based rule on the distribution.
- B. Generate one public S3 object URL per file and store the URLs in the browser cache.
- C. Use an S3 gateway endpoint in the user browser and a network ACL to count HTTP requests.
- D. Make the bucket public, use Route 53 weighted routing, and rely on the object names as secrets.

## SIM-A-14

**Choose ONE.**

A security team wants a managed service to analyze AWS data sources for suspicious behavior and unauthorized activity across accounts. Findings must be aggregated in a central security account where teams can prioritize them with other security standards. Which solution should be used?

- A. Use AWS Audit Manager as the network threat-detection engine for VPC traffic.
- B. Enable Amazon GuardDuty in the organization and aggregate its findings in AWS Security Hub in the delegated administrator account.
- C. Use Amazon Inspector only to correlate every account-level security standard and external finding.
- D. Use AWS Artifact to detect anomalous API calls and automatically isolate instances.

## SIM-A-15

**Choose ONE.**

A financial application stores immutable transaction exports in S3. Records must be undeletable by any user for seven years, encrypted with customer-controlled keys, and copied to a second Region for disaster recovery. Which architecture best satisfies all requirements?

- A. Enable versioning and S3 Object Lock compliance retention, use SSE-KMS with customer managed keys, and configure replication with the required destination key permissions.
- B. Store the only copy on an encrypted EBS volume and create a manual snapshot once per year.
- C. Use Object Lock governance mode and grant every administrator bypass permission for emergency deletion.
- D. Use S3 Standard with a lifecycle rule that expires objects after seven days and copy them with DataSync monthly.

## SIM-A-16

**Choose TWO.**

A web application sends sensitive data through an Application Load Balancer to an Amazon RDS database. Which controls protect data in transit on both network segments without relying on proprietary client-side encryption?

- A. Configure an HTTPS listener with a trusted certificate on the Application Load Balancer.
- B. Enable EBS fast snapshot restore for the database storage.
- C. Enable S3 Versioning on the bucket that stores application logs.
- D. Add a Route 53 health check for the web hostname.
- E. Require SSL or TLS connections from the application to the RDS database engine.

## SIM-A-17

**Choose ONE.**

A company must share an encrypted Amazon RDS snapshot with a separate AWS account. The source snapshot currently uses the default AWS managed RDS KMS key. The recipient must restore the database in its own account. What should the source account do?

- A. Make the source DB instance publicly accessible and give the recipient its master password.
- B. Export the snapshot metadata to CloudWatch Logs and let the recipient restore from the log group.
- C. Share the snapshot directly because AWS managed KMS keys automatically trust every account.
- D. Copy the snapshot using a customer managed KMS key, share the copied snapshot, and allow the recipient account to use that key.

## SIM-A-18

**Choose ONE.**

A healthcare service stores patient records in DynamoDB. Only selected attributes require application-level cryptographic separation, the service needs point-in-time recovery from accidental writes, and all requests must be attributable for audit. Which design best meets these requirements?

- A. Store every record in an unencrypted public S3 bucket and use Route 53 query logs for auditing.
- B. Encrypt only the EC2 root volume and rely on security group flow logs to reconstruct DynamoDB item changes.
- C. Use the AWS Database Encryption SDK for protected attributes, enable DynamoDB point-in-time recovery, and enable DynamoDB data events in CloudTrail.
- D. Use a DynamoDB global table as the only protection against accidental writes and disable CloudTrail to reduce cost.

## SIM-A-19

**Choose ONE.**

An analytics role in Account B must read objects from a bucket in Account A that uses SSE-KMS with a customer managed key. The bucket owner wants to retain full control and does not want to copy the data. Which access design is appropriate?

- A. Make the bucket and KMS key public so that the analytics role needs no policies.
- B. Share the AWS managed KMS key alias with Account B and omit any bucket policy.
- C. Grant only s3:GetObject in Account B because S3 permission automatically overrides the KMS key policy.
- D. Allow the Account B role in the bucket policy and KMS key policy, and grant the role matching S3 and KMS permissions.

## SIM-A-20

**Choose TWO.**

Versioning is already enabled on source and destination S3 buckets in different Regions. New source objects use SSE-KMS, and replication must preserve encryption under a destination customer managed key. Which configurations are required in the replication setup?

- A. Make both buckets publicly writable so that replication requests cannot be denied.
- B. Configure the replication rule to include SSE-KMS encrypted objects and specify the destination KMS key.
- C. Grant the replication IAM role the required decrypt permission on the source key and encrypt permission on the destination key.
- D. Disable the replication IAM role because S3 replication always uses the bucket owner root user.
- E. Use the source bucket default AWS managed key as the destination encryption key in every account.

## SIM-A-21

**Choose ONE.**

A web tier receives requests faster than a backend worker can process them during short traffic bursts. The company wants to decouple the components and retain work until a worker successfully processes it. Which AWS service is designed for this requirement?

- A. Amazon Route 53 Resolver
- B. Use Amazon Elastic Block Store volumes and periodic snapshots as the durable retry queue for the workers.
- C. AWS Certificate Manager
- D. Amazon Simple Queue Service (Amazon SQS)

## SIM-A-22

**Choose ONE.**

An Application Load Balancer distributes requests across an Auto Scaling group in three Availability Zones. Users intermittently lose their shopping carts when instances scale in. The company wants horizontal scaling without relying on load balancer stickiness. What should be changed?

- A. Write each cart only to the instance store volume of the first web server that receives it.
- B. Store session state in a shared durable or managed data store and keep the web instances stateless.
- C. Increase the EC2 instance termination protection setting and keep every instance permanently.
- D. Replace the Application Load Balancer with one NAT gateway per Availability Zone so requests always reach one instance.

## SIM-A-23

**Choose ONE.**

An order API receives unpredictable bursts. Each order must be processed in sequence for its customer, duplicate deliveries must not create duplicate charges, and failed messages must be isolated after repeated attempts. Which architecture best meets the requirements?

- A. Publish orders only to an SNS standard topic and assume every subscriber receives exactly one message in order.
- B. Write orders to an S3 bucket and poll the bucket once each week with a single EC2 instance.
- C. Send orders to an SQS FIFO queue using the customer ID as the message group, make the consumer idempotent, and configure a dead-letter queue.
- D. Invoke the payment service synchronously from the API and discard the request whenever the service is unavailable.

## SIM-A-24

**Choose TWO.**

An ecommerce application publishes an OrderCreated event. Billing and fulfillment must consume the event independently, a temporary failure in one consumer must not delay the other, and each team needs its own retry backlog. Which design elements should be used?

- A. Store events only in an EC2 instance memory buffer shared by both teams.
- B. Create a separate SQS queue for each consumer and subscribe or target both queues from the event distribution layer.
- C. Send the event to one shared SQS queue and let billing and fulfillment compete for each message.
- D. Configure independent EventBridge targets or routing rules for the billing and fulfillment queues.
- E. Use one synchronous Lambda invocation chain from billing to fulfillment.

## SIM-A-25

**Choose ONE.**

A checkout workflow reserves inventory, authorizes payment, and requests shipment. Failures require different compensating steps, workflow state must survive for days, and operators need an execution history. Shipping can be retried asynchronously. Which design is most appropriate?

- A. Use AWS Step Functions Standard Workflows to orchestrate the services and compensation logic, with an SQS queue for asynchronous shipping work.
- B. Use a single Lambda invocation that sleeps between steps for several days and stores state only in memory.
- C. Place all steps in EC2 user data and rerun the entire instance whenever payment fails.
- D. Use Route 53 failover records to determine which business compensation step runs.

## SIM-A-26

**Choose ONE.**

One application event must be delivered to multiple subscribed endpoints, and each subscriber should receive its own copy of the notification. Which managed AWS service provides a basic publish-and-subscribe fanout model?

- A. Amazon Elastic File System
- B. Amazon EC2 Auto Scaling
- C. AWS Direct Connect
- D. Amazon Simple Notification Service (Amazon SNS)

## SIM-A-27

**Choose ONE.**

A telemetry platform uses Amazon Kinesis Data Streams. Events for the same device must be processed in arrival order, while throughput should scale across many devices. Which producer strategy should the solutions architect recommend?

- A. Use a random partition key for every record from the same device.
- B. Replace every record payload with a Route 53 health check result.
- C. Send all devices through one fixed partition key to preserve global ordering regardless of the resulting shard throughput.
- D. Use the device ID as the partition key and provision enough shards for the aggregate traffic.

## SIM-A-28

**Choose TWO.**

A public API receives flash-sale bursts that exceed the safe write rate of a downstream service. Requests may be processed asynchronously, no accepted request may be lost, and retries must not create duplicate business records. Which design choices meet the requirements?

- A. Disable retries so duplicate records can never occur.
- B. Place an SQS queue between the API ingestion layer and the downstream workers.
- C. Increase the API timeout until every downstream write completes synchronously.
- D. Store accepted requests only in Lambda memory until the downstream service recovers.
- E. Scale consumers from the queue and implement idempotency using a stable request or business key.

## SIM-A-29

**Choose ONE.**

A stateless web fleet needs submillisecond access to short-lived session data, automatic failover within a Region, and compatibility with common Redis data structures. The session store may lose data only if the entire regional design fails. Which solution is most suitable?

- A. Store sessions on EC2 instance store volumes behind the load balancer and replicate them with custom application logic.
- B. Use Amazon ElastiCache for Redis OSS or Valkey with replication and Multi-AZ automatic failover.
- C. Use Amazon S3 Glacier Deep Archive for every session read and write.
- D. Use an RDS read replica without a primary database instance.

## SIM-A-30

**Choose ONE.**

A global relational application writes in one Region and serves read traffic near users in two other Regions. The business requires an RPO measured in seconds and a managed cross-Region promotion process, while DNS must route clients to the active writer after recovery. Which architecture best meets the requirements?

- A. Use an Aurora global database with secondary clusters and configure Route 53 failover routing for the application writer endpoint strategy.
- B. Run one large database instance without replicas and increase its EBS volume size.
- C. Create weekly manual RDS snapshots and copy them to one S3 bucket in the primary Region.
- D. Use an RDS Multi-AZ deployment and assume its standby is available in every AWS Region.

## SIM-A-31

**Choose ONE.**

A production Amazon RDS database must automatically fail over to a synchronously replicated standby if the primary instance or its Availability Zone fails. Which RDS feature directly provides this capability?

- A. An Amazon S3 lifecycle transition rule
- B. An RDS read replica used without promotion automation
- C. An RDS Multi-AZ DB instance deployment
- D. An EC2 cluster placement group

## SIM-A-32

**Choose TWO.**

A web application must remain available after the loss of any one Availability Zone. Its EC2 instances are replaceable and receive traffic through an Application Load Balancer. Which configurations are required for the web tier?

- A. Route all health checks to an S3 bucket rather than the application targets.
- B. Use one fixed EC2 instance and restore it manually after an Availability Zone failure.
- C. Attach the Auto Scaling group target group to an Application Load Balancer enabled in multiple Availability Zones.
- D. Configure the Auto Scaling group to use subnets in at least two Availability Zones.
- E. Place every instance in one subnet to avoid cross-zone health checks.

## SIM-A-33

**Choose ONE.**

A company delivers critical static configuration files from S3 to applications in two Regions. It must survive a regional S3 access disruption, recover from accidental overwrites, and prevent a bad overwrite from immediately destroying the last known good copy in both Regions. Which design best addresses the requirements?

- A. Enable versioning in both buckets, replicate to the second Region, and use controls such as replication scope or Object Lock so retained versions remain recoverable.
- B. Use one unversioned bucket and configure clients to retry the same regional endpoint forever.
- C. Copy the current file to EC2 instance store in the primary Region and delete old copies.
- D. Use S3 Transfer Acceleration without a second bucket or retained object versions.

## SIM-A-34

**Choose ONE.**

A company needs centrally managed backups for RDS, EBS, and DynamoDB. Recovery copies must be placed in a separate AWS account and Region, and backup retention must resist deletion by compromised administrators. Which solution requires the least custom automation?

- A. Use EC2 user data to copy database passwords to a second Region every night.
- B. Enable CloudFront origin failover for RDS, EBS, and DynamoDB backups.
- C. Create one Lambda function per resource and store all backup IDs in local files on an administrator laptop.
- D. Use AWS Backup policies with cross-account and cross-Region copy actions, and protect the destination vault with AWS Backup Vault Lock.

## SIM-A-35

**Choose ONE.**

A regional ecommerce platform has an RTO of one hour and an RPO of fifteen minutes. The business wants lower steady-state cost than a fully scaled warm standby, but recovery must be automated and core database data must be continuously replicated. Which disaster-recovery strategy is the best fit?

- A. Use a pilot-light environment with continuous data replication, minimal core services running, and tested infrastructure automation to scale the application during recovery.
- B. Run a fully active multi-Region application at production scale in both Regions.
- C. Keep no resources or backups outside the primary Region and purchase larger instances.
- D. Use backup and restore from a weekly offline backup with manual server creation.

## SIM-A-36

**Choose TWO.**

A solutions architect is explaining how Availability Zones support resilient regional architectures. Which statements are correct?

- A. An edge location is interchangeable with an Availability Zone for running an RDS Multi-AZ standby.
- B. An Availability Zone automatically spans multiple AWS Regions.
- C. Deploying redundant application capacity across at least two Availability Zones reduces dependence on one zonal failure domain.
- D. Two subnets in the same Availability Zone provide protection from a complete failure of that zone.
- E. Availability Zones in a Region are distinct locations engineered with independent failure domains.

## SIM-A-37

**Choose ONE.**

A company has primary and secondary regional endpoints for a web application. Traffic should use the primary while it is healthy and automatically resolve to the secondary only when the primary health check fails. Which Route 53 routing policy should be configured?

- A. Weighted routing with equal weights and no health evaluation
- B. Geolocation routing based only on the country of the DNS resolver
- C. Failover routing with primary and secondary records and an appropriate health check
- D. Use simple routing with both endpoints returned regardless of health and require clients to retry the secondary endpoint.

## SIM-A-38

**Choose ONE.**

A genomics team stores a multi-terabyte dataset in S3 and runs short, tightly coupled HPC jobs on EC2. Jobs need a high-throughput POSIX file system that can load data from S3, while inter-node communication requires very low latency. Which architecture best meets the requirements?

- A. Mount S3 as an EBS boot volume and distribute the instances across multiple Regions.
- B. Use Amazon EFS One Zone with all compute nodes connected through public internet gateways.
- C. Copy the dataset to individual instance store volumes manually and use spread placement across Regions.
- D. Use Amazon FSx for Lustre linked to the S3 data repository and run compatible EC2 instances in a cluster placement group with enhanced networking.

## SIM-A-39

**Choose ONE.**

A latency-sensitive database on EC2 requires sustained high IOPS, predictable sub-millisecond storage latency, and durable block storage that persists independently of the instance. Which storage choice is most appropriate?

- A. Use an EC2 instance store volume and rely on stop/start persistence across instance replacement for durability.
- B. Use S3 Glacier Deep Archive as the mounted transactional block device.
- C. Use a provisioned IOPS Amazon EBS io2 volume sized for the required performance.
- D. Use an EFS archive storage class for database transaction logs.

## SIM-A-40

**Choose TWO.**

Users around the world upload and download multi-gigabyte objects directly to one S3 bucket. Connections are sometimes unreliable, clients should retry only failed portions, and the company wants an AWS-managed accelerated path into S3 without deploying regional proxy servers. Which features should be used?

- A. Archive every object before upload by using S3 Glacier Deep Archive.
- B. Require each client to restart the entire object transfer after any network interruption.
- C. Place one NAT instance in the bucket Region and route all internet clients through it.
- D. Enable S3 Transfer Acceleration and use its acceleration endpoint from supported clients.
- E. Use S3 multipart upload so clients can transfer and retry independent object parts.

## SIM-A-41

**Choose ONE.**

A CPU-bound AWS Lambda function processes compressed JSON files. Tests show that execution time is too high even though the function does not run out of memory. Which configuration change can also provide more CPU resources to the function?

- A. Increase the SQS visibility timeout even though the function is invoked from S3.
- B. Add more Availability Zones to the Lambda function configuration.
- C. Increase the Lambda function memory setting and measure the resulting duration.
- D. Change the function log retention period in CloudWatch Logs.

## SIM-A-42

**Choose ONE.**

A scientific simulation runs continuously for six months on EC2 and performs heavy floating-point calculations with little memory or network pressure. The instance type will remain stable, and interruption is not acceptable. Which choice best matches performance needs?

- A. Select a compute optimized EC2 instance family and benchmark the required vCPU generation.
- B. Use T-family burstable instances and assume unlimited CPU credits are free.
- C. Run the simulation in an S3 Glacier retrieval job.
- D. Select a storage optimized instance because the application performs calculations, and maximize local NVMe capacity.

## SIM-A-43

**Choose ONE.**

An image-processing service packages proprietary libraries in containers. Jobs arrive in unpredictable bursts, each job can run for twenty minutes, and the company does not want to manage EC2 hosts. The API must accept jobs quickly while workers scale independently. Which architecture is most appropriate?

- A. Run a fixed EC2 container host at maximum size and write jobs to its local disk.
- B. Place jobs on SQS and run autoscaled Amazon ECS tasks on AWS Fargate as queue consumers.
- C. Invoke one Lambda function per job and increase its timeout to twenty minutes.
- D. Store the containers in S3 Glacier Deep Archive and process jobs during archive retrieval.

## SIM-A-44

**Choose TWO.**

A product catalog uses DynamoDB. Traffic is high, most requests repeatedly read a small set of items, and the table must avoid hot partitions as the catalog grows. Which design choices improve read performance and partition scalability?

- A. Add DynamoDB Accelerator (DAX) for compatible eventually consistent read-heavy access patterns.
- B. Choose a high-cardinality partition key that distributes requests across many partition values.
- C. Reduce the table to one partition and route all clients through a single EC2 instance.
- D. Use one constant partition key for every catalog item so all reads reach one partition.
- E. Scan the entire table for every product lookup instead of using keys.

## SIM-A-45

**Choose ONE.**

Thousands of Lambda functions query an Aurora PostgreSQL cluster during traffic spikes. Connection storms exhaust database resources, and read queries need additional capacity without sending writes to replicas. Which architecture best addresses both issues?

- A. Increase the Lambda timeout and direct every read and write to one database connection on the writer.
- B. Store active database connections in S3 so that every Lambda invocation can reuse the same socket.
- C. Replace the database endpoint with a Route 53 MX record and disable connection authentication.
- D. Place Amazon RDS Proxy between Lambda and the cluster, and direct read-only traffic to Aurora replicas through the appropriate reader path.

## SIM-A-46

**Choose ONE.**

A relational database serves the same reference records millions of times per day. The application can tolerate briefly stale cached values and needs microsecond-scale access for repeated reads. Which service is designed for this cache layer?

- A. Amazon ElastiCache
- B. AWS CloudFormation
- C. Amazon S3 Glacier Deep Archive
- D. Amazon Route 53 Resolver DNS Firewall

## SIM-A-47

**Choose ONE.**

A gaming API runs behind Network Load Balancers in two Regions. Clients require two static anycast IP addresses, traffic should enter through the AWS global network, and unhealthy regional endpoints must fail over quickly without waiting for long DNS caches. Which service fits the requirement?

- A. Amazon CloudFront using only an S3 origin
- B. AWS Global Accelerator with endpoint groups for both Regions
- C. A Route 53 private hosted zone associated with one VPC
- D. An internet gateway attached directly to both Network Load Balancers

## SIM-A-48

**Choose TWO.**

A global news site serves cacheable objects through CloudFront from one S3 origin. Origin request volume is still high because many edge locations request the same newly published object, and unnecessary query strings fragment the cache. Which changes improve cache efficiency and reduce origin load?

- A. Set the minimum, default, and maximum TTL values to zero for every object.
- B. Forward every viewer header, cookie, and query string in the cache key.
- C. Create a cache policy that includes only query strings and headers that actually change the response.
- D. Enable Origin Shield in a suitable Region to add a centralized cache layer before the origin.
- E. Bypass CloudFront and direct all viewers to the S3 origin.

## SIM-A-49

**Choose ONE.**

A company transfers a steady 2 Gbps of business data between its data center and a VPC. It needs more consistent private network performance than an internet VPN normally provides but wants encrypted backup connectivity if the dedicated path fails. Which design is appropriate?

- A. Use CloudFront origin failover to carry arbitrary private routing protocols.
- B. Use an S3 gateway endpoint as the dedicated physical connection to the data center.
- C. Use only an internet gateway in the VPC and advertise private data-center routes to it by using BGP.
- D. Use AWS Direct Connect for the primary path and a Site-to-Site VPN as backup connectivity.

## SIM-A-50

**Choose ONE.**

A retailer needs to ingest clickstream events in real time, let a fraud application consume each event with low latency, and continuously deliver the same stream to S3 in compressed batches for analytics. Producers must control partitioning for per-session order. Which architecture is best?

- A. Publish events as Route 53 TXT records and use DNS query logs as the analytics dataset.
- B. Write events directly to S3 Glacier Deep Archive and scan the archive for fraud once per day.
- C. Publish to Kinesis Data Streams with the session ID as partition key, use a stream consumer for fraud detection, and deliver to S3 through Amazon Data Firehose.
- D. Send all events to one SQS standard queue and allow the fraud and archive consumers to compete for each message.

## SIM-A-51

**Choose ONE.**

A data engineering team needs a managed service to discover schemas in data stored on S3, maintain a central metadata catalog, and run serverless extract-transform-load jobs. Which AWS service provides these capabilities?

- A. AWS Shield Advanced
- B. Use AWS Glue for the workload.
- C. Amazon Route 53
- D. Use AWS Certificate Manager to catalog the datasets and schedule extract-transform-load jobs.

## SIM-A-52

**Select THREE.**

A Kinesis Data Streams workload is approaching shard limits. Records for one customer must remain ordered, several consumers need low-latency reads without competing for shared read throughput, and traffic growth is uneven. Which actions improve the design?

- A. Reshard the stream or use an appropriate capacity mode as throughput requirements change.
- B. Use a stable customer identifier as the partition key for records that require per-customer order.
- C. Use enhanced fan-out for consumers that need dedicated read throughput and low propagation delay.
- D. Replace the stream with S3 Glacier Flexible Retrieval for subsecond consumption.
- E. Randomize the partition key independently for every record from the same customer.
- F. Send every customer through one universal partition key to preserve global order.

## SIM-A-53

**Choose ONE.**

An application writes compliance reports to S3. Reports are read daily for thirty days, about monthly through day ninety, and rarely afterward, but any later retrieval must begin in milliseconds. The company wants to minimize storage cost without rewriting the application. Which lifecycle design is most appropriate?

- A. Keep reports in S3 Standard initially, transition them to S3 Standard-IA after thirty days, and then to S3 Glacier Instant Retrieval after ninety days.
- B. Move reports to S3 Glacier Deep Archive after one day and promise millisecond retrieval.
- C. Move reports to S3 One Zone-IA immediately even though the compliance copy cannot tolerate loss of one Availability Zone.
- D. Keep every report in S3 Standard forever because lifecycle transitions cannot preserve the object key.

## SIM-A-54

**Choose ONE.**

A fleet uses general-purpose EBS volumes whose capacity was increased only to obtain more baseline IOPS. The workload now has known IOPS and throughput needs but does not require provisioned-IOPS durability. Which change can reduce cost while preserving performance?

- A. Migrate to magnetic standard volumes and assume they provide the same latency and IOPS.
- B. Use io2 Block Express for every volume regardless of required durability or IOPS.
- C. Migrate to EBS gp3 and configure volume size, IOPS, and throughput independently.
- D. Copy the block devices to S3 Glacier and attach the archive directly to EC2.

## SIM-A-55

**Choose ONE.**

A shared Amazon EFS file system contains project files that are active for two weeks and then are usually untouched for months. Occasional later access can tolerate a small first-byte latency increase. Which configuration reduces storage cost with minimal application change?

- A. Provision maximum EFS throughput permanently because higher throughput lowers storage price.
- B. Copy every file to EC2 instance store after two weeks and delete the EFS file system.
- C. Convert the file system into an EBS root volume attached simultaneously to all instances in multiple Availability Zones.
- D. Enable EFS lifecycle management to transition inactive files to an EFS infrequent-access or archive class.

## SIM-A-56

**Select THREE.**

A solutions architect is comparing Amazon S3 storage classes for cost optimization. Which statements are correct?

- A. S3 Intelligent-Tiering always charges a retrieval fee for objects in its frequent access tier.
- B. S3 Standard stores every object in only one Availability Zone to reduce cost.
- C. S3 Standard-IA has no retrieval charge and no minimum storage duration considerations.
- D. S3 Glacier Instant Retrieval provides millisecond retrieval for rarely accessed archive data.
- E. S3 One Zone-IA stores data in a single Availability Zone and is appropriate only when that resilience tradeoff is acceptable.
- F. S3 Glacier Deep Archive is designed for long-term archives whose retrieval can take hours.

## SIM-A-57

**Choose ONE.**

A fault-tolerant rendering farm runs independent jobs that checkpoint to S3 and can resume after interruption. Demand varies widely, and the company wants the lowest EC2 compute cost without committing to a fixed instance family. Which design is most appropriate?

- A. Use only On-Demand Instances and disable scaling during low demand.
- B. Use an EC2 Auto Scaling group with diversified Spot Instance capacity and interruption-aware workers.
- C. Run the entire farm on Dedicated Hosts at fixed maximum capacity.
- D. Purchase a zonal Reserved Instance for one exact type before measuring demand.

## SIM-A-58

**Choose ONE.**

A service has a steady compute baseline, unpredictable customer-facing peaks that cannot be interrupted, and a separate retryable batch queue. The company can commit to one year but expects instance families and Regions to change. Which purchasing mix is most cost effective?

- A. Purchase zonal Reserved Instances for peak capacity in one exact Availability Zone and run batch only on On-Demand.
- B. Run all three demand categories on Dedicated Hosts without a licensing requirement.
- C. Cover the steady eligible baseline with a Compute Savings Plan, use On-Demand capacity for noninterruptible excess, and use Spot for retryable batch workers.
- D. Use Spot for the customer-facing baseline and discard requests whenever Spot capacity is reclaimed.

## SIM-A-59

**Choose ONE.**

A lightweight report function runs for one minute every hour, has no local state, and needs 512 MB of memory. The company wants to avoid paying for idle servers and minimize operating effort. Which compute option is most cost effective?

- A. Keep a large On-Demand EC2 instance running continuously.
- B. Run the code as a scheduled AWS Lambda function.
- C. Purchase a Dedicated Host for the report function.
- D. Run an always-on Amazon ECS cluster with several unused EC2 container instances.

## SIM-A-60

**Select THREE.**

A company runs a steady production RDS database and several development databases used only during business hours. Performance data shows the production instance is oversized, and the company can make a one-year commitment after rightsizing. Which actions can reduce database cost?

- A. Purchase an appropriate Reserved DB Instance after the stable production requirement is right-sized.
- B. Keep every development database running all night to preserve billing discounts.
- C. Buy a Reserved DB Instance for the current oversized production shape before reviewing utilization.
- D. Stop eligible development DB instances outside business hours and account for automatic restart behavior.
- E. Create additional read replicas even though there is no read-performance requirement.
- F. Right-size the production DB instance based on measured CPU, memory, and I/O demand.

## SIM-A-61

**Choose ONE.**

A new DynamoDB workload has unpredictable request volume and no reliable capacity forecast. The team wants the table to scale automatically and prefers request-based billing until a stable pattern emerges. Which capacity mode should it choose?

- A. DynamoDB on-demand capacity mode
- B. A fixed EC2 instance that proxies every table request
- C. DynamoDB provisioned mode with no auto scaling and zero write capacity
- D. S3 Glacier Deep Archive retrieval capacity

## SIM-A-62

**Choose ONE.**

A production ElastiCache replication group has run at a stable size for a year and is expected to remain unchanged for three more years. The company wants a billing discount without changing cache behavior or reducing availability. What should it do?

- A. Replace the replication group with Spot EC2 instances and accept cache loss during every interruption.
- B. Move the hot cache data to S3 Glacier Deep Archive.
- C. Increase node count first so a larger reservation produces a larger percentage discount.
- D. Purchase reserved nodes that match the stable ElastiCache node configuration and term.

## SIM-A-63

**Choose ONE.**

A media site stores popular objects in S3 and serves a global audience. Direct origin downloads create high data-transfer cost and latency. Some query parameters are tracking-only, while signed authorization data must still be validated. Which architecture best balances cost, performance, and access control?

- A. Serve content through CloudFront, exclude tracking-only values from the cache key, preserve required authorization behavior, and protect the S3 origin with origin access control.
- B. Replicate every object to EC2 instance store in all Regions and bypass caching.
- C. Make S3 public and add every query parameter, cookie, and header to a unique cache key.
- D. Place a NAT gateway in every viewer network and route browser downloads through the gateways.

## SIM-A-64

**Select THREE.**

Private application subnets in three Availability Zones send heavy traffic to S3, DynamoDB, and Secrets Manager, plus a small amount of general internet traffic. The company wants lower NAT processing cost without creating a single zonal egress dependency. Which changes should be made?

- A. Remove every egress path, including the path required for the remaining internet destinations.
- B. Create S3 and DynamoDB gateway endpoints and associate them with the relevant private route tables.
- C. Create interface VPC endpoints for Secrets Manager in the required Availability Zones with private DNS.
- D. Route S3 and DynamoDB traffic through one NAT gateway in a fourth subnet.
- E. Keep a resilient same-AZ NAT path for only the general internet traffic that cannot use an endpoint.
- F. Send Secrets Manager API calls through a public Application Load Balancer.

## SIM-A-65

**Choose ONE.**

EC2 instances run in private subnets across three Availability Zones. Every subnet routes outbound traffic through one NAT gateway in the first Availability Zone, creating high cross-AZ data processing charges and a zonal dependency. What change best addresses both concerns?

- A. Keep one NAT gateway and move every application instance into its Availability Zone.
- B. Deploy a NAT gateway in each Availability Zone and route each private subnet to the NAT gateway in the same Availability Zone.
- C. Send outbound connections through an S3 bucket configured as a website endpoint.
- D. Replace the NAT gateway with an internet gateway attached directly to private instances without public addresses.
