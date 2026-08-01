# B12 — Questões

**Formato:** 10 questões autorais, uma resposta correta por questão<br>
**Idioma:** 4 em português e 6 em inglês<br>
**Tempo sugerido:** 20 minutos<br>
**Aulas:** 150–171<br>
**Tarefas:** SAA-C03 1.1, 1.3, 3.2, 3.4 e 4.4

Responda sem abrir o gabarito. Registre resposta, confiança e palavra decisiva.

## Metadados das questões

| ID | Domínio | Tarefa | Aulas | Idioma |
|---|---:|---:|---|---|
| B12-01 | 1 | 1.3 | 150–153 | Português |
| B12-02 | 1 | 1.1 | 154–155, 160–161 | Português |
| B12-03 | 1 | 1.3 | 156–162 | Português |
| B12-04 | 3 | 3.4 | 170–171 | Português |
| B12-05 | 3 | 3.4 | 165–167 | Inglês |
| B12-06 | 1 | 1.3 | 150–153 | Inglês |
| B12-07 | 1 | 1.3 | 150–153 | Inglês |
| B12-08 | 1 | 1.1 | 154–155 | Inglês |
| B12-09 | 3 | 3.2 | 164 | Inglês |
| B12-10 | 4 | 4.4 | 169 | Inglês |

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
anos. Qual controle deve ser usado?

- A. S3 Object Lock em compliance mode com retenção apropriada
- B. Versioning com delete markers
- C. MFA Delete sem Versioning
- D. Lifecycle expiration após sete dias

### B12-04

Uma aplicação global de voz usa UDP e precisa de IPs de entrada estáticos e
failover entre Regions. Qual serviço é apropriado?

- A. S3 Transfer Acceleration
- B. CloudFront com invalidations
- C. Global Accelerator com endpoint groups
- D. Uma presigned URL do S3

### B12-05

A company serves the same private videos to users worldwide over HTTPS. It must
reduce origin load and keep the S3 bucket nonpublic. Which design is best?

- A. CloudFront with an S3 origin, OAC, and a bucket policy scoped to the distribution
- B. Global Accelerator pointing directly to the S3 bucket
- C. Public S3 website hosting with an open bucket policy
- D. A separate Elastic IP for every object

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

- A. The S3 CORS configuration
- B. The KMS rotation schedule
- C. The SQS visibility timeout
- D. The Global Accelerator traffic dial

### B12-09

A new AWS customer in 2026 wants to transform S3 `GET` responses dynamically.
The design proposal uses a newly created S3 Object Lambda Access Point. What is
the key issue?

- A. Object Lambda supports only UDP
- B. Object Lambda has been unavailable to new customers since November 7, 2025
- C. Object Lambda requires every bucket to be public
- D. Object Lambda cannot transform object data

### B12-10

A team deploys a new JavaScript file many times per day through CloudFront. It
wants low operational cost and immediate adoption of each release. Which
strategy is preferred?

- A. Use the same object name and invalidate `/*` after every upload
- B. Disable caching globally
- C. Use versioned object names and update the application reference
- D. Replace CloudFront with a public EC2 instance

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
