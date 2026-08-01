# B20 — Checklist e revisões D+2/D+7

**Estudo inicial:** 17/08/2026<br>
**D+2:** 19/08/2026<br>
**D+7:** 24/08/2026<br>
**Conteúdo:** CloudWatch, EventBridge, CloudTrail, Config e Organizations

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B20](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b20) | 264–282 e Q21 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B20_Observabilidade_Auditoria_Config_e_Organizations.md) | explicar objetivos sem consulta | [ ] |
| [Laboratório](../05_Laboratorios/LAB_B20_CloudWatch_CloudTrail_e_Config_Read_Only.md) | executar dentro do custo e validar cleanup | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B20_Questoes.md) | responder 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B20_Gabarito.md) | corrigir A–D e registrar regra | [ ] |
| Caderno de Erros | registrar erro e baixa confiança | [ ] |
| Auditoria | confirmar custo e recursos residuais | [ ] |

### Resultado inicial

- **Quiz Udemy:** ____%
- **Questões autorais:** ____ / 10
- **Confiança baixa:** ____
- **Tempo:** ____ minutos
- **Laboratório:** concluído / diagrama / incompleto
- **Cleanup:** confirmado / investigar
- **Tópico mais fraco:**
- **Regra a recuperar:**

### Evidência mínima

- [ ] identidade não root;
- [ ] Region confirmada;
- [ ] preflight concluído;
- [ ] resultado esperado validado;
- [ ] custo registrado;
- [ ] recursos preexistentes preservados;
- [ ] cleanup concluído;
- [ ] sessão encerrada.

## 2. D+2 — 19/08/2026

Não releia antes da primeira tentativa. Use no máximo 12 minutos.

1. Compare CloudWatch, CloudTrail e Config.
2. Explique métrica, namespace e dimensão.
3. Por que memória EC2 exige agent?
4. Desenhe bus, rule e target.
5. Compare Event history e trail.
6. Compare management e data events.
7. O que NON_COMPLIANT significa?
8. Desenhe root, OU e accounts.

### Registro D+2

| Item | Correto sem consulta? | Confiança | Correção |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |
| 7 |  |  |  |
| 8 |  |  |  |

- **Resultado:** ____ / 8
- **Erros reabertos:**
- **Próxima ação:**
- **Recurso residual:** nenhum / investigar

## 3. D+7 — 24/08/2026

Resolva em inglês quando possível, sem consultar. Use no máximo 15 minutos.

### Cenário

Uma API apresenta CPU alta. Horas depois, alguém abre um security group. A equipe precisa alertar sobre CPU, identificar o autor da API, reconstruir a configuração e abrir ticket automaticamente.

Responda:
1. Qual serviço mede CPU?
2. Qual componente gera alerta?
3. Qual serviço identifica autor?
4. Qual mostra configuração?
5. Qual roteia evento ao ticket?
6. Memória aparece por padrão?
7. Event history cobre quanto tempo?
8. Config bloqueia mudança por si?

### Registro D+7

- **Corretos sem consulta:** ____ / 8
- **Tempo:** ____ minutos
- **Confiança:** alta / média / baixa
- **Palavras em inglês que atrasaram:**
- **Ainda confundo:**
- **Próxima ação:**

## 4. Critério de encerramento

O bloco pode ser marcado como consolidado quando:

- questões autorais atingirem pelo menos 8/10;
- D+2 atingir pelo menos 7/8;
- D+7 atingir pelo menos 7/8;
- nenhum erro crítico permanecer aberto;
- a tabela de decisão for reconstruída sem consulta;
- custos e cleanup forem explicados;
- recursos preexistentes estiverem preservados;
- erros de baixa confiança estiverem no Caderno de Erros.

Se falhar, revise somente a seção correspondente e repita os itens errados após 24 horas.
