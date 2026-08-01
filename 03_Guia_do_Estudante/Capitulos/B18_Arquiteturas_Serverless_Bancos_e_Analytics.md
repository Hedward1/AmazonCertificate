# B18 — Arquiteturas serverless, bancos e analytics

**Data planejada:** 14/08/2026<br>
**Comece pelas aulas:** [roteiro B18 — aulas 226–244](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b18); faça `Q17–Q18`<br>
**Domínios:** 2 — Resilient; 3 — High-Performing; 4 — Cost-Optimized<br>
**Tarefas principais:** 2.1, 3.3, 3.5 e 4.3<br>
**Tarefas secundárias:** 1.3, 2.2 e 3.2<br>
**Pré-requisito:** B17 — API Gateway, Lambda e DynamoDB

## 1. Objetivos de aprendizagem

Ao concluir, você deverá:

1. decompor uma aplicação serverless por requisitos, não por moda;
2. reconhecer fan-out, decoupling, cache e static-content patterns;
3. escolher banco pelo modelo e access pattern;
4. diferenciar OLTP, cache, object store, search e OLAP;
5. comparar RDS, Aurora, DynamoDB, ElastiCache e S3;
6. reconhecer DocumentDB, Neptune, Keyspaces e Timestream;
7. escolher Athena para SQL ad hoc sobre S3;
8. escolher Redshift para data warehouse/OLAP;
9. reconhecer OpenSearch e EMR;
10. prever custos de dados examinados, clusters, cache e replicação.

## 2. Aulas deste bloco

| Aulas | Foco |
|---|---|
| 226–229 | aplicações mobile/web, microservices e distribuição de updates |
| 230–239 | seleção de banco por modelo/acesso |
| 240–241 | Athena e custo por dados examinados |
| 242 | Redshift como warehouse analítico |
| 243 | OpenSearch para busca/log analytics |
| 244 | EMR para frameworks distribuídos |

O bloco abre analytics; Glue, Lake Formation, QuickSight, Flink e MSK ficam no
B19. Não antecipe detalhes, mas já separe ingestão, storage, catalog, query e BI.

**Atualização de disponibilidade:** Amazon Timestream for LiveAnalytics fechou
o acesso para novos clientes em **20 de junho de 2025**. Clientes existentes com
uma conta pagadora ativa que já usa o serviço podem continuar. Para uma conta
nova, avalie **Amazon Timestream for InfluxDB** ou outra solução de séries
temporais compatível com os requisitos. A palavra “Timestream” no curso ainda
ensina o modelo time series, mas não autoriza escolher LiveAnalytics sem validar
a disponibilidade.

## 3. Arquiteturas serverless: componentes e trade-offs

Uma arquitetura serverless típica:

```text
viewer -> CloudFront -> S3 (static)
                   \-> API Gateway -> Lambda -> DynamoDB
                                       |-> SQS -> workers
                                       +-> Step Functions
auth -> Cognito
events -> EventBridge/SNS
```

Benefícios: escala sob demanda, cobrança granular, menor gestão de servidores e
integrações gerenciadas. Trade-offs: quotas, eventual consistency, distributed
tracing, retries/duplicates, lock-in de APIs, cold starts e custo elevado em
cargas contínuas mal modeladas.

### 3.1 Mobile application

- Cognito User Pool autentica;
- API Gateway valida JWT/throttles;
- Lambda executa lógica;
- DynamoDB atende key-value por usuário;
- S3 + presigned URL recebe mídia;
- SNS push/event integration notifica.

Não entregue access keys de IAM user. Se o app precisa acesso AWS direto, use
Cognito Identity Pool com role mínima.

### 3.2 Website serverless

S3 privado + CloudFront/OAC entrega assets; API Gateway/Lambda serve API; banco
purpose-built armazena estado. Route 53/ACM fornecem DNS/certificado. WAF,
logging, backups e budgets fazem parte da solução.

### 3.3 Microservices

Cada serviço deve ter boundary e ownership de dados coerentes. Use API síncrona
quando o caller precisa de resposta imediata; SQS/EventBridge/SNS para reduzir
acoplamento temporal e fan-out. Microservices adicionam contratos, tracing,
idempotência, observabilidade e consistência distribuída; não são automaticamente
mais simples que um monólito modular.

### Cenário resolvido 1 — update de software global

Binários grandes e idênticos são colocados em S3 privado, nomes versionados e
CloudFront/OAC. O backend fornece metadata/authorization. CloudFront reduz carga
e saída da origem; Lambda não deve transmitir cada byte. Para acesso privado,
use signed URL/cookie apropriada e preserve versioning/rollback.

## 4. Escolha banco pelo modelo e access pattern

Perguntas:

1. relacional, key-value, document, graph, wide-column ou time series?
2. transações/joins são essenciais?
3. consultas são conhecidas ou ad hoc?
4. latência, throughput e tamanho?
5. single-Region, replicas ou active-active global?
6. read-heavy, write-heavy ou cacheável?
7. durabilidade, backup, RPO e RTO?
8. compatibilidade de engine/protocolo?
9. capacidade provisionada ou serverless/on-demand?
10. custo ocioso e operação aceitáveis?

## 5. Relacional: RDS e Aurora

Amazon RDS gerencia engines relacionais, backups, patching e deployment. Aurora
é compatível com MySQL/PostgreSQL e separa compute do storage distribuído.

| Requisito | Recurso provável |
|---|---|
| alta disponibilidade na mesma Region | Multi-AZ deployment/cluster |
| escalar leituras | read replicas/readers |
| disaster recovery/read global | cross-Region replica/Aurora Global Database |
| conexões Lambda | RDS Proxy quando apropriado |
| pause/scale variável compatível | Aurora Serverless conforme requisitos |

**Multi-AZ** é principalmente HA/failover; uma standby clássica não é read
scaling. **Read replica** atende leitura e pode ter lag; não substitui failover
síncrono automaticamente. Sempre leia o tipo exato de deployment.

### Cenário resolvido 2 — pedidos com joins

Um ERP exige SQL, foreign keys, joins e transações complexas. Escolha RDS/Aurora,
não DynamoDB apenas pela escala. Para HA, configure Multi-AZ; para relatórios de
leitura, readers/replica. Redshift é OLAP e não o banco transacional do pedido.

## 6. DynamoDB, ElastiCache e S3

### DynamoDB

Key-value/document com latência previsível em escala, access patterns conhecidos,
on-demand/provisioned, Streams, TTL, global tables e conditional writes. Não é
escolha ideal para joins/ad hoc SQL não modelados.

### ElastiCache

Cache in-memory (Valkey/Redis OSS ou Memcached conforme opção) para reduzir
latência/carga: cache-aside, sessions, leaderboard e dados efêmeros. Cache exige
TTL, invalidation, eviction, failover e estratégia de cache miss. Em geral não é
o system of record; o curso não deve fazê-lo parecer backup.

### S3

Object storage para data lake, backups, media, static content e datasets de
analytics. Não fornece transações relacionais nem filesystem block. Combine
Parquet/ORC, compression e partitioning para reduzir Athena scans.

### Cenário resolvido 3 — catálogo e sessões

Produtos têm lookup por ID e tráfego imprevisível: DynamoDB. Assets: S3 +
CloudFront. Sessões sub-millisecond e reconstruíveis: ElastiCache. Uma solução
pode usar três stores porque cada access pattern é diferente; replicar tudo em
um único banco cria compromisso ruim.

## 7. Bancos purpose-built

| Modelo/sinal | Serviço | Atenção |
|---|---|---|
| documentos JSON e compatibilidade MongoDB | Amazon DocumentDB | compatível, não “MongoDB idêntico”; valide features |
| relações altamente conectadas/traversal | Amazon Neptune | fraude, social, recommendation graph |
| Cassandra/wide-column | Amazon Keyspaces | API/compatibilidade Cassandra gerenciada |
| métricas/IoT por timestamp | Amazon Timestream for InfluxDB para novo cliente; LiveAnalytics para cliente elegível | valide engine, operação e disponibilidade |
| cache in-memory | ElastiCache | cache e dados efêmeros; durability depende do design |

Use purpose-built quando o modelo reduz complexidade e melhora performance, não
apenas para aumentar quantidade de serviços. Migração exige testar drivers,
queries e compatibilidade.

### Cenário resolvido 4 — fraude em rede

Detectar caminhos entre contas, devices, IPs e comerciantes requer travessias
de relações com profundidade variável. Neptune é o modelo de graph. DynamoDB
poderia armazenar edges, mas consultas de graph ficariam complexas; DocumentDB
é document, não engine de traversal.

## 8. OLTP versus OLAP

| OLTP | OLAP |
|---|---|
| muitas transações pequenas | scans/agregações grandes |
| baixa latência por operação | throughput de análise |
| estado atual | histórico |
| RDS/Aurora/DynamoDB | Redshift/Athena/EMR conforme necessidade |

Não rode relatórios pesados diretamente no banco OLTP se prejudicam clientes.
Extraia/replica para a plataforma analítica adequada.

## 9. Athena, Redshift, OpenSearch e EMR

### 9.1 Athena

Serverless interactive SQL sobre dados no S3, integrado ao Glue Data Catalog.
Paga principalmente por dados examinados. Reduza custo/performance:

- Parquet/ORC colunar;
- compression;
- partition pruning;
- selecione colunas necessárias;
- workgroups com limites e controle de output.

Athena não carrega dados para um cluster próprio. É excelente para ad hoc e
data lake; queries repetitivas muito intensas podem favorecer outra solução.

### 9.2 Redshift

Data warehouse colunar para analytics estruturado em escala, joins e BI. Use
provisioned ou Serverless conforme padrão. Distribuição/sort, workload
management, Spectrum e materialized views são otimizações posteriores. Redshift
não substitui RDS para pequenas transações OLTP.

### 9.3 OpenSearch

Indexação e pesquisa textual, observabilidade/log analytics e agregações de
search. Normalmente recebe cópia indexada de uma fonte; não é escolha padrão
para integridade transacional relacional. Planeje shards, mappings e storage.

### 9.4 EMR

Executa frameworks distribuídos como Spark, Hadoop e Trino/Presto em clusters,
EKS ou serverless offerings conforme serviço. Escolha quando precisa do
framework, custom code e controle de processamento big data, não apenas uma SQL
ad hoc simples sobre S3.

### Cenário resolvido 5 — três analytics

- analista faz SQL esporádica em Parquet no S3 → Athena;
- BI empresarial faz joins repetidos em warehouse → Redshift;
- data scientist executa Spark customizado em petabytes → EMR;
- usuários pesquisam texto e logs → OpenSearch.

## 10. Tabela de decisão consolidada

| Palavra decisiva | Escolha |
|---|---|
| joins/transações/SQL OLTP | RDS/Aurora |
| key-value em escala | DynamoDB |
| microsecond cache | ElastiCache |
| objeto/data lake | S3 |
| document | DocumentDB |
| graph traversal | Neptune |
| Cassandra | Keyspaces |
| telemetry by time | Timestream for InfluxDB em conta nova; LiveAnalytics apenas se elegível |
| SQL ad hoc em S3 | Athena |
| warehouse/OLAP | Redshift |
| full-text/log search | OpenSearch |
| Spark/Hadoop custom | EMR |

## 11. Custos, segurança e cleanup

- RDS/Aurora/Redshift/OpenSearch/EMR/ElastiCache podem cobrar capacity mesmo
  ociosa; Serverless também tem minimums/consumption conforme configuração.
- DynamoDB cobra requests/capacity, storage, indexes, backups e replication.
- Athena cobra bytes examinados e mantém query results no S3.
- S3 cobra storage, requests, retrieval e transfer.
- NAT/cross-AZ/cross-Region/logs podem dominar custos escondidos.

Encryption, private networking, least privilege, secrets, backups/PITR,
retention e audit são transversais. Cleanup: clusters, snapshots finais, replicas,
tables/backups, caches, workgroups, S3 query results, log groups e roles. O LAB
B18 não provisiona clusters; Athena é opcional com dataset minúsculo.

## 12. Armadilhas e recuperação ativa

- escolha por access pattern, não por “NoSQL escala”.
- Multi-AZ e read replica resolvem problemas diferentes.
- ElastiCache não é backup.
- DocumentDB é compatível com MongoDB, não o mesmo produto.
- Timestream for LiveAnalytics não aceita novos clientes desde 20/06/2025.
- Athena consulta S3; Redshift é warehouse.
- OpenSearch é search; EMR executa frameworks.
- formato colunar e partition pruning reduzem Athena scan.

Recupere a matriz inteira, resolva cinco cenários, explique OLTP/OLAP, desenhe a
aplicação serverless e liste custos/resíduos.

## 13. Ligações

- [Laboratório B18](../../05_Laboratorios/LAB_B18_Arquitetura_Serverless_e_Matriz_de_Bancos.md)
- [Questões B18](../../04_Questoes_e_Revisoes/Blocos/B18_Questoes.md)
- [Gabarito B18](../../04_Questoes_e_Revisoes/Blocos/B18_Gabarito.md)
- [Checklist B18](../../06_Progresso/B18_Checklist_e_Revisoes.md)
- Próximo: B19 — pipeline de analytics e serviços complementares.

## 14. Referências oficiais

- [Choosing an AWS database service](https://docs.aws.amazon.com/databases-on-aws-how-to-choose/)
- [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
- [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [Mudança de disponibilidade do Timestream for LiveAnalytics](https://docs.aws.amazon.com/timestream/latest/developerguide/AmazonTimestreamForLiveAnalytics-availability-change.html)
- [When to use Athena](https://docs.aws.amazon.com/athena/latest/ug/when-should-i-use-ate.html)
- [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)
- [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
- [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)
