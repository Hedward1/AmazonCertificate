# B12 — Questões

**Formato:** 10 questões autorais, com itens single-answer e multi-answer; siga a instrução de cada questão<br>
**Idioma:** 4 em português e 6 em inglês<br>
**Tempo sugerido:** 20 minutos<br>
**Aulas:** 150–171<br>
**Tarefas:** SAA-C03 1.1, 1.3, 3.2, 3.4 e 4.4

Responda sem abrir o gabarito. Registre resposta, confiança e palavra decisiva.

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Formato | Tipo | Dificuldade | Idioma |
|---|---:|---:|---|---|---|---|---|
| B12-01 | 1 | 1.3 | 150–153 | single | fundamental | básica | Português |
| B12-02 | 1 | 1.1 | 154–155, 160–161 | single | fundamental | básica | Português |
| B12-03 | 1 | 1.3 | 156–162 | multi-2 | integrada | avançada | Português |
| B12-04 | 3 | 3.4 | 170–171 | single | situacional | intermediária | Português |
| B12-05 | 3 | 3.4 | 165–167 | single | integrada | avançada | Inglês |
| B12-06 | 1 | 1.3 | 150–153 | single | situacional | intermediária | Inglês |
| B12-07 | 1 | 1.3 | 150–153 | single | situacional | intermediária | Inglês |
| B12-08 | 1 | 1.1 | 154–155 | multi-3 | integrada | avançada | Inglês |
| B12-09 | 3 | 3.2 | 164 | single | situacional | intermediária | Inglês |
| B12-10 | 4 | 4.4 | 169 | single | integrada | avançada | Inglês |

### B12-01

Uma empresa exige auditoria do uso da chave e a capacidade de revogar o acesso
a objetos S3 por uma política de chave. Qual solução atende melhor?

- A. SSE-S3 com ACL pública somente para leitura
- B. SSE-KMS com uma customer managed key e permissões de menor privilégio
- C. SSE-C enviando a chave por HTTP
- D. CORS com uma lista de origins confiáveis

### B12-02

Um navegador precisa enviar arquivos diretamente a um bucket privado sem
receber credenciais AWS. Qual desenho é o mais seguro?

- A. Desabilitar Block Public Access durante cada upload
- B. Colocar access keys de um usuário IAM no JavaScript
- C. O backend autenticado gera uma presigned URL de `PUT` curta; CORS limita a origin
- D. Permitir `s3:PutObject` para `Principal: *` e confiar em CORS

### B12-03

Registros regulados não podem ser apagados nem pela conta root durante sete
anos. Quais configurações devem ser usadas?

**Choose TWO.**

- A. Habilitar S3 Object Lock no bucket versionado que armazenará os registros.
- B. Usar governance mode e conceder `s3:BypassGovernanceRetention` à conta
  root.
- C. Aplicar compliance mode com período de retenção de sete anos às versões dos
  objetos.
- D. Usar apenas MFA Delete, sem Object Lock.
- E. Criar uma Lifecycle rule que expire as versões após sete dias.

### B12-04

Uma aplicação global de voz usa UDP e precisa de IPs de entrada estáticos e
failover entre Regions. Qual serviço é apropriado?

- A. S3 Transfer Acceleration
- B. CloudFront com invalidations
- C. Global Accelerator com endpoint groups
- D. Uma presigned URL do S3

### B12-05

A company serves the same private videos to users worldwide over HTTPS. It must
reduce origin load, keep the S3 bucket nonpublic, and minimize infrastructure
that the team must operate. Which design is best?

- A. CloudFront with an S3 origin, OAC, and a bucket policy scoped to the distribution
- B. S3 Transfer Acceleration with presigned URLs as the viewer delivery and
  caching layer
- C. CloudFront with the public S3 website endpoint as origin and an open bucket
  policy
- D. Global Accelerator in front of a self-managed public ALB and EC2 proxy tier
  that retrieves each object from the private bucket

### B12-06

A developer has `s3:GetObject` permission but receives `AccessDenied` for an
SSE-KMS object. What is the most likely missing authorization?

- A. Permission to invalidate CloudFront
- B. Permission to use the KMS key, allowed by IAM and the key policy
- C. A CORS rule for the developer's terminal
- D. An S3 website endpoint

### B12-07

A security team enables default SSE-KMS and wants to reduce AWS KMS request
costs for a high-volume bucket without changing the logical KMS key. What should
it enable?

- A. S3 Transfer Acceleration
- B. MFA Delete
- C. S3 Bucket Keys
- D. DSSE-KMS on every object

### B12-08

A browser request has valid AWS authorization, but JavaScript cannot read the
response because the web origin is not allowed. Which configuration should be
corrected?

**Select THREE.**

- A. The S3 CORS rule must allow the requesting origin, HTTP method, and
  required request headers.
- B. The KMS key rotation schedule determines which browser origins can read
  the response.
- C. CORS does not grant access by itself; IAM and bucket authorization remain
  separate checks.
- D. The SQS visibility timeout controls the browser's cross-origin response.
- E. A Global Accelerator traffic dial adds the required CORS response headers.
- F. The browser can issue a preflight `OPTIONS` request, which must match an
  applicable CORS rule.

### B12-09

A new AWS customer is designing a 2026 document-delivery path. Private source
objects remain in Amazon S3, but each authorized request needs a dynamically
redacted representation. The architecture proposal assumes that the customer
can create a new S3 Object Lambda Access Point and make it the long-lived
transformation dependency. The architect must validate current service
availability before selecting and securing a supported transformation design.

What is the blocking issue with the proposal?

- A. S3 Object Lambda supports only UDP, so an HTTPS document-delivery path can
  never use transformed object responses.
- B. S3 Object Lambda has been unavailable to new customers since November 7,
  2025, so this customer cannot base a new architecture on creating that access
  point and must evaluate a currently supported transformation pattern.
- C. S3 Object Lambda requires the source bucket and every transformed response
  to be public, which conflicts with all authenticated access.
- D. S3 Object Lambda was designed only to copy objects and never supported
  transformation of response data.

### B12-10

A team serves a private S3 origin through CloudFront and deploys JavaScript many
times per day. Each release must become immediately addressable, allow rapid
rollback to a prior build, retain effective edge caching, and avoid recurring
wildcard invalidations. The origin must remain private behind the distribution.

Which release design best meets the requirements?

- A. Overwrite the stable object name and issue a targeted invalidation for that
  path after every release, making invalidation part of every deployment.
- B. Overwrite one S3 key but append a new query string such as `?release=42`,
  assuming the query string permanently preserves the bytes of every prior
  build at the origin.
- C. Publish immutable versioned object names, update the application reference
  to the desired version, and retain prior versions for controlled rollback.
- D. Maintain two CloudFront distributions that both use the same mutable origin
  key and switch DNS between them, without retaining immutable prior objects.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B12-01 |  |  |  |
| B12-02 |  |  |  |
| B12-03 |  |  |  |
| B12-04 |  |  |  |
| B12-05 |  |  |  |
| B12-06 |  |  |  |
| B12-07 |  |  |  |
| B12-08 |  |  |  |
| B12-09 |  |  |  |
| B12-10 |  |  |  |

Depois consulte [B12 — Gabarito](B12_Gabarito.md).
