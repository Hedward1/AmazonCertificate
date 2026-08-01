# LAB B11 — S3 versioning, lifecycle e cleanup completo

**Tempo:** 35 minutos<br>
**Aulas:** 128–149<br>
**Capítulo:** [B11](../03_Guia_do_Estudante/Capitulos/B11_S3_Seguranca_Versioning_Replication_Classes_e_Eventos.md)<br>
**Modo:** criação controlada de um bucket e objetos pequenos<br>
**Custo esperado:** centavos ou menos; validar preço vigente antes de começar

## 1. Resultado esperado

Ao terminar, você deverá ter:

- criado bucket general purpose privado com tags;
- confirmado Block Public Access e Object Ownership;
- habilitado versioning;
- criado duas versões da mesma key e um delete marker;
- recuperado a versão anterior removendo o marker correto;
- configurado lifecycle para noncurrent versions e multipart incompleto;
- desenhado replication e event notification sem criá-los;
- removido todas as versões/markers e o bucket;
- confirmado zero recurso B11.

## 2. Conexão com o exame

| Evidência | Tarefa |
|---|---|
| policy/BPA/ownership | 1.1 / 1.3 |
| versioning/replication | 2.2 |
| storage/performance/event | 3.1 / 3.5 |
| lifecycle/classes/cleanup | 4.1 |

## 3. Preflight obrigatório (5 min)

- [ ] identidade não root e Region confirmadas;
- [ ] orçamento/alerta ativo;
- [ ] [preço S3](https://aws.amazon.com/s3/pricing/) consultado;
- [ ] nome sem account ID/dado pessoal: use o padrão
  `saa-b11-data-<sufixo-aleatorio>`, substituindo o placeholder e sem digitar
  os caracteres `<` e `>`;
- [ ] tags `Project=SAAC03`, `Lab=B11` e `Expires=AAAA-MM-DD`, substituindo
  `AAAA-MM-DD` pela data planejada para o cleanup (preferencialmente o mesmo dia);
- [ ] inventário inicial de buckets B11;
- [ ] dois arquivos locais de texto sem segredo, menores que 1 KB;
- [ ] nenhum domínio, policy pública ou website será criado;
- [ ] autorização para excluir somente o bucket novo confirmada.

Se qualquer tela indicar opção paga inesperada ou ownership ambíguo, pare e faça
o laboratório em diagrama.

## 4. Criar bucket seguro (5 min)

No console S3:

1. crie general purpose bucket na Region escolhida;
2. mantenha os quatro Block Public Access habilitados;
3. mantenha Object Ownership `Bucket owner enforced`;
4. habilite default encryption oferecida pela configuração segura vigente;
5. não habilite website, replication, Transfer Acceleration ou Object Lock;
6. aplique tags B11;
7. abra Permissions e confirme `Not public`.

Registre somente Region, BPA sim/não, versioning e contagem de objects. Não copie
nome completo do bucket para material público.

## 5. Versioning e delete marker (10 min)

1. Habilite versioning.
2. Envie `lab/evidencia.txt` com conteúdo `versao-1`.
3. Envie a mesma key com conteúdo `versao-2`.
4. Ative **Show versions** e confirme duas version IDs.
5. Exclua a key sem escolher version ID; confirme criação de delete marker.
6. Faça GET/list normal e observe que a key parece excluída.
7. Com Show versions, exclua **somente o delete marker** criado.
8. Confirme que `versao-2` volta a ser current.
9. Não exclua permanentemente uma versão antes de registrar a diferença.

Tabela:

| Etapa | Current | Versões | Delete markers |
|---|---|---:|---:|
| primeiro upload | v1 | 1 | 0 |
| overwrite | v2 | 2 | 0 |
| delete comum | marker | 2 | 1 |
| remove marker | v2 | 2 | 0 |

## 6. Lifecycle configurado, não aguardado (5 min)

Crie regra `b11-cleanup-learning` limitada ao prefixo `lab/`, que contém o
objeto deste laboratório:

- expire current objects após período didático coerente;
- delete noncurrent versions após período posterior;
- delete expired object delete markers quando compatível;
- abort incomplete multipart uploads após sete dias;
- não selecione transição com minimum duration que gere cobrança desnecessária.

O laboratório termina hoje, portanto a regra não será executada. Leia a
configuração salva e explique por que somente expirar current versions não
elimina storage de noncurrent versions.

## 7. Diagramas de replication e evento (3 min)

Sem criar recursos:

```text
source versioned ── CRR role/KMS ──> destination versioned

S3 ObjectCreated: incoming/* → SQS → idempotent worker → processed/*
                                  └→ DLQ
```

Anote: objetos antigos exigem Batch Replication; filter evita loop; duplicação
de evento exige idempotência.

## 8. Validação (2 min)

- [ ] bucket permanece privado;
- [ ] version IDs e marker observados;
- [ ] remoção do marker restaurou current;
- [ ] lifecycle cobre noncurrent/multipart;
- [ ] nenhum recurso de replication/event criado;
- [ ] nenhum arquivo contém segredo.

## 9. Cleanup version-aware (5 min)

1. Desative/remova event/lifecycle/replication de B11 se algo foi criado.
2. Abra **Empty bucket** e confirme o nome exigido pelo console.
3. Certifique-se de que a operação remove **todas as object versions e delete
   markers**, não apenas current keys.
4. Ative Show versions e confirme lista vazia.
5. Exclua o bucket B11 vazio.
6. Consulte a lista de buckets e confirme ausência.
7. Registre contagens, não IDs.

**Parada de segurança:** não use comando recursivo contra nome variável ou
bucket que não tenha tag/ownership B11. Se o console mostrar objects inesperados,
não prossiga.

## 10. Evidência final

| Controle | Resultado esperado |
|---|---|
| BPA | habilitado durante toda a prática |
| versions criadas | 2 |
| marker observado | sim |
| lifecycle lido | sim |
| replication/event provisionados | não |
| versões/markers finais | 0 |
| buckets B11 finais | 0 |

## 11. Solução de problemas

| Sintoma | Verificação segura |
|---|---|
| bucket não exclui | versions/delete markers/multipart |
| objeto continua após delete | Show versions e marker |
| AccessDenied | IAM, bucket policy, BPA, KMS e ownership; não abrir público |
| lifecycle não agiu | tempo de avaliação, filtro e elegibilidade |
| replication pending/fails | role, versioning, KMS e destination policy |
| evento duplica | comportamento at-least-once; idempotência |

## 12. Referências oficiais

- [Creating a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)
- [Blocking public access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)
- [Versioning workflows](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html)
- [Deleting object versions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)
- [Lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html)
- [Emptying a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/empty-bucket.html)
