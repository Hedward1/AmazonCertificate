# LAB B03 — Primeira instância EC2, website e cleanup completo

**Nível:** iniciante absoluto  
**Sistema local:** Windows com navegador e PowerShell  
**Tempo líquido:** 33 minutos  
**Espera assíncrona da AWS:** não conta como tempo líquido; não abandone o
laboratório antes de confirmar o cleanup  
**Aulas relacionadas:** 36–46, com foco em security groups, EC2 Instance
Connect, instance roles e modelos de compra  
**Capítulo relacionado:** [B03 — conexão ao EC2, roles e modelos de
compra](../03_Guia_do_Estudante/Capitulos/B03_Conexao_EC2_Roles_e_Modelos_de_Compra.md)  
**Tarefas oficiais:** 1.2 — Design secure workloads and applications; 3.2 —
Design high-performing and elastic compute solutions; 4.2 — Design
cost-optimized compute solutions  
**Instâncias permitidas:** exatamente 1  
**Identidade permitida:** não root, configurada no LAB B01  
**Profile da CLI:** `saa-lab-b02`, criado no LAB B02  
**Teto operacional deste laboratório:** USD 0,25; abortar antes do lançamento
se a estimativa total exceder esse valor

## 1. Resultado esperado

Ao terminar, você deverá ter:

- lançado exatamente uma instância Amazon EC2;
- usado Amazon Linux 2023;
- escolhido somente um tipo exibido como **Free tier eligible**;
- executado a instância como On-Demand e, se for T3/T4g, em CPU credit mode
  `standard`;
- instalado Apache automaticamente com user data;
- acessado o website pelo navegador;
- usado EC2 Instance Connect sem liberar SSH para a internet inteira;
- associado uma role para EC2 sem permissions policies;
- exigido IMDSv2;
- inspecionado metadados sem exibir credenciais;
- terminado a instância;
- confirmado a remoção do volume, endereço público e demais resíduos;
- excluído a role e o security group criados no laboratório.

## 2. Arquitetura do laboratório

```text
seu navegador
    │ HTTP 80
    ▼
public IPv4 temporário
    │
[saa-lab-b03-web-sg]
    │
    ▼
EC2 Amazon Linux 2023
├── httpd instalado por user data
├── EBS gp3 de 8 GiB
├── IMDSv2 required
└── instance profile
       └── SAA-Lab-B03-EC2-Empty
           ├── trust: ec2.amazonaws.com
           └── permissions: nenhuma

EC2 Instance Connect proxy
    │ SSH 22 — somente managed prefix list da Region
    ▼
EC2
```

O public IPv4 será atribuído automaticamente à instância. Ele não será um
Elastic IP e será liberado quando a instância for terminada.

## 3. Custos e elegibilidade

A expressão **Free tier eligible** não garante, sozinha, saldo gratuito na sua
conta. Ela informa que o tipo participa da oferta, mas ainda é necessário
confirmar:

- data de criação da conta;
- plano Free ou Paid;
- saldo e validade dos créditos;
- consumo anterior;
- Region;
- oferta vigente.

Para contas criadas antes de 15/07/2025, a oferta legada normalmente usa
`t2.micro` ou `t3.micro`, dentro do período e dos limites aplicáveis.

Para contas criadas em ou depois de 15/07/2025, a documentação atual lista tipos
como `t3.micro`, `t3.small`, `t4g.micro`, `t4g.small`, `c7i-flex.large` e
`m7i-flex.large`, com uso baseado no novo programa de créditos. A interface da
conta continua sendo a fonte decisiva.

Contas no plano Free usam créditos e podem bloquear atividades não disponíveis.
Contas Paid pagam o que ultrapassar créditos e ofertas gratuitas.

### Teto operacional

O limite máximo autorizado para todo o LAB B03 é **USD 0,25**, somando compute,
EBS, public IPv4 e qualquer outro item mostrado na estimativa.

Antes de escolher **Launch instance**:

1. confira a estimativa apresentada pelo console;
2. considere separadamente a cobrança possível do public IPv4;
3. confirme que não há recurso adicional no resumo;
4. aborte antes do lançamento se o total estimado puder exceder USD 0,25.

O teto é um critério de decisão, não uma garantia automática de bloqueio. AWS
Budgets e dados de cobrança podem ter atraso.

### Public IPv4

A tabela vigente cobra **USD 0,005 por endereço público IPv4 por hora**, com
cálculo por segundo e mínimo de 60 segundos. A AWS também documenta uma franquia
de 750 horas de public IPv4 para clientes EC2 Free Tier elegíveis.

Neste laboratório haverá no máximo um public IPv4 durante poucos minutos. Se a
franquia ou os créditos não se aplicarem, o IPv4 consumirá uma pequena fração de
centavo, além do compute e EBS conforme a Region.

O custo esperado é:

- coberto pela oferta/créditos, quando a conta for elegível; ou
- muito baixo, mas não necessariamente zero, se houver cobrança On-Demand.

### Pare antes do lançamento se:

- nenhum tipo compatível aparecer como **Free tier eligible**;
- a conta não tiver saldo/crédito e você não aceitar cobrança On-Demand;
- o custo estimado ultrapassar o teto operacional de USD 0,25;
- a Region estiver incorreta;
- não existir default VPC/default subnet;
- já existir uma instância ou recurso de uma tentativa B03 anterior;
- o resumo indicar mais de uma instância;
- a identidade não puder criar/passar a role prevista;
- a interface tentar criar NAT Gateway, load balancer, Elastic IP ou outro
  recurso não previsto.

## 4. Recursos permitidos

O laboratório pode criar somente:

| Recurso | Quantidade | Nome/configuração |
|---|---:|---|
| IAM role + instance profile | 1 | `SAA-Lab-B03-EC2-Empty` |
| Security group | 1 | `saa-lab-b03-web-sg` |
| EC2 instance | 1 | `SAA-Lab-B03-Web` |
| EBS root volume | 1 | gp3, 8 GiB, delete on termination |
| ENI primária | 1 | criada com a instância |
| Public IPv4 automático | 1 | não é Elastic IP |

Não crie:

- Elastic IP;
- key pair;
- snapshot;
- AMI;
- volume adicional;
- VPC, subnet, NAT Gateway ou load balancer;
- CloudWatch detailed monitoring;
- Spot request;
- Capacity Reservation;
- Dedicated Instance ou Dedicated Host.

## 5. Preflight

Preencha:

```text
DATA DE CRIAÇÃO DA CONTA: antes / em ou depois de 15/07/2025 / não sei
PLANO: Free / Paid / não sei
CRÉDITOS DISPONÍVEIS: USD ______ / não sei
REGION: __________________
BUDGET DO LAB B01 ATIVO: sim / não
TETO OPERACIONAL B03: USD 0,25
ESTIMATIVA TOTAL ANTES DO LAUNCH: USD ______
TIPO MARCADO FREE TIER ELIGIBLE: __________________
EIP ALLOCATIONS ANTES: ______
SNAPSHOTS OWNED BY ME ANTES: ______
RECURSOS B03 ANTERIORES: zero / investigar
```

No Billing and Cost Management, confira o Cost and Usage widget, créditos e
budget.

No EC2 Global View, procure por `SAA-Lab-B03`. Se encontrar uma tentativa
anterior, não lance outra instância. Conclua o cleanup anterior primeiro.

Como o LAB B02 terminou com logout, autentique novamente por apenas uma rota:

```powershell
# Se usa IAM Identity Center:
aws sso login --profile saa-lab-b02

# Se usa aws login:
aws login --profile saa-lab-b02
```

Confira localmente a identidade, sem registrar a saída:

```powershell
aws sts get-caller-identity --profile saa-lab-b02 --no-cli-pager
```

O ARN não pode ser root.

## 6. Roteiro de 33 minutos

### Etapa 1 — Preflight final — 4 minutos

1. Selecione a Region registrada no B01.
2. Confirme budget, plano e créditos.
3. Confirme que não existe recurso B03 anterior.
4. Anote as quantidades atuais de Elastic IPs e snapshots próprios.
5. Registre a estimativa e confirme que não excede USD 0,25.
6. Abra o console IAM e o console EC2 em abas separadas.

### Etapa 2 — Criar a role vazia — 3 minutos

No IAM:

1. Abra **Roles → Create role**.
2. Em **Trusted entity type**, escolha **AWS service**.
3. Em **Use case**, escolha **EC2**.
4. Continue sem selecionar permissions policy.
5. Use o nome `SAA-Lab-B03-EC2-Empty`.
6. Crie a role.
7. Confirme:
   - trusted service: `ec2.amazonaws.com`;
   - permissions policies: zero;
   - inline policies: zero.

Essa role é intencionalmente vazia porque o website não chama APIs AWS. Ela
permite estudar instance profiles e metadados sem conceder acesso a serviços.

Se a role já existir, use-a somente se a trust policy estiver correta e ambas as
listas de permissões estiverem vazias. Não crie uma duplicata.

### Etapa 3 — Configurar e lançar uma instância — 8 minutos

No EC2, escolha **Launch instance**.

#### Name and tags

- Name: `SAA-Lab-B03-Web`
- Tag adicional: `Project = SAA-Study`
- Tag adicional: `Lab = B03`

Não coloque nome, e-mail ou outros dados pessoais em tags.

#### Application and OS Images

Escolha:

- **Amazon Linux**;
- **Amazon Linux 2023 AMI** padrão;
- arquitetura `x86_64`;
- AMI marcada **Free tier eligible**.

Não use Amazon Linux 2, AMI de Marketplace, AMI com software pago ou imagem
customizada.

#### Instance type

Escolha somente um tipo que apareça naquele momento como **Free tier eligible**
e seja compatível com a AMI x86_64.

Preferência:

1. `t3.micro`, se estiver marcado;
2. `t2.micro`, se for a opção marcada da oferta legada;
3. outro tipo x86_64 somente se estiver explicitamente marcado e a oferta da
   conta tiver sido confirmada.

Não escolha `t4g`, pois ele usa arquitetura Arm e não é compatível com a AMI
x86_64 selecionada.

#### Key pair

Escolha **Proceed without a key pair**.

Neste laboratório o acesso administrativo será feito pelo EC2 Instance Connect,
que injeta uma chave pública temporária. Nenhum arquivo `.pem` será criado.

#### Network settings

Use:

- default VPC;
- uma default subnet;
- Auto-assign public IP: **Enable**;
- novo security group: `saa-lab-b03-web-sg`.

Inbound rules:

| Tipo | Porta | Source |
|---|---:|---|
| HTTP | 80 | **My IP** |
| SSH | 22 | managed prefix list `com.amazonaws.REGION.ec2-instance-connect` |

Substitua `REGION` pelo código atual, por exemplo:

```text
com.amazonaws.us-east-1.ec2-instance-connect
```

Para a regra SSH, escolha a AWS-managed prefix list exibida pelo console.

Nunca use nas regras SSH:

- `0.0.0.0/0`;
- `::/0`;
- Anywhere-IPv4;
- Anywhere-IPv6.

Se a prefix list não estiver disponível, omita completamente a porta 22 e pule
a conexão interativa. Não abra SSH global como alternativa.

Mantenha a outbound rule padrão para que a instância possa baixar o pacote
`httpd`.

#### Configure storage

Use somente o root volume:

- tamanho: **8 GiB**;
- tipo: **gp3**;
- IOPS: 3.000, baseline incluída;
- throughput: 125 MiB/s, baseline incluído;
- encrypted: **Yes**, usando a AWS managed key padrão para EBS;
- delete on termination: **Yes**.

Não adicione outro volume e não aumente IOPS ou throughput.

#### Advanced details

Configure:

- IAM instance profile: `SAA-Lab-B03-EC2-Empty`;
- purchasing option: On-Demand;
- tenancy: shared/default;
- detailed CloudWatch monitoring: **Disable**;
- termination protection: **Disable**, pois o cleanup é obrigatório;
- stop protection: Disable;
- hibernation: Disable;
- metadata accessible: **Enabled**;
- metadata version: **V2 only — token required**;
- metadata response hop limit: **1**;
- metadata tags: **Disabled**;
- IMDS IPv6 endpoint: Disabled.

Se o tipo for T3 ou T4g, configure **CPU credits = Standard** para impedir
cobrança de surplus CPU credits. T3/T4g usam Unlimited por padrão em muitos
casos.

#### User data

Cole exatamente:

```bash
#!/bin/bash
dnf install -y httpd
systemctl enable --now httpd

cat > /var/www/html/index.html <<'HTML'
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>SAA Lab B03</title>
</head>
<body>
  <h1>EC2 lab OK</h1>
  <p>Amazon Linux 2023 + Apache HTTP Server</p>
</body>
</html>
HTML
```

Não coloque senha, token, access key, account ID ou outro segredo em user data.

#### Revisão obrigatória

Antes de clicar em **Launch instance**, confirme:

```text
Number of instances: 1
AMI: Amazon Linux 2023 x86_64
Instance type: Free tier eligible
Purchase: On-Demand
Estimated total: no máximo USD 0,25
Public IPv4: 1 automático
Elastic IP: nenhum
Security group: novo, HTTP My IP e SSH somente prefix list
Root storage: 1 × gp3 8 GiB
Delete on termination: Yes
Role: SAA-Lab-B03-EC2-Empty
IMDS: V2 only / required
Detailed monitoring: disabled
User data: sem secrets
```

Somente depois escolha **Launch instance**.

Não clique novamente se o carregamento demorar. Isso poderia criar uma segunda
instância.

Copie localmente, sem publicar:

```powershell
$b03Region = '<REGION_CODE>'
$b03InstanceId = '<INSTANCE_ID>'
```

Obtenha e preserve temporariamente o ID do root volume:

```powershell
$b03VolumeId = aws ec2 describe-instances `
  --instance-ids $b03InstanceId `
  --region $b03Region `
  --profile saa-lab-b02 `
  --query 'Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId' `
  --output text `
  --no-cli-pager
```

Valide a configuração sem exibir account ID ou credenciais:

```powershell
aws ec2 describe-instances `
  --instance-ids $b03InstanceId `
  --region $b03Region `
  --profile saa-lab-b02 `
  --query 'Reservations[0].Instances[0].{State:State.Name,Type:InstanceType,IMDS:MetadataOptions.HttpTokens,RootDelete:BlockDeviceMappings[0].Ebs.DeleteOnTermination}' `
  --output table `
  --no-cli-pager
```

O esperado é:

```text
State       running ou pending
IMDS        required
RootDelete  True
```

### Etapa 4 — Validar o website — 5 minutos

Enquanto a instância inicia:

1. Abra a aba **Status checks**.
2. Aguarde `2/2 checks passed`.
3. Confirme que existe um public IPv4 automático.
4. Confirme que o root volume mostra **Delete on termination = Yes**.
5. Confirme que a role correta está associada.

No navegador, abra:

```text
http://PUBLIC_IPV4
```

Resultado esperado:

```text
EC2 lab OK
Amazon Linux 2023 + Apache HTTP Server
```

A execução de user data adiciona alguns minutos à inicialização. Se a página
ainda não responder:

1. aguarde mais dois minutos;
2. atualize o navegador;
3. confirme que HTTP 80 continua limitado ao seu IP atual;
4. confirme que o status é `2/2`;
5. não abra novas portas;
6. não lance outra instância.

Se seu IP público mudou, atualize a regra HTTP para o novo **My IP**. Não é
necessário liberar HTTP globalmente.

### Etapa 5 — Instance Connect e IMDSv2 — 5 minutos

Selecione a instância e escolha:

**Connect → EC2 Instance Connect → Connect using a Public IP**

Confirme:

- username: `ec2-user`;
- nenhuma private key;
- inbound 22 somente da managed prefix list;
- identidade não root.

O browser abre um terminal. Execute primeiro:

```bash
curl -s http://127.0.0.1/
```

A página HTML deve aparecer localmente.

Teste que IMDSv1 está bloqueado:

```bash
curl -s -o /dev/null \
  -w 'IMDSv1 HTTP status: %{http_code}\n' \
  http://169.254.169.254/latest/meta-data/instance-id
```

O resultado esperado é:

```text
IMDSv1 HTTP status: 401
```

Obtenha um token IMDSv2 de curta duração sem imprimi-lo:

```bash
TOKEN=$(curl -sS -X PUT \
  -H 'X-aws-ec2-metadata-token-ttl-seconds: 300' \
  http://169.254.169.254/latest/api/token)
```

Consulte somente metadados não secretos:

```bash
curl -sS \
  -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/placement/region

curl -sS \
  -H "X-aws-ec2-metadata-token: $TOKEN" \
  http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

O segundo comando deve retornar apenas:

```text
SAA-Lab-B03-EC2-Empty
```

Não acrescente o nome da role ao final desse URL. O endpoint abaixo retornaria
access key ID, secret access key e session token temporários:

```text
/latest/meta-data/iam/security-credentials/ROLE_NAME
```

Não o execute, não exponha o token IMDSv2 e não copie resultados para o material.

Remova a variável:

```bash
unset TOKEN
```

Se o teste IMDSv1 retornar `200`, não lance outra instância. No console, abra
**Actions → Instance settings → Modify instance metadata options**, configure
IMDSv2 como required e repita o teste. Se não puder corrigir a instância
existente, termine-a e marque o laboratório como incompleto.

Feche o terminal do Instance Connect. Em seguida, remova imediatamente do
security group a regra SSH 22 da prefix list. Mantenha somente HTTP até iniciar a
terminação.

### Etapa 6 — Terminar e auditar — 8 minutos

Selecione exatamente `SAA-Lab-B03-Web` e escolha:

**Instance state → Terminate instance**

Não escolha apenas **Stop**. Uma instância parada pode continuar mantendo EBS e
outros itens cobrados.

Confirme o nome e o instance ID antes da operação. Aguarde o estado
`terminated`.

#### Auditoria 1 — Instância

O registro da instância terminada pode permanecer visível por algum tempo. O
critério é não existir instância B03 em estado ativo.

```powershell
aws ec2 describe-instances `
  --region $b03Region `
  --profile saa-lab-b02 `
  --filters `
    'Name=tag:Name,Values=SAA-Lab-B03-Web' `
    'Name=instance-state-name,Values=pending,running,stopping,stopped,shutting-down' `
  --query 'length(Reservations[].Instances[])' `
  --output text `
  --no-cli-pager
```

Resultado esperado:

```text
0
```

#### Auditoria 2 — Root volume

No EC2, abra **Volumes** e procure exatamente `$b03VolumeId`.

Como `Delete on termination` foi configurado, o volume deve desaparecer. Se ele
ficar em estado `available`, confirme que é exatamente o volume B03 e exclua-o.
Nunca exclua volume pelo tamanho ou pela aparência.

Também é possível consultar:

```powershell
aws ec2 describe-volumes `
  --volume-ids $b03VolumeId `
  --region $b03Region `
  --profile saa-lab-b02 `
  --no-cli-pager
```

Depois da exclusão, o resultado esperado é `InvalidVolume.NotFound`.

#### Auditoria 3 — Snapshots

Abra **EC2 → Snapshots** e filtre **Owned by me**.

A quantidade deve ser igual à registrada antes. Este laboratório não cria
snapshots ou AMIs. Não exclua snapshots antigos ou snapshots públicos associados
à AMI da AWS.

Pela CLI:

```powershell
aws ec2 describe-snapshots `
  --owner-ids self `
  --region $b03Region `
  --profile saa-lab-b02 `
  --query 'length(Snapshots)' `
  --output text `
  --no-cli-pager
```

#### Auditoria 4 — Public IPv4 e Elastic IPs

O public IPv4 automático deve ser liberado com a terminação.

Abra **EC2 → Elastic IPs**. A quantidade deve permanecer igual à registrada
antes, pois nenhum EIP foi alocado.

Pela CLI:

```powershell
aws ec2 describe-addresses `
  --region $b03Region `
  --profile saa-lab-b02 `
  --query 'length(Addresses)' `
  --output text `
  --no-cli-pager
```

Não libere EIPs preexistentes.

#### Auditoria 5 — Security group

Depois que a ENI da instância desaparecer, exclua exatamente:

```text
saa-lab-b03-web-sg
```

Se o console disser que o grupo ainda está associado, aguarde a exclusão da ENI
e atualize a página. Não altere ou exclua o default security group.

#### Auditoria 6 — Role e instance profile

No IAM, exclua exatamente:

```text
SAA-Lab-B03-EC2-Empty
```

Como a role foi criada pelo console para EC2, o console também remove o instance
profile correspondente.

#### Auditoria 7 — Visão global

Abra **EC2 Global View** e procure `SAA-Lab-B03`.

Confirme em todas as Regions:

- zero instâncias B03 ativas;
- zero volumes B03;
- zero Elastic IPs B03;
- zero ENIs B03.

Global View não lista snapshots. A auditoria de snapshots continua sendo feita
na Region usada pelo laboratório.

#### Auditoria 8 — Custos

Confira novamente:

- Cost and Usage widget;
- Free Tier/credits;
- Bills;
- budget do LAB B01;
- teto operacional do B03 de USD 0,25.

Dados de cobrança e Free Tier não são atualizados em tempo real. Revise-os
novamente no dia seguinte. O alerta de budget também pode chegar com atraso.

Encerre a autenticação local:

```powershell
# IAM Identity Center:
aws sso logout

# aws login:
aws logout --profile saa-lab-b02
```

Remova as variáveis locais:

```powershell
Remove-Variable b03Region,b03InstanceId,b03VolumeId -ErrorAction SilentlyContinue
```

## 7. Tratamento de falhas

### Website não abriu

Não lance outra instância.

1. Confirme `2/2 status checks`.
2. Confirme o public IPv4.
3. Confirme HTTP 80 para seu IP atual.
4. Use EC2 Instance Connect.
5. Execute:

```bash
sudo systemctl status httpd --no-pager
sudo tail -n 30 /var/log/cloud-init-output.log
curl -s http://127.0.0.1/
```

6. Corrija a instância existente ou termine-a e marque o laboratório como
   incompleto.

### EC2 Instance Connect deu `AccessDenied`

A autenticação funcionou, mas a identidade não recebeu
`ec2-instance-connect:SendSSHPublicKey` ou outra permissão necessária.

Não use root e não anexe `AdministratorAccess` somente para contornar. Valide o
website e os parâmetros pela CLI/console, termine a instância e registre o acesso
interativo como pendente.

### A prefix list não aparece

Não use `0.0.0.0/0` como substituição. Omita a porta 22 e valide pela página HTTP
e pelas chamadas read-only da CLI.

### A instância não lançou

Não clique novamente antes de confirmar o resultado da primeira solicitação.
Pesquise pelo nome `SAA-Lab-B03-Web`. Se não houver instância e a solicitação
tiver falhado, limpe a role e o security group e encerre o laboratório.

## 8. Evidência permitida

Registre somente:

```text
Region: __________________
Account plan: Free / Paid
Credits checked: sim / não
Operational cap: USD 0,25
Estimate before launch: USD ______
AMI: Amazon Linux 2023 x86_64
Instance type: __________________
Free tier eligible label confirmed: sim / não
Number of instances launched: 1
Purchase option: On-Demand
CPU credit mode: standard / não se aplica
Public IPv4 automatic: sim
Elastic IP allocated: não
Security group HTTP source: My IP
SSH source: EC2 Instance Connect managed prefix list / omitido
Role: SAA-Lab-B03-EC2-Empty
Permissions policies on role: 0
IMDSv2 required: sim
IMDSv1 returned 401: sim / não
Website validated: sim / não
Instance terminated: sim / não
Root volume deleted: sim / não
Snapshot count unchanged: sim / não
Elastic IP count unchanged: sim / não
Security group deleted: sim / não
Role/instance profile deleted: sim / não
Global View audited: sim / não
Billing follow-up scheduled: sim / não
```

Não registre:

- instance ID;
- volume ID;
- public ou private IP;
- account ID;
- ARN;
- InstanceProfileId;
- token IMDSv2;
- access key;
- secret key;
- session token;
- saída do endpoint de credenciais.

## 9. Conexão com o exame

- EC2 é responsabilidade do cliente no guest OS, aplicação, user data,
  security group e dados.
- AMI, instance type, rede, storage, role e user data resolvem problemas
  diferentes.
- User data normalmente executa no primeiro boot e não deve conter secrets.
- Security groups são stateful e possuem somente regras `Allow`.
- HTTP e SSH não devem receber a mesma origem por conveniência.
- Uma role pode confiar no EC2 sem ter permissões para outros serviços.
- Trust policy não concede acesso a S3, DynamoDB ou outro serviço.
- Instance profile entrega a role à instância.
- IMDSv2 exige token.
- Credenciais da role são temporárias e não devem ser copiadas do metadata
  endpoint.
- `Stop` não equivale a cleanup.
- Volumes EBS, snapshots e Elastic IPs podem continuar gerando custos depois do
  compute.
- Um public IPv4 automático não é um Elastic IP.
- On-Demand é apropriado para laboratório curto e sem compromisso.
- Free tier eligibility depende da conta e da oferta vigente, não apenas do nome
  tradicional do instance type.

## 10. Referências oficiais

- [EC2 Free Tier before and after 15 July 2025](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-free-tier-usage.html)
- [AWS Free Tier FAQs](https://aws.amazon.com/free/free-tier-faqs/)
- [Launch an instance with the console wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html)
- [Amazon Linux 2023](https://docs.aws.amazon.com/linux/al2023/ug/what-is-amazon-linux.html)
- [AL2023 and IMDSv2](https://docs.aws.amazon.com/linux/al2023/ug/imdsv2.html)
- [EC2 user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
- [Configure IMDS for new instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html)
- [Access instance metadata with IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html)
- [Instance metadata categories](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)
- [Protect role credentials in instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-security-credentials.html)
- [EC2 Instance Connect prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-prerequisites.html)
- [Connect with EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html)
- [Security group recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html)
- [IAM roles for EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
- [gp3 volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html)
- [T instance Unlimited charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode.html)
- [Public IPv4 pricing](https://aws.amazon.com/vpc/pricing/)
- [Public IPv4 Free Tier allowance](https://aws.amazon.com/about-aws/whats-new/2024/02/aws-free-tier-750-hours-free-public-ipv4-addresses/)
- [How EC2 termination affects related resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html)
- [Delete an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-volume.html)
- [Delete EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-snapshot.html)
- [EC2 Global View](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/global-view.html)

**Referências verificadas em:** 24/07/2026.
