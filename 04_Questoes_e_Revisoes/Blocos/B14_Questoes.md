# B14 — Questões

**Formato:** 10 questões autorais; uma resposta correta<br>
**Idioma:** 2 em português e 8 em inglês<br>
**Aulas:** 182–190<br>
**Tarefa principal:** SAA-C03 2.1

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma |
|---|---:|---:|---|---|
| B14-01 | 2 | 2.1 | 183–186 | Português |
| B14-02 | 2 | 2.1 | 187 | Português |
| B14-03 | 2 | 2.1 | 183–185 | Inglês |
| B14-04 | 2 | 2.1 | 185 | Inglês |
| B14-05 | 2 | 2.1 | 186 | Inglês |
| B14-06 | 2 | 2.1 | 189–190 | Inglês |
| B14-07 | 2 | 2.1 | 190 | Inglês |
| B14-08 | 2 | 2.1 | 185 | Inglês |
| B14-09 | 3 | 3.2 | 188 | Inglês |
| B14-10 | 2 | 2.1 | 187 | Inglês |

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

A malformed message has failed many times and blocks useful investigation among
normal traffic. What is the best design?

- A. Increase retention indefinitely and ignore it
- B. Publish every failure to an email address only
- C. Configure a DLQ with an appropriate `maxReceiveCount`, alarm, and controlled redrive
- D. Disable all retries by deleting messages at receive time

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

An SNS topic sends to an SQS queue. The queue must reject messages from any
other topic. Which control is required?

- A. A CORS policy on the queue URL
- B. An S3 bucket policy
- C. A public queue policy combined with encryption
- D. An SQS resource policy allowing `SendMessage` with the expected topic `aws:SourceArn`

### B14-08

Which statement about SQS `ReceiveMessage` is correct?

- A. Receiving permanently removes the message immediately
- B. Receiving moves the message to an SNS topic
- C. Receiving makes it temporarily invisible; successful processing must be followed by delete
- D. Receiving automatically makes every business operation idempotent

### B14-09

An EC2 worker fleet has low CPU utilization, but queue age and backlog continue
to increase. Which scaling signal is most aligned with the workload?

- A. S3 bucket size
- B. Backlog per in-service worker and age of the oldest message
- C. Number of IAM users
- D. EBS snapshot count

### B14-10

A FIFO queue uses one `MessageGroupId` for all customers and throughput is lower
than required. Ordering is needed only per customer. What should the team do?

- A. Use a distinct customer ID as the message group to allow parallel groups
- B. Remove all deduplication IDs and switch to Standard silently
- C. Increase the visibility timeout to 12 hours
- D. Subscribe the same queue to itself

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
