# B14 — Questões

**Formato:** questões de resposta única e múltipla, conforme indicado<br>
**Idioma:** 2 em português e 8 em inglês<br>
**Aulas:** 182–190<br>
**Tarefa principal:** SAA-C03 2.1

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma | Formato | Tipo | Dificuldade |
|---|---:|---:|---|---|---|---|---|
| B14-01 | 2 | 2.1 | 183–186 | Português | single | fundamental | básica |
| B14-02 | 2 | 2.1 | 187 | Português | single | fundamental | básica |
| B14-03 | 2 | 2.1 | 183–185 | Inglês | single | situacional | intermediária |
| B14-04 | 2 | 2.1 | 185 | Inglês | multi-2 | situacional | avançada |
| B14-05 | 2 | 2.1 | 186 | Inglês | single | situacional | intermediária |
| B14-06 | 2 | 2.1 | 189–190 | Inglês | single | situacional | intermediária |
| B14-07 | 2 | 2.1 | 190 | Inglês | multi-2 | integrada | avançada |
| B14-08 | 2 | 2.1 | 185 | Inglês | single | integrada | avançada |
| B14-09 | 3 | 3.2 | 188 | Inglês | multi-3 | integrada | avançada |
| B14-10 | 2 | 2.1 | 187 | Inglês | single | integrada | avançada |

Responda antes de abrir o gabarito. Registre a palavra que decidiu sua escolha.
Marque também o requisito que eliminou cada alternativa incorreta.

### B14-01

Um worker processa uma mensagem SQS Standard, grava o resultado e falha antes
de executar `DeleteMessage`. A mensagem reaparece. Como evitar efeito duplicado?

- A. Tornar o processamento idempotente usando uma chave estável do negócio
- B. Reduzir o visibility timeout para zero
- C. Desabilitar a retenção da fila
- D. Trocar long polling por short polling

### B14-02

Eventos da mesma conta bancária precisam ser processados em ordem, mas contas
distintas devem ter paralelismo. Qual configuração atende?

- A. SQS Standard e timestamp no body
- B. Uma FIFO com o mesmo `MessageGroupId` para todas as contas
- C. SNS sem filas e uma subscription por conta
- D. SQS FIFO com `account-id` como `MessageGroupId`

### B14-03

A consumer normally needs 6 minutes to complete a job. The queue visibility
timeout is 30 seconds, causing simultaneous duplicate work. What should change?

- A. Reduce message retention to 30 seconds
- B. Set a suitable visibility timeout or extend it with a heartbeat, and remain idempotent
- C. Enable short polling
- D. Delete the message before processing starts

### B14-04

A payment queue contains occasional malformed messages. Valid messages must keep
flowing, failed payloads must remain available for diagnosis, and operators must
know when failures accumulate. **Choose TWO.**

- A. Set the source queue visibility timeout to zero after every receive
- B. Delete a message on its first failure and publish only an email notification
- C. Configure a dead-letter queue and an appropriate `maxReceiveCount` on the source queue
- D. Set the source queue retention to the maximum and retry every failure indefinitely
- E. Set adequate DLQ retention, alarm on visible DLQ messages, and redrive only after remediation

### B14-05

An application makes many empty `ReceiveMessage` calls while traffic is sparse.
It must reduce empty responses and SQS request cost. What should it use?

- A. Long polling with a nonzero wait time, up to 20 seconds
- B. A shorter message retention period
- C. A FIFO queue with one message group
- D. A CloudFront distribution

### B14-06

Three independent systems must each receive every order event and process at
different rates. They need durable buffers. Which architecture is best?

- A. One SQS queue with all three systems competing for messages
- B. One SNS topic with a separate SQS queue subscription for each system
- C. One FIFO queue with three consumers in the same group
- D. Store events only in an EC2 instance store volume

### B14-07

An SNS topic publishes confidential events to an SQS queue encrypted with a
customer managed KMS key. The queue must reject every other publisher, and SNS
must be able to deliver to the encrypted queue. **Choose TWO.**

- A. Enable CORS on the queue URL for the SNS endpoint
- B. Add an SQS resource policy that allows the SNS service to call `SendMessage` only when `aws:SourceArn` equals the expected topic ARN
- C. Make the queue public and rely on server-side encryption for authorization
- D. Allow the SNS service principal to use the KMS key for the required data-key operations, scoped to the expected service context
- E. Attach an IAM user policy to the queue URL instead of a resource policy

### B14-08

An order worker receives from SQS Standard, charges a payment, writes the order
status, and can crash before acknowledging the message. The design must avoid
lost orders and prevent a redelivery from charging the customer twice. Which
processing sequence best meets both requirements?

- A. Delete immediately after `ReceiveMessage`, then charge and update the order
- B. Set visibility longer than the expected runtime, charge normally, and rely on the timeout alone to prevent a duplicate after a crash
- C. Receive and hide the message, perform the charge through an idempotency key, commit the order, and delete only after success; extend visibility for long work
- D. Switch to SQS FIFO with content-based deduplication but keep the payment API non-idempotent and delete only after charging

### B14-09

An EC2 worker fleet processes variable-duration jobs from SQS. CPU remains low,
but backlog and message age breach the processing SLA. Jobs can be delivered more
than once and some take longer than the initial visibility timeout. Which actions
produce a resilient scaling and processing design? **Select THREE.**

- A. Publish backlog-per-in-service-instance and use it for target tracking
- B. Scale only on average CPU utilization because it is an EC2 fleet
- C. Alarm on `ApproximateAgeOfOldestMessage` to protect the latency SLA
- D. Put every job in one FIFO message group to maximize parallelism
- E. Extend visibility for active long jobs and make processing idempotent
- F. Delete each message immediately after receive to prevent redelivery

### B14-10

A multi-tenant checkout system sends order commands to an SQS FIFO queue. Each
customer's commands must remain ordered, different customers must run in
parallel during sales, and a retried producer request must not create a second
order. Which redesign best balances ordering, throughput, and duplicate safety?

- A. Use the customer ID as `MessageGroupId`, a stable order ID for deduplication, and idempotent consumers
- B. Use a Standard queue and sort completed orders by timestamp after charging
- C. Keep one global message group, enable high-throughput FIFO mode, and raise visibility timeout without changing the grouping key
- D. Provision and operate a separate FIFO queue for every customer, with independent redrive policies and lifecycle automation

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B14-01 |  |  |  |
| B14-02 |  |  |  |
| B14-03 |  |  |  |
| B14-04 |  |  |  |
| B14-05 |  |  |  |
| B14-06 |  |  |  |
| B14-07 |  |  |  |
| B14-08 |  |  |  |
| B14-09 |  |  |  |
| B14-10 |  |  |  |

Só depois do registro abra [B14 — Gabarito](B14_Gabarito.md).
