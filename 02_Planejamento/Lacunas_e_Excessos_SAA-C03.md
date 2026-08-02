# Lacunas, excessos e atualizações - AWS SAA-C03

**Data da análise:** 24/07/2026  
**Fontes:** currículo completo da Udemy e guia oficial vigente da AWS.

## Limite desta análise

A comparação usa os títulos das 396 aulas, porque vídeos, transcrições e slides
não estão disponíveis localmente. A ausência de um serviço no título não prova
que ele não seja citado dentro de outra aula. Por isso, os itens abaixo são
marcados como **não explícitos no currículo** e devem ser confirmados durante a
produção do capítulo correspondente.

As listas oficiais de serviços são não exaustivas e sujeitas a mudança. A
correspondência com os conhecimentos e habilidades das 14 tarefas tem
precedência sobre a simples presença ou ausência de um nome.

## Cobertura forte do curso

O currículo apresenta cobertura explícita e extensa das áreas centrais:

- IAM, múltiplas contas, IAM Identity Center, Directory Service e Control Tower;
- EC2, EBS, EFS, ELB, Auto Scaling e opções de compra;
- RDS, Aurora, DynamoDB, ElastiCache e bancos purpose-built;
- Route 53, CloudFront, Global Accelerator, VPC, VPN e Direct Connect;
- S3, classes de armazenamento, ciclo de vida, criptografia e replicação;
- SQS, SNS, EventBridge, Kinesis, Data Firehose e Amazon MQ;
- ECS, ECR, EKS, Fargate, Lambda, API Gateway e Step Functions;
- Athena, Redshift, OpenSearch, EMR, Glue, Lake Formation e MSK;
- CloudWatch, CloudTrail e AWS Config;
- KMS, Secrets Manager, ACM, CloudHSM, WAF, Shield, GuardDuty, Inspector e Macie;
- disaster recovery, DMS, AWS Backup, Application Migration Service e DataSync;
- CloudFormation, Systems Manager, Cost Explorer e Well-Architected.

A matriz inicial associa todas as 14 tarefas oficiais a pelo menos uma aula
principal. Isso confirma cobertura estrutural, mas não mede profundidade.

## Complementos prioritários

Os temas a seguir são citados no blueprint ou na lista oficial em escopo, mas
não aparecem de forma explícita nos títulos. Devem receber cápsulas específicas
no Guia ou ser confirmados dentro de aulas relacionadas.

### Prioridade alta

| Tema/serviço | Motivo | Local planejado no Guia |
|---|---|---|
| AWS X-Ray | Workload visibility e troubleshooting aparecem na tarefa 2.2 | Observabilidade e resiliência |
| Service Quotas e throttling | Conhecimento explícito da tarefa 2.2 | Resiliência, Lambda, APIs e mensageria |
| AWS Resource Access Manager (AWS RAM) | Serviço oficial em escopo e importante em ambientes multi-account | IAM avançado e VPC |
| AWS Security Hub e Amazon Detective | Serviços de segurança oficialmente em escopo | Segurança e resposta a ameaças |
| AWS Artifact e AWS Audit Manager | Compliance e governança de dados | Segurança e conformidade |
| AWS Compute Optimizer | Decisões de sizing e custo | Cost optimization |
| AWS Cost and Usage Report | Ferramenta oficial de custos | Cost optimization |
| Savings Plans | Opção de compra explicitamente relevante | EC2 e cost optimization |
| AWS Client VPN | Opção oficial de conectividade | VPC e conectividade híbrida |
| AWS PrivateLink | Endpoints privados e acesso a serviços | VPC endpoints e segurança |
| Amazon Aurora Serverless | Escolha de banco serverless e custo | Bancos de dados |
| AWS AppSync | Integração e serverless oficialmente em escopo | Serverless e APIs |

### Prioridade complementar

- AWS Data Exchange.
- AWS Serverless Application Repository.
- AWS Wavelength.
- Amazon ECS Anywhere.
- Amazon EKS Anywhere e Amazon EKS Distro.
- AWS Device Farm.
- AWS Health Dashboard.
- AWS License Manager.
- Amazon Managed Grafana.
- Amazon Managed Service for Prometheus.
- AWS Service Catalog.
- Amazon Elastic Transcoder.
- Amazon Kinesis Video Streams.

Esses serviços devem ser apresentados por caso de uso e comparação, sem
transformar o Guia em catálogo. A profundidade será reduzida quando não houver
ligação forte com uma habilidade oficial.

## Conteúdo explicitamente fora do escopo

Segundo a lista oficial consultada em 24/07/2026:

| Aula | Conteúdo | Ação |
|---:|---|---|
| 23 | AWS CloudShell: Region Availability | Pular ou consumir por interesse operacional |
| 24 | AWS CloudShell | Pular ou consumir por interesse operacional |
| 261 | Amazon Personalize | Pular para fins de prova |

A aula 18 mistura access keys, AWS CLI e SDK. Access keys e AWS CLI continuam
relevantes, mas AWS Tools and SDKs constam na lista oficial fora do escopo. A
aula deve ser estudada seletivamente.

## Conteúdo não listado que exige prioridade reduzida

Os itens abaixo não foram tratados automaticamente como fora do escopo, pois as
listas oficiais são não exaustivas. Eles permanecerão como complementares até a
validação do capítulo:

- Amazon RDS Custom.
- Amazon Timestream.
- Amazon Managed Service for Apache Flink.
- Amazon Comprehend Medical.
- Amazon Connect na aula de Lex.
- Amazon S3 Object Lambda.
- VPC Traffic Mirroring.
- CloudWatch Logs Live Tail.
- CloudWatch Network Synthetic Monitor.
- Amazon SES.
- Amazon Pinpoint.
- AWS Cost Anomaly Detection.
- Instance Scheduler on AWS.

## Nomenclatura e atualização

- O curso usa **QuickSight**, enquanto o guia oficial SAA-C03 vigente lista
  **Amazon QuickSuite**. A documentação atual do produto usa **Amazon Quick** e
  mantém **Amazon Quick Sight** como o componente de business intelligence e
  visualização. O Guia registra as três formas antes de ensinar o tópico:
  [domínio 3 do SAA-C03](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html)
  e [documentação Amazon Quick](https://docs.aws.amazon.com/quick/).
- O título da seção 17 usa “Active MQ”, mas a aula e o nome correto do serviço
  são **Amazon MQ**.
- A descrição comercial do curso ainda contém histórico e frases sobre
  SAA-C02, apesar de o currículo e o título atuais serem SAA-C03.
- Valores, limites, interfaces e recomendações de arquitetura nunca serão
  copiados do histórico comercial sem validação oficial.

## Lacuna pedagógica mais importante

O curso é organizado principalmente por serviço. A prova exige decisões que
atravessam vários serviços. O Guia deverá acrescentar sínteses transversais que
não aparecem como uma seção única:

1. cost optimization de storage, compute, database e network;
2. escolha por requisito entre segurança, resiliência, desempenho, custo e
   esforço operacional;
3. RTO/RPO e escolha de estratégia de disaster recovery;
4. arquiteturas multi-account e governança;
5. service quotas, throttling e mitigação de single points of failure;
6. leitura de cenários e palavras decisivas em inglês;
7. comparação de soluções gerenciadas com alternativas autogerenciadas.

## Ações aprovadas

- Manter a sequência da Udemy para o cronograma.
- Usar a matriz oficial para reorganizar revisão e questões.
- Acrescentar os complementos prioritários nos capítulos correspondentes.
- Reduzir tempo de conteúdo explicitamente fora do escopo.
- Validar nomes, limites e recomendações na documentação oficial durante a
  produção de cada capítulo.
- Reavaliar esta análise quando a AWS atualizar o guia ou as listas de serviços.

## Fontes oficiais

- [Guia do exame SAA-C03](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html)
- [Serviços em escopo](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html)
- [Serviços fora do escopo](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-out-of-scope-services.html)
