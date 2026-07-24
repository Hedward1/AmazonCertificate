# LAB B04 — Inventário EC2, ENI, placement, hibernação, EBS e AMI

**Nível:** iniciante absoluto  
**Sistema local:** Windows com navegador e PowerShell  
**Tempo líquido:** 30 minutos  
**Aulas relacionadas:** 47–60, com foco em endereçamento EC2, ENIs,
placement groups, hibernação, EBS, snapshots e AMIs  
**Capítulo relacionado:** [B04 — IPs, ENIs, placement groups, hibernação,
EBS, snapshots e AMIs](../03_Guia_do_Estudante/Capitulos/B04_IPs_ENI_Placement_Hibernation_EBS_Snapshots_e_AMI.md)  
**Domínios oficiais:** 2 — Design Resilient Architectures; 3 — Design
High-Performing Architectures; 4 — Design Cost-Optimized Architectures  
**Profile da CLI:** `saa-lab-b02`, criado no LAB B02  
**Modo do laboratório:** somente leitura  
**Recursos que podem ser criados:** zero  
**Custo esperado:** **USD 0,00**

## 1. Resultado esperado

Ao terminar, você deverá ter:

- reaberto com segurança a sessão encerrada no LAB B03;
- registrado um inventário inicial e final sem expor identificadores;
- relacionado Region, Availability Zone, subnet, ENI e endereço IP;
- diferenciado private IPv4, public IPv4 automático e Elastic IP;
- explicado o comportamento dos endereços em reboot, stop, hibernate e
  terminate;
- escolhido `cluster`, `partition` ou `spread` para três cenários;
- consultado se um instance type oferece suporte a hibernação;
- explicado onde a RAM é preservada e o limite vigente de 60 dias;
- distinguido o escopo de EBS volumes, EBS snapshots e AMIs;
- inspecionado o block device mapping de uma AMI pública;
- confirmado que nenhuma quantidade foi alterada pelo laboratório;
- encerrado a autenticação e removido somente variáveis e funções locais.

O laboratório não lança instância. Ele reutiliza o modelo mental e as evidências
não sensíveis do LAB B03, cujo cleanup já deve ter sido concluído.

## 2. Arquitetura observada

```text
Region
├── Elastic IP allocation
├── placement group
├── EBS snapshot
└── AMI

Availability Zone
├── subnet
├── ENI
│   ├── private IPv4
│   ├── associação opcional com public IPv4 ou Elastic IP
│   └── security groups
└── EBS volume

EC2 instance
├── primary ENI — device index 0
├── EBS root/data volumes
└── RAM e processos
```

O LAB B03 já demonstrou uma instância com ENI primária, public IPv4 automático
e root volume EBS. Como a instância foi terminada com
`DeleteOnTermination=true`, o B04 observa o inventário ou usa diagramas em vez
de recriar esses recursos.

## 3. Custos, escopo e regras de segurança

### Custo esperado

O custo esperado deste laboratório é **USD 0,00**, pois ele executa somente
consultas de metadados e inventário. Nenhum recurso faturável é provisionado.

Recursos preexistentes na conta podem continuar gerando seus próprios custos.
Este laboratório não autoriza sua alteração ou exclusão.

### Operações permitidas

Use somente:

- `aws sso login` ou `aws login`, conforme a autenticação já configurada;
- `aws sts get-caller-identity`;
- `aws ec2 describe-*`;
- `aws ssm get-parameter`;
- logout;
- criação e remoção de variáveis ou funções somente no PowerShell local.

### Operações proibidas

Não execute comandos ou botões com:

- `run-instances`;
- `create`;
- `allocate`;
- `associate`;
- `attach`;
- `modify`;
- `copy`;
- `delete`;
- `deregister`;
- `release`;
- `terminate`.

Não crie:

- instância;
- ENI;
- Elastic IP;
- placement group;
- EBS volume;
- EBS snapshot;
- AMI;
- VPC, subnet ou qualquer outro recurso.

Embora criar um placement group isolado não tenha cobrança direta, isso não
produziria uma observação útil sem instâncias. Por isso, a criação também fica
proibida.

### Regra para `AccessDenied` e outros erros

Uma chamada que retorna `AccessDenied`, timeout, falha de autenticação ou
qualquer outro erro **não equivale a uma contagem zero**.

Essa contagem deve ser marcada como:

```text
INVÁLIDA / NÃO VERIFICADA
```

A função deste laboratório interrompe o inventário se uma chamada falhar, para
evitar que saída vazia seja convertida incorretamente em zero. Não conceda
permissões adicionais, não anexe `AdministratorAccess` e não use a conta root
para contornar uma falha.

Se a mesma informação puder ser vista no console com a identidade atual,
registre manualmente a contagem. Caso contrário, conclua apenas as etapas
conceituais e marque a validação do inventário como incompleta.

## 4. Preflight

Preencha antes de iniciar:

```text
DATA: __________________
REGION USADA NO LAB B03: __________________
PROFILE: saa-lab-b02
IDENTIDADE NÃO ROOT CONFIRMADA: sim / não
CLEANUP DO LAB B03 CONFIRMADO: sim / não
ACTIVE INSTANCES ANTES: ______ / inválida
ENIs ANTES: ______ / inválida
ELASTIC IPs ANTES: ______ / inválida
EBS VOLUMES ANTES: ______ / inválida
SNAPSHOTS OWNED BY ME ANTES: ______ / inválida
AMIs OWNED BY ME ANTES: ______ / inválida
PLACEMENT GROUPS ANTES: ______ / inválida
CUSTO ESPERADO B04: USD 0,00
```

Se o LAB B03 ainda tiver instância, ENI, volume, security group ou outro resíduo,
não use o B04 como justificativa para excluí-lo. Volte ao cleanup documentado do
LAB B03 e confirme os IDs e nomes exatos antes de qualquer ação.

### 4.1 Login após o logout do LAB B03

O LAB B03 terminou com logout. Portanto, autentique novamente usando **apenas
uma** das rotas que já foi configurada no LAB B02.

Se usa IAM Identity Center:

```powershell
aws sso login --profile saa-lab-b02
```

Se usa `aws login`:

```powershell
aws login --profile saa-lab-b02
```

Não execute as duas rotas.

Configure variáveis locais:

```powershell
$b04Profile = 'saa-lab-b02'
$b04Region = '<REGION_USADA_NO_LAB_B03>'
$b04InstanceType = 't3.micro'
```

Se o LAB B03 utilizou outro instance type, substitua `t3.micro` pelo tipo
registrado em sua evidência. Essa variável será usada somente em uma consulta.

Confira localmente a identidade:

```powershell
aws sts get-caller-identity `
  --profile $b04Profile `
  --no-cli-pager
```

O ARN não pode ser root. Não copie a saída, pois ela contém identificadores da
conta e da identidade.

Se esse comando falhar, pare. Nenhuma contagem posterior será válida até a
autenticação funcionar.

### 4.2 Função local de inventário

Cole a função no PowerShell:

```powershell
function Get-B04Inventory {
    $counts = [ordered]@{}

    $counts.ActiveInstances = aws ec2 describe-instances `
        --region $b04Region `
        --profile $b04Profile `
        --filters 'Name=instance-state-name,Values=pending,running,stopping,stopped,shutting-down' `
        --query 'length(Reservations[].Instances[])' `
        --output text `
        --no-cli-pager
    if ($LASTEXITCODE -ne 0) {
        throw 'ActiveInstances inválida; não interprete a falha como zero.'
    }

    $counts.ENIs = aws ec2 describe-network-interfaces `
        --region $b04Region `
        --profile $b04Profile `
        --query 'length(NetworkInterfaces)' `
        --output text `
        --no-cli-pager
    if ($LASTEXITCODE -ne 0) {
        throw 'ENIs inválida; não interprete a falha como zero.'
    }

    $counts.ElasticIPs = aws ec2 describe-addresses `
        --region $b04Region `
        --profile $b04Profile `
        --query 'length(Addresses)' `
        --output text `
        --no-cli-pager
    if ($LASTEXITCODE -ne 0) {
        throw 'ElasticIPs inválida; não interprete a falha como zero.'
    }

    $counts.Volumes = aws ec2 describe-volumes `
        --region $b04Region `
        --profile $b04Profile `
        --query 'length(Volumes)' `
        --output text `
        --no-cli-pager
    if ($LASTEXITCODE -ne 0) {
        throw 'Volumes inválida; não interprete a falha como zero.'
    }

    $counts.OwnedSnapshots = aws ec2 describe-snapshots `
        --owner-ids self `
        --region $b04Region `
        --profile $b04Profile `
        --query 'length(Snapshots)' `
        --output text `
        --no-cli-pager
    if ($LASTEXITCODE -ne 0) {
        throw 'OwnedSnapshots inválida; não interprete a falha como zero.'
    }

    $counts.OwnedAMIs = aws ec2 describe-images `
        --owners self `
        --region $b04Region `
        --profile $b04Profile `
        --query 'length(Images)' `
        --output text `
        --no-cli-pager
    if ($LASTEXITCODE -ne 0) {
        throw 'OwnedAMIs inválida; não interprete a falha como zero.'
    }

    $counts.PlacementGroups = aws ec2 describe-placement-groups `
        --region $b04Region `
        --profile $b04Profile `
        --query 'length(PlacementGroups)' `
        --output text `
        --no-cli-pager
    if ($LASTEXITCODE -ne 0) {
        throw 'PlacementGroups inválida; não interprete a falha como zero.'
    }

    foreach ($name in @($counts.Keys)) {
        $rawCount = ([string]$counts[$name]).Trim()
        if ($rawCount -notmatch '^\d+$') {
            throw "$name inválida; a resposta não é uma contagem inteira."
        }
        $counts[$name] = [int]$rawCount
    }

    [pscustomobject]$counts
}
```

A função usa apenas chamadas `describe`. Ela não exclui nem altera recursos.

## 5. Roteiro de 30 minutos

### Etapa 1 — Inventário inicial — 4 minutos

Execute:

```powershell
$b04Before = Get-B04Inventory
$b04Before
```

Copie somente as contagens para a ficha de preflight. Não registre IDs, IPs,
ARNs ou account ID.

Se ocorrer `AccessDenied`, a função lançará um erro e não retornará um inventário
válido. Não crie manualmente um objeto com zero para prosseguir.

No console, a inspeção equivalente fica em:

- **EC2 → Instances**;
- **EC2 → Network Interfaces**;
- **EC2 → Elastic IPs**;
- **EC2 → Volumes**;
- **EC2 → Snapshots → Owned by me**;
- **EC2 → AMIs → Owned by me**;
- **EC2 → Placement Groups**.

Não selecione botões de criação ou exclusão.

### Etapa 2 — Private IP, public IP e ENI — 6 minutos

Liste as Availability Zones disponíveis:

```powershell
aws ec2 describe-availability-zones `
  --region $b04Region `
  --profile $b04Profile `
  --filters 'Name=state,Values=available' `
  --query 'AvailabilityZones[].{AZ:ZoneName,AZID:ZoneId,State:State}' `
  --output table `
  --no-cli-pager
```

Observe as default subnets sem revelar seus IDs:

```powershell
aws ec2 describe-subnets `
  --region $b04Region `
  --profile $b04Profile `
  --filters 'Name=default-for-az,Values=true' `
  --query 'Subnets[].{AZ:AvailabilityZone,AutoPublicIPv4:MapPublicIpOnLaunch,AvailablePrivateIPv4:AvailableIpAddressCount}' `
  --output table `
  --no-cli-pager
```

Uma lista vazia pode significar que não há default VPC nessa Region. Não
interprete isso como falha se o comando terminou com exit code zero.

Resuma as ENIs sem mostrar endereços ou identificadores:

```powershell
aws ec2 describe-network-interfaces `
  --region $b04Region `
  --profile $b04Profile `
  --query '{Total:length(NetworkInterfaces),Available:length(NetworkInterfaces[?Status==`available`]),InUse:length(NetworkInterfaces[?Status==`in-use`]),WithPublicIPv4:length(NetworkInterfaces[?Association.PublicIp])}' `
  --output table `
  --no-cli-pager
```

Conte os Elastic IPs:

```powershell
aws ec2 describe-addresses `
  --region $b04Region `
  --profile $b04Profile `
  --query '{Allocated:length(Addresses),Associated:length(Addresses[?AssociationId])}' `
  --output table `
  --no-cli-pager
```

Se qualquer comando retornar `AccessDenied`, aquela observação é inválida. Não
registre zero.

Reconstrua a instância do LAB B03:

```text
subnet em uma AZ
└── EC2 instance
    └── primary ENI — device index 0
        ├── private IPv4
        ├── security groups
        ├── MAC address
        └── public IPv4 automático temporário
```

Complete:

| Evento | Private IPv4 | Public IPv4 automático | Elastic IP |
|---|---|---|---|
| reboot | permanece | permanece | permanece |
| stop/start | permanece | liberado; normalmente recebe outro | permanece associado |
| hibernate/start | permanece | liberado; normalmente recebe outro | permanece associado |
| terminate | liberado com a ENI | liberado | desassociado, mas continua alocado |

Conclusões:

- a ENI pertence a uma subnet e não atravessa AZs;
- a ENI primária não pode ser destacada;
- uma ENI secundária pode mover private IPs e security groups entre instâncias
  compatíveis na mesma AZ;
- public IPv4 automático e Elastic IP não são o mesmo recurso;
- desassociar um Elastic IP não o libera e não encerra sua cobrança.

### Etapa 3 — Placement groups — 5 minutos

Consulte somente estratégias e estados existentes:

```powershell
aws ec2 describe-placement-groups `
  --region $b04Region `
  --profile $b04Profile `
  --query 'PlacementGroups[].{Strategy:Strategy,State:State,Partitions:PartitionCount}' `
  --output table `
  --no-cli-pager
```

Uma resposta vazia é esperada em uma conta de estudos limpa. Não crie um grupo.

Resolva:

| Cenário | Escolha | Razão |
|---|---|---|
| Simulação HPC tightly coupled, baixa latência e alto throughput em uma AZ | `cluster` | aproxima as instâncias |
| Kafka ou Cassandra grande, com réplicas topology-aware | `partition` | separa grupos de racks |
| Três instâncias críticas que não devem compartilhar hardware | `spread` | separa cada instância por hardware |

Regras para a prova:

- `cluster`: desempenho de rede, uma AZ, maior risco de falha correlacionada;
- `partition`: grandes sistemas distribuídos, até sete partições por AZ;
- `spread`: poucos nós críticos, até sete instâncias em execução por AZ por
  grupo;
- `precision time`: atualização da documentação atual para fontes locais de
  tempo com precisão de microssegundos; não substitui as três estratégias das
  aulas.

### Etapa 4 — Hibernação — 4 minutos

Consulte os metadados do instance type estudado:

```powershell
aws ec2 describe-instance-types `
  --instance-types $b04InstanceType `
  --region $b04Region `
  --profile $b04Profile `
  --query 'InstanceTypes[0].{Type:InstanceType,Hibernation:HibernationSupported,MemoryMiB:MemoryInfo.SizeInMiB,MaxENIs:NetworkInfo.MaximumNetworkInterfaces,IPv4PerENI:NetworkInfo.Ipv4AddressesPerInterface,Architectures:ProcessorInfo.SupportedArchitectures}' `
  --output json `
  --no-cli-pager
```

Essa consulta mostra características; ela não inicia uma instância e não garante
capacidade de lançamento na AZ.

No console, a alternativa é:

**EC2 → Instance Types → filtro On-Demand Hibernation support = true**

Não escolha **Launch instance**.

Fluxo:

```text
running
   │ hibernate
   ▼
RAM gravada no EBS root volume criptografado
   │
   ▼
stopped — sem cobrança de compute
   │ start
   ▼
RAM e processos restaurados
```

Pré-requisitos essenciais:

- habilitar hibernação durante o lançamento;
- usar AMI, sistema operacional, Region e instance type compatíveis;
- usar EBS como root volume;
- manter o root volume criptografado;
- dimensionar o root para o sistema, aplicações e conteúdo da RAM;
- usar um tipo de EBS compatível.

A AWS não oferece suporte a manter uma instância continuamente hibernada por
mais de **60 dias**. Ela deve ser iniciada antes de exceder esse período.

Enquanto hibernada:

- compute da instância não é cobrado no estado `stopped`;
- EBS continua armazenado e cobrado;
- RAM ocupa espaço no root volume;
- private IPv4 e IPv6 permanecem;
- public IPv4 automático é liberado;
- Elastic IP permanece associado e sujeito a cobrança;
- dados de instance store são perdidos.

Não habilite nem execute hibernação neste laboratório.

### Etapa 5 — EBS, snapshots e AMIs — 7 minutos

Resuma os volumes:

```powershell
aws ec2 describe-volumes `
  --region $b04Region `
  --profile $b04Profile `
  --query '{Total:length(Volumes),Available:length(Volumes[?State==`available`]),InUse:length(Volumes[?State==`in-use`])}' `
  --output table `
  --no-cli-pager
```

Conte snapshots e AMIs próprios:

```powershell
aws ec2 describe-snapshots `
  --owner-ids self `
  --region $b04Region `
  --profile $b04Profile `
  --query '{OwnedSnapshots:length(Snapshots)}' `
  --output table `
  --no-cli-pager
```

```powershell
aws ec2 describe-images `
  --owners self `
  --region $b04Region `
  --profile $b04Profile `
  --query '{OwnedAMIs:length(Images)}' `
  --output table `
  --no-cli-pager
```

Após o cleanup correto do B03, o root volume com
`DeleteOnTermination=true` não deve existir. Não lance outra instância para
substituir essa evidência.

Consulte o parâmetro público da AMI Amazon Linux 2023 mantido pela AWS:

```powershell
$b04AmiId = aws ssm get-parameter `
  --name '/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64' `
  --region $b04Region `
  --profile $b04Profile `
  --query 'Parameter.Value' `
  --output text `
  --no-cli-pager
if ($LASTEXITCODE -ne 0) {
    throw 'AMI pública não verificada; não trate a resposta como um ID válido.'
}
```

Não registre o AMI ID. Use-o apenas na consulta:

```powershell
aws ec2 describe-images `
  --image-ids $b04AmiId `
  --region $b04Region `
  --profile $b04Profile `
  --query 'Images[0].{State:State,Architecture:Architecture,RootDeviceType:RootDeviceType,RootDeviceName:RootDeviceName,Virtualization:VirtualizationType,BlockDevices:BlockDeviceMappings[].{DeviceName:DeviceName,VolumeType:Ebs.VolumeType,SizeGiB:Ebs.VolumeSize,DeleteOnTermination:Ebs.DeleteOnTermination}}' `
  --output json `
  --no-cli-pager
```

Se `get-parameter` ou `describe-images` falhar, a inspeção da AMI é inválida.
Não tente criar ou copiar uma AMI como alternativa.

Modelo mental:

```text
AMI — regional
  │ launch
  ▼
EC2 + EBS volume — volume pertence a uma AZ
              │ snapshot
              ▼
        EBS snapshot — regional
              │
              ├── novo volume em qualquer AZ da mesma Region
              ├── cópia para outra Region
              └── block device mapping de uma AMI
```

Conclusões:

- EBS volume é zonal e deve estar na mesma AZ da instância;
- EBS persiste em stop/start e continua cobrado até ser excluído;
- `DeleteOnTermination` é avaliado em terminate, não em stop;
- snapshot é um backup point-in-time regional;
- snapshots posteriores são incrementais, mas cada um é um ponto lógico
  completo de restauração;
- excluir um volume não exclui seus snapshots;
- AMI é um modelo regional e pode referenciar snapshots EBS;
- desregistrar uma AMI não termina instâncias existentes;
- snapshots associados podem permanecer depois do deregister e continuar
  cobrados.

### Etapa 6 — Validação e cleanup local — 4 minutos

Repita o inventário:

```powershell
$b04After = Get-B04Inventory
$b04After
```

Compare:

```powershell
$b04Unchanged = `
    ($b04Before | ConvertTo-Json -Compress) -eq `
    ($b04After | ConvertTo-Json -Compress)

$b04Unchanged
```

Resultado esperado:

```text
True
```

Esse teste só é válido se os dois inventários terminaram sem `AccessDenied` ou
outro erro. Contagens inválidas não podem ser comparadas nem substituídas por
zero.

Se o resultado for `False`:

1. mostre `$b04Before` e `$b04After`;
2. descubra qual contagem mudou;
3. verifique se outra pessoa ou automação alterou a conta;
4. não exclua, termine, desassocie ou libere recursos;
5. registre “alteração externa ou preexistente a investigar”.

O B04 não criou recursos AWS. Portanto, não existe cleanup no ambiente cloud.
Não exclua recursos preexistentes para tentar deixar todas as contagens em zero.
O objetivo é manter o valor final igual ao inicial, não tornar a conta vazia.

Remova somente o estado local criado neste PowerShell:

```powershell
Remove-Variable `
  b04Profile,b04Region,b04InstanceType,b04AmiId,`
  b04Before,b04After,b04Unchanged `
  -ErrorAction SilentlyContinue

Remove-Item function:Get-B04Inventory -ErrorAction SilentlyContinue
```

Encerre a autenticação usando somente a rota correspondente ao login:

```powershell
# IAM Identity Center:
aws sso logout

# aws login:
aws logout --profile saa-lab-b02
```

Não é necessário executar as duas rotas.

## 6. Validação conceitual

Responda sem consultar o capítulo:

1. Por que um public IPv4 automático pode mudar depois de `stop/start`?
2. Por que uma ENI não pode ser movida para outra AZ?
3. Qual placement group atende HPC tightly coupled?
4. Qual placement group atende Kafka topology-aware?
5. Qual placement group separa três instâncias críticas por hardware?
6. Onde a RAM é gravada durante a hibernação?
7. Qual é o limite vigente de permanência contínua em hibernação?
8. Qual recurso é zonal: volume EBS, snapshot ou AMI?
9. Como recuperar os dados de um volume em outra AZ da mesma Region?
10. Por que o deregister de uma AMI pode não concluir o cleanup?

Respostas:

1. O endereço automático é liberado no stop e outro pode ser atribuído no
   start.
2. A ENI pertence a uma subnet, e a subnet pertence a uma única AZ.
3. `cluster`.
4. `partition`.
5. `spread`.
6. No EBS root volume criptografado.
7. 60 dias.
8. O EBS volume; snapshot e AMI são regionais.
9. Criar conceitualmente um snapshot e, a partir dele, um novo volume na AZ de
   destino. Essa criação será praticada em outro laboratório, não no B04.
10. Porque snapshots associados podem permanecer e continuar cobrados.

## 7. Tratamento de falhas

### Login expirou

Use novamente somente a rota configurada no LAB B02. Depois repita
`get-caller-identity`. Não crie novas access keys.

### Uma consulta retornou `AccessDenied`

- marque a contagem como `INVÁLIDA / NÃO VERIFICADA`;
- não registre zero;
- não altere permissões;
- não use root;
- tente apenas a visualização equivalente no console com a identidade atual;
- se ela também estiver indisponível, marque a validação como incompleta.

### Não existem default subnets

Continue com os diagramas. A ausência de default VPC não é motivo para criar
VPC ou subnet neste laboratório.

### O parâmetro público da AMI não respondeu

Não use um AMI ID copiado de material antigo e não crie uma AMI. No console,
observe uma Amazon Linux 2023 AMI pública no **AMI Catalog** sem iniciar o
assistente de lançamento.

### O inventário final mudou

Não faça cleanup por contagem. Um número não identifica o proprietário nem a
origem do recurso. Registre a diferença e investigue fora do LAB B04 usando
tags, IDs e o responsável pela conta.

## 8. Evidência permitida

Registre somente:

```text
Region: __________________
Instance type consultado: __________________
HibernationSupported: true / false / não verificado
Continuous hibernation limit: 60 dias
Default subnet auto-assign public IPv4: true / false / não existe / não verificado
Placement para HPC: cluster
Placement para Kafka/Cassandra: partition
Placement para três nós críticos: spread
Recurso zonal: EBS volume
Recursos regionais: EBS snapshot e AMI
Active instances — antes/depois: ______ / ______
ENIs — antes/depois: ______ / ______
Elastic IPs — antes/depois: ______ / ______
EBS volumes — antes/depois: ______ / ______
Snapshots owned by me — antes/depois: ______ / ______
AMIs owned by me — antes/depois: ______ / ______
Placement groups — antes/depois: ______ / ______
Todas as contagens válidas: sim / não
Inventário unchanged: true / false / inválido
Recursos criados pelo LAB B04: zero
Recursos preexistentes excluídos: zero
Custo esperado: USD 0,00
Logout concluído: sim / não
Função local removida: sim / não
```

Não registre:

- account ID;
- ARN ou User ID;
- instance ID;
- ENI ID;
- subnet ID;
- volume ID;
- snapshot ID;
- AMI ID;
- public ou private IP;
- access key, secret key ou session token;
- captura de tela que exponha esses valores.

## 9. Conexão com o exame

- Private IPv4 permanece em reboot, stop/start e hibernate/start.
- Public IPv4 automático permanece em reboot, mas muda em stop/start e
  hibernate/start.
- Elastic IP permanece alocado até ser liberado e pode gerar cobrança.
- Uma ENI pertence a uma subnet e não atravessa AZs.
- Security groups são associados às ENIs.
- `cluster` prioriza rede; `partition` separa grupos; `spread` separa poucos
  nós críticos.
- Placement group não replica dados e não substitui uma arquitetura Multi-AZ.
- Hibernate preserva RAM no EBS root; stop não preserva RAM.
- Hibernação deve ser habilitada durante o lançamento.
- A permanência contínua em hibernação é limitada a 60 dias.
- Instância hibernada não cobra compute, mas EBS e Elastic IP podem continuar
  cobrando.
- EBS volume é zonal; EBS snapshot e AMI são regionais.
- `DeleteOnTermination` não é usado em stop.
- Excluir um volume não exclui snapshots.
- Deregister de AMI não afeta instâncias já lançadas e não deve ser tratado
  como prova de remoção dos snapshots.

## 10. Checklist final

- [ ] Usei somente uma rota de login.
- [ ] Confirmei que a identidade não era root.
- [ ] Todas as chamadas AWS foram de autenticação ou leitura.
- [ ] Não interpretei `AccessDenied` ou saída vazia como zero.
- [ ] Não criei instância, ENI, EIP, placement group, volume, snapshot ou AMI.
- [ ] Não excluí recursos preexistentes.
- [ ] Expliquei a mudança do public IPv4 após stop ou hibernate.
- [ ] Escolhi corretamente cluster, partition e spread.
- [ ] Expliquei a hibernação e seu limite de 60 dias.
- [ ] Diferenciei EBS volume, snapshot e AMI por escopo.
- [ ] O inventário final válido ficou igual ao inicial válido.
- [ ] Removi variáveis e `function:Get-B04Inventory` do PowerShell.
- [ ] Encerrei a autenticação.
- [ ] Registrei custo esperado de USD 0,00.

## 11. Referências oficiais

- [EC2 instance IP addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html)
- [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
- [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)
- [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
- [Placement strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html)
- [Stop and start EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)
- [Hibernate an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html)
- [How EC2 hibernation works and its limitations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-hibernate-overview.html)
- [Hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html)
- [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html)
- [How EBS snapshots work](https://docs.aws.amazon.com/ebs/latest/userguide/how_snapshots_work.html)
- [Create an EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-snapshot.html)
- [Delete an EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-snapshot.html)
- [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [Find AMIs with AWS Systems Manager public parameters](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami-parameter-store.html)
- [Deregister an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html)

**Referências verificadas em:** 24/07/2026.
