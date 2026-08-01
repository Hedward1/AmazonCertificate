# B09 — Questões: DNS e Route 53 básico

**Quantidade:** 10 · **Idioma:** 5 português/5 inglês · **Tempo:** 15 min<br>
**Gabarito:** [arquivo separado](B09_Gabarito.md)

Registre a confiança antes de corrigir. Uma resposta certa por adivinhação deve
entrar no Caderno de Erros como baixa confiança.

Não consulte o console durante a tentativa.

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B09-01 | 3.4 | Alias apex | Situacional | Básica | Português |
| B09-02 | 3.4 | TTL | Situacional | Intermediária | Português |
| B09-03 | 3.4 | Weighted | Situacional | Básica | Português |
| B09-04 | 3.4 | Latency | Situacional | Intermediária | Português |
| B09-05 | 3.4 | Private hosted zone | Situacional | Básica | Português |
| B09-06 | 3.4 | CNAME | Fundamental | Básica | Inglês |
| B09-07 | 3.4 | DNS roles | Fundamental | Intermediária | Inglês |
| B09-08 | 4.4 | TTL change | Situacional | Intermediária | Inglês |
| B09-09 | 3.4 | Simple routing | Fundamental | Intermediária | Inglês |
| B09-10 | 3.4 | DNS versus ELB | Situacional | Intermediária | Inglês |

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

- A. Criar weighted records com pesos relativos 90 e 10.
- B. Usar latency routing na mesma Region.
- C. Usar um CNAME sem pesos.
- D. Usar simple routing com uma única resposta.

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

- A. Alias records never expire.
- B. Route 53 copies values into EBS.
- C. Weighted routing disables caching.
- D. Resolvers may have cached the previous answer with the previous 3600-second
  TTL.

### B09-09

Which statement about simple routing is correct?

- A. It always routes by lowest latency.
- B. It can return one resource or multiple values, but it does not provide the
  health-aware selection behavior of advanced policies.
- C. It routes users by country.
- D. It guarantees equal request distribution after resolver caching.

### B09-10

A company expects a DNS policy to immediately terminate existing connections to
an unhealthy EC2 instance. What is wrong with this expectation?

- A. DNS works only with IPv6.
- B. Route 53 cannot point to load balancers.
- C. DNS answers are cached and do not proxy or terminate existing connections;
  use health-aware endpoints/load balancing as required.
- D. TTL controls EBS attachment.

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
