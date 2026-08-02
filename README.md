# Preparação AWS Certified Solutions Architect - Associate (SAA-C03)

Esta é a página inicial do projeto. A pasta está organizada por função; os
arquivos-fonte ficam separados do material produzido e não devem ser editados
durante a rotina normal de estudo.

## Estado atual — 01/08/2026

- **Exame:** AWS Certified Solutions Architect - Associate (SAA-C03), em inglês.
- **Perfil:** iniciante absoluto, com conta AWS e pequeno orçamento mensal.
- **Cronograma:** 25/07 a 31/08/2026, 32 dias, 96 horas, domingos livres;
  são 25 dias de conteúdo e 7 dias de consolidação.
- **Blocos de conteúdo:** B01–B25 completos, cada um com capítulo,
  laboratório, 10 questões, gabarito comentado e checklist D+2/D+7.
- **Fase final:** 7 dias adicionais de consolidação, com `SIM-A` em 26/08,
  Practice Udemy em 28/08 e `SIM-C` em 31/08. O `SIM-B` autoral fica como
  tentativa extra após o ciclo ou substituto se a Udemy estiver indisponível.
  Os três [pacotes completos](04_Questoes_e_Revisoes/Simulados/README.md) estão
  versionados; não abra bancos ou gabaritos antes da tentativa correspondente.
- **Questões autorais do curso:** 250, com 190 `single`, 45 `multi-2`, 15
  `multi-3` e 250 respostas comentadas em arquivos separados.
- **Simulados autorais:** 195 questões em inglês distribuídas entre SIM-A,
  SIM-B e SIM-C, com [questões, gabaritos e relatórios](04_Questoes_e_Revisoes/Simulados/README.md).
- **Último progresso capturado da Udemy:** 13 de 425 itens; aula atual 14.
- **Escopo oficial:** 189 itens individuais de Knowledge/Skills do SAA-C03 e
  listas de serviços revalidados em 01/08/2026.
- **Próximo passo de estudo:** começar pelo B01 e avançar em ordem, combinando
  as aulas selecionadas com o material do mesmo bloco.
- **Pendências pessoais:** definir o teto mensal em USD e a data da prova.

## Materiais disponíveis

Antes de cada bloco, consulte o [Roteiro diário das aulas da
Udemy](02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md). Ele informa o que
assistir, consultar ou pular e mostra os títulos exatos dos 425 itens.

| Bloco | Data | Teoria | Laboratório | Questões | Revisões |
|---|---|---|---|---|---|
| B01 | 25/07 | [Infraestrutura global, responsabilidade e IAM](03_Guia_do_Estudante/Capitulos/B01_Infraestrutura_Global_Responsabilidade_e_IAM.md) | [Segurança da conta](05_Laboratorios/LAB_B01_Seguranca_da_Conta_IAM.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B01_Questoes.md) | [D+2/D+7](06_Progresso/B01_Checklist_e_Revisoes.md) |
| B02 | 27/07 | [IAM aplicado, CLI, EC2 e security groups](03_Guia_do_Estudante/Capitulos/B02_IAM_Aplicado_CLI_EC2_e_Security_Groups.md) | [CLI, roles e auditoria](05_Laboratorios/LAB_B02_CLI_Roles_e_Auditoria_IAM.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B02_Questoes.md) | [D+2/D+7](06_Progresso/B02_Checklist_e_Revisoes.md) |
| B03 | 28/07 | [Conexão ao EC2, roles e modelos de compra](03_Guia_do_Estudante/Capitulos/B03_Conexao_EC2_Roles_e_Modelos_de_Compra.md) | [Primeira instância EC2 e cleanup](05_Laboratorios/LAB_B03_EC2_Web_Role_e_Cleanup.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B03_Questoes.md) | [D+2/D+7](06_Progresso/B03_Checklist_e_Revisoes.md) |
| B04 | 29/07 | [IPs, ENIs, placement groups, hibernação, EBS, snapshots e AMIs](03_Guia_do_Estudante/Capitulos/B04_IPs_ENI_Placement_Hibernation_EBS_Snapshots_e_AMI.md) | [Inventário read-only de EC2](05_Laboratorios/LAB_B04_Inventario_EC2_ENI_EBS_e_AMI.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B04_Questoes.md) | [D+2/D+7](06_Progresso/B04_Checklist_e_Revisoes.md) |
| B05 | 30/07 | [EBS, instance store, EFS e alta disponibilidade](03_Guia_do_Estudante/Capitulos/B05_EBS_Instance_Store_EFS_e_Fundamentos_de_HA.md) | [EBS, snapshot, restauração e projeto EFS](05_Laboratorios/LAB_B05_EBS_Snapshot_Restore_e_Projeto_EFS.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B05_Questoes.md) | [D+2/D+7](06_Progresso/B05_Checklist_e_Revisoes.md) |
| B06 | 31/07 | [ALB, NLB, GWLB e target groups](03_Guia_do_Estudante/Capitulos/B06_ALB_NLB_GWLB_Target_Groups_e_Cross_Zone.md) | [Projeto de load balancers Multi-AZ](05_Laboratorios/LAB_B06_Projeto_ALB_NLB_GWLB_Multi_AZ.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B06_Questoes.md) | [D+2/D+7](06_Progresso/B06_Checklist_e_Revisoes.md) |
| B07 | 01/08 | [TLS, ACM, deregistration e Auto Scaling](03_Guia_do_Estudante/Capitulos/B07_TLS_ACM_Deregistration_e_Auto_Scaling.md) | [Simulação ALB e ASG](05_Laboratorios/LAB_B07_Simulacao_ALB_ASG_e_Eventos_de_Escala.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B07_Questoes.md) | [D+2/D+7](06_Progresso/B07_Checklist_e_Revisoes.md) |
| B08 | 03/08 | [RDS, Aurora, RDS Proxy e ElastiCache](03_Guia_do_Estudante/Capitulos/B08_RDS_Aurora_RDS_Proxy_e_ElastiCache.md) | [Projeto de banco privado, proxy e cache](05_Laboratorios/LAB_B08_Projeto_RDS_Privado_Aurora_Proxy_e_Cache.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B08_Questoes.md) | [D+2/D+7](06_Progresso/B08_Checklist_e_Revisoes.md) |
| B09 | 04/08 | [DNS, Route 53, records, TTL e routing](03_Guia_do_Estudante/Capitulos/B09_DNS_Route53_Records_TTL_e_Routing.md) | [Observação DNS e cenários Route 53](05_Laboratorios/LAB_B09_Observacao_DNS_e_Cenarios_Route53.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B09_Questoes.md) | [D+2/D+7](06_Progresso/B09_Checklist_e_Revisoes.md) |
| B10 | 05/08 | [Route 53 avançado, arquiteturas clássicas e Beanstalk](03_Guia_do_Estudante/Capitulos/B10_Route53_Avancado_Arquiteturas_Classicas_e_Beanstalk.md) | [Failover, DNS híbrido e Beanstalk](05_Laboratorios/LAB_B10_Failover_DNS_Hibrido_e_Beanstalk.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B10_Questoes.md) | [D+2/D+7](06_Progresso/B10_Checklist_e_Revisoes.md) |
| B11 | 06/08 | [S3: segurança, versioning, replication, classes e eventos](03_Guia_do_Estudante/Capitulos/B11_S3_Seguranca_Versioning_Replication_Classes_e_Eventos.md) | [S3 versioning, lifecycle e cleanup](05_Laboratorios/LAB_B11_S3_Versioning_Lifecycle_e_Cleanup.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B11_Questoes.md) | [D+2/D+7](06_Progresso/B11_Checklist_e_Revisoes.md) |
| B12 | 07/08 | [S3, CloudFront e Global Accelerator](03_Guia_do_Estudante/Capitulos/B12_S3_Seguranca_CloudFront_e_Global_Accelerator.md) | [S3 privado, URL pré-assinada e arquitetura global](05_Laboratorios/LAB_B12_S3_Presigned_URL_CORS_e_Arquitetura_Global.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B12_Questoes.md) | [D+2/D+7](06_Progresso/B12_Checklist_e_Revisoes.md) |
| B13 | 08/08 | [Storage híbrido, FSx, DataSync, Transfer e Snow](03_Guia_do_Estudante/Capitulos/B13_Storage_Hibrido_FSx_DataSync_Transfer_e_Snow.md) | [Desenho de migração e storage híbrido](05_Laboratorios/LAB_B13_Desenho_de_Migracao_e_Storage_Hibrido.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B13_Questoes.md) | [D+2/D+7](06_Progresso/B13_Checklist_e_Revisoes.md) |
| B14 | 10/08 | [SQS, SNS, desacoplamento e fan-out](03_Guia_do_Estudante/Capitulos/B14_SQS_SNS_Desacoplamento_e_Fanout.md) | [SQS, SNS fan-out e DLQ](05_Laboratorios/LAB_B14_SQS_SNS_Fanout_e_DLQ.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B14_Questoes.md) | [D+2/D+7](06_Progresso/B14_Checklist_e_Revisoes.md) |
| B15 | 11/08 | [Streaming, Amazon MQ e ECS](03_Guia_do_Estudante/Capitulos/B15_Streaming_Amazon_MQ_e_ECS.md) | [Streaming e inspeção ECS](05_Laboratorios/LAB_B15_Streaming_e_Inspecao_ECS.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B15_Questoes.md) | [D+2/D+7](06_Progresso/B15_Checklist_e_Revisoes.md) |
| B16 | 12/08 | [ECR, EKS, Lambda, SnapStart e edge](03_Guia_do_Estudante/Capitulos/B16_ECR_EKS_Lambda_Concurrency_SnapStart_e_Edge.md) | [Lambda mínima, logs e cleanup](05_Laboratorios/LAB_B16_Lambda_Minima_Logs_e_Cleanup.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B16_Questoes.md) | [D+2/D+7](06_Progresso/B16_Checklist_e_Revisoes.md) |
| B17 | 13/08 | [Serverless, DynamoDB, API Gateway, Step Functions e Cognito](03_Guia_do_Estudante/Capitulos/B17_Serverless_VPC_DynamoDB_API_Gateway_Step_Functions_e_Cognito.md) | [Mini-API serverless](05_Laboratorios/LAB_B17_API_Serverless_Lambda_DynamoDB.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B17_Questoes.md) | [D+2/D+7](06_Progresso/B17_Checklist_e_Revisoes.md) |
| B18 | 14/08 | [Arquiteturas serverless, bancos e analytics](03_Guia_do_Estudante/Capitulos/B18_Arquiteturas_Serverless_Bancos_e_Analytics.md) | [Arquitetura serverless e matriz de bancos](05_Laboratorios/LAB_B18_Arquitetura_Serverless_e_Matriz_de_Bancos.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B18_Questoes.md) | [D+2/D+7](06_Progresso/B18_Checklist_e_Revisoes.md) |
| B19 | 15/08 | [Analytics, streaming e machine learning](03_Guia_do_Estudante/Capitulos/B19_Analytics_Streaming_e_Machine_Learning.md) | [Pipeline de analytics e seleção de AI/ML](05_Laboratorios/LAB_B19_Pipeline_Analytics_e_ML_Read_Only.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B19_Questoes.md) | [D+2/D+7](06_Progresso/B19_Checklist_e_Revisoes.md) |
| B20 | 17/08 | [Observabilidade, auditoria, Config e Organizations](03_Guia_do_Estudante/Capitulos/B20_Observabilidade_Auditoria_Config_e_Organizations.md) | [CloudWatch, CloudTrail e Config](05_Laboratorios/LAB_B20_CloudWatch_CloudTrail_e_Config_Read_Only.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B20_Questoes.md) | [D+2/D+7](06_Progresso/B20_Checklist_e_Revisoes.md) |
| B21 | 18/08 | [Organizations, IAM avançado, KMS e Parameter Store](03_Guia_do_Estudante/Capitulos/B21_Organizations_IAM_Avancado_KMS_e_Parameter_Store.md) | [Políticas, KMS e Parameter Store](05_Laboratorios/LAB_B21_Avaliacao_de_Politicas_KMS_e_Parameter_Store.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B21_Questoes.md) | [D+2/D+7](06_Progresso/B21_Checklist_e_Revisoes.md) |
| B22 | 19/08 | [Segredos, proteção de aplicações e fundamentos de VPC](03_Guia_do_Estudante/Capitulos/B22_Segredos_Protecao_de_Aplicacoes_e_Fundamentos_VPC.md) | [VPC pública e privada sem NAT Gateway](05_Laboratorios/LAB_B22_VPC_Publica_Privada_sem_NAT_Gateway.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B22_Questoes.md) | [D+2/D+7](06_Progresso/B22_Checklist_e_Revisoes.md) |
| B23 | 20/08 | [Redes avançadas e conectividade híbrida](03_Guia_do_Estudante/Capitulos/B23_Redes_Avancadas_e_Conectividade_Hibrida.md) | [Roteamento VPC e híbrido em diagrama](05_Laboratorios/LAB_B23_Roteamento_VPC_e_Hibrido_em_Diagrama.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B23_Questoes.md) | [D+2/D+7](06_Progresso/B23_Checklist_e_Revisoes.md) |
| B24 | 21/08 | [Custos de rede, DR, migração e arquiteturas integradas](03_Guia_do_Estudante/Capitulos/B24_Custos_de_Rede_DR_Migracao_e_Arquiteturas_Integradas.md) | [Estratégias de DR e migração](05_Laboratorios/LAB_B24_Estrategias_DR_e_Migracao_em_Diagrama.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B24_Questoes.md) | [D+2/D+7](06_Progresso/B24_Checklist_e_Revisoes.md) |
| B25 | 22/08 | [CloudFormation, operações, custos e Well-Architected](03_Guia_do_Estudante/Capitulos/B25_CloudFormation_Operacoes_Custos_e_Well_Architected.md) | [Auditoria final de custos e cleanup](05_Laboratorios/LAB_B25_Auditoria_Final_de_Custos_e_Cleanup.md) | [10 questões](04_Questoes_e_Revisoes/Blocos/B25_Questoes.md) | [D+2/D+7](06_Progresso/B25_Checklist_e_Revisoes.md) |

## Comece por aqui

1. Comece pelo **B01**, mesmo que queira acelerar; ele estabelece o vocabulário
   e as regras de segurança usados pelos demais blocos.
2. Em cada dia, abra primeiro o [roteiro das aulas da
   Udemy](02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md), assista somente
   o que estiver marcado para assistir/praticar e respeite as marcações de pulo.
3. Em seguida, estude o capítulo do mesmo bloco no [Guia do
   Estudante](03_Guia_do_Estudante/Guia_do_Estudante_SAA-C03.md).
4. Execute o laboratório correspondente em
   [Laboratórios](05_Laboratorios/README.md).
5. Resolva as questões sem abrir o gabarito em
   [Questões e Revisões](04_Questoes_e_Revisoes/README.md).
6. Registre erros e revisões em [Progresso](06_Progresso/README.md).

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
