# B22 — Gabarito comentado

Volte às [questões B22](B22_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B22-01 | A | 1.2 |
| B22-02 | B | 1.3 |
| B22-03 | C | 1.3 |
| B22-04 | D | 1.2 |
| B22-05 | A | 1.2 |
| B22-06 | B | 1.2 |
| B22-07 | C | 1.2 |
| B22-08 | D | 3.4 |
| B22-09 | A | 3.4 |
| B22-10 | B | 3.4 |

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

## B22-04 — Answer D

- **Central requirement:** The solution must inspect HTTP requests and block matching patterns.
- **Decisive words:** SQL injection, HTTP requests, patterns
- **Why the correct answer works:** AWS WAF provides Layer 7 rules that can detect and block web request patterns such as SQL injection.
- **A:** Security groups have no deny and do not inspect SQL injection.
- **B:** A NACL filters network fields, not HTTP content.
- **C:** Shield mitigates DDoS but is not the requested rule engine.
- **D:** This is correct.
- **Reusable rule:** HTTP application-layer filtering points to WAF.
- **Cost/operation:** Web ACLs, rules, managed rule groups, and requests can incur charges.
- **Variation:** Use count mode to validate new rules before blocking.
- **Lessons:** 305–309
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)

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

- **Central requirement:** It does not want to build its own detection pipeline.
- **Decisive words:** threat detection, DNS, VPC, account activity
- **Why the correct answer works:** GuardDuty analyzes supported threat intelligence and account and network data sources to generate findings.
- **A:** Macie focuses on sensitive data in S3.
- **B:** This is correct.
- **C:** Textract reads documents.
- **D:** Batch runs jobs.
- **Reusable rule:** Managed threat detection from account and network signals points to GuardDuty.
- **Cost/operation:** GuardDuty charges based on analyzed data sources and optional protections.
- **Variation:** Security Hub CSPM can aggregate findings but is not the detector described.
- **Lessons:** 310
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

## B22-07 — Answer C

- **Central requirement:** Each requirement should use the specialized managed service.
- **Decisive words:** vulnerabilities, sensitive data, S3
- **Why the correct answer works:** Inspector assesses supported workloads for vulnerabilities, while Macie discovers sensitive data in S3.
- **A:** The services are reversed.
- **B:** GuardDuty has a different threat-detection role.
- **C:** This is correct.
- **D:** Certificates and WAF do not meet the two requirements.
- **Reusable rule:** Inspector maps to workload vulnerabilities; Macie maps to sensitive S3 data.
- **Cost/operation:** Both services can charge according to resources or data analyzed.
- **Variation:** GuardDuty findings can complement these services.
- **Lessons:** 310–312
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)

## B22-08 — Answer D

- **Central requirement:** The designer must account for addresses reserved by AWS.
- **Decisive words:** slash 28, reserved by AWS, available
- **Why the correct answer works:** A /28 has 16 total addresses, and AWS reserves five in each IPv4 subnet, leaving 11 usable.
- **A:** Sixteen is the total.
- **B:** Fourteen assumes two reserved addresses.
- **C:** Thirteen assumes three reserved addresses.
- **D:** This is correct.
- **Reusable rule:** Usable IPv4 addresses in a VPC subnet equal total addresses minus five.
- **Cost/operation:** Small subnets can exhaust addresses and force disruptive redesign.
- **Variation:** Plan capacity for load balancers, endpoints, and scaling.
- **Lessons:** 313–319
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html)

## B22-09 — Answer A

- **Central requirement:** The instance must receive inbound IPv4 traffic from the internet.
- **Decisive words:** inbound IPv4, internet, additional condition
- **Why the correct answer works:** The route makes the subnet public, but the instance still needs public addressing and security and application configuration.
- **A:** This is correct.
- **B:** Private addressing alone is not internet-routable.
- **C:** NAT provides outbound translation, not inbound to the instance.
- **D:** A DynamoDB endpoint is unrelated.
- **Reusable rule:** Public subnet does not automatically make a resource publicly reachable.
- **Cost/operation:** Public IPv4 addresses incur charges and increase exposure.
- **Variation:** Prefer a public load balancer with private application instances.
- **Lessons:** 315–323
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)

## B22-10 — Answer B

- **Central requirement:** Both controls must be mapped correctly.
- **Decisive words:** stateful interface, ordered subnet deny
- **Why the correct answer works:** Security groups are stateful allow controls on interfaces; NACLs are stateless subnet controls with ordered allow and deny rules.
- **A:** The states are reversed.
- **B:** This is correct.
- **C:** Security groups do not have deny rules.
- **D:** The association levels differ.
- **Reusable rule:** SG is stateful allow; NACL is stateless ordered allow and deny.
- **Cost/operation:** Controls themselves do not replace the cost of traffic-processing services.
- **Variation:** NACL return traffic needs explicit ephemeral-port handling.
- **Lessons:** 329–330 plus fundamentals 313–326
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)
