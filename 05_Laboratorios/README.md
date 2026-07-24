# 05 - Laboratórios

Cada laboratório deve informar objetivo, custo estimado, validação e cleanup.

Regras de segurança:

- nunca criar access key para o usuário root;
- usar MFA e privilégio mínimo;
- confirmar a Region antes de criar recursos;
- definir um teto mensal no AWS Budgets antes de laboratórios cobrados;
- encerrar ou excluir todos os recursos indicados no cleanup;
- conferir o console de faturamento após as práticas.

O teto numérico do orçamento mensal ainda precisa ser definido pelo estudante.

## Laboratórios disponíveis

- [LAB B01 — Segurança da conta, orçamento e acesso temporário](LAB_B01_Seguranca_da_Conta_IAM.md)
- [LAB B02 — AWS CLI, roles e auditoria IAM](LAB_B02_CLI_Roles_e_Auditoria_IAM.md)
- [LAB B03 — Primeira instância EC2, website e cleanup](LAB_B03_EC2_Web_Role_e_Cleanup.md)
- [LAB B04 — Inventário read-only de EC2, ENI, EBS e AMI](LAB_B04_Inventario_EC2_ENI_EBS_e_AMI.md)
