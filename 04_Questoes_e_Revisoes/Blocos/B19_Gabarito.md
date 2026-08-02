# B19 — Gabarito comentado: analytics, ingestão segura e AI/ML

Volte às [questões B19](B19_Questoes.md) antes de corrigir.

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B19-01 | A | 3.5 |
| B19-02 | C | 3.5 |
| B19-03 | D | 3.5 |
| B19-04 | B,D | 3.5 |
| B19-05 | B | 3.5 |
| B19-06 | D | 3.5 |
| B19-07 | A,D | 3.5 |
| B19-08 | A | 3.5 |
| B19-09 | B,D,F | 3.5 |
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

## B19-04 — Answer B,D

- **Central requirement:** preserve Kafka APIs while minimizing broker and stateful stream-processing operations.
- **Decisive words:** *Kafka-compatible*, *managed*, *keyed five-minute windows*, *state*.
- **A:** incorrect; a crawler catalogs data and is not a streaming broker.
- **B:** correct; Amazon MSK provides the managed Kafka-compatible backbone.
- **C:** incorrect; periodic Athena queries are not a continuous stateful streaming engine.
- **D:** correct; Managed Service for Apache Flink supports keyed windows and application state.
- **E:** incorrect; Glacier is archival storage, not a consumer checkpoint mechanism.
- **Reusable rule:** preserve Kafka with MSK and add Flink when processing requires state, windows, or event-time semantics.
- **Lessons:** 248–251.
- **Official reference:** [Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html).

## B19-05 — Answer B

- **Central requirement:** secure cross-account Kinesis ingestion with
  least-privilege workload identity, private connectivity, TLS, and KMS
  encryption at rest.
- **Decisive words:** *producer account*, *data account*, *task role*, *no NAT*,
  *exact stream*, *customer managed KMS key*.
- **Why the correct answer works:** secure ingestion is layered: the caller's
  identity policy grants the write actions, the stream resource policy trusts
  that cross-account principal, the interface endpoint supplies the private
  path, its endpoint policy adds a boundary, TLS protects transit, and the KMS
  permissions allow the encrypted stream to serve the authorized producer.
- **A:** an identity policy in the producer account is only half of
  cross-account authorization; the stream must trust the external principal.
  It also violates the explicit no-NAT/private-path requirement.
- **B:** correct; it combines temporary task-role credentials, least privilege
  on the exact stream, resource trust, a private interface endpoint, TLS, and
  the customer managed key permissions required by the encrypted stream.
- **C:** a VPC endpoint and endpoint policy constrain a network path but do not
  replace the caller's identity permission or the cross-account stream resource
  policy.
- **D:** long-term credentials in a task definition, wildcard permissions, and
  a public path violate credential hygiene, least privilege, and private access.
- **Reusable rule:** secure ingestion requires a principal, permission on the
  target, resource trust when cross-account, an appropriate network path, and
  separate in-transit and at-rest encryption controls.
- **Cost/operation:** interface endpoints incur hourly/data processing charges,
  and customer managed KMS keys and requests can add cost.
- **Variation:** same-account access might not need a stream resource policy;
  an endpoint policy still does not grant permissions by itself.
- **Lessons:** 245–251 plus the official task 3.5 security objective.
- **Official references:** [Kinesis IAM and resource policies](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html), [Kinesis interface VPC endpoints](https://docs.aws.amazon.com/streams/latest/dev/vpc.html), [Kinesis data protection](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html), and [Kinesis infrastructure security](https://docs.aws.amazon.com/streams/latest/dev/infrastructure-security.html).

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

## B19-07 — Answer A,D

- **Central requirement:** turn speech into text and extract language insights with pretrained managed APIs.
- **Decisive words:** *recordings*, *searchable transcripts*, *sentiment*, *named entities*, *no model training*.
- **A:** correct; Transcribe converts speech recordings into text transcripts.
- **B:** incorrect; Kendra indexes and searches content but is not the speech-recognition engine.
- **C:** incorrect; Polly performs text-to-speech, the reverse direction.
- **D:** correct; Comprehend detects sentiment and entities in text.
- **E:** incorrect; Redshift can analyze stored structured results but does not transcribe speech.
- **Reusable rule:** compose narrow pretrained AI APIs by data transformation: speech-to-text first, NLP analysis second.
- **Lessons:** 252–263.
- **Official reference:** [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html) and [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html).

## B19-08 — Answer A

- **Central requirement:** provide managed, permission-aware semantic search across existing enterprise repositories without operating a custom model.
- **Decisive words:** connectors, source access controls, semantic relevance, systems of record
- **Why the correct answer works:** Kendra provides enterprise content connectors, indexing, relevance, and access-control-aware search patterns.
- **A:** correct; it separates the managed search index from source repositories while carrying document permissions into retrieval.
- **B:** OpenSearch can underpin enterprise search, but this option requires the connector, ACL, relevance, and API operations the team explicitly wants managed.
- **C:** Lex can provide a conversational interface, but independent keyword searches do not create the shared semantic, permission-aware enterprise index.
- **D:** a Bedrock knowledge base is plausible for RAG, but the option adds generative behavior and leaves connector/ACL work that the stated managed-search requirement avoids.
- **Reusable rule:** connector-based enterprise search with source permissions points to Kendra; a conversational front end or custom model is a separate layer.
- **Cost/operation:** Indexes, connectors, and editions can incur ongoing charges.
- **Variation:** A chatbot can use Lex or another interface and call Kendra as its retrieval backend.
- **Lessons:** 252–263
- **Official reference:** [AWS documentation](https://docs.aws.amazon.com/kendra/latest/dg/what-is-kendra.html)

## B19-09 — Answer B,D,F

- **Central requirement:** combine custom ML lifecycle, serverless lake SQL, and centralized data authorization.
- **Decisive words:** *proprietary model*, *managed inference*, *ad hoc SQL*, *fine-grained permissions*.
- **A:** incorrect; Textract is a pretrained document extraction API.
- **B:** correct; SageMaker AI manages training, experiments, artifacts, and inference endpoints.
- **C:** incorrect; Quick Sight consumes analytics data but is not the lake permissions engine.
- **D:** correct; Athena provides serverless SQL over Parquet in S3.
- **E:** incorrect; Translate neither catalogs nor governs the lake.
- **F:** correct; Lake Formation centrally manages supported fine-grained lake permissions.
- **Reusable rule:** integrated analytics separates ML compute, query engine, and governance rather than forcing one service to perform all roles.
- **Lessons:** 248–263.
- **Official reference:** [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), and [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html).

## B19-10 — Answer D

- **Central requirement:** add governed dashboards and row-level business access above the existing catalog and serverless query layers.
- **Decisive words:** Athena, interactive dashboards, scheduled refreshes, row-level visibility
- **Why the correct answer works:** Amazon Quick Sight connects to analytics sources such as Athena and supplies managed datasets, dashboards, sharing, and row-level security capabilities.
- **A:** a custom Athena-backed application can work, but it recreates managed BI capabilities and adds development/operation not requested.
- **B:** Managed Grafana is strong for operational metrics/log dashboards; it is a weaker fit for the stated governed business dataset and BI sharing requirements.
- **C:** Redshift Serverless can be a valid query/warehouse layer, but SQL access alone does not supply the requested managed visualization and row-level dashboard experience.
- **D:** correct; Quick Sight adds the visualization/access layer while Athena and Glue retain their query and catalog responsibilities.
- **Reusable rule:** Glue catalogs, Athena queries, and Quick Sight visualizes/governs BI consumption. Product documentation uses Amazon Quick and Amazon Quick Sight; the SAA-C03 guide currently lists Amazon QuickSuite, while the course may still say QuickSight.
- **Cost/operation:** Authors, readers, capacity, and features can affect pricing.
- **Variation:** The query engine and data preparation remain separate layers.
- **Lessons:** 245–251
- **Official reference:** [What is Amazon Quick?](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html)
