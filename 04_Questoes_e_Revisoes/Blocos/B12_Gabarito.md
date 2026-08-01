# B12 — Gabarito comentado

Abra somente depois de responder às [questões B12](B12_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B12-01 | B | 1.3 |
| B12-02 | C | 1.1 |
| B12-03 | A | 1.3 |
| B12-04 | C | 3.4 |
| B12-05 | A | 3.4 |
| B12-06 | B | 1.3 |
| B12-07 | C | 1.3 |
| B12-08 | A | 1.1 |
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

## B12-03 — Resposta A

- **Requisito central:** retenção WORM que nem root possa reduzir durante sete anos.
- **Palavras decisivas:** *nem root*, *não pode apagar*, *sete anos*.
- **A:** correta; compliance mode impede apagar ou reduzir a retenção durante o prazo.
- **B:** Versioning permite recuperação comum, mas versões ainda podem ser permanentemente removidas.
- **C:** MFA Delete não oferece retenção irredutível e depende de Versioning.
- **D:** Lifecycle expiration apaga dados; não os protege contra exclusão.
- **Regra reutilizável:** retenção regulatória irredutível → Object Lock compliance.
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

- **Central requirement:** cache private HTTPS content while reducing S3 origin load.
- **Decisive words:** *same videos*, *worldwide*, *nonpublic S3*.
- **A:** correct; CloudFront caches at edge while OAC and a scoped bucket policy restrict origin access.
- **B:** Global Accelerator does not provide an S3 object cache.
- **C:** public website hosting violates the nonpublic-origin requirement.
- **D:** S3 objects cannot be assigned Elastic IP addresses.
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

## B12-08 — Answer A

- **Central requirement:** let approved browser JavaScript read an authorized cross-origin response.
- **Decisive words:** *browser*, *origin not allowed*, *already authorized*.
- **A:** correct; the CORS configuration defines allowed origins, methods, and headers.
- **B:** KMS rotation does not control a browser origin.
- **C:** visibility timeout is an SQS setting.
- **D:** traffic dials govern Global Accelerator routing.
- **Reusable rule:** browser cross-origin failure after authorization → inspect CORS.
- **Lessons:** 154–155.
- **Reference:** [S3 CORS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html).
- **Common trap:** using CORS to troubleshoot an IAM `AccessDenied`.

## B12-09 — Answer B

- **Central requirement:** validate a service choice for a new AWS customer in 2026.
- **Decisive words:** *new customer*, *2026*, *Object Lambda*.
- **A:** Object Lambda handled S3 API responses, not UDP traffic.
- **B:** correct; it has been available only to existing customers and selected partners since November 7, 2025.
- **C:** S3 Object Lambda did not require a public bucket.
- **D:** dynamic response transformation was the service's purpose.
- **Reusable rule:** new customer → do not design a new dependency on S3 Object Lambda.
- **Lessons:** 164.
- **Reference:** [Availability change](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazons3-ol-change.html).
- **Common trap:** memorizing an older course slide without checking current availability.

## B12-10 — Answer C

- **Central requirement:** frequent static releases with low invalidation cost and fast adoption.
- **Decisive words:** *many times per day*, *immediate*, *low cost*.
- **A:** repeated wildcard invalidations add cost and invalidate more than necessary.
- **B:** disabling caching discards the CDN benefit.
- **C:** correct; immutable versioned names make the new reference a natural cache miss.
- **D:** a public EC2 instance adds operations and loses edge caching.
- **Reusable rule:** frequently changing assets → version filenames; invalidate only exceptional objects.
- **Lessons:** 169.
- **Reference:** [CloudFront invalidation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html).
- **Common trap:** invalidating `/*` as the normal deployment mechanism.

## Ação após a correção

Registre erros e acertos de baixa confiança no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md), incluindo requisito, palavra decisiva, regra e datas D+2/D+7.
