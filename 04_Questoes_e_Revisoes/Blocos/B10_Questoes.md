# B10 — Questões: Route 53 avançado, arquiteturas e Beanstalk

**Quantidade:** 10 · **Idioma:** 5 português/5 inglês · **Tempo:** 15 min<br>
**Formato:** questões single-answer e multi-answer; siga a instrução de cada questão<br>
**Gabarito:** [arquivo separado](B10_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B10-01 | 2.2 | Failover routing | single | fundamental | básica | Português |
| B10-02 | 3.4 | Geolocation | single | fundamental | básica | Português |
| B10-03 | 3.4 | Multivalue | multi-2 | fundamental | intermediária | Português |
| B10-04 | 3.4 | Resolver inbound | single | situacional | intermediária | Português |
| B10-05 | 2.1 | Stateless architecture | single | situacional | intermediária | Português |
| B10-06 | 3.4 | Geoproximity | single | situacional | intermediária | Inglês |
| B10-07 | 3.4 | External registrar | single | situacional | intermediária | Inglês |
| B10-08 | 3.4 | Resolver outbound | multi-2 | integrada | avançada | Inglês |
| B10-09 | 2.1 | Beanstalk worker | single | situacional | intermediária | Inglês |
| B10-10 | 4.2 | Beanstalk cost | single | integrada | avançada | Inglês |

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

Quais afirmações descrevem a solução adequada?

**Choose TWO.**

- A. Criar multivalue answer records e associar health checks aos records.
- B. O Route 53 pode retornar até oito records saudáveis em resposta a uma
  consulta multivalue.
- C. Usar ALB path routing para fazer o DNS devolver os IPs dos targets.
- D. Habilitar geoproximity, que é obrigatório para filtrar records não
  saudáveis.
- E. Usar MX records para representar os endpoints da aplicação.

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

Which components should a solutions architect configure?

**Choose TWO.**

- A. An outbound Route 53 Resolver endpoint with network and security paths
  that allow DNS traffic to the on-premises servers.
- B. An inbound Resolver endpoint only.
- C. A conditional forwarding rule for `corp.local` that targets the
  on-premises DNS servers and is associated with the VPC.
- D. A multivalue record for `corp.local` in a public hosted zone.
- E. A public ALB listener that recursively forwards DNS queries.

### B10-09

An order application is deployed with AWS Elastic Beanstalk. The public web tier
must return quickly after placing each order in Amazon SQS. A separately scalable
managed environment must poll the queue, invoke the application code for each
message, and expose health information without turning the background processors
into public HTTP endpoints.

Which Elastic Beanstalk design provides the background-processing component?

- A. A Route 53 health-check environment that executes the order code inside
  authoritative DNS servers.
- B. A worker environment tier that consumes messages from Amazon SQS and scales
  its processing instances separately from the web tier.
- C. A single DNS record whose resource values contain the queued order payloads.
- D. An EBS Multi-Attach tier that converts shared block storage into an SQS
  consumer.

### B10-10

A team deploys a load-balanced Elastic Beanstalk environment for a temporary
campaign. The campaign ends, traffic falls to zero, and the team removes the
application CNAME but leaves the environment running. A cost review must account
for provisioned compute, load balancing, storage, logs, and retained data, while
preserving any artifacts that have an explicit retention requirement.

Which statement should guide the review and decommissioning plan?

- A. Set the environment's Auto Scaling desired capacity to zero but retain the
  load balancer, volumes, logs, and environment indefinitely; zero instances
  guarantee that every billing dimension is zero.
- B. Terminate the environment and delete its logs, snapshots, and retained data
  immediately, before identifying ownership or applying retention requirements.
- C. Underlying EC2, load-balancing, Auto Scaling capacity, EBS, logs, and data
  retain their normal service pricing and may require explicit, retention-aware
  cleanup even though Beanstalk has no additional service charge.
- D. Remove the CNAME and archive only the application source bundle while
  leaving the running environment and its supporting resources provisioned.

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
