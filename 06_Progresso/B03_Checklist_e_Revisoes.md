# B03 — Checklist e revisões D+2/D+7

**Estudo inicial:** 28/07/2026  
**D+2:** 30/07/2026  
**D+7:** 04/08/2026  
**Conteúdo:** acesso ao EC2, SSH, EC2 Instance Connect, Session Manager,
instance roles, IMDSv2 e modelos de compra

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| Aulas 36–46 | concluir as aulas e acelerar apenas a repetição de sistema operacional | [ ] |
| Quiz da seção 5 | fazer na Udemy e registrar somente resultado e erros | [ ] |
| [Capítulo B03](../03_Guia_do_Estudante/Capitulos/B03_Conexao_EC2_Roles_e_Modelos_de_Compra.md) | explicar os dez objetivos sem consulta | [ ] |
| [Laboratório B03](../05_Laboratorios/LAB_B03_EC2_Web_Role_e_Cleanup.md) | lançar uma instância, validar e provar o cleanup | [ ] |
| [Questões B03](../04_Questoes_e_Revisoes/Blocos/B03_Questoes.md) | responder as 10 antes de abrir o gabarito | [ ] |
| Correção | justificar por que cada alternativa está certa ou errada | [ ] |
| Caderno de Erros | registrar erros e acertos de baixa confiança | [ ] |
| Auditoria de custos | confirmar instância, volume, SG, role e IP removidos | [ ] |

### Resultado inicial

- **Quiz da Udemy:** ____%
- **Questões autorais:** ____ / 10
- **Respostas com confiança baixa:** ____
- **Tempo das questões:** ____ minutos
- **Laboratório concluído:** sim / não / somente diagrama
- **Custo ou crédito observado:** USD ____
- **Tópico mais fraco:**
- **Regra que preciso recuperar:**

### Evidência mínima de cleanup

Marque somente depois de conferir:

- [ ] zero instâncias B03 ativas;
- [ ] root volume B03 excluído;
- [ ] nenhum snapshot ou AMI criado;
- [ ] nenhum Elastic IP criado;
- [ ] public IPv4 automático liberado;
- [ ] security group B03 excluído;
- [ ] role e instance profile B03 excluídos;
- [ ] EC2 Global View verificado.

## 2. D+2 — 30/07/2026

Não releia o capítulo antes da tentativa. Use no máximo 10 minutos.

1. Explique por que IAM, security group, rota, usuário da AMI e key pair
   resolvem camadas diferentes do acesso.
2. Crie uma sequência de diagnóstico para um timeout de SSH.
3. O que EC2 Instance Connect envia, por quanto tempo e de que caminho de rede
   ainda depende?
4. Quais pré-requisitos permitem usar Session Manager sem inbound 22?
5. Desenhe a cadeia trust policy → role → instance profile → IMDSv2 →
   credencial temporária.
6. Compare On-Demand, Compute Savings Plans e Reserved Instances por
   compromisso e flexibilidade.
7. Dê quatro características de um workload adequado para Spot e duas boas
   práticas contra interrupções.
8. Quando a resposta é Dedicated Host, Dedicated Instance ou Capacity
   Reservation?

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
- **Cleanup ainda confirmado:** sim / não

## 3. D+7 — 04/08/2026

Resolva o cenário sem consultar. Use no máximo 12 minutos.

### Cenário

A company has three requirements:

1. Administrators need an interactive shell on private EC2 instances. The
   security team prohibits inbound administrative ports and shared SSH keys.
2. A stable compute baseline can be committed for three years, but workloads
   may move across EC2 families, Regions, Fargate, and Lambda.
3. Additional batch workers are stateless, checkpoint their progress, and can
   be interrupted.

The company also owns a legacy license tied to physical sockets and cores for
one separate workload.

Responda:

1. Qual método de administração atende ao primeiro requisito?
2. Quais dependências esse método possui mesmo sem inbound rules?
3. Qual opção de desconto atende ao segundo requisito?
4. Por que EC2 Instance Savings Plan e Regional RI são menos flexíveis nesse
   cenário?
5. Qual opção atende aos batch workers?
6. Como distribuir a capacidade para reduzir dependência de um único Spot
   capacity pool?
7. Qual sinal deve ser tratado antes de uma interrupção Spot, e quanto tempo o
   aviso normalmente oferece?
8. Qual tenancy atende à licença e por que Dedicated Instance não basta?

### Registro D+7

- **Itens corretos sem consulta:** ____ / 8
- **Tempo:** ____ minutos
- **Confiança:** alta / média / baixa
- **Palavras em inglês que atrasaram a leitura:**
- **Ainda confundo:**
- **Próxima ação:**

## 4. Critério de encerramento do B03

O bloco pode ser marcado como consolidado quando:

- as questões autorais atingirem pelo menos 8/10;
- o D+2 atingir pelo menos 7/8;
- o D+7 atingir pelo menos 7/8;
- não houver erro aberto sobre SSH público, EIC versus Session Manager,
  instance role ou IMDSv2;
- você diferenciar desconto, interrupção, isolamento e reserva de capacidade;
- o cleanup do LAB B03 estiver integralmente confirmado.

Se falhar, revise somente a seção correspondente, atualize o Caderno de Erros e
repita as questões erradas depois de 24 horas. Não relance uma instância apenas
para repetir teoria; use o diagrama do laboratório até existir uma necessidade
prática específica.
