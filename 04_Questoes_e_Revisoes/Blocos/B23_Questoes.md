# B23 — Questões: Redes avançadas, endpoints, conectividade híbrida e IPv6

**Quantidade:** 10 questões autorais<br>
**Idioma:** 10 em inglês<br>
**Regra:** selecione a quantidade indicada em cada questão<br>
**Tempo sugerido:** 18 minutos<br>
**Gabarito:** [arquivo separado](B23_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B23-01 | 3.4 | VPC peering | single | fundamental | básica | Inglês |
| B23-02 | 3.4 | Gateway endpoint | single | situacional | intermediária | Inglês |
| B23-03 | 3.4 | Interface endpoint | single | situacional | intermediária | Inglês |
| B23-04 | 3.4 | Client VPN and Flow Logs | multi-2 | integrada | avançada | Inglês |
| B23-05 | 3.4 | Traffic Mirroring | single | situacional | intermediária | Inglês |
| B23-06 | 3.4 | Site-to-Site VPN | single | situacional | intermediária | Inglês |
| B23-07 | 3.4 | Direct Connect and encryption | multi-2 | integrada | avançada | Inglês |
| B23-08 | 3.4 | Transit Gateway | single | integrada | avançada | Inglês |
| B23-09 | 3.4 | IPv6 private egress | multi-3 | integrada | avançada | Inglês |
| B23-10 | 3.4 | Network troubleshooting | single | integrada | avançada | Inglês |

## Questões

### B23-01

**Context:** VPC A is peered with VPC B, and VPC B is peered with VPC C.

**Requirement:** Resources in A must communicate privately with resources in C by using B as a transit network.

**Question:** Will the existing peerings meet the requirement?

- A. Yes, peering is transitive by default.
- B. Yes, after adding only a security group rule in B.
- C. No, VPC peering does not support transitive routing.
- D. No, because peering supports only public traffic.

### B23-02

**Context:** Private EC2 instances need to access Amazon S3 without using a NAT Gateway or public IP addresses.

**Requirement:** The company wants the endpoint type that integrates with route tables and has no hourly endpoint charge.

**Question:** Which solution should be used?

- A. An S3 gateway endpoint.
- B. An internet gateway attached to each subnet.
- C. A Site-to-Site VPN.
- D. A Traffic Mirroring session.

### B23-03

**Context:** A VPC workload must access a supported AWS service through private IP addresses and private DNS.

**Requirement:** The endpoint must have security groups and be reachable as ENIs in selected subnets.

**Question:** Which endpoint type meets the requirement?

- A. Gateway endpoint.
- B. Egress-only Internet Gateway.
- C. Interface VPC endpoint powered by AWS PrivateLink.
- D. VPC peering.

### B23-04

**Context:** Remote employees need managed, certificate-based access to private VPC resources. Network operations must also record source, destination, ports, bytes, and ACCEPT or REJECT metadata for the endpoint ENIs.

**Requirement:** Provide remote-access connectivity and flow metadata without capturing packet payload. **Choose TWO.**

- A. Use VPC Traffic Mirroring as the employee VPN concentrator.
- B. Deploy AWS Client VPN and authorize the required network access.
- C. Use an Internet Gateway to assign employee devices private VPC addresses.
- D. Enable VPC Flow Logs for the relevant Client VPN endpoint network interfaces.
- E. Use AWS WAF logs as the VPN connection mechanism.

### B23-05

**Context:** A security appliance must inspect copies of packets from selected EC2 network interfaces.

**Requirement:** The solution needs packet content rather than only flow metadata.

**Question:** Which VPC feature should be used?

- A. VPC Traffic Mirroring.
- B. VPC Flow Logs.
- C. A gateway endpoint.
- D. An egress-only Internet Gateway.

### B23-06

**Context:** A new branch must reach private VPC workloads within hours. It has
a compatible customer gateway and needs redundant encrypted tunnels over its
existing internet connection. A dedicated circuit may be added later for more
predictable throughput, but it cannot block today's cutover.

**Requirement:** Choose the fastest managed hybrid-connectivity first step
without treating it as a dedicated private transport.

**Question:** Which design is appropriate?

- A. Order Direct Connect with MACsec-capable connectivity as the only first step and delay cutover until provisioning completes.
- B. Configure AWS Site-to-Site VPN with both managed IPsec tunnels now; evaluate Direct Connect later and add VPN over the desired transport if encryption remains required.
- C. Deploy AWS Client VPN and install individual user clients on branch servers, treating remote-user access as routed site-to-site connectivity.
- D. Attach the VPC to Transit Gateway but create no VPN or Direct Connect attachment from the branch, assuming the hub itself supplies the transport.

### B23-07

**Context:** A datacenter requires a dedicated path with consistent performance and IPsec encryption in transit to AWS. Public-internet VPN alone does not meet the transport requirement.

**Requirement:** Combine the dedicated connectivity and encryption mechanisms. **Choose TWO.**

- A. Provision AWS Direct Connect for the dedicated network path.
- B. Use Direct Connect alone and assume all virtual interfaces are IPsec encrypted by default.
- C. Use a NAT Gateway as the customer gateway device.
- D. Establish an AWS Site-to-Site VPN over an appropriate Direct Connect public virtual interface design.
- E. Replace both controls with VPC peering to the on-premises router.

### B23-08

**Context:** Dozens of VPCs and several Site-to-Site VPN attachments in one
Region need transitive connectivity. Production and development must use
different routing domains, while selected traffic is steered through inspection
appliances without building a peering mesh.

**Requirement:** Provide a scalable regional hub with attachment-level route
propagation and segmentation.

**Question:** Which design best fits?

- A. Use an AWS Cloud WAN core network for this single-Region estate, accepting broader global-policy scope and cost than the stated regional hub requires.
- B. Use AWS Transit Gateway with separate route tables/associations and explicit propagation or static inspection routes for the required segments.
- C. Build full-mesh VPC peering and maintain explicit routes between every pair, including the assumption that a peered VPC can transit VPN traffic.
- D. Use one Transit Gateway route table for every attachment and propagate all routes, omitting the required production/development and inspection segmentation.

### B23-09

**Context:** Dual-stack workloads in private subnets must initiate IPv6 internet connections without accepting new inbound internet connections. Their high-volume S3 traffic should avoid NAT processing, and operations needs connection metadata.

**Requirement:** Select the IPv6 egress, private S3 path, and observability controls. **Select THREE.**

- A. Route `::/0` to an egress-only Internet Gateway.
- B. Route inbound IPv6 traffic through a public NAT Gateway.
- C. Add an S3 gateway endpoint with the appropriate route tables and endpoint policy.
- D. Use VPC peering as the route to every internet destination.
- E. Enable VPC Flow Logs on the relevant network interfaces, subnets, or VPC.
- F. Assign public IPv4 addresses solely to make IPv6 egress private.

### B23-10

**Context:** DNS resolves correctly, but a private client cannot connect to a service through a routed network path.

**Requirement:** The architect must find the first blocking point without assuming that a security group is the only cause.

**Question:** Which approach is best?

- A. Open all inbound ports permanently.
- B. Replace every route with 0.0.0.0/0.
- C. Trace DNS, forward route, target, return route, NACLs, security groups, and the listening service in order.
- D. Create an additional VPC with overlapping CIDR.

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
