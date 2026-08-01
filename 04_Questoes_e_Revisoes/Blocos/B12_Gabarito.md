# B12 — Gabarito comentado

Abra somente depois de responder às [questões B12](B12_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B12-01 | B | 1.3 |
| B12-02 | C | 1.1 |
| B12-03 | A,C | 1.3 |
| B12-04 | C | 3.4 |
| B12-05 | A | 3.4 |
| B12-06 | B | 1.3 |
| B12-07 | C | 1.3 |
| B12-08 | A,C,F | 1.1 |
| B12-09 | B | 3.2 |
| B12-10 | C | 4.4 |

## B12-01 — Resposta B

- **Requisito central:** controlar, revogar e auditar o uso da chave.
- **Palavras decisivas:** *key policy*, *revogar*, *auditoria*.
- **A:** SSE-S3 cifra, mas uma ACL pública viola o acesso seguro e não oferece a política de chave solicitada.
- **B:** correta; SSE-KMS com customer managed key oferece key policy, controle e trilha de chamadas KMS.
- **C:** SSE-C entrega ao cliente a custódia da chave e exige HTTPS; a alternativa propõe HTTP.
- **D:** CORS controla comportamento do navegador, não a chave nem a autorização.
- **Regra reutilizável:** controle e trilha da chave → SSE-KMS com menor privilégio.
- **Aulas:** 150–153.
- **Referência:** [SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).
- **Erro comum:** confundir dados cifrados com acesso autorizado.

## B12-02 — Resposta C

- **Requisito central:** upload temporário sem credenciais AWS no cliente.
- **Palavras decisivas:** *browser*, *bucket privado*, *sem credenciais*.
- **A:** desabilitar Block Public Access cria uma exposição desnecessária.
- **B:** access keys no JavaScript são segredos recuperáveis pelo usuário.
- **C:** correta; o backend delega somente `PUT` por pouco tempo e CORS limita a origin do browser.
- **D:** `Principal: *` abre autorização; CORS não restringe chamadas fora do navegador.
- **Regra reutilizável:** delegação temporária de uma operação S3 → presigned URL curta; BPA continua ligado.
- **Aulas:** 154–155 e 160–161.
- **Referência:** [Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html).
- **Erro comum:** tratar a configuração CORS como bucket policy.

## B12-03 — Resposta A,C

- **Requisito central:** retenção WORM que nem root possa reduzir durante sete anos.
- **Palavras decisivas:** *nem root*, *não pode apagar*, *sete anos*.
- **A:** correta; Object Lock opera sobre versões de objetos em um bucket com o
  recurso habilitado.
- **B:** governance mode admite bypass por identidades autorizadas e não atende
  à proibição absoluta.
- **C:** correta; compliance mode impede apagar ou reduzir a retenção durante os
  sete anos, inclusive pelo root user.
- **D:** MFA Delete não oferece retenção WORM irredutível.
- **E:** Lifecycle expiration apaga versões elegíveis; não cria proteção
  regulatória.
- **Regra reutilizável:** retenção regulatória irredutível → Object Lock compliance.
- **Variação:** governance mode é adequado quando administradores autorizados
  precisam poder usar bypass em situações controladas.
- **Aulas:** 156–162.
- **Referência:** [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).
- **Erro comum:** escolher governance quando o enunciado proíbe qualquer bypass.

## B12-04 — Resposta C

- **Requisito central:** endpoint global UDP com IPs estáticos e failover regional.
- **Palavras decisivas:** *UDP*, *IPs estáticos*, *multi-Region*.
- **A:** S3 Transfer Acceleration atende transferência de objetos, não voz UDP arbitrária.
- **B:** CloudFront é uma CDN para HTTP/HTTPS e cache.
- **C:** correta; Global Accelerator fornece anycast IPs e roteia TCP/UDP a endpoint groups saudáveis.
- **D:** uma URL S3 não transporta o protocolo de voz.
- **Regra reutilizável:** TCP/UDP global + IP estático → Global Accelerator.
- **Aulas:** 170–171.
- **Referência:** [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html).
- **Erro comum:** escolher CloudFront apenas porque o cliente é global.

## B12-05 — Answer A

- **Central requirement:** cache private HTTPS content worldwide while reducing
  S3 origin load and operational overhead.
- **Decisive words:** *same videos*, *worldwide*, *nonpublic S3*, *minimize
  infrastructure*.
- **A:** correct; CloudFront caches at edge while OAC and a distribution-scoped
  bucket policy restrict direct origin access.
- **B:** S3 Transfer Acceleration optimizes transfers into or out of S3 through
  accelerated endpoints; it is not a viewer CDN cache and does not reduce
  repeated origin reads like CloudFront.
- **C:** the S3 website endpoint requires public-origin access and cannot use OAC,
  violating the nonpublic-bucket requirement.
- **D:** a proxy tier can be engineered to retrieve private objects, but Global
  Accelerator is not an object cache and the ALB/EC2 fleet adds avoidable
  infrastructure and origin requests.
- **Reusable rule:** repeated web content + private S3 origin → CloudFront with OAC.
- **Lessons:** 165–167.
- **Reference:** [Restrict S3 origin access](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).
- **Common trap:** using the S3 website endpoint when OAC is required.

## B12-06 — Answer B

- **Central requirement:** authorize decryption of an SSE-KMS object.
- **Decisive words:** *SSE-KMS*, *GetObject*, *AccessDenied*.
- **A:** CloudFront invalidation has no effect on KMS authorization.
- **B:** correct; S3 permission and permission to use the KMS key must both allow the request.
- **C:** browser CORS does not govern a terminal or grant decrypt permission.
- **D:** an S3 website endpoint cannot grant KMS access.
- **Reusable rule:** SSE-KMS reads require data access and KMS key access.
- **Lessons:** 150–153.
- **Reference:** [SSE-KMS permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).
- **Common trap:** checking only the identity policy and ignoring the key policy.

## B12-07 — Answer C

- **Central requirement:** reduce KMS request cost without changing the logical KMS key.
- **Decisive words:** *high volume*, *KMS request costs*.
- **A:** Transfer Acceleration changes the upload path, not KMS calls.
- **B:** MFA Delete protects version-management operations.
- **C:** correct; S3 Bucket Keys reduce S3-to-KMS request traffic for SSE-KMS.
- **D:** DSSE-KMS adds an encryption layer and does not support S3 Bucket Keys.
- **Reusable rule:** high-volume SSE-KMS bucket → evaluate S3 Bucket Keys.
- **Lessons:** 150–153.
- **Reference:** [S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html).
- **Common trap:** assuming Bucket Keys remove the need for KMS authorization.

## B12-08 — Answer A,C,F

- **Central requirement:** let approved browser JavaScript read an authorized cross-origin response.
- **Decisive words:** *browser*, *origin not allowed*, *already authorized*.
- **A:** correct; the CORS configuration defines allowed origins, methods, and
  request headers.
- **B:** KMS rotation does not control a browser origin.
- **C:** correct; CORS controls browser cross-origin behavior and does not
  replace IAM or bucket authorization.
- **D:** visibility timeout is an SQS setting.
- **E:** traffic dials govern Global Accelerator routing and do not add S3 CORS
  headers.
- **F:** correct; a browser preflight uses `OPTIONS`, and S3 must find a matching
  CORS rule to return the required response headers.
- **Reusable rule:** browser cross-origin failure after authorization → inspect CORS.
- **Variation:** an IAM `AccessDenied` must be corrected in authorization rather
  than hidden by a permissive CORS rule.
- **Lessons:** 154–155.
- **Reference:** [S3 CORS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html).
- **Common trap:** using CORS to troubleshoot an IAM `AccessDenied`.

## B12-09 — Answer B

- **Central requirement:** reject an unavailable new-customer dependency before
  designing authorization and dynamic redaction around it.
- **Decisive words:** *new AWS customer*, *2026*, *create a new Object Lambda
  Access Point*, *long-lived dependency*.
- **A:** Object Lambda transformed supported S3 API responses; UDP is unrelated
  to the service's availability restriction.
- **B:** correct; since November 7, 2025 it has been limited to existing customers
  and selected partners, so a new customer must choose a currently supported
  transformation architecture and secure that path explicitly.
- **C:** Object Lambda did not inherently require making the source bucket or
  transformed data public.
- **D:** response transformation was its core purpose, so capability is not the
  problem; new-customer availability is.
- **Reusable rule:** validate current availability first; do not make a new
  architecture depend on a service the account cannot adopt.
- **Variation:** the replacement design depends on where transformation can run,
  payload size, latency, cacheability, and authorization boundaries.
- **Lessons:** 164.
- **Reference:** [Availability change](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazons3-ol-change.html).
- **Common trap:** memorizing an older course slide without checking current availability.

## B12-10 — Answer C

- **Central requirement:** combine immediate static releases, cache efficiency,
  private-origin protection, and deterministic rollback.
- **Decisive words:** *private S3 origin*, *many times per day*, *immediately
  addressable*, *rollback*, *avoid wildcard invalidations*.
- **A:** targeted invalidation is narrower than `/*`, but making it part of every
  release still violates the requirement to avoid recurring invalidations and
  couples freshness to invalidation completion.
- **B:** a query string can create a distinct CloudFront cache key, but it does
  not preserve old bytes at a mutable S3 origin key; after eviction, an old
  query can retrieve the newly overwritten object and break deterministic
  rollback.
- **C:** correct; immutable versioned names create a new cache key, while changing
  the reference selects the release and retaining old versions enables rollback.
- **D:** two distributions add operational cost, and both still depend on the
  same mutable origin object, so previous releases are not retained for
  deterministic rollback.
- **Reusable rule:** frequent static releases → immutable versioned keys; update
  references for release/rollback and reserve invalidation for exceptions.
- **Variation:** a short-lived HTML entry point can use a different cache policy
  from immutable hashed assets.
- **Lessons:** 169.
- **Reference:** [CloudFront invalidation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html).
- **Common trap:** invalidating `/*` as the normal deployment mechanism.

## Ação após a correção

Registre erros e acertos de baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), incluindo requisito, palavra decisiva, regra e datas D+2/D+7.
