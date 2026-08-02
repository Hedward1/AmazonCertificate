# LAB B19 — Pipeline de analytics, ingestão segura e seleção de AI/ML

**Tempo:** 20 minutos<br>
**Modo:** diagrama e leitura<br>
**Custo:** USD 0,00 esperado<br>
**Capítulo:** [abrir](../03_Guia_do_Estudante/Capitulos/B19_Analytics_Streaming_e_Machine_Learning.md)

## 1. Objetivos

1. Desenhar pipeline batch.
2. Desenhar pipeline streaming.
3. Separar dados e catálogo.
4. Relacionar MSK e Flink.
5. Selecionar APIs de AI.
6. Aplicar em modo read-only as quatro camadas de segurança de um ponto de
   ingestão.
7. Comparar custo e operação.
8. Concluir sem recursos criados.

## 2. Resultado esperado

- Diagrama batch completo.
- Diagrama streaming completo.
- Matriz AI com dez casos.
- Matriz de acesso seguro à ingestão preenchida.
- Nenhum recurso criado.
- Inventário final igual ao inicial.
- Custo esperado zero.

## 3. Custo

USD 0,00 esperado.
- Confira preços e Region.
- Serviços anexos podem cobrar.
- Não crie recursos não previstos.
- O cleanup faz parte do laboratório.
- Serverless não significa gratuito.

## 4. Preflight

1. Autentique pela rota do LAB B02.
2. Confirme identidade não root.
3. Confirme Region.
4. Confira preços oficiais.
5. Registre somente contagens.
6. Não clique em Create.
7. Não execute crawler, query ou job.
8. Não crie cluster, application ou endpoint.
9. Prepare editor local.
10. Defina alarme de vinte minutos.

### Critério para prosseguir

- [ ] Identidade não root.
- [ ] Region confirmada.
- [ ] Inventário válido.
- [ ] Preços conferidos.
- [ ] Tempo de cleanup reservado.

## 5. Arquitetura

- Fonte para S3 raw.
- Glue crawler para Data Catalog.
- Glue job para S3 curado em Parquet.
- Athena para SQL ad hoc.
- Amazon Quick no nome atual da documentação, usando o componente de BI Amazon
  Quick Sight (antigo QuickSight); o guia SAA-C03 chama a plataforma de Amazon
  QuickSuite.
- Producers para MSK.
- Flink como processador stateful.
- S3 como destino durável.
- Redshift somente se warehouse for requisito.
- IAM, KMS, logs e lifecycle em todas as camadas.
- Produtor com role temporária e permissão de escrita no recurso exato.
- Resource policy quando o acesso for cross-account e o serviço a suportar.
- Endpoint privado e endpoint policy como limites de rede adicionais, não como
  substitutos da autorização.
- TLS em trânsito e criptografia KMS/SSE em repouso.

## 6. Execução

### Etapa 1 — Inventário

1. Observe workgroups Athena sem executar query.
2. Observe contagem de Glue databases.
3. Observe contagem de crawlers e jobs.
4. Observe contagem de MSK clusters.
5. Observe contagem de Flink applications.
6. Observe contagem de SageMaker endpoints.
7. Marque AccessDenied como não verificado.
8. Feche assistentes de criação.

### Etapa 2 — Batch

1. Desenhe fonte e S3 raw.
2. Adicione Glue Data Catalog.
3. Adicione crawler.
4. Adicione transformação.
5. Escolha Parquet e compressão.
6. Particione por data.
7. Ligue Athena ao catálogo.
8. Adicione Amazon Quick Sight, componente de BI do Amazon Quick, como consumidor.

### Etapa 3 — Streaming

1. Desenhe producers e MSK.
2. Adicione Flink.
3. Defina janela de cinco minutos.
4. Defina estado e checkpoint.
5. Adicione retry.
6. Adicione destino durável.
7. Escreva por que MSK não processa sozinho.
8. Anote alternativa sem Kafka.

### Etapa 4 — Aplicação read-only: secure ingestion access point

Use este cenário sem criar ou alterar recursos:

> Uma task ECS em uma conta produtora precisa usar o AWS SDK para gravar em um
> Kinesis Data Stream de uma conta de dados. A subnet não tem NAT. Somente a
> task role pode escrever, e o stream usa uma customer managed KMS key.

1. Não execute `PutRecord`, `PutRecords`, criação de endpoint, edição de policy
   ou alteração de criptografia.
2. Se houver um stream de treinamento cuja inspeção seja autorizada, abra
   apenas seus detalhes e registre `presente`, `ausente` ou `não verificado`
   para server-side encryption. Não copie nome, ARN ou key ID.
3. Na tela read-only de VPC endpoints, registre apenas se existe um interface
   endpoint para Kinesis na Region. Não registre IDs, IPs, DNS ou nomes.
4. No editor local, escreva a intenção da identity policy: a task role recebe
   somente `kinesis:PutRecord` e `kinesis:PutRecords` no ARN exato do stream.
5. Escreva a intenção da resource policy: o stream confia nessa role externa
   somente para as ações de ingestão necessárias.
6. Escreva a intenção da endpoint policy: permitir somente o principal e o
   stream esperados pelo caminho privado. Anote que essa policy não concede a
   autorização ausente nas duas policies anteriores.
7. Marque TLS 1.2+ para trânsito e valide conceitualmente as permissões
   cross-account da customer managed KMS key para a criptografia do stream.
8. Se não houver recursos preexistentes ou houver `AccessDenied`, use `não
   verificado` e conclua o desenho com a documentação oficial. Não crie nada
   para obter evidência.

Preencha esta matriz:

| Camada | Decisão no cenário | Evidência read-only |
|---|---|---|
| Autenticação | credenciais temporárias da ECS task role | presente/ausente/não verificado |
| Autorização da identidade | `PutRecord`/`PutRecords` no stream exato | presente/ausente/não verificado |
| Confiança do recurso | resource policy para a role cross-account | presente/ausente/não verificado |
| Caminho privado | interface endpoint Kinesis + private DNS | presente/ausente/não verificado |
| Limite do endpoint | endpoint policy restrita | presente/ausente/não verificado |
| Trânsito | TLS 1.2+ | exigido pela documentação |
| Repouso | SSE-KMS e permissões da customer managed key | presente/ausente/não verificado |

Conclua com uma frase: **rede privada reduz exposição, mas somente as policies
corretas autorizam a gravação**.

### Etapa 5 — AI

1. Mapeie Rekognition.
2. Mapeie Transcribe e Polly.
3. Mapeie Translate.
4. Mapeie Lex e Connect.
5. Mapeie Comprehend.
6. Mapeie SageMaker AI.
7. Mapeie Kendra e Textract.
8. Confirme que Personalize não aparece.

## 7. Validação

- [ ] Diagrama batch completo.
- [ ] Diagrama streaming completo.
- [ ] Matriz AI com dez casos.
- [ ] Matriz de acesso seguro à ingestão preenchida.
- [ ] Identity, resource e endpoint policies não foram tratadas como equivalentes.
- [ ] Nenhum registro foi enviado ao stream.
- [ ] Nenhum recurso criado.
- [ ] Inventário final igual ao inicial.
- [ ] Custo esperado zero.
- [ ] AccessDenied não virou zero.
- [ ] Nenhum dado sensível foi copiado.
- [ ] Contagens foram repetidas.

## 8. Cleanup

1. Nenhum recurso AWS deveria ter sido criado.
2. Feche assistentes de criação.
3. Não exclua recursos preexistentes.
4. Repita todas as contagens.
5. Investigue diferença sem excluir por contagem.
6. Remova apenas rascunhos locais desnecessários.
7. Encerre a autenticação pela mesma rota.
8. Confirme custo esperado zero.
9. Registre limitações.
10. Marque cleanup concluído.

### Checklist de cleanup

- [ ] Nenhum recurso criado.
- [ ] Preexistentes preservados.
- [ ] Inventário final validado.
- [ ] Sessão encerrada.

## 9. Tratamento de falhas

- AccessDenied significa não verificado.
- Region errada exige voltar.
- Recurso preexistente não deve ser alterado.
- Contagem externa mudou: registre.
- Login expirado: renove pela mesma rota.
- Preço indisponível: permaneça read-only.
- Dúvida de propriedade: não exclua.
- Timeout: preserve cleanup antes da teoria.

## 10. Evidência permitida

Registre Region, modo, contagens, decisões, custo e cleanup.

Não registre:
- account ID ou ARN.
- access key, secret ou token.
- IDs, IPs e nomes preexistentes.
- conteúdo de dados, logs ou secrets.
- screenshots sensíveis.

## 11. Conexão com o exame

- Desenhar pipeline batch.
- Desenhar pipeline streaming.
- Separar dados e catálogo.
- Relacionar MSK e Flink.
- Selecionar APIs de AI.
- Proteger pontos de ingestão com IAM, resource policy, endpoint privado, TLS e KMS.
- Comparar custo e operação.
- Concluir sem recursos criados.

Justifique a escolha e também as alternativas eliminadas.

## 12. Referências oficiais

- [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html)
- [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)
- [SAA-C03 — tarefa 3.5](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html)
- [Kinesis — IAM e resource policies](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html)
- [Kinesis — interface VPC endpoints](https://docs.aws.amazon.com/streams/latest/dev/vpc.html)
- [Kinesis — server-side encryption](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html)
- [Kinesis — TLS e segurança de infraestrutura](https://docs.aws.amazon.com/streams/latest/dev/infrastructure-security.html)
- [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html)

**Verificado em:** 01/08/2026.
