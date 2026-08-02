# B21 — Gabarito comentado

Volte às [questões B21](B21_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B21-01 | B | 1.1 |
| B21-02 | C | 1.1 |
| B21-03 | A | 1.1 |
| B21-04 | B,E | 1.1 |
| B21-05 | C | 1.1 |
| B21-06 | B | 1.1 |
| B21-07 | B,D | 1.3 |
| B21-08 | C | 1.3 |
| B21-09 | A,C,F | 1.2 |
| B21-10 | D | 1.3 |

## B21-01 — Answer B

- **Central requirement:** The role must list an S3 bucket.
- **Decisive words:** SCP allows, no identity policy
- **Why the correct answer works:** SCPs set permission guardrails but do not grant permissions; the role still needs an applicable Allow.
- **A:** An SCP does not grant.
- **B:** This is correct.
- **C:** The principal is in a member account.
- **D:** Implicit deny applies to roles too.
- **Reusable rule:** SCP defines the maximum; permissions policies grant access.
- **Cost/operation:** Test SCPs in a dedicated OU before broad attachment.
- **Variation:** A deny SCP can restrict even an administrator role.
- **Lessons:** 283–287
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

## B21-02 — Answer C

- **Central requirement:** The role attempts to terminate an EC2 instance in the member account.
- **Decisive words:** AdministratorAccess, SCP, explicit denies
- **Why the correct answer works:** An explicit deny in an applicable SCP overrides identity-based allows.
- **A:** AdministratorAccess cannot override an SCP deny.
- **B:** Another Allow does not override Deny.
- **C:** This is correct.
- **D:** No tag exception was specified.
- **Reusable rule:** Any applicable explicit Deny wins.
- **Cost/operation:** A broad deny can cause operational outages.
- **Variation:** SCPs do not restrict users and roles in the management account.
- **Lessons:** 283–287
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)

## B21-03 — Answer A

- **Central requirement:** The destination must define which principal is trusted to assume the role.
- **Decisive words:** assume role, destination, trusted principal
- **Why the correct answer works:** The trust policy is the resource-based policy on the role that specifies trusted principals.
- **A:** This is correct.
- **B:** Lifecycle controls objects.
- **C:** Alarm policy is unrelated.
- **D:** Tag policy does not create trust.
- **Reusable rule:** Trust policy answers who can assume; permissions policy answers what the session can do.
- **Cost/operation:** Temporary sessions avoid long-lived access keys.
- **Variation:** The origin also needs permission to call sts:AssumeRole.
- **Lessons:** 285–288
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html)

## B21-04 — Answer B,E

- **Central requirement:** centralize workforce account access and share supported network resources across organization accounts.
- **Decisive words:** *short-lived access*, *permission sets*, *shared subnets*, *without peering*.
- **A:** incorrect; Cognito user pools serve application identities, not workforce AWS account permission sets.
- **B:** correct; IAM Identity Center centrally assigns workforce access and permission sets.
- **C:** incorrect; KMS grants authorize cryptographic key use and do not share subnets.
- **D:** incorrect; Directory Service alone is not a general supported-resource sharing mechanism.
- **E:** correct; AWS RAM shares supported resources, including subnets, with accounts or organizational units.
- **Reusable rule:** Identity Center answers who can access accounts; RAM answers which supported resources accounts can use together.
- **Lessons:** 288–291.
- **Official reference:** [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) and [VPC sharing with AWS RAM](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html).

## B21-05 — Answer C

- **Central requirement:** The solution must provide Microsoft AD compatibility in AWS.
- **Decisive words:** Microsoft Active Directory, domain join
- **Why the correct answer works:** AWS Managed Microsoft AD in Directory Service provides a managed Microsoft AD domain.
- **A:** Identity Center is not itself the required AD domain.
- **B:** CloudFormation is IaC.
- **C:** This is correct.
- **D:** WAF filters web requests.
- **Reusable rule:** Managed Microsoft AD requirements point to Directory Service.
- **Cost/operation:** Directory resources can incur continuous hourly charges.
- **Variation:** Identity Center may use a directory as its identity source.
- **Lessons:** 289–290
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)

## B21-06 — Answer B

- **Central requirement:** The solution should orchestrate established AWS governance services.
- **Decisive words:** landing zone, account provisioning, controls
- **Why the correct answer works:** Control Tower sets up and governs a landing zone by orchestrating services such as Organizations and IAM Identity Center.
- **A:** GuardDuty detects threats.
- **B:** This is correct.
- **C:** EventBridge routes events.
- **D:** Batch runs jobs.
- **Reusable rule:** Governed multi-account landing zone points to Control Tower.
- **Cost/operation:** Do not enable a landing zone only for a personal lab; integrated services can charge.
- **Variation:** Organizations alone provides account hierarchy but not the complete landing-zone experience.
- **Lessons:** 291
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)

## B21-07 — Answer B,D

- **Central requirement:** encrypt a large payload locally while KMS protects the data-encryption key.
- **Decisive words:** *multi-gigabyte*, *avoid sending entire object to KMS*, *later decryption*.
- **A:** incorrect; KMS cryptographic APIs have payload-size limits and are not bulk-data engines.
- **B:** correct; `GenerateDataKey` returns a plaintext key for local use and an encrypted copy.
- **C:** incorrect; plaintext key material must not be persisted in tags or metadata.
- **D:** correct; retaining the encrypted data key enables later KMS decryption while erasing plaintext reduces exposure.
- **E:** incorrect; an SCP is an authorization guardrail, not cryptographic key material.
- **Reusable rule:** envelope encryption stores ciphertext plus the encrypted data key, never the retained plaintext data key.
- **Lessons:** 292–295.
- **Official reference:** [Envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping).

## B21-08 — Answer C

- **Central requirement:** decrypt replicated data locally with related material while retaining independent regional authorization and lifecycle controls.
- **Decisive words:** active-active, isolation event, local decrypt, independent policy and state
- **Why the correct answer works:** Related multi-Region keys have interoperable key material, but each regional key remains a separately managed resource for policy, grants, aliases, and state.
- **A:** an alias is a regional pointer and does not copy key material or authorization configuration.
- **B:** a single-Region key remains regional; depending on a remote key contradicts the isolation requirement.
- **C:** correct; it separates the cryptographic relationship from regional control and from the application's data-replication mechanism.
- **D:** KMS key replication does not copy ciphertext objects, S3 replication configuration, or bucket policy.
- **Reusable rule:** multi-Region KMS keys replicate compatible key material only; design data replication, access policy, state, monitoring, and cost per Region.
- **Cost/operation:** Each customer managed regional key and its requests can be billed.
- **Variation:** Prefer single-Region keys without an explicit multi-Region need.
- **Lessons:** 296–298
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html)

## B21-09 — Answer A,C,F

- **Central requirement:** store hierarchical encrypted configuration and authorize only one application role and KMS key.
- **Decisive words:** *hierarchical*, *encrypted*, *no managed rotation*, *least privilege*.
- **A:** correct; Parameter Store provides hierarchies and KMS-backed `SecureString` values.
- **B:** incorrect; user data is retrievable instance metadata and is unsuitable for plaintext secrets.
- **C:** correct; the designated KMS key protects the `SecureString` values.
- **D:** incorrect; account-wide path access violates the explicit least-privilege requirement.
- **E:** incorrect; MSK is managed Kafka, not a configuration hierarchy.
- **F:** correct; scoped parameter and KMS permissions restrict retrieval and decryption to the application role.
- **Reusable rule:** Parameter Store fits configuration/simple secrets without rotation; combine resource scoping and KMS authorization.
- **Lessons:** 299–300.
- **Official reference:** [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html).

## B21-10 — Answer D

- **Central requirement:** Account B must be able to launch the image.
- **Decisive words:** shared AMI, encrypted snapshots, another account
- **Why the correct answer works:** The recipient needs AMI launch permission
  and authorization to use the customer managed KMS key. EC2 provides launch
  access to the referenced snapshots through the shared AMI, so those snapshots
  do not need separate sharing.
- **A:** Viewing a name is insufficient.
- **B:** An SCP does not grant access.
- **C:** An unrelated key cannot decrypt snapshots.
- **D:** This is correct; AMI permission plus KMS authorization is required,
  without separately sharing the referenced snapshots.
- **Reusable rule:** Sharing an encrypted AMI requires launch permission and
  customer managed KMS key access; do not add a separate snapshot-sharing step.
- **Cost/operation:** Copied snapshots and KMS use can incur charges.
- **Variation:** AWS managed keys generally cannot be shared cross-account in the same way.
- **Lessons:** 297–298
- **Official reference:** [Share an AMI with specific AWS accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html)
