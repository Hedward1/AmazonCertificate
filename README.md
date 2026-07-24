# Preparação AWS Certified Solutions Architect - Associate (SAA-C03)

Esta é a página inicial do projeto. A pasta está organizada por função; os
arquivos-fonte ficam separados do material produzido e não devem ser editados
durante a rotina normal de estudo.

## Estado atual — 24/07/2026

- **Exame:** AWS Certified Solutions Architect - Associate (SAA-C03), em inglês.
- **Perfil:** iniciante absoluto, com conta AWS e pequeno orçamento mensal.
- **Cronograma:** 25/07 a 31/08/2026, 32 dias, 96 horas, domingos livres.
- **Blocos de conteúdo:** 25 no total; B01–B04 prontos e B05–B25 restantes.
- **Fase final:** 7 dias adicionais de consolidação, incluindo 3 simulados.
- **Questões autorais:** 40, com gabaritos separados.
- **Último progresso capturado da Udemy:** 13 de 425 itens; aula atual 14.
- **Próxima produção:** B05 — AMIs, instance store, tipos e criptografia de EBS,
  EFS e introdução à alta disponibilidade.
- **Pendências pessoais:** definir o teto mensal em USD e a data da prova.

## Materiais disponíveis

| Bloco | Data | Teoria | Laboratório | Questões | Revisões |
|---|---|---|---|---|---|
| B01 | 25/07 | [Infraestrutura global, responsabilidade e IAM](03_Guia_do_Estudante/Capitulos/B01_Infraestrutura_Global_Responsabilidade_e_IAM.md) | [Segurança da conta](05_Laboratorios/LAB_B01_Seguranca_da_Conta_IAM.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B01_Questoes.md) | [D+2/D+7](06_Progresso/B01_Checklist_e_Revisoes.md) |
| B02 | 27/07 | [IAM aplicado, CLI, EC2 e security groups](03_Guia_do_Estudante/Capitulos/B02_IAM_Aplicado_CLI_EC2_e_Security_Groups.md) | [CLI, roles e auditoria](05_Laboratorios/LAB_B02_CLI_Roles_e_Auditoria_IAM.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B02_Questoes.md) | [D+2/D+7](06_Progresso/B02_Checklist_e_Revisoes.md) |
| B03 | 28/07 | [Conexão ao EC2, roles e modelos de compra](03_Guia_do_Estudante/Capitulos/B03_Conexao_EC2_Roles_e_Modelos_de_Compra.md) | [Primeira instância EC2 e cleanup](05_Laboratorios/LAB_B03_EC2_Web_Role_e_Cleanup.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B03_Questoes.md) | [D+2/D+7](06_Progresso/B03_Checklist_e_Revisoes.md) |
| B04 | 29/07 | [IPs, ENIs, placement groups, hibernação, EBS, snapshots e AMIs](03_Guia_do_Estudante/Capitulos/B04_IPs_ENI_Placement_Hibernation_EBS_Snapshots_e_AMI.md) | [Inventário read-only de EC2](05_Laboratorios/LAB_B04_Inventario_EC2_ENI_EBS_e_AMI.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B04_Questoes.md) | [D+2/D+7](06_Progresso/B04_Checklist_e_Revisoes.md) |

## Comece por aqui

1. Consulte o [cronograma diário](02_Planejamento/Cronograma_Diario_SAA-C03.md).
2. Estude o bloco indicado no [Guia do Estudante](03_Guia_do_Estudante/Guia_do_Estudante_SAA-C03.md).
3. Execute o laboratório correspondente em
   [Laboratórios](05_Laboratorios/README.md).
4. Resolva as questões sem abrir o gabarito em
   [Questões e Revisões](04_Questoes_e_Revisoes/README.md).
5. Registre erros e revisões em [Progresso](06_Progresso/README.md).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| [00_Projeto](00_Projeto/README.md) | objetivo, perfil, decisões e estado do projeto |
| [01_Fontes](01_Fontes/README.md) | guia oficial, HTML, imagens e inventário da Udemy |
| [02_Planejamento](02_Planejamento/README.md) | cronograma, matriz, análise e lacunas |
| [03_Guia_do_Estudante](03_Guia_do_Estudante/README.md) | capítulos teóricos e navegação do guia |
| [04_Questoes_e_Revisoes](04_Questoes_e_Revisoes/README.md) | questões, gabaritos e Caderno de Erros |
| [05_Laboratorios](05_Laboratorios/README.md) | práticas guiadas e regras de cleanup |
| [06_Progresso](06_Progresso/README.md) | checklists, D+2, D+7 e resultados |
| [99_Ferramentas](99_Ferramentas/README.md) | scripts de extração e validação |

## Fontes de verdade

- Escopo e comportamento dos serviços: documentação oficial vigente da AWS.
- Sequência e duração das aulas: inventário extraído do curso da Udemy.
- Prioridades: matriz de cobertura e cronograma deste projeto.
- Dificuldades pessoais: Caderno de Erros e registros de revisão.

## Regras permanentes de segurança e custo

- Não usar root em atividades diárias nem criar access key para root.
- Preferir IAM Identity Center, `aws login` ou roles com credenciais temporárias.
- Não habilitar AWS Organizations em uma Free account sem avaliar a perda de
  créditos e a mudança para o plano pago.
- Confirmar account, identidade e Region antes de comandos que alterem recursos.
- Tratar AWS Budgets como alerta, não como bloqueio instantâneo.
- No LAB B03, abortar antes do lançamento se a estimativa ultrapassar USD 0,25.
- O LAB B04 é somente leitura e deve terminar sem criar, alterar ou excluir
  recursos.
- Não confundir `Stop` com cleanup: terminar a instância e verificar EBS e IPv4.
- Executar e validar o cleanup de cada laboratório.

Nenhum arquivo foi descartado na reorganização de 24/07/2026.
