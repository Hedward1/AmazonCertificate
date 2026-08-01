# B12 — Segurança do S3, CloudFront e Global Accelerator

**Data planejada:** 07/08/2026<br>
**Nível:** iniciante<br>
**Comece pelas aulas:** [roteiro B12 — aulas 150–171](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b12); assista `150–171` e faça `Q11–Q12`<br>
**Domínios oficiais:** 1 — Design Secure Architectures; 3 — Design High-Performing Architectures<br>
**Tarefas principais:** 1.1 — Design secure access to AWS resources; 1.3 — Determine appropriate data security controls; 3.4 — Determine high-performing and/or scalable network architectures<br>
**Tarefas secundárias:** 1.2, 2.2 e 4.4<br>
**Pré-requisito:** B11 — classes de armazenamento e ciclo de vida do S3

## 1. Objetivos de aprendizagem

Ao terminar, você deverá conseguir:

1. escolher entre SSE-S3, SSE-KMS, DSSE-KMS, SSE-C e criptografia no cliente;
2. separar criptografia, autorização e acesso de rede;
3. explicar por que CORS não concede permissão ao S3;
4. usar URLs pré-assinadas sem transformá-las em credenciais permanentes;
5. diferenciar Versioning, MFA Delete, Object Lock e backup;
6. reconhecer Access Points e a situação atual do S3 Object Lambda;
7. manter uma origem S3 privada atrás do CloudFront;
8. comparar CloudFront e Global Accelerator por protocolo, cache e endpoint;
9. prever custos de KMS, logs, invalidações, transferência e IPv4;
10. identificar resíduos no cleanup.

## 2. Como estudar as aulas

| Aulas | Foco |
|---|---|
| 150–153 | modelos de encryption, default encryption e DSSE-KMS |
| 154–155 | CORS como regra do navegador, não autorização |
| 156–159 | MFA Delete, server access logging e auditoria |
| 160–161 | URL pré-assinada, expiração e permissões de quem assina |
| 162 | Vault Lock versus S3 Object Lock; foque Object Lock |
| 163 | Access Points e políticas por aplicação |
| 164 | reconhecer Object Lambda e ler a atualização de disponibilidade abaixo |
| 165–169 | CloudFront, origem privada, restrição geográfica e invalidation |
| 170–171 | Global Accelerator e endereços anycast estáticos |

### Atualização importante em 2026

Desde **7 de novembro de 2025**, S3 Object Lambda está disponível apenas para
clientes que já o utilizavam e para determinados parceiros APN. Para uma conta
nova, trate a aula 164 como reconhecimento histórico e escolha alternativas
como Lambda por API Gateway/Function URL, transformação no cliente ou uma
solução de transformação de imagens com CloudFront.

Todos os buckets S3 aplicam SSE-S3 aos novos objetos por padrão. Isso não
substitui a decisão por SSE-KMS/DSSE-KMS quando há requisito de controle de
chave, auditoria ou duas camadas de criptografia.

## 3. Criptografia: escolha pela responsabilidade sobre a chave

| Método | Chave | Vantagem dominante | Atenção de prova |
|---|---|---|---|
| SSE-S3 | gerenciada pelo S3 | simples, padrão e sem chamadas KMS do cliente | não oferece key policy ou trilha KMS por objeto |
| SSE-KMS | AWS KMS | controle de chave, policy e auditoria | exige permissão KMS; há custo e quota de chamadas |
| DSSE-KMS | duas camadas com KMS | requisito regulatório de dupla criptografia | maior custo; S3 Bucket Keys não são compatíveis |
| SSE-C | cliente fornece a chave em cada request | AWS não armazena a chave | HTTPS obrigatório; perder a chave perde o objeto |
| client-side | cliente cifra antes do upload | plaintext não chega ao S3 | cliente gerencia biblioteca, chaves e recuperação |

### 3.1 O que default encryption faz — e o que não faz

Default encryption define o comportamento quando o `PUT` não solicita outro
método permitido. Uma bucket policy ainda pode negar uploads que não usem a
chave KMS exigida. Em SSE-KMS, autorizações do S3 **e** do KMS precisam permitir
a operação. Uma S3 Bucket Key reduz as chamadas do S3 ao KMS e, portanto, custo
e pressão sobre quotas; ela não muda a chave lógica exigida pela política.

Criptografia em repouso não resolve:

- exposição pública por policy/ACL;
- tráfego sem TLS;
- principal com permissão excessiva;
- exfiltração por uma URL pré-assinada vazada;
- indisponibilidade causada pela remoção ou negação da chave KMS.

### Cenário resolvido 1 — chave controlada e auditoria

Uma empresa precisa revogar centralmente acesso a objetos e auditar o uso da
chave. Escolha **SSE-KMS com uma customer managed key**, key policy e IAM de
menor privilégio. SSE-S3 cifra os dados, mas não oferece o mesmo controle sobre
a chave. Se o requisito disser explicitamente “duas camadas independentes de
server-side encryption”, escolha DSSE-KMS, não duas chaves SSE-KMS arbitrárias.

## 4. CORS e URLs pré-assinadas

**CORS** informa ao navegador quais origins, métodos e headers podem participar
de uma requisição cross-origin. A sequência é:

```text
IAM/bucket policy permite? -> S3 processa a autorização
CORS permite a origin?     -> navegador entrega ou bloqueia a resposta ao código
```

CORS não deixa bucket público e não corrige `AccessDenied` de IAM. Configure
apenas origins e métodos necessários; `*` é inadequado quando o requisito pede
restrição explícita.

Uma **S3 presigned URL** delega temporariamente uma operação que o assinante
pode executar. Ela:

- funciona como bearer token até expirar ou as credenciais perderem validade;
- nunca pode sobreviver às credenciais temporárias que a assinaram;
- pode autorizar `GET` ou `PUT`, conforme a operação assinada;
- não torna o bucket público;
- deve ter expiração curta e nunca aparecer em logs, tickets ou Git;
- pode ser limitada por condições de policy, como idade da assinatura e rede.

### Cenário resolvido 2 — upload direto de um navegador

O navegador deve enviar uma foto sem receber credenciais AWS. O backend
autenticado valida o usuário, gera uma URL pré-assinada de `PUT` curta e retorna
somente ao cliente. A bucket policy limita o prefixo e o principal gerador;
CORS permite apenas a origin e o método necessários. Block Public Access fica
habilitado. CORS sozinho não atenderia à autorização; credenciais no browser
violariam menor privilégio.

## 5. Proteção contra exclusão e auditoria

| Controle | Protege principalmente | Limite importante |
|---|---|---|
| Versioning | sobrescrita/exclusão acidental | delete marker não é retenção imutável |
| MFA Delete | exclusão permanente de versões e mudança do Versioning | habilitação via API/CLI pela conta root; não serve como operação diária |
| Object Lock governance | retenção WORM com bypass autorizado | precisa Versioning; principal com permissão pode contornar |
| Object Lock compliance | retenção WORM rígida | nem root reduz/remove a retenção durante o prazo |
| legal hold | retenção sem data final | permanece até remoção explícita autorizada |
| backup/replicação | cópia recuperável em outro domínio | precisa política, teste de restore e proteção da cópia |

Server access logging entrega registros de acesso a um bucket de destino; a
entrega é best effort. CloudTrail data events oferecem outra trilha de chamadas
de objeto, com cobrança. Nunca envie logs para o mesmo bucket/prefixo de forma
que gere um loop. Auditoria e imutabilidade são decisões separadas.

## 6. Access Points e Object Lambda

Um S3 Access Point fornece hostname e policy próprios para um bucket. Ele reduz
a complexidade quando várias aplicações precisam de políticas e caminhos de
rede distintos. Um access point não duplica dados e sua policy trabalha em
conjunto com a bucket policy.

S3 Object Lambda transformava respostas `GET`, `LIST` e `HEAD` por uma função
Lambda. Além da restrição a novos clientes desde 2025, ele não deve ser
confundido com event notification: a transformação ocorria no caminho de
leitura, não após um upload.

## 7. CloudFront

CloudFront é uma CDN para HTTP/HTTPS. Edge locations armazenam objetos conforme
cache key e TTL. Um cache hit reduz latência e carga na origem; um miss consulta
a origem.

Para S3:

1. mantenha Block Public Access;
2. use uma origem S3 regular, não o website endpoint, quando precisa de OAC;
3. configure **Origin Access Control (OAC)**;
4. permita na bucket policy apenas a distribuição esperada;
5. use HTTPS, logging e WAF conforme o risco.

OAI é o mecanismo legado; OAC é a escolha moderna, inclusive para SSE-KMS e
requisições dinâmicas compatíveis. Signed URLs/cookies do CloudFront controlam
o acesso do viewer; uma URL pré-assinada do S3 contorna o cache do CloudFront e
é outro mecanismo.

**Geo restriction** usa país do viewer e serve para allowlist/denylist simples.
Não é autenticação. **Invalidation** remove objetos do cache antes do TTL, mas
tem custo além da franquia e não altera o objeto na origem. Prefira nomes
versionados (`app.20260807.js`) para releases frequentes.

## 8. Global Accelerator

Global Accelerator fornece dois endereços IPv4 anycast estáticos (ou
dual-stack quando configurado), leva tráfego TCP/UDP pela rede global da AWS e
encaminha para endpoints regionais saudáveis. É indicado quando o cliente exige
IP estático global, protocolos não HTTP ou failover regional rápido.

### Tabela de decisão — CloudFront versus Global Accelerator

| Decisão | CloudFront | Global Accelerator |
|---|---|---|
| protocolo | HTTP/HTTPS | TCP/UDP |
| cache em edge | sim | não |
| endpoint para cliente | DNS da distribuição | IPs anycast estáticos + DNS |
| conteúdo estático/dinâmico web | excelente | acelera caminho, mas não cacheia |
| jogos/VoIP/custom TCP | não | sim |
| origem típica | S3, ALB, API, HTTP origin | ALB, NLB, EC2, Elastic IP |
| controle geográfico de conteúdo | geo restriction | traffic dials/endpoint groups, não DRM |

### Cenário resolvido 3 — portal de vídeos

Milhões de usuários fazem `GET` dos mesmos vídeos via HTTPS. A prioridade é
cache e redução de carga no S3. Escolha CloudFront com OAC. Global Accelerator
não armazena vídeos em edge e não oferece ganho de cache.

### Cenário resolvido 4 — jogo UDP com allowlist

Jogadores globais acessam backends em duas Regions por UDP; clientes corporativos
exigem IPs fixos. Escolha Global Accelerator com endpoint groups e health
checks. CloudFront não transporta o protocolo UDP do jogo.

## 9. Custos e cleanup

Custos que aparecem mesmo quando “não há servidor”:

- armazenamento, requests e transferência do S3;
- requests do KMS e mensalidade de customer managed keys;
- armazenamento de versões antigas e logs;
- CloudTrail data events;
- tráfego/requests do CloudFront e invalidações adicionais;
- taxa fixa e dados do Global Accelerator;
- IPv4 público dos endpoints quando aplicável.

Cleanup do laboratório: uma presigned URL não tem recurso próprio para excluir;
quando necessário, invalide-a removendo o objeto, negando a operação ou
revogando as credenciais que assinaram; remova objetos, versões e delete markers;
excluir configuração de CORS/policy criada; esvaziar e excluir o bucket de
laboratório. Não crie uma KMS key, distribuição CloudFront ou accelerator apenas
para este bloco.

## 10. Armadilhas de prova

- “encrypted by default” não significa “somente principals autorizados”.
- CORS é aplicado pelo navegador; não é uma IAM policy.
- Presigned URL herda alcance e validade do assinante; não é URL pública eterna.
- MFA Delete não substitui Object Lock compliance.
- Object Lock age sobre versões; requer Versioning.
- CloudFront signed URL é diferente de S3 presigned URL.
- OAC mantém S3 privado; website endpoint não usa OAC da mesma forma.
- CloudFront cacheia HTTP; Global Accelerator acelera TCP/UDP sem cache.
- S3 Object Lambda não está aberto para novas contas desde 07/11/2025.

## 11. Checklist de decisão

1. Qual é o protocolo e existe conteúdo repetível para cache?
2. Preciso de IP global estático ou de uma CDN?
3. Quem controla a chave e quem precisa auditá-la?
4. A política exige uma ou duas camadas de encryption?
5. O acesso temporário é `GET`, `PUT` ou conteúdo privado do CloudFront?
6. A proteção exige recuperação, retenção WORM ou apenas versionamento?
7. Onde ficam logs, versões, chaves e objetos após o teste?

## 12. Recuperação ativa

Sem consulta, responda:

1. Por que SSE-KMS pode retornar `AccessDenied` mesmo com `s3:GetObject`?
2. Dê um exemplo em que CORS permite a origin, mas o S3 ainda nega o acesso.
3. Compare governance e compliance mode.
4. Desenhe S3 privado → OAC → CloudFront → viewer.
5. Escolha CloudFront ou Global Accelerator para vídeo, API HTTP, MQTT/TCP e UDP.
6. Cite três resíduos que podem continuar cobrando depois do laboratório.

## 13. Ligações

- Próximo: B13 — opções extras de armazenamento e migração.
- Retomar: B11 — storage classes, Versioning e lifecycle.
- Revisar depois: B21–B22 — avaliação de policies, KMS e segurança.
- [Laboratório B12](../../05_Laboratorios/LAB_B12_S3_Presigned_URL_CORS_e_Arquitetura_Global.md)
- [Questões B12](../../04_Questoes_e_Revisoes/Blocos/B12_Questoes.md)
- [Gabarito B12](../../04_Questoes_e_Revisoes/Blocos/B12_Gabarito.md)
- [Checklist e revisões B12](../../06_Progresso/B12_Checklist_e_Revisoes.md)

## 14. Referências oficiais

- [Default encryption no S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html)
- [S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
- [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
- [S3 Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html)
- [Mudança de disponibilidade do S3 Object Lambda](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazons3-ol-change.html)
- [Restringir origem S3 com OAC](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
- [CloudFront caching](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
- [O que é AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
