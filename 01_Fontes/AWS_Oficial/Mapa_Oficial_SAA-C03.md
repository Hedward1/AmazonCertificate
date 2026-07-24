# Mapa oficial de conteúdo — AWS Certified Solutions Architect – Associate (SAA-C03)

**Finalidade:** referência oficial para mapear as 425 aulas/itens do curso, planejar o estudo e verificar lacunas de cobertura.  
**Data de consulta:** 24/07/2026.  
**Idioma deste mapa:** português, com nomes de serviços e termos importantes em inglês preservados para a realização da prova em inglês.

> Este documento traduz e organiza o guia oficial da AWS. As listas oficiais de serviços em escopo e fora do escopo são **não exaustivas** e estão sujeitas a alteração. Portanto, a ausência de um serviço nas duas listas não prova, sozinha, que ele esteja fora do exame. Para classificar uma aula, a correspondência com os conhecimentos e habilidades das 14 tarefas é o critério principal.

## Fontes oficiais

- [Guia oficial do exame SAA-C03](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html)
- [Domínio 1 — Design Secure Architectures](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html)
- [Domínio 2 — Design Resilient Architectures](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html)
- [Domínio 3 — Design High-Performing Architectures](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html)
- [Domínio 4 — Design Cost-Optimized Architectures](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html)
- [Tecnologias e conceitos](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-technologies-concepts.html)
- [Serviços AWS em escopo](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html)
- [Serviços AWS fora do escopo](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-out-of-scope-services.html)
- [Como os nomes dos serviços aparecem no exame](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-service-mentions.html)

## Visão geral do exame

O exame valida a capacidade de:

- projetar soluções com serviços AWS para requisitos atuais e necessidades futuras;
- projetar arquiteturas seguras, resilientes, de alto desempenho e otimizadas em custo;
- revisar soluções existentes e determinar melhorias;
- tomar decisões de arquitetura segundo o AWS Well-Architected Framework.

O candidato-alvo oficial possui pelo menos um ano de experiência prática projetando soluções em nuvem com serviços AWS. Esse é um perfil-alvo, não uma exigência formal para iniciar a preparação.

| Domínio | Nome oficial | Peso no conteúdo pontuado | Tarefas |
|---|---|---:|---:|
| 1 | Design Secure Architectures | 30% | 3 |
| 2 | Design Resilient Architectures | 26% | 2 |
| 3 | Design High-Performing Architectures | 24% | 5 |
| 4 | Design Cost-Optimized Architectures | 20% | 4 |
| **Total** |  | **100%** | **14** |

**Validação estrutural:** 3 + 2 + 5 + 4 = **14 tarefas**.

## Domínio 1 — Projetar arquiteturas seguras (30%)

Fonte: [Content Domain 1: Design Secure Architectures](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html).

### Tarefa 1.1 — Projetar acesso seguro aos recursos AWS

Nome oficial: **Design secure access to AWS resources**.

**Conhecimentos**

- Controles de acesso e gerenciamento em múltiplas contas.
- Serviços de identidade e acesso federado da AWS, como IAM e AWS IAM Identity Center.
- Infraestrutura global da AWS, como Availability Zones e AWS Regions.
- Boas práticas de segurança da AWS, como o princípio do menor privilégio.
- Modelo de responsabilidade compartilhada da AWS.

**Habilidades**

- Aplicar boas práticas de segurança a usuários IAM e ao usuário root, incluindo multi-factor authentication (MFA).
- Projetar um modelo de autorização flexível com usuários, grupos, roles e policies do IAM.
- Projetar uma estratégia de role-based access control, incluindo AWS STS, troca de roles e acesso entre contas.
- Projetar uma estratégia de segurança para múltiplas contas, incluindo AWS Control Tower e service control policies (SCPs).
- Determinar o uso apropriado de resource policies nos serviços AWS.
- Determinar quando federar um serviço de diretório com IAM roles.

### Tarefa 1.2 — Projetar workloads e aplicações seguras

Nome oficial: **Design secure workloads and applications**.

**Conhecimentos**

- Segurança da configuração e das credenciais de aplicações.
- Endpoints de serviços AWS.
- Controle de portas, protocolos e tráfego de rede na AWS.
- Acesso seguro a aplicações.
- Serviços de segurança e seus casos de uso, como Amazon Cognito, Amazon GuardDuty e Amazon Macie.
- Vetores de ameaça externos à AWS, como DDoS e SQL injection.

**Habilidades**

- Projetar arquiteturas de VPC com componentes de segurança, incluindo security groups, route tables, network ACLs e NAT gateways.
- Determinar estratégias de segmentação de rede, incluindo public subnets e private subnets.
- Integrar serviços AWS para proteger aplicações, incluindo AWS Shield, AWS WAF, IAM Identity Center e AWS Secrets Manager.
- Proteger conexões de rede externas de entrada e saída da AWS Cloud, incluindo VPN e AWS Direct Connect.

### Tarefa 1.3 — Determinar controles apropriados de segurança de dados

Nome oficial: **Determine appropriate data security controls**.

**Conhecimentos**

- Acesso e governança de dados.
- Recuperação de dados.
- Retenção e classificação de dados.
- Criptografia e gerenciamento apropriado de chaves.

**Habilidades**

- Alinhar tecnologias AWS a requisitos de conformidade.
- Criptografar dados em repouso, incluindo o uso do AWS KMS.
- Criptografar dados em trânsito, incluindo TLS com AWS Certificate Manager (ACM).
- Implementar políticas de acesso para chaves de criptografia.
- Implementar backups e replicações de dados.
- Implementar políticas de acesso, ciclo de vida e proteção de dados.
- Fazer rotação de chaves de criptografia e renovação de certificados.

## Domínio 2 — Projetar arquiteturas resilientes (26%)

Fonte: [Content Domain 2: Design Resilient Architectures](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html).

### Tarefa 2.1 — Projetar arquiteturas escaláveis e fracamente acopladas

Nome oficial: **Design scalable and loosely coupled architectures**.

**Conhecimentos**

- Criação e gerenciamento de APIs, incluindo Amazon API Gateway e REST APIs.
- Serviços gerenciados da AWS e seus casos de uso, como AWS Transfer Family, Amazon SQS e AWS Secrets Manager.
- Estratégias de cache.
- Princípios de design de microsserviços, incluindo workloads stateless versus stateful.
- Arquiteturas orientadas a eventos.
- Escalabilidade horizontal e vertical.
- Uso apropriado de aceleradores de borda, como content delivery networks (CDNs).
- Migração de aplicações para containers.
- Conceitos de load balancing, como Application Load Balancer (ALB).
- Arquiteturas em múltiplas camadas (multi-tier).
- Conceitos de filas e mensageria, como publish/subscribe.
- Tecnologias e padrões serverless, como AWS Fargate e AWS Lambda.
- Tipos de armazenamento e suas características: object, file e block.
- Orquestração de containers, como Amazon ECS e Amazon EKS.
- Quando usar read replicas.
- Orquestração de workflows, como AWS Step Functions.

**Habilidades**

- Projetar arquiteturas orientadas a eventos, de microsserviços e/ou multi-tier com base em requisitos.
- Determinar estratégias de scaling para os componentes de uma arquitetura.
- Determinar quais serviços AWS fornecem loose coupling segundo os requisitos.
- Determinar quando usar containers.
- Determinar quando usar tecnologias e padrões serverless.
- Recomendar tecnologias apropriadas de compute, storage, networking e database segundo os requisitos.
- Usar serviços AWS purpose-built para os workloads.

### Tarefa 2.2 — Projetar arquiteturas altamente disponíveis e/ou tolerantes a falhas

Nome oficial: **Design highly available and/or fault-tolerant architectures**.

**Conhecimentos**

- Infraestrutura global da AWS, incluindo Availability Zones, AWS Regions e Amazon Route 53.
- Serviços gerenciados da AWS e seus casos de uso, incluindo Amazon Comprehend e Amazon Polly.
- Conceitos básicos de rede, como route tables.
- Estratégias de disaster recovery (DR): backup and restore, pilot light, warm standby e active-active failover; recovery point objective (RPO) e recovery time objective (RTO).
- Padrões de design distribuído.
- Estratégias de failover.
- Infraestrutura imutável.
- Conceitos de load balancing, como ALB.
- Conceitos de proxy, como Amazon RDS Proxy.
- Service quotas e throttling, incluindo quotas de um workload em ambiente de standby.
- Opções e características de armazenamento, como durabilidade e replicação.
- Visibilidade do workload, como AWS X-Ray.

**Habilidades**

- Determinar estratégias de automação que preservem a integridade da infraestrutura.
- Determinar os serviços AWS necessários para alta disponibilidade e/ou tolerância a falhas entre Regions ou Availability Zones.
- Identificar métricas baseadas em requisitos de negócio para entregar uma solução altamente disponível.
- Implementar designs que eliminem ou mitiguem single points of failure.
- Implementar estratégias que garantam a durabilidade e a disponibilidade dos dados, incluindo backups.
- Selecionar a estratégia de DR apropriada aos requisitos de negócio.
- Usar serviços AWS que aumentem a confiabilidade de aplicações legadas e aplicações não criadas para a nuvem, inclusive quando não for possível alterar a aplicação.
- Usar serviços AWS purpose-built para os workloads.

## Domínio 3 — Projetar arquiteturas de alto desempenho (24%)

Fonte: [Content Domain 3: Design High-Performing Architectures](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html).

### Tarefa 3.1 — Determinar soluções de armazenamento de alto desempenho e/ou escaláveis

Nome oficial: **Determine high-performing and/or scalable storage solutions**.

**Conhecimentos**

- Soluções de armazenamento híbrido que atendam aos requisitos de negócio.
- Serviços de armazenamento e seus casos de uso, como Amazon S3, Amazon EFS e Amazon EBS.
- Tipos de armazenamento e suas características: object, file e block.

**Habilidades**

- Determinar serviços e configurações de armazenamento que atendam às demandas de desempenho.
- Determinar serviços de armazenamento capazes de escalar para necessidades futuras.

### Tarefa 3.2 — Projetar soluções de compute elásticas e de alto desempenho

Nome oficial: **Design high-performing and elastic compute solutions**.

**Conhecimentos**

- Serviços de compute da AWS e seus casos de uso, como AWS Batch, Amazon EMR e AWS Fargate.
- Conceitos de computação distribuída apoiados pela infraestrutura global e pelos serviços de borda da AWS.
- Conceitos de filas e mensageria, como publish/subscribe.
- Recursos de escalabilidade e seus casos de uso, como Amazon EC2 Auto Scaling e AWS Auto Scaling.
- Tecnologias e padrões serverless, como AWS Lambda e AWS Fargate.
- Orquestração de containers, como Amazon ECS e Amazon EKS.

**Habilidades**

- Desacoplar workloads para que seus componentes escalem de forma independente.
- Identificar métricas e condições que disparem ações de scaling.
- Selecionar opções e recursos de compute apropriados, como EC2 instance types, para atender aos requisitos de negócio.
- Selecionar o tipo e o tamanho de recurso apropriados, como a quantidade de memória de uma função Lambda.

### Tarefa 3.3 — Determinar soluções de banco de dados de alto desempenho

Nome oficial: **Determine high-performing database solutions**.

**Conhecimentos**

- Infraestrutura global da AWS, incluindo Availability Zones e AWS Regions.
- Estratégias e serviços de cache, como Amazon ElastiCache.
- Padrões de acesso a dados, como workloads read-intensive versus write-intensive.
- Planejamento de capacidade de bancos de dados, incluindo capacity units, instance types e Provisioned IOPS.
- Conexões e proxies de bancos de dados.
- Database engines e seus casos de uso, incluindo migrações homogêneas e heterogêneas.
- Replicação de bancos de dados, como read replicas.
- Tipos e serviços de bancos de dados, incluindo serverless, relational versus non-relational e in-memory.

**Habilidades**

- Configurar read replicas para atender aos requisitos de negócio.
- Projetar arquiteturas de bancos de dados.
- Determinar o database engine apropriado, como MySQL versus PostgreSQL.
- Determinar o tipo de banco apropriado, como Amazon Aurora versus Amazon DynamoDB.
- Integrar cache para atender aos requisitos de negócio.

### Tarefa 3.4 — Determinar arquiteturas de rede de alto desempenho e/ou escaláveis

Nome oficial: **Determine high-performing and/or scalable network architectures**.

**Conhecimentos**

- Serviços de edge networking e seus casos de uso, como Amazon CloudFront e AWS Global Accelerator.
- Como projetar uma arquitetura de rede, incluindo camadas de subnets, routing e IP addressing.
- Conceitos de load balancing, como Application Load Balancer.
- Opções de conexão de rede, como AWS VPN, AWS Direct Connect e AWS PrivateLink.

**Habilidades**

- Criar uma topologia de rede para diferentes arquiteturas, como global, hybrid e multi-tier.
- Determinar configurações de rede capazes de escalar para necessidades futuras.
- Determinar o posicionamento apropriado dos recursos para atender aos requisitos de negócio.
- Selecionar a estratégia apropriada de load balancing.

### Tarefa 3.5 — Determinar soluções de ingestão e transformação de dados de alto desempenho

Nome oficial: **Determine high-performing data ingestion and transformation solutions**.

**Conhecimentos**

- Serviços de analytics e visualização e seus casos de uso, como Amazon Athena, AWS Lake Formation e Amazon Quick.
- Padrões de ingestão de dados, como frequência.
- Serviços de transferência de dados e seus casos de uso, como AWS DataSync e AWS Storage Gateway.
- Serviços de transformação de dados e seus casos de uso, como AWS Glue.
- Acesso seguro aos pontos de ingestão.
- Volumes e velocidades necessários para atender aos requisitos de negócio.
- Serviços de streaming de dados e seus casos de uso, como Amazon Kinesis.

**Habilidades**

- Construir e proteger data lakes.
- Projetar arquiteturas de streaming de dados.
- Projetar soluções de transferência de dados.
- Implementar estratégias de visualização.
- Selecionar opções de compute apropriadas ao processamento de dados, como Amazon EMR.
- Selecionar configurações apropriadas de ingestão.
- Transformar dados entre formatos, como `.csv` para `.parquet`.

## Domínio 4 — Projetar arquiteturas otimizadas em custo (20%)

Fonte: [Content Domain 4: Design Cost-Optimized Architectures](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html).

### Tarefa 4.1 — Projetar soluções de armazenamento otimizadas em custo

Nome oficial: **Design cost-optimized storage solutions**.

**Conhecimentos**

- Opções de acesso, como um bucket S3 com Requester Pays.
- Recursos de serviços de gerenciamento de custos, incluindo cost allocation tags e faturamento de múltiplas contas.
- Ferramentas de gerenciamento de custos e seus casos de uso, como AWS Cost Explorer, AWS Budgets e AWS Cost and Usage Report.
- Serviços de armazenamento AWS e seus casos de uso, como Amazon FSx, Amazon EFS, Amazon S3 e Amazon EBS.
- Estratégias de backup.
- Opções de block storage, incluindo tipos de volume HDD e SSD.
- Ciclos de vida dos dados.
- Opções de armazenamento híbrido, como AWS DataSync, AWS Transfer Family e AWS Storage Gateway.
- Padrões de acesso ao armazenamento.
- Camadas de armazenamento, incluindo cold tiering para object storage.
- Tipos de armazenamento e suas características: object, file e block.

**Habilidades**

- Projetar estratégias de armazenamento apropriadas, como uploads em lote para o Amazon S3 versus uploads individuais.
- Determinar a capacidade correta de armazenamento para um workload.
- Determinar o método de menor custo para transferir dados do workload ao armazenamento AWS.
- Determinar quando é necessário auto scaling de armazenamento.
- Gerenciar o ciclo de vida de objetos S3.
- Selecionar a solução apropriada de backup e/ou arquivamento.
- Selecionar o serviço apropriado para migrar dados aos serviços de armazenamento.
- Selecionar a camada de armazenamento apropriada.
- Selecionar o ciclo de vida correto dos dados.
- Selecionar o serviço de armazenamento mais econômico para um workload.

### Tarefa 4.2 — Projetar soluções de compute otimizadas em custo

Nome oficial: **Design cost-optimized compute solutions**.

**Conhecimentos**

- Recursos de serviços de gerenciamento de custos, incluindo cost allocation tags e faturamento de múltiplas contas.
- Ferramentas de gerenciamento de custos e seus casos de uso, como AWS Cost Explorer, AWS Budgets e AWS Cost and Usage Report.
- Infraestrutura global da AWS, incluindo Availability Zones e AWS Regions.
- Opções de compra, como Spot Instances, Reserved Instances e Savings Plans.
- Estratégias de computação distribuída, como edge processing.
- Opções de compute híbrido, como AWS Outposts.
- Tipos, famílias e tamanhos de instância, incluindo memory optimized, compute optimized e virtualização.
- Otimização da utilização de compute, incluindo containers, serverless computing e microsserviços.
- Estratégias de scaling, incluindo auto scaling e hibernation.

**Habilidades**

- Determinar uma estratégia apropriada de load balancing: Application Load Balancer (Layer 7), Network Load Balancer (Layer 4) ou Gateway Load Balancer.
- Determinar métodos e estratégias de scaling para workloads elásticos, incluindo horizontal versus vertical e EC2 hibernation.
- Determinar serviços de compute econômicos e seus casos de uso, como AWS Lambda, Amazon EC2 e AWS Fargate.
- Determinar a disponibilidade necessária para diferentes classes de workloads, como produção versus não produção.
- Selecionar a família de instância apropriada para um workload.
- Selecionar o tamanho de instância apropriado para um workload.

### Tarefa 4.3 — Projetar soluções de banco de dados otimizadas em custo

Nome oficial: **Design cost-optimized database solutions**.

**Conhecimentos**

- Recursos de serviços de gerenciamento de custos, incluindo cost allocation tags e faturamento de múltiplas contas.
- Ferramentas de gerenciamento de custos e seus casos de uso, como AWS Cost Explorer, AWS Budgets e AWS Cost and Usage Report.
- Estratégias de cache.
- Políticas de retenção de dados.
- Planejamento de capacidade de banco de dados, incluindo capacity units.
- Conexões e proxies de bancos de dados.
- Database engines e seus casos de uso, incluindo migrações heterogêneas e homogêneas.
- Replicação de bancos de dados, como read replicas.
- Tipos e serviços de bancos de dados, como relational versus non-relational, Amazon Aurora e Amazon DynamoDB.

**Habilidades**

- Projetar políticas apropriadas de backup e retenção, incluindo frequência de snapshots.
- Determinar o database engine apropriado, como MySQL versus PostgreSQL.
- Determinar serviços AWS de banco de dados econômicos segundo o caso de uso, como DynamoDB versus Amazon RDS e opções serverless.
- Determinar tipos de banco de dados econômicos, como formato time series versus columnar.
- Migrar schemas e dados entre locais e/ou database engines diferentes.

### Tarefa 4.4 — Projetar arquiteturas de rede otimizadas em custo

Nome oficial: **Design cost-optimized network architectures**.

**Conhecimentos**

- Recursos de serviços de gerenciamento de custos, incluindo cost allocation tags e faturamento de múltiplas contas.
- Ferramentas de gerenciamento de custos e seus casos de uso, como AWS Cost Explorer, AWS Budgets e AWS Cost and Usage Report.
- Conceitos de load balancing, como Application Load Balancer.
- NAT gateways, incluindo custos de NAT instances versus NAT gateways.
- Conectividade de rede, incluindo linhas privadas, linhas dedicadas e VPNs.
- Routing, topology e peering, incluindo AWS Transit Gateway e VPC peering.
- Serviços de rede e seus casos de uso, como DNS.

**Habilidades**

- Configurar uma estratégia apropriada de NAT gateway, como um gateway compartilhado versus um gateway por Availability Zone.
- Configurar conexões de rede apropriadas, comparando AWS Direct Connect, VPN e internet.
- Configurar rotas que minimizem custos de transferência: Region para Region, Availability Zone para Availability Zone, privado para público, AWS Global Accelerator e VPC endpoints.
- Determinar a necessidade estratégica de CDNs e edge caching.
- Revisar workloads existentes em busca de otimizações de rede.
- Selecionar uma estratégia apropriada de throttling.
- Selecionar a alocação de bandwidth apropriada para um dispositivo de rede, como uma VPN versus múltiplas VPNs e a velocidade do Direct Connect.

## Tecnologias e conceitos oficiais

A AWS informa que estes tópicos podem aparecer no exame; a lista não é exaustiva, pode mudar e sua ordem não indica peso ou importância:

- Compute.
- Cost management.
- Database.
- Disaster recovery.
- High performance.
- Management and governance.
- Microservices and component delivery.
- Migration and data transfer.
- Networking, connectivity, and content delivery.
- Resiliency.
- Security.
- Serverless and event-driven design principles.
- Storage.

Fonte: [Technologies and Concepts](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-technologies-concepts.html).

## Serviços AWS atualmente em escopo

Esta é a lista oficial consultada em 24/07/2026. Ela é **não exaustiva**, está sujeita a mudanças e agrupa os serviços por sua função principal.

### Analytics

- Amazon Athena
- AWS Data Exchange
- Amazon Data Firehose
- Amazon EMR
- AWS Glue
- Amazon Kinesis
- AWS Lake Formation
- Amazon Managed Streaming for Apache Kafka (Amazon MSK)
- Amazon OpenSearch Service
- Amazon Quick
- Amazon Redshift

### Application Integration

- Amazon AppFlow
- AWS AppSync
- Amazon EventBridge
- Amazon MQ
- Amazon SNS
- Amazon SQS
- AWS Step Functions

### AWS Cost Management

- AWS Budgets
- AWS Cost and Usage Report
- AWS Cost Explorer
- Savings Plans

### Compute

- AWS Batch
- Amazon EC2
- Amazon EC2 Auto Scaling
- AWS Elastic Beanstalk
- AWS Outposts
- AWS Serverless Application Repository
- VMware Cloud on AWS
- AWS Wavelength

### Containers

- Amazon ECR
- Amazon ECS
- Amazon ECS Anywhere
- Amazon EKS
- Amazon EKS Anywhere
- Amazon EKS Distro

### Database

- Amazon Aurora
- Amazon Aurora Serverless
- Amazon DocumentDB
- Amazon DynamoDB
- Amazon ElastiCache
- Amazon Keyspaces
- Amazon Neptune
- Amazon RDS
- Amazon Redshift

### Developer Tools

- AWS X-Ray

### Front-End Web and Mobile

- AWS Amplify
- Amazon API Gateway
- AWS Device Farm

### Machine Learning

- Amazon Comprehend
- Amazon Kendra
- Amazon Lex
- Amazon Polly
- Amazon Rekognition
- Amazon SageMaker AI
- Amazon Textract
- Amazon Transcribe
- Amazon Translate

### Management and Governance

- AWS Auto Scaling
- AWS CLI
- AWS CloudFormation
- AWS CloudTrail
- Amazon CloudWatch
- AWS Compute Optimizer
- AWS Config
- AWS Control Tower
- AWS Health Dashboard
- AWS License Manager
- Amazon Managed Grafana
- Amazon Managed Service for Prometheus
- AWS Management Console
- AWS Organizations
- AWS Service Catalog
- AWS Systems Manager
- AWS Trusted Advisor
- AWS Well-Architected Tool

### Media Services

- Amazon Elastic Transcoder
- Amazon Kinesis Video Streams

### Migration and Transfer

- AWS Application Migration Service
- AWS DataSync
- AWS Database Migration Service (AWS DMS)
- AWS Snow Family
- AWS Transfer Family

### Networking and Content Delivery

- AWS Client VPN
- Amazon CloudFront
- AWS Direct Connect
- Elastic Load Balancing (ELB)
- AWS Global Accelerator
- AWS PrivateLink
- Amazon Route 53
- AWS Site-to-Site VPN
- AWS Transit Gateway
- Amazon VPC

### Security, Identity, and Compliance

- AWS Artifact
- AWS Audit Manager
- AWS Certificate Manager (ACM)
- AWS CloudHSM
- Amazon Cognito
- Amazon Detective
- AWS Directory Service
- AWS Firewall Manager
- Amazon GuardDuty
- AWS IAM Identity Center
- Amazon Inspector
- AWS Key Management Service (AWS KMS)
- Amazon Macie
- AWS Network Firewall
- AWS Resource Access Manager (AWS RAM)
- AWS Secrets Manager
- AWS Security Hub
- AWS Shield
- AWS WAF
- AWS Identity and Access Management (IAM)

### Serverless

- AWS AppSync
- AWS Fargate
- AWS Lambda

### Storage

- AWS Backup
- Amazon Elastic Block Store (Amazon EBS)
- Amazon Elastic File System (Amazon EFS)
- Amazon FSx (todos os tipos)
- Amazon Simple Storage Service (Amazon S3)
- Amazon S3 Glacier
- AWS Storage Gateway

Fonte: [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-in-scope-services.html).

## Serviços AWS atualmente fora do escopo

Esta é a lista oficial consultada em 24/07/2026. Ela é **não exaustiva** e está sujeita a mudanças. Serviços completamente alheios ao papel-alvo podem nem aparecer nesta lista.

### Application Integration

- Amazon Managed Workflows for Apache Airflow (Amazon MWAA)

### AR and VR

- Amazon Sumerian

### Blockchain

- Amazon Managed Blockchain

### Compute

- Amazon Lightsail

### Database

- Amazon RDS on VMware

### Developer Tools

- AWS Cloud Development Kit (AWS CDK)
- AWS CloudShell
- AWS CodeArtifact
- AWS CodeBuild
- AWS CodeCommit
- AWS CodeDeploy
- Amazon Corretto
- AWS Fault Injection Simulator (AWS FIS)
- AWS Tools and SDKs

### Front-End Web and Mobile

- Amazon Location Service

### Game Tech

- Amazon GameLift

### Internet of Things

- Todos os serviços de IoT.

### Machine Learning

- Apache MXNet on AWS
- Amazon Augmented AI (Amazon A2I)
- AWS DeepComposer
- AWS Deep Learning AMIs (DLAMI)
- AWS Deep Learning Containers
- Amazon DevOps Guru
- Amazon Elastic Inference
- Amazon HealthLake
- AWS Inferentia
- Amazon Personalize
- PyTorch on AWS
- Amazon SageMaker Canvas
- Amazon SageMaker Ground Truth
- TensorFlow on AWS

### Management and Governance

- AWS Console Mobile Application
- AWS Distro for OpenTelemetry

### Media Services

- AWS Elemental Appliances and Software
- AWS Elemental MediaConnect
- AWS Elemental MediaConvert
- AWS Elemental MediaLive
- AWS Elemental MediaPackage
- AWS Elemental MediaTailor
- Amazon Interactive Video Service (Amazon IVS)

### Migration and Transfer

- Migration Evaluator

### Networking and Content Delivery

- AWS Cloud Map

### Quantum Technologies

- Amazon Braket

### Satellite

- AWS Ground Station

Fonte: [Out-of-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/saa-03-out-of-scope-services.html).

## Regras práticas para classificar as aulas

Cada item do curso deve receber **uma categoria principal**, um ou mais códigos de tarefa quando aplicável e uma justificativa curta. A categoria descreve a melhor ação de estudo; ela não substitui o mapeamento aos domínios.

### 1. Essencial

Classificar como **Essencial** quando a aula:

- ensina diretamente um conhecimento ou uma habilidade citada em uma das 14 tarefas;
- prepara o aluno para **projetar, determinar, selecionar, recomendar, revisar ou comparar** soluções segundo requisitos;
- explica um trade-off de arquitetura entre segurança, resiliência, desempenho, custo ou esforço operacional;
- cobre um serviço, recurso ou padrão indispensável para responder a cenários típicos de uma tarefa;
- contém uma prática sem a qual não seria possível compreender uma decisão explícita do blueprint.

**Ação de estudo:** assistir integralmente, produzir notas de decisão e comparação, realizar prática quando útil e criar questões/revisões D+2 e D+7.

**Teste rápido:** “Consigo apontar a frase exata de conhecimento ou habilidade oficial que esta aula ensina?” Se sim, há forte evidência de que é essencial.

### 2. Complementar

Classificar como **Complementar** quando a aula:

- dá contexto, vocabulário ou fundamento útil a uma tarefa, mas não cobre diretamente uma habilidade de decisão;
- apresenta um serviço em escopo de uso menos central ou sem ligação forte com o título/conteúdo conhecido da aula;
- aprofunda detalhes além do nível necessário ao Solutions Architect – Associate;
- é revisão geral, preparação para o exame ou comparação auxiliar;
- ajuda na formação profissional, embora sua contribuição direta para a SAA-C03 seja secundária.

**Ação de estudo:** assistir em velocidade maior ou ler o resumo; registrar somente os pontos que ajudam a diferenciar soluções. Não dedicar o mesmo volume de revisão de uma aula essencial.

**Regra importante:** aparecer na lista “em escopo” não torna automaticamente uma aula essencial. A AWS afirma que a lista é não exaustiva e não atribui peso individual aos serviços.

### 3. Operacional

Classificar como **Operacional** quando o objetivo principal da aula é:

- demonstrar cliques no console, comandos da AWS CLI, instalação, configuração ou troubleshooting passo a passo;
- executar um laboratório de um serviço em escopo sem acrescentar nova decisão de arquitetura;
- ensinar uma ferramenta ou procedimento de apoio ao aprendizado prático.

**Ação de estudo:** executar ou acompanhar seletivamente. Registrar o resultado, os custos e o procedimento de encerramento/limpeza dos recursos. Não memorizar sequências de cliques ou comandos que não correspondam a uma habilidade do blueprint.

Uma aula prática pode ser **Essencial** em vez de Operacional se o núcleo da prática demonstrar uma habilidade oficial — por exemplo, eliminar um single point of failure, escolher uma política IAM, validar failover ou comparar classes de armazenamento. A categoria deve refletir o objetivo principal, não apenas o formato “hands-on”.

### 4. Fora do escopo

Classificar como **Fora do escopo** quando:

- o objetivo principal é um serviço ou recurso explicitamente presente na lista oficial de fora do escopo;
- não há correspondência razoável com nenhum conhecimento, habilidade, tecnologia ou conceito das 14 tarefas;
- o conteúdo pertence a outro exame ou aprofunda uma função operacional sem valor claro para as decisões da SAA-C03.

**Ação de estudo:** pular, assistir apenas por interesse profissional ou consumir em velocidade alta. Não incluir nas revisões obrigatórias nem na meta de domínio da prova.

**Exemplos atuais:** uma aula cujo objetivo é ensinar AWS CloudShell ou Amazon Personalize deve, em princípio, ser marcada como Fora do escopo, pois ambos constam explicitamente na lista oficial de fora do escopo.

### Ordem de decisão

Aplicar esta sequência a cada aula:

1. Identificar o objetivo principal pelo título, seção, tipo de item e, quando disponível, descrição.
2. Procurar correspondência direta com os conhecimentos e habilidades das 14 tarefas.
3. Identificar os serviços e conceitos envolvidos.
4. Consultar as listas oficiais em escopo e fora do escopo.
5. Se houver correspondência direta com uma tarefa e foco em decisão de arquitetura, marcar **Essencial**.
6. Se houver contribuição indireta ou profundidade adicional, marcar **Complementar**.
7. Se o foco for execução prática/procedimental de conteúdo relevante, marcar **Operacional**.
8. Se o foco principal estiver explicitamente fora do escopo ou não tiver correspondência com o blueprint, marcar **Fora do escopo**.
9. Registrar uma justificativa de uma frase e os códigos das tarefas relacionadas.

### Regras para casos ambíguos

- **Serviço ausente das duas listas:** não classificar automaticamente como fora do escopo. Usar a correspondência com as 14 tarefas e os conceitos oficiais.
- **Serviço fora do escopo usado apenas como ferramenta:** se a aula ensina principalmente o serviço, usar Fora do escopo; se ele aparece incidentalmente em um laboratório que ensina uma decisão oficial, classificar pelo objetivo real da aula.
- **Aula com vários assuntos:** escolher a categoria do assunto predominante e mapear todas as tarefas relevantes.
- **Aula essencial com demonstração:** manter Essencial se a demonstração sustenta uma decisão de arquitetura; usar Operacional se for apenas execução.
- **Quiz ou simulado:** classificar de acordo com a cobertura das questões quando ela estiver disponível. Sem acesso às questões, registrar como item de avaliação ainda não classificável em nível de tarefa.
- **Introdução, conclusão e material administrativo:** normalmente Complementar; usar Fora do escopo apenas quando não houver valor de estudo.
- **Atualização conflitante:** a documentação oficial vigente prevalece sobre o curso. Registrar a divergência em vez de memorizar conteúdo antigo.

### Campos mínimos para a futura matriz de cobertura

| Campo | Uso |
|---|---|
| Item/aula | Número ou identificador do curso |
| Seção | Seção curricular |
| Título | Título original da Udemy |
| Tipo | Vídeo, artigo, quiz, simulado ou recurso |
| Duração | Tempo informado |
| Serviço(s) | Nomes oficiais envolvidos |
| Conceito(s) | Padrões e tecnologias relevantes |
| Tarefa(s) | Códigos 1.1 a 4.4 |
| Domínio principal | 1, 2, 3 ou 4 |
| Categoria | Essencial, Complementar, Operacional ou Fora do escopo |
| Justificativa | Evidência curta baseada no blueprint |
| Ação | Estudar integralmente, acelerar, praticar ou pular |

## Controle de integridade deste mapa

- Domínio 1: tarefas 1.1, 1.2 e 1.3 = **3**.
- Domínio 2: tarefas 2.1 e 2.2 = **2**.
- Domínio 3: tarefas 3.1, 3.2, 3.3, 3.4 e 3.5 = **5**.
- Domínio 4: tarefas 4.1, 4.2, 4.3 e 4.4 = **4**.
- Total: **3 + 2 + 5 + 4 = 14 tarefas**.
- Pesos: **30% + 26% + 24% + 20% = 100%** do conteúdo pontuado.

