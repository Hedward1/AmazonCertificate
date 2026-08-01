# B10 — Gabarito comentado

Abra depois das [questões B10](B10_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B10-01 | B | 2.2 |
| B10-02 | C | 3.4 |
| B10-03 | A | 3.4 |
| B10-04 | D | 3.4 |
| B10-05 | B | 2.1 |
| B10-06 | C | 3.4 |
| B10-07 | A | 3.4 |
| B10-08 | D | 3.4 |
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

## B10-03 — Resposta A

- **Requisito central:** retornar até oito IPs saudáveis via DNS.
- **Palavras decisivas:** *até oito*, *saudáveis*, *não proxy*.
- **A:** correta; multivalue pode associar saúde por record.
- **B:** ALB é proxy L7 e não retorna uma lista de IPs de targets.
- **C:** geoproximity não é necessária para seleção aleatória saudável.
- **D:** MX anuncia mail exchangers.
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

## B10-08 — Answer D

- **Requisito central:** forward VPC queries to on-premises DNS.
- **Palavras decisivas:** *VPC workloads*, *corp.local*, *on premises*.
- **A:** inbound handles the reverse query direction.
- **B:** ALB does not provide recursive DNS forwarding.
- **C:** public records would not query the corporate resolver.
- **D:** correct; outbound endpoint plus rule and network path performs forwarding.
- **Regra reutilizável:** AWS VPC → external DNS → outbound.
- **Variação:** associate the rule with VPCs and share through RAM when required;
  include redundant endpoint IPs.
- **Aulas:** 119.
- **Referência:** [Outbound forwarding](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html).

## B10-09 — Answer B

- **Requisito central:** process background jobs from SQS in Beanstalk.
- **Palavras decisivas:** *background*, *Amazon SQS*.
- **A:** health checks are not environment tiers.
- **B:** correct; worker tier processes messages from an SQS queue.
- **C:** a DNS record cannot run application jobs.
- **D:** storage attachment is unrelated to execution tier.
- **Regra reutilizável:** HTTP application → web tier; SQS background jobs →
  worker tier.
- **Variação:** a worker environment can scale its EC2/ASG capacity while the
  queue buffers work.
- **Aulas:** 126–127.
- **Referência:** [Beanstalk worker environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-worker.html).

## B10-10 — Answer C

- **Requisito central:** identify costs hidden behind managed orchestration.
- **Palavras decisivas:** *load-balanced*, *no additional service charge*.
- **A:** Beanstalk provisions resources into the customer account.
- **B:** runtime resources, storage and observability also charge.
- **C:** correct; underlying resources retain normal service pricing/cleanup.
- **D:** CNAME does not stop or delete infrastructure.
- **Regra reutilizável:** no Beanstalk surcharge ≠ free environment.
- **Variação:** terminating an environment should remove managed resources, but
  audit EIP, snapshots, logs, buckets and data independently.
- **Aulas:** 126–127.
- **Referência:** [Beanstalk concepts](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.html).

## Ação após a correção

Classifique cada erro como policy, health, DNS híbrido, arquitetura stateful ou
PaaS/custo. Registre palavra decisiva e regra no
[Caderno de Erros](../Caderno_de_Erros_SAA-C03.md). Depois inverta a direção do
cenário híbrido para confirmar inbound versus outbound.
