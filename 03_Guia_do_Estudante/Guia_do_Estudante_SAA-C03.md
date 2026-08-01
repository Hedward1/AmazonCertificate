# Guia do Estudante - AWS SAA-C03

**Estado:** B01–B25 completos; consulte o [índice dos capítulos](Capitulos/README.md).
**Idioma:** português, com nomes oficiais, vocabulário de arquitetura e palavras decisivas em inglês.  
**Perfil:** iniciante absoluto em AWS, com conta disponível para laboratórios.  
**Exame-alvo:** AWS Certified Solutions Architect - Associate (SAA-C03).

## Como usar este guia

Este guia é autossuficiente: o curso da Udemy fornece a sequência de aulas,
mas a documentação oficial vigente da AWS determina comportamento, escopo e
recomendações. Assistir a uma aula não significa dominar o tópico.

Cada assunto seguirá a progressão:

> Compreender -> Comparar -> Aplicar -> Resolver -> Revisar

Arquivos de controle:

- [Perfil de estudo](../00_Projeto/Perfil_Estudo_SAA-C03.md)
- [Mapa oficial do exame](../01_Fontes/AWS_Oficial/Mapa_Oficial_SAA-C03.md)
- [Inventário do curso](../01_Fontes/Udemy/Inventario_Curso_Udemy_SAA-C03.csv)
- [Matriz de cobertura](../02_Planejamento/Matriz_Cobertura_SAA-C03.csv)
- [Cronograma diário](../02_Planejamento/Cronograma_Diario_SAA-C03.md)
- [Roteiro diário das aulas da
  Udemy](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md)
- [Apostila de questões](../04_Questoes_e_Revisoes/Apostila_de_Questoes_SAA-C03.md)
- [Gabarito comentado](../04_Questoes_e_Revisoes/Gabarito_Comentado_SAA-C03.md)
- [Caderno de erros](../04_Questoes_e_Revisoes/Caderno_de_Erros_SAA-C03.md)

## Sumário planejado

**Blocos disponíveis:** [B01–B25 completos](Capitulos/README.md), na mesma
ordem do cronograma. Comece pelo B01 e abra, no início de cada capítulo, as
aulas correspondentes da Udemy.

### Parte I - Fundamentos, identidade e computação

1. Infraestrutura global, Regions, Availability Zones e responsabilidade compartilhada  
   Curso: seções 1 a 3.
2. IAM, autenticação, autorização e segurança da conta  
   Curso: seções 4 e 25.
3. Amazon EC2, tipos de instância e modelos de compra  
   Curso: seções 5 e 6.
4. EBS, instance store, AMIs e Amazon EFS  
   Curso: seção 7.
5. Elastic Load Balancing, Auto Scaling e alta disponibilidade  
   Curso: seção 8.

### Parte II - Bancos, armazenamento e entrega global

6. Amazon RDS, Aurora, Aurora Serverless, ElastiCache e proxies  
   Curso: seção 9.
7. Route 53, políticas de roteamento e DNS híbrido  
   Curso: seção 10.
8. Arquiteturas clássicas e Elastic Beanstalk  
   Curso: seção 11.
9. Amazon S3: fundamentos, classes, desempenho e ciclo de vida  
   Curso: seções 12 e 13.
10. Segurança do S3, criptografia e proteção de objetos  
    Curso: seção 14.
11. CloudFront, Global Accelerator e edge  
    Curso: seção 15.
12. FSx, Storage Gateway, Snow Family, Transfer Family e DataSync  
    Curso: seção 16.

### Parte III - Desacoplamento, contêineres e serverless

13. SQS, SNS, EventBridge, Kinesis, Data Firehose e Amazon MQ  
    Curso: seção 17.
14. ECS, ECR, EKS, Fargate e decisões sobre contêineres  
    Curso: seção 18.
15. Lambda, DynamoDB, API Gateway, AppSync, Step Functions e Cognito  
    Curso: seção 19.
16. Arquiteturas serverless e microservices  
    Curso: seção 20.

### Parte IV - Dados, observabilidade, segurança e redes

17. Escolha de bancos de dados purpose-built  
    Curso: seção 21.
18. Analytics, ingestão, transformação e visualização, incluindo Amazon Quick
    Sight (antigo QuickSight) dentro do Amazon Quick
    Curso: seção 22.
19. Serviços gerenciados de Machine Learning relevantes ao exame  
    Curso: seção 23.
20. CloudWatch, X-Ray, EventBridge, CloudTrail e AWS Config  
    Curso: seção 24.
21. KMS, Secrets Manager, Parameter Store, ACM e CloudHSM  
    Curso: seção 26.
22. WAF, Shield, Firewall Manager, GuardDuty, Inspector, Macie, Security Hub,
    Detective, Artifact e Audit Manager  
    Curso: seção 26.
23. Amazon VPC, subnets, routing, PrivateLink, Client VPN, Direct Connect e
    Resource Access Manager  
    Curso: seção 27.

### Parte V - Recuperação, migração, custos e arquiteturas integradas

24. Disaster Recovery, RTO, RPO, backup e migrações  
    Curso: seção 28.
25. Event processing, cache, HPC e arquiteturas integradas  
    Curso: seção 29.
26. CloudFormation, Systems Manager e serviços complementares  
    Curso: seção 30.
27. Cost optimization em compute, storage, database e network, incluindo
    Savings Plans, Compute Optimizer e Cost and Usage Report  
    Curso: seções 5, 7, 9, 12, 13, 21, 27 e 30.
28. AWS Well-Architected Framework e revisão arquitetural  
    Curso: seção 31.

### Parte VI - Revisão e prova em inglês

29. Vocabulário decisivo e leitura de cenários em inglês.
30. Estratégia de prova, controle de tempo e eliminação de alternativas.
31. Revisão pelos quatro domínios e pelo Caderno de Erros.

## Estrutura obrigatória de cada capítulo

Cada capítulo deverá conter:

1. identificação na matriz;
2. domínio e tarefas oficiais;
3. aulas correspondentes;
4. objetivos de aprendizagem;
5. pré-requisitos;
6. vocabulário essencial em inglês;
7. base e fundamentos;
8. aprofundamento;
9. aplicação arquitetural;
10. comparações entre serviços;
11. pelo menos dois cenários resolvidos quando aplicável;
12. laboratório, diagrama ou exercício;
13. mapa ou tabela de decisão;
14. armadilhas de prova;
15. custos e esforço operacional;
16. resumo de revisão;
17. perguntas de recuperação ativa;
18. referências oficiais;
19. ligação com questões, D+2 e D+7.

## Modelo de tabela de decisão

| Requisito | Opções viáveis | Melhor escolha | Trade-off decisivo |
|---|---|---|---|
| A preencher | A preencher | A preencher | A preencher |

## Modelo de cenário resolvido

1. **Cenário**
2. **Requisito obrigatório**
3. **Restrições**
4. **Palavras decisivas em inglês**
5. **Alternativas plausíveis**
6. **Decisão**
7. **Justificativa**
8. **Por que as demais alternativas são inferiores**
9. **Variação que mudaria a resposta**

## Modelo de laboratório

- **Objetivo:**
- **Tarefa oficial:**
- **Serviços:**
- **Pré-requisitos:**
- **Tempo estimado:**
- **Estimativa de custo:**
- **Compatível com Free Tier:**
- **Passos:**
- **Validação:**
- **Cleanup obrigatório:**
- **Risco de cobrança residual:**
- **Conexão com o exame:**

## Controle de produção

| Capítulo | Base | Comparação | Cenários | Laboratório/diagrama | Questões | D+2 | D+7 |
|---|---|---|---|---|---|---|---|
| B01 — capítulos 1 e 2 (fundamentos) | Pronto | Pronto | 3 prontos | Pronto | 10 prontas | Pronto | Pronto |
| B02 — capítulos 2 e 3 (início) | Pronto | Pronto | 3 prontos | Pronto | 10 prontas | Pronto | Pronto |
| B03 — capítulo 3 (continuação) | Pronto | Pronto | 4 prontos | Pronto | 10 prontas | Pronto | Pronto |
| B04 — capítulos 3 e 4 (transição) | Pronto | Pronto | 6 prontos | Pronto | 10 prontas | Pronto | Pronto |
| B05–B25 | Pronto | Pronto | 3 ou mais por bloco | Pronto | 210 prontas | Pronto | Pronto |
