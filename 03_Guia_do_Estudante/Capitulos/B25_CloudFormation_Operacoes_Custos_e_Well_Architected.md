# B25 — CloudFormation, operações, custos, Well-Architected e fechamento

**Data planejada:** 22/08/2026<br>
**Nível:** iniciante absoluto<br>
**Comece pelas aulas da Udemy:** [roteiro B25 — aulas 367–385 e 387–388](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b25); Consulte 386 e 389–393; pule 394–396. Não abra o practice exam.<br>
**Quizzes:** Q27 e Q28<br>
**Domínios oficiais:** Todos, com ênfase em 2 — Resilient e 4 — Cost-Optimized<br>
**Tarefas:** 2.2 e 4.2 principais; revisão integrada<br>
**Pré-requisito:** B24 — DR e migração

## 1. Objetivos de aprendizagem

1. Explicar template e stack.
2. Revisar change set.
3. Explicar drift e rollback.
4. Usar service role com mínimo privilégio.
5. Escolher Systems Manager.
6. Reconhecer serviços complementares.
7. Analisar custos e anomalias.
8. Aplicar seis pilares.
9. Usar Trusted Advisor corretamente.
10. Concluir auditoria sem abrir practice exam.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 367–381 | CloudFormation, SSM, custos e serviços complementares |
| Q27 | Fazer após recuperação |
| 382–385 | Well-Architected, Trusted Advisor e arquiteturas |
| Q28 | Fazer após recuperação |
| 386 e 389–393 | Consultar perto da prova |
| 387–388 | Checkpoint e exam tips |
| 394–396 | Pular |
| Practice exam | Reservado ao evento Practice Udemy de 28/08; não confundir com o `SIM-B` autoral privado |

Use aulas, capítulo, laboratório e questões nessa ordem. Não copie credenciais nem crie recursos pagos para reproduzir telas.

### Classificação da atualização do Amazon Pinpoint

- **`núcleo SAA-C03`:** escolher o serviço pelo requisito: SES para email transacional ou em massa; entrega programática por outros canais e engajamento orquestrado são necessidades diferentes. Em uma arquitetura nova, não selecione um serviço em encerramento.
- **`atualização relevante`:** Amazon Pinpoint não aceita novos clientes desde 20/05/2025 e encerra suporte em 30/10/2026. Para novos desenhos, use Amazon Connect Customer outbound campaigns para engajamento proativo, AWS End User Messaging para canais de mensagem e SES para email.
- **`conteúdo profissional opcional`:** mapeamento de endpoints para Customer Profiles, migração de templates, journeys, analytics e APIs de canal. Isso é útil para migração real, mas **não é para memorizar** para a SAA-C03.

## 3. Vocabulário essencial

| Termo | Significado |
|---|---|
| template | descrição declarativa |
| stack | unidade gerenciada |
| change set | prévia de alterações |
| rollback | retorno após falha |
| drift | diferença entre real e template |
| service role | role usada pelo CloudFormation |
| managed node | node administrado pelo SSM |
| cost allocation tag | dimensão de custo ativada |
| pillar | área de decisão arquitetural |
| improvement plan | ações após review |

## 4. Modelo mental

1. Identifique o requisito.
2. Marque restrições.
3. Determine escopo.
4. Avalie segurança.
5. Avalie resiliência.
6. Avalie performance.
7. Compare operação e custo.
8. Elimine violações.

## 5. Fundamentos e decisões

### 5.1 Ponto 1

CloudFormation descreve infraestrutura declarativamente.
### 5.2 Ponto 2

Stack é a unidade de lifecycle.
### 5.3 Ponto 3

Parameters recebem entradas.
### 5.4 Ponto 4

Resources é a seção obrigatória de recursos.
### 5.5 Ponto 5

Outputs não devem expor segredos.
### 5.6 Ponto 6

References criam dependências implícitas.
### 5.7 Ponto 7

Change set compara alterações propostas.
### 5.8 Ponto 8

Change set pode indicar replacement.
### 5.9 Ponto 9

Change set não garante ausência de impacto.
### 5.10 Ponto 10

Rollback tenta retornar após falha.
### 5.11 Ponto 11

Stack policy protege contra updates.
### 5.12 Ponto 12

Termination protection protege contra exclusão acidental.
### 5.13 Ponto 13

DeletionPolicy Retain preserva recurso.
### 5.14 Ponto 14

Excluir stack não remove recurso com Retain.
### 5.15 Ponto 15

Drift detection compara propriedades suportadas.
### 5.16 Ponto 16

Drift não cobre tudo.
### 5.17 Ponto 17

Drift não corrige automaticamente.
### 5.18 Ponto 18

Service role é assumida pelo CloudFormation.
### 5.19 Ponto 19

Controle iam PassRole é importante.
### 5.20 Ponto 20

Service role deve ter mínimo privilégio.
### 5.21 Ponto 21

Session Manager evita inbound SSH ou RDP.
### 5.22 Ponto 22

Managed node precisa agente, IAM e conectividade.
### 5.23 Ponto 23

Run Command executa comandos em frota.
### 5.24 Ponto 24

Patch Manager organiza patching.
### 5.25 Ponto 25

SES atende email transacional e em massa.
### 5.26 Ponto 26

Amazon Pinpoint atende campanhas multicanal apenas em contas existentes durante a transição e encerra suporte em 30/10/2026; não é escolha para um novo projeto.
### 5.27 Ponto 27

AWS Outposts estende infraestrutura, APIs e ferramentas AWS a uma instalação do
cliente. A AWS opera o hardware; o cliente fornece site, energia, rede e
conectividade do **service link** com a Region associada. A capacidade local é
finita e precisa incluir crescimento e tolerância a manutenção/falha.

**Escolha Outposts** quando o workload precisa executar no site por latência com
sistemas locais, processamento/residência de dados ou dependências locais, mas
quer o modelo operacional e APIs AWS suportadas. **Não escolha** apenas porque a
aplicação é híbrida: Direct Connect conecta o datacenter à Region sem levar
compute AWS ao site; Local Zones colocam recursos em uma instalação AWS próxima
de uma área metropolitana, não dentro do datacenter do cliente; infraestrutura
on-premises autogerenciada mantém outra responsabilidade operacional.

| Opção | Onde executa | Decisão dominante |
|---|---|---|
| AWS Region | Region AWS | maior elasticidade e catálogo; latência até o site |
| AWS Local Zones | local AWS metropolitano | proximidade a usuários, não presença no site do cliente |
| AWS Outposts | instalação do cliente | AWS gerenciada localmente; capacidade e service link planejados |
| on-premises autogerenciado | instalação do cliente | máximo controle e máxima responsabilidade operacional |

**Cenário resolvido — fábrica:** um sistema de controle precisa responder em
poucos milissegundos aos equipamentos locais, manter o processamento no site e
usar EC2/EBS/ECS compatíveis. Se a instalação atende aos requisitos físicos e a
empresa aceita planejar capacidade e service link resiliente, Outposts é a
opção híbrida. Se basta acesso privado à Region, Direct Connect é mais simples.
### 5.28 Ponto 28

Batch executa jobs batch containerizados.
### 5.29 Ponto 29

AppFlow integra SaaS e AWS.
### 5.30 Ponto 30

Amplify acelera apps web e mobile.
### 5.31 Ponto 31

Cost Explorer analisa custo e uso.
### 5.32 Ponto 32

Budgets alerta sobre limiares.
### 5.33 Ponto 33

Cost Anomaly Detection detecta padrão incomum.
### 5.34 Ponto 34

Anomaly Detection não encerra recursos.
### 5.35 Ponto 35

Dados de billing têm atraso.
### 5.36 Ponto 36

Instance Scheduler é uma solução implantada.
### 5.37 Ponto 37

Operational Excellence é operar e melhorar.
### 5.38 Ponto 38

Security protege identidade, dados e infraestrutura.
### 5.39 Ponto 39

Reliability recupera e atende demanda.
### 5.40 Ponto 40

Performance Efficiency usa recursos eficientes.
### 5.41 Ponto 41

Cost Optimization elimina desperdício.
### 5.42 Ponto 42

Sustainability reduz impacto ambiental.
### 5.43 Ponto 43

Well-Architected Tool organiza reviews.
### 5.44 Ponto 44

Trusted Advisor produz checks e recomendações.
### 5.45 Ponto 45

Cobertura do Trusted Advisor depende do plano.
### 5.46 Ponto 46

Practice exam fica inédito até o evento Practice Udemy de 28/08. O `SIM-B`
autoral privado permanece fechado como tentativa extra posterior ou substituto
se a Udemy estiver indisponível.

### Cápsula de decisão — AWS Compute Optimizer

- **Problema que resolve:** analisar configuração e métricas de utilização para identificar recursos ociosos ou super/subdimensionados e recomendar rightsizing com melhor relação preço-performance.
- **Tarefa SAA-C03 relacionada:** 4.2 — projetar arquiteturas de compute com custo otimizado; as recomendações também podem apoiar decisões de storage e banco nos tipos de recurso compatíveis.
- **Quando escolher:** a pergunta fornece histórico de utilização e pede recomendações de tamanho ou configuração para EC2, Auto Scaling, EBS, Lambda, ECS on Fargate, RDS/Aurora ou outros recursos suportados.
- **Quando não escolher:** para alertar imediatamente que um orçamento foi excedido, detalhar uma fatura por linha ou alterar recursos automaticamente.
- **Serviço semelhante:** Trusted Advisor oferece checks amplos; Compute Optimizer aprofunda rightsizing com configuração, métricas e projeção de utilização.
- **Armadilha:** recomendações não são alterações automáticas. É preciso optar pelo serviço, acumular métricas suficientes e validar performance e capacidade antes de aplicar; o lookback padrão é de 14 dias e recursos avançados podem ter custo.
- **Questão situacional extra (fora do banco de 250):** uma frota EC2 opera há meses, mas a equipe não sabe quais tipos menores manteriam performance aceitável. Qual serviço fornece recomendações baseadas em utilização?
- **Resposta curta:** AWS Compute Optimizer; revise os gráficos e o risco de performance antes de executar o rightsizing.
- **Referência oficial:** [What is AWS Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

### Cápsula de decisão — AWS Cost and Usage Report (CUR 2.0)

- **Problema que resolve:** entregar dados recorrentes e granulares de custo e uso em S3 para rateio, auditoria e análises próprias.
- **Tarefas SAA-C03 relacionadas:** apoia 4.1–4.4 ao fornecer evidência detalhada para otimizar storage, compute, bancos e rede.
- **Quando escolher:** a organização precisa de linhas detalhadas de billing, esquema controlado e processamento posterior com SQL, Athena, Amazon Quick Sight (componente de BI do Amazon Quick; Amazon QuickSuite no guia SAA-C03) ou ferramentas próprias. Em Data Exports, CUR 2.0 é a opção nova e recomendada.
- **Quando não escolher:** para uma exploração rápida no console, um limiar de orçamento ou detecção de anomalia; use Cost Explorer, Budgets ou Cost Anomaly Detection, respectivamente.
- **Serviço semelhante:** Cost Explorer oferece análise interativa pronta; CUR 2.0 fornece o dataset granular e recorrente para análises personalizadas.
- **Armadilha:** o relatório não reduz nem bloqueia gastos. Legacy CUR ainda existe, mas CUR 2.0 via AWS Data Exports é recomendado; considere atraso dos dados e custos de S3, consulta e visualização.
- **Questão situacional extra (fora do banco de 250):** FinOps precisa atribuir custos por conta, serviço, tag e tipo de uso, guardar o histórico em S3 e consultar milhões de linhas com SQL. Qual recurso deve ser configurado?
- **Resposta curta:** CUR 2.0 em AWS Data Exports, com entrega recorrente no S3 e consulta por Athena ou outra ferramenta.
- **Referência oficial:** [What is AWS Data Exports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html)

## 6. Tabela de decisão

| Requisito | Escolha | Motivo |
|---|---|---|
| IaC declarativa | CloudFormation | stack repetível |
| Prévia de update | Change set | impacto proposto |
| Mudança manual | Drift detection | comparação suportada |
| Shell sem inbound | Session Manager | canal gerenciado |
| Email transacional | SES | entrega de email |
| Engajamento proativo com segmentação, campanhas ou jornadas | Amazon Connect Customer outbound campaigns | destino atual para capacidades de engagement do Pinpoint |
| SMS, MMS, push, WhatsApp ou voz por API | AWS End User Messaging | canais de entrega programática atuais |
| Job container batch | AWS Batch | fila e compute |
| SaaS para AWS | AppFlow | integração gerenciada |
| Analisar gasto | Cost Explorer | dimensões históricas |
| Detectar gasto incomum | Cost Anomaly Detection | modelo e alerta |
| Rightsizing baseado em utilização | AWS Compute Optimizer | recomenda tamanho/configuração sem alterar automaticamente |
| Exportar billing granular e recorrente | CUR 2.0 em AWS Data Exports | dataset customizável entregue no S3 |

## 7. Cenários resolvidos


### Cenário resolvido 1 — Update arriscado

- **Contexto:** Template novo pode substituir banco.
- **Requisito:** Revisar impacto e preservar dados.
- **Decisão:** Change set, backup e retention apropriada.
- **Por quê:** A prévia mostra replacement planejado.
- **Por que não:** Executar update direto ignora evidência.
- **Trade-off:** Change set não prova segurança total.
- **Validação:** Revisar mudança e testar restore.
- **Custo/cleanup:** Recursos substituídos e snapshots podem persistir.
- **Variação:** Stack policy pode proteger recurso.

### Cenário resolvido 2 — Sem bastion

- **Contexto:** Instâncias privadas não aceitam SSH.
- **Requisito:** Sessão auditável administrativa.
- **Decisão:** SSM Session Manager.
- **Por quê:** Não exige inbound nem bastion quando pré-requisitos existem.
- **Por que não:** Abrir SSH para internet amplia superfície.
- **Trade-off:** Agente, IAM, conectividade e logs precisam ser mantidos.
- **Validação:** Testar sessão e auditoria.
- **Custo/cleanup:** Logs e endpoints podem cobrar.
- **Variação:** Port forwarding pode atender acesso controlado.

### Cenário resolvido 3 — Anomalia de custo

- **Contexto:** Gasto diário sobe sem mudança conhecida.
- **Requisito:** Detectar, atribuir e conter com segurança.
- **Decisão:** Anomaly Detection para alerta e Cost Explorer para análise.
- **Por quê:** Um detecta padrão e o outro detalha dimensões.
- **Por que não:** Excluir recurso desconhecido automaticamente é perigoso.
- **Trade-off:** Billing tem atraso.
- **Validação:** Correlacionar serviço, Region, tag e CloudTrail.
- **Custo/cleanup:** Confirmar cleanup em todas as Regions.
- **Variação:** Budgets cobre limiar planejado.

## 8. Fluxo de projeto

1. Identificar requisito e superlativo.
2. Eliminar violação explícita.
3. Definir escopo do recurso.
4. Preferir gerenciado quando reduz operação e atende.
5. Revisar segurança.
6. Revisar resiliência.
7. Revisar performance.
8. Revisar custo total.
9. Revisar sustentabilidade.
10. Planejar observabilidade.
11. Planejar cleanup.
12. Registrar trade-off.

## 9. Custos e cleanup

- Template não custa; recursos da stack custam.
- Retain pode deixar recurso cobrado.
- Logs e endpoints de SSM podem cobrar.
- Outposts envolve compromisso significativo.
- Batch cobra compute consumido.
- AppFlow, Amplify, SES, AWS End User Messaging e Amazon Connect cobram conforme uso e recursos configurados.
- Audite public IPv4, NAT, endpoints, volumes, snapshots, bancos, logs, secrets e KMS.
- Não excluir recurso sem provar propriedade.

Faça inventário antes e depois. Exclua apenas recursos criados pelo bloco.

## 10. Armadilhas

- Change set não executa.
- Change set não garante segurança.
- Drift não corrige.
- Drift não cobre tudo.
- Service role ampla aumenta impacto.
- Anomaly Detection não bloqueia gasto.
- Trusted Advisor depende do plano.
- Pinpoint é uma pista legada: novos clientes não entram e o serviço encerra em 30/10/2026.
- Well-Architected Tool não altera arquitetura.
- Retain sobrevive à stack.
- Não abrir practice exam no B25.

## 11. Checklist

- [ ] Objetivos explicados sem consulta.
- [ ] Tabela reconstruída.
- [ ] Três cenários resolvidos.
- [ ] Trade-offs justificados.
- [ ] Custos identificados.
- [ ] Laboratório concluído.
- [ ] Dez questões respondidas.
- [ ] Erros registrados.
- [ ] D+2 e D+7 agendados.

## 12. Recuperação ativa

1. Desenhe template até rollback.
2. Explique change set.
3. Explique drift.
4. Explique service role e PassRole.
5. Compare Session Manager e bastion.
6. Associe seis serviços complementares.
7. Compare três ferramentas de custo.
8. Recite seis pilares.
9. Explique Trusted Advisor.
10. Faça auditoria sem practice exam.

## 13. Ligações

- Identidade limita o principal.
- Rede limita o caminho.
- Criptografia protege dados.
- Observabilidade fornece evidência.
- Resiliência atende objetivos.
- Performance deve ser medida.
- Custo inclui recursos ociosos.
- Simulados integram blocos.

## 14. Referências oficiais AWS

- [CloudFormation concepts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html)
- [Change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html)
- [Drift](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)
- [Service roles](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html)
- [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
- [Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)
- [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)
- [AWS Data Exports e CUR 2.0](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html)
- [O que é AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html)
- [Capacidade do AWS Outposts](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-capacity.html)
- [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [Pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html)
- [Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
- [Amazon Pinpoint end of support](https://docs.aws.amazon.com/pinpoint/latest/userguide/migrate.html)

**Referências verificadas em:** 01/08/2026.

## 15. Continue o bloco

- [Laboratório B25](../../05_Laboratorios/LAB_B25_Auditoria_Final_de_Custos_e_Cleanup.md)
- [Questões B25](../../04_Questoes_e_Revisoes/Blocos/B25_Questoes.md)
- [Gabarito B25](../../04_Questoes_e_Revisoes/Blocos/B25_Gabarito.md)
- [Checklist e revisões B25](../../06_Progresso/B25_Checklist_e_Revisoes.md)
