# B10 — Questões: Route 53 avançado, arquiteturas e Beanstalk

**Quantidade:** 10 · **Idioma:** 5 português/5 inglês · **Tempo:** 15 min<br>
**Gabarito:** [arquivo separado](B10_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B10-01 | 2.2 | Failover routing | Situacional | Básica | Português |
| B10-02 | 3.4 | Geolocation | Situacional | Intermediária | Português |
| B10-03 | 3.4 | Multivalue | Fundamental | Intermediária | Português |
| B10-04 | 3.4 | Resolver inbound | Situacional | Intermediária | Português |
| B10-05 | 2.1 | Stateless architecture | Situacional | Intermediária | Português |
| B10-06 | 3.4 | Geoproximity | Situacional | Intermediária | Inglês |
| B10-07 | 3.4 | External registrar | Situacional | Básica | Inglês |
| B10-08 | 3.4 | Resolver outbound | Situacional | Intermediária | Inglês |
| B10-09 | 2.1 | Beanstalk worker | Fundamental | Intermediária | Inglês |
| B10-10 | 4.2 | Beanstalk cost | Situacional | Básica | Inglês |

## Questões

### B10-01

Uma aplicação possui ALB principal e site de manutenção secundário. Novas
consultas DNS devem usar o secundário quando o principal estiver unhealthy.

- A. Simple routing com dois valores sem health check.
- B. Failover records primary/secondary com avaliação de saúde e TTL adequado.
- C. Weighted 50/50 permanente.
- D. Geolocation sem default.

### B10-02

Por licença, usuários de um país devem receber catálogo específico mesmo que
outra Region tenha menor latência.

- A. Latency routing.
- B. Multivalue.
- C. Geolocation routing com record/default apropriado.
- D. Simple com CNAME aleatório.

### B10-03

Uma empresa quer retornar até oito IPs saudáveis via DNS. Ela aceita caching e
que isso não seja um proxy de conexões.

- A. Multivalue answer routing com health checks.
- B. ALB path routing.
- C. Geoproximity obrigatório.
- D. MX records.

### B10-04

Servidores DNS on-premises precisam resolver nomes de uma private hosted zone
associada à VPC.

- A. Outbound endpoint apenas.
- B. Publicar a private zone na internet.
- C. CNAME no zone apex.
- D. Resolver inbound endpoint e conditional forwarding on-premises.

### B10-05

Um web tier em ASG perde sessões quando instâncias são substituídas. Qual mudança
melhora elasticidade?

- A. Armazenar mais estado em instance store.
- B. Externalizar sessão para store compartilhado adequado e tornar instâncias
  substituíveis.
- C. Desabilitar health checks.
- D. Fixar desired=1.

### B10-06

A company wants to shift more traffic toward one resource location by changing
a relative bias, without defining users by country.

- A. Simple routing.
- B. IP-based routing only.
- C. Geoproximity routing with a carefully tested bias.
- D. MX routing.

### B10-07

A domain is registered with a third-party registrar. The company created a Route
53 public hosted zone, but internet queries still use the old DNS provider.

- A. Update the domain delegation at the registrar to the Route 53 hosted
  zone's name servers.
- B. Create an EBS snapshot.
- C. Add a private IP to the SOA record.
- D. Create an outbound Resolver endpoint only.

### B10-08

Workloads in a VPC must resolve `corp.local` by sending queries to DNS servers
on premises over Direct Connect.

- A. An inbound endpoint only.
- B. A public ALB listener.
- C. A multivalue record in a public zone.
- D. An outbound Resolver endpoint, forwarding rule and network path to the
  on-premises DNS servers.

### B10-09

Which Elastic Beanstalk environment tier is designed to process background work
from an Amazon SQS queue?

- A. A Route 53 health-check environment.
- B. Worker environment tier.
- C. A single DNS record.
- D. An EBS Multi-Attach tier.

### B10-10

A team assumes that a load-balanced Elastic Beanstalk environment is free
because there is no additional Beanstalk service charge. What is correct?

- A. Beanstalk environments never create AWS resources.
- B. Only application source code can incur cost.
- C. Underlying EC2, ELB, ASG-related capacity, EBS, logs and data can incur
  charges and require cleanup.
- D. Setting the environment CNAME to empty stops all charges.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B10-01 | | | |
| B10-02 | | | |
| B10-03 | | | |
| B10-04 | | | |
| B10-05 | | | |
| B10-06 | | | |
| B10-07 | | | |
| B10-08 | | | |
| B10-09 | | | |
| B10-10 | | | |
