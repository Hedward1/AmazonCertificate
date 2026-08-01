# B25 — Checklist e revisões D+2/D+7

**Estudo inicial:** 22/08/2026<br>
**D+2:** 24/08/2026<br>
**D+7:** 29/08/2026<br>
**Conteúdo:** CloudFormation, operações, custos e Well-Architected

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B25](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b25) | 367–385 e 387–388; consultar 386/389–393; pular 394–396; não abrir practice exam | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B25_CloudFormation_Operacoes_Custos_e_Well_Architected.md) | explicar objetivos sem consulta | [ ] |
| [Laboratório](../05_Laboratorios/LAB_B25_Auditoria_Final_de_Custos_e_Cleanup.md) | executar dentro do custo e validar cleanup | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B25_Questoes.md) | responder 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B25_Gabarito.md) | corrigir A–D e registrar regra | [ ] |
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

## 2. D+2 — 24/08/2026

Não releia antes da primeira tentativa. Use no máximo 12 minutos.

1. Explique stack e template.
2. Explique change set.
3. Explique drift.
4. Explique service role e PassRole.
5. Compare Session Manager e bastion.
6. Associe serviços complementares.
7. Compare ferramentas de custo.
8. Recite os seis pilares.

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

## 3. D+7 — 29/08/2026

Resolva em inglês quando possível, sem consultar. Use no máximo 15 minutos.

### Cenário

Uma stack será atualizada e pode substituir banco. Instâncias privadas precisam de administração sem SSH. Um gasto incomum apareceu e alguns recursos podem ter DeletionPolicy Retain.

Responda:
1. Como revisar update?
2. Change set garante segurança?
3. Como administrar instâncias?
4. Que pré-requisitos existem?
5. Qual detecta anomalia?
6. Qual detalha custos?
7. Retain faz o quê?
8. O practice exam deve ser aberto?

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
