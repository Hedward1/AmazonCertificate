# B09 — Questões: DNS e Route 53 básico

**Quantidade:** 10 · **Idioma:** 5 português/5 inglês · **Tempo:** 15 min<br>
**Formato:** questões single-answer e multi-answer; siga a instrução de cada questão<br>
**Gabarito:** [arquivo separado](B09_Gabarito.md)

Registre a confiança antes de corrigir. Uma resposta certa por adivinhação deve
entrar no Caderno de Erros como baixa confiança.

Não consulte o console durante a tentativa.

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B09-01 | 3.4 | Alias apex | single | fundamental | básica | Português |
| B09-02 | 3.4 | TTL | single | fundamental | básica | Português |
| B09-03 | 3.4 | Weighted | multi-2 | fundamental | intermediária | Português |
| B09-04 | 3.4 | Latency | single | situacional | intermediária | Português |
| B09-05 | 3.4 | Private hosted zone | single | situacional | intermediária | Português |
| B09-06 | 3.4 | CNAME | single | situacional | intermediária | Inglês |
| B09-07 | 3.4 | DNS roles | single | situacional | intermediária | Inglês |
| B09-08 | 4.4 | TTL change | multi-2 | integrada | avançada | Inglês |
| B09-09 | 3.4 | Simple routing | single | situacional | intermediária | Inglês |
| B09-10 | 3.4 | DNS versus ELB | single | integrada | avançada | Inglês |

## Questões

### B09-01

O zone apex `example.com` deve apontar para um ALB.

- A. Criar CNAME no apex para o DNS do ALB.
- B. Criar Alias A/AAAA do Route 53 para o ALB.
- C. Criar MX com o endereço do ALB.
- D. Criar PTR na private hosted zone.

### B09-02

Uma migração de endpoint ocorrerá amanhã. O record atual tem TTL de 24 horas.

- A. Alterar o endpoint amanhã e reduzir o TTL no mesmo segundo.
- B. Excluir a hosted zone para limpar caches.
- C. Reduzir o TTL com antecedência suficiente para o valor antigo expirar,
  migrar e restaurar um TTL adequado depois.
- D. Trocar A por MX.

### B09-03

Uma implantação blue/green precisa receber aproximadamente 90%/10% das respostas
DNS durante o teste.

Quais configurações atendem ao requisito?

**Choose TWO.**

- A. Criar weighted records com o mesmo nome e tipo, apontando para os endpoints
  blue e green.
- B. Atribuir pesos relativos 90 e 10 aos records; os valores não precisam
  somar 100.
- C. Usar latency routing para produzir uma divisão percentual fixa na mesma
  Region.
- D. Criar um único CNAME sem pesos para os dois ambientes.
- E. Usar simple routing com uma única resposta.

### B09-04

Uma aplicação ativa em duas Regions quer direcionar usuários ao endpoint com
menor latência medida pela rede da AWS.

- A. Weighted 50/50 obrigatoriamente.
- B. Private hosted zone.
- C. Geolocation por país sem medir desempenho.
- D. Latency-based routing com endpoints regionais e saúde apropriada.

### B09-05

Nomes de banco devem resolver apenas em duas VPCs autorizadas.

- A. Public hosted zone e record público.
- B. Private hosted zone associada às VPCs, além da conectividade necessária.
- C. Registrar novo domínio público para cada subnet.
- D. Usar um EIP no banco.

### B09-06

Which statement about a standard DNS CNAME record is correct?

- A. It maps a name to another canonical name and is normally used below the
  zone apex.
- B. It maps a name directly to an IPv4 address.
- C. It is the Route 53 health-check protocol.
- D. It can coexist with NS and SOA records at the same zone apex.

### B09-07

Which component normally performs recursive lookups and caches answers for a
client?

- A. The domain registry only.
- B. An ALB target group.
- C. A recursive DNS resolver.
- D. An EBS snapshot.

### B09-08

A team lowers a record TTL from 3600 to 60 at the exact moment it changes the
record value. Why can some clients still use the old value for almost an hour?

Which statements explain the behavior and the appropriate cutover practice?

**Choose TWO.**

- A. Resolvers that cached the previous answer can retain it for the previous
  3600-second TTL.
- B. The team should lower the TTL sufficiently before the cutover and wait for
  old cached answers to expire.
- C. Alias records never expire, so their answers cannot be refreshed.
- D. Weighted routing disables DNS caching for all clients.
- E. Route 53 stores the previous record value in an EBS snapshot used by
  resolvers.

### B09-09

A legacy client resolves `ingest.example.com` and can choose among several
equivalent ingestion endpoints returned in one DNS response. The company does
not need latency, geography, weights, or Route 53 health-check selection at the
DNS layer; endpoint health and retries are handled by the client. Architects
must avoid promising per-request balancing because recursive resolvers cache
answers.

Which routing design and limitation fit the requirements?

- A. Simple routing always chooses the endpoint with the lowest measured
  latency.
- B. Simple routing can return one resource or multiple values, but it does not
  provide the health-aware selection behavior of advanced policies and does not
  guarantee equal request distribution after resolver caching.
- C. Simple routing maps users to endpoints by their country automatically.
- D. Simple routing guarantees exact equal request distribution even when
  recursive resolvers and clients cache the answer.

### B09-10

A multi-Region API uses Route 53 health-aware records in front of regional load
balancers. When one Region becomes unhealthy, new DNS answers should stop
directing clients there. Some clients, however, retain cached answers and
long-lived connections, and the operations team expects the DNS health change
to terminate those connections immediately.

Which explanation and design response are correct?

- A. Set the record TTL to zero during the outage and rely on that change to
  revoke already cached answers and terminate established TCP connections.
- B. Lower the TTL only after the Region fails and assume clients immediately
  apply the new value to DNS responses they cached with the previous TTL.
- C. DNS answers can be cached and DNS does not proxy or terminate existing
  connections; combine health-aware DNS with appropriate load-balancer health,
  client retry/reconnect behavior, and connection-draining design.
- D. Enable ALB cross-zone load balancing and rely on it to migrate existing
  sessions between load balancers in different AWS Regions.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B09-01 | | | |
| B09-02 | | | |
| B09-03 | | | |
| B09-04 | | | |
| B09-05 | | | |
| B09-06 | | | |
| B09-07 | | | |
| B09-08 | | | |
| B09-09 | | | |
| B09-10 | | | |
