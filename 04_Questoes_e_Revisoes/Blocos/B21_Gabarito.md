# B21 — Gabarito comentado

Volte às [questões B21](B21_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B21-01 | B | 1.1 |
| B21-02 | C | 1.1 |
| B21-03 | A | 1.1 |
| B21-04 | B | 1.1 |
| B21-05 | C | 1.1 |
| B21-06 | B | 1.1 |
| B21-07 | B | 1.3 |
| B21-08 | C | 1.3 |
| B21-09 | A | 1.2 |
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

## B21-04 — Answer B

- **Central requirement:** Administrators want centrally assigned permission sets.
- **Decisive words:** employees, SSO, many accounts, permission sets
- **Why the correct answer works:** IAM Identity Center centrally manages workforce access and permission sets across AWS accounts.
- **A:** Directory Service alone is not the account access portal.
- **B:** This is correct.
- **C:** KMS manages cryptographic keys.
- **D:** Cognito serves application customers.
- **Reusable rule:** Workforce multi-account SSO points to IAM Identity Center.
- **Cost/operation:** Avoid duplicating IAM users and long-lived keys.
- **Variation:** An external identity provider can be connected as the identity source.
- **Lessons:** 288–291
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

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

## B21-07 — Answer B

- **Central requirement:** The design should follow envelope encryption.
- **Decisive words:** large object, KMS, envelope encryption
- **Why the correct answer works:** Envelope encryption uses a data key for data and a KMS key to protect the data key.
- **A:** SCP is authorization, not encryption.
- **B:** This is correct.
- **C:** Tags are not secret storage.
- **D:** An alarm is not a key.
- **Reusable rule:** Data key encrypts data; KMS key encrypts the data key.
- **Cost/operation:** KMS requests and customer managed keys can incur charges.
- **Variation:** Encryption context can add authenticated non-secret context.
- **Lessons:** 292–295
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping)

## B21-08 — Answer C

- **Central requirement:** The related keys must have interoperable key material.
- **Decisive words:** decrypt locally, another Region, interoperable material
- **Why the correct answer works:** Related multi-Region keys share key ID and material, but each regional key has independent policy, aliases, grants, and state.
- **A:** Aliases do not copy key material.
- **B:** Single-Region keys remain regional.
- **C:** This is correct.
- **D:** Data replication is a separate design.
- **Reusable rule:** Multi-Region KMS keys replicate key material, not data or all properties.
- **Cost/operation:** Each customer managed regional key and its requests can be billed.
- **Variation:** Prefer single-Region keys without an explicit multi-Region need.
- **Lessons:** 296–298
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html)

## B21-09 — Answer A

- **Central requirement:** The team wants a Systems Manager capability.
- **Decisive words:** hierarchical configuration, encrypted strings, no rotation
- **Why the correct answer works:** Parameter Store provides hierarchical String, StringList, and KMS-backed SecureString parameters.
- **A:** This is correct.
- **B:** MSK is Kafka.
- **C:** Shield is DDoS protection.
- **D:** Quick Sight is BI.
- **Reusable rule:** Configuration and simple secrets without managed rotation point to Parameter Store.
- **Cost/operation:** Advanced parameters and higher throughput can incur charges.
- **Variation:** Managed database credential rotation points to Secrets Manager.
- **Lessons:** 299–300
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

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
