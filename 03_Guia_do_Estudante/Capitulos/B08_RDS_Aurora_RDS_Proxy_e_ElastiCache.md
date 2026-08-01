# B08 — RDS, Aurora, RDS Proxy e ElastiCache

**Data planejada:** 03/08/2026<br>
**Nível:** iniciante absoluto<br>
**Comece pelas aulas:** [roteiro B08 — aulas 087–100](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b08); faça `Q06`<br>
**Domínios:** 1 — Secure; 2 — Resilient; 3 — High-Performing; 4 — Cost-Optimized<br>
**Tarefas principais:** 3.3 — Determine high-performing database solutions; 2.2 — Design highly available and/or fault-tolerant architectures<br>
**Secundárias:** 1.3 e 4.3<br>
**Pré-requisito:** [B07 — TLS e Auto Scaling](B07_TLS_ACM_Deregistration_e_Auto_Scaling.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá conseguir:

1. decidir entre RDS DB instance, Multi-AZ DB instance e read replica;
2. reconhecer Multi-AZ DB cluster como opção diferente do standby tradicional;
3. explicar failover, endpoint e DNS caching;
4. selecionar Aurora por arquitetura de cluster e storage distribuído;
5. diferenciar backup automático, snapshot manual e point-in-time restore;
6. aplicar subnet group, security group, encryption e Secrets Manager;
7. explicar quando RDS Custom é necessário;
8. usar RDS Proxy para pooling e picos de conexão;
9. escolher cache-aside, write-through e session store;
10. comparar Valkey/Redis OSS e Memcached por requisito;
11. reconhecer portas sem usá-las como único controle de segurança;
12. identificar custos e executar cleanup correto.

## 2. Como estudar as aulas

| Aulas | Tratamento |
|---|---|
| 87 | modelo administrado do RDS e motores |
| 88 | alta prioridade: read replica versus Multi-AZ |
| 89 | walkthrough; não crie sem estimativa aceita |
| 90 | RDS Custom somente quando acesso ao SO/database é requisito |
| 91–93 | Aurora, endpoints, replicas e Serverless v2 |
| 94 | backup, restore e monitoring |
| 95 | rede, IAM, KMS e autenticação |
| 96 | pooling com RDS Proxy |
| 97–99 | ElastiCache e padrões de cache |
| 100 | portas como vocabulário operacional |
| Q06 | fazer antes das questões autorais |

## 3. Modelo mental do RDS

RDS administra tarefas como provisionamento, backups, patching e substituição de
infraestrutura conforme o motor e configuração. O cliente continua responsável
por schema, queries, índices, contas do banco, parâmetros permitidos, rede e
classificação dos dados.

```text
Application private subnets
       │ TCP database port
       ▼
RDS endpoint → primary DB instance
                 └→ synchronous standby in another AZ (Multi-AZ DB instance)
```

Uma DB subnet group deve abranger subnets em pelo menos duas AZs para opções de
resiliência. Bancos normalmente permanecem privados; a aplicação alcança o SG
do banco na porta necessária. “Publicly accessible=false” não substitui SG,
routes ou autenticação.

## 4. Multi-AZ versus read replica

| Recurso | Multi-AZ DB instance | Read replica |
|---|---|---|
| objetivo principal | HA/failover | escalar leitura/DR |
| replicação típica | síncrona para standby | assíncrona |
| leitura no secundário | não no standby clássico | sim |
| endpoint | mesmo endpoint após failover | endpoint próprio |
| promoção | failover administrado | pode ser promovida; torna-se independente |
| lag | não é usada como reader | pode haver replica lag |

O **Multi-AZ DB cluster** do RDS é outra topologia: writer e duas instâncias
readable em três AZs para motores/Regions compatíveis. Não aplique a frase “o
standby nunca lê” a essa opção; ela vale para o deployment clássico com uma
standby.

### Cenário resolvido 1 — disponibilidade sem leitura extra

Um ERP exige failover automático e usa apenas um endpoint de escrita. A carga de
leitura é pequena. Escolha RDS Multi-AZ DB instance. Uma read replica aumentaria
leitura, mas não substitui a semântica de HA solicitada.

### Cenário resolvido 2 — relatórios pesados

Relatórios degradam o primary e toleram dados alguns segundos atrasados. Crie
read replica e envie consultas read-only ao endpoint dela. Preserve Multi-AZ no
primary se HA também for requisito: as duas decisões podem coexistir.

## 5. Failover e conexão

No failover Multi-AZ, o endpoint permanece, mas seu endereço resolvido muda.
Aplicações devem reconectar, aplicar backoff e evitar cache DNS indefinido. Uma
conexão TCP aberta não migra magicamente.

Falhas de instância, manutenção, indisponibilidade de AZ e reboot com failover
podem iniciar a troca. O tempo depende do workload e recovery; não prometa RTO
fixo sem medir.

## 6. Aurora

Aurora separa compute de um cluster volume distribuído. O writer modifica
dados; Aurora Replicas atendem leitura e podem assumir escrita em failover.
Endpoints ajudam o cliente:

- **cluster/writer endpoint:** escrita e conexão ao writer atual;
- **reader endpoint:** balanceia novas conexões entre readers;
- **instance/custom endpoint:** uso específico, com responsabilidade maior.

Adicionar replicas melhora capacidade de leitura e alvos de failover; o storage
já mantém cópias distribuídas entre três AZs. Aurora Serverless v2 ajusta
capacidade em ACUs dentro do mínimo/máximo configurado; não significa custo zero
nem ausência de instâncias/endpoints.

### Cenário resolvido 3 — carga variável e conexões

Uma API apresenta picos imprevisíveis de compute e milhares de funções Lambda
abrem conexões curtas. Aurora Serverless v2 pode ajustar compute; RDS Proxy reduz
connection churn. São soluções para dimensões distintas e podem ser combinadas.

## 7. Backup e recuperação

- automated backups permitem point-in-time restore dentro da retention;
- snapshot manual permanece até ser excluído;
- restore cria uma **nova** DB instance/cluster e endpoint;
- backups e snapshots não são read replicas;
- copy de snapshot pode atender outra Region/conta, observando KMS e permissões;
- deletion protection evita exclusão acidental, mas não substitui backup;
- backup retention zero (quando permitido) desabilita automated backups;
- restore exige redirecionar/testar aplicação; não sobrescreve o banco atual.

RPO descreve perda de dados aceitável; RTO descreve tempo aceitável de retorno.
Escolha tecnologia e frequência por esses requisitos, não por “ter backup”.

## 8. Segurança

```text
client IAM role/secret
  → SG application
    → SG database: allow DB port only from application SG
      → encrypted RDS/Aurora storage with KMS
```

- encryption at rest cobre storage, logs, backups e snapshots derivados;
- TLS protege trânsito; valide CA e hostname;
- Secrets Manager armazena/rotaciona credenciais em integrações suportadas;
- IAM database authentication gera token temporário em motores compatíveis, mas
  não substitui autorização dentro do banco;
- Enhanced Monitoring, Performance Insights/Database Insights, CloudWatch e
  logs têm finalidades e custos diferentes;
- RDS Custom permite acesso/controle maior para Oracle ou SQL Server suportado,
  aumentando responsabilidade e restrições operacionais.

## 9. RDS Proxy

RDS Proxy mantém pool compartilhado e multiplexa conexões quando possível. É
útil para Lambda, picos, aplicações com connection churn e failover mais suave.
Transações/estado de sessão podem causar **pinning**, reduzindo multiplexação.

Proxy não corrige query lenta, não é read replica e não muda consistência do
banco. Ele precisa de Secrets Manager/IAM, subnets e SG corretos e gera custo.

## 10. ElastiCache

| Requisito | Valkey/Redis OSS | Memcached |
|---|---|---|
| estruturas avançadas, replication, pub/sub, sorted sets | sim | não |
| persistência/failover conforme configuração | sim | cache simples |
| sharding | cluster mode | distribuição no cliente |
| multithread simples | varia por engine/recurso | característica clássica |
| sessão/cache simples descartável | sim | sim |

Padrões:

- **cache-aside/lazy:** aplicação lê cache; no miss, lê DB e preenche;
- **write-through:** atualiza cache junto da escrita; maior consistência
  operacional, mais writes;
- **TTL:** limita staleness e memória, mas expiração simultânea pode causar
  stampede;
- **session store:** permite compute stateless, mas escolha HA e persistência
  coerentes.

Cache introduz invalidação, dados stale, eviction e hot keys. Não o use como
fonte durável sem um desenho específico.

## 11. Portas essenciais

| Serviço | Porta comum |
|---|---:|
| PostgreSQL | 5432 |
| MySQL/Aurora MySQL/MariaDB | 3306 |
| SQL Server | 1433 |
| Oracle | 1521 |
| Valkey/Redis OSS | 6379 |
| Memcached | 11211 |

Porta é um destino, não autenticação. SG deve permitir somente a origem
necessária; banco/cache não deve ser aberto a `0.0.0.0/0`.

## 12. Tabela de decisão

| Palavra decisiva | Escolha inicial |
|---|---|
| automatic failover, same endpoint | Multi-AZ |
| offload reads, eventual lag acceptable | read replica |
| MySQL/PostgreSQL compatible, distributed cluster storage | Aurora |
| bursty connections/Lambda | RDS Proxy |
| sub-millisecond repeated reads | ElastiCache |
| OS/database customization | RDS Custom |
| restore to an exact recent time | PITR |

## 13. Custos e cleanup

Custos incluem instâncias/ACUs, storage, I/O conforme opção, backups além da
franquia, data transfer, Proxy, cache nodes/serverless, monitoring e snapshots
retidos. Multi-AZ e replicas adicionam compute. Parar um RDS suportado é
temporário e storage/backups continuam cobrando.

No laboratório, não criar banco. Se criar por decisão própria: use configuração
elegível confirmada, private, sem Multi-AZ; não carregue dados; exclua ao fim sem
snapshot final somente se a instância for exclusivamente B08; remova snapshots,
proxy, subnet/parameter groups e cache B08 após confirmar ownership.

## 14. Armadilhas

- standby clássico não atende reads;
- read replica assíncrona pode atrasar;
- restore cria endpoint novo;
- reader endpoint distribui conexões, não queries dentro da mesma conexão;
- RDS Proxy não é cache;
- cache miss ainda precisa de fonte durável;
- Multi-AZ não protege contra exclusão lógica sem backup;
- abrir porta no SG não cria usuário/senha válida.

## 15. Checklist e recuperação ativa

- [ ] diferencio três topologias Multi-AZ/read replica;
- [ ] desenho endpoints Aurora;
- [ ] explico restore e PITR;
- [ ] escolho Proxy por conexão, não por query;
- [ ] escolho cache e política de invalidação;
- [ ] associo portas ao serviço sem abrir internet.

Sem consulta, resolva: banco com failover; relatórios; Lambda connection storm;
sessões compartilhadas; recuperação às 14:37; acesso ao SO do Oracle.

## 16. Ligações e referências oficiais

- [LAB B08](../../05_Laboratorios/LAB_B08_Projeto_RDS_Privado_Aurora_Proxy_e_Cache.md)
- [Questões B08](../../04_Questoes_e_Revisoes/Blocos/B08_Questoes.md)
- [Gabarito B08](../../04_Questoes_e_Revisoes/Blocos/B08_Gabarito.md)
- [Checklist B08](../../06_Progresso/B08_Checklist_e_Revisoes.md)
- Próximo: [B09 — Route 53 básico](B09_DNS_Route53_Records_TTL_e_Routing.md)
- [RDS Multi-AZ DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html)
- [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)
- [Aurora high availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html)
- [RDS backup and restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)
- [RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)
- [ElastiCache use cases](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/elasticache-use-cases.html)
