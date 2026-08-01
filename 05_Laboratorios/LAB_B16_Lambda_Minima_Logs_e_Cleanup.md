# LAB B16 — Lambda mínima, logs e cleanup

**Timebox:** 45 minutos<br>
**Modo:** console AWS<br>
**Custo esperado:** desprezível para poucas invocações; valide preço e budget<br>
**Objetivo:** criar uma função mínima, observar logs/metrics/role e remover tudo

**Capítulo:** [B16 — Lambda, EKS e edge](../03_Guia_do_Estudante/Capitulos/B16_ECR_EKS_Lambda_Concurrency_SnapStart_e_Edge.md)

## 1. Limites do exercício

- Não criar cluster EKS nem ECR repository.
- Não colocar a função em VPC.
- Não criar provisioned concurrency, Function URL ou API Gateway.
- Não usar dados reais, secrets ou identificadores da conta em logs.
- Não anexar policies administrativas à execution role.

## 2. Preflight — 5 min

- [ ] Acessar com identidade não root.
- [ ] Selecionar uma Region com Lambda disponível.
- [ ] Confirmar budget/alerta de cobrança.
- [ ] Registrar quantidade inicial de functions, log groups e roles `b16-*`.
- [ ] Ter permissão para criar e excluir Lambda, role e log group.

```text
Region: __________
Functions b16 antes: ____
Log groups b16 antes: ____
Roles b16 antes: ____
```

Se não houver permissão de IAM, peça uma role de laboratório pré-aprovada ou
faça o fluxo em diagrama. Não conceda `AdministratorAccess` para contornar.

## 3. Crie a função — 7 min

1. Abra Lambda → **Create function** → **Author from scratch**.
2. Nome: `b16-minimal-20260812`.
3. Runtime: versão Python atualmente suportada exibida no console.
4. Architecture: `x86_64` ou `arm64`; registre a escolha.
5. Permissions: crie uma role com basic Lambda permissions.
6. Não habilite VPC, URL, tags sensíveis ou triggers.
7. Crie a função e anote apenas o nome, nunca account ID/ARN.

Resultado esperado: função `Active`, role com policy de logs e nenhum trigger.

## 4. Código e primeira invocação — 6 min

Use:

```python
import json
import os

def lambda_handler(event, context):
    request_id_suffix = context.aws_request_id[-6:]
    print(json.dumps({"level": "INFO", "lab": "B16", "request": request_id_suffix}))
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "ok", "input": event.get("action", "none")})
    }
```

Faça **Deploy**. Crie test event privado:

```json
{"action":"health-check"}
```

Execute uma vez. Confirme `statusCode=200`, `message=ok` e que nenhum dado
sensível foi logado.

## 5. Execution role — 5 min

Em **Configuration → Permissions**:

1. abra a role criada;
2. confirme somente a policy básica de CloudWatch Logs;
3. identifique as ações de criar stream e publicar log;
4. explique por que a função não precisa `s3:*` ou `dynamodb:*`;
5. não edite a trust policy.

```text
Role serve ao código para: __________________________
Resource policy serviria para: ______________________
Permissão extra necessária neste LAB: nenhuma / investigar
```

## 6. Logs e métricas — 6 min

1. Abra **Monitor → View CloudWatch logs**.
2. Localize o log group `/aws/lambda/b16-minimal-20260812`.
3. Encontre `START`, linha JSON, `END` e `REPORT`.
4. Registre duration e max memory used sem copiar request ID completo.
5. Volte às métricas e identifique Invocations, Errors, Duration e Throttles.
6. Configure mentalmente um alarm, mas não o crie neste timebox.

```text
Invocations observadas: ____
Errors: ____
Duration aproximada: ____ ms
Max memory used: ____ MB
```

## 7. Memory, timeout e concurrency — 5 min

Sem salvar mudanças desnecessárias, inspecione:

- memory configurada e seu vínculo com CPU;
- timeout configurado e máximo de 15 minutos para esta Lambda Function padrão;
- ephemeral storage;
- reserved concurrency;
- async destinations/dead-letter configuration.

Calcule:

```text
taxa = 50 requests/s
duração média = 0,4 s
concurrency aproximada = ______
```

Explique por que reserved concurrency de 10 causaria throttling e por que
provisioned concurrency não é a ferramenta para limitar conexões de banco.

## 8. Comparação somente em diagrama — 3 min

```text
redirect/header simples no viewer -> CloudFront Functions
auth avançada + chamada externa    -> Lambda@Edge
Kubernetes obrigatório             -> EKS
container longo sem hosts          -> ECS/Fargate
evento curto e stateless           -> Lambda
```

Não abra ou crie distributions/clusters.

## 9. Cleanup obrigatório — 5 min

1. Delete a função `b16-minimal-20260812`.
2. No CloudWatch Logs, delete o log group correspondente.
3. Em IAM, confirme que a role é exclusiva; detach/delete a policy inline se
   necessário e delete a role.
4. Confirme que não existem versions/aliases, triggers ou ENIs.
5. Compare inventário final com inicial.

```text
Function removida: sim / não
Log group removido: sim / não
Role exclusiva removida: sim / não
Triggers/URLs/ENIs: zero / investigar
```

## 10. Validação e resultado esperado

- [ ] função executou e retornou JSON;
- [ ] log estruturado foi encontrado;
- [ ] role mínima foi inspecionada;
- [ ] quatro métricas foram identificadas;
- [ ] concurrency foi calculada;
- [ ] nenhuma informação sensível apareceu;
- [ ] função, log group e role foram removidos.

## Conexão com o exame

O laboratório liga *application permission* à execution role, *can run again* à
idempotência, *database connection limit* a reserved/max concurrency e buffer,
e *consistent low cold-start latency* a provisioned concurrency ou SnapStart
compatível. Sempre verifique timeout e cleanup de logs.

## Referências oficiais

- [Criar função no console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
- [Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)
- [CloudWatch Logs para Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html)
- [Lambda concurrency](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html)
