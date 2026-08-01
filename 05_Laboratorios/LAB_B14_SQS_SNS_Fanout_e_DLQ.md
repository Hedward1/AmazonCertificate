# LAB B14 — SQS, SNS fan-out e DLQ

**Timebox:** 45 minutos<br>
**Modo:** console AWS, recursos descartáveis<br>
**Custo esperado:** muito baixo; confira preços e orçamento antes de iniciar<br>
**Objetivo:** observar fan-out, visibility, redelivery, DLQ e cleanup

**Capítulo:** [B14 — SQS, SNS e fan-out](../03_Guia_do_Estudante/Capitulos/B14_SQS_SNS_Desacoplamento_e_Fanout.md)

## 1. Arquitetura e nomes — 3 min

```text
SNS b14-events
  |-> SQS b14-orders -> DLQ b14-orders-dlq
  +-> SQS b14-audit
```

Use a mesma Region para todos os recursos. Não reutilize filas reais.

## 2. Preflight — 5 min

- [ ] Identidade não root confirmada.
- [ ] Region e budget/alerta de cobrança confirmados.
- [ ] Nenhuma informação real será colocada em mensagem.
- [ ] Inventário inicial de topics, queues, subscriptions e alarms registrado.
- [ ] Permissões para criar/excluir SNS/SQS validadas.

```text
Region: __________
Topics iniciais: ____
Queues iniciais: ____
Subscriptions iniciais: ____
```

Se houver limitação de permissão, faça as etapas em diagrama e não relaxe uma
policy corporativa.

## 3. Crie DLQ e filas — 7 min

1. Em SQS, crie Standard queue `b14-orders-dlq`.
2. Crie Standard queue `b14-orders`.
3. Configure visibility timeout em 60 s e receive wait time em 20 s.
4. Configure a redrive policy para `b14-orders-dlq`, `maxReceiveCount=2`.
5. Crie Standard queue `b14-audit` com long polling 20 s.
6. Mantenha encryption padrão e acesso privado.

Registre:

```text
Visibility: ______
Wait time: ______
Retention: ______
maxReceiveCount: ______
```

## 4. Crie tópico e fan-out — 6 min

1. Em SNS, crie Standard topic `b14-events`.
2. Crie subscription SQS para `b14-orders`.
3. Crie subscription SQS para `b14-audit`.
4. Confira queue policies: devem permitir `sqs:SendMessage` do ARN do tópico,
   sem abrir publishers arbitrários.
5. Confirme ambas as subscriptions.

Não use email/SMS: podem gerar entrega externa ou cobrança desnecessária.

## 5. Publique e confirme fan-out — 6 min

Publique no tópico:

```json
{"eventId":"b14-001","orderId":"demo-42","action":"CREATED"}
```

Faça `Poll for messages` nas duas filas. Confirme que **cada fila** recebeu sua
própria cópia. Não delete ainda a mensagem de `b14-orders`.

```text
orders recebeu: sim / não
audit recebeu: sim / não
Mesmo eventId: sim / não
```

## 6. Visibility e redelivery — 6 min

1. Receba a mensagem de `b14-orders` sem deletar.
2. Durante o visibility timeout, outro poll normalmente não deve devolvê-la.
3. Espere o prazo ou altere sua visibility para 0 no console.
4. Receba novamente e registre `ApproximateReceiveCount`.
5. Não delete novamente; após exceder a redrive policy, confirme a DLQ.

O tempo de propagação pode não ser instantâneo. Não publique mensagens extras
para “forçar”. A observação principal é: receive não apaga; delete confirma.

## 7. Idempotência e scaling — 4 min

Em papel, complete:

```text
idempotency key: eventId / orderId / outra: __________
conditional write store: ____________________
efeito que não pode duplicar: ____________________

backlog = 1.000 mensagens
workers = 10
backlog/worker = ______
taxa por worker = 2 msg/s
tempo otimista para drenar = ______ s
```

Escolha `ApproximateAgeOfOldestMessage` e backlog/worker para scaling. Explique
por que CPU sozinha pode ficar baixa enquanto a fila cresce.

## 8. Segurança e custo — 2 min

- [ ] Policy do tópico não permite publish público.
- [ ] Policies das filas limitam o tópico pelo `SourceArn`.
- [ ] Nenhum payload sensível foi usado.
- [ ] Nenhuma customer managed KMS key foi criada.
- [ ] Long polling foi habilitado para reduzir empty receives.

## 9. Cleanup obrigatório — 5 min

Nesta ordem:

1. delete as duas subscriptions;
2. delete o tópico `b14-events`;
3. delete `b14-orders`, `b14-audit` e `b14-orders-dlq`;
4. delete alarms/policies de scaling se criou algum;
5. confirme inventário final contra o inicial.

`PurgeQueue` não substitui `DeleteQueue`; a fila vazia continua existindo.

```text
Subscriptions residuais: zero / investigar
Topics residuais: zero / investigar
Queues residuais: zero / investigar
Alarms residuais: zero / investigar
```

## 10. Validação

- [ ] uma publicação gerou duas cópias independentes;
- [ ] receive e delete foram distinguidos;
- [ ] redelivery e `ApproximateReceiveCount` foram observados;
- [ ] mensagem problemática chegou à DLQ ou fluxo foi explicado;
- [ ] uma chave idempotente foi escolhida;
- [ ] backlog por worker foi calculado;
- [ ] cleanup deixou inventário original.

## Conexão com o exame

Palavras decisivas: *buffer* e *competing consumers* → SQS; *each subscriber
must receive a copy* → SNS + fila por subscriber; *ordered per entity* → FIFO +
message group; *duplicate delivery* → idempotência; *failed repeatedly* → DLQ;
*empty receives* → long polling.

## Referências oficiais

- [Getting started with SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)
- [Visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)
- [Dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
- [SNS fan-out para SQS](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)
