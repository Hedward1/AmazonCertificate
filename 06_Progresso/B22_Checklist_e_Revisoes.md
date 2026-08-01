# B22 — Checklist e revisões D+2/D+7

**Estudo inicial:** 19/08/2026<br>
**D+2:** 21/08/2026<br>
**D+7:** 26/08/2026<br>
**Conteúdo:** segredos, proteção de aplicações e fundamentos de VPC

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B22](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b22) | 301–326 e Q23 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B22_Segredos_Protecao_de_Aplicacoes_e_Fundamentos_VPC.md) | explicar objetivos sem consulta | [ ] |
| [Laboratório](../05_Laboratorios/LAB_B22_VPC_Publica_Privada_sem_NAT_Gateway.md) | executar dentro do custo e validar cleanup | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B22_Questoes.md) | responder 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B22_Gabarito.md) | corrigir A–D e registrar regra | [ ] |
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

## 2. D+2 — 21/08/2026

Não releia antes da primeira tentativa. Use no máximo 12 minutos.

1. Compare Secrets Manager e Parameter Store.
2. Compare ACM, KMS e CloudHSM.
3. Posicione WAF e Shield.
4. Compare GuardDuty, Inspector e Macie.
5. Calcule /24 e /28.
6. Explique subnet pública.
7. Desenhe NAT IPv4.
8. Compare SG e NACL.

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

## 3. D+7 — 26/08/2026

Resolva em inglês quando possível, sem consultar. Use no máximo 15 minutos.

### Cenário

Um ALB público atende aplicação privada com senha RDS rotacionada. A aplicação precisa de saída IPv4, proteção contra SQL injection e descoberta de PII no S3.

Responda:
1. Onde guardar a senha?
2. Qual certificado para ALB?
3. Qual bloqueia SQL injection?
4. Qual descobre PII?
5. Onde fica NAT Gateway?
6. Qual rota existe na subnet privada?
7. SG é stateful?
8. NACL permite deny?

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
