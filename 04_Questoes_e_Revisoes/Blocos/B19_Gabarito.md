# B19 — Gabarito comentado

Volte às [questões B19](B19_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B19-01 | A | 3.5 |
| B19-02 | C | 3.5 |
| B19-03 | D | 3.5 |
| B19-04 | B | 3.5 |
| B19-05 | B | 3.5 |
| B19-06 | D | 3.5 |
| B19-07 | C | 3.5 |
| B19-08 | A | 3.5 |
| B19-09 | B | 3.5 |
| B19-10 | D | 3.5 |

## B19-01 — Answer A

- **Central requirement:** A solução deve evitar administração de infraestrutura e cobrar de acordo com os dados consultados.
- **Decisive words:** Parquet, S3, ad hoc, sem infraestrutura
- **Why the correct answer works:** Athena consulta dados no S3 de forma serverless e cobra conforme os dados examinados.
- **A:** Athena é a escolha direta.
- **B:** Redshift é um warehouse e adiciona capacidade.
- **C:** RDS é OLTP e não consulta S3 como requisito.
- **D:** Quick Sight visualiza e não substitui o query engine.
- **Reusable rule:** SQL ad hoc sobre S3 com baixa operação aponta para Athena.
- **Cost/operation:** Partições e Parquet reduzem bytes examinados.
- **Variation:** Consultas recorrentes de warehouse podem favorecer Redshift.
- **Lessons:** 240–251
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)

## B19-02 — Answer C

- **Central requirement:** Ela quer uma API gerenciada e pré-treinada, sem construir um modelo próprio.
- **Decisive words:** formulários, tabelas, documentos, sem treinar
- **Why the correct answer works:** Textract extrai texto e estrutura, incluindo formulários e tabelas, de documentos.
- **A:** Rekognition analisa imagem e vídeo.
- **B:** Transcribe converte fala em texto.
- **C:** Textract é a escolha correta.
- **D:** SageMaker AI adiciona ciclo de modelo desnecessário.
- **Reusable rule:** Documentos estruturados apontam para Textract.
- **Cost/operation:** A API cobra por páginas e recursos usados.
- **Variation:** Imagem com objetos, sem estrutura documental, aponta para Rekognition.
- **Lessons:** 252–263
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)

## B19-03 — Answer D

- **Central requirement:** It needs centrally managed fine-grained permissions for the data lake.
- **Decisive words:** fine-grained permissions, data lake, catalog
- **Why the correct answer works:** Lake Formation provides centralized governance and fine-grained permissions for data lake resources.
- **A:** Transcribe converts audio to text.
- **B:** Quick Sight is business intelligence.
- **C:** MSK is managed Kafka.
- **D:** Lake Formation is correct.
- **Reusable rule:** Govern a cataloged data lake with Lake Formation; query it with engines such as Athena.
- **Cost/operation:** Permissions do not remove storage or query charges.
- **Variation:** A crawler discovers schema but is not the governance layer.
- **Lessons:** 245–251
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)

## B19-04 — Answer B

- **Central requirement:** The solution must preserve Kafka compatibility and perform stateful stream processing.
- **Decisive words:** Kafka, continuously, windows, stateful
- **Why the correct answer works:** MSK provides managed Kafka, and Managed Service for Apache Flink performs stateful stream processing.
- **A:** Glue crawler catalogs data, and BI is downstream.
- **B:** The combination meets both explicit requirements.
- **C:** Athena and Polly address unrelated needs.
- **D:** Archive and batch do not meet continuous latency.
- **Reusable rule:** MSK is the Kafka layer; Flink is the stateful processing layer.
- **Cost/operation:** Do not provision either service only for study; both can generate material charges.
- **Variation:** Without Kafka compatibility, evaluate more serverless ingestion options.
- **Lessons:** 248–251
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html)

## B19-05 — Answer B

- **Central requirement:** The company needs searchable text transcripts of the conversations.
- **Decisive words:** audio, transcripts, speech to text
- **Why the correct answer works:** Amazon Transcribe converts speech in audio into text.
- **A:** Polly produces speech from text.
- **B:** Transcribe is correct.
- **C:** Translate changes language of text.
- **D:** Textract reads documents.
- **Reusable rule:** Speech to text is Transcribe; text to speech is Polly.
- **Cost/operation:** Audio duration and features affect API cost.
- **Variation:** After transcription, Comprehend can analyze text sentiment.
- **Lessons:** 252–263
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html)

## B19-06 — Answer D

- **Central requirement:** The team wants a managed API and does not need to train a model.
- **Decisive words:** read text aloud, voices, managed API
- **Why the correct answer works:** Amazon Polly converts text into lifelike speech.
- **A:** Glue integrates data.
- **B:** Transcribe has the opposite direction.
- **C:** Rekognition analyzes visual media.
- **D:** Polly is correct.
- **Reusable rule:** Text to speech maps to Polly.
- **Cost/operation:** Characters and selected features influence pricing.
- **Variation:** Speech input that must become text maps to Transcribe.
- **Lessons:** 252–263
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/polly/latest/dg/what-is.html)

## B19-07 — Answer C

- **Central requirement:** It must detect sentiment and named entities without developing a custom model.
- **Decisive words:** written reviews, sentiment, entities, no custom model
- **Why the correct answer works:** Comprehend uses managed natural language processing for sentiment, entities, and related insights.
- **A:** Connect is a contact center.
- **B:** Kendra is enterprise search.
- **C:** Comprehend is correct.
- **D:** Redshift is a warehouse.
- **Reusable rule:** Managed NLP insights from text point to Comprehend.
- **Cost/operation:** Analyze only required text and apply data governance.
- **Variation:** Clinical text with healthcare entities may point to Comprehend Medical.
- **Lessons:** 252–263
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)

## B19-08 — Answer A

- **Central requirement:** The company wants managed intelligent enterprise search rather than a model-building platform.
- **Decisive words:** enterprise search, internal repositories, managed
- **Why the correct answer works:** Kendra is designed for intelligent enterprise search across organizational content.
- **A:** Kendra is correct.
- **B:** SageMaker AI is a model platform.
- **C:** Lex builds conversational interfaces.
- **D:** Athena queries structured data with SQL.
- **Reusable rule:** Enterprise intelligent search points to Kendra.
- **Cost/operation:** Indexes, connectors, and editions can incur ongoing charges.
- **Variation:** A chatbot can use Lex and call a search backend.
- **Lessons:** 252–263
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html)

## B19-09 — Answer B

- **Central requirement:** They need control of training code, artifacts, experiments, and deployment.
- **Decisive words:** proprietary model, training, endpoint, control
- **Why the correct answer works:** SageMaker AI supports building, training, and deploying custom machine learning models.
- **A:** Textract is a pre-trained document API.
- **B:** SageMaker AI is correct.
- **C:** Translate is a pre-trained translation API.
- **D:** Quick Sight is BI.
- **Reusable rule:** Custom model lifecycle points to SageMaker AI; a pre-trained API is narrower.
- **Cost/operation:** Training jobs, storage, notebooks, and endpoints can all incur charges.
- **Variation:** Do not use SageMaker AI when a pre-trained API fully satisfies the requirement.
- **Lessons:** 252–263
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

## B19-10 — Answer D

- **Central requirement:** The service must provide managed business intelligence and visualization.
- **Decisive words:** dashboards, business intelligence, visualization
- **Why the correct answer works:** Amazon Quick Sight is the business intelligence capability within Amazon Quick and provides dashboards and visualization.
- **A:** Textract extracts documents.
- **B:** Data Catalog stores metadata.
- **C:** MSK provides Kafka.
- **D:** Quick Sight is correct.
- **Reusable rule:** Dashboards and BI point to Amazon Quick Sight; preserve the course title QuickSight when matching the lesson.
- **Cost/operation:** Authors, readers, capacity, and features can affect pricing.
- **Variation:** The query engine and data preparation remain separate layers.
- **Lessons:** 245–251
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)
