# B10 — Route 53 avançado, arquiteturas clássicas e Elastic Beanstalk

**Data planejada:** 05/08/2026<br>
**Comece pelas aulas:** [roteiro B10 — aulas 111–127](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b10); faça `Q07` e `Q08`<br>
**Domínios:** 2, 3 e 4<br>
**Tarefas principais:** 2.2 — Design highly available and/or fault-tolerant architectures; 2.1 — Design scalable and loosely coupled architectures<br>
**Secundárias:** 3.2, 3.4, 4.2 e 4.4<br>
**Pré-requisito:** [B09 — DNS e Route 53 básico](B09_DNS_Route53_Records_TTL_e_Routing.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá conseguir:

1. explicar health checks, calculated checks e CloudWatch alarm checks;
2. projetar active-passive failover;
3. selecionar geolocation, geoproximity ou IP-based routing;
4. reconhecer multivalue como DNS health-aware, não ELB;
5. delegar domínio de registrar externo ao Route 53;
6. desenhar inbound e outbound Route 53 Resolver endpoints;
7. aplicar conditional forwarding em DNS híbrido;
8. combinar Route 53, ELB, ASG, RDS e cache em arquiteturas clássicas;
9. escolher inicialização por AMI, user data, snapshot ou EFS;
10. explicar application, version, environment e platform no Beanstalk;
11. comparar single-instance, load-balanced web e worker environment;
12. identificar recursos e custos escondidos pelo serviço gerenciado.

## 2. Como estudar as aulas

| Aulas | Tratamento |
|---|---|
| 111–113 | health checks e failover, alta prioridade |
| 114 | geolocation: localização/regra de conteúdo |
| 115 | geoproximity: localização dos recursos e bias |
| 116 | IP-based: CIDRs conhecidos |
| 117 | multivalue: até oito respostas saudáveis |
| 118 | registrar externo e delegação NS |
| 119 | Resolver endpoints/rules híbridos |
| 120 | cleanup; não remover domínio/zone sem ownership |
| Q07 | quiz Route 53 |
| 121–125 | arquiteturas clássicas e inicialização rápida |
| 126–127 | Elastic Beanstalk; walkthrough sem criar environment |
| Q08 | quiz de arquiteturas |

## 3. Health checks

Route 53 health checks são globais e podem observar endpoints públicos por HTTP,
HTTPS ou TCP, monitorar outros health checks (calculated) ou o estado de um
CloudWatch alarm. Eles não ficam “dentro” de uma VPC para alcançar diretamente
um endereço privado.

```text
Route 53 health checkers → public endpoint
                           └→ status + thresholds
record/policy → associate health check
```

Para recurso AWS Alias como ELB, **Evaluate Target Health** normalmente evita
criar health check separado para o load balancer. Ele herda/avalia a saúde do
target AWS conforme regras do serviço.

Health check deve testar uma função representativa e barata. Um path que sempre
retorna 200 é raso; um que falha quando qualquer dependência opcional cai pode
retirar todas as Regions. Use desenho de dependências e blast radius.

### Cenário resolvido 1 — endpoint privado

Um serviço privado precisa afetar DNS quando uma métrica indica falha. Health
checkers públicos não alcançam seu IP privado. Publique uma métrica/CloudWatch
alarm apropriada e crie health check baseado no alarm, ou use automação/target
health compatível. Não abra o serviço à internet somente para testá-lo.

## 4. Failover routing

Failover cria records primary e secondary com o mesmo nome/tipo. Quando primary
é saudável, ele é retornado. Quando unhealthy e secondary saudável, Route 53
retorna secondary.

TTL e caching significam que não é failover instantâneo por request. O secondary
precisa estar pronto, dimensionado e testado. Backups sem ambiente recuperável
não constituem um secondary ativo.

### Cenário resolvido 2 — site estático de manutenção

Primary Alias aponta ao ALB. Secondary aponta a um site estático apropriado. Use
failover e saúde do target; garanta que o conteúdo secundário, DNS e TLS atendam
o domínio. O site não processará operações dinâmicas, portanto comunique modo
degradado.

## 5. Geolocation, geoproximity e IP-based

| Política | Entrada/decisão | Uso |
|---|---|---|
| geolocation | continente, país ou subdivision do usuário | localização de conteúdo, compliance, idioma |
| geoproximity | localização do recurso/usuário e bias | deslocar fronteira de tráfego entre recursos |
| IP-based | CIDR da origem do resolver/consulta | redes conhecidas, ISP/corporate mapping |
| latency | medição AWS entre origem e Region | performance; revisada do B09 |

Geolocation deve ter default record para origens sem correspondência, quando
necessário. Geoproximity pode ser configurado diretamente nos records; Traffic
Flow é opcional para políticas complexas e visualização. Seu bias é relativo e
mudanças podem ter efeitos grandes, portanto ajuste e meça. IP-based não é
security control: um record diferente não impede acesso direto ao endpoint.

### Cenário resolvido 3 — conteúdo licenciado

Usuários do país X devem receber endpoint com catálogo permitido, qualquer que
seja a latência. Escolha geolocation com default seguro. Latency poderia mandar
um usuário ao catálogo errado; geoproximity não expressa regra jurídica exata.

### Cenário resolvido 4 — rede corporativa conhecida

Consultas vindas de CIDRs corporativos devem receber endpoint dedicado. Use
IP-based routing. Ainda aplique autenticação/autorização no endpoint; DNS não é
controle de acesso.

## 6. Multivalue answer

Multivalue retorna até oito records saudáveis. Se houver oito ou menos, retorna
todos; se houver mais, pode selecionar conjuntos diferentes para resolvers
diferentes. Cada record pode ter health check. Ele melhora disponibilidade DNS
e permite múltiplos IPs, mas não substitui load balancer:

- o cliente recebe e escolhe respostas;
- respostas ficam em cache;
- não há proxy, listener, connection draining ou regras L7;
- se todos forem unhealthy, Route 53 pode retornar respostas unhealthy para não
  devolver nada, conforme comportamento documentado.

## 7. Domínio em terceiro e Route 53

Registrar e DNS autoritativo podem ser fornecedores diferentes. Para usar Route
53 com domínio registrado externamente:

1. crie public hosted zone;
2. obtenha os quatro name servers delegados;
3. atualize os NS no registrar externo;
4. evite criar múltiplas zones e delegar a errada;
5. valide com consulta NS pública;
6. só remova a antiga depois da convergência.

Copiar records sem mudar delegação não altera quem responde autoritativamente.

## 8. Route 53 Resolver híbrido

```text
on-prem DNS ──conditional forward aws.corp──> inbound endpoint IPs
                                                → private hosted zone/VPC DNS

VPC workload ──query corp.local──> outbound endpoint
                                   → rule forwards to on-prem DNS IPs
```

- **inbound endpoint:** consultas de on-premises entram no Route 53 Resolver;
- **outbound endpoint:** queries da VPC são encaminhadas a DNS externo por
  Resolver rules;
- rules podem ser compartilhadas com AWS RAM;
- use múltiplos IPs/AZs, SG TCP/UDP 53 e conectividade VPN/DX/TGW;
- não encaminhe `.` indiscriminadamente sem entender o impacto;
- endpoints cobram por IP/hora e queries processadas conforme preço vigente.

## 9. Arquiteturas clássicas

### Stateless web tier

```text
Route 53 Alias → ALB → ASG EC2 across AZs
                         ├→ RDS Multi-AZ
                         ├→ ElastiCache session/cache
                         └→ EFS or S3 for shared content
```

Instâncias são substituíveis; estado sai da frota. ALB health checks e ASG
restauram compute; RDS Multi-AZ trata banco; backups tratam erro lógico.

### Escala de leitura

Use read replicas/Aurora readers quando queries read-only dominam. Cache atende
dados repetidos e tolerância a staleness. Não adicione cache sem estratégia de
invalidação.

### Inicialização rápida

| Conteúdo | Mecanismo |
|---|---|
| SO e dependências estáveis | AMI pré-construída |
| configuração pequena/dinâmica | user data/config service |
| dados de bloco | snapshot → volume |
| arquivos compartilhados | EFS/S3 conforme interface |

AMI reduz bootstrap, mas exige pipeline de atualização. User data enorme torna
launch lento e frágil. Não coloque segredos em AMI/user data.

## 10. Elastic Beanstalk

Beanstalk orquestra recursos da conta para implantar aplicações. O serviço não
elimina a cobrança dos recursos provisionados.

| Conceito | Significado |
|---|---|
| application | contêiner lógico de versions/environments/configurations |
| application version | versão rotulada do código em S3 |
| environment | coleção de recursos executando uma versão |
| platform | SO, runtime, web/app server e componentes Beanstalk |
| configuration | parâmetros dos recursos e plataforma |

Environment tiers:

- **web server:** atende HTTP; pode ser single-instance ou load-balanced;
- **worker:** consome mensagens de SQS para background processing.

Deployment policies trocam velocidade, custo e disponibilidade: all-at-once,
rolling, rolling with additional batch, immutable e traffic splitting conforme
plataforma/suporte. Immutable cria frota nova e facilita rollback, com custo
temporário maior. Blue/green usa environments separados e swap de CNAME.

### Cenário resolvido 5 — equipe pequena

Uma equipe quer deploy de aplicação web padrão sem operar manualmente ALB, ASG
e EC2, mas aceita esses recursos na conta. Use load-balanced Beanstalk environment.
Se o requisito fosse controle fino de orquestração/container, outros serviços
poderiam ser melhores; Beanstalk não é “serverless”.

## 11. Tabela de decisão

| Requisito | Escolha |
|---|---|
| primary/secondary | failover |
| país/continente | geolocation |
| mover fronteira por bias | geoproximity |
| CIDRs conhecidos | IP-based |
| até 8 respostas saudáveis | multivalue |
| on-prem consulta private zone | inbound endpoint |
| VPC consulta DNS on-prem | outbound endpoint + rule |
| PaaS simples em EC2 | Elastic Beanstalk |

## 12. Custos e cleanup

Health checks, Resolver endpoints, queries, hosted zones e traffic flow podem
cobrar. Beanstalk em si não tem taxa adicional, mas EC2, EBS, ELB, ASG, S3,
CloudWatch e dados cobram. Terminar environment deve remover seus recursos, mas
audite EIP, snapshots, buckets/versions e logs.

O LAB é desenho/read-only. Não crie Resolver endpoint nem environment Beanstalk:
mesmo poucos minutos podem criar múltiplos recursos e dependências.

## 13. Armadilhas

- health check público não alcança IP privado;
- failover sofre TTL/cache;
- geolocation não é latency;
- IP-based não é firewall;
- multivalue não é ELB;
- inbound/outbound são nomeados pela perspectiva do Resolver/VPC;
- mudar registrar não é necessário para mudar DNS, mas mudar NS é;
- Beanstalk cria recursos cobrados na sua conta;
- environment worker usa SQS, não atende web diretamente.

## 14. Checklist e recuperação ativa

- [ ] escolho seis policies sem hesitar;
- [ ] desenho health e TTL no failover;
- [ ] desenho DNS híbrido nas duas direções;
- [ ] decomponho arquitetura clássica por falha;
- [ ] seleciono mecanismo de bootstrap;
- [ ] explico Beanstalk e custos subjacentes.

## 15. Ligações e referências oficiais

- [LAB B10](../../05_Laboratorios/LAB_B10_Failover_DNS_Hibrido_e_Beanstalk.md)
- [Questões B10](../../04_Questoes_e_Revisoes/Blocos/B10_Questoes.md)
- [Gabarito B10](../../04_Questoes_e_Revisoes/Blocos/B10_Gabarito.md)
- [Checklist B10](../../06_Progresso/B10_Checklist_e_Revisoes.md)
- Próximo: [B11 — S3](B11_S3_Seguranca_Versioning_Replication_Classes_e_Eventos.md)
- [Route 53 health checking](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html)
- [Routing policy guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
- [Geoproximity routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html)
- [Multivalue routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-multivalue.html)
- [Route 53 Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)
- [Elastic Beanstalk concepts](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.html)
- [Beanstalk deployment policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html)
