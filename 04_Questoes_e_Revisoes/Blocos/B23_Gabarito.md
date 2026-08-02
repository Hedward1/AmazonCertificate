# B23 — Gabarito comentado

Volte às [questões B23](B23_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B23-01 | C | 3.4 |
| B23-02 | A | 3.4 |
| B23-03 | C | 3.4 |
| B23-04 | B,D | 3.4 |
| B23-05 | A | 3.4 |
| B23-06 | B | 3.4 |
| B23-07 | A,D | 3.4 |
| B23-08 | B | 3.4 |
| B23-09 | A,C,E | 3.4 |
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

## B23-04 — Answer B,D

- **Central requirement:** provide managed remote-user connectivity and record network flow metadata without payload capture.
- **Decisive words:** *remote employees*, *certificate-based*, *private resources*, *ACCEPT or REJECT*, *no payload*.
- **A:** incorrect; Traffic Mirroring copies packets for appliances and is not a remote-access VPN concentrator.
- **B:** correct; Client VPN provides managed client connectivity with authentication and authorization controls.
- **C:** incorrect; an Internet Gateway does not enroll remote devices into the VPC address space.
- **D:** correct; Flow Logs capture the requested connection metadata for the relevant ENIs.
- **E:** incorrect; WAF logs neither establish a VPN tunnel nor provide general VPC flow metadata.
- **Reusable rule:** Client VPN solves user-to-VPC access; Flow Logs observe connection metadata; Traffic Mirroring is for packet content.
- **Lessons:** 335–340.
- **Official reference:** [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html) and [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html).

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

- **Central requirement:** establish redundant encrypted hybrid connectivity immediately while keeping a later dedicated-transport option separate.
- **Decisive words:** within hours, existing internet, two IPsec tunnels, dedicated circuit later
- **Why the correct answer works:** Site-to-Site VPN can be configured quickly over the internet and supplies two managed tunnel endpoints; Direct Connect is a distinct provisioning and transport decision.
- **A:** Direct Connect/MACsec can be appropriate on supported connections, but provisioning cannot satisfy the within-hours first step and MACsec is not a universal substitute for the stated IPsec design.
- **B:** correct; it meets the immediate encrypted requirement and leaves a staged path to dedicated transport or VPN over Direct Connect.
- **C:** Client VPN is designed for individual remote clients, not a branch-router site-to-site network attachment with redundant managed tunnels.
- **D:** Transit Gateway can be the hub, but an explicit VPN or Direct Connect attachment is still required to carry branch traffic to it.
- **Reusable rule:** use Site-to-Site VPN for rapid encrypted hybrid access; add Direct Connect for dedicated capacity/consistency and retain explicit encryption when required.
- **Cost/operation:** VPN connection-hours and data transfer can incur charges.
- **Variation:** Dynamic routing with BGP and customer-device redundancy can improve convergence beyond merely creating both AWS tunnels.
- **Lessons:** 337–338
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

## B23-07 — Answer A,D

- **Central requirement:** combine a dedicated network path with IPsec encryption to AWS.
- **Decisive words:** *dedicated*, *consistent performance*, *IPsec*, *not public-internet VPN alone*.
- **A:** correct; Direct Connect supplies the dedicated transport path.
- **B:** incorrect; Direct Connect virtual interfaces are not all IPsec encrypted by default.
- **C:** incorrect; a NAT Gateway cannot act as an on-premises customer gateway.
- **D:** correct; Site-to-Site VPN over an appropriate Direct Connect public-VIF design adds IPsec to the dedicated path.
- **E:** incorrect; VPC peering does not connect an on-premises router or create IPsec.
- **Reusable rule:** dedicated plus IPsec often requires Direct Connect plus Site-to-Site VPN; neither service alone satisfies both clauses.
- **Lessons:** 339–340.
- **Official reference:** [AWS Direct Connect plus VPN](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-plus-vpn.html).

## B23-08 — Answer B

- **Central requirement:** centralize transitive regional routing while isolating environments and steering only intended paths through inspection.
- **Decisive words:** dozens of VPCs, VPN attachments, routing domains, inspection, no mesh
- **Why the correct answer works:** Transit Gateway is a regional transit hub whose attachments can associate with and propagate into controlled route tables.
- **A:** Cloud WAN could be justified for centrally governed multi-Region/global networks, but it is broader than necessary for the explicitly regional requirement.
- **B:** correct; multiple TGW route tables and deliberate association/propagation implement segmentation, with explicit routes for inspection paths.
- **C:** peering is non-transitive; a mesh scales operationally poorly and cannot use a peer as a general VPN transit path.
- **D:** Transit Gateway is the right service family, but one fully propagated route table defeats the required segmentation and inspection steering.
- **Reusable rule:** Transit Gateway handles regional many-to-many network transit; route-table design determines reachability and segmentation, not attachment alone.
- **Cost/operation:** Attachments and data processing are billed.
- **Variation:** For multi-Region or global network policy, evaluate inter-Region TGW peering or Cloud WAN separately from this regional requirement.
- **Lessons:** 341
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)

## B23-09 — Answer A,C,E

- **Central requirement:** provide outbound-only IPv6, a private S3 path, and network-flow observability.
- **Decisive words:** *initiate IPv6*, *no new inbound*, *S3 avoid NAT*, *metadata*.
- **A:** correct; an egress-only Internet Gateway permits outbound-initiated IPv6 connections and blocks new inbound initiation.
- **B:** incorrect; a public NAT Gateway is not the IPv6-specific outbound-only target requested.
- **C:** correct; an S3 gateway endpoint routes supported S3 traffic privately through associated route tables.
- **D:** incorrect; peering is private VPC connectivity, not a default internet path.
- **E:** correct; Flow Logs provide accepted/rejected connection metadata at supported scopes.
- **F:** incorrect; public IPv4 addressing does not satisfy or secure IPv6 egress.
- **Reusable rule:** design each path independently: egress-only IGW for IPv6 internet, gateway endpoint for S3, Flow Logs for metadata.
- **Lessons:** 333–345.
- **Official reference:** [Egress-only Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html) and [S3 gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).

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
