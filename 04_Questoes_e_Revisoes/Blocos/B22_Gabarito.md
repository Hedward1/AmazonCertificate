# B22 — Gabarito comentado

Volte às [questões B22](B22_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B22-01 | A | 1.2 |
| B22-02 | B | 1.3 |
| B22-03 | C | 1.3 |
| B22-04 | B,D | 1.2 |
| B22-05 | A | 1.2 |
| B22-06 | B | 1.2 |
| B22-07 | A,E | 1.2 |
| B22-08 | D | 3.4 |
| B22-09 | A,C,F | 1.2 |
| B22-10 | B | 1.2 |

## B22-01 — Answer A

- **Central requirement:** The credential must be stored securely and rotated automatically on a schedule.
- **Decisive words:** database password, rotated automatically
- **Why the correct answer works:** Secrets Manager is designed for secret storage, versioning, access control, and managed rotation.
- **A:** This is correct.
- **B:** A plain String is not encrypted and Parameter Store does not provide the same managed rotation workflow.
- **C:** Tags are not secret storage.
- **D:** Outputs must not expose secrets.
- **Reusable rule:** Managed credential rotation points to Secrets Manager.
- **Cost/operation:** Secrets and API calls can incur charges; deletion has recovery behavior.
- **Variation:** SecureString can fit a simple encrypted parameter when managed rotation is not required.
- **Lessons:** 301–302
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

## B22-02 — Answer B

- **Central requirement:** The certificate should be provisioned and renewed with minimal operations.
- **Decisive words:** ALB, TLS, managed certificate, renewal
- **Why the correct answer works:** ACM provisions and manages certificates for integrated AWS services such as an ALB.
- **A:** KMS manages cryptographic keys, not the requested certificate lifecycle.
- **B:** This is correct.
- **C:** CloudHSM is dedicated HSM infrastructure.
- **D:** Inspector finds vulnerabilities.
- **Reusable rule:** Managed TLS certificates on integrated services point to ACM.
- **Cost/operation:** Public managed certificates used with integrated services differ from paid private CA resources.
- **Variation:** A private certificate hierarchy can require AWS Private CA.
- **Lessons:** 303
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)

## B22-03 — Answer C

- **Central requirement:** A standard multi-tenant managed key service does not satisfy the requirement.
- **Decisive words:** single-tenant HSM, direct control
- **Why the correct answer works:** CloudHSM provides customer-controlled, single-tenant HSMs.
- **A:** Shield is DDoS protection.
- **B:** Macie discovers sensitive S3 data.
- **C:** This is correct.
- **D:** EventBridge routes events.
- **Reusable rule:** Dedicated HSM requirements point to CloudHSM; integrated managed keys usually point to KMS.
- **Cost/operation:** CloudHSM clusters have continuous hourly costs and operational responsibilities.
- **Variation:** Use KMS unless the dedicated HSM requirement is explicit.
- **Lessons:** 304
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)

## B22-04 — Answer B,D

- **Central requirement:** inspect malicious HTTP requests and enforce the same WAF policy across organization accounts.
- **Decisive words:** *SQL injection*, *ALBs*, *many accounts*, *centrally enforced*.
- **A:** incorrect; security groups filter connections and do not parse SQL syntax or provide deny rules.
- **B:** correct; AWS WAF web ACLs inspect and block Layer 7 request patterns at supported resources.
- **C:** incorrect; Shield Standard provides baseline DDoS protection but is not the SQL-injection rule engine.
- **D:** correct; Firewall Manager centrally deploys and governs WAF policies across in-scope organization resources.
- **E:** incorrect; route tables select network paths and cannot inspect HTTP bodies.
- **Reusable rule:** WAF defines application rules; Firewall Manager scales consistent policy administration across accounts.
- **Lessons:** 305–309.
- **Official reference:** [AWS Firewall Manager WAF policies](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policies.html).

## B22-05 — Answer A

- **Central requirement:** Administration and compliance must be centralized.
- **Decisive words:** many accounts, consistent WAF policies, centralized
- **Why the correct answer works:** Firewall Manager centrally configures and audits supported security policies across accounts and resources.
- **A:** This is correct.
- **B:** Inspector assesses vulnerabilities.
- **C:** ACM manages certificates.
- **D:** Flow Logs records network metadata.
- **Reusable rule:** Organization-wide security policy administration points to Firewall Manager.
- **Cost/operation:** Firewall Manager and the managed security services it configures can incur charges.
- **Variation:** Control Tower governs landing zones but is not the WAF policy manager.
- **Lessons:** 305–309
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)

## B22-06 — Answer B

- **Central requirement:** deploy managed organization-wide threat detection and aggregate its findings without conflating the two roles.
- **Decisive words:** account/DNS/VPC signals, new organization accounts, common findings view
- **Why the correct answer works:** GuardDuty is the detector for the described signals; organization administration scales enablement, and Security Hub CSPM aggregates findings from GuardDuty and other integrations.
- **A:** Macie organization administration is useful for sensitive-data discovery, but Macie does not replace the stated account/DNS/VPC threat detector.
- **B:** correct; it combines purpose-built detection with a separate centralized findings and posture view.
- **C:** Security Hub CSPM aggregates and evaluates findings/posture, but it cannot aggregate GuardDuty network threats that were never detected.
- **D:** Detective accelerates investigation of findings and related entities; it is not the primary detector/organization-enablement layer described.
- **Reusable rule:** GuardDuty detects threats; Security Hub CSPM aggregates/prioritizes findings; Detective supports investigation. Keep roles distinct.
- **Cost/operation:** GuardDuty charges based on analyzed data sources and optional protections.
- **Variation:** Add Detective when investigators need entity relationships and historical activity after a finding.
- **Lessons:** 310
- **Official reference:** [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) and [Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)

## B22-07 — Answer A,E

- **Central requirement:** investigate a threat finding in context and separately identify software vulnerabilities.
- **Decisive words:** *GuardDuty finding*, *relationships and historical activity*, *software vulnerabilities*.
- **A:** correct; Detective analyzes linked entities and activity to support finding investigation.
- **B:** incorrect; Macie discovers sensitive data in S3 and does not patch compute packages.
- **C:** incorrect; Artifact provides compliance documents rather than an investigation graph.
- **D:** incorrect; WAF filters web requests and does not inventory CVEs.
- **E:** correct; Inspector assesses supported workloads for software vulnerabilities and exposure.
- **Reusable rule:** GuardDuty detects suspicious activity, Detective supports investigation, and Inspector manages vulnerability findings.
- **Lessons:** 310–312.
- **Official reference:** [Amazon Detective](https://docs.aws.amazon.com/detective/latest/userguide/what-is-detective.html) and [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html).

## B22-08 — Answer D

- **Central requirement:** test ENI capacity against actual usable addresses and preserve scaling/replacement headroom.
- **Decisive words:** slash 28, 12 ENIs, AWS-reserved, exhaustion
- **Why the correct answer works:** A /28 contains 16 total IPv4 addresses and AWS reserves five, leaving only 11 assignable addresses before considering headroom.
- **A:** sixteen is the total CIDR size, not the usable ENI capacity.
- **B:** subtracting only network and broadcast conventions ignores AWS's five reserved addresses per IPv4 subnet.
- **C:** thirteen uses the wrong reservation count and would still provide inadequate operational headroom.
- **D:** correct; the requirement already exceeds usable capacity, so the architecture needs a larger valid subnet or redistributed ENIs rather than optimistic overcommit.
- **Reusable rule:** subnet sizing must include AWS reservations, all ENI consumers, scale/replacement overlap, and future endpoints or load-balancer needs.
- **Cost/operation:** Small subnets can exhaust addresses and force disruptive redesign.
- **Variation:** Existing subnet CIDRs cannot be resized in place; plan nonoverlapping address space before deployment.
- **Lessons:** 313–319
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html)

## B22-09 — Answer A,C,F

- **Central requirement:** combine Layer 7 exploit filtering, enhanced DDoS response, and least-privilege tier isolation.
- **Decisive words:** *SQL injection*, *sophisticated DDoS*, *only from ALB*.
- **A:** correct; WAF inspects supported HTTP requests and blocks SQL-injection patterns.
- **B:** incorrect; unrestricted public instance access bypasses the load-balancer security boundary.
- **C:** correct; Shield Advanced adds enhanced detection, response support, and eligible cost protection features.
- **D:** incorrect; a NAT Gateway is for egress translation, not inbound HTTP load balancing or inspection.
- **E:** incorrect; a NACL is stateless and cannot be the only application-layer control.
- **F:** correct; security-group referencing restricts the application tier to traffic from the ALB tier.
- **Reusable rule:** layered public application defense combines edge/application controls with explicit trust between network tiers.
- **Lessons:** 305–323.
- **Official reference:** [AWS WAF, Shield Advanced, and Shield network security](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html).

## B22-10 — Answer B

- **Central requirement:** enforce application-tier least privilege and a CIDR deny at the correct layers with correct return-path behavior.
- **Decisive words:** ALB security group source, interface, ordered deny, ephemeral return ports
- **Why the correct answer works:** security groups are stateful allow controls associated with ENIs and can reference another SG; NACLs are ordered stateless subnet controls with allow and deny entries.
- **A:** public ALB node addresses can change and the option loses SG-to-SG least privilege; a one-direction NACL rule also ignores stateless return traffic.
- **B:** correct; it uses identity-like SG referencing for the application path and handles both directions explicitly at the NACL layer.
- **C:** Network Firewall can add centralized filtering, but permitting the whole VPC CIDR fails the explicit ALB-only application-tier requirement and adds a service beyond the requested control mapping.
- **D:** the SG half is correct, but the NACL half breaks return flows because stateless subnet rules must cover the response path and ephemeral ports.
- **Reusable rule:** SG = stateful ENI allow policy; NACL = ordered stateless subnet allow/deny guardrail, including return traffic.
- **Cost/operation:** Controls themselves do not replace the cost of traffic-processing services.
- **Variation:** NACL return traffic needs explicit ephemeral-port handling.
- **Lessons:** 329–330 plus fundamentals 313–326
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)
