# B21 — Questões: Organizations, IAM avançado, KMS e Parameter Store

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione a quantidade indicada em cada questão<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B21_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B21-01 | 1.1 | SCP behavior | single | fundamental | básica | Inglês |
| B21-02 | 1.1 | Explicit deny | single | situacional | intermediária | Inglês |
| B21-03 | 1.1 | Role trust policy | single | situacional | intermediária | Inglês |
| B21-04 | 1.1 | Identity Center and RAM | multi-2 | situacional | avançada | Inglês |
| B21-05 | 1.1 | Directory Service | single | situacional | intermediária | Inglês |
| B21-06 | 1.1 | Control Tower | single | situacional | intermediária | Inglês |
| B21-07 | 1.3 | Envelope encryption | multi-2 | integrada | avançada | Inglês |
| B21-08 | 1.3 | Multi-Region KMS keys | single | integrada | avançada | Inglês |
| B21-09 | 1.2 | Configuration and secrets | multi-3 | integrada | avançada | Inglês |
| B21-10 | 1.3 | Encrypted AMI sharing | single | integrada | avançada | Inglês |

## Questões

### B21-01

**Context:** A member account has an SCP that allows Amazon S3. A new IAM role has no identity-based policies.

**Requirement:** The role must list an S3 bucket.

**Question:** What is the current authorization result?

- A. Allowed because the SCP grants S3.
- B. Denied because an SCP does not grant permissions and the role has no Allow.
- C. Allowed only from the management account.
- D. Allowed because implicit deny applies only to users.

### B21-02

**Context:** A role has AdministratorAccess, but an SCP attached to its OU explicitly denies ec2:TerminateInstances.

**Requirement:** The role attempts to terminate an EC2 instance in the member account.

**Question:** What happens?

- A. The action is allowed because AdministratorAccess is broader.
- B. The action is allowed after adding a second identity-based Allow.
- C. The action is denied because an applicable explicit Deny prevails.
- D. The action is allowed if the instance is tagged.

### B21-03

**Context:** A workload in account A must assume a role in account B.

**Requirement:** The destination must define which principal is trusted to assume the role.

**Question:** Which policy provides that control?

- A. The role trust policy in account B.
- B. An S3 lifecycle policy.
- C. A CloudWatch alarm policy.
- D. A tag policy.

### B21-04

**Context:** Employees need centrally assigned, short-lived access to many AWS accounts. Application teams in those accounts must also use subnets shared from a central networking account without VPC peering.

**Requirement:** Select the managed service for workforce access and the service for sharing supported resources across the organization. **Choose TWO.**

- A. Use Amazon Cognito user pools for AWS Management Console permission sets.
- B. Use AWS IAM Identity Center for workforce access and permission sets.
- C. Use AWS KMS grants to share VPC subnets.
- D. Use AWS Directory Service alone to share every supported AWS resource.
- E. Use AWS Resource Access Manager (AWS RAM) to share the supported subnets.

### B21-05

**Context:** A legacy application requires a managed Microsoft Active Directory domain and domain join.

**Requirement:** The solution must provide Microsoft AD compatibility in AWS.

**Question:** Which service is the best fit?

- A. AWS IAM Identity Center only.
- B. AWS CloudFormation.
- C. AWS Directory Service for Microsoft Active Directory.
- D. AWS WAF.

### B21-06

**Context:** A company needs a governed multi-account landing zone with account provisioning and preventive and detective controls.

**Requirement:** The solution should orchestrate established AWS governance services.

**Question:** Which service meets the requirement?

- A. Amazon GuardDuty.
- B. AWS Control Tower.
- C. Amazon EventBridge.
- D. AWS Batch.

### B21-07

**Context:** An application encrypts multi-gigabyte objects and uses AWS KMS to protect key material. It must avoid sending the entire object to KMS and must retain what is needed for later decryption.

**Requirement:** Implement envelope encryption correctly. **Choose TWO.**

- A. Send the full object to the KMS `Encrypt` API.
- B. Call `GenerateDataKey` and use the plaintext data key locally to encrypt the object.
- C. Store the plaintext data key permanently in object tags.
- D. Store the encrypted data key with the ciphertext and erase the plaintext key from memory after use.
- E. Use an Organizations SCP as the symmetric data key.

### B21-08

**Context:** An active-active application replicates encrypted objects between
two Regions. Each Region must decrypt locally during an isolation event, but
security teams need independent regional key policies, grants, aliases, and the
ability to disable one regional key without automatically disabling the other.

**Requirement:** Reuse compatible cryptographic material without assuming that
KMS also replicates data or authorization configuration.

**Question:** Which design statement is correct?

- A. Copy the key alias to the second Region; aliases reproduce key material and policy automatically.
- B. Use one single-Region KMS key because its ARN is globally callable during a regional isolation event.
- C. Use a multi-Region primary and replica: related keys share interoperable key material, while policy, grants, aliases, enabled state, and application-data replication remain regional concerns.
- D. Replicate the KMS key and rely on KMS to copy every encrypted S3 object and its bucket policy.

### B21-09

**Context:** EC2 applications need hierarchical configuration and several encrypted values. Managed credential rotation is not required, and access must be limited to one application role and one KMS key.

**Requirement:** Use the lowest-operations Systems Manager capability with least privilege. **Select THREE.**

- A. Store the hierarchy in Systems Manager Parameter Store and encrypted values as `SecureString` parameters.
- B. Store plaintext secrets in EC2 user data because the instances are private.
- C. Encrypt `SecureString` values with the designated KMS key.
- D. Grant all account roles `ssm:GetParametersByPath` on every parameter.
- E. Use Amazon MSK as the configuration hierarchy.
- F. Grant the application role only the required parameter ARNs and KMS decrypt permission.

### B21-10

**Context:** Account A must share an AMI whose EBS snapshots are encrypted with a customer managed KMS key with account B.

**Requirement:** Account B must be able to launch the image.

**Question:** Which access is required?

- A. Only permission to view the AMI name.
- B. Only an SCP Allow in account B.
- C. Only access to an unrelated AWS managed key.
- D. AMI launch permission and permission to use the relevant customer managed
  KMS key; the snapshots referenced by the shared AMI do not need to be shared
  separately.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B21-01 |  |  |  |
| B21-02 |  |  |  |
| B21-03 |  |  |  |
| B21-04 |  |  |  |
| B21-05 |  |  |  |
| B21-06 |  |  |  |
| B21-07 |  |  |  |
| B21-08 |  |  |  |
| B21-09 |  |  |  |
| B21-10 |  |  |  |
