# SIM-C — Questions

**Navigation:** [Simulators index](../README.md) | [Result report](Relatorio.md)

- **Time:** 130 minutes
- **Language:** English
- **Rules:** Closed book. Complete all 65 questions before opening the answer key.

## Question metadata

| ID | Domain | Task | Format | Type | Difficulty |
|---|---:|---:|---|---|---|
| SIM-C-01 | 1 | 1.1 | single | fundamental | basic |
| SIM-C-02 | 1 | 1.1 | single | situational | intermediate |
| SIM-C-03 | 1 | 1.1 | single | integrated | advanced |
| SIM-C-04 | 1 | 1.1 | multi-2 | situational | intermediate |
| SIM-C-05 | 1 | 1.1 | single | integrated | advanced |
| SIM-C-06 | 1 | 1.1 | single | fundamental | basic |
| SIM-C-07 | 1 | 1.1 | single | situational | intermediate |
| SIM-C-08 | 1 | 1.2 | multi-2 | integrated | advanced |
| SIM-C-09 | 1 | 1.2 | single | situational | intermediate |
| SIM-C-10 | 1 | 1.2 | single | integrated | advanced |
| SIM-C-11 | 1 | 1.2 | single | fundamental | basic |
| SIM-C-12 | 1 | 1.2 | multi-2 | situational | intermediate |
| SIM-C-13 | 1 | 1.2 | single | integrated | advanced |
| SIM-C-14 | 1 | 1.2 | single | situational | intermediate |
| SIM-C-15 | 1 | 1.3 | single | integrated | advanced |
| SIM-C-16 | 1 | 1.3 | multi-2 | fundamental | basic |
| SIM-C-17 | 1 | 1.3 | single | situational | intermediate |
| SIM-C-18 | 1 | 1.3 | single | integrated | advanced |
| SIM-C-19 | 1 | 1.3 | single | situational | intermediate |
| SIM-C-20 | 1 | 1.3 | multi-2 | integrated | advanced |
| SIM-C-21 | 2 | 2.1 | single | fundamental | basic |
| SIM-C-22 | 2 | 2.1 | single | situational | intermediate |
| SIM-C-23 | 2 | 2.1 | single | integrated | advanced |
| SIM-C-24 | 2 | 2.1 | multi-2 | situational | intermediate |
| SIM-C-25 | 2 | 2.1 | single | integrated | advanced |
| SIM-C-26 | 2 | 2.1 | single | fundamental | basic |
| SIM-C-27 | 2 | 2.1 | single | situational | intermediate |
| SIM-C-28 | 2 | 2.1 | multi-2 | integrated | advanced |
| SIM-C-29 | 2 | 2.1 | single | situational | intermediate |
| SIM-C-30 | 2 | 2.2 | single | integrated | advanced |
| SIM-C-31 | 2 | 2.2 | single | fundamental | basic |
| SIM-C-32 | 2 | 2.2 | multi-2 | situational | intermediate |
| SIM-C-33 | 2 | 2.2 | single | integrated | advanced |
| SIM-C-34 | 2 | 2.2 | single | situational | intermediate |
| SIM-C-35 | 2 | 2.2 | single | integrated | advanced |
| SIM-C-36 | 2 | 2.2 | multi-2 | fundamental | basic |
| SIM-C-37 | 2 | 2.2 | single | situational | intermediate |
| SIM-C-38 | 3 | 3.1 | single | integrated | advanced |
| SIM-C-39 | 3 | 3.1 | single | situational | intermediate |
| SIM-C-40 | 3 | 3.1 | multi-2 | integrated | advanced |
| SIM-C-41 | 3 | 3.2 | single | fundamental | basic |
| SIM-C-42 | 3 | 3.2 | single | situational | intermediate |
| SIM-C-43 | 3 | 3.2 | single | integrated | advanced |
| SIM-C-44 | 3 | 3.3 | multi-2 | situational | intermediate |
| SIM-C-45 | 3 | 3.3 | single | integrated | advanced |
| SIM-C-46 | 3 | 3.3 | single | fundamental | basic |
| SIM-C-47 | 3 | 3.4 | single | situational | intermediate |
| SIM-C-48 | 3 | 3.4 | multi-2 | integrated | advanced |
| SIM-C-49 | 3 | 3.4 | single | situational | intermediate |
| SIM-C-50 | 3 | 3.5 | single | integrated | advanced |
| SIM-C-51 | 3 | 3.5 | single | fundamental | intermediate |
| SIM-C-52 | 3 | 3.5 | multi-3 | situational | intermediate |
| SIM-C-53 | 4 | 4.1 | single | integrated | intermediate |
| SIM-C-54 | 4 | 4.1 | single | situational | intermediate |
| SIM-C-55 | 4 | 4.1 | single | situational | intermediate |
| SIM-C-56 | 4 | 4.1 | multi-3 | fundamental | intermediate |
| SIM-C-57 | 4 | 4.2 | single | situational | intermediate |
| SIM-C-58 | 4 | 4.2 | single | integrated | intermediate |
| SIM-C-59 | 4 | 4.2 | single | situational | intermediate |
| SIM-C-60 | 4 | 4.3 | multi-3 | situational | intermediate |
| SIM-C-61 | 4 | 4.3 | single | fundamental | intermediate |
| SIM-C-62 | 4 | 4.3 | single | situational | intermediate |
| SIM-C-63 | 4 | 4.4 | single | integrated | intermediate |
| SIM-C-64 | 4 | 4.4 | multi-3 | situational | intermediate |
| SIM-C-65 | 4 | 4.4 | single | situational | intermediate |

## SIM-C-01

**Choose ONE.**

During an access incident, an IAM role has an identity policy that allows s3:GetObject, but a bucket policy explicitly denies that action for the role. No other policy changes are pending. What is the authorization result?

- A. The request is denied because an applicable explicit deny overrides the allow.
- B. The request succeeds because an identity policy always overrides a resource policy.
- C. The request succeeds only if the object uses SSE-S3 encryption.
- D. The request is retried automatically by IAM until the policies converge.

## SIM-C-02

**Choose ONE.**

An incident-response Lambda function in a security account must inspect snapshots in a workload account for two hours. The company prohibits IAM users and long-lived keys, and the workload account must control who can enter. Which design best meets these requirements?

- A. Copy the workload account root access keys into Secrets Manager in the security account.
- B. Create a cross-account role in the workload account that trusts the response role, then call AWS STS AssumeRole.
- C. Make every snapshot public and restrict access by an undocumented naming convention.
- D. Attach an SCP in the security account that grants read access to snapshots in all workload accounts through AWS Organizations.

## SIM-C-03

**Choose ONE.**

A global operations team uses IAM Identity Center across an AWS Organization. During a breach, access to production must be revoked centrally while an emergency role remains available only through audited short sessions. Which architecture best balances centralized control and break-glass access?

- A. Use Amazon Cognito user pools to issue AWS Management Console administrator permissions to employees.
- B. Create IAM users with permanent administrator keys in every production account.
- C. Assign normal permission sets through IAM Identity Center and maintain a tightly trusted emergency role with MFA, short maximum session duration, and CloudTrail monitoring.
- D. Place the production accounts outside Organizations so no central policy can affect emergency access.

## SIM-C-04

**Choose TWO.**

A compromised deployment role can create IAM roles. Security must prevent it from escalating privileges while allowing teams to create application roles within an approved permission ceiling. Which two controls should be applied?

- A. Require application roles to use a permissions boundary that caps their effective identity permissions.
- B. Restrict iam:CreateRole and iam:PutRolePermissionsBoundary so the deployment role can use only the approved boundary.
- C. Allow the deployment role to attach AdministratorAccess if the new role name starts with app-.
- D. Store the administrator policy document in an encrypted S3 bucket before attaching it.
- E. Use a CloudWatch dashboard as the preventive permission ceiling.

## SIM-C-05

**Choose ONE.**

A global storefront serves private S3 objects through CloudFront and dynamic traffic through regional ALBs. An incident showed direct S3 URL access and malicious requests reaching the application. The company wants one public edge, private origins, and centralized Layer 7 filtering. Which design is best?

- A. Use Route 53 latency records that resolve users directly to S3 website endpoints and public ALBs.
- B. Make the S3 bucket public, use signed object names, and rely on ALB security groups for SQL injection filtering.
- C. Put a NAT Gateway in front of S3 and attach network ACL rules containing malicious URL strings.
- D. Use CloudFront with Origin Access Control for S3, restrict the bucket to the distribution, place AWS WAF on CloudFront, and route dynamic behavior to the ALBs.

## SIM-C-06

**Choose ONE.**

A developer needs command-line access to an AWS account for one hour. The organization forbids embedded access keys and wants credentials to expire automatically. Which credential characteristic directly satisfies the requirement?

- A. Temporary AWS STS credentials with a limited session duration.
- B. An IAM user access key stored in an encrypted local file with a one-hour credential-process cache.
- C. The AWS account root access key protected by MFA.
- D. A presigned S3 URL used as a general AWS CLI credential.

## SIM-C-07

**Choose ONE.**

A consumer application authenticates millions of customers with social identity providers and MFA. A subset of signed-in users must upload directly to a user-specific S3 prefix without passing through the API servers. Which design has the least credential-management overhead?

- A. Create one IAM user and permanent access key for every customer account.
- B. Use a Cognito user pool for authentication and a Cognito identity pool that maps users to scoped IAM roles for temporary S3 credentials.
- C. Make the upload bucket public and include the customer ID only in the object key.
- D. Use IAM Identity Center permission sets in the mobile application for consumer sign-in.

## SIM-C-08

**Choose TWO.**

A serverless order API has bursty Lambda traffic and an RDS password rotated every 30 days. During rotation, old connections and sudden connection storms cause failures. Which two services should be combined to reduce credential and connection operations?

- A. Store and rotate the database credential in AWS Secrets Manager.
- B. Embed both old and new passwords in Lambda environment variables during every rotation window.
- C. Place Amazon RDS Proxy between Lambda and the database and integrate it with the secret.
- D. Increase the Lambda timeout to fifteen minutes so connections remain open longer.
- E. Move the function to a public subnet to obtain more source IP addresses.

## SIM-C-09

**Choose ONE.**

Private EC2 instances use an interface VPC endpoint to call Secrets Manager. A response team discovers that every role in the VPC can reach every secret allowed by IAM. The team wants an additional network-path policy that permits only one role and selected secrets. What should be changed?

- A. Add a network ACL rule containing the approved IAM role ARN.
- B. Replace the endpoint with an Internet Gateway and filter secret names in the route table.
- C. Attach a restrictive endpoint policy to the Secrets Manager interface endpoint and retain least-privilege IAM and secret policies.
- D. Disable TLS on the endpoint so packet inspection can identify the role.

## SIM-C-10

**Choose ONE.**

GuardDuty produces a high-severity finding for credential exfiltration in a member account. The organization wants centralized finding aggregation, automatic isolation of tagged instances, and an investigation view of related entities without building a custom event poller. Which architecture is best?

- A. Enable only CloudWatch CPU alarms and terminate every instance above 80 percent utilization.
- B. Send monthly Config snapshots to S3 and have administrators inspect them manually for credential exfiltration.
- C. Use AWS Artifact to aggregate findings and Amazon Macie to isolate EC2 network interfaces.
- D. Aggregate findings in Security Hub, route the finding event through EventBridge to an idempotent remediation workflow, and use Detective for relationship investigation.

## SIM-C-11

**Choose ONE.**

An EC2 security group allows inbound HTTPS from a client. The response packets must return to that client. Which security-group behavior is relevant when evaluating whether a separate outbound response rule is required?

- A. Security groups are stateful, so response traffic for an allowed connection is automatically permitted.
- B. Security groups are stateless and require mirrored inbound and outbound rules for every application connection.
- C. Security groups support ordered deny rules before allow rules.
- D. Security groups evaluate the HTTP method before allowing the response.

## SIM-C-12

**Choose TWO.**

A private REST API in API Gateway must be callable only through one interface VPC endpoint and only by principals from approved organization accounts. The API must have no public invocation path. Which two controls are required?

- A. Configure the API as a private API and associate or use the execute-api interface VPC endpoint.
- B. Place a NAT Gateway in each private subnet and allow the public API hostname.
- C. Use only a usage plan API key as the security boundary.
- D. Add an API resource policy that restricts the source VPC endpoint and approved principals or organization context.
- E. Add an S3 gateway endpoint because gateway endpoints support every AWS API.

## SIM-C-13

**Choose ONE.**

A company hosts public applications behind ALBs in fifty accounts. A new zero-day request pattern must be blocked consistently within minutes, and DDoS response support is required for the most critical endpoints. Which design minimizes decentralized operations?

- A. Ask each account owner to update security-group rules containing the malicious HTTP string.
- B. Use AWS Firewall Manager to deploy organization-wide AWS WAF policies and enroll critical resources in AWS Shield Advanced.
- C. Route all web requests through centralized NAT Gateways and use network ACLs to inspect and block the malicious request body.
- D. Use Amazon Inspector findings as inline ALB request filters.

## SIM-C-14

**Choose ONE.**

After an outage, auditors need to know who changed a security group, reconstruct the resulting configuration over time, and correlate the change with application error metrics. Which service mapping provides the necessary evidence?

- A. Use AWS Artifact for the configuration timeline and IAM Access Analyzer for application latency.
- B. Use CloudWatch for API caller identity and payloads, CloudTrail for CPU and error metrics, and AWS Config for packet captures.
- C. Use CloudTrail for API caller history, AWS Config for configuration timeline, and CloudWatch for operational metrics and logs.
- D. Use only VPC Flow Logs because flow records include every API caller and resource configuration.

## SIM-C-15

**Choose ONE.**

A regulated archive stores signed records in S3. Even administrators must be unable to shorten a seven-year retention period, and the evidence must survive accidental stack deletion. Which design provides the strongest required immutability?

- A. Replicate the objects to an unversioned public bucket in another Region.
- B. Use S3 Lifecycle expiration after seven years and grant administrators s3:DeleteObjectVersion.
- C. Enable only MFA Delete and keep the root virtual MFA device with the operations team.
- D. Create an S3 Object Lock compliance-mode retention period in a versioned bucket and protect the bucket lifecycle through controlled infrastructure policies.

## SIM-C-16

**Choose TWO.**

An application encrypts large files client-side and uses a customer managed KMS key only to protect data-key material. Which two steps are part of correct envelope encryption?

- A. Call GenerateDataKey and use the returned plaintext data key locally to encrypt the file.
- B. Send the entire multi-gigabyte file to the KMS Encrypt API.
- C. Write the plaintext data key into S3 object tags for recovery.
- D. Use an Organizations SCP as the symmetric cipher key.
- E. Store the encrypted copy of the data key with the file ciphertext and erase the plaintext key after use.

## SIM-C-17

**Choose ONE.**

A payment API terminates client TLS at an ALB and connects to an RDS database that requires encrypted sessions. Security wants managed public certificate renewal at the edge and verified TLS on the database hop. Which design best meets the requirement?

- A. Use an ACM public certificate on the ALB, configure HTTPS listeners, and require the application to validate the RDS CA certificate over TLS.
- B. Terminate TLS at the ALB and send plaintext database connections because the traffic remains in a VPC.
- C. Install one self-signed certificate on every client and disable certificate validation in the application.
- D. Use an S3 presigned URL as the ALB and RDS certificate.

## SIM-C-18

**Choose ONE.**

A global application encrypts regional DynamoDB exports before replication. During a regional outage, the recovery Region must decrypt locally without a cross-Region KMS dependency, while administrators require equivalent key identifiers and independent regional key policies. Which design is best?

- A. Use one single-Region KMS key and call its original regional endpoint from every recovery Region.
- B. Use related KMS multi-Region primary and replica keys, grant the recovery workload locally, and encrypt data keys with the regional related key.
- C. Export KMS key material to S3 and import it into an AWS managed key in the recovery Region.
- D. Disable encryption on replicas so recovery never depends on KMS.

## SIM-C-19

**Choose ONE.**

A data lake receives millions of new S3 objects daily. Security must discover likely personal data, publish findings centrally, and limit recurring classification cost to newly arrived high-risk prefixes. Which approach is most appropriate?

- A. Use GuardDuty DNS findings to classify every object column.
- B. Enable Amazon Inspector enhanced scanning on the S3 bucket objects.
- C. Configure Amazon Macie classification jobs scoped to the selected buckets or prefixes and schedule them for the required sampling window.
- D. Download every object to an administrator laptop and search it manually.

## SIM-C-20

**Choose TWO.**

Objects encrypted with a customer managed KMS key must replicate to a bucket in another account and Region. Replication is enabled but encrypted objects fail while unencrypted objects succeed. Which two changes are required?

- A. Replace both customer managed keys with the source account's default AWS managed S3 key.
- B. Grant the S3 replication role permission to decrypt with the source KMS key and encrypt with the destination KMS key.
- C. Configure the replication rule to include SSE-KMS objects and specify the destination KMS key.
- D. Make both buckets public so S3 can bypass KMS authorization.
- E. Use a NAT Gateway in the source Region as the replication identity.

## SIM-C-21

**Choose ONE.**

An order worker receives messages from an SQS Standard queue. After completing a database update, it crashes before deleting a message, and the message is delivered again. Which delivery property must the application design for?

- A. Strict global ordering across all producers and consumers.
- B. Exactly-once business transactions automatically coordinated with the database.
- C. At-most-once delivery, so the repeated message proves the queue is corrupted.
- D. At-least-once delivery, requiring idempotent processing of repeated messages.

## SIM-C-22

**Choose ONE.**

Several SaaS applications emit order events with different JSON shapes. Five internal consumers need filtered subsets and independent retry behavior, and producers must not know consumer endpoints. Which managed design has the lowest coupling?

- A. Publish normalized or partner events to Amazon EventBridge and use content-based rules with separate targets and failure handling.
- B. Write every event to one EC2 instance file and let all consumers poll the same file.
- C. Call all five consumers synchronously from each producer in a fixed sequence.
- D. Place every consumer on one SQS queue so each event is processed five times.

## SIM-C-23

**Choose ONE.**

A global ticketing platform accepts bursts through API Gateway. Each request starts a multi-step reservation with a five-minute payment wait, compensating release on failure, and an audit trail of state transitions. The team wants to avoid custom workflow coordination. Which design is best?

- A. Have API Gateway synchronously call every service, keep the client connection open for five minutes, and write compensating API calls in the client.
- B. Start an AWS Step Functions Standard workflow and use service integrations, wait states, retries, and compensation branches.
- C. Publish the reservation to one SNS topic and assume SNS tracks each workflow step.
- D. Store workflow state only in Lambda global variables between invocations.

## SIM-C-24

**Choose TWO.**

An EventBridge rule invokes a payment target that sometimes throttles. Matched events must be retried for a bounded period and preserved for operator-controlled replay after delivery attempts are exhausted. Which two configurations meet the requirement?

- A. Increase the root EBS volume of an unrelated EC2 instance.
- B. Configure an EventBridge target retry policy with an appropriate maximum age and retry attempts.
- C. Disable all retries so duplicate delivery can never occur.
- D. Configure an SQS dead-letter queue for the EventBridge target with the required queue policy.
- E. Use a CloudWatch dashboard as the failed-event storage destination.

## SIM-C-25

**Choose ONE.**

A serverless image pipeline receives unpredictable uploads in S3. It must create three derivatives, tolerate duplicate events, isolate poison images, and never overwhelm a third-party moderation API limited to 50 concurrent calls. Which architecture best meets all requirements?

- A. Use one Lambda directly from S3 with unreserved concurrency and delete failed objects immediately.
- B. Invoke the moderation API synchronously from the S3 upload client and retry forever in the browser.
- C. Route S3 events to SQS, process with Lambda using idempotency, cap event-source concurrency, and configure a DLQ or redrive path for repeated failures.
- D. Run a single EC2 instance that scans the bucket once per day and stores progress on instance store.

## SIM-C-26

**Choose ONE.**

Orders for the same customer must be processed in order, while orders for different customers should be processed concurrently on an SQS FIFO queue. What should the producer use as the MessageGroupId?

- A. Use the queue URL because FIFO derives order from the endpoint.
- B. Use one constant value for every customer to maximize parallelism.
- C. Use a new random value for every order from the same customer.
- D. Use the customer identifier so each customer is an ordered lane and different customers can run in parallel.

## SIM-C-27

**Choose ONE.**

Telemetry producers emit hundreds of thousands of ordered records per second. Several consumers need independent replay from their own checkpoints, and new analytics consumers may be added later. Which service is the best ingestion backbone?

- A. Use Amazon Kinesis Data Streams with partition-key planning and a retention period that covers replay.
- B. Use one SQS Standard queue with all consumers competing for each message and set a long retention period for later consumer replays.
- C. Use Amazon SNS without durable subscriptions or downstream queues.
- D. Write records directly to one EC2 instance store volume.

## SIM-C-28

**Choose TWO.**

An order table in DynamoDB must trigger independent fraud, fulfillment, and analytics processing. Each consumer must retry without blocking the others, and events older than seven days are not needed. Which two components form the most decoupled design?

- A. Have one Lambda synchronously call all three consumers in sequence.
- B. Capture item changes with DynamoDB Streams as the ordered per-item change source.
- C. Make the DynamoDB table public so consumers can poll every partition.
- D. Store each event only in Lambda temporary storage for seven days.
- E. Use an EventBridge Pipes or Lambda fan-out path that delivers to separate durable queues for each consumer.

## SIM-C-29

**Choose ONE.**

A mobile API accepts video-processing requests that take up to forty minutes. Clients need an immediate request ID, processing must continue if the client disconnects, and status must be queryable without holding an HTTP connection. Which pattern is best?

- A. Increase the API Gateway integration timeout to forty minutes and keep the client socket open.
- B. Return an accepted response with a job ID, enqueue work durably, and expose a status resource backed by persistent state.
- C. Run the job inside a standard Lambda function with a forty-minute timeout.
- D. Store the job identifier and pending status only in browser local storage, then ask the client to resubmit after any disconnect.

## SIM-C-30

**Choose ONE.**

A global serverless API writes region-local data and must survive a complete regional outage with an RPO measured in seconds and an RTO under five minutes. Clients should fail over automatically, and writes must not create uncontrolled multi-writer conflicts. Which design best fits?

- A. Use one regional RDS instance with Multi-AZ and assume it survives a regional outage.
- B. Back up one regional table nightly and ask clients to change endpoints manually after an outage.
- C. Use DynamoDB global tables with a deliberate conflict-safe data model, deploy the API in both Regions, and route through Route 53 or Global Accelerator health-based failover.
- D. Send every write to both Regions synchronously from the client without idempotency or conflict design.

## SIM-C-31

**Choose ONE.**

A business states that after a disaster it can lose no more than fifteen minutes of committed data. Which disaster-recovery metric expresses this limit?

- A. A deployment interval of fifteen minutes.
- B. A recovery time objective of fifteen minutes.
- C. A mean time between failures of fifteen minutes.
- D. A recovery point objective of fifteen minutes.

## SIM-C-32

**Choose TWO.**

An internet-facing application runs in an Auto Scaling group behind an Application Load Balancer. It must remain available after one Availability Zone fails and replace instances that pass EC2 status checks but fail application health checks. Which two configurations are required?

- A. Put every instance in one large subnet to simplify routing.
- B. Use only EC2 status checks because they verify every application endpoint.
- C. Place the Auto Scaling group and ALB subnets across at least two Availability Zones.
- D. Configure the Auto Scaling group to use Elastic Load Balancing health checks with an appropriate grace period.
- E. Disable ALB cross-zone behavior and register only one target at a time.

## SIM-C-33

**Choose ONE.**

A write-heavy relational application uses Aurora in one Region. Recovery requires read-local reporting in a second Region, cross-Region replication with low lag, and managed promotion during a regional incident. The application can tolerate a short DNS change but not hours of restore. Which architecture is best?

- A. Use an Aurora global database with a secondary cluster in the recovery Region and rehearse managed switchover or failover.
- B. Take monthly manual snapshots and copy them after the primary Region fails.
- C. Use Multi-AZ DB instances only in the primary Region.
- D. Replicate SQL statements through CloudWatch Logs to an EC2 database.

## SIM-C-34

**Choose ONE.**

A media company stores source videos in S3. A regional outage must not prevent access to newly uploaded originals, and replication must occur automatically to a separately governed recovery account. The workload can accept asynchronous replication. What should be configured?

- A. Use an S3 Lifecycle rule to transition source objects to Glacier in the same Region.
- B. Configure S3 Cross-Region Replication to a versioned destination bucket in the recovery account with an authorized replication role.
- C. Mount the bucket as an EBS volume and enable Multi-Attach in the recovery Region.
- D. Create a Route 53 record for the source bucket without copying any objects.

## SIM-C-35

**Choose ONE.**

A customer-facing platform has an RTO of ten minutes and an RPO under one minute. The recovery Region must be continuously usable for health checks but running full production capacity there at all times is too expensive. Which DR strategy best balances the objectives?

- A. Keep only infrastructure templates with no running services or replicated data.
- B. Use backup and restore from weekly snapshots after declaring the disaster.
- C. Maintain a warm standby deployment with continuously replicated data, reduced application capacity, tested automation to scale, and health-based traffic failover.
- D. Run full production capacity active-active in every Region despite the explicit cost constraint.

## SIM-C-36

**Choose TWO.**

A public endpoint uses Route 53 failover routing between a primary and secondary Region. Which two elements are fundamental for automatic DNS failover?

- A. Set both records to simple routing because simple records have implicit health ordering.
- B. Use a network ACL as the authoritative DNS health checker.
- C. Create primary and secondary failover records for the same name and record type.
- D. Lower TTL to zero and omit all health checks.
- E. Associate an appropriate health evaluation with the primary record or supported alias target.

## SIM-C-37

**Choose ONE.**

A ransomware recovery policy requires centrally managed backups from member accounts, immutable retention in a logically isolated vault, and cross-account recovery copies that workload administrators cannot delete. Which design best meets the requirement?

- A. Enable termination protection on EC2 instances and treat it as immutable backup retention.
- B. Let each workload owner create untagged manual snapshots in the same account.
- C. Export CloudTrail Event history as the only database backup.
- D. Use AWS Backup policies with cross-account copy and logically air-gapped vault controls, separating backup administration from workload accounts.

## SIM-C-38

**Choose ONE.**

A scientific workload performs tightly coupled MPI calculations requiring low-latency, high-bandwidth node-to-node communication and fast shared parallel file access. Jobs run in one Availability Zone and can be resubmitted after failure. Which architecture is most appropriate?

- A. Use compute-optimized EC2 instances in a cluster placement group with Elastic Fabric Adapter and Amazon FSx for Lustre.
- B. Spread instances across Regions behind CloudFront and store scratch data in S3 Glacier Deep Archive.
- C. Run each MPI rank as an independent Lambda function communicating through API Gateway.
- D. Place instances in a spread placement group across many racks, use EFS One Zone for shared files, and carry MPI traffic over the regular VPC network.

## SIM-C-39

**Choose ONE.**

An Auto Scaling web fleet experiences predictable weekday peaks at 09:00 and unpredictable bursts during promotions. The team wants capacity ready before the known peak while retaining automatic response to unexpected demand. Which scaling design is best?

- A. Use only a fixed desired capacity sized for the largest possible promotion throughout the entire month to avoid any scaling events.
- B. Combine scheduled scaling for the known ramp with target tracking scaling for the live workload metric.
- C. Use scale-in protection on every instance and never allow scale out.
- D. Trigger scaling from the number of IAM users in the account.

## SIM-C-40

**Choose TWO.**

Users worldwide upload large files to a regional application. They need static anycast entry addresses, traffic must enter the AWS network near users, and only healthy regional endpoints should receive traffic. The existing application uses ALBs. Which two components meet the requirements?

- A. Replace the upload API with CloudFront signed cookies only.
- B. Publish one changing ALB IP address as a permanent client allow-list entry.
- C. Use an S3 gateway endpoint in each user's home network.
- D. Place AWS Global Accelerator in front of the regional ALB endpoints.
- E. Configure endpoint groups and health-aware traffic dials for the deployed Regions.

## SIM-C-41

**Choose ONE.**

A Lambda function receives 120 requests each second, and each invocation runs for an average of 2 seconds. Ignoring burst variation, approximately how much concurrent execution is required in steady state?

- A. Exactly 120 concurrent executions regardless of duration.
- B. Approximately 60 concurrent executions.
- C. Approximately 240 concurrent executions.
- D. Exactly 2 concurrent executions because the duration is 2 seconds.

## SIM-C-42

**Choose ONE.**

A small team runs a spiky containerized API on ECS. It has no Kubernetes dependency, must scale to zero tasks overnight, and the team does not want to patch or size EC2 cluster hosts. Which compute option has the lowest operational overhead?

- A. Package the container as an Amazon Machine Image and launch it manually for every request.
- B. Run ECS on a fixed fleet of On-Demand EC2 instances sized for the annual peak.
- C. Migrate to Amazon EKS solely to avoid managing worker infrastructure.
- D. Run the ECS tasks on AWS Fargate and use service scaling for demand.

## SIM-C-43

**Choose ONE.**

A global product catalog serves mostly cacheable reads through API Gateway and Lambda, but a personalized endpoint must query DynamoDB. Latency spikes from cold starts and repeated database reads are breaching the SLA. Which redesign best targets both paths without caching private responses globally?

- A. Cache public catalog responses at CloudFront, use provisioned concurrency for the latency-critical Lambda path, and add DynamoDB DAX only if the personalized access pattern benefits from read-through caching.
- B. Cache every personalized response at CloudFront with a single shared cache key.
- C. Increase Lambda ephemeral storage and disable DynamoDB partition keys.
- D. Move all catalog data to instance store on one EC2 instance in one Region.

## SIM-C-44

**Choose TWO.**

A DynamoDB table receives IoT writes with deviceId as the partition key. One fleet gateway represents 40 percent of devices and causes throttling, while operators also need to query recent alarms by severity. Which two design changes address the hot write path and new query pattern?

- A. Increase partition-key cardinality by distributing the gateway workload across deterministic write shards.
- B. Create a global secondary index whose partition and sort keys support severity and event-time queries.
- C. Create a local secondary index after the table is already in production with severity as a new partition key.
- D. Increase item size so DynamoDB allocates more partitions to the gateway key.
- E. Use a strongly consistent Scan for every recent alarm request.

## SIM-C-45

**Choose ONE.**

A multi-tenant SaaS platform uses PostgreSQL and has unpredictable connection bursts from Lambda. Tenants require relational transactions, read scaling, and automatic capacity growth without a planned migration window. Which architecture best balances performance and operations?

- A. Use one DynamoDB table and emulate every multi-row relational transaction in the browser.
- B. Use Aurora PostgreSQL-Compatible with Aurora Serverless v2 capacity ranges, reader instances or endpoints, and RDS Proxy for Lambda connection pooling.
- C. Run PostgreSQL on a single EC2 Spot Instance with local NVMe as the only database copy.
- D. Create a new full Aurora cluster for every request and delete it after the transaction.

## SIM-C-46

**Choose ONE.**

An RDS database needs additional capacity for read-only reporting queries. The reporting workload may accept replication lag and does not need to become the synchronous standby automatically. Which feature directly addresses the requirement?

- A. Increase backup retention and query the automated backups.
- B. Enable Multi-AZ and direct reporting queries to the standby endpoint.
- C. Create an RDS read replica and direct reporting connections to it.
- D. Create an RDS event subscription for SELECT statements.

## SIM-C-47

**Choose ONE.**

Private subnets send large DynamoDB API traffic through NAT Gateways. The application must keep traffic on the AWS network and reduce recurring NAT processing charges without changing the SDK calls. Which network change is most appropriate?

- A. Peer the VPC with itself and send DynamoDB traffic through the peering route.
- B. Create a public IPv4 address for every application instance.
- C. Deploy an interface endpoint for an unrelated service and route DynamoDB through it.
- D. Create a DynamoDB gateway VPC endpoint, associate the private route tables, and restrict the endpoint policy as required.

## SIM-C-48

**Choose TWO.**

A trading company needs a dedicated path from its datacenter to AWS with predictable performance and IPsec encryption. It also requires an independent backup path that can fail over if the dedicated circuit is unavailable. Which two components form the primary and backup design?

- A. Use only a NAT Gateway as the datacenter customer gateway.
- B. Configure a separate Site-to-Site VPN over the internet as the independent backup path.
- C. Use AWS Direct Connect for the dedicated primary transport and an appropriate virtual interface.
- D. Establish AWS Site-to-Site VPN over an appropriate Direct Connect public virtual interface for IPsec on the primary path.
- E. Use VPC peering as the physical circuit between the datacenter and AWS.

## SIM-C-49

**Choose ONE.**

A company has eighty VPCs, several Site-to-Site VPNs, and separate development and production routing domains. It needs transitive hub routing with centralized inspection while preventing development routes from reaching production. Which service is best?

- A. Use AWS Transit Gateway with separate route tables, controlled associations and propagations, and inspection attachments.
- B. Create a full mesh of VPC peering connections and designate selected peer VPCs as transit hubs for transitive routing across every connected network.
- C. Use one Internet Gateway as a private transit router for all VPCs and VPNs.
- D. Attach every VPC to one NAT Gateway and use security groups as route tables.

## SIM-C-50

**Choose ONE.**

A gaming platform emits clickstream events worldwide. It needs subsecond anomaly aggregates, durable raw delivery to partitioned S3 for later SQL, schema discovery, and independent replay during an incident. Which architecture best meets the combined requirements?

- A. Send all events directly to S3 Glacier Deep Archive and run one annual Athena query.
- B. Ingest through Kinesis Data Streams, process stateful windows with Managed Service for Apache Flink, and deliver a separate stream path to Firehose for partitioned S3 storage cataloged by Glue.
- C. Put all consumers on one SQS queue and assume each receives a complete replayable copy.
- D. Write events to an RDS instance through synchronous global client connections.

## SIM-C-51

**Choose ONE.**

Analysts run occasional SQL queries directly against partitioned Parquet files in Amazon S3 and do not want to administer a database cluster. Which service is the most direct fit?

- A. Use Amazon ElastiCache as the authoritative SQL engine for Parquet.
- B. Use Amazon RDS for Oracle and copy every object into a relational table first.
- C. Use Amazon Athena and pay according to the data scanned by queries.
- D. Use Amazon SNS message filtering to execute SELECT statements.

## SIM-C-52

**Select THREE.**

A data lake receives daily CSV exports and continuous JSON events. The company needs managed transformation into partitioned Parquet, a shared catalog for Athena, and fine-grained cross-account table permissions. Which three components meet the requirements?

- A. Use AWS Glue jobs or appropriate Glue serverless ETL capabilities to transform source data into Parquet.
- B. Use AWS Glue Data Catalog for table schemas and partition metadata.
- C. Use AWS Lake Formation to govern supported table, column, and cross-account data permissions.
- D. Use Amazon Route 53 hosted zones as the schema registry.
- E. Use EBS snapshots as the cross-account permission system for S3 tables.
- F. Use Amazon Polly to convert JSON events into Parquet files.

## SIM-C-53

**Choose ONE.**

A compliance archive ingests objects into S3 Standard, reads most during the first month, rarely reads them for six years, and must delete them after year seven. Retrieval after month one can take hours. Which design minimizes storage cost while preserving automated retention?

- A. Move objects to S3 One Zone-IA even if the archive requires resilience to loss of an Availability Zone.
- B. Keep every object in S3 Standard for seven years because lifecycle transitions always reduce durability.
- C. Copy every object to EC2 instance store after one month.
- D. Use an S3 Lifecycle policy to transition eligible objects to an appropriate Glacier class after the active period and expire them after the required retention boundary.

## SIM-C-54

**Choose ONE.**

A database uses a 2 TiB gp2 EBS volume only to obtain sufficient baseline IOPS, but actual capacity needs are 500 GiB. Performance monitoring shows 6,000 IOPS and 250 MiB/s are adequate. Which change is most cost-effective?

- A. Migrate to a properly sized gp3 volume and provision the required IOPS and throughput independently of capacity.
- B. Increase the gp2 volume to 4 TiB so baseline IOPS doubles.
- C. Move the database files to EC2 instance store without replication.
- D. Create hourly EBS snapshots and use snapshots as the live database volume.

## SIM-C-55

**Choose ONE.**

A document repository has unpredictable object access: some files are opened weekly, others become cold for months, and access patterns change without notice. The team wants automatic savings without retrieval fees or operational analysis of each object. Which class is best?

- A. Put every object immediately into S3 Glacier Deep Archive.
- B. Use S3 Intelligent-Tiering and enable the archive tiers only if their retrieval behavior is acceptable.
- C. Keep all objects permanently in S3 Standard, manually review every access log each day, and change storage classes by hand.
- D. Store the repository on one EC2 instance store volume.

## SIM-C-56

**Select THREE.**

A storage review must distinguish durable block, shared file, and archival object options before optimization. Which three statements are correct?

- A. Amazon EBS volumes provide persistent block storage for supported EC2 attachment patterns within an Availability Zone.
- B. EC2 instance store is the preferred durable system of record after an instance is stopped or terminated.
- C. A NAT Gateway is a shared POSIX file system for private subnets.
- D. Amazon EFS provides managed shared file access for multiple Linux clients across Availability Zones in a Region.
- E. S3 Glacier storage classes are object-storage archival tiers with retrieval-time and minimum-duration tradeoffs.
- F. CloudFront edge caches are authoritative block-device backups for EBS volumes.

## SIM-C-57

**Choose ONE.**

A company runs steady EC2 and Fargate production workloads in several Regions, but instance families may change during modernization. It can commit to a consistent hourly compute spend for three years. Which discount model offers the most flexibility?

- A. Use Spot Instances for every production task regardless of interruption tolerance.
- B. Purchase Standard Reserved Instances for one exact family and assume they cover Fargate.
- C. Purchase a Compute Savings Plan sized to the conservative baseline spend.
- D. Prepay three years of NAT Gateway hourly charges as a Savings Plan.

## SIM-C-58

**Choose ONE.**

A rendering platform has a steady queue plus large overnight bursts. Jobs checkpoint every five minutes and can be retried on interruption. The company wants guaranteed baseline completion capacity and the lowest cost for burst capacity. Which design is best?

- A. Move the render queue to Glacier Deep Archive and retrieve it before each job.
- B. Run every worker on one Spot instance type in one Availability Zone with no interruption handling.
- C. Reserve peak On-Demand capacity all day even though bursts occur only overnight.
- D. Run the baseline on On-Demand or committed compute and scale the retryable burst workers on EC2 Spot capacity diversified across instance types and Availability Zones.

## SIM-C-59

**Choose ONE.**

A Lambda image transformation function uses 512 MB and runs for 12 seconds. Testing shows that 1,536 MB finishes in 3 seconds, and both configurations meet correctness requirements. What should the team do before choosing the cheaper setting?

- A. Compare measured GB-seconds, request charges, and downstream effects for both configurations, then select the best cost-performance point.
- B. Always select the minimum memory because Lambda price depends only on configured memory.
- C. Always select maximum memory because shorter execution is automatically free.
- D. Move the function to a public subnet because public subnets reduce Lambda GB-second pricing.

## SIM-C-60

**Select THREE.**

A database estate includes predictable production RDS instances, an Aurora cluster with high I/O charges, and development databases idle every night. Which three actions should be evaluated for cost optimization without violating workload requirements?

- A. Delete automated backups for production because recovery does not affect cost architecture.
- B. Purchase appropriate Reserved DB Instances for the stable, well-measured RDS baseline.
- C. Scale every database to the largest instance class to reduce query duration.
- D. Compare Aurora I/O-Optimized with the standard configuration using the cluster's actual I/O-to-compute cost profile.
- E. Convert relational workloads with joins and constraints to ElastiCache without application analysis.
- F. Schedule supported nonproduction DB instances to stop and start during verified idle windows.

## SIM-C-61

**Choose ONE.**

A new DynamoDB application has unknown and highly variable request traffic. The team wants to avoid capacity forecasting and throttling caused by an incorrect initial provisioned setting. Which capacity mode is the simplest starting choice?

- A. Use provisioned capacity fixed permanently at one read and one write unit.
- B. Use DynamoDB on-demand capacity mode.
- C. Use an EC2 Auto Scaling group to add DynamoDB partitions manually.
- D. Use S3 Intelligent-Tiering as the table capacity controller.

## SIM-C-62

**Choose ONE.**

An Aurora workload's monthly I/O charges consistently exceed its instance charges, and load testing confirms the same high read and write volume after query tuning. The team wants predictable database cost without reducing throughput. What should it evaluate?

- A. Move all tables to one Lambda execution environment's temporary storage and rely on environment reuse to persist the database between invocations.
- B. Disable database backups and transaction logging to remove I/O.
- C. Compare the cluster's measured break-even point with Aurora I/O-Optimized and switch if the total cost is lower.
- D. Add more cross-Region replicas solely to reduce primary I/O billing.

## SIM-C-63

**Choose ONE.**

A global download service sends large immutable objects from an S3 origin to users on five continents. Costs are dominated by repeated origin transfer, NAT processing from private application hosts, and cross-AZ calls to a centralized NAT Gateway. Which redesign best improves both cost and resilience?

- A. Copy the objects to EBS volumes attached to a single web server.
- B. Assign public IPv4 addresses to every private host and bypass all security controls.
- C. Route all Regions through one NAT Gateway in the origin Region.
- D. Serve cacheable objects through CloudFront, use an S3 gateway endpoint for private host access, and route remaining egress through zonally aligned NAT Gateways where volume and resilience justify them.

## SIM-C-64

**Select THREE.**

A multi-AZ application transfers terabytes each month to S3, sends static responses globally, and uses interface endpoints for services that support gateway endpoints. Which three actions directly target recurring network charges?

- A. Send S3 traffic through a NAT Gateway in a different Availability Zone.
- B. Disable compression for all text responses.
- C. Use an S3 gateway endpoint for VPC-to-S3 traffic and associate the required route tables.
- D. Add public IPv4 addresses to all instances solely to avoid endpoint hourly charges.
- E. Cache eligible static content with CloudFront and tune cache keys and TTLs.
- F. Review endpoint type and consolidate or remove unnecessary interface endpoints while preserving required private connectivity.

## SIM-C-65

**Choose ONE.**

A company exports 8 TB of analytics data from AWS to the same on-premises facility every month. The transfer is steady, internet performance is inconsistent, and finance wants a predictable private connectivity model. Which option should be evaluated first?

- A. Evaluate AWS Direct Connect capacity and data-transfer pricing against the steady volume and required redundancy.
- B. Create a larger NAT Gateway because NAT provides a dedicated circuit to the facility, and assign it a fixed public IP for deterministic routing.
- C. Use an S3 gateway endpoint from the on-premises network through Transit Gateway.
- D. Send the monthly dataset through Route 53 Resolver outbound endpoints.
