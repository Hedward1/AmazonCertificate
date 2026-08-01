# B10 — Gabarito comentado

Abra depois das [questões B10](B10_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B10-01 | B | 2.2 |
| B10-02 | C | 3.4 |
| B10-03 | A,B | 3.4 |
| B10-04 | D | 3.4 |
| B10-05 | B | 2.1 |
| B10-06 | C | 3.4 |
| B10-07 | A | 3.4 |
| B10-08 | A,C | 3.4 |
| B10-09 | B | 2.1 |
| B10-10 | C | 4.2 |

## B10-01 — Resposta B

- **Requisito central:** usar secundário quando primary estiver unhealthy.
- **Palavras decisivas:** *principal*, *secundário*, *unhealthy*.
- **A:** simple não oferece seleção active-passive por saúde.
- **B:** correta; failover records expressam primary/secondary e health.
- **C:** weighted enviaria tráfego ao secundário durante operação saudável.
- **D:** geolocation seleciona localização, não estado primary.
- **Regra reutilizável:** active-passive DNS → failover routing.
- **Variação:** TTL e cache impedem promessa de troca instantânea; dimensione e
  teste o secondary.
- **Aulas:** 111–113.
- **Referência:** [Failover routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html).

## B10-02 — Resposta C

- **Requisito central:** aplicar regra de conteúdo por país.
- **Palavras decisivas:** *licença*, *país*, *mesmo que menor latência*.
- **A:** latency pode selecionar catálogo incompatível.
- **B:** multivalue retorna IPs saudáveis sem regra geográfica.
- **C:** correta; geolocation seleciona continente/país/subdivision e default.
- **D:** simple não expressa localização nem escolha controlada.
- **Regra reutilizável:** conteúdo/compliance por localização → geolocation.
- **Variação:** crie default record para origens sem correspondência quando o
  serviço precisar responder a elas.
- **Aulas:** 114.
- **Referência:** [Geolocation routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html).

## B10-03 — Resposta A,B

- **Requisito central:** retornar até oito IPs saudáveis via DNS.
- **Palavras decisivas:** *até oito*, *saudáveis*, *não proxy*.
- **A:** correta; multivalue pode associar um health check a cada record.
- **B:** correta; uma resposta multivalue contém até oito records saudáveis.
- **C:** ALB é proxy L7 e não faz o DNS retornar uma lista de IPs dos targets.
- **D:** geoproximity não é obrigatória para seleção multivalue saudável.
- **E:** MX anuncia mail exchangers.
- **Regra reutilizável:** múltiplas respostas DNS com health → multivalue.
- **Variação:** caching e escolha do cliente permanecem; não há draining ou
  regras por path.
- **Aulas:** 117.
- **Referência:** [Multivalue routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-multivalue.html).

## B10-04 — Resposta D

- **Requisito central:** trazer queries on-premises para o Resolver da VPC.
- **Palavras decisivas:** *on-premises*, *resolver private hosted zone*.
- **A:** outbound leva queries da VPC para fora, direção oposta.
- **B:** private zone não deve ser publicada.
- **C:** CNAME no apex não cria caminho híbrido.
- **D:** correta; inbound endpoint recebe queries encaminhadas por on-prem DNS.
- **Regra reutilizável:** on-prem → AWS Resolver → inbound.
- **Variação:** use IPs em AZs diferentes, SG TCP/UDP 53 e VPN/DX/TGW.
- **Aulas:** 119.
- **Referência:** [Inbound Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html).

## B10-05 — Resposta B

- **Requisito central:** preservar sessão durante substituição horizontal.
- **Palavras decisivas:** *ASG*, *sessões*, *substituídas*.
- **A:** instance store aumenta acoplamento à instância efêmera.
- **B:** correta; estado compartilhado deixa compute descartável.
- **C:** sem health checks, falhas permanecem servindo.
- **D:** desired=1 reduz resiliência e não compartilha estado.
- **Regra reutilizável:** tier horizontal → externalize required state.
- **Variação:** escolha ElastiCache/database conforme durabilidade e consistência,
  não apenas latência.
- **Aulas:** 121–124.
- **Referência:** [Reliability design principles](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html).

## B10-06 — Answer C

- **Requisito central:** move a traffic boundary using relative bias.
- **Palavras decisivas:** *resource location*, *relative bias*, *not country*.
- **A:** simple has no location/bias logic.
- **B:** IP-based maps known CIDRs rather than geographic resource bias.
- **C:** correct; geoproximity uses resource/user locations and bias.
- **D:** MX controls mail delivery.
- **Regra reutilizável:** geographic boundary plus bias → geoproximity.
- **Variação:** bias effects are relative and can be significant; change in
  small increments and measure.
- **Aulas:** 115.
- **Referência:** [Geoproximity routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html).

## B10-07 — Answer A

- **Requisito central:** delegate an externally registered domain to Route 53.
- **Palavras decisivas:** *third-party registrar*, *old DNS provider*.
- **A:** correct; update registrar delegation to the hosted zone NS set.
- **B:** block snapshots have no DNS authority.
- **C:** SOA is not changed to a private address for delegation.
- **D:** outbound endpoints solve hybrid forwarding, not public delegation.
- **Regra reutilizável:** registrar and authoritative DNS may differ; NS
  delegation chooses the authority.
- **Variação:** creating multiple hosted zones can produce different NS sets;
  delegate the exact intended zone.
- **Aulas:** 118.
- **Referência:** [Using Route 53 with another registrar](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html).

## B10-08 — Answer A,C

- **Requisito central:** forward VPC queries to on-premises DNS.
- **Palavras decisivas:** *VPC workloads*, *corp.local*, *on premises*.
- **A:** correct; an outbound endpoint sends queries toward the on-premises
  resolvers, and the network/security path must permit DNS traffic.
- **B:** inbound endpoints handle queries entering Route 53 Resolver from
  external networks.
- **C:** correct; the conditional forwarding rule matches `corp.local`, names
  the target resolvers, and must be associated with the VPC.
- **D:** a public multivalue record would answer publicly instead of querying
  the corporate resolver.
- **E:** ALB does not provide recursive DNS forwarding.
- **Regra reutilizável:** AWS VPC → external DNS → outbound.
- **Variação:** associate the rule with VPCs and share through RAM when required;
  include redundant endpoint IPs.
- **Aulas:** 119.
- **Referência:** [Outbound forwarding](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html).

## B10-09 — Answer B

- **Requisito central:** decouple synchronous order intake from independently
  scalable SQS-backed processing within Elastic Beanstalk.
- **Palavras decisivas:** *return quickly*, *places each order in SQS*,
  *separately scalable*, *not public HTTP endpoints*.
- **A:** Route 53 health checks observe endpoints; authoritative DNS servers do
  not execute the application's background jobs.
- **B:** correct; the worker tier integrates an SQS queue with worker instances
  and can scale independently of the public web environment.
- **C:** DNS records describe name resolution and cannot carry or execute the
  queued order workload.
- **D:** EBS Multi-Attach is a block-storage attachment capability, not a
  Beanstalk execution tier or message consumer.
- **Regra reutilizável:** synchronous HTTP intake → web tier; buffered SQS work →
  separately scaled worker tier.
- **Variação:** if Beanstalk constraints no longer fit, the same decoupling
  principle can be implemented with another compute consumer and SQS.
- **Aulas:** 126–127.
- **Referência:** [Beanstalk worker environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-worker.html).

## B10-10 — Answer C

- **Requisito central:** decommission a zero-traffic managed environment without
  confusing absence of a Beanstalk surcharge with absence of resource cost or
  retention obligations.
- **Palavras decisivas:** *traffic falls to zero*, *removes CNAME*, *leaves the
  environment running*, *retention requirement*.
- **A:** reducing instance capacity can lower compute cost, but a retained load
  balancer, storage, logs, and other provisioned resources keep their own
  lifecycle and pricing.
- **B:** immediate deletion without an ownership and retention inventory can
  destroy audit evidence or recoverable data that the scenario requires the
  team to preserve.
- **C:** correct; the team must inventory underlying resources, terminate what is
  obsolete, and preserve or separately manage artifacts required for retention.
- **D:** changing DNS and archiving source code do not terminate the environment
  or deprovision its supporting resources.
- **Regra reutilizável:** no platform surcharge ≠ free architecture; decommission
  by resource ownership, dependency, and retention policy.
- **Variação:** environment termination can remove managed components, but audit
  retained logs, buckets, snapshots, Elastic IPs, and external dependencies
  separately.
- **Aulas:** 126–127.
- **Referência:** [Beanstalk concepts](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.html).

## Ação após a correção

Classifique cada erro como policy, health, DNS híbrido, arquitetura stateful ou
PaaS/custo. Registre palavra decisiva e regra no
[Caderno de Erros](../Caderno_de_Erros_SAA-C03.md). Depois inverta a direção do
cenário híbrido para confirmar inbound versus outbound.
