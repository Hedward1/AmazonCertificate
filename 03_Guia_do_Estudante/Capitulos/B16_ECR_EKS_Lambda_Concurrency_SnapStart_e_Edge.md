# B16 — ECR, EKS, Lambda, concurrency, SnapStart e edge

**Data planejada:** 12/08/2026<br>
**Comece pelas aulas:** [roteiro B16 — aulas 203–216](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b16); faça `Q15`<br>
**Domínios:** 2 — Resilient; 3 — High-Performing<br>
**Tarefas principais:** 2.1 e 3.2<br>
**Tarefas secundárias:** 1.2, 3.3, 4.2 e 4.3<br>
**Pré-requisito:** B15 — containers e ECS

## 1. Objetivos de aprendizagem

Ao concluir, você deverá:

1. escolher ECS/Fargate, EKS ou Lambda;
2. explicar registry, repository, tag, digest e lifecycle no ECR;
3. reconhecer o custo/control plane do EKS;
4. descrever o ciclo de invocação e execution environment do Lambda;
5. aplicar timeout, memory, ephemeral storage e quotas sem decorar valores velhos;
6. diferenciar reserved e provisioned concurrency;
7. explicar throttling e downstream protection;
8. reconhecer quando SnapStart reduz cold starts;
9. comparar Lambda@Edge e CloudFront Functions;
10. executar e limpar uma função mínima com menor privilégio.

## 2. Aulas deste bloco

| Aulas | Foco |
|---|---|
| 203–204 | padrões ECS e cleanup completo |
| 205 | ECR, image security e lifecycle |
| 206–207 | EKS, Kubernetes e custo do control plane; hands-on só walkthrough |
| 208–210 | serverless e modelo do Lambda |
| 211–214 | hands-on, quotas e concurrency |
| 215 | SnapStart e cold start |
| 216 | Lambda@Edge versus CloudFront Functions |

## 3. ECR e supply chain de images

Amazon ECR é um registry gerenciado. Um **repository** agrupa images; uma tag é
um rótulo mutável; um **digest** identifica conteúdo imutável.

Boas práticas:

- deployment de produção por digest ou tag imutável;
- scanning básico/aprimorado conforme risco;
- encryption e repository policy de menor privilégio;
- lifecycle policy para remover images antigas;
- autenticação temporária, nunca password em arquivo;
- replicação cross-Region/account quando o RTO exige;
- assinatura/verificação de artifacts conforme supply chain.

Uma lifecycle policy pode excluir a única image necessária para rollback se a
regra não preservar releases. Tags mutáveis como `latest` prejudicam
reprodutibilidade.

## 4. EKS: quando Kubernetes é requisito

Amazon EKS fornece um control plane Kubernetes gerenciado. Você ainda escolhe:

- managed node groups, self-managed nodes ou Fargate;
- networking/pod IPs, ingress/load balancer e storage classes;
- add-ons, version upgrades, policies e observabilidade;
- IAM roles for service accounts ou EKS Pod Identity;
- autoscaling de pods e nodes.

EKS é indicado quando o requisito dominante é Kubernetes: APIs/ecossistema,
portabilidade ou plataforma organizacional já padronizada. ECS é mais simples
para containers AWS-native sem esse requisito. EKS tem cobrança de control
plane por cluster, além do compute e dos recursos auxiliares; não o crie apenas
para conhecer o console.

### Cenário resolvido 1 — “precisamos de containers”

Uma equipe pequena quer executar uma API containerizada sem gerenciar hosts e
não usa Kubernetes. Escolha **ECS on Fargate**. EKS on Fargate também evita
nodes, mas adiciona Kubernetes/control plane sem requisito. Se a aplicação for
event-driven, curta e compatível com Lambda, compare operação e custo antes de
preservar o container.

## 5. Modelo do Lambda

Lambda executa código em resposta a events sem servidor provisionado pelo
cliente. Uma invocação usa um execution environment:

```text
download/configuração -> init -> invoke -> ambiente pode ser reutilizado
                                ^ cold start na primeira preparação
```

Inicialize SDK clients/conexões reutilizáveis fora do handler, mas nunca suponha
que o mesmo ambiente sobreviverá. `/tmp` pode persistir no ambiente aquecido,
mas não é um banco durável. Código deve ser stateless e idempotente quando a
origem entrega ao menos uma vez.

### 5.1 Configuração e limites

- timeout máximo de uma invocação de **Lambda Function padrão**: 15 minutos;
- memory também aloca CPU proporcionalmente;
- ephemeral storage `/tmp` é configurável dentro dos limites atuais;
- deployment package/container image tem quotas próprias;
- environment variables não devem armazenar plaintext secrets;
- execution role fornece permissões do código;
- resource-based policy autoriza quem invoca.

Na documentação vigente em 2026, “AWS Lambda” também inclui **Durable
Functions**, cujas execuções com checkpoints podem durar até um ano, e **Lambda
MicroVMs**, com sessões de até oito horas. Esses modelos não aumentam para 40
minutos o timeout de uma invocação de Lambda Function padrão. Neste bloco e nas
aulas do curso, “Lambda” sem qualificador significa a função event-driven
padrão; em projetos atuais, identifique explicitamente o modelo de execução
avaliado.

Para processamento longo, stateful ou com controle de runtime/host, use
containers/EC2/Batch/Step Functions conforme o requisito.

### Cenário resolvido 2 — trabalho de 40 minutos

Um job determinístico leva 40 minutos e não pode ser dividido. Uma Lambda
Function padrão não atende ao timeout máximo. Use ECS/Fargate, AWS Batch ou EC2
conforme scheduling e controle; em uma avaliação atual fora do escopo do curso,
compare também Lambda MicroVMs. Aumentar memory pode acelerar alguns jobs, mas
não altera o teto de 15 minutos por invocação da função padrão.

## 6. Concurrency e scaling

**Concurrency** é a quantidade de invocações em processamento ao mesmo tempo.

```text
concurrency aproximada = requests por segundo × duração média em segundos
```

100 requests/s × 2 s ≈ 200 execuções concorrentes. Essa estimativa permite
dimensionar quota e proteger banco/API downstream.

| Controle | O que faz | Uso típico |
|---|---|---|
| account concurrency quota | pool regional compartilhado | capacidade total |
| reserved concurrency | reserva e também limita a função | garantir capacidade e limitar downstream |
| provisioned concurrency | ambientes pré-inicializados | reduzir cold-start previsivelmente |
| event-source maximum concurrency | limita consumo daquela origem | proteger downstream por trigger |

Reserved concurrency não mantém ambientes aquecidos; provisioned concurrency
não substitui permissões nem código eficiente e gera custo enquanto alocada.
Quando a quota é excedida, invocações síncronas recebem throttling; fontes
assíncronas/queues aplicam retry conforme sua integração. Projete DLQ/destination
e idempotência.

### Cenário resolvido 3 — banco com 100 conexões

Uma função pode escalar rapidamente, mas o banco tolera só 100 conexões. Defina
reserved/maximum concurrency compatível, reutilize conexões, considere RDS
Proxy e use SQS para amortecer picos. Provisioned concurrency reduziria cold
start, mas não limitaria por si o dano ao banco.

## 7. Cold starts e SnapStart

Cold start inclui preparar runtime e executar initialization code. Mitigações:

- reduzir package/dependencies e init;
- escolher memory adequada;
- evitar VPC quando não necessária e otimizar conexões quando for;
- provisioned concurrency para latência previsível;
- SnapStart em runtime compatível.

SnapStart cria um snapshot criptografado do ambiente inicializado ao publicar
uma version e restaura cópias a partir dele. O código precisa tratar unicidade,
randomness, sockets e secrets que possam ficar “congelados”; use runtime hooks
quando necessário. Verifique runtimes/Regions atuais em vez de assumir que toda
linguagem é compatível.

Na documentação consultada em 01/08/2026, os managed runtimes compatíveis são
Java 11+, Python 3.12+ e .NET 8+. SnapStart exige version publicada/alias, não
funciona em `$LATEST` nem em container image e não pode ser combinado com
provisioned concurrency, EFS, S3 Files ou `/tmp` maior que 512 MB.

Provisioned concurrency mantém ambientes prontos e cobra capacidade provisionada.
SnapStart reduz initialization em versões compatíveis e tem modelo/limitações
próprios. São decisões diferentes.

## 8. Edge compute

| Critério | CloudFront Functions | Lambda@Edge |
|---|---|---|
| events | viewer request/response | viewer e origin request/response |
| runtime | JavaScript leve do CloudFront | Node.js/Python conforme suporte |
| duração/recursos | muito curta e limitada | mais recursos e tempo |
| network/file access | não | network disponível em eventos/limites compatíveis |
| escala/custo | altíssima escala e baixo custo | lógica mais complexa, custo maior |
| caso | header, redirect, URL rewrite, cache key | auth avançada, origin logic, network call |

Lambda@Edge é criado/publicado na Region exigida pelo serviço e replicado ao
associar à distribuição. Não trate réplicas como funções regionais independentes.

### Cenário resolvido 4 — redirect versus validação externa

Normalizar URL e adicionar um header em viewer request cabe em CloudFront
Functions. Validar token chamando um endpoint externo e alterar a origin requer
Lambda@Edge, respeitando event type e quotas. Usar Lambda@Edge para cada redirect
simples aumenta latência/custo sem benefício.

## 9. Tabela de decisão

| Requisito dominante | Escolha inicial |
|---|---|
| evento curto, stateless, escala rápida | Lambda |
| container, processo longo/custom runtime | ECS/Fargate |
| Kubernetes/ecossistema K8s | EKS |
| viewer manipulation muito leve | CloudFront Functions |
| lógica edge mais rica/origin event | Lambda@Edge |
| latência de init previsível | provisioned concurrency ou SnapStart compatível |
| limitar pressão no downstream | reserved/max concurrency + buffer |

## 10. Segurança, custos e cleanup

- execution role mínima, sem wildcard desnecessário;
- resource policy apenas para invokes esperados;
- code signing/scanning e dependencies atualizadas;
- secrets em Secrets Manager/Parameter Store, não em logs/env plaintext;
- logs com retenção explícita e dados saneados;
- VPC adiciona ENIs, subnets/routes e possível NAT cost.

Lambda cobra requests, duration e recursos adicionais; provisioned concurrency
cobra enquanto configurada. ECR cobra storage/scanning/transfer; EKS cobra
control plane e compute. CloudWatch Logs persiste após excluir função. Cleanup
deve remover function versions/aliases, event sources, provisioned concurrency,
log group, role/policies exclusivas, ECR images/repos e stacks auxiliares.

## 11. Armadilhas e recuperação ativa

- serverless não significa sem limites ou sem custo ocioso de configurações;
- reserved concurrency limita/reserva; provisioned reduz cold start;
- invocação de Lambda Function padrão não ultrapassa 15 min; Durable Functions e
  MicroVMs são modelos diferentes;
- task execution role do ECS não é Lambda execution role conceitualmente;
- EKS é Kubernetes gerenciado, não “containers grátis”;
- SnapStart exige runtime e código compatíveis;
- CloudFront Functions não faz chamadas de rede.

Recupere: matriz ECS/EKS/Lambda; cálculo de concurrency; três soluções para cold
start; roles/policies; edge comparison; lista completa de cleanup.

## 12. Ligações

- [Laboratório B16](../../05_Laboratorios/LAB_B16_Lambda_Minima_Logs_e_Cleanup.md)
- [Questões B16](../../04_Questoes_e_Revisoes/Blocos/B16_Questoes.md)
- [Gabarito B16](../../04_Questoes_e_Revisoes/Blocos/B16_Gabarito.md)
- [Checklist B16](../../06_Progresso/B16_Checklist_e_Revisoes.md)
- Próximo: B17 — VPC, DynamoDB, API Gateway, Step Functions e Cognito.

## 13. Referências oficiais

- [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
- [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- [Modelos atuais do AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Lambda concurrency](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html)
- [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)
- [CloudFront edge functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions.html)
