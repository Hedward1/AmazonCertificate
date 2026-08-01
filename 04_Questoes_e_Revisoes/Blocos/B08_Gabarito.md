# B08 — Gabarito comentado

Abra depois das [questões B08](B08_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B08-01 | B | 2.2 |
| B08-02 | C | 3.3 |
| B08-03 | A | 2.2 |
| B08-04 | D | 3.3 |
| B08-05 | B | 3.3 |
| B08-06 | C | 2.2 |
| B08-07 | A | 1.3 |
| B08-08 | D | 3.3 |
| B08-09 | C | 4.3 |
| B08-10 | B | 2.2 |

## B08-01 — Resposta B

- **Requisito central:** failover automático em outra AZ sem leitura extra.
- **Palavras decisivas:** *failover automático*, *mesmo endpoint*, *sem reads*.
- **A:** snapshot oferece recuperação, não failover automático.
- **B:** correta; Multi-AZ clássico mantém standby síncrono para HA.
- **C:** cache não fornece banco relacional autoritativo.
- **D:** read replica é assíncrona e recebe leituras, não todas as escritas.
- **Regra reutilizável:** HA de RDS → Multi-AZ; read scaling → read replica.
- **Aulas:** 87–89.
- **Referência:** [RDS Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html).

## B08-02 — Resposta C

- **Requisito central:** retirar consultas read-only com lag aceitável.
- **Palavras decisivas:** *relatórios*, *read-only*, *atraso tolerado*.
- **A:** retention não oferece endpoint de leitura.
- **B:** standby do Multi-AZ DB instance clássico não serve reads.
- **C:** correta; read replica tem endpoint próprio para leitura.
- **D:** Proxy reutiliza conexões, não replica dados.
- **Regra reutilizável:** leitura escalável e eventual lag aceitável → replica.
- **Aulas:** 88.
- **Referência:** [RDS read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html).

## B08-03 — Resposta A

- **Requisito central:** recuperar estado anterior sem sobrescrever produção.
- **Palavras decisivas:** *14:57*, *backups ativos*, *nova instância*.
- **A:** correta; PITR cria nova DB no ponto selecionado.
- **B:** standby replica a exclusão lógica.
- **C:** standby clássico não é consultável e contém a mudança replicada.
- **D:** cache não restaura tabela do banco.
- **Regra reutilizável:** erro lógico em tempo conhecido → PITR + nova DB.
- **Aulas:** 94.
- **Referência:** [Restoring to a specified time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html).

## B08-04 — Resposta D

- **Requisito central:** controlar uma tempestade de conexões curtas.
- **Palavras decisivas:** *Lambda*, *milhares*, *esgotam conexões*.
- **A:** DNS não faz pooling.
- **B:** snapshots não alteram conexões.
- **C:** afinidade HTTP não reutiliza conexão DB entre funções.
- **D:** correta; RDS Proxy mantém pool e multiplexa quando possível.
- **Regra reutilizável:** connection churn/serverless → RDS Proxy.
- **Aulas:** 96.
- **Referência:** [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html).

## B08-05 — Resposta B

- **Requisito central:** reduzir latência/carga com staleness limitada.
- **Palavras decisivas:** *repetidamente*, *dois minutos*, *reduzir carga*.
- **A:** PITR é recuperação, não serving path.
- **B:** correta; cache-aside com TTL/invalidação atende leituras repetidas.
- **C:** exposição pública não melhora o padrão e reduz segurança.
- **D:** KMS protege chaves, não armazena resultados de query.
- **Regra reutilizável:** leitura repetida e tolerância a stale → cache.
- **Aulas:** 97–99.
- **Referência:** [ElastiCache strategies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html).

## B08-06 — Answer C

- **Requisito central:** route writes and load-balance read connections.
- **Palavras decisivas:** *current writer*, *Aurora Replicas*.
- **A:** instance endpoints bypass role-aware cluster routing.
- **B:** snapshots do not expose SQL endpoints.
- **C:** correct; writer and reader endpoints express the two roles.
- **D:** a proxy without a database target cannot serve queries.
- **Regra reutilizável:** Aurora writes → cluster endpoint; reads → reader.
- **Aulas:** 91–93.
- **Referência:** [Aurora endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoints.html).

## B08-07 — Answer A

- **Requisito central:** diagnose private DB connectivity securely.
- **Palavras decisivas:** *private*, *cannot connect*, *initial check*.
- **A:** correct; validate SG-to-SG port, DNS/routes and credentials.
- **B:** opening to the internet violates least privilege.
- **C:** RDS instances do not receive EIPs this way.
- **D:** encryption at rest does not block network routing.
- **Regra reutilizável:** connection path = DNS + route + SG/NACL + TLS/auth.
- **Aulas:** 95 e 100.
- **Referência:** [RDS VPC security](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html).

## B08-08 — Answer D

- **Requisito central:** supported OS/database customization for Oracle.
- **Palavras decisivas:** *operating-system access*, *standard RDS does not*.
- **A:** Aurora is MySQL/PostgreSQL compatible, not custom Oracle.
- **B:** cache does not host Oracle.
- **C:** replica preserves the same standard-RDS constraints.
- **D:** correct; evaluate RDS Custom and its shared responsibilities.
- **Regra reutilizável:** supported Oracle/SQL Server customization → RDS Custom.
- **Aulas:** 90.
- **Referência:** [RDS Custom](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-custom.html).

## B08-09 — Answer C

- **Requisito central:** prevent stale prices in cache-aside.
- **Palavras decisivas:** *after an update*, *stale*.
- **A:** changing a port does not invalidate data.
- **B:** no expiry makes staleness unbounded.
- **C:** correct; invalidate/update on write and use bounded TTL.
- **D:** replica promotion is unrelated and disruptive.
- **Regra reutilizável:** cache correctness requires explicit invalidation/TTL.
- **Aulas:** 97–99.
- **Referência:** [Caching patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/cache-aside.html).

## B08-10 — Answer B

- **Requisito central:** understand read-replica promotion in DR.
- **Palavras decisivas:** *cross-Region*, *promoted*, *consequence*.
- **A:** promotion ends the read-replica relationship.
- **B:** correct; it becomes independent/writable and endpoints/plans change.
- **C:** promotion does not establish synchronous reversal automatically.
- **D:** promotion is not point-in-time restore.
- **Regra reutilizável:** promote replica → independent DB; plan DNS/failback.
- **Aulas:** 88 e 94.
- **Referência:** [Promoting a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Promote).

## Ação após a correção

Registre no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md) se confundiu HA,
read scaling, restore, connection pooling ou cache. Refaça a tabela de decisão.

Classifique cada erro em uma única causa primária:

- disponibilidade e failover;
- escala de leitura;
- recuperação de dados;
- conectividade e segurança;
- gerenciamento de conexões;
- cache e invalidação;
- custo e operação.

Depois escreva uma frase que elimine o distrator escolhido.

Ao revisar, formule também o requisito inverso. Por exemplo: se o cenário
passasse de “failover sem leitura” para “relatórios com atraso aceitável”, a
resposta mudaria de Multi-AZ clássico para read replica. Essa variação confirma
que você escolheu pelo requisito e não apenas pelo nome do serviço.
