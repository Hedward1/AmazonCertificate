# LAB B02 — AWS CLI v2, credenciais temporárias e role para EC2

**Nível:** iniciante  
**Sistema:** Windows 64-bit com PowerShell  
**Tarefas oficiais:** 1.1 — Design secure access to AWS resources; 1.2 — Design
secure workloads and applications  
**Tempo líquido:** 45 minutos  
**Custo esperado:** USD 0  
**Compatibilidade:** contas Free e Paid  
**Recursos cobrados criados:** nenhum  
**Identidade permitida:** não root, configurada no LAB B01

## 1. Resultado esperado

Ao terminar, você deverá:

- validar uma instalação oficial da AWS CLI v2;
- autenticar sem criar access key permanente;
- identificar qual user ou role está chamando a AWS;
- confirmar que o profile não usa credencial de longo prazo;
- executar somente consultas de IAM e STS;
- compreender trust policy, permissions policy e instance profile;
- opcionalmente criar e excluir uma role vazia para EC2;
- encerrar a sessão sem deixar credenciais expostas.

## 2. Preencha antes de começar

```text
PLANO DA CONTA: Free / Paid / não sei
ROTA DO LAB B01: IAM Identity Center / IAM user transitório
REGION PADRÃO DO LAB B01: __________________
PROFILE DESTE LAB: saa-lab-b02
IDENTIDADE NÃO ROOT CONFIRMADA: sim / não
```

Este laboratório não cria AWS Organizations, não habilita IAM Identity Center e
não lança EC2. Se o Identity Center já foi configurado no B01, apenas o
utilizaremos.

## 3. Regras de segurança

Durante o laboratório:

- não entre como root;
- não crie access key;
- não execute `aws configure` sem o subcomando `sso`;
- não abra ou copie arquivos de cache em `%USERPROFILE%\.aws`;
- não execute comandos com `--debug`;
- não mostre senha, código MFA, token, account ID ou ARN completos;
- use `--profile saa-lab-b02` explicitamente;
- se aparecer `AccessDenied`, analise a autorização e não amplie permissões
  apenas para concluir o exercício.

`sts get-caller-identity` mostra account ID, user ID e ARN. Confira a saída
localmente; não a copie nem publique captura.

## 4. Roteiro de 45 minutos

### Etapa 1 — Preparação segura — 5 minutos

Feche qualquer sessão root no navegador e abra um PowerShell novo.

Confira somente os nomes das variáveis AWS existentes, nunca seus valores:

```powershell
Get-ChildItem Env:AWS_* | Select-Object -ExpandProperty Name
```

Se aparecerem variáveis de credencial, remova-as somente desta janela para
evitar que uma credencial antiga tenha precedência:

```powershell
Remove-Item Env:AWS_ACCESS_KEY_ID -ErrorAction SilentlyContinue
Remove-Item Env:AWS_SECRET_ACCESS_KEY -ErrorAction SilentlyContinue
Remove-Item Env:AWS_SESSION_TOKEN -ErrorAction SilentlyContinue
Remove-Item Env:AWS_SECURITY_TOKEN -ErrorAction SilentlyContinue
```

Isso não apaga configurações permanentes nem altera outras janelas abertas.

### Etapa 2 — Instalar ou validar a AWS CLI v2 — 7 minutos

```powershell
Get-Command aws -ErrorAction SilentlyContinue
where.exe aws
aws --version
```

O resultado precisa começar com `aws-cli/2.`.

Se o comando não existir ou mostrar versão 1, use o instalador oficial para o
usuário atual:

<https://awscli.amazonaws.com/AWSCLIV2-User.msi>

Esse instalador não exige privilégio administrativo. Depois, feche e reabra o
PowerShell e repita a validação.

Se `where.exe aws` mostrar vários executáveis, não desinstale nada
automaticamente. Registre o conflito e confirme qual caminho `Get-Command aws`
selecionou.

Para usar `aws login`, a versão mínima é 2.32.0. Na rota IAM Identity Center,
mantenha a CLI v2 atualizada.

### Etapa 3 — Autenticar com credenciais temporárias — 10 minutos

Execute somente a rota correspondente ao LAB B01.

#### Rota A — IAM Identity Center

Se o profile ainda não existir:

```powershell
aws configure sso --profile saa-lab-b02
```

Use o Start URL ou Issuer URL, a SSO Region, a conta e o permission set definidos
no B01. Depois:

```powershell
aws sso login --profile saa-lab-b02
```

O navegador deve mostrar a identidade do IAM Identity Center, nunca root.

#### Rota B — `aws login` com IAM user transitório

A identidade precisa da AWS managed policy
`SignInLocalDevelopmentAccess`. Ela permite o fluxo de autenticação local; não
concede acesso geral aos demais serviços.

```powershell
aws login --profile saa-lab-b02
```

No navegador, selecione `saa-admin`, nunca uma sessão root. Nenhuma access key
deve ser criada ou digitada.

### Etapa 4 — Validar profile e identidade — 8 minutos

```powershell
aws configure list-profiles
aws configure list --profile saa-lab-b02
aws sts get-caller-identity --profile saa-lab-b02 --output json --no-cli-pager
```

Valide localmente:

- na rota `aws login`, a fonte deve ser `login`;
- na rota Identity Center, a fonte deve ser SSO;
- a fonte não deve ser `shared-credentials-file` nem `env`;
- o ARN não deve terminar em `:root`;
- a conta deve ser a conta de laboratório;
- no Identity Center, é normal o ARN representar uma `assumed-role`.

Se a fonte for `shared-credentials-file` ou `env`, pare. Não apague a pasta
`.aws`; investigue a origem ou use um profile novo.

`sts get-caller-identity` é útil porque identifica o principal efetivo e não
exige uma permissão explícita.

### Etapa 5 — Consultas e exercício de role — 9 minutos

Comece com consultas somente leitura:

```powershell
aws iam get-account-summary `
  --profile saa-lab-b02 `
  --output table `
  --no-cli-pager

aws iam list-roles `
  --profile saa-lab-b02 `
  --max-items 10 `
  --query 'Roles[].{Role:RoleName,Created:CreateDate}' `
  --output table `
  --no-cli-pager
```

- `get-account-summary` mostra contagens e indicadores da conta.
- `list-roles` mostra identidades assumíveis, não credenciais permanentes.
- Se ocorrer `AccessDenied`, a autenticação funcionou, mas a autorização não
  permitiu a ação. Não use root para contornar.

#### Exercício opcional — role vazia para EC2

Execute somente se a identidade tiver autorização administrativa previamente
aprovada.

1. No IAM, abra **Roles** e escolha **Create role**.
2. Selecione **AWS service** e o caso de uso **EC2**.
3. Continue sem escolher permissions policy.
4. Nomeie a role `SAA-Lab-B02-EC2-Empty`.
5. Não anexe `AdministratorAccess`, não crie inline policy e não abra o
   assistente de lançamento do EC2.

Valide:

```powershell
aws iam get-role `
  --role-name SAA-Lab-B02-EC2-Empty `
  --profile saa-lab-b02 `
  --query 'Role.{Name:RoleName,TrustedService:AssumeRolePolicyDocument.Statement[0].Principal.Service}' `
  --output table `
  --no-cli-pager

aws iam list-attached-role-policies `
  --role-name SAA-Lab-B02-EC2-Empty `
  --profile saa-lab-b02 `
  --output table `
  --no-cli-pager

aws iam list-instance-profiles-for-role `
  --role-name SAA-Lab-B02-EC2-Empty `
  --profile saa-lab-b02 `
  --query 'InstanceProfiles[].InstanceProfileName' `
  --output table `
  --no-cli-pager
```

Resultado conceitual:

- o trusted service é `ec2.amazonaws.com`;
- a lista de permissions policies está vazia;
- sem `Allow`, as ações continuam implicitamente negadas;
- o console cria o instance profile usado para entregar a role à instância;
- nenhuma instância foi criada.

### Etapa 6 — Cleanup e logout — 6 minutos

Se criou a role, exclua exatamente `SAA-Lab-B02-EC2-Empty` pelo console IAM.
Confirme:

```powershell
aws iam get-role `
  --role-name SAA-Lab-B02-EC2-Empty `
  --profile saa-lab-b02 `
  --no-cli-pager
```

O resultado esperado é `NoSuchEntity`.

Encerre a autenticação correspondente:

```powershell
# Rota IAM Identity Center — encerra as sessões SSO locais da AWS CLI:
aws sso logout

# Rota aws login — encerra o profile indicado:
aws logout --profile saa-lab-b02
```

Teste a ausência da sessão:

```powershell
aws sts get-caller-identity --profile saa-lab-b02 --no-cli-pager
```

Sem nova autenticação, a chamada deve falhar. Não apague
`%USERPROFILE%\.aws`; outros profiles podem existir. Mantenha a CLI instalada.

## 5. Extensão opcional — IAM credential report

Se restarem 5–10 minutos, abra **IAM → Credential report** e gere o relatório.
Ele contém metadados sensíveis; não o salve nesta pasta/OneDrive nem o envie por
chat.

Confira apenas:

- `mfa_active`;
- `access_key_1_active`;
- `access_key_2_active`;
- a linha `root_account`;
- a linha de `saa-admin`, se existir.

O relatório cobre root e IAM users. Roles e usuários do IAM Identity Center não
aparecem como IAM users.

## 6. Evidência permitida

Registre somente:

```text
AWS CLI: versão 2.__.__
Rota: IAM Identity Center / aws login
Profile: saa-lab-b02
Credential source: sso / login
Caller: IAM user / assumed role
Root utilizado: não
Consultas IAM: sucesso / AccessDenied analisado
Role temporária criada: sim / não
Role temporária removida: sim / não se aplica
EC2 lançado: não
Logout confirmado: sim / não
Custo esperado: USD 0
```

Não registre account ID, user ID, ARN completo, URL do portal, códigos, tokens
ou conteúdo dos caches.

## 7. Conexão com o exame

- autenticação determina quem está chamando;
- autorização determina o que a identidade pode executar;
- `AccessDenied` pode indicar autenticação bem-sucedida e autorização negada;
- profiles selecionam credenciais/configurações, não concedem permissões;
- credenciais temporárias são preferíveis a access keys permanentes;
- trust policy e permissions policy respondem perguntas diferentes;
- uma role confiável para EC2, sem permissions policy, não recebe acesso aos
  recursos.

## 8. Referências oficiais

- [Install or update AWS CLI on Windows](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS CLI authentication options](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)
- [`aws login`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)
- [`SignInLocalDevelopmentAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/SignInLocalDevelopmentAccess.html)
- [AWS CLI with IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)
- [`sts get-caller-identity`](https://docs.aws.amazon.com/cli/latest/reference/sts/get-caller-identity.html)
- [Create a service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html)
- [Delete roles and instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html)
- [IAM credential report](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)

**Referências verificadas em:** 24/07/2026.
