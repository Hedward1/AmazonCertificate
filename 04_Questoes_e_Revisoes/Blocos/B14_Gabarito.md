# B14 — Gabarito comentado

Abra somente depois das [questões B14](B14_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B14-01 | A | 2.1 |
| B14-02 | D | 2.1 |
| B14-03 | B | 2.1 |
| B14-04 | C,E | 2.1 |
| B14-05 | A | 2.1 |
| B14-06 | B | 2.1 |
| B14-07 | B,D | 2.1 |
| B14-08 | C | 2.1 |
| B14-09 | A,C,E | 3.2 |
| B14-10 | A | 2.1 |

## B14-01 — Resposta A

- **Requisito central:** impedir que redelivery repita o efeito de negócio.
- **Palavras decisivas:** *falha antes de DeleteMessage*, *reaparece*, *duplicado*.
- **A:** correta; a chave estável permite detectar e reaproveitar o resultado anterior.
- **B:** timeout zero aumenta redelivery e não protege o efeito.
- **C:** retention não controla duplicação de processing.
- **D:** polling muda a forma de receber, não a idempotência.
- **Regra reutilizável:** SQS Standard é at-least-once → consumer idempotente.
- **Aulas:** 183–185.
- **Referência:** [SQS Standard](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html).
- **Erro comum:** deletar antes de persistir o resultado.

## B14-02 — Resposta D

- **Requisito central:** ordenar por conta mantendo paralelismo entre contas.
- **Palavras decisivas:** *mesma conta em ordem*, *contas distintas paralelas*.
- **A:** Standard não garante ordenação estrita.
- **B:** um grupo global serializa todas as contas.
- **C:** SNS não implementa sozinho a fila ordenada pedida.
- **D:** correta; FIFO ordena dentro de cada `MessageGroupId` e paraleliza grupos.
- **Regra reutilizável:** ordem por entidade → FIFO com a entidade como group ID.
- **Aulas:** 187.
- **Referência:** [SQS FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html).
- **Erro comum:** interpretar FIFO como paralelismo ilimitado dentro de um grupo.

## B14-03 — Answer B

- **Central requirement:** prevent premature redelivery of a six-minute job.
- **Decisive words:** *6 minutes*, *30 seconds*, *simultaneous duplicate work*.
- **A:** retention controls total queue lifetime, not in-flight processing time.
- **B:** correct; size or extend visibility and keep the operation idempotent.
- **C:** short polling does not change visibility.
- **D:** deleting first can lose the job after a worker failure.
- **Reusable rule:** visibility must cover processing, with heartbeat for variable work.
- **Lessons:** 185.
- **Reference:** [Visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html).
- **Common trap:** solving a timeout problem by raising retry count.

## B14-04 — Answer C,E

- **Central requirement:** isolate poison messages without losing evidence and make failures operationally visible.
- **Decisive words:** *valid messages keep flowing*, *available for diagnosis*, *operators know*.
- **A:** incorrect; zero visibility causes immediate concurrent redelivery.
- **B:** incorrect; deleting on first failure loses the durable diagnostic payload.
- **C:** correct; the source redrive policy moves repeatedly failing messages after the chosen receive threshold.
- **D:** incorrect; indefinite retries consume capacity and never isolate poison messages.
- **E:** correct; sufficient DLQ retention, an alarm, and controlled redrive provide evidence and an operable recovery path.
- **Reusable rule:** poison-message handling requires isolation plus monitoring and diagnosed redrive; a DLQ alone is incomplete.
- **Lessons:** 185.
- **Reference:** [Amazon SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).

## B14-05 — Answer A

- **Central requirement:** reduce empty receive calls and request cost.
- **Decisive words:** *sparse*, *empty responses*, *request cost*.
- **A:** correct; long polling waits up to 20 seconds and reduces false/empty responses.
- **B:** retention changes expiry of stored messages.
- **C:** FIFO is an ordering decision, not an empty-poll optimization.
- **D:** CloudFront is unrelated to SQS receives.
- **Reusable rule:** sparse queue + empty receives → long polling.
- **Lessons:** 186.
- **Reference:** [Long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html).
- **Common trap:** setting the HTTP client timeout shorter than the wait time.

## B14-06 — Answer B

- **Central requirement:** give every independent consumer a durable copy.
- **Decisive words:** *each receive every event*, *different rates*, *durable*.
- **A:** consumers on one queue compete; each event normally goes to one path.
- **B:** correct; SNS fans out to independent SQS buffers.
- **C:** a single FIFO queue still distributes messages among consumers.
- **D:** instance store is ephemeral and not a messaging system.
- **Reusable rule:** durable fan-out → SNS topic + one SQS queue per consumer.
- **Lessons:** 189–190.
- **Reference:** [SNS to SQS fan-out](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html).
- **Common trap:** expecting three workers on one queue to receive three copies.

## B14-07 — Answer B,D

- **Central requirement:** authorize only one SNS topic and permit delivery to a KMS-encrypted SQS queue.
- **Decisive words:** *reject every other publisher*, *customer managed KMS key*, *SNS deliver*.
- **A:** incorrect; CORS controls browser behavior, not service-to-service authorization.
- **B:** correct; the queue policy grants `SendMessage` to SNS and `aws:SourceArn` binds the grant to the expected topic.
- **C:** incorrect; encryption does not compensate for public write authorization.
- **D:** correct; the customer managed key policy must permit the SNS service to perform the data-key operations required for encrypted delivery.
- **E:** incorrect; a queue resource policy, not an IAM user attached to a URL, controls the SNS service principal.
- **Reusable rule:** encrypted SNS-to-SQS delivery needs both destination authorization and usable KMS key permissions.
- **Lessons:** 189–190.
- **Reference:** [Fanout to encrypted SQS queues](https://docs.aws.amazon.com/sns/latest/dg/sns-enable-encryption-for-topic-sqs-queue-subscriptions.html).

## B14-08 — Answer C

- **Central requirement:** preserve at-least-once delivery without repeating the external payment effect.
- **Decisive words:** *crash before acknowledging*, *avoid lost orders*, *not charge twice*.
- **A:** deleting before the durable business commit can lose the order if processing fails afterward.
- **B:** adequate visibility reduces premature parallel work but cannot cover the crash window after a successful charge; timeout alone is not idempotency.
- **C:** correct; visibility protects in-flight work, an idempotency key protects the charge, and delete acknowledges only a completed transaction.
- **D:** FIFO producer deduplication helps repeated sends, but a consumer can still be redelivered after charging and before delete; the payment effect remains unsafe.
- **Reusable rule:** for at-least-once messaging, combine delete-after-commit, adequate visibility, and idempotent business effects.
- **Lessons:** 183–185.
- **Reference:** [Visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html).
- **Common trap:** treating queue acknowledgement as a distributed transaction with the payment system.

## B14-09 — Answer A,C,E

- **Central requirement:** scale on queue pressure, protect message-age SLA, and make long at-least-once processing safe.
- **Decisive words:** *CPU remains low*, *backlog and age*, *more than once*, *longer than visibility*.
- **A:** correct; backlog per in-service worker expresses the capacity each worker must absorb.
- **B:** incorrect; CPU is poorly correlated with this I/O-bound queue workload.
- **C:** correct; oldest-message age exposes latency/SLA risk that backlog alone can hide.
- **D:** incorrect; one FIFO group serializes the workload and limits parallelism.
- **E:** correct; visibility extension prevents premature parallel work, while idempotency protects against unavoidable redelivery.
- **F:** incorrect; delete-before-success can permanently lose work after a worker failure.
- **Reusable rule:** asynchronous scaling uses backlog/capacity and age; delivery correctness still needs visibility management and idempotency.
- **Lessons:** 183–188.
- **Reference:** [Scaling based on Amazon SQS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html).

## B14-10 — Answer A

- **Central requirement:** preserve per-customer order, scale across customers, and suppress retried producer commands.
- **Decisive words:** *per customer*, *parallel*, *retried producer*, *second order*.
- **A:** correct; customer-scoped groups create parallel ordered lanes, while stable deduplication and consumer idempotency protect the business effect.
- **B:** post-processing sort cannot undo out-of-order or duplicated payment execution on a Standard queue.
- **C:** high-throughput FIFO improves supported throughput dimensions but cannot create parallel processing inside one ordered message group.
- **D:** per-customer queues can isolate/order work, but dynamic queue, policy, monitoring, quota, and cleanup management is unnecessary compared with message groups.
- **Reusable rule:** partition FIFO ordering by the smallest required business key and retain end-to-end idempotency.
- **Lessons:** 187.
- **Reference:** [FIFO message groups](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html).
- **Common trap:** one group ID for the whole workload.

## Ação após a correção

Registre erro ou baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), incluindo o requisito, a alternativa atraente e a regra correta.
