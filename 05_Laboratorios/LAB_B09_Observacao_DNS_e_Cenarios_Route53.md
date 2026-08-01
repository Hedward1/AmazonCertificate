# LAB B09 — Observação DNS e cenários Route 53

**Tempo:** 40 minutos<br>
**Aulas:** 101–110<br>
**Capítulo:** [B09](../03_Guia_do_Estudante/Capitulos/B09_DNS_Route53_Records_TTL_e_Routing.md)<br>
**Modo:** consultas públicas + diagramas, sem recursos AWS<br>
**Custo:** USD 0,00

## 1. Resultado esperado

Ao terminar, você deverá ter:

- evidência de resolução A/AAAA/CNAME/NS/SOA/TXT em domínio público;
- TTL observado duas vezes;
- fluxo stub → recursive → authoritative desenhado;
- quatro cenários Route 53 resolvidos;
- comparação Alias/CNAME;
- inventário Route 53 inicial e final igual;
- zero domínio, hosted zone, record ou health check criado.

## 2. Conexão com o exame

| Exercício | Tarefa |
|---|---|
| records e resolução | 3.4 |
| routing policies | 3.4 / 2.2 |
| TTL/custo | 4.4 |

## 3. Preflight (5 min)

- [ ] identidade não root e Region registradas apenas se abrir console;
- [ ] inventário de hosted zones/domains/health checks;
- [ ] nenhuma informação de conta será copiada;
- [ ] usar `Resolve-DnsName` no PowerShell;
- [ ] escolher somente domínios públicos conhecidos, sem dados pessoais;
- [ ] não registrar domínio nem concluir criação de zone.

## 4. Observação DNS (12 min)

No PowerShell, execute consultas read-only equivalentes a:

```powershell
Resolve-DnsName aws.amazon.com -Type A
Resolve-DnsName aws.amazon.com -Type AAAA
Resolve-DnsName amazon.com -Type NS
Resolve-DnsName amazon.com -Type SOA
Resolve-DnsName amazon.com -Type MX
Resolve-DnsName amazon.com -Type TXT
```

Os resultados variam. Não trate a ausência de AAAA/MX/TXT em um nome específico
como erro do DNS; selecione outro domínio público se necessário.

Registre somente:

| Consulta | Tipo | TTL | Quantidade | Interpretação |
|---|---|---:|---:|---|
| | A | | | |
| | AAAA | | | |
| | NS | | | |
| | SOA | | | |
| | MX | | | |
| | TXT | | | |

Repita uma consulta A após 30 segundos. Explique por que o TTL observado pode
diminuir no cache e depois voltar ao consultar outro resolver.

## 5. Cenários de arquitetura (15 min)

### Cenário A — apex para ALB

Escolha Alias A/AAAA. Anote por que CNAME é inválido no apex e quando Evaluate
Target Health faz sentido.

### Cenário B — canary

Produção peso 95, canary peso 5. Calcule proporções relativas e explique por que
dez consultas não provam a distribuição.

### Cenário C — duas Regions

Usuários devem receber endpoint de menor latência medida. Escolha latency records
e desenhe health checks/ALBs regionais.

### Cenário D — nome interno

`db.corp.example` deve resolver somente em duas VPCs autorizadas. Escolha private
hosted zone associada às VPCs e liste conectividade que DNS não cria.

## 6. Walkthrough no console (5 min)

Abra Route 53 e localize Hosted zones, Registered domains, Health checks e
Resolver. Inicie a tela de criação de record em uma zone somente se já houver
zone de laboratório autorizada; caso contrário, use capturas/documentação.
Localize name, type, Alias, target, TTL e routing policy. Cancele.

## 7. Validação (2 min)

- [ ] Alias/CNAME corretamente separados;
- [ ] weighted calculado por razão;
- [ ] latency não descrito como país;
- [ ] private zone não descrita como firewall;
- [ ] nenhum recurso criado.

## 8. Cleanup seguro (1 min)

Feche console e shell. O inventário deve ser idêntico. Se uma hosted zone foi
criada acidentalmente, não a exclua sem confirmar records/ownership; remova
somente artefatos B09. Um domínio registrado não deve ser abandonado nem ter
autorenew alterado sem decisão explícita do proprietário.

## 9. Solução de problemas

| Sintoma | Verificação |
|---|---|
| `Non-existent domain` | nome/tipo, authoritative NS, negative cache |
| resposta antiga | TTL anterior e resolver usado |
| private name não resolve | associação da VPC, DNS attributes, Resolver |
| Alias target não aparece | tipo/Region/integração suportada |
| weighted parece desigual | amostra, caching e pesos relativos |
| mudança não chega | delegação NS e caches, não “propagation” genérica |

## 10. Referências oficiais

- [Route 53 concepts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html)
- [Supported record types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html)
- [Alias versus non-Alias](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html)
- [Weighted routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html)
- [Latency routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html)
