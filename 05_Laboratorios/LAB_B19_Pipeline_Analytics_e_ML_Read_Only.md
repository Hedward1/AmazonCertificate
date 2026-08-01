# LAB B19 — Pipeline de analytics e seleção de AI/ML

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
6. Registrar controles de segurança.
7. Comparar custo e operação.
8. Concluir sem recursos criados.

## 2. Resultado esperado

- Diagrama batch completo.
- Diagrama streaming completo.
- Matriz AI com dez casos.
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
- Amazon Quick Sight, antigo QuickSight, para visualização.
- Producers para MSK.
- Flink como processador stateful.
- S3 como destino durável.
- Redshift somente se warehouse for requisito.
- IAM, KMS, logs e lifecycle em todas as camadas.

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
8. Adicione Amazon Quick Sight como consumidor.

### Etapa 3 — Streaming

1. Desenhe producers e MSK.
2. Adicione Flink.
3. Defina janela de cinco minutos.
4. Defina estado e checkpoint.
5. Adicione retry.
6. Adicione destino durável.
7. Escreva por que MSK não processa sozinho.
8. Anote alternativa sem Kafka.

### Etapa 4 — AI e segurança

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
- Registrar controles de segurança.
- Comparar custo e operação.
- Concluir sem recursos criados.

Justifique a escolha e também as alternativas eliminadas.

## 12. Referências oficiais

- [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html)
- [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)

**Verificado em:** 01/08/2026.
