# B01 — Infraestrutura global, responsabilidade compartilhada e IAM

**Data planejada:** 25/07/2026  
**Nível:** iniciante absoluto  
**Aulas relacionadas:** 1–18; o conteúdo técnico começa principalmente nas
aulas 8–18  
**Domínios oficiais:** 1 — Design Secure Architectures; 2 — Design Resilient
Architectures  
**Tarefas principais:** 1.1 — Design secure access to AWS resources; 2.2 —
Design highly available and/or fault-tolerant architectures  
**Tarefas secundárias:** 2.1 — Design scalable and loosely coupled
architectures; 3.4 — Determine high-performing and/or scalable network
architectures  
**Tempo sugerido:** 50 minutos de teoria, além das aulas, laboratório e questões
do cronograma

## 1. O que você deve conseguir fazer ao terminar

Sem consultar o material, você deverá conseguir:

1. diferenciar Region, Availability Zone e edge location;
2. explicar quando uma solução precisa de múltiplas AZs ou múltiplas Regions;
3. separar as responsabilidades de segurança da AWS e do cliente;
4. distinguir autenticação de autorização;
5. comparar root user, IAM user, user group, IAM role e policy;
6. prever o resultado básico da avaliação de uma policy;
7. escolher credenciais temporárias em vez de access keys de longo prazo;
8. explicar por que uma aplicação em EC2 deve usar uma role;
9. reconhecer as palavras decisivas desses assuntos em inglês.

## 2. Pré-requisitos e limites deste bloco

Você precisa apenas de uma conta AWS e acesso ao e-mail e ao telefone associados
a ela. Não é necessário conhecer redes ou programação.

O laboratório deste bloco não exige criar EC2, banco ou armazenamento. IAM não
tem cobrança adicional, mas AWS Budgets é um sistema de alerta — não um bloqueio
instantâneo de gastos. O teto mensal ainda deve ser escolhido antes de qualquer
laboratório que possa gerar cobrança.

## 3. Mapa mental da infraestrutura global

```text
AWS Cloud
├── Region A — área geográfica isolada
│   ├── Availability Zone A1 — uma ou mais instalações isoladas
│   ├── Availability Zone A2 — uma ou mais instalações isoladas
│   └── Availability Zone A3 — uma ou mais instalações isoladas
├── Region B
│   ├── Availability Zone B1
│   └── Availability Zone B2...
└── Global edge network — pontos próximos dos usuários
    ├── edge locations / points of presence
    └── regional edge caches
```

### 3.1 Region

Uma **AWS Region** é uma área geográfica separada das demais Regions. Exemplos de
códigos são `sa-east-1` e `us-east-1`.

Grande parte dos recursos é **regional**: você escolhe uma Region ao criá-los e
eles não são replicados automaticamente para outra. A escolha considera:

- **compliance and data residency:** onde os dados podem permanecer;
- **latency:** proximidade dos usuários;
- **service and feature availability:** nem tudo está em todas as Regions;
- **cost:** o preço pode variar entre Regions;
- **resilience:** necessidade de sobreviver à perda de uma Region.

Regra de prova: “mais perto” não vence uma exigência obrigatória de compliance.
Primeiro cumpra as restrições; depois otimize latência e custo.

### 3.2 Availability Zone (AZ)

Uma **Availability Zone** é uma localização isolada dentro de uma Region. Ela
consiste em um ou mais data centers discretos, com energia, rede e conectividade
redundantes. As AZs de uma Region são interligadas por rede de alta largura de
banda e baixa latência.

Um recurso **zonal** pertence a uma AZ específica. Se todos os componentes de uma
aplicação estiverem em uma única AZ, essa AZ é um **single point of failure**.

**Multi-AZ** normalmente atende ao requisito de alta disponibilidade diante da
falha de uma AZ. Isso não é o mesmo que **Multi-Region**, usado quando o requisito
inclui desastre regional, alcance global, soberania de dados ou recuperação mais
ampla.

> Observação atual: as letras das AZs podem não representar a mesma localização
> física entre contas antigas. Quando for necessário coordenar a mesma AZ física
> entre contas, use o **AZ ID**, não apenas um nome como `us-east-1a`.

### 3.3 Edge location / point of presence (PoP)

Um ponto de presença coloca serviços de borda próximos dos usuários. A rede de
PoPs é usada por serviços como Amazon CloudFront, Amazon Route 53 e AWS Global
Accelerator.

Uma edge location:

- não é outra forma de chamar uma AZ;
- não substitui automaticamente a Region de origem;
- reduz latência ou melhora a entrega e o roteamento conforme o serviço;
- pode armazenar conteúdo em cache quando usada pelo CloudFront.

### 3.4 Escopos que você encontrará

| Escopo | Significado | Exemplo mental |
|---|---|---|
| Global | A configuração não é criada separadamente em cada Region | identidades do IAM |
| Regional | O recurso pertence a uma Region | uma VPC |
| Zonal | O recurso pertence a uma AZ | uma instância EC2 |
| Edge | O serviço atende próximo do usuário | cache do CloudFront |

Os exemplos ajudam a formar o modelo mental, mas sempre confira a documentação
do serviço: diferentes componentes do mesmo serviço podem ter escopos distintos.

## 4. Alta disponibilidade: a primeira decisão arquitetural

Considere um site com dois servidores:

```text
Errado para alta disponibilidade       Melhor

Region                                 Region
└── AZ-A                               ├── AZ-A: servidor 1
    ├── servidor 1                     └── AZ-B: servidor 2
    └── servidor 2
```

No primeiro desenho, a perda da AZ derruba os dois servidores. No segundo, a
falha de uma AZ ainda deixa capacidade na outra — desde que o restante da
arquitetura também seja distribuído e o tráfego possa chegar ao componente
saudável.

### Cenário resolvido 1 — Multi-AZ ou Multi-Region?

1. **Cenário:** aplicação nacional precisa continuar disponível após falha de um
   data center, com baixa latência entre componentes.
2. **Requisito obrigatório:** tolerar falha de infraestrutura isolada.
3. **Restrição:** não há exigência de sobreviver à perda de toda a Region.
4. **Palavras decisivas:** *high availability*, *low latency*, *AZ failure*.
5. **Decisão:** distribuir os componentes entre pelo menos duas AZs da mesma
   Region.
6. **Por quê:** AZs fornecem isolamento de falha com conexão regional de baixa
   latência.
7. **Por que Multi-Region é inferior aqui:** adiciona complexidade, replicação e
   custo sem existir requisito regional.
8. **Variação:** se o requisito disser *survive a regional outage*, passa a ser
   necessário avaliar uma arquitetura Multi-Region.

## 5. Modelo de responsabilidade compartilhada

A frase mais importante é:

> AWS é responsável pela **security of the cloud**; o cliente é responsável pela
> **security in the cloud**.

### 5.1 Responsabilidade da AWS

A AWS protege e opera a infraestrutura que fornece os serviços:

- instalações físicas;
- hardware;
- rede física;
- camada de virtualização;
- sistema operacional hospedeiro;
- componentes subjacentes dos serviços gerenciados.

### 5.2 Responsabilidade do cliente

O cliente continua responsável por decisões e configurações como:

- dados e classificação dos dados;
- identidades, credenciais, MFA e permissões;
- configuração de rede e security groups;
- configuração de criptografia;
- aplicação e código;
- sistema operacional convidado e patches em EC2;
- requisitos legais aplicáveis ao workload.

### 5.3 A divisão muda conforme o serviço

| Situação | AWS | Cliente |
|---|---|---|
| EC2 | hardware, host e virtualização | guest OS, patches, aplicação, dados, firewall |
| Banco gerenciado | infraestrutura e mais tarefas operacionais do engine | dados, acessos, configuração permitida, desenho e uso |
| Serviço serverless/gerenciado | maior parte da pilha operacional | código/configuração, dados, identidade e uso seguro |

“Managed” reduz trabalho operacional; não transfere à AWS a responsabilidade
pelos dados, permissões e configuração do cliente.

### Cenário resolvido 2 — Quem aplica o patch?

1. **Cenário:** uma empresa executa uma aplicação em uma instância EC2.
2. **Pergunta:** quem corrige vulnerabilidades do sistema operacional convidado?
3. **Decisão:** o cliente.
4. **Justificativa:** a AWS protege o host e a infraestrutura; o cliente
   administra o guest OS da instância.
5. **Variação:** em um serviço mais gerenciado, a AWS pode operar mais camadas,
   mas o cliente ainda controla dados, acessos e suas configurações.

## 6. IAM: identidade antes da permissão

**AWS Identity and Access Management (IAM)** controla quem está autenticado e o
que essa identidade pode fazer.

- **Authentication:** provar quem você é.
- **Authorization:** determinar o que você pode fazer.
- **Principal:** pessoa, aplicação, serviço ou sessão que faz uma solicitação.
- **Policy:** documento que define permissões.

```text
principal autenticado
        │
        ▼
solicitação: Action + Resource + contexto
        │
        ▼
policies aplicáveis
        │
        ▼
Allow ou Deny
```

### 6.1 Root user

O **AWS account root user** nasce com a conta e possui acesso completo. Um IAM
user com permissão de administrador não é o root user.

Para o root:

- habilite MFA;
- use senha única e forte;
- mantenha e-mail, telefone e contatos de recuperação protegidos e atualizados;
- não crie access keys;
- não o use em atividades diárias;
- use-o apenas nas poucas tarefas que realmente exigem root.

Uma policy do IAM não é a estratégia correta para “reduzir” o uso diário do
root. A estratégia é guardar suas credenciais e trabalhar com outra identidade.

### 6.2 IAM user

Um **IAM user** é uma identidade duradoura dentro de uma conta. Pode ter senha de
console e/ou access keys, conforme o caso de uso. Um novo IAM user não possui
permissões por padrão.

O exame ainda cobra users, mas a recomendação atual para pessoas é preferir
federação e credenciais temporárias, normalmente com IAM Identity Center.
IAM users ficam para casos específicos que não suportam federação.

### 6.3 IAM user group

Um **user group** reúne IAM users para facilitar a atribuição de permissões.

- a policy anexada ao grupo é herdada pelos usuários do grupo;
- um usuário pode pertencer a vários grupos;
- grupos contêm usuários, não outros grupos;
- grupo não tem credenciais e não é um principal autenticável;
- uma role não “entra” em um grupo.

Use grupos para permissões comuns, como `Developers` ou `Auditors`, em vez de
duplicar a mesma policy usuário por usuário.

### 6.4 IAM role

Uma **IAM role** é uma identidade com permissões que pode ser assumida. Ela não
possui senha ou access keys permanentes. Ao assumir a role, o principal recebe
credenciais temporárias para uma sessão.

Uma role tem duas perguntas diferentes:

1. **Trust policy:** quem pode assumir esta role?
2. **Permissions policies:** o que a sessão da role pode fazer?

Roles são adequadas para:

- um serviço AWS acessar outro serviço;
- uma aplicação em EC2 acessar S3;
- acesso temporário de pessoas federadas;
- acesso entre contas;
- elevação temporária e controlada de privilégio.

### 6.5 Policy

Uma policy é um documento JSON de permissões. Em uma
**identity-based policy**, os elementos centrais são:

- `Effect`: `Allow` ou `Deny`;
- `Action`: operação da API;
- `Resource`: recurso ao qual a ação se aplica;
- `Condition`: restrição opcional baseada no contexto.

Exemplo didático de leitura de um bucket específico:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListOnlyOneBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::example-study-bucket"
    },
    {
      "Sid": "ReadObjectsOnly",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::example-study-bucket/*"
    }
  ]
}
```

Leia em linguagem humana: “permitir listar este bucket e ler seus objetos”. Não
permite gravar, excluir ou acessar outro bucket.

O elemento `Principal` normalmente aparece em **resource-based policies**, como
uma bucket policy, e identifica quem recebe a permissão. Ele não é usado em uma
identity-based policy porque a identidade à qual a policy foi anexada já é o
principal implícito.

### 6.6 Managed policy versus inline policy

- **AWS managed policy:** criada e mantida pela AWS; facilita o início, mas pode
  ser mais ampla do que seu caso exige.
- **Customer managed policy:** criada pelo cliente e reutilizável por várias
  identidades.
- **Inline policy:** incorporada diretamente em uma única identidade; seu ciclo
  de vida fica ligado a ela.

Para muitas identidades com o mesmo acesso, uma customer managed policy é mais
fácil de versionar e reutilizar do que várias inline policies.

## 7. Como a autorização básica é avaliada

Use este modelo simplificado:

1. tudo começa com **implicit deny**;
2. um `Allow` aplicável pode autorizar a solicitação;
3. qualquer `Deny` explícito aplicável vence um `Allow`;
4. sem `Allow` aplicável, o resultado continua negado.

```text
Existe Deny explícito aplicável? ── sim ──> DENY
             │
             não
             ▼
Existe Allow aplicável? ───────── sim ──> ALLOW
             │
             não
             ▼
        IMPLICIT DENY
```

Permissions boundaries, session policies e policies do AWS Organizations podem
reduzir as permissões efetivas. Neste bloco, memorize a regra reutilizável:
**explicit deny overrides allow**.

## 8. Least privilege

**Least privilege** significa conceder somente as ações necessárias, nos
recursos necessários e sob as condições necessárias.

Compare:

| Policy | Resultado | Avaliação |
|---|---|---|
| `Action: "*"` e `Resource: "*"` | tudo | ampla demais para uma tarefa limitada |
| somente `s3:GetObject` no bucket necessário | leitura específica | mais próxima de least privilege |
| acesso temporário por role | expira com a sessão | menor exposição que chave permanente |

Least privilege não significa “dar pouca permissão aleatoriamente”. Significa
entender a tarefa e conceder o mínimo que a completa.

## 9. MFA e credenciais

### 9.1 MFA

**Multi-factor authentication** exige mais de um fator. Uma senha é algo que você
sabe; um dispositivo, passkey ou security key representa outro fator.

MFA fortalece a autenticação. Ele não concede autorização adicional por si só.
Uma identidade com MFA ainda precisa de policies que permitam a ação.

### 9.2 Tipos de credencial

| Credencial | Uso típico | Duração | Preferência |
|---|---|---|---|
| senha de console | login interativo | longa, até alteração | proteger com MFA |
| access key de IAM user | CLI/API em exceções | longa, até revogação | evitar quando houver alternativa |
| credenciais de role/STS | CLI, API, workload ou federação | temporária | preferida |
| access key do root | CLI/API com privilégio total | longa | nunca criar |

Uma access key é formada por um **access key ID** e um **secret access key**.
Credenciais temporárias acrescentam um **session token** e expiram.

Nunca:

- coloque chaves no código-fonte;
- envie chaves por chat ou e-mail;
- grave chaves em repositórios;
- reutilize uma chave do root;
- entregue a mesma identidade humana a várias pessoas.

### 9.3 Console, CLI e SDK não mudam a autorização

Console, AWS CLI e SDK são formas diferentes de chamar as APIs da AWS. A policy
é avaliada para a ação, não para a aparência da ferramenta.

A documentação atual recomenda credenciais temporárias para acesso humano e de
workloads. Para CLI local, métodos atuais incluem autenticação de curta duração
com sessão de console e IAM Identity Center. Access keys de IAM user devem ser
tratadas como exceção, não como primeira escolha.

> O AWS SDK aparece na aula 18 para explicar acesso programático, mas o guia
> oficial do exame lista SDKs como fora de escopo. Aprenda a diferença entre
> console, CLI e API; não gaste tempo memorizando código de SDK.

### Cenário resolvido 3 — EC2 precisa ler S3

1. **Cenário:** uma aplicação em EC2 precisa ler objetos de um único bucket.
2. **Requisito:** acesso programático seguro.
3. **Alternativas plausíveis:** gravar access key no código; criar access key do
   root; anexar uma IAM role à instância.
4. **Decisão:** anexar à instância uma role com `s3:GetObject` apenas no bucket
   necessário.
5. **Por quê:** o serviço entrega credenciais temporárias e o código não guarda
   segredo permanente.
6. **Variação:** se o workload estiver fora da AWS e não puder usar federação,
   avalie a alternativa de credenciais temporárias adequada; chave de longo
   prazo permanece último recurso e deve ter privilégio mínimo.

## 10. Tabela de decisão

| Requisito | Escolha | Razão decisiva |
|---|---|---|
| atividade que exige o proprietário da conta | root user, somente durante a tarefa | privilégio exclusivo |
| trabalho administrativo diário | identidade administrativa não root | reduz exposição do root |
| pessoas em uma ou várias contas | federação/IAM Identity Center e roles | acesso central e temporário |
| aplicação em serviço AWS | IAM role | credenciais temporárias automáticas |
| mesmas permissões para vários IAM users legados | user group + policy | administração em conjunto |
| negar uma ação mesmo se outra policy permitir | explicit `Deny` | Deny explícito prevalece |
| tolerar perda de uma AZ | Multi-AZ | isolamento dentro da Region |
| tolerar perda de uma Region | Multi-Region | isolamento regional |
| conteúdo global com menor latência | serviço de edge, como CloudFront | PoPs próximos dos usuários |

## 11. Armadilhas de prova

1. **Region ≠ AZ.** Region é a área geográfica; AZ é a localização isolada dentro
   dela.
2. **Uma AZ não significa obrigatoriamente um único data center.**
3. **Multi-AZ ≠ Multi-Region.** Leia qual domínio de falha precisa ser tolerado.
4. **Edge location ≠ AZ.** Edge atende perto do usuário; a origem pode continuar
   em uma Region.
5. **Administrator IAM user ≠ root user.**
6. **MFA autentica; policy autoriza.**
7. **Group não é principal e não contém groups ou roles.**
8. **Role não possui access keys permanentes.**
9. **Uma policy sem `Allow` aplicável não concede acesso.**
10. **Explicit Deny vence Allow.**
11. **AWS managed policy não garante least privilege para seu caso.**
12. **“Managed service” não torna a AWS dona da segurança dos dados e acessos.**
13. **CLI não exige automaticamente access key permanente.** Prefira credenciais
    temporárias.
14. **Nunca escolha root access key**, mesmo que pareça a forma mais rápida de
    dar acesso total.

## 12. Custos e esforço operacional

- IAM não possui cobrança adicional.
- Um dispositivo MFA físico pode ter custo; métodos compatíveis variam.
- Recursos distribuídos entre AZs ou Regions podem gerar custos de recursos e
  transferência de dados conforme o serviço.
- Multi-Region normalmente custa e exige mais operação do que Multi-AZ.
- AWS Budgets ajuda a monitorar, mas os dados e alertas têm atraso; ele não
  substitui cleanup nem acompanhamento do faturamento.

## 13. Checklist de domínio

Marque apenas depois de explicar sem consultar:

- [ ] Posso desenhar Region, AZ e edge location.
- [ ] Sei escolher Multi-AZ versus Multi-Region pelo requisito.
- [ ] Sei dar três exemplos de responsabilidade do cliente.
- [ ] Sei diferenciar root, user, group, role e policy.
- [ ] Sei explicar trust policy versus permissions policy.
- [ ] Sei prever implicit deny, Allow e explicit Deny.
- [ ] Sei justificar role em vez de access key dentro de uma aplicação.
- [ ] Sei explicar por que MFA não concede permissões.

## 14. Recuperação ativa

Responda em voz alta antes de consultar:

1. O que falha junto quando todos os recursos estão em uma AZ?
2. Quais quatro fatores orientam a escolha de uma Region?
3. Quem corrige o guest OS de uma instância EC2?
4. Um IAM user administrador é o root? Por quê?
5. Qual é a diferença entre autenticação e autorização?
6. Um grupo pode assumir uma role?
7. Qual documento diz quem pode assumir uma role?
8. O que acontece se uma policy permite uma ação e outra a nega explicitamente?
9. Por que credenciais temporárias reduzem risco?
10. Qual credencial nunca deve ser criada?

## 15. Ligações deste bloco

- [Laboratório B01](../../05_Laboratorios/LAB_B01_Seguranca_da_Conta_IAM.md)
- [Questões B01](../../04_Questoes_e_Revisoes/Blocos/B01_Questoes.md)
- [Gabarito B01](../../04_Questoes_e_Revisoes/Blocos/B01_Gabarito.md)
- [Revisões B01](../../06_Progresso/B01_Checklist_e_Revisoes.md)

## 16. Referências oficiais

- [AWS Regions and Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html)
- [AWS Regions — critérios e lista](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html)
- [AWS Availability Zones e AZ IDs](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-availability-zones.html)
- [AWS points of presence](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/points-of-presence.html)
- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [IAM identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)
- [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Root user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)
- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Policies and permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [Secure access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/securing_access-keys.html)
- [AWS CLI authentication options](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)

**Última verificação das referências:** 24/07/2026.
