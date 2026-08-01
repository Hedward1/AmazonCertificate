# B19 — Checklist e revisões D+2/D+7

**Estudo inicial:** 15/08/2026<br>
**D+2:** 17/08/2026<br>
**D+7:** 22/08/2026<br>
**Conteúdo:** analytics, streaming e serviços gerenciados de AI/ML

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B19](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b19) | 245–260 e 262–263; pular 261; Q19–Q20 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B19_Analytics_Streaming_e_Machine_Learning.md) | explicar objetivos sem consulta | [ ] |
| [Laboratório](../05_Laboratorios/LAB_B19_Pipeline_Analytics_e_ML_Read_Only.md) | executar dentro do custo e validar cleanup | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B19_Questoes.md) | responder 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B19_Gabarito.md) | corrigir A–D e registrar regra | [ ] |
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

## 2. D+2 — 17/08/2026

Não releia antes da primeira tentativa. Use no máximo 12 minutos.

1. Desenhe pipeline S3, Glue, Athena e Amazon Quick Sight.
2. Compare Athena e Redshift.
3. Explique crawler, catálogo, job e Lake Formation.
4. Compare batch e streaming.
5. Explique MSK e Flink.
6. Associe Transcribe, Polly, Textract e Rekognition.
7. Quando usar SageMaker AI?
8. Por que Personalize não entra?

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

## 3. D+7 — 22/08/2026

Resolva em inglês quando possível, sem consultar. Use no máximo 15 minutos.

### Cenário

A empresa recebe eventos Kafka e formulários digitalizados. Precisa calcular agregações stateful em cinco minutos, arquivar resultados no S3, consultar histórico ocasionalmente e extrair tabelas dos formulários sem treinar modelo.

Responda:
1. Qual serviço mantém Kafka gerenciado?
2. Qual processa janelas stateful?
3. Qual serviço arquiva objetos?
4. Qual consulta SQL ad hoc?
5. Qual extrai tabelas de documentos?
6. Onde guardar metadados?
7. Como reduzir bytes do Athena?
8. Qual serviço foi deliberadamente excluído?

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
