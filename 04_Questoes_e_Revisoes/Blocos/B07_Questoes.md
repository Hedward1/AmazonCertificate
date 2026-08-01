# B07 — Questões: TLS, ACM e Auto Scaling

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 6 em português e 4 em inglês<br>
**Regra:** selecione uma resposta<br>
**Tempo sugerido:** 15 minutos<br>
**Gabarito:** [arquivo separado](B07_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B07-01 | 3.4 | ACM/TLS | Situacional | Básica | Português |
| B07-02 | 3.4 | TLS no backend | Situacional | Intermediária | Português |
| B07-03 | 2.2 | Deregistration | Situacional | Intermediária | Português |
| B07-04 | 3.2 | Capacidade ASG | Fundamental | Básica | Português |
| B07-05 | 3.2 | Target tracking | Situacional | Básica | Português |
| B07-06 | 3.2 | Scheduled scaling | Situacional | Intermediária | Português |
| B07-07 | 3.2 | Warmup | Fundamental | Intermediária | Inglês |
| B07-08 | 2.2 | Health replacement | Situacional | Intermediária | Inglês |
| B07-09 | 3.2 | Launch template | Situacional | Intermediária | Inglês |
| B07-10 | 4.2 | Stateful scaling | Situacional | Intermediária | Inglês |

## Como resolver

Separe quatro planos: certificado e listener; target e draining; capacidade do
grupo; política que altera a capacidade. Marque se a demanda é imprevisível,
graduada, calendarizada ou previsível por histórico. Não trate warmup, grace
period e deregistration como um único timeout.

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

Qual ajuste é central?

- A. Aumentar o TTL de todos os records do Route 53.
- B. Configurar deregistration delay compatível com a duração das requisições e
  alinhar o shutdown da aplicação.
- C. Criar snapshots EBS a cada minuto.
- D. Alterar a rotação da KMS key.

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

What is expected after the applicable grace period?

- A. The ALB creates a database replica.
- B. ACM renews the instance AMI.
- C. The ASG permanently raises its maximum capacity.
- D. The ASG can mark and replace the unhealthy instance.

### B07-09

What is the safest way to roll out a new AMI to an existing ASG fleet?

- A. Change an unversioned file on one instance.
- B. Reboot all instances because reboot adopts the newest AMI.
- C. Create a new launch template version and perform a controlled instance
  refresh with rollback criteria.
- D. Modify the AMI ID property of each running instance.

### B07-10

An application keeps shopping-cart state only in the memory of each EC2
instance. Why is this problematic for horizontal scaling?

- A. New or replaced instances do not share that state; externalizing required
  session state makes instances disposable.
- B. An ASG always copies RAM between instances.
- C. Stickiness guarantees durable recovery after target failure.
- D. TLS automatically replicates sessions to EBS.

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
