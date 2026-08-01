# B16 — Checklist e revisões D+2/D+7

**Estudo inicial:** 12/08/2026<br>
**D+2:** 14/08/2026<br>
**D+7:** 19/08/2026<br>
**Conteúdo:** ECR, EKS, Lambda, concurrency, SnapStart e edge

## 1. Conclusão inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b16) | 203–216 e Q15 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B16_ECR_EKS_Lambda_Concurrency_SnapStart_e_Edge.md) | explicar decisões sem consulta | [ ] |
| [LAB](../05_Laboratorios/LAB_B16_Lambda_Minima_Logs_e_Cleanup.md) | executar, observar e limpar | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B16_Questoes.md) | 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B16_Gabarito.md) | justificar A–D | [ ] |
| Correção | justificar A–D | [ ] |
| Caderno de Erros | erro/baixa confiança | [ ] |

- **Q15:** ____%
- **Questões:** ____ / 10
- **Tempo:** ____ min
- **Função executou:** sim / não
- **Cleanup completo:** sim / não
- **Regra mais fraca:**

### Evidência

- [ ] ECR tag/digest/lifecycle explicados;
- [ ] ECS/Fargate e EKS diferenciados;
- [ ] timeout de 15 min da função padrão diferenciado de Durable Functions e MicroVMs;
- [ ] concurrency calculada;
- [ ] reserved/provisioned diferenciadas;
- [ ] SnapStart explicado sem prometer suporte universal;
- [ ] edge functions comparadas;
- [ ] function, log group e role removidos.

## 2. D+2 — 14/08/2026

Sem consulta:

1. Compare ECS/Fargate, EKS e Lambda.
2. Explique tag mutável versus digest.
3. Calcule concurrency para três taxas/durações.
4. Compare reserved, provisioned e maximum concurrency.
5. Explique cold start e SnapStart.
6. Compare Lambda@Edge e CloudFront Functions.

| Item | Correto? | Confiança | Correção |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

**Resultado:** ____ / 6

## 3. D+7 — 19/08/2026

Uma API tem funções de 500 ms, picos de 400 req/s e banco limitado a 100
conexões. Outra rotina leva 30 min. A empresa usa containers e Kubernetes apenas
em um produto; redirects simples rodam no edge.

1. Concurrency aproximada da API?
2. Como proteger o banco?
3. Como reduzir cold start previsivelmente?
4. Onde executar a rotina de 30 min?
5. Qual serviço para containers sem Kubernetes?
6. Qual serviço para o produto Kubernetes?
7. Onde executar redirect simples?
8. Quais resíduos do LAB Lambda remover?

- **Corretos:** ____ / 8
- **Tempo:** ____ min
- **Confiança:** alta / média / baixa
- **Próxima ação:**

## 4. Critério de encerramento

- questões ≥ 8/10;
- D+2 ≥ 5/6 e D+7 ≥ 7/8;
- compute escolhido por duração, packaging e orquestração;
- concurrency/cold start explicados sem consulta;
- cleanup confirmado no inventário.
