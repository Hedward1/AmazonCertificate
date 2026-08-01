# B19 — Analytics, streaming, ingestão segura e serviços de machine learning

**Data planejada:** 15/08/2026<br>
**Nível:** iniciante absoluto<br>
**Comece pelas aulas da Udemy:** [roteiro B19 — aulas 245–260 e 262–263](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b19); Pule a aula 261: Amazon Personalize está fora do escopo.<br>
**Quizzes:** Q19 e Q20<br>
**Domínios oficiais:** 3 — Design High-Performing Architectures<br>
**Tarefas:** 3.5 principal; 3.3, 4.3 e 1.3 secundárias<br>
**Pré-requisito:** B18 — serverless, bancos e início de analytics

## 1. Objetivos de aprendizagem

1. Montar um pipeline de dados por camadas.
2. Distinguir armazenamento, catálogo, transformação, consulta e visualização.
3. Escolher Athena para SQL ad hoc sobre S3.
4. Escolher Redshift para data warehouse analítico.
5. Explicar Glue Data Catalog, crawler e ETL.
6. Explicar Lake Formation como governança do data lake.
7. Separar batch de streaming.
8. Relacionar MSK e Managed Service for Apache Flink.
9. Reconhecer serviços gerenciados de AI por entrada e saída.
10. Proteger pontos de ingestão com identidade, autorização, criptografia e
    conectividade adequadas ao serviço.
11. Avaliar operação, segurança e custo antes do serviço.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 245–247 | Amazon QuickSuite no guia SAA-C03; Amazon Quick na documentação do produto; Amazon Quick Sight como componente de BI (título original da aula: QuickSight); Glue e Lake Formation: estudar decisões e responsabilidades |
| 248–251 | Flink, MSK e pipeline: desenhar; não provisionar clusters |
| 252–260 | AI/ML: reconhecer entrada, saída e caso de uso |
| 261 | PULAR: Amazon Personalize fora do escopo |
| 262–263 | Textract e resumo: consolidar mapa |
| Q19–Q20 | Fazer depois da recuperação; ignorar eventual item só de Personalize |

Use as aulas para o primeiro mapa, este capítulo para consolidar decisões, o laboratório para praticar e as questões para diagnosticar lacunas.

## 3. Vocabulário essencial

| Termo | Significado no cenário |
|---|---|
| data lake | dados em escala, usualmente no S3 |
| Data Catalog | metadados de localização, esquema e partições |
| crawler | descobre fontes e infere metadados |
| ETL | extrair, transformar e carregar |
| OLAP | consulta analítica |
| columnar format | formato como Parquet que lê colunas necessárias |
| partition | divisão lógica que reduz leitura |
| stream | eventos contínuos |
| stateful processing | processamento que mantém estado |
| inference | uso de modelo para produzir previsão |
| ingestion access point | API, stream, broker ou endpoint que recebe dados de produtores |
| authentication | prova de quem é o chamador |
| authorization | decisão sobre quais ações o chamador pode executar em quais recursos |
| resource policy | política anexada ao recurso que declara principals, ações e condições permitidas |
| VPC endpoint policy | limite adicional para o uso do endpoint; não substitui as permissões IAM ou do recurso |

## 4. Modelo mental

Para cada cenário, siga esta sequência:

1. identifique o requisito principal;
2. marque restrições e superlativos;
3. determine escopo regional, zonal ou global;
4. avalie segurança e resiliência;
5. avalie performance e escala;
6. compare operação e custo;
7. elimine opções que violam uma restrição;
8. escolha serviço e configuração.

## 5. Fundamentos e decisões

### 5.1 Ponto 1

S3 costuma ser a camada durável e desacoplada de um data lake.
### 5.2 Ponto 2

Glue Data Catalog armazena metadados, não os dados do conjunto.
### 5.3 Ponto 3

Glue crawler cria ou atualiza tabelas e partições no catálogo.
### 5.4 Ponto 4

Inferência de esquema não substitui validação de qualidade.
### 5.5 Ponto 5

Glue jobs executam integração e ETL serverless.
### 5.6 Ponto 6

Lake Formation centraliza governança e permissões finas no data lake.
### 5.7 Ponto 7

Lake Formation não é mecanismo SQL.
### 5.8 Ponto 8

Athena executa SQL serverless sobre dados, normalmente no S3.
### 5.9 Ponto 9

Athena cobra principalmente pelos bytes examinados.
### 5.10 Ponto 10

Parquet, compressão e partições reduzem leitura e custo no Athena.
### 5.11 Ponto 11

Redshift é um data warehouse para analytics recorrente e em escala.
### 5.12 Ponto 12

Redshift não é a resposta padrão para consulta ocasional em poucos arquivos.
### 5.13 Ponto 13

O guia oficial SAA-C03 vigente cita **Amazon QuickSuite**. A documentação atual
do produto usa **Amazon Quick**, plataforma que inclui **Amazon Quick Sight**
como componente de business intelligence e visualização; o curso ainda mostra
o nome histórico Amazon QuickSight.
### 5.14 Ponto 14

Amazon Quick Sight não transforma nem cataloga dados por si só.
### 5.15 Ponto 15

Batch processa conjuntos delimitados, geralmente por agenda.
### 5.16 Ponto 16

Streaming processa eventos conforme chegam.
### 5.17 Ponto 17

Managed Service for Apache Flink executa aplicações Flink gerenciadas.
### 5.18 Ponto 18

Flink atende janelas, agregações e processamento stateful contínuo.
### 5.19 Ponto 19

Amazon MSK fornece Apache Kafka gerenciado.
### 5.20 Ponto 20

MSK mantém brokers; a aplicação ainda produz e consome registros.
### 5.21 Ponto 21

MSK pode ser origem para uma aplicação Flink.
### 5.22 Ponto 22

Rekognition analisa imagem e vídeo.
### 5.23 Ponto 23

Transcribe converte áudio em texto; Polly converte texto em voz.
### 5.24 Ponto 24

Translate traduz texto; Comprehend extrai insights de linguagem.
### 5.25 Ponto 25

Lex cria interfaces conversacionais; Connect oferece contact center.
### 5.26 Ponto 26

SageMaker AI cobre construção, treinamento e implantação de modelos próprios.
### 5.27 Ponto 27

Kendra oferece pesquisa empresarial inteligente.
### 5.28 Ponto 28

Textract extrai texto, formulários e tabelas de documentos.
### 5.29 Ponto 29

APIs de AI pré-treinadas reduzem operação quando atendem ao caso.
### 5.30 Ponto 30

Dados sensíveis exigem IAM mínimo, criptografia e governança.

### 5.31 Ponto 31 — Secure access to ingestion access points

O guia oficial inclui literalmente **secure access to ingestion access points**
na tarefa 3.5. Um ponto de ingestão pode ser uma API, um stream, um broker ou um
destino de objetos. Protegê-lo exige responder separadamente a quatro perguntas:

1. **Quem é o produtor?** Prefira roles e credenciais temporárias. Chaves
   estáticas dentro de código, imagem ou task definition não são autenticação
   operacionalmente segura.
2. **O que ele pode gravar?** Conceda apenas as ações de escrita necessárias no
   ARN exato. Separe produtores de consumidores e administradores.
3. **Por onde a chamada passa?** Quando o requisito proíbe internet/NAT, use o
   tipo de endpoint privado suportado pelo serviço e restrinja também sua
   policy e security groups quando aplicável.
4. **Como os dados são protegidos?** TLS protege o trânsito; KMS ou o mecanismo
   de criptografia do destino protege o repouso. Um não substitui o outro.

#### Autenticação, IAM e resource policies

- Uma role de workload fornece credenciais temporárias e identifica o produtor.
- A identity policy da role define ações como `kinesis:PutRecord` e
  `kinesis:PutRecords` no stream específico.
- No acesso cross-account, serviços que aceitam resource policies normalmente
  exigem confiança no recurso e permissão na identidade chamadora. Kinesis Data
  Streams aceita resource policies para compartilhar streams; a policy deve
  nomear o principal e as ações permitidas.
- Uma VPC endpoint policy é outra fronteira. Ela pode limitar principals,
  ações e recursos que atravessam o endpoint, mas não concede sozinha a
  permissão que falta na identity policy ou na resource policy de destino.
- Nem todo serviço oferece os mesmos tipos de policy. Confirme suporte e chaves
  de condição, como `aws:SourceVpce`, na documentação daquele serviço.

#### TLS, KMS e caminho privado

- Kinesis Data Streams exige clientes com TLS 1.2 ou posterior e aceita
  server-side encryption com AWS KMS. Ao usar uma customer managed key, as
  permissões da key policy/IAM também precisam cobrir os produtores e
  consumidores necessários; compartilhamento cross-account requer atenção
  especial à chave.
- Um **interface VPC endpoint para Kinesis**, com private DNS, mantém chamadas
  de recursos da VPC no caminho privado do AWS PrivateLink e elimina a
  dependência de internet gateway ou NAT para esse acesso.
- O endpoint privado reduz exposição de rede, mas não autentica o produtor, não
  substitui IAM e não ativa criptografia em repouso.
- Criptografe também destinos, buffers, logs e dead-letter paths do pipeline.

## 6. Tabela de decisão

| Requisito dominante | Escolha inicial | Motivo |
|---|---|---|
| SQL ad hoc sobre S3 | Athena | serverless e paga por consulta |
| ETL e catálogo | AWS Glue | integração e metadados gerenciados |
| Permissão fina no data lake | Lake Formation | governança central |
| Warehouse recorrente | Redshift | OLAP em escala |
| Dashboard | Amazon Quick Sight, componente de BI do Amazon Quick | visualização de negócio |
| Kafka gerenciado | Amazon MSK | compatibilidade Apache Kafka |
| Stream stateful | Managed Service for Apache Flink | janelas e estado contínuo |
| Áudio para texto | Transcribe | speech-to-text |
| Formulário digitalizado | Textract | estrutura documental |
| Modelo customizado | SageMaker AI | treino e endpoint próprios |

### 6.1 Comparação — segurança do ponto de ingestão

| Ponto de ingestão | Autenticação e autorização | Policy do recurso/endpoint | Caminho privado | Criptografia |
|---|---|---|---|---|
| Kinesis Data Streams | chamadas AWS assinadas por role; conceder somente `PutRecord`/`PutRecords` no stream necessário | resource policy para compartilhamento cross-account; endpoint policy como limite adicional | interface VPC endpoint com AWS PrivateLink | TLS 1.2+ em trânsito; SSE com KMS em repouso e permissões da chave |
| API Gateway private REST API | IAM/SigV4 ou outro authorizer compatível com o caso | API resource policy com `aws:SourceVpc`/`aws:SourceVpce`; endpoint policy primeiro filtra o acesso | interface VPC endpoint; somente REST APIs podem ser private APIs | private REST API usa TLS 1.2; proteger cache, logs, integração e destino conforme o desenho |
| Amazon MSK | escolher IAM, SASL/SCRAM ou mTLS e a autorização compatível; não deixar listener sem autenticação | cluster policy e controles Kafka conforme o modo e o cenário cross-account/multi-VPC | brokers ficam na VPC; multi-VPC private connectivity quando necessário | TLS entre cliente e broker; KMS para dados em repouso |
| Amazon S3 como entrada | SigV4 com role e ações mínimas de objeto | bucket/access point policy e endpoint policy podem restringir principal, VPC ou VPCE | gateway endpoint ou interface endpoint conforme o requisito | HTTPS/TLS em trânsito; SSE-S3 ou SSE-KMS em repouso |

**Regra de prova:** conectividade privada responde **por onde**; autenticação
responde **quem**; autorização responde **o quê**; TLS e KMS respondem **como o
dado é protegido**. Uma camada isolada não cumpre as quatro funções.

## 7. Cenários resolvidos


### Cenário resolvido 1 — Data lake de vendas

- **Contexto:** Arquivos diários chegam ao S3.
- **Requisito:** SQL ocasional, catálogo central e menor operação.
- **Decisão:** Glue Data Catalog e Athena; Lake Formation se houver governança fina.
- **Por quê:** O catálogo descreve dados e Athena consulta sem cluster.
- **Por que não:** Redshift provisionado adicionaria operação sem necessidade recorrente.
- **Trade-off:** Athena depende de layout eficiente para custo e performance.
- **Validação:** Comparar bytes examinados antes e depois de Parquet e partições.
- **Custo/cleanup:** Cobrança de S3, catálogo aplicável e consultas Athena.
- **Variação:** Amazon Quick Sight pode apresentar o resultado.

### Cenário resolvido 2 — Fraude em eventos

- **Contexto:** Eventos Kafka chegam continuamente.
- **Requisito:** Manter estado por cliente em janelas de cinco minutos.
- **Decisão:** MSK para Kafka e Flink para processamento stateful.
- **Por quê:** Cada serviço atende uma camada diferente.
- **Por que não:** Glue batch noturno não atende à latência.
- **Trade-off:** Compatibilidade e controle aumentam custo operacional.
- **Validação:** Testar atraso, checkpoint, retry e destino durável.
- **Custo/cleanup:** Não provisionar no laboratório; clusters e aplicações geram cobrança.
- **Variação:** Sem requisito Kafka, avaliar opções serverless nativas.

### Cenário resolvido 3 — Sinistros digitalizados

- **Contexto:** Formulários contêm campos e tabelas.
- **Requisito:** Extrair estrutura sem treinar modelo.
- **Decisão:** Amazon Textract.
- **Por quê:** É a API específica para documentos estruturados.
- **Por que não:** Rekognition reconhece conteúdo visual, não é a escolha para tabelas.
- **Trade-off:** Serviço pré-treinado limita customização, mas reduz operação.
- **Validação:** Medir acurácia em amostra representativa.
- **Custo/cleanup:** API cobra por páginas e features.
- **Variação:** SageMaker AI cabe se o requisito exigir modelo próprio.

### Cenário resolvido 4 — Ingestão privada cross-account

- **Contexto:** Tasks ECS de uma conta produtora enviam eventos regulados, pelo
  AWS SDK, para um Kinesis Data Stream em uma conta de dados. As tasks ficam em
  subnets privadas sem NAT.
- **Requisito:** Somente a task role pode gravar no stream; o tráfego não pode
  usar internet pública e os registros precisam de criptografia em trânsito e
  em repouso com customer managed key.
- **Decisão:** Conceder `PutRecord`/`PutRecords` no ARN exato à task role; na
  conta de dados, autorizar essa role na resource policy do stream; criar um
  interface VPC endpoint para Kinesis com private DNS e endpoint policy
  restritiva; usar TLS e SSE-KMS com as permissões cross-account da chave.
- **Por quê:** A role autentica, as duas policies estabelecem a autorização
  cross-account, o endpoint define o caminho privado e TLS/KMS cobrem trânsito
  e repouso.
- **Por que não:** Endpoint policy ou security group sem IAM não concede escrita;
  KMS não autentica o produtor; uma identity policy isolada não estabelece a
  confiança cross-account do stream.
- **Trade-off:** Interface endpoints e KMS geram custo; compare com NAT sem
  remover requisitos de segurança.
- **Validação:** Confirmar principal, ações, ARN, condições de endpoint, private
  DNS, key policy e ausência de credenciais estáticas antes de enviar dados.
- **Custo/cleanup:** No laboratório, apenas inspecionar e desenhar. Não criar
  stream, endpoint, role ou chave.
- **Variação:** Na mesma conta, a resource policy do stream pode não ser
  necessária; ainda permanecem IAM mínimo, endpoint, TLS e criptografia.

## 8. Fluxo de projeto

1. Classificar a fonte como batch ou stream.
2. Escolher armazenamento durável.
3. Definir catálogo e esquema.
4. Definir governança e donos.
5. Escolher transformação batch ou contínua.
6. Escolher consulta ad hoc ou warehouse.
7. Escolher visualização apenas após preparar dados.
8. Definir autenticação, IAM/resource policy, endpoint policy, TLS, KMS e caminho
   privado conforme o ponto de ingestão.
9. Definir retenção e lifecycle.
10. Estimar bytes, jobs, capacidade e chamadas de API.
11. Planejar observabilidade e tratamento de falhas.
12. Validar com amostra pequena antes de escalar.

## 9. Custos e cleanup

- Não criar MSK, Redshift, OpenSearch, Flink ou endpoint SageMaker AI.
- Athena cobra pelos dados examinados.
- Glue crawlers e jobs podem cobrar por execução.
- Amazon Quick Sight pode exigir assinatura, capacidade ou usuários pagos.
- APIs de AI cobram por unidade processada.
- Interface VPC endpoints cobram por hora e por dados processados; KMS pode
  cobrar pela chave e por chamadas.
- S3 mantém custo de storage e requests.
- Logs e resultados de consulta também precisam de lifecycle.
- Cleanup deve conferir clusters, aplicações, endpoints, buckets e logs.

Faça inventário antes e depois. Exclua somente recursos criados por você e identificados pelo bloco. Nunca tente zerar a conta removendo recursos preexistentes.

## 10. Armadilhas de prova

- Catálogo não contém os dados.
- Lake Formation não executa SQL.
- Amazon Quick Sight não é data warehouse.
- MSK não escreve consumidores.
- Transcribe e Polly têm direções opostas.
- Textract e Rekognition não são equivalentes.
- SageMaker AI não é resposta universal.
- Streaming não implica obrigatoriamente Kafka.
- Serverless não significa gratuito.
- VPC endpoint privado não concede permissão por si só.
- Endpoint policy não substitui identity policy nem resource policy.
- TLS protege trânsito; KMS/SSE protege repouso.
- No cross-account, valide a confiança do recurso e as permissões da chave.
- Não estudar Amazon Personalize neste bloco.

## 11. Checklist de domínio

- [ ] Consigo explicar os objetivos sem consultar.
- [ ] Reconstruo a tabela de decisão.
- [ ] Resolvo os quatro cenários.
- [ ] Sei proteger um ponto de ingestão em todas as quatro camadas.
- [ ] Sei justificar duas alternativas erradas.
- [ ] Conheço custos residuais.
- [ ] Completei o laboratório.
- [ ] Respondi às dez questões antes do gabarito.
- [ ] Registrei erros e baixa confiança.
- [ ] Agendei D+2 e D+7.

## 12. Recuperação ativa

1. Desenhe pipeline batch de ponta a ponta.
2. Explique por que Parquet reduz custo.
3. Compare crawler, catálogo e job.
4. Compare Athena e Redshift.
5. Compare batch e streaming.
6. Explique relação MSK e Flink.
7. Associe dez serviços AI à entrada e saída.
8. Resolva formulário, áudio, chatbot e busca.
9. Compare IAM, resource policy e endpoint policy em uma ingestão cross-account.
10. Explique por que TLS, KMS e endpoint privado não são controles equivalentes.
11. Liste custos residuais.
12. Explique por que a aula 261 foi pulada.

## 13. Ligações com outros blocos

- A identidade limita quem inicia a operação.
- A rede limita por onde o dado passa.
- A criptografia protege conteúdo e chaves.
- A observabilidade prova comportamento e mudanças.
- Resiliência deve corresponder ao objetivo do negócio.
- Custo deve incluir recursos ociosos e tráfego.
- Operação gerenciada reduz tarefas, mas não remove responsabilidade.
- Os simulados combinam estes conceitos.

## 14. Referências oficiais AWS

- [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)
- [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
- [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html)
- [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)
- [SAA-C03 — tarefa 3.5](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html)
- [Kinesis Data Streams — IAM e resource policies](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html)
- [Kinesis Data Streams — interface VPC endpoints](https://docs.aws.amazon.com/streams/latest/dev/vpc.html)
- [Kinesis Data Streams — proteção de dados](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html)
- [Kinesis Data Streams — segurança de infraestrutura](https://docs.aws.amazon.com/streams/latest/dev/infrastructure-security.html)
- [API Gateway — private REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html)
- [Amazon MSK — criptografia](https://docs.aws.amazon.com/msk/latest/developerguide/msk-working-with-encryption.html)
- [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)
- [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [SAA-C03 — domínio 3 (Amazon QuickSuite)](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html)
- [Amazon Quick e Amazon Quick Sight](https://docs.aws.amazon.com/quick/)

**Referências verificadas em:** 01/08/2026.

## 15. Continue o bloco

- [Laboratório B19](../../05_Laboratorios/LAB_B19_Pipeline_Analytics_e_ML_Read_Only.md)
- [Questões B19](../../04_Questoes_e_Revisoes/Blocos/B19_Questoes.md)
- [Gabarito B19](../../04_Questoes_e_Revisoes/Blocos/B19_Gabarito.md)
- [Checklist e revisões B19](../../06_Progresso/B19_Checklist_e_Revisoes.md)
