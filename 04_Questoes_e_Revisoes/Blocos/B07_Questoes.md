# B07 — Questões: TLS, ACM e Auto Scaling

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 6 em português e 4 em inglês<br>
**Formato:** questões single-answer e multi-answer; siga a instrução de cada questão<br>
**Tempo sugerido:** 15 minutos<br>
**Gabarito:** [arquivo separado](B07_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B07-01 | 3.4 | ACM/TLS | single | fundamental | básica | Português |
| B07-02 | 3.4 | TLS no backend | single | fundamental | básica | Português |
| B07-03 | 2.2 | Deregistration | multi-2 | fundamental | intermediária | Português |
| B07-04 | 3.2 | Capacidade ASG | single | situacional | intermediária | Português |
| B07-05 | 3.2 | Target tracking | single | situacional | intermediária | Português |
| B07-06 | 3.2 | Scheduled scaling | single | situacional | intermediária | Português |
| B07-07 | 3.2 | Warmup | single | situacional | intermediária | Inglês |
| B07-08 | 2.2 | Health replacement | multi-2 | integrada | avançada | Inglês |
| B07-09 | 3.2 | Launch template | single | integrada | avançada | Inglês |
| B07-10 | 4.2 | Stateful scaling | single | integrada | avançada | Inglês |

## Questões

### B07-01

Um ALB em `eu-west-1` serve `api.example.com`. Onde deve estar o certificado ACM
usado pelo listener?

- A. Somente em `us-east-1`, pois todo certificado ACM deve ficar lá.
- B. Na mesma Region do ALB e cobrindo o hostname usado pelo cliente.
- C. Dentro do root volume das instâncias.
- D. Em qualquer Region, pois certificados ACM são globais.

### B07-02

Uma norma exige criptografia também entre o ALB e seus targets.

Qual solução atende ao requisito?

- A. Usar listener HTTPS e target group HTTPS, configurando certificados e
  confiança no backend conforme necessário.
- B. Usar somente HTTP interno e descrevê-lo como end-to-end.
- C. Associar um Elastic IP ao EBS.
- D. Desativar os health checks.

### B07-03

Durante scale-in, downloads ativos não devem ser encerrados imediatamente.

Quais ajustes ajudam a concluir os downloads antes da terminação?

**Choose TWO.**

- A. Configurar o deregistration delay do target group de acordo com a duração
  esperada das requisições.
- B. Aumentar o TTL de todos os records do Route 53.
- C. Associar o target group ao Auto Scaling group para que o scale-in
  deregistre o target e aguarde o connection draining antes da terminação.
- D. Criar snapshots EBS a cada minuto.
- E. Alterar a rotação da KMS key.

### B07-04

Um ASG tem `min=2`, `desired=4` e `max=8`. Não há scaling activity em andamento.

Quantas instâncias o grupo busca manter agora?

- A. Duas, porque `min` sempre substitui `desired`.
- B. Oito, porque `max` é a capacidade padrão.
- C. Quatorze, somando os três valores.
- D. Quatro, pois `desired` é o alvo atual dentro dos limites.

### B07-05

A CPU média por instância acompanha bem uma carga imprevisível. A equipe quer
mantê-la próxima de 50%.

Qual política deve ser a primeira escolha?

- A. Target tracking.
- B. Scheduled scaling apenas.
- C. Lifecycle hook.
- D. Termination policy.

### B07-06

Há um pico previsível toda sexta-feira às 18:00, e o boot das instâncias leva
dez minutos.

Qual abordagem atende melhor?

- A. Esperar o health check falhar e então aumentar `max`.
- B. Criar um snapshot no horário do pico.
- C. Executar scheduled scaling antes do pico e combinar com política dinâmica
  para desvios, se necessário.
- D. Habilitar sticky sessions como mecanismo de capacidade.

### B07-07

Why should the default instance warmup approximate the time required for a new
instance to serve representative traffic?

- A. To encrypt the instance AMI.
- B. To keep startup metrics from distorting dynamic scaling and prevent
  premature scale-in.
- C. To reserve an Elastic IP.
- D. To extend the DNS TTL.

### B07-08

An instance is EC2-healthy but its application consistently fails the load
balancer health check. The ASG is configured to use ELB health checks.

Which statements describe the expected behavior?

**Choose TWO.**

- A. The ALB creates a database replica for the unhealthy application.
- B. After the grace period, the ASG can mark the instance unhealthy and
  replace it.
- C. ACM renews the instance AMI before the ASG evaluates health.
- D. The ASG permanently raises its maximum capacity whenever one health check
  fails.
- E. The health check grace period can prevent replacement while a new
  application instance is still bootstrapping.

### B07-09

A regulated web tier runs in an Auto Scaling group across three Availability
Zones behind an Application Load Balancer. A patched AMI must replace the entire
fleet while the service keeps at least 90% healthy capacity. The company needs
an auditable rollout, health-based checkpoints, and automatic rollback if a
CloudWatch alarm enters `ALARM`.

Which deployment design best meets the requirements?

- A. Create a parallel Auto Scaling group from the patched AMI and shift all
  traffic to it at once after checking only EC2 instance status, without staged
  checkpoints or alarm-based rollback.
- B. Set the patched launch-template version as the default but wait for normal
  scaling and failures to replace the existing instances over time.
- C. Create a versioned launch template that references the patched AMI, start a
  controlled instance refresh with the required minimum healthy percentage and
  checkpoints, and configure alarm-based rollback criteria.
- D. Patch files in place across the running fleet and create an AMI from one
  instance afterward, without replacing the fleet from an immutable template.

### B07-10

A shopping application runs in a Multi-AZ Auto Scaling group behind an
Application Load Balancer. Cart state exists only in each instance's memory.
During scale-out, load-balancer deregistration, and instance replacement, users
either reach a different target or lose the cart. The company requires elastic
replacement without making one instance a durable dependency.

Cart contents are business data and must remain recoverable after an instance or
Availability Zone failure. A cache may accelerate reads but cannot be the only
copy of the cart.

Which redesign addresses the root cause?

- A. Persist cart state in a shared durable database such as DynamoDB or Aurora,
  keep EC2 targets disposable, and use ElastiCache only as an optional cache in
  front of the durable system of record.
- B. Enable ALB stickiness and a long deregistration delay so the instance's RAM
  remains the authoritative cart store during scaling and replacement.
- C. Move cart state only to a nonpersistent cache and accept eviction or cache
  loss as the recovery behavior after an Availability Zone failure.
- D. Replicate each session synchronously between pairs of EC2 instances and
  keep the only durable copies on their local root volumes.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B07-01 | | | |
| B07-02 | | | |
| B07-03 | | | |
| B07-04 | | | |
| B07-05 | | | |
| B07-06 | | | |
| B07-07 | | | |
| B07-08 | | | |
| B07-09 | | | |
| B07-10 | | | |
