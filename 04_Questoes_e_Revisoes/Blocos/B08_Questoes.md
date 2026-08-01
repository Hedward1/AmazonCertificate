# B08 — Questões: RDS, Aurora, Proxy e ElastiCache

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 5 em português e 5 em inglês<br>
**Regra:** uma resposta<br>
**Tempo:** 15 minutos<br>
**Gabarito:** [arquivo separado](B08_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B08-01 | 2.2 | RDS Multi-AZ | Situacional | Básica | Português |
| B08-02 | 3.3 | Read replica | Situacional | Básica | Português |
| B08-03 | 2.2 | Backup/PITR | Situacional | Intermediária | Português |
| B08-04 | 3.3 | RDS Proxy | Situacional | Intermediária | Português |
| B08-05 | 3.3 | ElastiCache | Situacional | Intermediária | Português |
| B08-06 | 2.2 | Aurora endpoints | Situacional | Intermediária | Inglês |
| B08-07 | 1.3 | RDS network security | Diagnóstico | Básica | Inglês |
| B08-08 | 3.3 | RDS Custom | Situacional | Intermediária | Inglês |
| B08-09 | 4.3 | Cache invalidation | Situacional | Avançada | Inglês |
| B08-10 | 2.2 | Read replica promotion | Situacional | Intermediária | Inglês |

## Questões

### B08-01

Um banco PostgreSQL precisa de failover automático para outra AZ, mantendo o
mesmo endpoint lógico. Não existe requisito de leitura no secundário.

- A. Criar somente snapshot manual diário.
- B. Usar RDS Multi-AZ DB instance deployment.
- C. Usar ElastiCache Memcached.
- D. Criar uma read replica e enviar todas as escritas a ela.

### B08-02

Relatórios read-only degradam o primary e toleram alguns segundos de atraso.

- A. Aumentar apenas backup retention.
- B. Habilitar Multi-AZ clássico e consultar o standby.
- C. Criar uma read replica e direcionar relatórios ao endpoint dela.
- D. Usar RDS Proxy como réplica de dados.

### B08-03

Às 15:00, uma tabela foi excluída por engano. A retenção de backups automáticos
está ativa e a empresa quer o estado das 14:57 sem sobrescrever produção.

- A. Fazer point-in-time restore para uma nova DB instance e recuperar os dados.
- B. Fazer failover Multi-AZ para desfazer a exclusão.
- C. Consultar o standby clássico diretamente.
- D. Aumentar o TTL no ElastiCache.

### B08-04

Milhares de invocações Lambda abrem conexões curtas e esgotam conexões do RDS.
As queries já estão adequadas.

- A. Criar uma hosted zone pública.
- B. Aumentar apenas a retention de snapshots.
- C. Usar sticky sessions no ALB.
- D. Inserir RDS Proxy para pooling/multiplexação de conexões.

### B08-05

Um catálogo é lido repetidamente e aceita dados com até dois minutos de atraso.
O objetivo é reduzir latência e carga do banco.

- A. Executar PITR a cada leitura.
- B. Usar cache-aside no ElastiCache com TTL e invalidação definidos.
- C. Tornar o banco publicamente acessível.
- D. Usar uma KMS key como cache.

### B08-06

An Aurora application needs to send writes to the current writer and distribute
new read-only connections across Aurora Replicas.

- A. Use each instance endpoint for all operations.
- B. Use an EBS snapshot endpoint.
- C. Use the cluster/writer endpoint for writes and the reader endpoint for
  read-only connections.
- D. Use only the RDS Proxy endpoint without a database target.

### B08-07

An application in private subnets cannot connect to a private RDS database. What
is the best initial network-security check?

- A. Verify that the DB security group allows the engine port from the
  application security group, plus DNS/routes and credentials.
- B. Open the database port to `0.0.0.0/0`.
- C. Add an Elastic IP to the DB subnet group.
- D. Disable encryption at rest.

### B08-08

A legacy Oracle workload requires supported operating-system access and custom
database software configuration that standard RDS does not expose.

- A. Aurora Serverless v2.
- B. ElastiCache for Memcached.
- C. RDS read replica only.
- D. Evaluate RDS Custom for Oracle and accept the added responsibilities.

### B08-09

A cache-aside implementation sometimes returns stale product prices after an
update. Which design addresses the issue most directly?

- A. Increase the database port number.
- B. Never expire cache entries.
- C. Invalidate/update the relevant key on writes and keep an appropriate TTL.
- D. Promote a read replica after every price change.

### B08-10

A cross-Region RDS read replica is promoted during disaster recovery. What is a
key consequence?

- A. It remains a read-only child forever.
- B. It becomes an independent writable DB instance, and applications must use
  the appropriate endpoint/failback plan.
- C. It automatically becomes the old primary through synchronous replication.
- D. Promotion restores deleted rows from any point in time.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B08-01 | | | |
| B08-02 | | | |
| B08-03 | | | |
| B08-04 | | | |
| B08-05 | | | |
| B08-06 | | | |
| B08-07 | | | |
| B08-08 | | | |
| B08-09 | | | |
| B08-10 | | | |
