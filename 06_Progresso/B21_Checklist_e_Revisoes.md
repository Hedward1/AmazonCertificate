# B21 — Checklist e revisões D+2/D+7

**Estudo inicial:** 18/08/2026<br>
**D+2:** 20/08/2026<br>
**D+7:** 25/08/2026<br>
**Conteúdo:** Organizations, IAM avançado, KMS e Parameter Store

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B21](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b21) | 283–300 e Q22 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B21_Organizations_IAM_Avancado_KMS_e_Parameter_Store.md) | explicar objetivos sem consulta | [ ] |
| [Laboratório](../05_Laboratorios/LAB_B21_Avaliacao_de_Politicas_KMS_e_Parameter_Store.md) | executar dentro do custo e validar cleanup | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B21_Questoes.md) | responder 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B21_Gabarito.md) | corrigir A–D e registrar regra | [ ] |
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

## 2. D+2 — 20/08/2026

Não releia antes da primeira tentativa. Use no máximo 12 minutos.

1. Explique por que SCP não concede.
2. Resolva explicit deny.
3. Compare policies IAM.
4. Desenhe cross-account role.
5. Compare Identity Center e Directory Service.
6. Desenhe envelope encryption.
7. Compare tipos de KMS key.
8. Compare Parameter Store e Secrets Manager.

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

## 3. D+7 — 25/08/2026

Resolva em inglês quando possível, sem consultar. Use no máximo 15 minutos.

### Cenário

Uma role com AdministratorAccess em member account precisa descriptografar dados. Um SCP nega a ação, e a aplicação global quer usar material relacionado em duas Regions sem copiar dados automaticamente.

Responda:
1. A chamada é permitida?
2. Por que outro Allow não ajuda?
3. SCP afeta management account?
4. Qual policy controla uso da KMS key?
5. O que envelope encryption cifra diretamente?
6. Que recurso atende duas Regions?
7. O que não é sincronizado?
8. A chave replica os dados?

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
