# B02 — Checklist e revisões D+2/D+7

**Estudo inicial:** 27/07/2026  
**D+2:** 29/07/2026  
**D+7:** 03/08/2026  
**Conteúdo:** AWS CLI, IAM roles e auditoria, Budgets, EC2, user data, instance
types e security groups

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B02](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b02) | executar Windows/CLI; acelerar macOS/Linux; pular CloudShell para a prova | [ ] |
| Quiz da seção 4 | fazer na Udemy e registrar apenas resultado/erros | [ ] |
| [Capítulo B02](../03_Guia_do_Estudante/Capitulos/B02_IAM_Aplicado_CLI_EC2_e_Security_Groups.md) | explicar os dez objetivos sem consulta | [ ] |
| [Laboratório B02](../05_Laboratorios/LAB_B02_CLI_Roles_e_Auditoria_IAM.md) | validar identidade, role e auditoria; concluir logout | [ ] |
| [Questões B02](../04_Questoes_e_Revisoes/Blocos/B02_Questoes.md) | responder as 10 antes do gabarito | [ ] |
| Correção | analisar todas as alternativas | [ ] |
| Caderno de Erros | registrar erros e acertos de baixa confiança | [ ] |
| D+2 do B01 | concluir no arquivo do B01 | [ ] |

### Resultado inicial

- **Quiz da Udemy:** ____%
- **Questões autorais:** ____ / 10
- **Respostas com confiança baixa:** ____
- **Tempo das questões:** ____ minutos
- **Tópico mais fraco:**
- **Regra que preciso recuperar:**

## 2. D+2 — 29/07/2026

Não releia o capítulo antes da tentativa. Use no máximo 10 minutos.

1. Qual comando revela a conta e o ARN usados pela AWS CLI?
2. Explique a diferença entre profile e Region.
3. Compare trust policy, permissions policy e instance profile.
4. Quando se usa `iam:PassRole`, e por que ele deve ser restrito?
5. Qual ferramenta mostra MFA/access keys dos IAM users? Qual ajuda a remover
   permissões sem uso recente?
6. Desenhe os sete componentes básicos do lançamento de uma instância EC2.
7. O que EC2 user data faz por padrão, e o que nunca deve conter?
8. Escreva duas inbound rules: HTTPS público e SSH somente do IP administrativo.

### Registro D+2

| Item | Correto sem consulta? | Confiança | Correção necessária |
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

## 3. D+7 — 03/08/2026

Resolva o cenário sem consultar. Use no máximo 12 minutos.

### Cenário

Um administrador usa access keys permanentes no notebook sem saber qual profile
está ativo. Uma aplicação em EC2 possui outra access key gravada em user data. O
website usa TCP 443, mas o security group também libera SSH de `0.0.0.0/0`. A
empresa acredita que parar a instância garante custo zero.

Responda:

1. Como o administrador pode autenticar a CLI com credencial temporária?
2. Quais comandos deve usar para conferir profile, identidade e Region?
3. Como substituir a access key da aplicação?
4. Qual policy define quem pode assumir a role, e qual define o acesso ao
   recurso?
5. Por que gravar um secret em user data é inseguro?
6. Quais inbound rules atendem ao website e à administração segura?
7. Por que o tráfego de resposta não precisa de regra simétrica?
8. Que custos podem continuar depois de parar a instância?

### Registro D+7

- **Itens corretos sem consulta:** ____ / 8
- **Tempo:** ____ minutos
- **Confiança:** alta / média / baixa
- **Ainda confundo:**
- **Próxima ação:**

## 4. Critério de encerramento do B02

O bloco pode ser marcado como consolidado quando:

- as questões autorais atingirem pelo menos 8/10;
- o D+2 atingir pelo menos 7/8;
- o D+7 atingir pelo menos 7/8;
- não houver erro aberto sobre root/access keys, role/instance profile,
  stateful security groups ou portas administrativas públicas;
- você explicar em voz alta por que `stopped` não significa custo total zero.

Se falhar, revise somente a seção correspondente, execute novamente a validação
segura do laboratório e repita as questões erradas depois de 24 horas.
