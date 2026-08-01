# B17 — Checklist e revisões D+2/D+7

**Estudo inicial:** 13/08/2026<br>
**D+2:** 15/08/2026<br>
**D+7:** 20/08/2026<br>
**Conteúdo:** Lambda VPC, DynamoDB, API Gateway, Step Functions e Cognito

## 1. Conclusão inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b17) | 217–225 e Q16 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B17_Serverless_VPC_DynamoDB_API_Gateway_Step_Functions_e_Cognito.md) | decisões sem consulta | [ ] |
| [LAB](../05_Laboratorios/LAB_B17_API_Serverless_Lambda_DynamoDB.md) | API 200/404 e cleanup | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B17_Questoes.md) | 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B17_Gabarito.md) | justificar A–D | [ ] |
| Caderno de Erros | erro e baixa confiança | [ ] |

- **Q16:** ____%
- **Questões:** ____ / 10
- **API 200/404:** sim / não
- **Cleanup:** completo / investigar
- **Tópico mais fraco:**

### Evidência

- [ ] rede de Lambda na VPC desenhada;
- [ ] RDS events diferenciados de CDC;
- [ ] access patterns/chaves DynamoDB definidos;
- [ ] GSI/LSI e capacity comparados;
- [ ] API types e auth comparados;
- [ ] Step Functions explicado;
- [ ] User/Identity Pools diferenciados;
- [ ] API/function/table/log/role removidos.

## 2. D+2 — 15/08/2026

1. Desenhe Lambda→RDS privado e internet.
2. Modele PK/SK para clientes/pedidos.
3. Compare on-demand/provisioned e GSI/LSI.
4. Compare HTTP/REST/WebSocket API.
5. Desenhe Retry/Catch de Step Functions.
6. Compare User Pool e Identity Pool.

| Item | Correto? | Confiança | Correção |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

**Resultado:** ____ / 6

## 3. D+7 — 20/08/2026

Uma API mobile usa usuários federados, acesso direto a S3, Lambda, banco privado
e carrinho DynamoDB global. O pedido tem quatro etapas com compensação.

1. User Pool ou Identity Pool para login?
2. Qual fornece AWS credentials temporárias?
3. Como a função alcança banco e internet?
4. Como escolher PK do carrinho?
5. Quando global tables se justificam?
6. HTTP ou REST API para API simples?
7. Serviço de orchestration?
8. Quais recursos do LAB devem estar ausentes?

- **Corretos:** ____ / 8
- **Tempo:** ____ min
- **Confiança:** alta / média / baixa
- **Próxima ação:**

## 4. Critério de encerramento

- questões ≥ 8/10;
- D+2 ≥ 5/6 e D+7 ≥ 7/8;
- acesso/rede/modelagem escolhidos por requisito;
- API e identity components não confundidos;
- zero recursos B17 residuais.
