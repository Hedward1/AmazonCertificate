# B08 — Questões: RDS, Aurora, Proxy e ElastiCache

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 5 em português e 5 em inglês<br>
**Formato:** questões single-answer e multi-answer; siga a instrução de cada questão<br>
**Tempo:** 15 minutos<br>
**Gabarito:** [arquivo separado](B08_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B08-01 | 2.2 | RDS Multi-AZ | single | fundamental | básica | Português |
| B08-02 | 3.3 | Read replica | single | fundamental | básica | Português |
| B08-03 | 2.2 | Backup/PITR | multi-2 | fundamental | intermediária | Português |
| B08-04 | 3.3 | RDS Proxy | single | situacional | intermediária | Português |
| B08-05 | 3.3 | ElastiCache | single | situacional | intermediária | Português |
| B08-06 | 2.2 | Aurora endpoints | single | situacional | intermediária | Inglês |
| B08-07 | 1.3 | RDS network security | single | situacional | intermediária | Inglês |
| B08-08 | 3.3 | RDS Custom | multi-3 | integrada | avançada | Inglês |
| B08-09 | 4.3 | Cache invalidation | single | integrada | avançada | Inglês |
| B08-10 | 2.2 | Read replica promotion | single | integrada | avançada | Inglês |

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

Quais ações atendem ao requisito?

**Choose TWO.**

- A. Fazer point-in-time restore para uma nova DB instance no horário desejado.
- B. Fazer failover Multi-AZ para desfazer a exclusão lógica.
- C. Consultar diretamente o standby clássico para obter a versão anterior.
- D. Aumentar o TTL no ElastiCache para reconstruir a tabela.
- E. Validar a instância restaurada e copiar os dados necessários ou redirecionar
  a aplicação de forma controlada, preservando a produção atual até a validação.

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

Which statements should a solutions architect consider?

**Select THREE.**

- A. RDS Custom for Oracle provides access to the underlying operating system
  and database environment for supported customizations.
- B. The customer accepts additional management and security responsibilities
  compared with standard RDS.
- C. Adding a standard RDS read replica exposes operating-system access on the
  replica.
- D. Aurora Serverless v2 is Oracle-compatible and preserves custom Oracle
  software.
- E. RDS Custom monitors the environment through its support perimeter, and
  unsupported changes can place the instance outside that perimeter.
- F. ElastiCache for Memcached can host the Oracle database while preserving
  its custom software.

### B08-09

A Multi-AZ application reads product prices through a cache-aside layer in front
of Amazon RDS. Writes commit successfully to the primary database, but subsequent
requests can continue reading the previous cached value until a long TTL expires.
Read replicas are used for reporting and must not become part of the write path.
After a successful price change, the next request for that product must not
receive the old price; unrelated products must remain cached.

Which design addresses the consistency problem most directly?

- A. Reduce the TTL to 60 seconds and perform no write-triggered invalidation,
  accepting that the old price can still be returned during that interval.
- B. Update the cache before starting the database transaction and leave the new
  cached value in place even if the database write rolls back.
- C. Invalidate or update the affected cache key only after the database write
  succeeds and before acknowledging the change, use a version or ordering guard
  where concurrent writers require one, and retain an appropriate TTL as a
  recovery safeguard.
- D. Flush the entire cache before each database transaction, including keys for
  unrelated products, and repopulate it synchronously.

### B08-10

A company uses an asynchronous cross-Region Amazon RDS read replica as part of a
regional disaster-recovery design. During an outage, the replica is promoted and
the application is redirected through DNS. After the original Region recovers,
the team must avoid assuming that replication direction and application
endpoints repaired themselves.

Which statement correctly describes the promoted database and the required
operational plan?

- A. Promote the replica but leave applications on the original DB endpoint,
  because promotion moves that endpoint to the recovery Region automatically.
- B. It becomes an independent writable DB instance; applications must use its
  endpoint, and the team must design resynchronization and failback explicitly.
- C. Put an RDS Proxy in each Region and assume the proxy automatically rebinds
  across Regions to the promoted independent DB without endpoint changes.
- D. Promote the replica, accept writes, and fail back to the recovered original
  primary immediately without reconciling divergent data or recreating
  replication.

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
