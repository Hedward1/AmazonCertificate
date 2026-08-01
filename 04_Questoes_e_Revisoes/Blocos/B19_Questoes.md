# B19 — Questões: Analytics, streaming e serviços gerenciados de AI/ML

**Quantidade:** 10 questões autorais<br>
**Idioma:** 2 em português e 8 em inglês<br>
**Regra:** selecione uma resposta em cada questão<br>
**Tempo sugerido:** 18 minutos; registre confiança antes de corrigir<br>
**Gabarito:** [arquivo separado](B19_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B19-01 | 3.5 | Athena versus Redshift | Situacional | Intermediária | Português |
| B19-02 | 3.5 | Extração de documentos | Situacional | Básica | Português |
| B19-03 | 3.5 | Data lake governance | Situacional | Intermediate | Inglês |
| B19-04 | 3.5 | MSK and Flink | Situacional | Intermediate | Inglês |
| B19-05 | 3.5 | Speech to text | Situacional | Basic | Inglês |
| B19-06 | 3.5 | Text to speech | Situacional | Basic | Inglês |
| B19-07 | 3.5 | Natural language insights | Situacional | Basic | Inglês |
| B19-08 | 3.5 | Enterprise search | Situacional | Intermediate | Inglês |
| B19-09 | 3.5 | Custom ML lifecycle | Situacional | Intermediate | Inglês |
| B19-10 | 3.5 | Business intelligence | Situacional | Basic | Inglês |

## Questões

### B19-01

**Context:** Uma equipe grava arquivos Parquet particionados no Amazon S3 e executa poucas consultas SQL ad hoc por semana.

**Requirement:** A solução deve evitar administração de infraestrutura e cobrar de acordo com os dados consultados.

**Question:** Qual serviço atende melhor?

- A. Amazon Athena.
- B. Amazon Redshift provisionado com nós sempre ativos.
- C. Amazon RDS for PostgreSQL Multi-AZ.
- D. Amazon Quick Sight usado como mecanismo SQL.

**Before moving on:** record the decisive words and your confidence.

### B19-02

**Context:** Uma seguradora recebe formulários digitalizados que contêm texto, pares chave-valor e tabelas.

**Requirement:** Ela quer uma API gerenciada e pré-treinada, sem construir um modelo próprio.

**Question:** Qual serviço deve ser escolhido?

- A. Amazon Rekognition.
- B. Amazon Transcribe.
- C. Amazon Textract.
- D. Amazon SageMaker AI.

**Before moving on:** record the decisive words and your confidence.

### B19-03

**Context:** A company has tables in the AWS Glue Data Catalog that reference data in Amazon S3.

**Requirement:** It needs centrally managed fine-grained permissions for the data lake.

**Question:** Which service should the company use?

- A. Amazon Transcribe.
- B. Amazon Quick Sight.
- C. Amazon MSK.
- D. AWS Lake Formation.

**Before moving on:** record the decisive words and your confidence.

### B19-04

**Context:** Applications publish Apache Kafka records continuously. The company must calculate per-customer aggregates in five-minute windows.

**Requirement:** The solution must preserve Kafka compatibility and perform stateful stream processing.

**Question:** Which combination best meets the requirements?

- A. AWS Glue crawler and Amazon Quick Sight.
- B. Amazon MSK and Amazon Managed Service for Apache Flink.
- C. Amazon Athena and Amazon Polly.
- D. Amazon S3 Glacier and AWS Batch.

**Before moving on:** record the decisive words and your confidence.

### B19-05

**Context:** A call center stores customer calls as audio files.

**Requirement:** The company needs searchable text transcripts of the conversations.

**Question:** Which service should be used?

- A. Amazon Polly.
- B. Amazon Transcribe.
- C. Amazon Translate.
- D. Amazon Textract.

**Before moving on:** record the decisive words and your confidence.

### B19-06

**Context:** An accessibility feature must read application text aloud in natural-sounding voices.

**Requirement:** The team wants a managed API and does not need to train a model.

**Question:** Which service is the best fit?

- A. AWS Glue.
- B. Amazon Transcribe.
- C. Amazon Rekognition.
- D. Amazon Polly.

**Before moving on:** record the decisive words and your confidence.

### B19-07

**Context:** A retailer has millions of written reviews.

**Requirement:** It must detect sentiment and named entities without developing a custom model.

**Question:** Which service should it use?

- A. Amazon Connect.
- B. Amazon Kendra.
- C. Amazon Comprehend.
- D. Amazon Redshift.

**Before moving on:** record the decisive words and your confidence.

### B19-08

**Context:** Employees need a natural-language search experience across internal document repositories.

**Requirement:** The company wants managed intelligent enterprise search rather than a model-building platform.

**Question:** Which service is most appropriate?

- A. Amazon Kendra.
- B. Amazon SageMaker AI.
- C. Amazon Lex.
- D. Amazon Athena.

**Before moving on:** record the decisive words and your confidence.

### B19-09

**Context:** Data scientists must train a proprietary forecasting model and deploy it behind a managed inference endpoint.

**Requirement:** They need control of training code, artifacts, experiments, and deployment.

**Question:** Which service best meets the requirement?

- A. Amazon Textract.
- B. Amazon SageMaker AI.
- C. Amazon Translate.
- D. Amazon Quick Sight.

**Before moving on:** record the decisive words and your confidence.

### B19-10

**Context:** Business users need interactive dashboards based on curated analytics results.

**Requirement:** The service must provide managed business intelligence and visualization.

**Question:** Which service should be selected?

- A. Amazon Textract.
- B. AWS Glue Data Catalog.
- C. Amazon MSK.
- D. Amazon Quick Sight, formerly Amazon QuickSight and now a component of Amazon Quick.

**Before moving on:** record the decisive words and your confidence.

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
