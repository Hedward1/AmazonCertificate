# B20 — Observabilidade, auditoria, Config e introdução a Organizations

**Data planejada:** 17/08/2026<br>
**Nível:** iniciante absoluto<br>
**Comece pelas aulas da Udemy:** [roteiro B20 — aulas 264–282](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b20); Nenhuma aula é pulada.<br>
**Quizzes:** Q21<br>
**Domínios oficiais:** 1 — Secure; 2 — Resilient<br>
**Tarefas:** 1.2 e 2.2 principais; 1.3, 2.1 e 1.1 secundárias<br>
**Pré-requisito:** B19 — analytics, streaming e AI/ML

## 1. Objetivos de aprendizagem

1. Distinguir métricas, logs e eventos.
2. Configurar mentalmente um CloudWatch alarm.
3. Explicar métricas padrão e customizadas.
4. Identificar quando usar CloudWatch agent.
5. Rotejar eventos com EventBridge.
6. Usar CloudTrail para atividade de API.
7. Usar Config para configuração e compliance.
8. Comparar CloudWatch, CloudTrail e Config.
9. Explicar Event history e trail.
10. Reconhecer Organizations, root, OU e accounts.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 264–275 | CloudWatch e EventBridge; prática limitada a leitura |
| 276–281 | CloudTrail, Config e comparação; alta prioridade |
| 282 | Organizations; introdução, aprofundamento no B21 |
| Q21 | Fazer após recuperação ativa |

Use as aulas para o primeiro mapa, este capítulo para consolidar decisões, o laboratório para praticar e as questões para diagnosticar lacunas.

## 3. Vocabulário essencial

| Termo | Significado no cenário |
|---|---|
| metric | série temporal |
| namespace | contêiner de métricas |
| dimension | par nome/valor que identifica métrica |
| alarm | avalia métrica por janela |
| log group | grupo com retenção e permissões |
| event bus | roteador de eventos |
| rule | padrão que seleciona eventos |
| target | destino da regra |
| management event | atividade de controle/API |
| configuration item | estado registrado de recurso |

## 4. Modelo mental

Para cada cenário, siga esta sequência:

1. identifique o requisito principal;
2. marque restrições e superlativos;
3. determine escopo regional, zonal ou global;
4. avalie segurança e resiliência;
5. avalie performance e escala;
6. compare operação e custo;
7. elimine opções que violam uma restrição;
8. escolha serviço e configuração.

## 5. Fundamentos e decisões

### 5.1 Ponto 1

CloudWatch é o centro de observabilidade operacional.
### 5.2 Ponto 2

Métricas são séries temporais organizadas em namespaces.
### 5.3 Ponto 3

Dimensões identificam combinações específicas.
### 5.4 Ponto 4

Alarm avalia períodos, threshold e quantidade de pontos.
### 5.5 Ponto 5

Estados comuns são OK, ALARM e INSUFFICIENT_DATA.
### 5.6 Ponto 6

Métricas padrão variam por serviço.
### 5.7 Ponto 7

EC2 expõe CPU e rede do hypervisor por padrão.
### 5.8 Ponto 8

Memória e disco do sistema operacional exigem agente ou publicação customizada.
### 5.9 Ponto 9

CloudWatch agent coleta métricas e logs do sistema.
### 5.10 Ponto 10

Logs usam log groups, streams e eventos.
### 5.11 Ponto 11

Defina retenção para evitar armazenamento indefinido.
### 5.12 Ponto 12

Logs Insights consulta logs e pode cobrar por dados examinados.
### 5.13 Ponto 13

Metric filters transformam padrões de log em métricas.
### 5.14 Ponto 14

EventBridge recebe eventos em event buses.
### 5.15 Ponto 15

Rules filtram por padrão e enviam a targets.
### 5.16 Ponto 16

Targets precisam de permissões apropriadas.
### 5.17 Ponto 17

Retries e DLQ devem ser planejados para eventos críticos.
### 5.18 Ponto 18

EventBridge Scheduler é preferível para novas agendas em escala.
### 5.19 Ponto 19

CloudTrail registra atividade de API e da conta.
### 5.20 Ponto 20

Event history oferece 90 dias de management events por Region.
### 5.21 Ponto 21

Um trail entrega eventos continuamente ao S3.
### 5.22 Ponto 22

Data events têm alto volume e seleção/custo próprios.
### 5.23 Ponto 23

CloudTrail responde quem chamou uma API.
### 5.24 Ponto 24

AWS Config registra configuração e relacionamento de recursos habilitados.
### 5.25 Ponto 25

Config rules avaliam compliance.
### 5.26 Ponto 26

NON_COMPLIANT não bloqueia a mudança sozinho.
### 5.27 Ponto 27

CloudWatch mede comportamento; CloudTrail registra ação; Config registra estado.
### 5.28 Ponto 28

Organizations centraliza contas e consolidated billing.
### 5.29 Ponto 29

OUs agrupam contas para governança.
### 5.30 Ponto 30

Não criar organização ou Config organization-wide para praticar.

### Cápsula de decisão — AWS X-Ray

- **Problema resolvido:** seguir uma request por serviços e dependências para
  localizar erro, throttling ou latência em uma aplicação distribuída.
- **Relação SAA-C03:** tarefa 2.2 — validar dependências e pontos de falha de uma
  arquitetura resiliente.
- **Quando escolher:** métricas agregadas mostram degradação, mas é necessário
  ver traces, segmentos e o trace map por request.
- **Quando não escolher:** CloudTrail responde quem chamou uma API; CloudWatch
  metrics/alarms respondem saúde agregada; nenhum deles é substituído pelo X-Ray.
- **Serviço semelhante:** CloudWatch Application Signals, voltado a serviços,
  SLOs e saúde; X-Ray fornece o detalhe do trace correlacionado.
- **Armadilha:** sampling significa que nem toda request será registrada e a
  aplicação precisa de instrumentação. Para código novo, prefira OpenTelemetry;
  os SDKs e o daemon próprios do X-Ray estão em maintenance mode desde
  25/02/2026.
- **Questão situacional extra (fora do banco de 250):** uma chamada passa por API, Lambda e banco, mas
  só 2% ficam lentas. **Resposta curta:** instrumente com OpenTelemetry e envie
  traces ao X-Ray; use o trace map para localizar o segmento lento.
- **Referência oficial:** [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) e [migração para OpenTelemetry](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-migration.html).

### Cápsula de decisão — AWS Security Hub

- **Problema resolvido:** correlacionar e priorizar sinais de segurança de
  múltiplas fontes em contas e Regions para orientar resposta.
- **Relação SAA-C03:** tarefa 1.2 — proteção e operação segura de workloads.
- **Quando escolher:** GuardDuty, Inspector, Macie, IAM Access Analyzer e outros
  geram findings que precisam de visão e workflows centralizados; habilite
  Security Hub CSPM também quando quiser standards e control checks.
- **Quando não escolher:** ele não substitui o serviço que detecta a ameaça nem
  um SIEM/data lake quando o requisito é guardar e consultar todo evento bruto.
- **Serviço semelhante:** GuardDuty detecta atividade potencialmente maliciosa;
  Security Hub reúne/correlaciona findings e exposures.
- **Armadilha:** finding não é remediação nem prova automática de compliance;
  configuração central, cobertura regional, integrações e custo precisam ser
  planejados.
- **Questão situacional extra (fora do banco de 250):** uma empresa recebe findings de GuardDuty,
  Inspector e Macie e quer priorizar riscos correlacionados. **Resposta curta:**
  AWS Security Hub; acrescente Security Hub CSPM para standards e controles.
- **Referência oficial:** [Introduction to AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html).

### Cápsula de decisão — AWS Artifact

- **Problema resolvido:** obter relatórios/certificações de segurança e
  compliance da infraestrutura AWS e gerenciar acordos com a AWS.
- **Relação SAA-C03:** tarefas 1.2 e 1.3 — evidência do provedor e controles de
  segurança/compliance sob responsabilidade compartilhada.
- **Quando escolher:** auditor solicita SOC, ISO, PCI ou outro documento da AWS,
  ou a organização precisa revisar/aceitar um acordo disponível no portal.
- **Quando não escolher:** para provar como a própria conta configurou recursos
  ou coletar evidência contínua do workload, use Audit Manager/Config/CloudTrail.
- **Serviço semelhante:** AWS Audit Manager, que organiza evidência sobre o uso
  da AWS pelo cliente; Artifact entrega documentos e acordos do provedor.
- **Armadilha:** relatórios podem ser confidenciais e receber watermark; baixe e
  compartilhe somente conforme os termos. Artifact não transfere ao provedor a
  responsabilidade pelos controles do cliente.
- **Questão situacional extra (fora do banco de 250):** o auditor pede o relatório SOC da AWS, não a
  configuração das suas instâncias. **Resposta curta:** baixe-o no AWS Artifact
  com permissões e tratamento seguro.
- **Referência oficial:** [What is AWS Artifact?](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html).

### Cápsula de decisão — AWS Audit Manager

- **Problema resolvido:** estruturar assessments por frameworks/controls e
  coletar continuamente evidências automáticas e manuais para auditorias.
- **Relação SAA-C03:** tarefas 1.2 e 1.3 — demonstrar a operação de controles do
  cliente, sem confundir evidência com garantia jurídica.
- **Quando escolher:** contas e serviços em escopo precisam de evidência
  recorrente de Config, CloudTrail, Security Hub CSPM e APIs, além de revisão por
  stakeholders e relatório de assessment.
- **Quando não escolher:** para obter certificações SOC/ISO da AWS, use Artifact;
  para bloquear uma mudança, use preventive guardrails/policies.
- **Serviço semelhante:** AWS Config avalia configuração de recursos; Audit
  Manager agrega diferentes fontes como evidência de controles de auditoria.
- **Armadilha:** o serviço auxilia a coleta, mas não declara compliance e pode
  exigir evidência manual. Assessment ativo continua coletando evidência e pode
  gerar custo.
- **Questão situacional extra (fora do banco de 250):** PCI exige um pacote recorrente de evidências da
  configuração e atividade das contas. **Resposta curta:** Audit Manager com
  framework/assessment e escopo definidos; complete lacunas manualmente.
- **Referência oficial:** [What is AWS Audit Manager?](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html).

## 6. Tabela de decisão

| Requisito dominante | Escolha inicial | Motivo |
|---|---|---|
| CPU alta e alerta | CloudWatch metric e alarm | sinal operacional |
| Memória do EC2 | CloudWatch agent | dado do guest OS |
| Erros da aplicação | CloudWatch Logs | conteúdo de log |
| Mudança de estado | EventBridge | roteamento de evento |
| Quem excluiu recurso | CloudTrail | autoria de API |
| Histórico de SG | AWS Config | timeline de configuração |
| Compliance de configuração | Config rule | avalia estado |
| Trace de uma request distribuída | X-Ray com OpenTelemetry | encontra latência/erro por segmento |
| Correlacionar findings de segurança | AWS Security Hub | prioriza sinais e exposures |
| Relatório SOC/ISO da AWS | AWS Artifact | documento do provedor |
| Evidência contínua para auditoria | AWS Audit Manager | framework, controls e assessment |
| 90 dias de management events | CloudTrail Event history | consulta regional |
| Retenção longa de auditoria | Trail para S3 | entrega contínua |
| Agrupar contas | Organizations e OUs | governança multi-account |

## 7. Cenários resolvidos


### Cenário resolvido 1 — CPU alta

- **Contexto:** Aplicação precisa alertar após três períodos acima de 80%.
- **Requisito:** Notificação operacional com janela explícita.
- **Decisão:** CloudWatch metric, alarm e target de notificação.
- **Por quê:** CloudWatch avalia séries temporais.
- **Por que não:** CloudTrail não mede CPU.
- **Trade-off:** Períodos curtos e métricas customizadas aumentam custo e ruído.
- **Validação:** Testar mudança de estado e recuperação.
- **Custo/cleanup:** Alarm e notificações conforme preços.
- **Variação:** Composite alarm reduz ruído de múltiplos sinais.

### Cenário resolvido 2 — Security group aberto

- **Contexto:** Uma regra administrativa ficou ampla.
- **Requisito:** Descobrir autor e configuração resultante.
- **Decisão:** CloudTrail para API; Config para timeline/compliance.
- **Por quê:** Os serviços respondem perguntas complementares.
- **Por que não:** CloudWatch CPU não mostra autoria ou estado de configuração.
- **Trade-off:** Registrar mais recursos/eventos aumenta custo.
- **Validação:** Correlacionar timestamp, event name e configuration item.
- **Custo/cleanup:** Config items e trail/log storage podem cobrar.
- **Variação:** EventBridge pode disparar automação após evento.

### Cenário resolvido 3 — Automação por evento

- **Contexto:** Instância entra no estado stopped.
- **Requisito:** Criar ticket automaticamente.
- **Decisão:** EventBridge rule para target apropriado.
- **Por quê:** O evento pode ser filtrado e roteado sem polling.
- **Por que não:** Log group sozinho não executa target.
- **Trade-off:** Entrega assíncrona exige idempotência, retry e DLQ.
- **Validação:** Testar padrão com evento de amostra.
- **Custo/cleanup:** Targets e logs associados podem cobrar.
- **Variação:** Use Scheduler se a necessidade for horário, não mudança de estado.

## 8. Fluxo de projeto

1. Definir pergunta operacional.
2. Escolher sinal mensurável.
3. Identificar namespace e dimensões.
4. Escolher período e estatística.
5. Definir threshold e missing data.
6. Definir target e permissões.
7. Definir logs e retenção.
8. Definir auditoria de API.
9. Definir histórico de configuração.
10. Planejar retry e DLQ.
11. Testar alerta de ponta a ponta.
12. Revisar custo e ruído.

## 9. Custos e cleanup

- Métricas customizadas geram cobrança.
- Logs cobram ingestão, armazenamento e consulta.
- Alarms e chamadas podem cobrar.
- Trails, data events, S3 e KMS podem cobrar.
- Event history não exige criar trail.
- Config cobra itens e avaliações.
- EventBridge targets podem gerar custo downstream.
- Não habilitar recursos organization-wide no laboratório.

Faça inventário antes e depois. Exclua somente recursos criados por você e identificados pelo bloco. Nunca tente zerar a conta removendo recursos preexistentes.

## 10. Armadilhas de prova

- CloudWatch não substitui CloudTrail.
- CloudTrail não mede saúde da aplicação.
- Config detecta; não bloqueia automaticamente.
- EventBridge roteia; não é armazenamento de logs.
- Event history não equivale a trail durável.
- Memória EC2 não é métrica padrão.
- INSUFFICIENT_DATA não prova falha.
- Data events não são todos gratuitos.
- Alarm sem ação não notifica.
- Organization muda governança e billing.

## 11. Checklist de domínio

- [ ] Consigo explicar os objetivos sem consultar.
- [ ] Reconstruo a tabela de decisão.
- [ ] Resolvo os três cenários.
- [ ] Sei justificar duas alternativas erradas.
- [ ] Conheço custos residuais.
- [ ] Completei o laboratório.
- [ ] Respondi às dez questões antes do gabarito.
- [ ] Registrei erros e baixa confiança.
- [ ] Agendei D+2 e D+7.

## 12. Recuperação ativa

1. Compare os três serviços principais.
2. Explique namespace e dimensão.
3. Por que memória exige agente?
4. Desenhe bus, rule e target.
5. Compare Event history e trail.
6. Compare management e data events.
7. Explique Config rule.
8. Dê exemplo de NON_COMPLIANT.
9. Desenhe root, OU e accounts.
10. Liste custos de observabilidade.

## 13. Ligações com outros blocos

- A identidade limita quem inicia a operação.
- A rede limita por onde o dado passa.
- A criptografia protege conteúdo e chaves.
- A observabilidade prova comportamento e mudanças.
- Resiliência deve corresponder ao objetivo do negócio.
- Custo deve incluir recursos ociosos e tráfego.
- Operação gerenciada reduz tarefas, mas não remove responsabilidade.
- Os simulados combinam estes conceitos.

## 14. Referências oficiais AWS

- [CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)
- [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
- [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
- [EventBridge concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is-how-it-works-concepts.html)
- [CloudTrail concepts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html)
- [Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)
- [AWS Config concepts](https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html)
- [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [X-Ray SDK/daemon support timeline](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html)
- [AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html)
- [Security Hub e Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html)
- [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)
- [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)

**Referências verificadas em:** 01/08/2026.

## 15. Continue o bloco

- [Laboratório B20](../../05_Laboratorios/LAB_B20_CloudWatch_CloudTrail_e_Config_Read_Only.md)
- [Questões B20](../../04_Questoes_e_Revisoes/Blocos/B20_Questoes.md)
- [Gabarito B20](../../04_Questoes_e_Revisoes/Blocos/B20_Gabarito.md)
- [Checklist e revisões B20](../../06_Progresso/B20_Checklist_e_Revisoes.md)
