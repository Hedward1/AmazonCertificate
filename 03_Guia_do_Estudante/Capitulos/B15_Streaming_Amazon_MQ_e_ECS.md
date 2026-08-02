# B15 — Streaming, Amazon MQ e Amazon ECS

**Data planejada:** 11/08/2026<br>
**Comece pelas aulas:** [roteiro B15 — aulas 191–202](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b15); faça o quiz `Q14`<br>
**Domínios:** 2 — Resilient Architectures; 3 — High-Performing Architectures<br>
**Tarefas principais:** 2.1, 3.2 e 3.5<br>
**Pré-requisito:** B14 — SQS/SNS e desacoplamento

## 1. Objetivos de aprendizagem

Ao concluir, você deverá:

1. escolher SQS, SNS, Kinesis Data Streams, Data Firehose ou Amazon MQ;
2. explicar partition key, shard, ordering e retention em Kinesis;
3. distinguir shared throughput de enhanced fan-out;
4. separar stream replayable de delivery stream gerenciado;
5. reconhecer Amazon MQ para protocolos/engines legados;
6. explicar image, container, registry e orchestration;
7. diferenciar cluster, task definition, task e service no ECS;
8. escolher ECS on EC2 ou Fargate;
9. separar task role de task execution role;
10. prever scaling, custo, observabilidade e cleanup.

## 2. Aulas deste bloco

| Aulas | Foco |
|---|---|
| 191 | revisar SNS hands-on e policies |
| 192–193 | Kinesis Data Streams, shards e consumers |
| 194–195 | Amazon Data Firehose, buffers e destinos |
| 196 | matriz SQS/SNS/Kinesis |
| 197 | Amazon MQ e compatibilidade ActiveMQ/RabbitMQ |
| 198 | imagem versus container; Docker como fundamento |
| 199–201 | ECS cluster, task definition, task e service |
| 202 | Service Auto Scaling |

**Nome atual:** o serviço antes chamado *Kinesis Data Firehose* é **Amazon Data
Firehose**. O curso pode manter o nome antigo; as decisões arquiteturais
continuam válidas.

## 3. Kinesis Data Streams (KDS)

KDS é um log de eventos ordenado por shard, com múltiplos consumidores e
retenção que permite replay. Producers usam uma **partition key**; o hash decide
o shard. Todos os registros da mesma key seguem para o mesmo shard e preservam
ordem relativa, desde que o producer também envie de modo coerente.

```text
producers -> partition key -> shards -> consumers
                                 |        |-> analytics
                                 |        |-> fraud
                                 +-------> archive
```

### 3.1 Capacity modes

- **On-demand:** o serviço gerencia shards/capacidade; adequado a tráfego
  imprevisível e início simples, com modelo de preço próprio.
- **Provisioned:** você provisiona shards, monitora hot shards e escala; oferece
  controle para tráfego previsível.

Um shard provisioned possui quotas de leitura/escrita específicas; use a página
atual de quotas em vez de decorar números fora de contexto. O exame costuma
testar a causa de um **hot shard**: partition key pouco distribuída.

### 3.2 Consumers

No modelo shared throughput, consumers compartilham a capacidade de leitura do
shard e fazem polling. **Enhanced fan-out** registra consumers que recebem
throughput dedicado por shard via HTTP/2 e menor latência, com custo adicional.

KDS retém registros por 24 horas por padrão e pode ter retenção ampliada. O
consumer mantém checkpoint; uma falha pode reprocessar registros. Efeitos ainda
devem ser idempotentes.

### Cenário resolvido 1 — fraude e replay

Transações precisam ser lidas por fraude e analytics independentemente; fraude
precisa reler a última hora após implantar uma correção. Use KDS com partition
key que distribua carga e permita a ordem necessária. SQS distribui mensagens
entre consumers e não é um event log para múltiplos replays independentes.

### Cenário resolvido 2 — hot shard

Todos os eventos usam `country=BR` como partition key e um shard satura, embora
outros estejam vazios. Aumentar consumers não corrige o write hot spot. Escolha
uma key de maior cardinalidade, como `customer-id`, ou aplique sufixo/hash quando
a ordem global por país não for requisito. Reavalie capacity mode e shards.

## 4. Amazon Data Firehose

Data Firehose entrega dados continuamente a destinos como S3, Redshift (via S3),
OpenSearch, Splunk e endpoints HTTP compatíveis. É quase serverless do ponto de
vista operacional: aceita records, agrupa por tamanho/intervalo, opcionalmente
transforma com Lambda, comprime, cifra e entrega.

| Aspecto | Kinesis Data Streams | Amazon Data Firehose |
|---|---|---|
| finalidade | stream replayable para consumers | entrega gerenciada a destino |
| consumers customizados | sim | transformação/destino, não log geral de consumers |
| retention/replay | sim | não como API de replay do stream |
| capacity | on-demand ou shards | escala gerenciada |
| latência | baixa | near-real-time, inclui buffering |
| destino S3 | consumer/Firehose | nativo |

Buffer maior melhora eficiência de arquivos e custo downstream, mas aumenta
latência. Para analytics S3/Athena, combine conversão para Parquet e
particionamento apropriado quando o volume justificar.

### Cenário resolvido 3 — logs no S3 sem consumers

Milhares de dispositivos enviam logs; o requisito é comprimir e entregar ao S3
em poucos minutos sem gerenciar shards ou consumer. Escolha Data Firehose. Se a
empresa exigir múltiplas aplicações de leitura com replay em segundos, escolha
KDS, possivelmente com Firehose como um consumidor/destino.

## 5. Tabela de decisão — SQS, SNS, Kinesis, Firehose e Amazon MQ

| Palavra decisiva | Serviço |
|---|---|
| buffer de jobs/competing consumers | SQS |
| push/pub-sub e fan-out | SNS |
| ordered event log, retention e replay | Kinesis Data Streams |
| entrega gerenciada a S3/Redshift/OpenSearch/HTTP | Data Firehose |
| JMS/AMQP/STOMP/MQTT/OpenWire ou RabbitMQ compatibility | Amazon MQ |

Amazon MQ gerencia brokers ActiveMQ ou RabbitMQ. É uma ponte para aplicações
que dependem de protocolos/APIs tradicionais e não podem ser reescritas agora.
Para aplicações cloud-native, SQS/SNS costuma oferecer mais escala e menos
operação. Broker single-instance é mais barato, mas Multi-AZ/active-standby é a
opção de produção resiliente conforme engine e deployment.

### Cenário resolvido 4 — migração JMS

Um sistema Java usa JMS e recursos do ActiveMQ; a empresa quer migrar sem
alterar o cliente nesta fase. Escolha Amazon MQ for ActiveMQ. SQS não oferece a
mesma API/protocolo JMS nativo. O trade-off é administrar capacidade/configuração
do broker e pagar instâncias/storage, inclusive ocioso.

## 6. Containers e imagens

- **image:** pacote imutável com filesystem e metadados;
- **container:** processo isolado iniciado a partir da image;
- **registry:** armazena versões de images, por exemplo ECR;
- **orchestrator:** agenda, reinicia, escala e conecta containers.

Containers compartilham o kernel do host; não são VMs completas. Nunca grave
estado durável apenas no filesystem efêmero do container. Use S3, EFS, EBS ou
banco conforme o padrão.

### 6.1 Migração de uma aplicação para containers

Containerizar não é copiar a VM inteira para uma image. Use este fluxo de
decisão:

1. **Avaliar:** inventarie processos, portas, dependências, jobs, estado local,
   requisitos de sistema operacional, licenças e padrões de tráfego. Se o prazo
   só permite rehost, AWS Application Migration Service pode ser mais adequado
   que uma falsa modernização.
2. **Separar estado e configuração:** mova sessões e dados duráveis para o
   serviço apropriado; entregue configuração por Parameter Store e segredos por
   Secrets Manager, usando task role em vez de access keys estáticas.
3. **Construir e testar:** crie uma image mínima e reproduzível, faça scan,
   publique no ECR e fixe tag imutável ou digest. Registre CPU, memória, portas,
   logs, health check, roles e volumes em uma task definition versionada.
4. **Escolher a plataforma:** ECS/Fargate reduz gestão de hosts; ECS on EC2 dá
   controle da capacidade; EKS é indicado quando Kubernetes é um requisito real,
   não apenas por portabilidade genérica.
5. **Migrar tráfego:** teste fora de produção e use rolling ou blue/green com
   métricas, health checks e rollback. Só desligue o ambiente anterior depois de
   validar estado, integrações, observabilidade e recuperação.

**Quando não escolher containers:** dependências de kernel/licença ou um prazo
de rehost podem tornar EC2/MGN mais seguro no primeiro ciclo. Containers também
não tornam automaticamente uma aplicação stateless ou resiliente.

### Cenário resolvido — monólito stateful para ECS

Uma API em EC2 grava sessão no disco e usa credenciais IAM estáticas. Para
migrá-la com baixo esforço operacional, externalize sessão/dados, use
Parameter Store/Secrets Manager e task role, publique a image versionada no ECR
e implante um ECS service em Fargate atrás do ALB. Faça cutover controlado com
health checks e rollback; simplesmente montar o disco do host em um único
container preservaria o ponto único de falha.

## 7. Modelo do Amazon ECS

```text
cluster
  service (desired count, deployment, load balancer, scaling)
    task -> container(s)
    task -> container(s)
  task definition (versioned blueprint)
```

- **Task definition:** JSON declarativo de images, CPU/memory, ports, roles,
  environment, secrets, logs e volumes.
- **Task:** instanciação em execução de uma revision.
- **Service:** mantém desired count, faz deployment e integra load balancer.
- **Cluster:** agrupamento lógico/capacidade onde tasks executam.

Uma task com vários containers é adequada a componentes que compartilham ciclo
de vida, por exemplo app + sidecar. Não coloque microservices independentes na
mesma task apenas para “economizar”.

## 8. ECS on EC2 versus AWS Fargate

| Decisão | ECS on EC2 | ECS on Fargate |
|---|---|---|
| gestão de host | cliente gerencia capacity/AMI/patch | AWS gerencia infraestrutura |
| cobrança dominante | instâncias/ASG, inclusive capacidade ociosa | vCPU/memory/storage por task |
| controle/recursos do host | maior | restrito ao modelo Fargate |
| workload pequeno/variável | pode deixar ocioso | simples e granular |
| otimização em grande escala estável | Savings Plans/Spot/bin packing | Compute Savings Plans; Fargate Spot para workload tolerante a interrupção |

Fargate é **launch type/capacity provider**, não outro orchestrator. ECS e EKS
podem usar Fargate. Para ECS on EC2, Service Auto Scaling e scaling do cluster
são camadas diferentes: aumentar desired tasks não cria capacidade EC2 por si.

## 9. IAM, rede, logs e scaling

- **Task execution role:** usada pelo agente/runtime para pull da image, logs e
  secrets necessários ao start.
- **Task role:** credenciais entregues ao código da aplicação para acessar AWS.
- **Task ENI/security group:** controla o tráfego em `awsvpc`.
- **CloudWatch Logs:** use driver `awslogs`, retenção e dados não sensíveis.
- **Secrets:** referencie Secrets Manager/Parameter Store; não grave na image.

Service Auto Scaling ajusta desired count por CPU, memória ou métricas custom.
Para HTTP, ALB distribui para tasks e health checks devem representar prontidão.
Deployment com circuit breaker/rollback reduz impacto de image defeituosa.

### Cenário resolvido 5 — permissão da aplicação

Uma task baixa a image e envia logs corretamente, mas o código recebe
`AccessDenied` ao ler um objeto S3. Alterar execution role é o diagnóstico
errado: dê `s3:GetObject` mínimo à **task role**. A execution role atende ações
do runtime, não vira automaticamente credencial do app.

## 10. Custos e cleanup

- KDS cobra capacity mode, shards/throughput, retenção e enhanced fan-out.
- Firehose cobra dados ingeridos/processados e serviços de transformação/destino.
- Amazon MQ cobra broker e storage enquanto executa.
- ECS control plane não é o custo principal; EC2/Fargate, EBS/EFS, ALB, NAT,
  logs, images ECR e transferência continuam cobrando.

Cleanup: apagar Firehose/KDS/MQ de laboratório; parar/delete ECS service antes do
cluster; deregister task definitions se necessário; remover tasks, ALB/target
groups, capacity providers/ASG/EC2, log groups, ECR images/repository, ENIs e
roles criadas. O LAB B15 é read-only/diagrama para evitar esses resíduos.

## 11. Armadilhas e recuperação ativa

- KDS ordena por shard/partition key, não globalmente por padrão.
- Firehose usa buffer; não prometa zero latência.
- SQS não é substituto de stream replayable.
- Amazon MQ é compatibilidade, não a escolha default cloud-native.
- ECS service ≠ task definition; Fargate ≠ ECS.
- execution role ≠ task role.
- escalar tasks sem capacidade EC2 pode deixá-las `PENDING`.

Sem consulta, desenhe a matriz dos cinco serviços, resolva hot shard, explique
task definition/task/service/cluster, compare EC2/Fargate e enumere cleanup.

## 12. Ligações

- [Laboratório B15](../../05_Laboratorios/LAB_B15_Streaming_e_Inspecao_ECS.md)
- [Questões B15](../../04_Questoes_e_Revisoes/Blocos/B15_Questoes.md)
- [Gabarito B15](../../04_Questoes_e_Revisoes/Blocos/B15_Gabarito.md)
- [Checklist B15](../../06_Progresso/B15_Checklist_e_Revisoes.md)
- Próximo: B16 — ECR/EKS/Lambda e edge compute.

## 13. Referências oficiais

- [Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [Kinesis consumers e enhanced fan-out](https://docs.aws.amazon.com/streams/latest/dev/building-consumers.html)
- [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
- [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html)
- [Amazon ECS components](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [Containerizar e migrar aplicações com AWS App2Container](https://docs.aws.amazon.com/prescriptive-guidance/latest/containerize-java-a2c/introduction.html)
- [Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html)
- [Fargate ou Lambda — guia de decisão](https://docs.aws.amazon.com/pdfs/decision-guides/latest/fargate-or-lambda/fargate-or-lambda.pdf)
