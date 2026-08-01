# LAB B15 — Arquitetura de streaming e inspeção ECS

**Timebox:** 40 minutos<br>
**Modo:** diagrama + console/CLI read-only<br>
**Custo esperado:** zero<br>
**Objetivo:** selecionar mensageria/streaming e interpretar uma task definition

**Capítulo:** [B15 — streaming, MQ e ECS](../03_Guia_do_Estudante/Capitulos/B15_Streaming_Amazon_MQ_e_ECS.md)

## 1. Restrições

Não crie Amazon MQ, Kinesis stream, Firehose delivery stream, ECS service,
Fargate task, ALB, NAT Gateway ou cluster EKS. Esses recursos podem cobrar por
hora, capacity ou dados. O objetivo é decisão e leitura, não clique.

## 2. Preflight — 4 min

- [ ] Identidade não root e Region confirmadas.
- [ ] AWS CLI autenticada, se usada.
- [ ] Somente comandos `list`, `describe` e `get` autorizados.
- [ ] Nenhum ARN/account ID será copiado para o material.
- [ ] Inventário inicial registrado.

```powershell
$LabRegion = aws configure get region
aws sts get-caller-identity --query 'Arn' --output text
aws kinesis list-streams --region $LabRegion
aws firehose list-delivery-streams --region $LabRegion
aws mq list-brokers --region $LabRegion
aws ecs list-clusters --region $LabRegion
```

Confirme visualmente a identidade, mas não salve o ARN.

## 3. Matriz de quatro eventos — 8 min

Escolha e justifique:

| Caso | SQS | SNS | KDS | Firehose | MQ | Escolha |
|---|---|---|---|---|---|---|
| jobs, cada um processado por um worker |  |  |  |  |  |  |
| evento para cinco subscribers |  |  |  |  |  |  |
| fraude com replay por consumer |  |  |  |  |  |  |
| logs comprimidos no S3 |  |  |  |  |  |  |
| aplicação JMS sem alteração |  |  |  |  |  |  |

Para KDS, acrescente partition key, retention, capacity mode e tipo de consumer.
Para Firehose, acrescente buffer, formato e destination.

## 4. Hot shard — 4 min

Um stream tem quatro shards. 90% dos records usam partition key `mobile`.

```text
Causa: ______________________________________________
Correção de partition key: __________________________
Ordem que precisa ser preservada: ___________________
Métrica/erro a observar: ____________________________
```

Explique por que adicionar consumer não corrige saturação de escrita.

## 5. Task definition de referência — 8 min

Se a conta tiver task definitions, liste e descreva uma que você reconheça e
tenha autorização para inspecionar:

```powershell
aws ecs list-task-definitions --status ACTIVE --sort DESC --max-items 5 --region $LabRegion
aws ecs describe-task-definition --task-definition NOME_OU_ARN --region $LabRegion `
  --query 'taskDefinition.{family:family,cpu:cpu,memory:memory,networkMode:networkMode,requires:requiresCompatibilities,taskRole:taskRoleArn,executionRole:executionRoleArn,containers:containerDefinitions[*].{name:name,image:image,cpu:cpu,memory:memory,ports:portMappings,logs:logConfiguration.logDriver}}'
```

Não copie ARNs nem private registry credentials. Se não houver definition,
interprete este esqueleto sem registrá-lo:

```json
{
  "family": "b15-demo",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "containerDefinitions": [
    {"name": "api", "image": "repo/image:immutable-tag", "essential": true}
  ]
}
```

## 6. Interpretação — 6 min

Preencha:

| Campo | Decisão arquitetural |
|---|---|
| image/tag ou digest |  |
| task CPU/memory |  |
| container CPU/memory |  |
| task role |  |
| execution role |  |
| `awsvpc`/security group |  |
| ports/ALB target |  |
| log driver/retention |  |
| secrets |  |
| ephemeral/persistent storage |  |

Marque qualquer senha em environment como **anti-pattern**; não a copie.

### 6.1 Aplicação — plano de migração para containers

Considere uma API em uma VM que grava sessões e uploads no disco local, lê
configuração de um arquivo e usa access keys fixas. Sem criar recursos, preencha:

| Etapa | Decisão e evidência de conclusão |
|---|---|
| assessment | processos, portas, dependências, estado, jobs e requisitos de SO/licença |
| estado | destino de sessões, uploads e dados duráveis |
| configuração/segredos | Parameter Store ou Secrets Manager e task role |
| build | Dockerfile/image testada, scan e ECR com versão imutável |
| runtime | ECS/Fargate, ECS on EC2 ou EKS, com justificativa operacional |
| deployment | task definition, service, ALB/health check, logs e scaling |
| cutover | teste, métrica de sucesso, estratégia de tráfego e rollback |

Compare o plano com um rehost por AWS Application Migration Service. Registre
qual requisito justificaria adiar a containerização em vez de forçá-la.

## 7. Service e capacity — 4 min

Desenhe duas opções:

```text
ECS service -> Fargate tasks -> ALB
ECS service -> ECS tasks -> capacity provider -> ASG/EC2
```

Para cada uma, indique quem escala desired tasks, quem fornece capacidade,
onde há custo ocioso e como ocorre health check/rollback.

## 8. Custos e segurança — 3 min

- [ ] KDS retention/enhanced fan-out identificados como custos.
- [ ] Firehose transformation e destination identificados.
- [ ] Broker Amazon MQ por hora identificado.
- [ ] EC2/Fargate, ALB, NAT, logs, ECR e storage identificados.
- [ ] Task role e execution role separados.
- [ ] Nenhum segredo foi exibido ou salvo.

## 9. Cleanup e validação — 3 min

Como o LAB é read-only, inventário final deve ser idêntico ao inicial:

```text
Streams criados: zero / investigar
Delivery streams criados: zero / investigar
Brokers criados: zero / investigar
Tasks/services/clusters criados: zero / investigar
Inventário final igual: sim / não
```

Feche CloudShell/terminal e remova rascunhos que contenham identificadores.

## Resultado esperado

- cinco padrões escolhidos corretamente;
- hot shard diagnosticado;
- task definition interpretada;
- roles e capacity layers diferenciadas;
- zero recursos mutáveis.

## Conexão com o exame

Procure *replay* e *ordered log* para KDS; *deliver to S3 with no consumers* para
Firehose; *JMS/ActiveMQ/RabbitMQ* para Amazon MQ; *no host management* para
Fargate; e *application AWS permissions* para task role.

## Referências oficiais

- [Kinesis concepts](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html)
- [Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
- [ECS task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)
- [ECS task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)
