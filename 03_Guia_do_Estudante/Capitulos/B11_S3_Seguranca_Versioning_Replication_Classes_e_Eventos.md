# B11 — S3: segurança, versioning, replication, classes, lifecycle e eventos

**Data planejada:** 06/08/2026<br>
**Comece pelas aulas:** [roteiro B11 — aulas 128–149](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b11); faça `Q09` e `Q10`<br>
**Domínios:** 1, 2, 3 e 4<br>
**Tarefas principais:** 3.1 — Determine high-performing and/or scalable storage solutions; 4.1 — Design cost-optimized storage solutions; 1.1 — Design secure access to AWS resources; 2.2 — Design resilient architectures<br>
**Secundárias:** 1.3, 2.1 e 3.5<br>
**Pré-requisito:** [B10 — DNS e arquiteturas](B10_Route53_Avancado_Arquiteturas_Classicas_e_Beanstalk.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá conseguir:

1. explicar bucket, object, key, prefix e Region;
2. aplicar Block Public Access e bucket policy com menor privilégio;
3. prever política IAM + bucket policy + explicit deny;
4. reconhecer limitações de S3 static website hosting;
5. explicar version IDs, null version e delete markers;
6. planejar SRR/CRR e replication de objetos existentes;
7. selecionar storage class por acesso, resiliência, retrieval e duração mínima;
8. distinguir S3 Express One Zone e directory buckets;
9. criar lifecycle para current/noncurrent versions e incomplete multipart;
10. explicar Requester Pays;
11. escolher SNS, SQS, Lambda ou EventBridge para eventos;
12. projetar consumidor idempotente para duplicação/reordenação;
13. otimizar uploads/downloads e usar Batch Operations;
14. explicar Storage Lens e executar cleanup version-aware.

## 2. Como estudar as aulas

| Aulas | Tratamento |
|---|---|
| 128–129 | modelo S3 e hands-on |
| 130–131 | bucket policy e Block Public Access, alta prioridade |
| 132–133 | website; lembrar HTTP-only no endpoint |
| 134–135 | version IDs e delete markers |
| 136–138 | SRR/CRR, role e limites |
| 139–140 | storage classes e custos não óbvios |
| 141 | S3 Express One Zone/directory bucket |
| Q09 | quiz básico |
| 142–143 | lifecycle current/noncurrent |
| 144 | Requester Pays |
| 145–146 | notifications e idempotência |
| 147 | performance/multipart/ranges |
| 148 | Batch Operations |
| 149 | Storage Lens |
| Q10 | quiz avançado |

## 3. Modelo do S3

S3 é object storage. Um general purpose bucket é criado em uma Region e tem nome
globalmente único dentro da partition. Objetos são identificados por key; pastas
do console são prefixes no namespace, não diretórios de filesystem.

```text
bucket: saa-example
  ├── key: images/logo.png
  ├── key: reports/2026/aug.csv
  └── metadata + tags + storage class + version ID
```

O tamanho, API, consistência e quotas devem ser consultados na documentação
vigente. S3 fornece strong read-after-write consistency para PUT/DELETE e LIST,
mas isso não torna uma aplicação distribuída livre de concorrência lógica.
Conditional writes e versioning podem ser necessários.

S3 não é EBS nem EFS:

| Interface | Serviço inicial |
|---|---|
| object API HTTP | S3 |
| block device para EC2 | EBS |
| NFS compartilhado | EFS |

## 4. Segurança de acesso

Um request S3 pode ser afetado por IAM identity policy, bucket/access point
policy, ACLs quando habilitadas, VPC endpoint policy, KMS key policy, SCP e
Block Public Access. **Explicit deny vence allow.** A ausência de allow aplicável
resulta em implicit deny.

Prática segura:

1. habilite S3 Block Public Access em conta e bucket conforme governança;
2. use Object Ownership `Bucket owner enforced` para desabilitar ACLs quando
   possível;
3. conceda actions, bucket/object ARNs e principals mínimos;
4. imponha TLS com deny a `aws:SecureTransport=false` quando apropriado;
5. use VPC endpoint/Access Points conforme escala da política;
6. registre/audite sem expor dados.

Bucket ARN é `arn:aws:s3:::bucket`; objects usam
`arn:aws:s3:::bucket/prefix/*`. `s3:ListBucket` aplica ao bucket; `s3:GetObject`
aplica ao object ARN. Trocar os dois é uma pegadinha frequente.

### Cenário resolvido 1 — acesso somente ao prefixo

Uma role de aplicação precisa listar `tenant-a/` e ler objetos sob esse prefixo.
Conceda `ListBucket` no bucket condicionado ao prefix e `GetObject` em
`bucket/tenant-a/*`. Não torne o bucket público e não conceda `s3:*`.

## 5. Static website hosting

Website endpoint serve conteúdo estático e documentos de index/error. Para
acesso público direto, política/BPA precisariam permitir leitura pública — uma
decisão que deve ser explícita. O website endpoint aceita HTTP, não HTTPS.

Para domínio customizado HTTPS, use CloudFront na frente de uma origem S3
privada, com Origin Access Control, tema aprofundado no B12. Não confunda website
endpoint com REST endpoint.

### Cenário resolvido 2 — site público seguro

Marketing exige HTTPS e domínio próprio. Não abra website endpoint HTTP. Use
CloudFront + certificado apropriado + bucket privado/OAC. Se o exercício pedir
apenas website endpoint sem HTTPS, reconheça a limitação e a exposição exigida.

## 6. Versioning

Estados clássicos: unversioned, enabled e suspended. Após habilitar, suspender
para novas versões não apaga histórico nem retorna completamente ao estado
original.

- cada PUT da mesma key cria version ID novo;
- DELETE sem version ID geralmente cria delete marker, ocultando a versão atual;
- excluir o delete marker pode “reaparecer” a versão anterior;
- excluir uma version ID específica é permanente;
- em bucket que tinha objetos antes de habilitar, versões antigas podem ter ID
  `null`;
- versioning protege contra overwrite/delete acidental, mas aumenta storage.

### Cenário resolvido 3 — objeto “sumiu”

Após `DELETE report.csv`, um GET sem version ID retorna ausência, mas versões
anteriores continuam. Liste object versions/delete markers e remova o delete
marker correto se a intenção for restaurar. Não faça novo upload sem entender
qual versão deve ser current.

## 7. Replication

S3 Replication pode ser Same-Region (SRR) ou Cross-Region (CRR). Fonte e destino
precisam de versioning e S3 assume uma IAM role autorizada. Replication é
assíncrona; monitore status/métricas.

| Requisito | Opção |
|---|---|
| compliance/cópia em outra Region | CRR |
| agregação entre contas/mesma Region | SRR |
| objetos existentes | S3 Batch Replication/job apropriado |
| SLA de tempo para novos objetos elegíveis | Replication Time Control |

Regras podem filtrar prefix/tags e escolher storage class no destino. Objetos
existentes antes da regra não são retroativamente replicados pelo fluxo live;
use Batch Replication. Delete marker replication e mudança de ownership/KMS
exigem configuração/permissões específicas.

### Cenário resolvido 4 — histórico anterior

Uma empresa ativa CRR hoje, mas precisa copiar cinco anos de objetos existentes.
Configure replication para novos objects e execute S3 Batch Replication para o
histórico com manifest/job e role. Reenviar manualmente alteraria metadados e
seria operacionalmente frágil.

## 8. Storage classes

| Classe | Padrão de acesso | Resiliência/recuperação a considerar |
|---|---|---|
| Standard | frequente, baixa latência | Multi-AZ |
| Intelligent-Tiering | desconhecido/mudando | tiers automáticos; monitoring/automation fee por objeto elegível |
| Standard-IA | infrequente, ms | Multi-AZ, retrieval fee e mínimo |
| One Zone-IA | recriável, infrequente | uma AZ; não para única cópia crítica |
| Glacier Instant Retrieval | arquivo raro, ms | retrieval/minimum duration |
| Glacier Flexible Retrieval | arquivo, minutos–horas | restore antes do uso |
| Glacier Deep Archive | longo prazo, horas | menor custo, maior duração mínima |
| Express One Zone | altíssimo desempenho, single-digit ms | uma AZ e directory bucket |

Não escolha apenas por preço/GB. Inclua retrieval, requests, minimum billable
object size/duration, transições, replicas e custo de recuperação antecipada.
Confira preços atuais e Region.

### Cenário resolvido 5 — cópia recriável

Uma transformação gera arquivos grandes, acessados mensalmente, que podem ser
recriados a partir do original Multi-AZ. One Zone-IA pode reduzir custo aceitando
o risco zonal. A única cópia de documentos regulatórios não deve usar esse
raciocínio.

## 9. S3 Express One Zone

Express One Zone usa **directory buckets** em uma única AZ, voltados a workloads
latency-sensitive e alta taxa de requests. Directory buckets diferem em naming,
endpoint zonal, API/feature support e authorization/session model. Não presuma
paridade total com general purpose buckets.

Use quando compute e dados podem ser co-localizados na AZ e a aplicação aceita o
failure domain. Não é a opção de arquivo barato nem a única cópia de DR.

## 10. Lifecycle

Lifecycle automatiza transição e expiração. Em bucket versionado, trate
separadamente:

- current version transitions/expiration;
- noncurrent version transitions/expiration;
- expired object delete markers;
- abort incomplete multipart uploads;
- filtros por prefix, tag ou tamanho suportado.

A expiration de current version em bucket versionado normalmente cria delete
marker; sem regra para noncurrent versions, dados/custo permanecem. Transições
precisam respeitar restrições de classe e duração mínima.

S3 Storage Class Analysis ajuda a observar padrões para transições entre
Standard e classes IA suportadas; não decide todos os Glacier tiers por você.

## 11. Requester Pays

Em Requester Pays, o requester autenticado inclui confirmação de pagamento e
assume request/data transfer aplicáveis; o bucket owner continua pagando storage.
Anonymous access não funciona nesse modelo. Use para grandes datasets
compartilhados quando consumidores devem pagar acesso, com política/autorização.

## 12. Event notifications

S3 pode enviar eventos a SNS Standard, SQS Standard, Lambda ou EventBridge,
conforme integração/configuração. Filters por prefix/suffix reduzem ruído.

Entrega de notifications é at-least-once e pode haver duplicação/reordenação.
Consumidor deve ser idempotente, usar event/version/sequencer quando aplicável e
evitar loop (por exemplo, Lambda grava no mesmo prefix que a dispara).

### Cenário resolvido 6 — processamento de imagens

Uploads em `incoming/` disparam SQS; workers processam e escrevem em
`processed/`. Filter impede loop, fila absorve pico, DLQ trata falhas e uma chave
idempotente evita processar a mesma versão duas vezes. Invocar Lambda diretamente
seria válido para fluxo simples, mas oferece menos buffering.

## 13. Performance

- S3 escala por prefix e taxa de requests; não é necessário randomizar prefixes
  somente por conselho antigo;
- use multipart upload para objetos grandes e recuperação de partes;
- faça parallel byte-range GET quando a aplicação se beneficia;
- co-localize compute/Region para reduzir latência/transferência;
- Transfer Acceleration usa edge network para longas distâncias, com custo e
  benefício a medir;
- cache/CloudFront reduz downloads repetidos globais;
- `503 Slow Down` pede retry com exponential backoff e investigação do padrão.

## 14. Batch Operations e Storage Lens

S3 Batch Operations executa ação em grande conjunto definido por manifest, com
IAM role, job, prioridade, relatório e confirmação conforme configuração. Use
para copy, tag, restore, invoke Lambda, replication e outras operações suportadas;
não escreva loop caseiro para bilhões de objects.

S3 Storage Lens agrega métricas de uso/atividade e recomendações em escopo de
organização/conta/Region/bucket/prefix conforme dashboard e tier. Ajuda a achar
noncurrent versions, incomplete multipart uploads e oportunidades de custo.
Não é ferramenta de conteúdo: métricas não leem os dados dos objetos.

## 15. Tabela de decisão

| Palavra decisiva | Escolha |
|---|---|
| accidental overwrite/delete | versioning |
| copy new objects to another Region | CRR |
| replicate existing inventory | Batch Replication |
| unknown access pattern | Intelligent-Tiering |
| recreatable, infrequent, one AZ accepted | One Zone-IA |
| highest-performance object access in one AZ | Express One Zone |
| automatic transition/expiration | Lifecycle |
| consumer pays requests/transfer | Requester Pays |
| billions of object actions | Batch Operations |
| organization-wide storage visibility | Storage Lens |

## 16. Custos e cleanup

S3 cobra storage por classe, requests, retrieval, lifecycle transitions, data
transfer, replication, acceleration, inventory/analytics/Storage Lens advanced,
Batch jobs e minimum durations/tamanhos conforme opção. Versões, delete markers e
multipart incompleto são fontes comuns de resíduo.

No LAB, use dois objetos pequenos em um bucket general purpose e exclua no mesmo
dia. Lifecycle não terá tempo de agir; valide a configuração por leitura. Antes
de excluir bucket versionado, remova **todas as versões e delete markers**. Audite
replication destination, notifications e policies.

## 17. Armadilhas

- prefix não é diretório real;
- Block Public Access pode negar policy pública;
- website endpoint não oferece HTTPS;
- delete marker não apaga versões anteriores;
- versioning suspenso mantém histórico;
- live replication não copia histórico automaticamente;
- One Zone classes aceitam failure domain zonal;
- lifecycle de current não limpa noncurrent;
- notifications podem duplicar;
- Requester Pays não transfere custo de storage;
- esvaziar current keys não esvazia bucket versionado.

## 18. Checklist e recuperação ativa

- [ ] avalio allow/deny/BPA;
- [ ] recupero versão atrás de delete marker;
- [ ] escolho SRR/CRR/Batch Replication;
- [ ] seleciono classe por quatro dimensões;
- [ ] escrevo lifecycle current/noncurrent;
- [ ] desenho evento idempotente;
- [ ] explico Batch e Lens;
- [ ] executo cleanup version-aware.

## 19. Ligações e referências oficiais

- [LAB B11](../../05_Laboratorios/LAB_B11_S3_Versioning_Lifecycle_e_Cleanup.md)
- [Questões B11](../../04_Questoes_e_Revisoes/Blocos/B11_Questoes.md)
- [Gabarito B11](../../04_Questoes_e_Revisoes/Blocos/B11_Gabarito.md)
- [Checklist B11](../../06_Progresso/B11_Checklist_e_Revisoes.md)
- [S3 security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [Using versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
- [S3 Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [Storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [Lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)
- [S3 performance guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html)
- [S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html)
- [S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html)
