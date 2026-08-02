# B17 — Serverless: VPC, DynamoDB, API Gateway, Step Functions e Cognito

**Data planejada:** 13/08/2026<br>
**Comece pelas aulas:** [roteiro B17 — aulas 217–225](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b17); faça `Q16`<br>
**Domínios:** 1 — Secure; 2 — Resilient; 3 — High-Performing<br>
**Tarefas principais:** 1.2, 2.1, 3.2 e 3.3<br>
**Tarefas secundárias:** 4.2 e 4.3<br>
**Pré-requisito:** B16 — Lambda e concurrency

## 1. Objetivos de aprendizagem

Ao concluir, você deverá:

1. decidir quando uma função Lambda precisa entrar em uma VPC;
2. explicar por que public subnet não dá internet pública à função;
3. distinguir RDS events de mudanças em linhas;
4. modelar DynamoDB a partir de access patterns;
5. escolher partition/sort key e evitar hot partitions;
6. comparar on-demand/provisioned, GSI/LSI, Streams e global tables;
7. escolher HTTP, REST ou WebSocket API no API Gateway;
8. usar Step Functions para orchestration com retry/catch;
9. diferenciar Cognito User Pools e Identity Pools;
10. construir e limpar uma mini-API serverless.

## 2. Aulas deste bloco

| Aulas | Foco |
|---|---|
| 217 | Lambda em VPC, subnets, SG, endpoints/NAT |
| 218 | RDS invocando Lambda e event notifications |
| 219–221 | DynamoDB, capacity, indexes, Streams, global tables, DAX |
| 222–223 | API Gateway e hands-on |
| 224 | Step Functions e service integrations |
| 225 | Cognito User/Identity Pools |

## 3. Lambda em VPC

Por padrão, uma função Lambda executa em rede gerenciada pelo serviço e pode
acessar endpoints públicos, mas não recursos privados da sua VPC. Ao configurar
subnets e security groups, o Lambda cria/usa conectividade de rede gerenciada
para alcançar recursos da VPC.

```text
Lambda sem VPC -> internet/endpoints públicos
Lambda na VPC  -> recursos privados conforme routes + SG
                 -> internet somente via NAT/egress apropriado
                 -> serviços AWS via NAT ou VPC endpoints
```

Colocar a função em uma **public subnet não lhe atribui public IP**. Para saída
IPv4 à internet, use private subnets com rota para NAT Gateway/instance na
public subnet, ou evite internet com VPC endpoints. NAT Gateway tem custo/hora
e por dados; uma função que precisa apenas DynamoDB/S3 pode usar gateway
endpoint conforme arquitetura.

Escolha subnets em pelo menos duas AZs e security group mínimo. A execution role
também precisa das permissões de rede gerenciada exigidas para a configuração,
além das APIs que o código usa.

### Cenário resolvido 1 — banco privado e API externa

Uma função acessa RDS privado e uma API pública. Configure a função nas private
subnets, SG permitindo banco no destino e saída por NAT para a API, ou use um
serviço privado/endpoint se disponível. Public subnet não elimina NAT. Considere
RDS Proxy para pooling e controle a concurrency para não esgotar conexões.

## 4. RDS, Lambda e eventos

Não confunda três fluxos:

- mecanismos/integrações específicos de engines podem invocar Lambda;
- **RDS event subscriptions** notificam eventos operacionais (failover, backup,
  manutenção) normalmente via SNS/EventBridge, não cada alteração de linha;
- para change data capture de tabelas, use recursos do engine/DMS/streaming
  apropriado, não RDS event notification.

Permissões têm duas direções: a origem precisa autorização para invocar a função
e a função precisa role para acessar serviços. Network reachability continua
separada de IAM.

## 5. DynamoDB: modele access patterns primeiro

DynamoDB é key-value/document, serverless e distribuído. Não comece convertendo
as tabelas relacionais uma a uma. Liste consultas e escolha chaves:

- **partition key (PK):** hash distribui items entre partitions;
- **sort key (SK):** ordena items da mesma PK e permite range/prefix queries;
- primary key pode ser simples (PK) ou composta (PK + SK);
- `Query` exige PK e é eficiente; `Scan` lê muitos items e deve ser exceção.

Exemplo single-table:

```text
PK=CUSTOMER#42  SK=PROFILE
PK=CUSTOMER#42  SK=ORDER#2026-08-13#9001
PK=CUSTOMER#42  SK=ORDER#2026-08-13#9002
```

Consultas por cliente ficam juntas e ordenadas. Uma PK constante (`ALL`) cria
hot partition; distribua tráfego por uma dimensão de alta cardinalidade.

### 5.1 Capacity e consistency

| Escolha | Quando |
|---|---|
| on-demand | tráfego imprevisível, início simples, pay per request |
| provisioned + auto scaling | tráfego previsível, otimização de custo/capacity |
| eventually consistent read | padrão e menor consumo; aceita propagação |
| strongly consistent read | leitura base precisa do valor mais recente |
| transaction | atomicidade ACID entre múltiplos items |
| conditional write | idempotência/concorrência otimista |

Strong consistency não está disponível em todo tipo de leitura/replicação, por
exemplo GSI e global table cross-Region têm características próprias.

### 5.2 Índices

- **GSI:** partition/sort key diferentes; pode ser criado/removido depois;
  capacity própria conforme modo; leitura eventualmente consistente.
- **LSI:** mesma partition key e sort key alternativa; definido na criação;
  compartilha constraints/capacity da tabela e tem limite de collection.

Indexes duplicam attributes projetados e custam storage/write. Não crie um GSI
para cada campo; comece pelos access patterns.

### 5.3 Recursos avançados

- DynamoDB Streams: sequência de mudanças para Lambda/consumers, retenção
  limitada; consumers idempotentes.
- TTL: exclusão assíncrona de items expirados, não scheduler exato.
- PITR/on-demand backup: recuperação, não consulta.
- Global tables: active-active multi-Region e replicação; resolva conflitos.
- DAX: cache in-memory compatível para leituras eventualmente consistentes;
  não acelera writes nem substitui modelagem.

### Cenário resolvido 2 — carrinho global

Um carrinho precisa latência baixa, escala imprevisível e operações por
`customer-id`; outra Region deve aceitar writes. Use DynamoDB on-demand com PK
de alta cardinalidade e global tables se os requisitos de multi-Region/RPO
justificarem. Modele conflito; DAX não cria active-active e RDS read replica não
aceita o mesmo padrão de write global.

## 6. API Gateway

| API | Escolha dominante |
|---|---|
| HTTP API | APIs HTTP simples, baixa latência/custo, recursos suficientes |
| REST API | recursos avançados: usage plans/API keys, caching, request validation/transformation conforme necessidade |
| WebSocket API | conexão bidirecional stateful do protocolo WebSocket |

API Gateway fornece routes/methods, stages, deployments, throttling, quotas,
authorization, logging e integrações. **API key/usage plan não é autenticação**;
serve a medição/throttling de clientes. Para auth, use IAM, Cognito/JWT ou Lambda
authorizer conforme o tipo.

Lambda proxy integration passa request ao handler e espera resposta no formato
compatível. Proteja backend com throttling e concurrency; valide payload;
habilite logs sem secrets; configure CORS apenas para browsers autorizados.

### Cenário resolvido 3 — API CRUD simples

Uma API pública de baixo custo precisa routes CRUD, JWT e Lambda, sem caching ou
usage plan. Escolha HTTP API. Se o requisito pedir API keys/usage plans, caching
gerenciado ou certos recursos REST avançados, escolha REST API. WebSocket só é
necessário para comunicação bidirecional persistente.

### Cápsula de decisão — AWS AppSync

- **Problema resolvido:** expor uma API GraphQL serverless que reúne uma ou mais
  fontes de dados e entrega atualizações em tempo real a clientes web/mobile.
- **Relação SAA-C03:** tarefas 2.1 e 3.2 — arquitetura desacoplada e compute/API
  escalável sem administrar servidores.
- **Quando escolher:** clientes precisam selecionar exatamente os campos, o
  schema GraphQL é parte do contrato, resolvers acessam fontes como DynamoDB ou
  Lambda e subscriptions/PubSub evitam operar WebSockets.
- **Quando não escolher:** uma API HTTP/REST simples já atende, o cliente exige
  semântica REST/usage plans específicos, ou só é necessário buffer assíncrono.
- **Serviço semelhante:** API Gateway; ele é a escolha natural para APIs
  HTTP/REST/WebSocket, enquanto AppSync é orientado a GraphQL e Pub/Sub.
- **Armadilha:** AppSync não é banco de dados nem autenticação automática;
  schema, resolvers, autorização por campo/fonte e custos de requests, mensagens
  e cache continuam sendo decisões explícitas.
- **Questão situacional extra (fora do banco de 250):** um app mobile consulta DynamoDB e Lambda por um
  único schema e precisa receber atualizações em tempo real sem manter servidores
  WebSocket. **Resposta curta:** AppSync com GraphQL, resolvers e subscriptions;
  escolha a autorização apropriada.
- **Referência oficial:** [What is AWS AppSync?](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html)

## 7. Step Functions

Step Functions orquestra workflows como state machines. States incluem Task,
Choice, Wait, Parallel, Map, Pass, Succeed e Fail. Service integrations reduzem
código de cola. `Retry` trata falhas transitórias com backoff; `Catch` direciona
falhas tratadas; execution history facilita auditoria.

| Workflow | Característica |
|---|---|
| Standard | exatamente uma execução do workflow, longa duração e histórico durável |
| Express | alto volume/curta duração, modelo de entrega/cobrança próprio |

Use Step Functions para dependências e estado explícitos. Use SQS para buffer de
jobs independentes. Lambda chamando Lambda em cadeia cria acoplamento, retries
difíceis e desperdício de tempo cobrado.

### Cenário resolvido 4 — pedido com compensação

Validar pedido → cobrar → reservar estoque → notificar, com retry de falhas
transitórias e compensação da cobrança, é um workflow Step Functions. Um único
Uma Lambda Function padrão única, limitada a 15 minutos, teria estado/erros
opacos; SNS não expressa sequência e compensação.

## 8. Cognito

- **User Pool:** diretório e autenticação de usuários; sign-up/sign-in, MFA,
  federation e tokens OIDC/JWT. Pode autorizar API Gateway.
- **Identity Pool:** troca identidade autenticada/não autenticada por
  credenciais AWS temporárias associadas a IAM roles.

Um app pode usar ambos: User Pool autentica e emite token; Identity Pool troca o
token por credenciais temporárias para acesso AWS direto. Não entregue IAM user
access keys ao mobile app.

## 9. Tabela de decisão serverless

| Requisito | Serviço/controle |
|---|---|
| banco privado | Lambda em VPC + SG/routes; RDS Proxy se necessário |
| key-value por access pattern | DynamoDB |
| evento de mudança de item | DynamoDB Streams |
| endpoint HTTP gerenciado | API Gateway HTTP/REST |
| GraphQL com múltiplas fontes/real-time | AWS AppSync |
| workflow com retry/branch | Step Functions |
| autenticar usuários | Cognito User Pool |
| credenciais AWS temporárias | Cognito Identity Pool |

## 10. Custos, segurança e cleanup

Custos: NAT hourly/data, Lambda requests/duration/concurrency, DynamoDB
reads/writes/storage/backups/global replication, API requests/cache/logs, Step
Functions transitions/duration, Cognito MAU e CloudWatch logs.

Segurança: least privilege, private subnets/SG, encryption, authorizer, input
validation, throttling, WAF quando aplicável, secrets fora do código, backups e
logs saneados.

Cleanup da mini-API: delete API routes/stages/API, function/event permission,
table/backups, log groups e role exclusiva. Confirmar ENIs, NAT e endpoints — o
LAB não cria os três últimos.

## 11. Armadilhas e recuperação ativa

- Lambda em public subnet não recebe public IP.
- RDS event notification não é row-level CDC.
- DynamoDB Scan não substitui key design.
- GSI e LSI não são intercambiáveis.
- API key não autentica usuário.
- Step Functions orquestra; SQS faz buffering.
- User Pool autentica; Identity Pool fornece AWS credentials.

Recupere sem consulta: caminho Lambda VPC; tabela DynamoDB; três API types;
workflow com Retry/Catch; Cognito; custo e cleanup.

## 12. Ligações

- [Laboratório B17](../../05_Laboratorios/LAB_B17_API_Serverless_Lambda_DynamoDB.md)
- [Questões B17](../../04_Questoes_e_Revisoes/Blocos/B17_Questoes.md)
- [Gabarito B17](../../04_Questoes_e_Revisoes/Blocos/B17_Gabarito.md)
- [Checklist B17](../../06_Progresso/B17_Checklist_e_Revisoes.md)
- Próximo: B18 — arquiteturas serverless, bancos e analytics.

## 13. Referências oficiais

- [Lambda com VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)
- [DynamoDB core components](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)
- [DynamoDB read consistency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html)
- [Escolher API Gateway HTTP, REST ou WebSocket](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html)
- [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html)
- [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
