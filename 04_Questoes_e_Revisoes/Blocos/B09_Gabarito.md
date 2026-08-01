# B09 — Gabarito comentado

Abra depois das [questões B09](B09_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B09-01 | B | 3.4 |
| B09-02 | C | 3.4 |
| B09-03 | A | 3.4 |
| B09-04 | D | 3.4 |
| B09-05 | B | 3.4 |
| B09-06 | A | 3.4 |
| B09-07 | C | 3.4 |
| B09-08 | D | 4.4 |
| B09-09 | B | 3.4 |
| B09-10 | C | 3.4 |

## B09-01 — Resposta B

- **Requisito central:** apontar zone apex a um ALB.
- **Palavras decisivas:** *apex*, *ALB*.
- **A:** CNAME padrão não é permitido no apex com NS/SOA.
- **B:** correta; Route 53 Alias A/AAAA suporta ALB e apex.
- **C:** MX define mail exchanger.
- **D:** PTR trata reverse DNS e private zone não publica o apex.
- **Regra reutilizável:** apex → recurso AWS suportado → Alias.
- **Aulas:** 107.
- **Referência:** [Alias versus non-Alias](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html).

## B09-02 — Resposta C

- **Requisito central:** reduzir duração de respostas antigas na migração.
- **Palavras decisivas:** *amanhã*, *TTL 24 horas*.
- **A:** caches já receberam o TTL antigo.
- **B:** excluir a zone quebra autoridade e não limpa resolvers.
- **C:** correta; baixe antes, aguarde, migre e normalize depois.
- **D:** MX não representa endpoint web.
- **Regra reutilizável:** TTL deve ser reduzido antes da mudança.
- **Aulas:** 106.
- **Referência:** [TTL values](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-basic.html#rrsets-values-basic-ttl).

## B09-03 — Resposta A

- **Requisito central:** canary com proporção aproximada.
- **Palavras decisivas:** *90%/10%*, *respostas DNS*.
- **A:** correta; weighted usa pesos relativos.
- **B:** latency seleciona por desempenho regional.
- **C:** CNAME sozinho não oferece peso.
- **D:** simple não controla proporção.
- **Regra reutilizável:** canary/blue-green gradual → weighted.
- **Aulas:** 109.
- **Referência:** [Weighted routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html).

## B09-04 — Resposta D

- **Requisito central:** selecionar Region pela latência AWS.
- **Palavras decisivas:** *duas Regions*, *menor latência medida*.
- **A:** 50/50 ignora origem/desempenho.
- **B:** private zone trata visibilidade, não seleção regional pública.
- **C:** país é regra de geolocation, não latency.
- **D:** correta; latency records selecionam endpoint regional adequado.
- **Regra reutilizável:** menor latência entre Regions → latency routing.
- **Aulas:** 110.
- **Referência:** [Latency routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html).

## B09-05 — Resposta B

- **Requisito central:** resolução restrita a VPCs.
- **Palavras decisivas:** *apenas*, *duas VPCs*.
- **A:** public zone expõe respostas publicamente.
- **B:** correta; private zone associada limita a resolução, com rede separada.
- **C:** registros públicos não são necessários.
- **D:** EIP não controla DNS privado.
- **Regra reutilizável:** nomes internos de VPC → private hosted zone.
- **Aulas:** 102–105.
- **Referência:** [Private hosted zones](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html).

## B09-06 — Answer A

- **Requisito central:** identify CNAME semantics.
- **Palavras decisivas:** *canonical name*, *zone apex*.
- **A:** correct; it maps an owner name to another name.
- **B:** an A record stores IPv4.
- **C:** health checks are separate resources/configuration.
- **D:** CNAME cannot coexist with other data at the same owner/apex.
- **Regra reutilizável:** subdomain → arbitrary hostname can use CNAME.
- **Aulas:** 107.
- **Referência:** [CNAME record type](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#CNAMEFormat).

## B09-07 — Answer C

- **Requisito central:** identify recursive lookup and caching role.
- **Palavras decisivas:** *for a client*, *caches answers*.
- **A:** registry maintains TLD registration data.
- **B:** target groups route application traffic.
- **C:** correct; recursive resolvers query/caches DNS answers.
- **D:** snapshots store block recovery data.
- **Regra reutilizável:** client asks recursive resolver; authoritative serves zone.
- **Aulas:** 101–102.
- **Referência:** [DNS concepts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html).

## B09-08 — Answer D

- **Requisito central:** explain old answer after simultaneous TTL reduction.
- **Palavras decisivas:** *exact moment*, *previous 3600*.
- **A:** Alias responses still follow DNS caching behavior.
- **B:** EBS is unrelated.
- **C:** weighted records also have TTL/caching.
- **D:** correct; cached entries retain the TTL supplied earlier.
- **Regra reutilizável:** lowering TTL is not retroactive.
- **Aulas:** 106.
- **Referência:** [TTL](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-basic.html#rrsets-values-basic-ttl).

## B09-09 — Answer B

- **Requisito central:** define simple routing limitations.
- **Palavras decisivas:** *simple routing*, *multiple values*.
- **A:** latency is another policy.
- **B:** correct; simple lacks advanced health-aware selection.
- **C:** geolocation is another policy.
- **D:** resolver caching prevents per-request equal guarantees.
- **Regra reutilizável:** no special routing requirement → simple.
- **Aulas:** 108.
- **Referência:** [Simple routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-simple.html).

## B09-10 — Answer C

- **Requisito central:** distinguish DNS answers from connection proxying.
- **Palavras decisivas:** *immediately*, *existing connections*.
- **A:** DNS supports A and AAAA.
- **B:** Route 53 Alias can target supported load balancers.
- **C:** correct; cached DNS does not terminate existing flows.
- **D:** TTL does not attach storage.
- **Regra reutilizável:** DNS selects endpoints; ELB handles live connections.
- **Aulas:** 102 e 108–110.
- **Referência:** [How Route 53 routes traffic](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html).

## Ação após a correção

Registre erros no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md). Reescreva a
regra usando apex, TTL, weight, latency, resolver e authoritative corretamente.

## Variações para confirmar entendimento

- Se o apex mudar para um subdomínio e o destino for externo, reavalie CNAME.
- Se a proporção 90/10 mudar para preferência por desempenho regional, troque o
  critério weighted por latency.
- Se “menor latência” mudar para “conteúdo obrigatório por país”, não preserve
  latency: a política será geolocation, estudada no B10.
- Se o nome público mudar para um nome interno de VPC, reavalie a hosted zone e
  lembre que resolução não cria conectividade.
- Se o requisito disser “encerrar conexões existentes”, DNS sozinho é
  insuficiente; projete o endpoint/load balancer e comportamento do cliente.

Essas variações testam se a resposta veio das palavras decisivas. Refaça a
questão mudando somente uma restrição e explique por que a alternativa correta
mudou, mantendo as demais inválidas.
