# B21 — Organizations, IAM avançado, KMS e Parameter Store

**Data planejada:** 18/08/2026<br>
**Nível:** iniciante absoluto<br>
**Comece pelas aulas da Udemy:** [roteiro B21 — aulas 283–300](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b21); Nenhuma aula é pulada.<br>
**Quizzes:** Q22<br>
**Domínios oficiais:** 1 — Design Secure Architectures<br>
**Tarefas:** 1.1 e 1.3 principais; 1.2 secundária<br>
**Pré-requisito:** B20 — observabilidade e auditoria

## 1. Objetivos de aprendizagem

1. Explicar hierarchy de Organizations.
2. Aplicar SCP como limite.
3. Resolver policy evaluation.
4. Distinguir políticas IAM.
5. Projetar cross-account role.
6. Escolher IAM Identity Center.
7. Reconhecer Directory Service e Control Tower.
8. Explicar envelope encryption.
9. Comparar tipos de KMS key.
10. Escolher Parameter Store pelo requisito.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 283–291 | Organizations, policies, Identity Center, Directory Service e Control Tower |
| 292–298 | Criptografia, KMS, multi-Region, S3 e AMI criptografada |
| 299–300 | Parameter Store; prática de leitura |
| Q22 | Fazer depois das questões autorais |

Use as aulas para o primeiro mapa, este capítulo para consolidar decisões, o laboratório para praticar e as questões para diagnosticar lacunas.

## 3. Vocabulário essencial

| Termo | Significado no cenário |
|---|---|
| SCP | guardrail de permissão |
| OU | agrupamento de contas |
| explicit deny | negação que prevalece |
| permissions boundary | máximo para identidade |
| trust policy | quem assume uma role |
| federation | identidade externa com credenciais temporárias |
| data key | chave que cifra dados |
| KMS key | chave que protege data keys |
| grant | permissão KMS delegada |
| SecureString | parâmetro cifrado com KMS |

## 4. Modelo mental

Para cada cenário, siga esta sequência:

1. identifique o requisito principal;
2. marque restrições e superlativos;
3. determine escopo regional, zonal ou global;
4. avalie segurança e resiliência;
5. avalie performance e escala;
6. compare operação e custo;
7. elimine opções que violam uma restrição;
8. escolha serviço e configuração.

## 5. Fundamentos e decisões

### 5.1 Ponto 1

Management account administra a organização.
### 5.2 Ponto 2

Workloads devem preferencialmente ficar em member accounts.
### 5.3 Ponto 3

OUs agrupam contas e herdam controles.
### 5.4 Ponto 4

SCP limita o máximo de permissões.
### 5.5 Ponto 5

SCP não concede permissão.
### 5.6 Ponto 6

SCP afeta principals em member accounts.
### 5.7 Ponto 7

SCP não afeta users e roles do management account.
### 5.8 Ponto 8

SCP não restringe service-linked roles.
### 5.9 Ponto 9

Explicit Deny aplicável vence Allow.
### 5.10 Ponto 10

Implicit deny é o padrão.
### 5.11 Ponto 11

Identity-based policy é anexada a identidade.
### 5.12 Ponto 12

Resource-based policy é anexada a recurso e contém Principal.
### 5.13 Ponto 13

Trust policy controla quem assume role.
### 5.14 Ponto 14

Permissions policy da role controla o que a sessão faz.
### 5.15 Ponto 15

Permissions boundary limita o máximo da identidade.
### 5.16 Ponto 16

Session policy também pode limitar a sessão.
### 5.17 Ponto 17

Cross-account role exige confiança e permissão de assume role.
### 5.18 Ponto 18

Credenciais temporárias são preferíveis a access keys duradouras.
### 5.19 Ponto 19

IAM Identity Center atende workforce multi-account.
### 5.20 Ponto 20

Permission sets viram acesso nas contas atribuídas.
### 5.21 Ponto 21

Directory Service atende casos Microsoft AD.
### 5.22 Ponto 22

Control Tower cria e governa landing zone.
### 5.23 Ponto 23

Tag policy não concede ou nega ações IAM.
### 5.24 Ponto 24

Envelope encryption usa data key para os dados.
### 5.25 Ponto 25

KMS key protege a data key.
### 5.26 Ponto 26

AWS owned key não é visível nem controlada pelo cliente.
### 5.27 Ponto 27

AWS managed key é criada para integração do serviço.
### 5.28 Ponto 28

Customer managed key dá controle de policy e lifecycle e cobra.
### 5.29 Ponto 29

Multi-Region keys compartilham key ID e material relacionado.
### 5.30 Ponto 30

Policies, aliases, grants e estado não são sincronizados entre réplicas.
### 5.31 Ponto 31

Replicar KMS key não replica dados.
### 5.32 Ponto 32

Parameter Store guarda configuração hierárquica.
### 5.33 Ponto 33

SecureString usa KMS.
### 5.34 Ponto 34

Secrets Manager é melhor quando rotação gerenciada é requisito.

### Cápsula de decisão — AWS Resource Access Manager (AWS RAM)

- **Problema resolvido:** compartilhar tipos de recurso suportados com contas,
  OUs, a organização ou principals compatíveis sem criar cópias em cada conta.
- **Relação SAA-C03:** tarefa 1.1 — acesso seguro entre contas; também pode
  reduzir duplicação operacional e custo quando o recurso é compartilhável.
- **Quando escolher:** uma conta central possui, por exemplo, uma subnet ou
  outro recurso suportado que workloads de contas consumidoras devem usar.
- **Quando não escolher:** o tipo de recurso não é compartilhável, é necessário
  apenas conceder ações sobre dados, ou uma role/resource policy cross-account
  atende de forma mais direta.
- **Serviço semelhante:** cross-account IAM role/resource-based policy concede
  ações; RAM cria uma resource share com permissões próprias do tipo suportado.
- **Armadilha:** compartilhar não transfere ownership. Região, RAM permission,
  IAM, SCPs, quotas e cobranças do serviço continuam aplicáveis; fora da
  organização pode haver convite a aceitar.
- **Questão situacional extra (fora do banco de 250):** várias contas devem lançar recursos em subnets
  administradas por uma conta de rede, sem duplicar VPCs. **Resposta curta:**
  compartilhe as subnets suportadas via AWS RAM e conceda IAM mínimo nas contas
  consumidoras.
- **Referência oficial:** [What is AWS RAM?](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html).

## 6. Tabela de decisão

| Requisito dominante | Escolha inicial | Motivo |
|---|---|---|
| Limitar member account | SCP | guardrail |
| Conceder ação a role | Identity policy | allow aplicável |
| Permitir acesso a bucket | Resource policy | principal no recurso |
| Quem assume role | Trust policy | relação de confiança |
| Máximo para role | Permissions boundary | limite |
| Workforce em contas | IAM Identity Center | SSO e credenciais temporárias |
| Microsoft AD gerenciado | Directory Service | integração de diretório |
| Landing zone | Control Tower | governança multi-account |
| Compartilhar recurso suportado entre contas | AWS RAM | resource share sem mudar ownership |
| Criptografia controlada | Customer managed KMS key | policy e auditoria |
| Configuração hierárquica | Parameter Store | parâmetros centralizados |

## 7. Cenários resolvidos


### Cenário resolvido 1 — Admin bloqueado

- **Contexto:** Role tem AdministratorAccess.
- **Requisito:** Terminar instância, mas SCP nega a ação.
- **Decisão:** A chamada permanece negada.
- **Por quê:** SCP limita o máximo e Deny prevalece.
- **Por que não:** Adicionar outro Allow não remove explicit Deny.
- **Trade-off:** Guardrails reduzem blast radius, mas exigem teste.
- **Validação:** Simular em OU de teste antes do root.
- **Custo/cleanup:** Policies não têm custo direto.
- **Variação:** Management account não é afetada pelo SCP.

### Cenário resolvido 2 — Cross-account

- **Contexto:** Pipeline da conta A precisa ler recurso na B.
- **Requisito:** Sem access key compartilhada.
- **Decisão:** Role na B com trust restrita e permissions mínimas.
- **Por quê:** STS fornece sessão temporária.
- **Por que não:** Uma identity policy isolada não cria confiança no destino.
- **Trade-off:** Duas camadas precisam estar corretas.
- **Validação:** Testar principal, action, resource e conditions.
- **Custo/cleanup:** Sem chave permanente para armazenar.
- **Variação:** Resource policy direta pode atender serviços compatíveis.

### Cenário resolvido 3 — Criptografia global

- **Contexto:** Ciphertext precisa ser decifrado localmente em duas Regions.
- **Requisito:** Mesma identidade/material de chave sem chamada cross-Region.
- **Decisão:** Primary e replica multi-Region KMS keys.
- **Por quê:** Related keys interoperam criptograficamente.
- **Por que não:** Copiar alias não copia material.
- **Trade-off:** Cada key mantém policy, estado e custo.
- **Validação:** Testar encrypt/decrypt e replicação de dados separadamente.
- **Custo/cleanup:** Cobrança por cada customer managed key e requests.
- **Variação:** Use single-Region quando não há requisito explícito.

## 8. Fluxo de projeto

1. Autenticar o principal.
2. Começar em implicit deny.
3. Encontrar Allow aplicável.
4. Avaliar resource policy.
5. Aplicar SCP.
6. Aplicar permissions boundary.
7. Aplicar session policy.
8. Verificar explicit Deny.
9. Verificar trust policy em assume role.
10. Verificar key policy para KMS.
11. Usar Policy Simulator quando compatível.
12. Registrar decisão e condição decisiva.

## 9. Custos e cleanup

- Não criar customer managed KMS key para treino.
- Customer managed key cobra por mês e requests.
- Não criar Organization em conta pessoal sem planejamento.
- Directory Service e Control Tower podem gerar recursos pagos.
- Advanced parameters podem cobrar.
- Maior throughput de Parameter Store pode cobrar.
- Exclusão de KMS key é destrutiva e não é cleanup aceitável.
- Auditar aliases não prova ausência de chaves.

Faça inventário antes e depois. Exclua somente recursos criados por você e identificados pelo bloco. Nunca tente zerar a conta removendo recursos preexistentes.

## 10. Armadilhas de prova

- SCP não concede.
- Allow não vence Deny.
- Tag policy não autoriza.
- Identity Center não é Microsoft AD.
- Trust e permissions policies têm funções diferentes.
- KMS key não cifra payload grande diretamente no padrão envelope.
- Multi-Region key não replica dados.
- Key policies não sincronizam entre réplicas.
- SecureString depende de KMS.
- Nome, tag e descrição não devem conter segredo.

## 11. Checklist de domínio

- [ ] Consigo explicar os objetivos sem consultar.
- [ ] Reconstruo a tabela de decisão.
- [ ] Resolvo os três cenários.
- [ ] Sei justificar duas alternativas erradas.
- [ ] Conheço custos residuais.
- [ ] Completei o laboratório.
- [ ] Respondi às dez questões antes do gabarito.
- [ ] Registrei erros e baixa confiança.
- [ ] Agendei D+2 e D+7.

## 12. Recuperação ativa

1. Desenhe hierarquia Organizations.
2. Explique Administrator bloqueado.
3. Compare cinco tipos de policy.
4. Explique cross-account role.
5. Compare Identity Center e Directory Service.
6. Explique Control Tower.
7. Desenhe envelope encryption.
8. Compare três tipos de KMS key.
9. Liste propriedades não sincronizadas em multi-Region.
10. Compare Parameter Store e Secrets Manager.

## 13. Ligações com outros blocos

- A identidade limita quem inicia a operação.
- A rede limita por onde o dado passa.
- A criptografia protege conteúdo e chaves.
- A observabilidade prova comportamento e mudanças.
- Resiliência deve corresponder ao objetivo do negócio.
- Custo deve incluir recursos ociosos e tráfego.
- Operação gerenciada reduz tarefas, mas não remove responsabilidade.
- Os simulados combinam estes conceitos.

## 14. Referências oficiais AWS

- [SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [Policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [Identity versus resource policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html)
- [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
- [Compartilhamento de recursos com AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html)
- [KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
- [Multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html)
- [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

**Referências verificadas em:** 01/08/2026.

## 15. Continue o bloco

- [Laboratório B21](../../05_Laboratorios/LAB_B21_Avaliacao_de_Politicas_KMS_e_Parameter_Store.md)
- [Questões B21](../../04_Questoes_e_Revisoes/Blocos/B21_Questoes.md)
- [Gabarito B21](../../04_Questoes_e_Revisoes/Blocos/B21_Gabarito.md)
- [Checklist e revisões B21](../../06_Progresso/B21_Checklist_e_Revisoes.md)
