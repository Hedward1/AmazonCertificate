# B09 — DNS, Route 53, records, TTL e políticas de roteamento

**Data planejada:** 04/08/2026<br>
**Comece pelas aulas:** [roteiro B09 — aulas 101–110](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b09); o quiz fica no B10<br>
**Domínios:** 2, 3 e 4<br>
**Tarefa principal:** 3.4 — Determine high-performing and/or scalable network architectures<br>
**Secundárias:** 2.2 e 4.4<br>
**Pré-requisito:** [B08 — bancos e cache](B08_RDS_Aurora_RDS_Proxy_e_ElastiCache.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá conseguir:

1. explicar resolver, authoritative server, registrar e registry;
2. percorrer resolução DNS recursiva e caching;
3. diferenciar public e private hosted zones;
4. reconhecer records A, AAAA, CNAME, Alias, NS, SOA, MX e TXT;
5. escolher Alias versus CNAME, inclusive no zone apex;
6. prever efeito do TTL antes e depois de uma alteração;
7. usar simple routing sem tratá-lo como health-aware;
8. calcular weighted routing por pesos relativos;
9. selecionar latency routing pelo menor latency measurement da AWS;
10. distinguir DNS routing de proxy/load balancing;
11. testar DNS sem criar domínio/hosted zone;
12. identificar custo recorrente e cleanup.

## 2. Como estudar as aulas

| Aulas | Tratamento |
|---|---|
| 101 | vocabulário e fluxo de DNS |
| 102 | Route 53: domain registration, DNS e health checking |
| 103 | entender custo/renovação; não registrar domínio no LAB |
| 104–105 | records e targets; acompanhar sem criar EC2 |
| 106 | TTL, cache e mudança planejada |
| 107 | CNAME versus Alias, alta prioridade |
| 108 | simple routing |
| 109 | weighted routing e pesos relativos |
| 110 | latency routing e Regions |

## 3. Fluxo DNS

```text
client/stub resolver
  → recursive resolver/cache
    → root
      → TLD (.com)
        → authoritative name servers for example.com
          → record answer + TTL
```

O resolver recursivo reutiliza respostas até o TTL expirar. Por isso uma
alteração autoritativa não força clientes a esquecer caches imediatamente.
Negative caching também existe para respostas como NXDOMAIN.

- **registrar:** vende/gerencia registro do domínio;
- **registry:** mantém base do TLD;
- **hosted zone:** conjunto de records administrado no Route 53;
- **name server authoritative:** responde com autoridade pela zone;
- **recursive resolver:** consulta a hierarquia em nome do cliente.

Route 53 combina serviços de registro, DNS autoritativo e health checking, mas
cada função tem preço/configuração próprios.

## 4. Public e private hosted zones

| Zona | Visibilidade | Uso |
|---|---|---|
| public hosted zone | internet pública | nomes públicos de aplicações |
| private hosted zone | VPCs associadas | nomes internos e split-horizon |

Uma private hosted zone não torna um endpoint alcançável. Ainda são necessários
rotas, SG/NACL e serviço ouvindo. VPC DNS attributes/resolver influenciam a
resolução interna.

É possível usar o mesmo nome em public e private zones: clientes na VPC podem
receber resposta privada, enquanto internet recebe pública. Isso é split-view
DNS e exige governança para evitar surpresa.

## 5. Records essenciais

| Tipo | Valor | Uso típico |
|---|---|---|
| A | IPv4 | host/endereço IPv4 |
| AAAA | IPv6 | host/endereço IPv6 |
| CNAME | outro nome | alias DNS padrão, não no zone apex |
| Alias Route 53 | recurso AWS/record suportado | pode funcionar no apex; consultas a targets AWS elegíveis não são cobradas como consultas Alias |
| MX | prioridade + mail server | entrega de e-mail |
| TXT | texto | verificação, SPF e metadados |
| NS | authoritative name servers | delegação |
| SOA | metadados da zone | autoridade/serial/timers |

Route 53 Alias é uma extensão do serviço, não um record type DNS separado. Ele
pode apontar para targets AWS suportados, como load balancers, CloudFront,
API Gateway e outros, além de records na mesma hosted zone conforme regras.

## 6. Alias versus CNAME

| Pergunta | CNAME | Alias Route 53 |
|---|---|---|
| permitido no zone apex | não | sim para target suportado |
| destino | hostname | recurso AWS/record suportado |
| resposta ao cliente | cadeia CNAME | tipo A/AAAA solicitado |
| Evaluate Target Health | não como Alias | disponível conforme target/policy |
| custo de query | normal | queries Alias para certos AWS targets são gratuitas |

### Cenário resolvido 1 — apex para ALB

`example.com` deve apontar para um ALB. Use Alias A/AAAA no apex para o load
balancer. CNAME no apex conflitaria com records obrigatórios NS/SOA e não é
permitido pelo DNS padrão.

### Cenário resolvido 2 — serviço externo em subdomínio

`docs.example.com` aponta para `vendor.example.net`, que não é um Alias target
AWS suportado. Use CNAME no subdomínio. Se o fornecedor exigir apex, avalie
recursos suportados/redirect/arquitetura; não invente um Alias genérico.

## 7. TTL

TTL informa por quantos segundos uma resposta pode ficar em cache. TTL baixo
acelera convergência após mudança, mas aumenta consultas e custo/carga. TTL alto
reduz consultas e estabiliza cache, mas prolonga valores antigos.

Para migração planejada:

1. reduza TTL **antes**, aguardando o TTL antigo expirar;
2. altere o record;
3. monitore respostas/saúde;
4. restaure TTL adequado quando estabilizar.

Reduzir o TTL no mesmo instante da troca não elimina respostas antigas já em
cache com o TTL anterior.

## 8. Simple routing

Simple escolhe um record quando há um único recurso ou retorna múltiplos valores
definidos em um record. Ele não oferece associação de health check no mesmo
sentido das políticas avançadas e não é uma estratégia completa de failover.

Se houver múltiplos valores, o cliente/resolver pode receber todos; não há
controle de proporção nem garantia de que um endpoint unhealthy seja removido.

## 9. Weighted routing

Records com o mesmo nome e tipo recebem pesos relativos:

```text
blue weight 80 + green weight 20
→ aproximadamente 80% / 20% das respostas ao longo de muitas queries
```

Não é porcentagem absoluta e não atua por request de aplicação: caching e
resolvers influenciam observação. Peso zero permite parar tráfego normal para um
record, mas regras de saúde e grupos de records têm nuances.

Use para canary, blue/green, migração gradual ou distribuição controlada.

### Cenário resolvido 3 — canary 5%

Crie dois weighted records de mesmo nome/tipo: produção peso 95 e canary peso 5.
Use health checking quando aplicável. Meça no lado da aplicação, pois 20 queries
não garantem exatamente 19/1.

## 10. Latency routing

Latency-based routing escolhe o record na Region que fornece menor latência
medida pela AWS para a origem da consulta/resolver. Não mede o tempo de uma
request específica em tempo real e não escolhe “a Region geograficamente mais
próxima” por regra fixa.

É necessário ter recursos/records nas Regions pretendidas. Combine com health
checks/Evaluate Target Health quando o design exige evitar endpoint unhealthy.

### Cenário resolvido 4 — usuários globais

Uma aplicação ativa em `us-east-1` e `eu-west-1` quer enviar usuários ao endpoint
de menor latência observada. Use latency records com endpoints regionais e
saúde. Geolocation, estudada no B10, seria correta se a decisão fosse localização
ou regra de conteúdo, não performance medida.

## 11. Tabela de decisão

| Requisito | Política/record |
|---|---|
| um recurso sem seleção especial | simple |
| 90/10 ou canary | weighted |
| menor latency AWS entre Regions | latency |
| apex para ALB | Alias A/AAAA |
| subdomínio para hostname externo | CNAME |
| nome interno da VPC | private hosted zone |

## 12. DNS não é load balancer

DNS retorna nomes/endpoints e sofre caching. Ele não mantém conexão, não inspeciona
cada request e não retira instantaneamente uma resposta já cacheada. Um ALB/NLB
recebe conexões e executa health-based distribution próximo ao tráfego.

Route 53 e ELB frequentemente se combinam:

```text
Route 53 Alias/latency/failover
  → regional ALB
    → healthy targets in multiple AZs
```

## 13. Custos e cleanup

Hosted zones geram cobrança mensal; queries, health checks, traffic flow e domain
registration/renewal podem cobrar. Registrar domínio cria compromisso anual e
dados de contato/renovação. Não existe estado “stop” da hosted zone.

No laboratório: use domínios públicos existentes e ferramentas locais. Não
registre domínio, não crie hosted zone, health check ou EC2. Se algo for criado
por engano, confirme ownership e remova records antes da zone; domain registration
não é simplesmente reversível/reembolsável.

## 14. Armadilhas

- DNS propagation não é um temporizador único global;
- CNAME não vai no apex;
- Alias não aponta para qualquer hostname arbitrário;
- TTL baixo não corrige endpoint unhealthy;
- weighted é proporcional e aproximado;
- latency não é geolocation;
- private DNS não cria conectividade;
- resolver cache pode esconder uma mudança correta.

## 15. Checklist e recuperação ativa

- [ ] desenho resolução recursiva;
- [ ] escolho zone pública/privada;
- [ ] diferencio Alias/CNAME no apex;
- [ ] planejo mudança de TTL;
- [ ] calculo pesos relativos;
- [ ] separo latency de proximidade geográfica fixa.

Sem consultar: explique `A`, `AAAA`, `CNAME`, `Alias`, `NS`, `SOA`; depois resolva
apex→ALB, canary 5%, duas Regions por latência e nome interno.

## 16. Ligações e referências oficiais

- [LAB B09](../../05_Laboratorios/LAB_B09_Observacao_DNS_e_Cenarios_Route53.md)
- [Questões B09](../../04_Questoes_e_Revisoes/Blocos/B09_Questoes.md)
- [Gabarito B09](../../04_Questoes_e_Revisoes/Blocos/B09_Gabarito.md)
- [Checklist B09](../../06_Progresso/B09_Checklist_e_Revisoes.md)
- Próximo: [B10 — Route 53 avançado e Beanstalk](B10_Route53_Avancado_Arquiteturas_Classicas_e_Beanstalk.md)
- [How Route 53 routes traffic](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
- [Choosing Alias or non-Alias](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)
- [DNS record types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html)
- [Weighted routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html)
- [Latency routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html)
