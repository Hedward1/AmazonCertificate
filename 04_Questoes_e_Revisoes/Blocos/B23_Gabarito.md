# B23 — Gabarito comentado

Volte às [questões B23](B23_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B23-01 | C | 3.4 |
| B23-02 | A | 3.4 |
| B23-03 | C | 3.4 |
| B23-04 | D | 3.4 |
| B23-05 | A | 3.4 |
| B23-06 | B | 3.4 |
| B23-07 | C | 3.4 |
| B23-08 | B | 3.4 |
| B23-09 | B | 3.4 |
| B23-10 | C | 3.4 |

## B23-01 — Answer C

- **Central requirement:** Resources in A must communicate privately with resources in C by using B as a transit network.
- **Decisive words:** A to B, B to C, transit
- **Why the correct answer works:** VPC peering is a one-to-one non-transitive relationship; A cannot use B to reach C.
- **A:** Peering is not transitive.
- **B:** A security group cannot add transit routing.
- **C:** This is correct.
- **D:** Peering uses private IP connectivity.
- **Reusable rule:** Peering is not transitive; use a transit architecture such as Transit Gateway when required.
- **Cost/operation:** A mesh of peerings increases route and operational complexity.
- **Variation:** CIDR overlap also prevents supported peering connectivity.
- **Lessons:** 331–332
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations-partial-access.html)

## B23-02 — Answer A

- **Central requirement:** The company wants the endpoint type that integrates with route tables and has no hourly endpoint charge.
- **Decisive words:** S3, route tables, no NAT, no hourly endpoint
- **Why the correct answer works:** An S3 gateway endpoint is added to route tables and provides private S3 access without hourly endpoint charges.
- **A:** This is correct.
- **B:** An IGW does not satisfy private access.
- **C:** A VPN is for hybrid connectivity.
- **D:** Traffic Mirroring copies packets.
- **Reusable rule:** S3 or DynamoDB plus route table points to a gateway endpoint.
- **Cost/operation:** Data and the destination service still follow their pricing.
- **Variation:** Endpoint and bucket policies both participate in authorization.
- **Lessons:** 333–334
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html)

## B23-03 — Answer C

- **Central requirement:** The endpoint must have security groups and be reachable as ENIs in selected subnets.
- **Decisive words:** private IP, private DNS, ENIs, security groups
- **Why the correct answer works:** Interface endpoints create ENIs with private IPs, support security groups, and can provide private DNS.
- **A:** Gateway endpoints use route tables for S3 and DynamoDB.
- **B:** Egress-only IGW is IPv6 internet egress.
- **C:** This is correct.
- **D:** Peering connects VPCs.
- **Reusable rule:** PrivateLink service access through ENIs points to an interface endpoint.
- **Cost/operation:** Interface endpoints charge per endpoint-hour and data processed.
- **Variation:** Deploy endpoints in the AZs needed for resilience and cost-aware routing.
- **Lessons:** 333–334
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html)

## B23-04 — Answer D

- **Central requirement:** Packet payload is not required.
- **Decisive words:** metadata, ACCEPT REJECT, no payload
- **Why the correct answer works:** Flow Logs capture network flow metadata at VPC, subnet, or ENI scope without packet payload.
- **A:** Mirroring copies packets and is more than required.
- **B:** WAF logs are application web-layer data.
- **C:** Inspector assesses vulnerabilities.
- **D:** This is correct.
- **Reusable rule:** Flow metadata points to Flow Logs; packet content points to Traffic Mirroring.
- **Cost/operation:** Log delivery, storage, and analysis can incur charges.
- **Variation:** A REJECT entry narrows the investigation but does not identify every possible blocking layer.
- **Lessons:** 335–336
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

## B23-05 — Answer A

- **Central requirement:** The solution needs packet content rather than only flow metadata.
- **Decisive words:** copies of packets, packet content, appliance
- **Why the correct answer works:** Traffic Mirroring copies traffic from supported ENIs to a monitoring target for deep inspection.
- **A:** This is correct.
- **B:** Flow Logs provide metadata only.
- **C:** Gateway endpoints provide service access.
- **D:** Egress-only IGW controls IPv6 egress.
- **Reusable rule:** Packet inspection points to Traffic Mirroring.
- **Cost/operation:** Mirrored traffic and analysis targets create processing and compute costs.
- **Variation:** Use filters to limit mirrored traffic.
- **Lessons:** 342
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html)

## B23-06 — Answer B

- **Central requirement:** The service should provide managed IPsec tunnels.
- **Decisive words:** encrypted, public internet, within hours, IPsec
- **Why the correct answer works:** Site-to-Site VPN provides managed IPsec tunnels over the internet and can be provisioned faster than a dedicated circuit.
- **A:** Direct Connect is dedicated and slower to provision; it is not IPsec by itself.
- **B:** This is correct.
- **C:** Peering connects VPCs.
- **D:** CloudFront is a CDN.
- **Reusable rule:** Fast hybrid IPsec over the internet points to Site-to-Site VPN.
- **Cost/operation:** VPN connection-hours and data transfer can incur charges.
- **Variation:** Configure both tunnels for availability.
- **Lessons:** 337–338
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

## B23-07 — Answer C

- **Central requirement:** Both dedication and encryption must be satisfied.
- **Decisive words:** dedicated, consistent, IPsec
- **Why the correct answer works:** Direct Connect supplies the dedicated path, while VPN adds IPsec when the design supports the combination.
- **A:** Direct Connect alone is not IPsec automatically.
- **B:** VPN alone does not satisfy dedicated path.
- **C:** This is correct.
- **D:** NAT is unrelated.
- **Reusable rule:** Dedicated plus encrypted often maps to Direct Connect plus VPN.
- **Cost/operation:** Ports, transfer, VPN, and provider circuits all contribute to cost.
- **Variation:** VPN over the internet can remain a backup path.
- **Lessons:** 339–340
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-plus-vpn.html)

## B23-08 — Answer B

- **Central requirement:** The company wants a regional hub-and-spoke design.
- **Decisive words:** dozens, transitive, regional hub, segmentation
- **Why the correct answer works:** Transit Gateway is a regional transit hub for VPC and hybrid attachments with route-table segmentation.
- **A:** Peering is non-transitive and a mesh is complex.
- **B:** This is correct.
- **C:** IGWs cannot be shared as the requested transit hub.
- **D:** Resolver handles DNS, not packet transit.
- **Reusable rule:** Many networks plus transitive hub points to Transit Gateway.
- **Cost/operation:** Attachments and data processing are billed.
- **Variation:** Multiple TGW route tables can isolate environments.
- **Lessons:** 341
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)

## B23-09 — Answer B

- **Central requirement:** The solution must be managed and IPv6-specific.
- **Decisive words:** IPv6, initiate outbound, no inbound initiation
- **Why the correct answer works:** An egress-only Internet Gateway supports outbound-initiated IPv6 internet traffic and blocks new inbound-initiated connections.
- **A:** NAT Gateway is the classic IPv4 clue.
- **B:** This is correct.
- **C:** A gateway endpoint is service-specific.
- **D:** Peering is not internet egress.
- **Reusable rule:** Private IPv6 egress points to an egress-only Internet Gateway.
- **Cost/operation:** The gateway choice does not remove normal data transfer charges.
- **Variation:** An Internet Gateway provides bidirectional routing when security controls allow.
- **Lessons:** 343–345
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html)

## B23-10 — Answer C

- **Central requirement:** The architect must find the first blocking point without assuming that a security group is the only cause.
- **Decisive words:** first blocking point, routed path, not only SG
- **Why the correct answer works:** End-to-end tracing checks every required routing and filtering layer in both directions.
- **A:** Broad access is unsafe and does not diagnose routing.
- **B:** A default route can be incorrect and insecure.
- **C:** This is correct.
- **D:** Overlapping CIDR worsens connectivity.
- **Reusable rule:** Connectivity requires DNS, routes both ways, network controls, and a listening service.
- **Cost/operation:** Use Flow Logs carefully because delivery and analysis can incur charges.
- **Variation:** Traffic Mirroring is reserved for packet-level evidence.
- **Lessons:** 327–345
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
