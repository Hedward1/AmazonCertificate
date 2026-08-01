# B23 — Checklist e revisões D+2/D+7

**Estudo inicial:** 20/08/2026<br>
**D+2:** 22/08/2026<br>
**D+7:** 27/08/2026<br>
**Conteúdo:** redes avançadas, endpoints, híbrido e IPv6

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B23](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b23) | 327–345; Q24 somente no B24 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B23_Redes_Avancadas_e_Conectividade_Hibrida.md) | explicar objetivos sem consulta | [ ] |
| [Laboratório](../05_Laboratorios/LAB_B23_Roteamento_VPC_e_Hibrido_em_Diagrama.md) | executar dentro do custo e validar cleanup | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B23_Questoes.md) | responder 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B23_Gabarito.md) | corrigir A–D e registrar regra | [ ] |
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

## 2. D+2 — 22/08/2026

Não releia antes da primeira tentativa. Use no máximo 12 minutos.

1. Explique peering não transitivo.
2. Compare endpoints.
3. Compare Flow Logs e Mirroring.
4. Compare VPN e Direct Connect.
5. Desenhe DX com VPN.
6. Explique Transit Gateway.
7. Explique dual-stack.
8. Explique egress-only IGW.

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

## 3. D+7 — 27/08/2026

Resolva em inglês quando possível, sem consultar. Use no máximo 15 minutos.

### Cenário

Quarenta VPCs precisam de hub transitivo e acesso privado a S3. O datacenter exige link dedicado com IPsec. Subnets IPv6 privadas só podem iniciar conexões.

Responda:
1. Qual hub usar?
2. Qual endpoint para S3?
3. Ele cobra por hora?
4. Qual conexão dedicada?
5. Como adicionar IPsec?
6. Qual recurso de saída IPv6?
7. Flow Logs captura payload?
8. Peering atenderia trânsito?

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
