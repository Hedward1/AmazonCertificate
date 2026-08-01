# B19 — Questões: Analytics, streaming, ingestão segura e AI/ML

**Quantidade:** 10 questões autorais<br>
**Idioma:** 2 em português e 8 em inglês<br>
**Regra:** selecione a quantidade indicada em cada questão<br>
**Tempo sugerido:** 18 minutos; registre confiança antes de corrigir<br>
**Gabarito:** [arquivo separado](B19_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B19-01 | 3.5 | Athena versus Redshift | single | fundamental | básica | Português |
| B19-02 | 3.5 | Extração de documentos | single | situacional | intermediária | Português |
| B19-03 | 3.5 | Data lake governance | single | situacional | intermediária | Inglês |
| B19-04 | 3.5 | MSK and Flink | multi-2 | integrada | avançada | Inglês |
| B19-05 | 3.5 | Secure ingestion access point | single | integrada | avançada | Inglês |
| B19-06 | 3.5 | Text to speech | single | situacional | intermediária | Inglês |
| B19-07 | 3.5 | AI/ML content pipeline | multi-2 | integrada | avançada | Inglês |
| B19-08 | 3.5 | Enterprise search | single | integrada | avançada | Inglês |
| B19-09 | 3.5 | Analytics and ML pipeline | multi-3 | integrada | avançada | Inglês |
| B19-10 | 3.5 | Business intelligence | single | situacional | intermediária | Inglês |

## Questões

### B19-01

**Context:** Uma equipe grava arquivos Parquet particionados no Amazon S3 e executa poucas consultas SQL ad hoc por semana.

**Requirement:** A solução deve evitar administração de infraestrutura e cobrar de acordo com os dados consultados.

**Question:** Qual serviço atende melhor?

- A. Amazon Athena.
- B. Amazon Redshift provisionado com nós sempre ativos.
- C. Amazon RDS for PostgreSQL Multi-AZ.
- D. Amazon Quick Sight usado como mecanismo SQL.

### B19-02

**Context:** Uma seguradora recebe formulários digitalizados que contêm texto, pares chave-valor e tabelas.

**Requirement:** Ela quer uma API gerenciada e pré-treinada, sem construir um modelo próprio.

**Question:** Qual serviço deve ser escolhido?

- A. Amazon Rekognition.
- B. Amazon Transcribe.
- C. Amazon Textract.
- D. Amazon SageMaker AI.

### B19-03

**Context:** A company has tables in the AWS Glue Data Catalog that reference data in Amazon S3.

**Requirement:** It needs centrally managed fine-grained permissions for the data lake.

**Question:** Which service should the company use?

- A. Amazon Transcribe.
- B. Amazon Quick Sight.
- C. Amazon MSK.
- D. AWS Lake Formation.

### B19-04

**Context:** Applications publish Apache Kafka records continuously. The company must calculate per-customer aggregates in five-minute windows and retain a durable, scalable Kafka-compatible event backbone.

**Requirement:** Minimize broker operations while preserving Kafka APIs and use managed stateful stream processing. **Choose TWO.**

- A. Use an AWS Glue crawler as the streaming broker.
- B. Use Amazon MSK for the Kafka-compatible event backbone.
- C. Run periodic Amazon Athena queries as the subsecond stream processor.
- D. Use Amazon Managed Service for Apache Flink for keyed windows and state.
- E. Use Amazon S3 Glacier Flexible Retrieval as the consumer checkpoint store.

### B19-05

**Context:** An ECS service in a producer account uses the AWS SDK to write
regulated events to an Amazon Kinesis Data Stream in a data account. The tasks
run in private subnets with no NAT gateway or internet route. Assume the Region
supports policies on Kinesis interface VPC endpoints.

**Requirement:** Only the service's task role may call `PutRecord` and
`PutRecords` on that stream. Traffic must use a private AWS path and TLS, and the
stream must use server-side encryption with a customer managed KMS key.

**Question:** Which design meets the requirements?

- A. Grant the task role the write actions in its identity policy, omit a stream
  resource policy because the role is already trusted in its own account, and
  send requests to the public Regional endpoint through a new NAT gateway.
- B. Grant the task role only `PutRecord` and `PutRecords` on the exact stream
  ARN, authorize that external role in the stream resource policy, use a
  Kinesis interface VPC endpoint with private DNS and a restrictive endpoint
  policy, and configure TLS plus the required cross-account permissions for the
  customer managed KMS key.
- C. Create a Kinesis interface VPC endpoint and name the stream in its endpoint
  policy, but grant no permissions to the task role or stream because private
  connectivity authorizes the request.
- D. Create an IAM user in the data account, store its long-term access keys in
  the task definition, grant `kinesis:*` and `kms:*` on all resources, and use
  the public Kinesis endpoint.

### B19-06

**Context:** An accessibility feature must read application text aloud in natural-sounding voices.

**Requirement:** The team wants a managed API and does not need to train a model.

**Question:** Which service is the best fit?

- A. AWS Glue.
- B. Amazon Transcribe.
- C. Amazon Rekognition.
- D. Amazon Polly.

### B19-07

**Context:** A contact center stores call recordings and needs searchable transcripts plus sentiment and named-entity analysis.

**Requirement:** Use managed, pretrained AI services and avoid building a speech or natural-language model. **Choose TWO.**

- A. Use Amazon Transcribe to convert the audio to text.
- B. Use Amazon Kendra to train a speech recognition model.
- C. Use Amazon Polly to convert each recording into another audio format.
- D. Use Amazon Comprehend to analyze sentiment and entities in the transcripts.
- E. Use Amazon Redshift as the speech-to-text engine.

### B19-08

**Context:** Employees must search policies stored across supported internal
repositories. Results should use semantic relevance and preserve source access
controls. The team does not want to train, host, or tune a search model.

**Requirement:** Provide managed enterprise search with connectors and
permission-aware results, while leaving document repositories as systems of
record.

**Question:** Which architecture is most appropriate?

- A. Index the repositories with Amazon Kendra connectors and map document access controls into the search experience.
- B. Build an OpenSearch index plus custom crawlers, relevance tuning, ACL synchronization, and query APIs for every repository.
- C. Put Amazon Lex in front of keyword searches performed independently by each source repository, with no shared permission-aware index.
- D. Build a Bedrock knowledge base and generative answer layer while implementing repository connectors and source-ACL enforcement separately.

### B19-09

**Context:** A company stores raw Parquet in S3, trains a proprietary forecasting model, and exposes curated results to governed analytics accounts.

**Requirement:** Data scientists need managed training and inference, analysts need serverless ad hoc SQL, and administrators need centralized fine-grained lake permissions. **Select THREE.**

- A. Use Amazon Textract for model training.
- B. Use Amazon SageMaker AI for training, experiments, and managed inference.
- C. Use Amazon Quick Sight as the data lake permissions engine.
- D. Use Amazon Athena for ad hoc SQL over the Parquet data.
- E. Use Amazon Translate to catalog the lake.
- F. Use AWS Lake Formation for centralized data permissions.

### B19-10

**Context:** Curated sales data is cataloged by AWS Glue and queried with
Athena. Business teams need interactive dashboards, scheduled refreshes, and
row-level visibility by Region without receiving direct S3 object permissions.

**Requirement:** Add a managed BI and visualization layer while preserving the
catalog/query layers and applying dataset-level access controls.

**Question:** Which service should be selected?

- A. Build a custom web dashboard that calls Athena for every interaction and reimplements caching, scheduled refresh, sharing, and row-level filtering.
- B. Use Amazon Managed Grafana as the business semantic layer, even though the primary requirement is governed business analytics rather than operational telemetry.
- C. Move curated data into Redshift Serverless and give business users SQL access, but provide no managed dashboard or row-level visualization layer.
- D. Amazon Quick Sight, the BI capability of Amazon Quick (listed as Amazon QuickSuite in the SAA-C03 guide), integrated with Athena and configured for row-level security.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B19-01 |  |  |  |
| B19-02 |  |  |  |
| B19-03 |  |  |  |
| B19-04 |  |  |  |
| B19-05 |  |  |  |
| B19-06 |  |  |  |
| B19-07 |  |  |  |
| B19-08 |  |  |  |
| B19-09 |  |  |  |
| B19-10 |  |  |  |
