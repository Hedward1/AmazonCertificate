# B21 — Questões: Organizations, IAM avançado, KMS e Parameter Store

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione uma resposta<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B21_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B21-01 | 1.1 | SCP behavior | Situacional | Basic | Inglês |
| B21-02 | 1.1 | Explicit deny | Situacional | Intermediate | Inglês |
| B21-03 | 1.1 | Role trust policy | Situacional | Intermediate | Inglês |
| B21-04 | 1.1 | IAM Identity Center | Situacional | Basic | Inglês |
| B21-05 | 1.1 | Directory Service | Situacional | Basic | Inglês |
| B21-06 | 1.1 | Control Tower | Situacional | Intermediate | Inglês |
| B21-07 | 1.3 | Envelope encryption | Situacional | Intermediate | Inglês |
| B21-08 | 1.3 | Multi-Region KMS keys | Situacional | Advanced | Inglês |
| B21-09 | 1.2 | Parameter Store | Situacional | Basic | Inglês |
| B21-10 | 1.3 | Encrypted AMI sharing | Situacional | Advanced | Inglês |

## Questões

### B21-01

**Context:** A member account has an SCP that allows Amazon S3. A new IAM role has no identity-based policies.

**Requirement:** The role must list an S3 bucket.

**Question:** What is the current authorization result?

- A. Allowed because the SCP grants S3.
- B. Denied because an SCP does not grant permissions and the role has no Allow.
- C. Allowed only from the management account.
- D. Allowed because implicit deny applies only to users.

**Before moving on:** record decisive words and confidence.

### B21-02

**Context:** A role has AdministratorAccess, but an SCP attached to its OU explicitly denies ec2:TerminateInstances.

**Requirement:** The role attempts to terminate an EC2 instance in the member account.

**Question:** What happens?

- A. The action is allowed because AdministratorAccess is broader.
- B. The action is allowed after adding a second identity-based Allow.
- C. The action is denied because an applicable explicit Deny prevails.
- D. The action is allowed if the instance is tagged.

**Before moving on:** record decisive words and confidence.

### B21-03

**Context:** A workload in account A must assume a role in account B.

**Requirement:** The destination must define which principal is trusted to assume the role.

**Question:** Which policy provides that control?

- A. The role trust policy in account B.
- B. An S3 lifecycle policy.
- C. A CloudWatch alarm policy.
- D. A tag policy.

**Before moving on:** record decisive words and confidence.

### B21-04

**Context:** Employees need single sign-on to many AWS accounts by using short-lived credentials.

**Requirement:** Administrators want centrally assigned permission sets.

**Question:** Which service should be used?

- A. AWS Directory Service alone.
- B. AWS IAM Identity Center.
- C. AWS KMS.
- D. Amazon Cognito user pools.

**Before moving on:** record decisive words and confidence.

### B21-05

**Context:** A legacy application requires a managed Microsoft Active Directory domain and domain join.

**Requirement:** The solution must provide Microsoft AD compatibility in AWS.

**Question:** Which service is the best fit?

- A. AWS IAM Identity Center only.
- B. AWS CloudFormation.
- C. AWS Directory Service for Microsoft Active Directory.
- D. AWS WAF.

**Before moving on:** record decisive words and confidence.

### B21-06

**Context:** A company needs a governed multi-account landing zone with account provisioning and preventive and detective controls.

**Requirement:** The solution should orchestrate established AWS governance services.

**Question:** Which service meets the requirement?

- A. Amazon GuardDuty.
- B. AWS Control Tower.
- C. Amazon EventBridge.
- D. AWS Batch.

**Before moving on:** record decisive words and confidence.

### B21-07

**Context:** An application must encrypt a large object while using AWS KMS to protect key material.

**Requirement:** The design should follow envelope encryption.

**Question:** Which process is correct?

- A. Encrypt the entire object directly with an SCP.
- B. Use a plaintext data key to encrypt the object, store its encrypted copy, and discard the plaintext key.
- C. Store the plaintext data key in tags.
- D. Use a CloudWatch alarm as the encryption key.

**Before moving on:** record decisive words and confidence.

### B21-08

**Context:** Ciphertext created in one Region must be decrypted locally in another Region without a cross-Region KMS call.

**Requirement:** The related keys must have interoperable key material.

**Question:** Which statement is correct?

- A. Copying an alias replicates the key material.
- B. A single-Region key automatically appears globally.
- C. A multi-Region primary and replica share related key material, while policies and state remain independent.
- D. Replicating the KMS key also replicates application data.

**Before moving on:** record decisive words and confidence.

### B21-09

**Context:** An application needs hierarchical configuration values and a few encrypted strings. Managed credential rotation is not required.

**Requirement:** The team wants a Systems Manager capability.

**Question:** Which service should it choose?

- A. AWS Systems Manager Parameter Store.
- B. Amazon MSK.
- C. AWS Shield Advanced.
- D. Amazon Quick Sight.

**Before moving on:** record decisive words and confidence.

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

**Before moving on:** record decisive words and confidence.

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
