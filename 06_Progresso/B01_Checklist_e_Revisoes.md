# B01 — Checklist e revisões D+2/D+7

**Estudo inicial:** 25/07/2026  
**D+2:** 27/07/2026  
**D+7:** 01/08/2026  
**Conteúdo:** infraestrutura global, shared responsibility, segurança da conta e
IAM básico

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B01](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b01) | recuperar ou assistir 8, 10–12 e 14–18; tratar os demais conforme o roteiro | [ ] |
| [Capítulo B01](../03_Guia_do_Estudante/Capitulos/B01_Infraestrutura_Global_Responsabilidade_e_IAM.md) | explicar os oito objetivos sem consulta | [ ] |
| [Laboratório B01](../05_Laboratorios/LAB_B01_Seguranca_da_Conta_IAM.md) | concluir validações e cleanup | [ ] |
| [Questões B01](../04_Questoes_e_Revisoes/Blocos/B01_Questoes.md) | responder as 10 antes de abrir o gabarito | [ ] |
| [Gabarito B01](../04_Questoes_e_Revisoes/Blocos/B01_Gabarito.md) | revisar todas as alternativas | [ ] |
| Caderno de Erros | registrar erros e acertos de baixa confiança | [ ] |

### Resultado inicial

- **Acertos:** ____ / 10
- **Respostas com confiança baixa:** ____
- **Tempo:** ____ minutos
- **Tópico mais fraco:**
- **Regra que preciso memorizar:**

## 2. D+2 — 27/07/2026

Não releia o capítulo antes da primeira tentativa. Use no máximo 10 minutos.

1. Desenhe uma Region com duas AZs e um ponto de presença. Explique o domínio de
   falha de cada elemento.
2. Dê quatro critérios para escolher uma Region e identifique qual deles funciona
   como restrição obrigatória.
3. Compare a responsabilidade do cliente em EC2 e em S3.
4. Explique root user, IAM user, user group, role e policy com uma frase para cada.
5. Uma aplicação EC2 precisa acessar S3. Qual identidade deve usar e por quê?
6. Uma policy contém um `Allow` e outra contém um `Deny` explícito aplicável. Qual
   é o resultado?
7. MFA altera autenticação ou autorização?
8. Cite duas alternativas atuais a access keys permanentes para usar a AWS CLI.

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
- **Erros reabertos no Caderno de Erros:**

## 3. D+7 — 01/08/2026

Resolva o cenário sem consultar. Use no máximo 12 minutos.

### Cenário

Uma empresa mantém uma aplicação em uma única AWS Region. Todos os servidores
estão em uma AZ. A aplicação em EC2 lê objetos privados no S3 usando uma access
key de um IAM user gravada no código. A equipe utiliza o root user nas tarefas
diárias. Uma auditoria exige tolerância à falha de uma AZ, credenciais
temporárias e menor exposição da conta.

Responda:

1. Qual é o single point of failure de infraestrutura?
2. Qual mudança atende à falha de uma AZ sem criar uma segunda Region?
3. Como substituir a access key guardada no código?
4. Como deve ser tratado o root user?
5. Quem é responsável pelos patches do guest OS das instâncias?
6. Escreva a regra de avaliação de policy em três linhas: implicit deny, Allow e
   explicit Deny.
7. Liste três palavras do cenário em inglês que apontariam para as decisões.

### Registro D+7

- **Itens corretos sem consulta:** ____ / 7
- **Tempo:** ____ minutos
- **Confiança:** alta / média / baixa
- **Ainda confundo:**
- **Próxima ação:**

## 4. Critério de encerramento do B01

O bloco pode ser marcado como consolidado quando:

- o resultado inicial for pelo menos 8/10;
- D+2 tiver pelo menos 7/8;
- D+7 tiver pelo menos 6/7;
- nenhum erro de root, role, access key ou explicit Deny continuar aberto;
- as diferenças Region/AZ/edge e Multi-AZ/Multi-Region forem explicadas sem
  consulta.

Se um critério falhar, revise apenas a seção correspondente do capítulo, crie uma
nova explicação em palavras próprias e repita as questões erradas 24 horas depois.
