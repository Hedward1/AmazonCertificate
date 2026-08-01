# LAB B10 — Failover, DNS híbrido e Elastic Beanstalk

**Tempo:** 20 minutos<br>
**Aulas:** 111–127<br>
**Capítulo:** [B10](../03_Guia_do_Estudante/Capitulos/B10_Route53_Avancado_Arquiteturas_Classicas_e_Beanstalk.md)<br>
**Modo:** diagrama e console read-only<br>
**Custo:** USD 0,00 causado pelo laboratório

## 1. Resultado esperado

- diagrama failover primary/secondary com saúde e TTL;
- mapa das políticas avançadas;
- fluxo inbound/outbound de DNS híbrido;
- arquitetura web clássica Multi-AZ;
- cartão de environment Beanstalk;
- inventário inicial/final igual;
- zero health check, endpoint ou environment criado.

## 2. Conexão com o exame

| Evidência | Tarefa |
|---|---|
| DNS failover e saúde | 2.2 |
| políticas e híbrido | 3.4 / 4.4 |
| arquitetura desacoplada | 2.1 |
| compute elástico | 3.2 / 4.2 |

## 3. Preflight (3 min)

- [ ] identidade não root e inventário confirmados;
- [ ] não criar Route 53 health check;
- [ ] não criar Resolver endpoint (cobra por IP/hora);
- [ ] não criar Beanstalk environment (provisiona EC2/ELB/ASG etc.);
- [ ] não copiar IDs/ARNs/domínios reais;
- [ ] cronômetro de 20 minutos iniciado.

## 4. Failover em papel (5 min)

```text
app.example.test
  primary Alias → ALB Region A → targets Multi-AZ
  secondary     → página de manutenção/ALB Region B
```

Preencha:

| Campo | Primary | Secondary |
|---|---|---|
| record type/target | | |
| saúde | | |
| TTL | | |
| capacidade | | |
| modo degradado | | |
| retorno/failback | | |

Simule primary unhealthy. Considere cache anterior e diga quando o secondary
pode aparecer a um novo resolver. Não prometa interrupção zero.

## 5. Policies em 60 segundos (3 min)

Associe:

- país obrigatório → geolocation;
- bias entre localizações → geoproximity;
- CIDR corporativo → IP-based;
- até oito IPs saudáveis → multivalue;
- menor latência regional → latency;
- primary/secondary → failover.

## 6. DNS híbrido (4 min)

Desenhe dois Resolver endpoint IPs por direção em AZs distintas:

1. on-prem → inbound → `aws.corp` private hosted zone;
2. VPC → outbound rule `corp.local` → dois DNS on-prem;
3. VPN/DX/TGW como conectividade;
4. SG permitindo TCP/UDP 53 somente dos resolvers;
5. regra compartilhada via RAM como opção.

Marque setas com a perspectiva do Resolver para não inverter inbound/outbound.

## 7. Arquitetura e Beanstalk (3 min)

Desenhe Route 53 → ALB → ASG em duas AZs → RDS Multi-AZ, com sessão em cache e
arquivos em S3/EFS. Transforme o web tier em um Beanstalk load-balanced
environment e liste recursos que continuarão aparecendo na conta.

Cartão:

| Campo | Decisão |
|---|---|
| application/version | |
| platform | |
| web ou worker | |
| single/load-balanced | |
| deployment policy | |
| rollback | |
| recursos/custo | |

## 8. Validação e cleanup (2 min)

- [ ] health check não tenta acessar IP privado diretamente;
- [ ] geolocation/geoproximity/IP-based não foram trocados;
- [ ] endpoints híbridos estão na direção correta;
- [ ] Beanstalk não foi chamado de serverless;
- [ ] nenhum botão de criação foi concluído;
- [ ] inventário final = inicial.

Cleanup: fechar console/shell. Se algo foi criado por engano, pare e confirme
tags/ownership. Exclua somente environment/endpoints/checks B10 e audite EC2,
ELB, ASG, EBS, EIP, S3, logs e ENIs após a exclusão completar.

## 9. Solução de problemas

| Sintoma | Verificação |
|---|---|
| failover não ocorre | associação de saúde, TTL e estado secondary |
| private health falha | usar alarm/arquitetura, não checker público direto |
| on-prem não resolve AWS | inbound, rota, SG 53, conditional forward |
| VPC não resolve on-prem | outbound, rule association e DNS IPs |
| environment caro | recursos subjacentes e tipo load-balanced |
| domínio externo não usa zone | delegação NS no registrar |

## 10. Referências oficiais

- [DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
- [Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-choose-vpc.html)
- [Forwarding rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html)
- [Beanstalk environment types](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-types.html)
- [Beanstalk concepts](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.html)
