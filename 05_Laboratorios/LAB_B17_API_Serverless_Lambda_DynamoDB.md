# LAB B17 — Mini-API com Lambda, API Gateway e DynamoDB

**Timebox:** 40 minutos<br>
**Modo:** console AWS; recursos descartáveis<br>
**Custo esperado:** muito baixo/Free Tier elegível; confira preços e budget<br>
**Objetivo:** criar `GET /items/{id}` sobre Lambda e DynamoDB e limpar tudo<br>
**Capítulo:** [B17 — Serverless](../03_Guia_do_Estudante/Capitulos/B17_Serverless_VPC_DynamoDB_API_Gateway_Step_Functions_e_Cognito.md)

## 1. Arquitetura

```text
cliente -> API Gateway HTTP API -> Lambda -> DynamoDB on-demand
                                      |
                                      +-> CloudWatch Logs
```

Sem VPC, NAT, Cognito ou Step Functions neste timebox. A API usa somente item de
teste e será excluída.

## 2. Preflight — 4 min

- [ ] Identidade não root e Region confirmadas.
- [ ] Budget/alerta de cobrança confirmado.
- [ ] Permissões para DynamoDB, Lambda, IAM, API Gateway e Logs validadas.
- [ ] Inventário inicial de APIs/functions/tables/log groups/roles registrado.
- [ ] Nenhum dado real ou secret será usado.

```text
Region: __________
HTTP APIs b17: ____
Functions b17: ____
Tables b17: ____
Roles b17: ____
```

## 3. Tabela DynamoDB — 5 min

1. Crie table `b17-items-20260813`.
2. Partition key: `id` (String); sem sort key.
3. Capacity mode: **On-demand**.
4. Não crie GSI, global table, DAX ou backup adicional.
5. Crie item:

```json
{"id":"demo-1","name":"study-item","status":"READY"}
```

Confirme encryption padrão e que a table está `ACTIVE`.

## 4. Função Lambda — 8 min

1. Crie `b17-get-item-20260813` com runtime Python suportado.
2. Crie basic execution role.
3. Adicione policy mínima: `dynamodb:GetItem` apenas na table B17.
4. Adicione environment variable `TABLE_NAME=b17-items-20260813`.
5. Não coloque função em VPC e não crie Function URL.

Código:

```python
import json
import os
import boto3

table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    item_id = event.get("pathParameters", {}).get("id")
    if not item_id:
        return {"statusCode": 400, "body": json.dumps({"error": "missing id"})}
    response = table.get_item(Key={"id": item_id})
    item = response.get("Item")
    return {
        "statusCode": 200 if item else 404,
        "headers": {"content-type": "application/json"},
        "body": json.dumps(item or {"error": "not found"})
    }
```

Teste diretamente com:

```json
{"pathParameters":{"id":"demo-1"}}
```

Resultado esperado: 200 e o item; teste `missing` e espere 404.

## 5. HTTP API — 8 min

1. API Gateway → **Build HTTP API**.
2. Nome `b17-items-api-20260813`.
3. Integration: função `b17-get-item-20260813`.
4. Route: `GET /items/{id}`.
5. Stage: `$default`, auto-deploy habilitado.
6. Não configure CORS: não há browser neste teste.
7. Não adicione autorização à API pública descartável; não use payload real.

Abra somente:

```text
https://API-ID.execute-api.REGION.amazonaws.com/items/demo-1
```

Espere 200. Para `/items/missing`, espere 404. Não registre API ID neste repo.

## 6. Validação técnica — 4 min

- [ ] `demo-1` retorna 200 e JSON.
- [ ] `missing` retorna 404.
- [ ] método diferente não corresponde à route.
- [ ] CloudWatch Logs registra invocação sem dados sensíveis.
- [ ] role permite GetItem somente na table.
- [ ] table usa on-demand e não tem indexes extras.

Explique por que API key não autenticaria um usuário e o que Cognito/JWT mudaria
em uma API de produção.

## 7. Falhas dirigidas — 3 min

Sem salvar mudanças, responda:

```text
Remover GetItem da role -> erro esperado: ____________________
Nome de table incorreto -> erro esperado: ____________________
Lambda em public subnet sem NAT -> internet? _________________
1000 invokes concorrentes + DB frágil -> controle: ___________
```

Não execute negações IAM no timebox.

## 8. Segurança e custos — 2 min

- [ ] API descartável contém somente item fictício.
- [ ] Sem access keys no código.
- [ ] Sem `dynamodb:*` em `Resource: *`.
- [ ] Sem NAT, VPC endpoints, DAX, global tables ou cache API.
- [ ] Logs serão excluídos.

## 9. Cleanup obrigatório — 6 min

1. Delete HTTP API, routes e stage.
2. Delete função Lambda.
3. Delete table DynamoDB; confirme que nenhum backup foi criado.
4. Delete o log group `/aws/lambda/b17-get-item-20260813`.
5. Delete a role/policy exclusivas após confirmar que não são compartilhadas.
6. Compare inventário final com inicial.

```text
APIs B17: zero / investigar
Functions B17: zero / investigar
Tables/backups B17: zero / investigar
Log groups B17: zero / investigar
Roles B17: zero / investigar
```

## Resultado esperado

Uma request percorreu API→Lambda→DynamoDB, retornou 200/404, foi observada em
logs e todos os recursos foram removidos.

## Conexão com o exame

O fluxo treina: HTTP API para requisitos simples; execution role para acesso do
código; on-demand para tráfego imprevisível; key lookup em vez de Scan; logs e
throttling como controles operacionais. Em produção, auth, WAF, backups e IaC
seriam decisões explícitas.

## Referências oficiais

- [Tutorial HTTP API + Lambda + DynamoDB](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html)
- [Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)
- [DynamoDB GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html)
