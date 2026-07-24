# LAB B01 — Segurança da conta, orçamento e acesso temporário

**Nível:** iniciante  
**Tarefa oficial:** 1.1 — Design secure access to AWS resources  
**Parte principal:** 35–50 minutos  
**Extensão opcional de CLI:** 15–25 minutos; também pode ser concluída no B02  
**Custo esperado deste laboratório:** USD 0, pois nenhum recurso de workload será
criado e o budget usará somente monitoramento/notificações  
**Cleanup:** encerrar sessões; manter MFA, contatos, budget e identidade diária

## 1. Resultado esperado

Ao terminar, você deverá ter:

- MFA ativo no root user;
- telefone, e-mail e contatos alternativos verificados;
- zero access keys no root;
- uma identidade administrativa diária que não seja o root;
- um budget mensal ou, enquanto o teto não for definido, um zero-spend budget;
- alertas de Free Tier habilitados, quando disponíveis;
- nenhuma senha, chave, token ou seed de MFA registrada neste projeto.

## 2. Preencha antes de começar

```text
TETO_MENSAL_USD: ainda não definido / USD ______
REGION_PADRÃO DOS LABS: ________________________
PLANO DA CONTA: Free / Paid / não sei
CONTA JÁ ESTÁ EM AWS ORGANIZATIONS: sim / não / não sei
IDENTIDADE DIÁRIA NÃO ROOT JÁ EXISTE: sim / não
```

### Alerta sobre Free account plan e IAM Identity Center

Para usar permission sets do IAM Identity Center no acesso à conta AWS, é
necessária uma **organization instance**. Uma account instance isolada não
oferece essa função.

Se a conta estiver no **Free account plan**, criar ou ingressar em AWS
Organizations a converte automaticamente para o plano pago e faz os créditos do
Free Tier expirarem imediatamente. Portanto, não habilite Organizations neste
laboratório sem confirmar o plano e aceitar conscientemente essa consequência.

Use a rota adequada:

- **Rota A — preferida:** IAM Identity Center, se a conta já estiver em uma
  Organization, já for Paid ou essa mudança tiver sido aprovada.
- **Rota B — transição segura:** IAM user administrativo com MFA, senha de
  console e nenhuma access key, se for necessário preservar o Free account plan.

## 3. Parte principal

### Etapa 1 — Proteger o root user

Entre como root somente para esta configuração inicial.

1. No menu da conta, abra **Account**.
2. Confirme o e-mail e o telefone do root. O telefone precisa estar acessível
   para recuperação.
3. Em **Alternate contacts**, confira ou preencha:
   - Billing;
   - Operations;
   - Security.
4. Em Billing, localize **IAM user and role access to Billing information** e
   ative o acesso IAM ao faturamento. Isso permite administrar custos sem usar o
   root.
5. Abra **Security credentials**.
6. Em **Multi-factor authentication (MFA)**, confirme que existe um dispositivo
   ativo. Se não existir, registre:
   - preferencialmente uma passkey ou security key resistente a phishing; ou
   - um aplicativo autenticador TOTP.
7. Se possível, registre um segundo dispositivo MFA como contingência.
8. Em **Access keys**, confirme que a quantidade é zero.

Se existir uma access key do root, não a copie e não mostre seu segredo. Antes de
desativá-la, verifique se algum sistema antigo depende dela. Depois substitua a
dependência, desative, valide e exclua a chave.

Validação:

- [ ] E-mail e telefone do root estão acessíveis.
- [ ] Contatos principal e alternativos estão corretos.
- [ ] MFA do root está ativo.
- [ ] Um segundo MFA foi registrado, se disponível.
- [ ] Root access keys = 0.
- [ ] Acesso IAM ao Billing está ativo.

Saia da sessão root assim que terminar.

### Etapa 2 — Garantir uma identidade diária não root

Se já existir uma identidade administrativa não root, entre com ela, confirme
MFA e pule para a etapa 3.

#### Rota A — IAM Identity Center

Execute somente depois de confirmar o impacto do plano da conta.

1. Habilite uma **organization instance** do IAM Identity Center.
2. Crie o usuário `saa-admin` e o grupo `SAA-Admins`.
3. Adicione o usuário ao grupo.
4. Selecione a conta em **AWS accounts**.
5. Atribua ao grupo um permission set administrativo para o bootstrap.
6. Ative o usuário pelo e-mail recebido, defina uma senha única e registre MFA.
7. Entre pelo AWS access portal e confirme que a identidade exibida não é root.

Depois do bootstrap, use um permission set mais restrito para laboratórios
cotidianos e reserve o administrativo para alterações de identidade ou
governança.

#### Rota B — IAM user transitório

Esta rota preserva uma conta Free de entrar em Organizations.

1. Como root, abra IAM e crie o grupo `SAA-Administrators`.
2. Anexe `AdministratorAccess` ao grupo para o bootstrap da conta.
3. Crie o IAM user `saa-admin` com acesso ao console.
4. Adicione o usuário ao grupo.
5. **Não crie access key.**
6. Saia do root e entre pelo endereço de login IAM como `saa-admin`.
7. Registre MFA para o novo usuário.
8. Confirme em **Security credentials** que suas access keys são zero.

`AdministratorAccess` é deliberadamente amplo e não representa least privilege.
Ele é usado aqui para substituir o root durante o bootstrap de uma conta de
estudo com um único administrador. Depois, separe uma identidade ou role mais
restrita para os laboratórios.

Validação:

- [ ] Login diário realizado sem root.
- [ ] MFA ativo na identidade diária.
- [ ] Access keys da identidade diária = 0.
- [ ] Nome/ARN da identidade foi conferido no menu do console.

### Etapa 3 — Criar proteção de custo

Execute como `saa-admin` ou pela identidade do IAM Identity Center.

1. Abra **Billing and Cost Management**.
2. Em **Billing preferences**, habilite **Receive AWS Free Tier usage alerts**,
   se a opção estiver disponível, e confira o e-mail.
3. Abra **Budgets** e escolha uma das opções:

   - se o teto já foi decidido: crie um **Cost budget**, mensal, recorrente,
     fixo, chamado `SAA-Labs-Monthly`;
   - se o teto ainda não foi decidido: use o template **Zero spend budget**,
     chamado `SAA-Labs-Zero-Spend`, e substitua-o quando o teto for escolhido.

4. Para o cost budget, use `TETO_MENSAL_USD` e monitore toda a conta.
5. Cadastre alertas por e-mail. Sugestão:
   - 25% actual;
   - 50% actual;
   - 80% actual;
   - 100% forecasted;
   - 100% actual.
6. Não crie neste laboratório SNS, Chatbot, budget action ou budget report.
7. Revise o endereço de e-mail e crie o budget.

Um budget **não é um bloqueio de gastos**. Os dados de cobrança e os alertas têm
atraso; custos podem ultrapassar o limite antes da notificação. Cleanup e
conferência de Bills continuam obrigatórios.

Validação:

- [ ] Budget mensal ou zero-spend criado.
- [ ] E-mail correto.
- [ ] Alertas configurados.
- [ ] Nenhuma ação automática ou relatório pago configurado.
- [ ] Free Tier usage alerts habilitados, se aplicável.

## 4. Extensão opcional — AWS CLI sem access key permanente

Não use uma sessão root nesta extensão.

### Opção A — IAM Identity Center

```powershell
aws --version
aws configure sso
aws sso login --profile saa-lab
aws configure list --profile saa-lab
aws sts get-caller-identity --profile saa-lab
```

O ARN esperado contém uma role/sessão do IAM Identity Center, nunca `:root`.

### Opção B — `aws login`

Esta opção requer AWS CLI 2.32.0 ou posterior. A identidade precisa da permissão
da AWS managed policy `SignInLocalDevelopmentAccess`; anexe-a ao grupo
`SAA-Administrators` ou à identidade apropriada.

```powershell
aws --version
aws login --profile saa-lab
aws configure list --profile saa-lab
aws sts get-caller-identity --profile saa-lab
```

No navegador, selecione `saa-admin`, nunca root.

Em `aws configure list`, o tipo de credencial deve aparecer como `login`. Se
aparecer `shared-credentials-file`, pare: o profile está encontrando credenciais
permanentes antigas. Não apague nada sem verificar; use um profile novo e
investigue a configuração anterior.

O comando `sts get-caller-identity` deve mostrar a conta e a identidade esperadas.
Não copie o account ID completo para o material de estudo.

## 5. Cleanup e evidências

Encerre a autenticação de CLI utilizada:

```powershell
# Se usou IAM Identity Center:
aws sso logout

# Se usou aws login:
aws logout --profile saa-lab
```

Depois:

- saia do console ou AWS access portal;
- confirme que não existe sessão root aberta;
- mantenha MFA, contatos, budget, alertas e identidade administrativa;
- confira **Bills** para garantir que nenhum serviço adicional foi criado.

Registre apenas:

```text
MFA root: ativo / pendente
Root access keys: 0 / investigar
Identidade diária: Identity Center / IAM user transitório
MFA identidade diária: ativo / pendente
Budget: SAA-Labs-Monthly / SAA-Labs-Zero-Spend
Teto mensal: pendente / USD ____
CLI credential type: sso / login / não executado
Cleanup concluído: sim / não
```

Nunca registre senha, código MFA, QR code/seed, telefone, endereço, access key,
secret key ou session token.

## 6. Conexão com o exame

- root é reservado a tarefas que exigem root;
- MFA fortalece autenticação, não concede autorização;
- pessoas devem preferir federação e credenciais temporárias;
- access keys permanentes são exceção;
- um budget alerta, mas não substitui controles e cleanup;
- a interface usada — console ou CLI — não altera as permissões avaliadas.

## 7. Referências oficiais

- [Root user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html)
- [MFA for the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-mfa-for-root.html)
- [IAM Identity Center instances](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html)
- [AWS account access with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html)
- [AWS Free Tier FAQs](https://aws.amazon.com/free/free-tier-faqs/)
- [Creating a cost budget](https://docs.aws.amazon.com/cost-management/latest/userguide/create-cost-budget.html)
- [AWS Budgets pricing](https://aws.amazon.com/aws-cost-management/aws-budgets/pricing/)
- [Billing alert preferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-pref.html)
- [AWS CLI with IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)
- [`aws login` with temporary credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)

**Referências verificadas em:** 24/07/2026.
