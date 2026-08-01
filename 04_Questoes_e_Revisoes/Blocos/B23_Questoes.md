# B23 — Questões: Redes avançadas, endpoints, conectividade híbrida e IPv6

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione uma resposta<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B23_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B23-01 | 3.4 | VPC peering | Situacional | Intermediate | Inglês |
| B23-02 | 3.4 | Gateway endpoint | Situacional | Basic | Inglês |
| B23-03 | 3.4 | Interface endpoint | Situacional | Intermediate | Inglês |
| B23-04 | 3.4 | VPC Flow Logs | Situacional | Basic | Inglês |
| B23-05 | 3.4 | Traffic Mirroring | Situacional | Intermediate | Inglês |
| B23-06 | 3.4 | Site-to-Site VPN | Situacional | Basic | Inglês |
| B23-07 | 3.4 | Direct Connect and encryption | Situacional | Intermediate | Inglês |
| B23-08 | 3.4 | Transit Gateway | Situacional | Intermediate | Inglês |
| B23-09 | 3.4 | Egress-only Internet Gateway | Situacional | Basic | Inglês |
| B23-10 | 3.4 | Network troubleshooting | Situacional | Advanced | Inglês |

## Questões

### B23-01

**Context:** VPC A is peered with VPC B, and VPC B is peered with VPC C.

**Requirement:** Resources in A must communicate privately with resources in C by using B as a transit network.

**Question:** Will the existing peerings meet the requirement?

- A. Yes, peering is transitive by default.
- B. Yes, after adding only a security group rule in B.
- C. No, VPC peering does not support transitive routing.
- D. No, because peering supports only public traffic.

**Before moving on:** record decisive words and confidence.

### B23-02

**Context:** Private EC2 instances need to access Amazon S3 without using a NAT Gateway or public IP addresses.

**Requirement:** The company wants the endpoint type that integrates with route tables and has no hourly endpoint charge.

**Question:** Which solution should be used?

- A. An S3 gateway endpoint.
- B. An internet gateway attached to each subnet.
- C. A Site-to-Site VPN.
- D. A Traffic Mirroring session.

**Before moving on:** record decisive words and confidence.

### B23-03

**Context:** A VPC workload must access a supported AWS service through private IP addresses and private DNS.

**Requirement:** The endpoint must have security groups and be reachable as ENIs in selected subnets.

**Question:** Which endpoint type meets the requirement?

- A. Gateway endpoint.
- B. Egress-only Internet Gateway.
- C. Interface VPC endpoint powered by AWS PrivateLink.
- D. VPC peering.

**Before moving on:** record decisive words and confidence.

### B23-04

**Context:** A network team needs source address, destination address, ports, bytes, and ACCEPT or REJECT metadata for an ENI.

**Requirement:** Packet payload is not required.

**Question:** Which feature should be enabled after reviewing cost?

- A. VPC Traffic Mirroring.
- B. AWS WAF logging only.
- C. Amazon Inspector.
- D. VPC Flow Logs.

**Before moving on:** record decisive words and confidence.

### B23-05

**Context:** A security appliance must inspect copies of packets from selected EC2 network interfaces.

**Requirement:** The solution needs packet content rather than only flow metadata.

**Question:** Which VPC feature should be used?

- A. VPC Traffic Mirroring.
- B. VPC Flow Logs.
- C. A gateway endpoint.
- D. An egress-only Internet Gateway.

**Before moving on:** record decisive words and confidence.

### B23-06

**Context:** A branch office needs encrypted connectivity to a VPC within hours by using the public internet.

**Requirement:** The service should provide managed IPsec tunnels.

**Question:** Which service is appropriate?

- A. AWS Direct Connect only.
- B. AWS Site-to-Site VPN.
- C. VPC peering.
- D. Amazon CloudFront.

**Before moving on:** record decisive words and confidence.

### B23-07

**Context:** A datacenter requires a dedicated network path with more consistent performance and also requires IPsec encryption.

**Requirement:** Both dedication and encryption must be satisfied.

**Question:** Which design is most appropriate?

- A. Direct Connect alone.
- B. Site-to-Site VPN over the public internet only.
- C. Direct Connect combined with a compatible Site-to-Site VPN design.
- D. A NAT Gateway.

**Before moving on:** record decisive words and confidence.

### B23-08

**Context:** Dozens of VPCs and multiple VPN connections need centralized transitive routing with segmentation.

**Requirement:** The company wants a regional hub-and-spoke design.

**Question:** Which service should it use?

- A. A full mesh of VPC peerings.
- B. AWS Transit Gateway.
- C. One Internet Gateway for all VPCs.
- D. Amazon Route 53 Resolver only.

**Before moving on:** record decisive words and confidence.

### B23-09

**Context:** IPv6 workloads in a private subnet must initiate internet connections, but the internet must not initiate new connections to them.

**Requirement:** The solution must be managed and IPv6-specific.

**Question:** Which target should the subnet route use?

- A. A public NAT Gateway.
- B. An egress-only Internet Gateway.
- C. A gateway endpoint for all internet sites.
- D. A VPC peering connection.

**Before moving on:** record decisive words and confidence.

### B23-10

**Context:** DNS resolves correctly, but a private client cannot connect to a service through a routed network path.

**Requirement:** The architect must find the first blocking point without assuming that a security group is the only cause.

**Question:** Which approach is best?

- A. Open all inbound ports permanently.
- B. Replace every route with 0.0.0.0/0.
- C. Trace DNS, forward route, target, return route, NACLs, security groups, and the listening service in order.
- D. Create an additional VPC with overlapping CIDR.

**Before moving on:** record decisive words and confidence.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B23-01 |  |  |  |
| B23-02 |  |  |  |
| B23-03 |  |  |  |
| B23-04 |  |  |  |
| B23-05 |  |  |  |
| B23-06 |  |  |  |
| B23-07 |  |  |  |
| B23-08 |  |  |  |
| B23-09 |  |  |  |
| B23-10 |  |  |  |
