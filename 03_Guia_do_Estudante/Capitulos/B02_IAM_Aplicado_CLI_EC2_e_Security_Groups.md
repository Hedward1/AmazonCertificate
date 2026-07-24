# B02 — IAM aplicado, AWS CLI, EC2 e security groups

**Data planejada:** 27/07/2026  
**Nível:** iniciante absoluto  
**Aulas relacionadas:** 19–35  
**Domínios oficiais:** 1 — Design Secure Architectures; 3 — Design
High-Performing Architectures; 4 — Design Cost-Optimized Architectures  
**Tarefas principais:** 1.1 — Design secure access to AWS resources; 1.2 —
Design secure workloads and applications; 3.2 — Design high-performing and
elastic compute solutions  
**Tarefa secundária:** 4.2 — Design cost-optimized compute solutions  
**Pré-requisito:** [B01 — infraestrutura global, responsabilidade e
IAM](B01_Infraestrutura_Global_Responsabilidade_e_IAM.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá conseguir:

1. explicar por que console, CLI e SDK obedecem às mesmas policies;
2. autenticar a AWS CLI sem criar access key permanente;
3. identificar a conta e a identidade usadas por um profile da CLI;
4. diferenciar trust policy, permissions policy, role e instance profile;
5. escolher a ferramenta correta para auditar credenciais ou permissões não
   utilizadas;
6. explicar os componentes necessários para lançar uma instância EC2;
7. descrever o comportamento padrão de EC2 user data;
8. escolher uma família de instância pelo requisito dominante;
9. construir uma regra de security group com protocolo, porta e origem;
10. explicar por que security groups são stateful e contêm somente regras de
    permissão.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 19 — CLI no Windows | estudar e executar |
| 20–21 — CLI no macOS/Linux | acelerar; os conceitos são os mesmos |
| 22 — CLI hands-on | executar com credenciais temporárias |
| 23–24 — AWS CloudShell | pular para a prova; opcional como ferramenta |
| 25–30 — roles e IAM security tools | estudar integralmente |
| 31 — AWS Budget | revisar a proteção criada no LAB B01 |
| 32–35 — EC2, user data, tipos e security groups | estudar integralmente |

O guia oficial lista AWS CloudShell como fora do escopo. Isso não significa que
o serviço seja inútil; significa apenas que não deve consumir tempo de
memorização para o SAA-C03.

### Atualizações importantes em 2026

- **Amazon Linux 2 encerrou o suporte em 30/06/2026.** Os novos laboratórios
  deste projeto usarão Amazon Linux 2023 e `dnf`.
- Não memorize `t2.micro` como “a instância gratuita”. A elegibilidade varia com
  a data, o plano e os créditos da conta; no console, escolha somente um tipo
  marcado **Free tier eligible** e compatível com a AMI.
- Endereços IPv4 públicos têm cobrança na tabela vigente. O laboratório B03
  minimizará o tempo em execução e não criará Elastic IP.
- A recomendação atual não é manter access keys permanentes e rotacioná-las por
  calendário como primeira opção; é evitá-las e usar credenciais temporárias.

## 3. Visão geral do bloco

```text
pessoa no Windows
    │
    ├── console
    └── AWS CLI ── credencial temporária ──┐
                                           ▼
                                      APIs da AWS
                                           │
                                  IAM avalia a solicitação
                                           │
                                           ▼
EC2: AMI + instance type + storage + rede + security group + role + user data
```

Console e CLI são interfaces. IAM decide se a ação é autorizada. EC2 é o recurso
de computação que começaremos a configurar.

## 4. AWS CLI com credenciais temporárias

### 4.1 O que é a CLI

A **AWS Command Line Interface** transforma comandos de terminal em chamadas às
APIs da AWS. Uma policy que permite ou nega uma ação produz o mesmo resultado,
independentemente de a chamada vir do console, da CLI ou de um SDK.

Exemplos:

```powershell
aws --version
aws sts get-caller-identity --profile saa-lab
aws configure list --profile saa-lab
```

- `aws --version` confirma a instalação.
- `sts get-caller-identity` informa account, user ID e ARN da identidade usada.
- `aws configure list` mostra o profile, a Region e de onde vieram as
  credenciais.

`get-caller-identity` não concede permissão nem troca a identidade. Ele apenas
responde: “quem está fazendo esta chamada?”.

### 4.2 Instalação no Windows

A documentação oficial oferece dois instaladores MSI de 64 bits:

- para todos os usuários, com privilégio administrativo;
- somente para o usuário atual, sem exigir privilégio administrativo.

Depois da instalação ou atualização, feche e reabra o PowerShell se `aws` não for
encontrado no `PATH`.

### 4.3 Métodos de autenticação

| Situação | Método preferido | Comando inicial |
|---|---|---|
| IAM Identity Center | sessão SSO temporária | `aws configure sso` |
| identidade IAM com console, CLI 2.32+ | login temporário pelo navegador | `aws login --profile saa-lab` |
| workload em EC2 | IAM role/instance profile | automático |
| sistema legado sem alternativa | access key de IAM user | último recurso |
| root user | nenhum uso diário | nunca criar access key |

Para `aws login`, a identidade precisa da permissão
`SignInLocalDevelopmentAccess`. A sessão do navegador gera credenciais
temporárias; não use root só porque o comando tecnicamente aceita essa
identidade.

### 4.4 Profiles e Region

Um **named profile** evita misturar contas e identidades:

```powershell
aws sts get-caller-identity --profile saa-lab
aws ec2 describe-regions --profile saa-lab --region us-east-1
```

O parâmetro `--profile` escolhe as credenciais. O parâmetro `--region` escolhe o
endpoint regional para aquela chamada. Trocar a Region não troca a conta nem a
identidade.

Antes de um comando que altere recursos, confirme sempre:

1. account;
2. ARN da identidade;
3. Region;
4. ação e recursos afetados.

### 4.5 Diagnóstico de credenciais

```text
aws configure list --profile saa-lab
```

Se o tipo esperado for `login` ou `sso` mas aparecer
`shared-credentials-file`, há outra fonte de credenciais com precedência. Não
apague o arquivo às cegas: use um profile novo e investigue a configuração.

Nunca copie para o material:

- access key ID;
- secret access key;
- session token;
- URL de autenticação temporária;
- código MFA.

## 5. IAM roles para serviços AWS

### 5.1 As duas policies de uma role

Uma role resolve duas perguntas:

```text
Trust policy                         Permissions policy
Quem pode assumir?                   O que a sessão pode fazer?

EC2 service principal ──assume──> role ──temporário──> ação no recurso
```

- **Trust policy:** identifica principals autorizados a assumir a role.
- **Permissions policy:** define `Action`, `Resource`, `Effect` e condições da
  sessão.

Uma trust policy que permite `ec2.amazonaws.com` não dá acesso ao S3 por si só.
A permissions policy deve conceder as operações de S3 necessárias.

### 5.2 Role de EC2 e instance profile

Uma aplicação executada em EC2 não deve receber access keys gravadas em código,
user data, AMI ou arquivo de configuração.

O fluxo correto é:

1. criar uma IAM role;
2. permitir que o serviço EC2 assuma a role;
3. anexar uma permissions policy com least privilege;
4. colocar a role em um **instance profile**;
5. anexar o instance profile à instância;
6. deixar a CLI ou o SDK obter credenciais temporárias automaticamente.

No console, a criação da role para EC2 normalmente cria o instance profile. Pela
CLI/API, role e instance profile podem exigir ações separadas. Um instance
profile contém uma role, e uma instância EC2 usa uma role por vez.

### 5.3 `iam:PassRole` não é `sts:AssumeRole`

Uma pessoa que lança uma instância e associa uma role precisa poder **passar** a
role ao serviço EC2. Isso usa `iam:PassRole`.

- `sts:AssumeRole`: o principal passa a operar como a role.
- `iam:PassRole`: o principal autoriza um serviço a receber aquela role.

Armadilha: conceder `iam:PassRole` sobre qualquer role pode permitir elevação de
privilégio. Restrinja quais roles podem ser passadas e para quais serviços.

### Cenário resolvido 1 — Website em EC2 lê um bucket

1. **Cenário:** o código do website precisa ler objetos privados de um bucket.
2. **Requisito:** não armazenar credenciais permanentes.
3. **Solução:** role de EC2 em um instance profile, com somente
   `s3:GetObject` nos objetos necessários.
4. **Trust policy:** permite que EC2 assuma a role.
5. **Permissions policy:** permite a leitura do bucket.
6. **Por que não IAM user:** criaria segredo de longo prazo para distribuir e
   rotacionar.
7. **Variação:** se o código precisar gravar em um único prefixo, adicione somente
   a ação e o ARN desse prefixo.

## 6. IAM security tools

### 6.1 Credential report

O **IAM credential report** é um CSV de toda a conta que mostra informações de
credenciais do root e dos IAM users, como:

- senha habilitada e último uso;
- MFA ativo;
- access keys ativas, rotação e último uso;
- certificados de assinatura gerenciados pelo IAM.

Ele não é uma lista de permissions policies nem um inventário de roles. Roles
usam credenciais temporárias e não aparecem como IAM users com access keys
permanentes.

O relatório pode ser gerado no máximo uma vez a cada quatro horas; uma nova
solicitação nesse intervalo recupera o relatório mais recente.

### 6.2 Last accessed information

A informação **last accessed** ajuda a localizar serviços e ações permitidos que
uma identidade ou policy não utiliza. Ela serve para refinar permissões em
direção a least privilege.

Cuidados:

- registra tentativas, inclusive algumas negadas, não apenas sucessos;
- pode levar tempo para aparecer;
- tem cobertura e períodos de retenção específicos;
- CloudTrail é a fonte autoritativa para investigar chamadas e seu resultado.

Ausência de atividade não prova, sozinha, que uma permissão pode ser removida.
Confirme o caso de uso e outras evidências antes da alteração.

### 6.3 IAM Access Analyzer

Use o IAM Access Analyzer para:

- identificar acesso externo ou público a recursos compatíveis;
- encontrar acesso não utilizado, conforme o analyzer configurado;
- validar policies;
- ajudar a gerar policies baseadas em atividade.

Ele complementa o credential report. Um analisa acesso e policies; o outro
resume credenciais duradouras da conta.

### 6.4 Tabela de escolha

| Pergunta | Ferramenta |
|---|---|
| Quais IAM users não têm MFA? | credential report |
| Existe access key antiga ou sem uso? | credential report |
| Quais serviços permitidos esta role não usa? | last accessed |
| Um bucket ou uma role permite acesso externo? | IAM Access Analyzer |
| Qual API foi chamada e foi aceita ou negada? | AWS CloudTrail |

## 7. IAM best practices consolidadas

1. Proteger e quase nunca usar root.
2. Preferir federação e credenciais temporárias para pessoas.
3. Usar roles e credenciais temporárias para workloads.
4. Exigir MFA.
5. Aplicar least privilege.
6. Não colocar secrets em código, AMIs, user data ou repositórios.
7. Revisar e remover identidades, policies e credenciais não utilizadas.
8. Usar conditions para restringir quando e de onde uma ação pode ocorrer.
9. Validar acesso público e cross-account.
10. Monitorar as ações com CloudTrail e ferramentas de auditoria.

## 8. AWS Budgets: proteção, não trava

O LAB B01 criou um cost budget ou zero-spend budget. Revise a regra:

- alerta **actual** usa custo já registrado;
- alerta **forecasted** usa a previsão de custo;
- dados de cobrança e alertas não são instantâneos;
- um budget comum não encerra recursos nem impede automaticamente novos gastos;
- budget actions existem, mas exigem planejamento e não fazem parte deste bloco.

Em uma questão, “notificar quando o custo se aproximar do limite” aponta para AWS
Budgets. “Investigar detalhadamente o que já foi gasto” pode apontar para Cost
Explorer ou relatórios, conforme o requisito.

## 9. Amazon EC2: o servidor virtual

Uma **EC2 instance** é um servidor virtual. Você escolhe e administra o sistema
operacional convidado, instala aplicações e configura a segurança do workload.

### 9.1 Componentes do lançamento

```text
AMI                    sistema e imagem de boot
Instance type          CPU, memória, rede e características de hardware
Subnet/AZ              posicionamento de rede e domínio de falha
Security group         tráfego permitido
Storage                root volume e volumes de dados
IAM role               acesso temporário a APIs da AWS
User data              automação inicial
```

### 9.2 AMI

Uma **Amazon Machine Image** fornece o software necessário para inicializar a
instância. A AMI está ligada a:

- Region;
- sistema operacional;
- arquitetura do processador;
- tipo de root volume;
- modo de virtualização.

Uma AMI não é uma instância em execução. É um molde que pode lançar várias
instâncias. Para utilizá-la em outra Region, ela precisa estar disponível ou ser
copiada para essa Region.

### 9.3 Root volume

Toda instância possui um root volume com a imagem usada no boot. Na maioria dos
casos de estudo modernos, ele é um volume Amazon EBS.

Parar uma instância EBS-backed normalmente interrompe a cobrança de compute, mas
o volume EBS continua existindo e pode continuar cobrando armazenamento.

### 9.4 User data

**EC2 user data** permite executar script ou configuração automática quando a
instância é lançada.

Comportamento básico:

- no Linux, pode usar shell script ou cloud-init;
- por padrão, o script normalmente roda somente no primeiro boot;
- em Linux, normalmente executa com privilégio de root e não é interativo;
- a execução adiciona tempo à inicialização;
- o conteúdo bruto tem limite e é tratado como dado a ser interpretado pela
  instância;
- user data não é incorporado automaticamente a uma AMI criada depois.

User data não é um cofre. Não coloque senha, access key ou secret nele.
Alterar o atributo enquanto a instância está parada não faz o script executar
automaticamente no próximo start. Em Amazon Linux, a saída pode ser investigada
em `/var/log/cloud-init-output.log`.

Exemplo conceitual para Amazon Linux 2023:

```bash
#!/bin/bash
dnf install -y httpd
systemctl enable --now httpd
echo "SAA lab" > /var/www/html/index.html
```

O script instala e inicia um servidor web. Para acessá-lo, a instância ainda
precisa de rede e de uma regra de security group para HTTP.

### 9.5 Estados e custos

| Estado | Significado básico | Cobrança de compute |
|---|---|---|
| `pending` | preparando para executar | não |
| `running` | em execução | sim |
| `stopping` | preparando para parar | normalmente não |
| `stopped` | desligada, pode iniciar novamente | não |
| `shutting-down` | preparando para terminar | não |
| `terminated` | excluída, não pode reiniciar | não |

Mesmo em `stopped`, outros componentes podem cobrar: EBS, snapshots, endereços
IPv4 públicos e outros recursos, conforme a configuração e a oferta vigente.
**Stop não é cleanup completo.**

`Terminate` é irreversível para a instância. O root EBS volume costuma ser
excluído por padrão na terminação, mas volumes e outros recursos podem ser
preservados conforme seus atributos.

## 10. Instance types

O instance type define a combinação de compute, memória, armazenamento e rede.

### 10.1 Famílias principais

| Necessidade dominante | Categoria | Famílias para reconhecer |
|---|---|---|
| equilíbrio geral | general purpose | T, M |
| CPU | compute optimized | C |
| grandes dados em memória | memory optimized | R, X |
| I/O local intenso | storage optimized | I, D |
| GPU/acelerador | accelerated computing | G, P, Inf, Trn |

- T oferece desempenho de CPU com baseline e capacidade de burst.
- M é equilibrada.
- C prioriza compute.
- R prioriza memória.

Famílias T usam CPU credits. Manter CPU acima da baseline em modo Unlimited pode
gerar cobrança adicional; por isso, T não é resposta automática para carga de
CPU sustentada.

Não escolha pela letra isoladamente; primeiro identifique a restrição do
workload.

### 10.2 Como ler um nome

Exemplo: `c7gn.xlarge`

- `c`: série compute optimized;
- `7`: geração;
- `g` e `n`: opções de processador/rede;
- `xlarge`: tamanho dentro da família.

Uma geração mais nova normalmente oferece melhorias, mas a arquitetura do
processador precisa ser compatível com a AMI e a aplicação.

### Cenário resolvido 2 — Família de instância

1. **Cenário:** aplicação faz cálculos intensivos, mantém pouco estado em memória
   e precisa de alto desempenho de CPU.
2. **Palavras decisivas:** *compute-intensive*, *high-performance processors*.
3. **Escolha:** família compute optimized, como C.
4. **Por que não R:** R prioriza memória, que não é a restrição.
5. **Variação:** se o requisito principal for processar grande conjunto em
   memória, a resposta muda para memory optimized.

## 11. Security groups

Um **security group** funciona como firewall virtual dos recursos associados.
Para EC2, controla tráfego de entrada e saída das interfaces da instância.

### 11.1 Regras fundamentais

- contém somente regras `Allow`, não regras `Deny`;
- um novo security group não tem inbound rules;
- por padrão, costuma ter uma outbound rule permitindo todo o tráfego;
- todas as regras dos security groups associados são agregadas;
- uma alteração é aplicada aos recursos associados;
- é **stateful**.

O **default security group** é um caso específico: sua configuração inicial
também permite inbound proveniente de recursos associados ao próprio default
security group.

Stateful significa:

> se uma solicitação é permitida em uma direção, o tráfego de resposta é
> permitido automaticamente, sem exigir uma regra simétrica.

Isso não significa que uma nova conexão independente seja liberada.

### 11.2 Anatomia de uma regra

Uma inbound rule define:

```text
protocol + port/range + source
```

Uma outbound rule define:

```text
protocol + port/range + destination
```

Fontes/destinos podem ser um IP/CIDR, prefix list ou outro security group, entre
as opções compatíveis.

### 11.3 Portas para reconhecer

| Porta | Protocolo/uso comum | Regra segura |
|---:|---|---|
| 22 | SSH/SFTP | restringir ao IP administrativo necessário |
| 80 | HTTP | pode ser público para website HTTP |
| 443 | HTTPS | pode ser público para website HTTPS |
| 3389 | RDP | restringir ao IP administrativo necessário |
| 3306 | MySQL/Aurora MySQL | permitir apenas da camada de aplicação |
| 5432 | PostgreSQL/Aurora PostgreSQL | permitir apenas da camada de aplicação |

`0.0.0.0/0` significa qualquer endereço IPv4. É plausível para HTTP/HTTPS de um
site público; é perigoso para SSH, RDP ou banco de dados.

### 11.4 Referenciar outro security group

Em uma arquitetura em camadas:

```text
Internet
   │ 443
   ▼
[SG do load balancer]
   │ porta da aplicação; source = SG do load balancer
   ▼
[SG da aplicação]
   │ 3306; source = SG da aplicação
   ▼
[SG do banco]
```

A referência não copia as regras do SG de origem. Ela permite tráfego proveniente
das interfaces associadas ao SG referenciado, no protocolo e na porta definidos.
Essa comunicação usa os endereços privados e ainda depende de rotas, NACLs e
firewalls do sistema operacional compatíveis.

### Cenário resolvido 3 — Website público administrado por SSH

1. **Requisito público:** qualquer usuário precisa acessar HTTPS.
2. **Requisito administrativo:** somente seu computador deve usar SSH.
3. **Inbound rules:**
   - TCP 443 de `0.0.0.0/0` para o público IPv4;
   - TCP 22 de `SEU_IP/32`.
4. **Não fazer:** TCP 22 de `0.0.0.0/0`.
5. **Stateful:** as respostas das conexões permitidas retornam automaticamente.
6. **Variação:** se não houver necessidade de SSH, não abra a porta 22.

## 12. Não confunda IAM com security group

| Pergunta | Controle |
|---|---|
| A identidade pode chamar `ec2:RunInstances`? | IAM policy |
| O navegador pode alcançar TCP 443 na instância? | security group |
| EC2 pode assumir a role? | trust policy |
| A role pode ler o bucket? | permissions policy |
| Qual software inicia no primeiro boot? | user data |

IAM controla chamadas às APIs. Security groups controlam tráfego de rede.

## 13. Tabela de decisão

| Requisito | Escolha | Motivo |
|---|---|---|
| usar CLI como pessoa | SSO ou `aws login` | credencial temporária |
| saber qual identidade a CLI usa | `sts get-caller-identity` | mostra account e ARN |
| aplicação EC2 chama S3 | IAM role + instance profile | sem secret permanente |
| auditar MFA e access keys de users | credential report | visão de credenciais da conta |
| reduzir permissões não utilizadas | last accessed/Access Analyzer | evidência de uso |
| automatizar configuração inicial EC2 | user data | bootstrap no lançamento |
| workload equilibrado | general purpose | equilíbrio de recursos |
| workload CPU-intensive | compute optimized | processador |
| website público | 80/443 do público | tráfego da aplicação |
| administração SSH | 22 somente do IP necessário | reduz exposição |
| negar um IP em security group | não é possível diretamente | SG só possui Allow |

## 14. Armadilhas de prova

1. `aws configure` não concede permissões.
2. Trocar console por CLI não contorna um `Deny`.
3. Trocar `--region` não troca account.
4. Role não guarda access keys permanentes.
5. Trust policy não substitui permissions policy.
6. `iam:PassRole` não é `sts:AssumeRole`.
7. Credential report não é relatório de todas as chamadas API.
8. Last accessed pode incluir tentativas negadas; CloudTrail mostra o evento.
9. Budget alerta; não é hard spending cap.
10. AMI é imagem; EC2 instance é servidor em execução.
11. AMI e instance type precisam ser compatíveis.
12. User data normalmente roda uma vez no primeiro boot.
13. User data não deve conter secrets.
14. Instância `stopped` pode continuar gerando custos externos ao compute.
15. `Terminate` não equivale a excluir automaticamente todos os recursos
    relacionados.
16. Security group só possui regras de permissão.
17. Security groups são stateful.
18. Não é necessário criar regra de retorno para uma conexão permitida.
19. Vários security groups agregam regras; não existe “Deny” em um deles para
    cancelar o `Allow` de outro.
20. `0.0.0.0/0` em SSH/RDP é exposição ampla, não facilidade aceitável.

## 15. Custos e cleanup

- IAM roles e security groups não têm cobrança adicional.
- Uma EC2 instance começa a cobrar compute quando entra em `running`.
- Parar interrompe o compute, mas não necessariamente EBS, snapshots, IPv4 ou
  outros recursos.
- Um IPv4 público é um item cobrado na tabela vigente, sujeito aos créditos e às
  ofertas aplicáveis à conta.
- Uma AMI personalizada pode manter snapshots que geram armazenamento.
- User data pode instalar software ou criar recursos que tenham custos próprios.
- O LAB B02 não lança EC2; o primeiro lançamento e cleanup ocorrerão no B03.

Sempre confirme a Region e confira **EC2 Global View**, **Volumes**, **Elastic
IPs** e **Bills** após laboratórios com recursos.

## 16. Checklist de domínio

- [ ] Consigo autenticar a CLI sem access key permanente.
- [ ] Confiro account, ARN, profile e Region antes de alterar recursos.
- [ ] Explico trust policy, permissions policy e instance profile.
- [ ] Escolho credential report versus last accessed.
- [ ] Desenho os componentes de uma instância EC2.
- [ ] Sei quando user data roda por padrão.
- [ ] Escolho M/T, C, R ou I pelo requisito dominante.
- [ ] Explico por que security groups são stateful.
- [ ] Escrevo regras seguras para 22, 80, 443 e 3389.
- [ ] Sei por que stopped não significa custo zero.

## 17. Recuperação ativa

Responda sem consultar:

1. Console e CLI recebem permissões diferentes?
2. Qual comando revela a identidade atual da CLI?
3. Qual é a diferença entre `--profile` e `--region`?
4. O que a trust policy de uma role controla?
5. Para que serve um instance profile?
6. Quem precisa de `iam:PassRole`?
7. Qual relatório mostra IAM users sem MFA?
8. Por que last accessed não substitui CloudTrail?
9. Quais sete componentes aparecem no lançamento de EC2?
10. User data roda em todo reboot por padrão?
11. Qual família atende CPU intensa? E memória intensa?
12. O que existe em um novo security group?
13. Por que não é necessária uma regra de retorno?
14. Qual a diferença entre parar e terminar uma instância?

## 18. Ligações deste bloco

- [Laboratório B02](../../05_Laboratorios/LAB_B02_CLI_Roles_e_Auditoria_IAM.md)
- [Questões B02](../../04_Questoes_e_Revisoes/Blocos/B02_Questoes.md)
- [Gabarito B02](../../04_Questoes_e_Revisoes/Blocos/B02_Gabarito.md)
- [Revisões B02](../../06_Progresso/B02_Checklist_e_Revisoes.md)

## 19. Referências oficiais

- [Install or update AWS CLI on Windows](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [AWS CLI authentication options](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)
- [`aws login` with console credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)
- [IAM Identity Center authentication for CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)
- [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)
- [IAM credential report](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)
- [Last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html)
- [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Managing costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html)
- [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [EC2 user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
- [EC2 instance lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html)
- [EC2 instance type categories](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-type-specifications.html)
- [Amazon Linux 2 end of support](https://aws.amazon.com/amazon-linux-2/)
- [EC2 Free Tier eligibility](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-free-tier-usage.html)
- [Amazon VPC pricing for public IPv4](https://aws.amazon.com/vpc/pricing/)
- [Security group basics](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
- [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)

**Referências verificadas em:** 24/07/2026.
