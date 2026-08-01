# B14 — SQS, SNS, desacoplamento e fan-out

**Data planejada:** 10/08/2026<br>
**Comece pelas aulas:** [roteiro B14 — aulas 182–190](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b14); o quiz fica para B15<br>
**Domínio principal:** 2 — Design Resilient Architectures<br>
**Tarefa principal:** 2.1 — Design scalable and loosely coupled architectures<br>
**Tarefas secundárias:** 3.2 e 3.5<br>
**Pré-requisito:** entender producers, consumers, retries e métricas

## 1. Objetivos de aprendizagem

Ao concluir, você deverá:

1. explicar como uma fila reduz acoplamento temporal;
2. diferenciar SQS Standard e FIFO;
3. projetar consumers idempotentes para entrega at-least-once;
4. ajustar visibility timeout ao tempo de processamento;
5. usar long polling para reduzir respostas vazias e custo;
6. mover mensagens venenosas para uma DLQ;
7. escalar workers por backlog, não só por CPU;
8. diferenciar SQS pull e SNS push/pub-sub;
9. aplicar SNS→múltiplas filas SQS para fan-out durável;
10. prever encryption, policies, métricas, custos e cleanup.

## 2. Aulas deste bloco

| Aulas | Decisão a recuperar |
|---|---|
| 182 | síncrono versus assíncrono; fila versus pub/sub |
| 183–184 | SQS Standard, producer, consumer, receive e delete |
| 185 | visibility timeout e redelivery |
| 186 | long polling e custo de requests vazios |
| 187 | FIFO, message group e deduplication |
| 188 | backlog como sinal de Auto Scaling |
| 189 | SNS e múltiplos subscribers |
| 190 | fan-out SNS→SQS |

Atualização útil: a documentação atual permite mensagens SQS de até **1 MiB**.
Não use um número antigo do curso para decidir arquitetura. Para payloads muito
maiores, armazene o objeto no S3 e envie apenas referência e metadados.

## 3. Por que desacoplar

Fluxo síncrono:

```text
cliente -> serviço A -> serviço B
                    falha/lentidão retorna ao cliente
```

Fluxo com buffer:

```text
producer -> SQS -> consumer pool
              |      escala e falha independentemente
              +-> DLQ após tentativas
```

O producer precisa apenas que a fila aceite a mensagem. O consumer pode estar
temporariamente indisponível; a mensagem permanece até processamento ou fim da
retention. Isso absorve picos, mas introduz eventual consistency, atraso e a
necessidade de observar idade/backlog.

Uma fila não corrige automaticamente:

- mensagens duplicadas;
- processamento não idempotente;
- poison pills em retry infinito;
- throughput insuficiente do downstream;
- payload ou retenção inadequados;
- perda causada por o consumer deletar antes de concluir.

## 4. SQS Standard

Standard oferece throughput muito alto, entrega **at least once** e ordenação
best effort. Uma cópia pode chegar mais de uma vez ou fora de ordem. A aplicação
precisa produzir o mesmo resultado ao repetir a operação.

### 4.1 Receive, visibility e delete

```text
ReceiveMessage
  -> mensagem continua na fila, mas invisível
  -> processar
  -> persistir resultado com idempotência
  -> DeleteMessage usando receipt handle
```

Se o consumer não deletar antes do visibility timeout, a mensagem reaparece.
Isso é recuperação, não erro do SQS. O timeout deve superar a duração normal; se
o tempo varia, o consumer pode chamar `ChangeMessageVisibility` como heartbeat.
O limite total de invisibilidade desde o receive continua relevante.

Timeout muito curto causa processamento simultâneo duplicado. Muito longo
atrasa retry após crash. Delete antes de commit pode perder trabalho.

### 4.2 Idempotência

Uma operação idempotente aceita repetição sem duplicar o efeito final. Técnicas:

- chave de idempotência em DynamoDB com conditional write;
- unique constraint em banco relacional;
- estado `processed` ligado a um business ID;
- operações naturalmente idempotentes, como definir valor em vez de somar.

Não confie somente no `MessageId`; retries do producer podem criar mensagens
novas. Use identificador estável do evento de negócio.

### Cenário resolvido 1 — cobrança duplicada

Uma fila Standard entrega duas vezes o evento `charge order-42`. O worker
registra `order-42` condicionalmente antes de chamar a cobrança e retorna o
resultado existente na repetição. A fila absorve picos; a idempotência impede
efeito duplicado. Trocar apenas para FIFO não elimina a necessidade de tratar
retries e efeitos externos.

## 5. Polling, retention, delay e DLQ

**Long polling** usa `WaitTimeSeconds > 0` (máximo 20 s) para consultar todos os
servidores amostrados pelo serviço e aguardar mensagem. Reduz empty responses,
false empties e custo. O timeout HTTP do cliente deve ser maior que o wait time.

Não confunda:

| Configuração | Pergunta que responde |
|---|---|
| delay queue/message timer | quando uma mensagem se torna inicialmente visível? |
| visibility timeout | por quanto tempo some após um receive? |
| retention | por quanto tempo pode permanecer antes de expirar? |
| receive wait time | quanto um receive espera por mensagens? |
| redrive maxReceiveCount | depois de quantas entregas vai à DLQ? |

Uma **DLQ** recebe mensagens que excederam `maxReceiveCount`. Use a mesma classe
de fila (Standard/FIFO), alarmes e retenção suficiente. Investigue, corrija o
consumer e faça redrive controlado. Uma DLQ em fluxo FIFO pode quebrar a ordem;
se a ordem absoluta é mais importante que isolar a mensagem, avalie o efeito.

### Cenário resolvido 2 — tarefa de 8 minutos

O processamento costuma levar oito minutos, mas o visibility timeout é 30 s.
Não aumente `maxReceiveCount` para esconder o sintoma. Configure timeout acima
do tempo esperado ou estenda-o por heartbeat, delete somente após commit e
mantenha idempotência. Use DLQ para falhas persistentes, não para trabalhos que
apenas precisam de mais tempo.

## 6. SQS FIFO

FIFO é escolhida quando o requisito exige ordering e deduplication. O nome
termina em `.fifo`. Conceitos:

- `MessageGroupId`: ordem estrita **dentro do grupo**;
- grupos diferentes podem ser processados em paralelo;
- `MessageDeduplicationId` ou content-based deduplication evita duplicatas de
  envio dentro da janela de deduplicação;
- throughput é configurável e diferente de Standard;
- deduplication do SQS não torna efeitos externos magicamente idempotentes.

Uma única group ID serializa toda a fila e limita paralelismo. Para pedidos,
usar `customer-id` ou `order-id` como group requer decidir qual entidade precisa
de ordem.

### Cenário resolvido 3 — eventos por conta

Transações da mesma conta precisam ordem, mas contas diferentes podem processar
em paralelo. Use FIFO com `account-id` como `MessageGroupId`, deduplication ID
estável e consumer idempotente. Uma Standard com timestamp não garante ordem; um
único group `all` satisfaria ordem global, mas sacrificaria throughput.

## 7. Escalar consumers com backlog

Métricas úteis:

- `ApproximateNumberOfMessagesVisible`: backlog esperando;
- `ApproximateAgeOfOldestMessage`: risco de violar SLA;
- `ApproximateNumberOfMessagesNotVisible`: mensagens in flight;
- DLQ depth: falhas persistentes.

CPU baixa não significa capacidade suficiente. Use **backlog per instance**:

```text
mensagens visíveis / workers em serviço
```

Derive o alvo do SLA e da taxa de processamento. Scale-out cedo; scale-in deve
permitir drenagem e respeitar visibility/instance termination.

## 8. SNS e fan-out

SNS é pub/sub gerenciado e empurra cada publicação aos subscribers compatíveis:
SQS, Lambda, HTTP/S, email, SMS e outros endpoints. Filter policies evitam que
todos recebam tudo. Delivery retries dependem do protocolo; logging e DLQ da
subscription ajudam a diagnosticar falhas.

SQS é pull e cada mensagem normalmente é consumida por um worker lógico. Se
três sistemas independentes precisam da mesma mensagem, uma única fila não é
fan-out: os consumers competem. Use:

```text
publisher -> SNS topic
              |-> SQS billing
              |-> SQS analytics
              +-> SQS audit
```

Cada subscriber tem retenção, retry, scaling e DLQ independentes. A queue policy
deve permitir `sqs:SendMessage` somente do tópico esperado (`aws:SourceArn`).

### Cenário resolvido 4 — três destinos, velocidades diferentes

Billing, analytics e audit precisam de todo evento, mas analytics fica offline
por uma hora. SNS direto para três Lambdas poderia sofrer retries e limites; um
tópico com três filas preserva buffers independentes. Billing não espera
analytics, e cada consumer confirma sua própria cópia.

## 9. Tabela de decisão

| Requisito | Escolha |
|---|---|
| buffer e competing consumers | SQS Standard |
| ordem/dedup por entidade | SQS FIFO com grupos |
| push para vários subscribers | SNS |
| fan-out durável e independente | SNS + uma SQS por consumer |
| entrega de falhas para análise | DLQ + alarm/redrive |
| pico de jobs | SQS + Auto Scaling por backlog |

## 10. Segurança, custo e cleanup

- Use IAM/queue/topic policies mínimas e conditions de `SourceArn`/account.
- Habilite encryption; SSE-SQS simplifica, SSE-KMS adiciona controle/custo.
- Não coloque segredos ou dados sensíveis em nomes, atributos ou logs.
- Use VPC endpoints quando o requisito pede caminho privado.
- Custo depende de requests, payload chunks, KMS, transferência, deliveries e
  recursos consumidores; long polling reduz receives vazios.

Cleanup: purge não é delete. Exclua subscriptions, tópico, filas principal/DLQ,
alarms, scaling policies e log groups. Se uma customer managed KMS key foi criada
exclusivamente para a PoC, confirme dependências, desabilite-a e **agende** a
exclusão dentro da janela permitida pelo KMS; uma key não é apagada imediatamente.
Antes, confirme que não há mensagens de outro exercício e registre ARNs apenas
localmente quando necessário.

## 11. Armadilhas e checklist

- at-least-once → idempotência;
- visibility timeout não é retention;
- long polling não atrasa mensagem existente;
- FIFO ordena por group, não necessariamente a fila inteira;
- SNS sozinho não oferece backlog de fila a todos os protocolos;
- uma fila com três consumers distribui trabalho, não copia para todos;
- DLQ sem alarme vira cemitério silencioso;
- backlog/idade frequentemente são melhores que CPU para scaling.

Pergunte: todos precisam de uma cópia? ordem é global ou por entidade? o
consumer pode repetir? quanto pode atrasar? onde ficam poison messages? como
escala? qual policy autoriza o publisher? o que será excluído?

## 12. Recuperação ativa

1. Desenhe receive → visibility → delete e a rota de crash.
2. Compare Standard e FIFO em cinco critérios.
3. Explique delay, visibility, retention, wait time e redrive.
4. Projete fan-out para três consumidores.
5. Calcule backlog por worker e escolha duas métricas.
6. Liste controles de policy e todos os itens de cleanup.

## 13. Ligações

- [Laboratório B14](../../05_Laboratorios/LAB_B14_SQS_SNS_Fanout_e_DLQ.md)
- [Questões B14](../../04_Questoes_e_Revisoes/Blocos/B14_Questoes.md)
- [Gabarito B14](../../04_Questoes_e_Revisoes/Blocos/B14_Gabarito.md)
- [Checklist B14](../../06_Progresso/B14_Checklist_e_Revisoes.md)
- Próximo: B15 — Kinesis, Firehose, MQ e ECS.

## 14. Referências oficiais

- [SQS visibility timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)
- [SQS long polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html)
- [SQS FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fifo-queues.html)
- [SQS dead-letter queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
- [SNS fan-out para SQS](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)
