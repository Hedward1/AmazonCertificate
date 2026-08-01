# B14 — Gabarito comentado

Abra somente depois das [questões B14](B14_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B14-01 | A | 2.1 |
| B14-02 | D | 2.1 |
| B14-03 | B | 2.1 |
| B14-04 | C | 2.1 |
| B14-05 | A | 2.1 |
| B14-06 | B | 2.1 |
| B14-07 | D | 2.1 |
| B14-08 | C | 2.1 |
| B14-09 | B | 3.2 |
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

## B14-04 — Answer C

- **Central requirement:** isolate repeatedly failing messages for investigation.
- **Decisive words:** *malformed*, *failed many times*, *investigation*.
- **A:** unlimited retries waste capacity and hide the problem.
- **B:** email alone is neither a durable redrive workflow nor the requested isolation.
- **C:** correct; a DLQ, alarm, and controlled redrive create an operable failure path.
- **D:** delete-at-receive can permanently lose recoverable work.
- **Reusable rule:** persistent processing failure → DLQ + alarm + diagnosed redrive.
- **Lessons:** 185.
- **Reference:** [SQS DLQs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).
- **Common trap:** creating a DLQ without monitoring it.

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

## B14-07 — Answer D

- **Central requirement:** restrict an SQS subscription to one SNS topic.
- **Decisive words:** *reject any other topic*, *queue*.
- **A:** CORS applies to browser cross-origin behavior.
- **B:** an S3 policy cannot authorize an SQS queue.
- **C:** encryption does not repair a public send policy.
- **D:** correct; resource policy plus `aws:SourceArn` scopes `SendMessage`.
- **Reusable rule:** service-to-service resource policy → allow action and constrain source.
- **Lessons:** 189–190.
- **Reference:** [Subscribe SQS to SNS](https://docs.aws.amazon.com/sns/latest/dg/subscribe-sqs-queue-to-sns-topic.html).
- **Common trap:** allowing the SNS service principal without a source condition.

## B14-08 — Answer C

- **Central requirement:** identify the SQS acknowledgement lifecycle.
- **Decisive words:** *ReceiveMessage*, *correct*.
- **A:** receive does not permanently remove a message.
- **B:** receive does not move data to SNS.
- **C:** correct; receive hides temporarily and delete acknowledges completion.
- **D:** the application must still design idempotent effects.
- **Reusable rule:** receive → invisible; success → delete; no delete → redelivery.
- **Lessons:** 183–185.
- **Reference:** [Visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html).
- **Common trap:** confusing receipt with acknowledgement.

## B14-09 — Answer B

- **Central requirement:** scale workers by the actual queue workload.
- **Decisive words:** *low CPU*, *age and backlog increase*.
- **A:** bucket size does not represent worker demand.
- **B:** correct; backlog per worker measures capacity and age protects the SLA.
- **C:** IAM user count is unrelated.
- **D:** snapshot count is unrelated.
- **Reusable rule:** asynchronous worker scaling → backlog/capacity and oldest age.
- **Lessons:** 188.
- **Reference:** [SQS backlog per instance](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html).
- **Common trap:** using CPU for an I/O-bound worker pool.

## B14-10 — Answer A

- **Central requirement:** increase parallelism while retaining per-customer order.
- **Decisive words:** *one group*, *order only per customer*.
- **A:** correct; each customer becomes an ordered lane processed alongside other groups.
- **B:** silently moving to Standard violates the ordering requirement.
- **C:** visibility does not create group parallelism.
- **D:** self-subscription is invalid and would create a loop conceptually.
- **Reusable rule:** choose the smallest entity requiring order as message group.
- **Lessons:** 187.
- **Reference:** [FIFO message groups](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html).
- **Common trap:** one group ID for the whole workload.

## Ação após a correção

Registre erro ou baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), incluindo o requisito, a alternativa atraente e a regra correta.
