# B02 — Gabarito comentado

Abra este arquivo somente depois de responder e registrar a confiança em todas
as [questões B02](B02_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B02-01 | B | 1.1 |
| B02-02 | C | 1.2 |
| B02-03 | A | 1.1 |
| B02-04 | D | 1.1 |
| B02-05 | B | 4.2 |
| B02-06 | C | 3.2 |
| B02-07 | A | 3.2 |
| B02-08 | D | 1.2 |
| B02-09 | B | 1.2 |
| B02-10 | C | 3.2 |

## B02-01 — Resposta B

- **Requisito central:** CLI local sem credencial permanente.
- **Palavras decisivas:** *CLI 2.32+*, *console access*, *avoid access keys*.
- **A:** access keys do root não devem ser criadas nem usadas diariamente.
- **B:** correta; `aws login` usa o navegador e gerencia uma sessão temporária.
- **C:** variáveis permanentes continuam expondo credenciais de longo prazo.
- **D:** repositório privado não torna seguro versionar secrets.
- **Regra reutilizável:** acesso humano programático → prefira SSO ou login
  temporário.
- **Variação:** com IAM Identity Center, use `aws configure sso` e
  `aws sso login`.
- **Aulas:** 19–22.
- **Referência:** [`aws login`](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html).

## B02-02 — Resposta C

- **Requisito central:** EC2 acessar S3 sem segredo permanente.
- **Palavras decisivas:** *application on EC2*, *only read*, *specific bucket*.
- **A:** senha de console não autentica a aplicação em APIs e não deve ser
  armazenada.
- **B:** chaves na AMI se tornam secrets reutilizáveis e difíceis de rotacionar.
- **C:** correta; instance profile entrega credenciais temporárias da role.
- **D:** acesso público viola a necessidade de controle.
- **Regra reutilizável:** workload em serviço AWS → role com least privilege.
- **Variação:** se precisar gravar em um prefixo, conceda somente a ação e o ARN
  desse prefixo.
- **Aulas:** 25–26, 32–33.
- **Referência:** [IAM role for applications on EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

## B02-03 — Resposta A

- **Requisito central:** separar auditoria de credenciais de análise de
  permissões não utilizadas.
- **Palavras decisivas:** *password/MFA/access keys* e *services not used*.
- **A:** correta; credential report resume credenciais, e last accessed ajuda a
  refinar permissões.
- **B:** CloudTrail registra eventos, mas security groups não analisam IAM.
- **C:** Budgets trata de custos; Config trata de configuração/compliance.
- **D:** Access Analyzer não substitui o inventário de credenciais, e CUR é
  relatório de custos.
- **Regra reutilizável:** credencial duradoura → credential report; uso de
  permissão → last accessed.
- **Variação:** para confirmar uma chamada e seu resultado, consulte CloudTrail.
- **Aulas:** 27–28.
- **Referências:** [Credential report](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html) e [last accessed](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html).

## B02-04 — Resposta D

- **Requisito central:** conjunto atual de boas práticas IAM.
- **A:** MFA não torna root uma identidade de uso diário.
- **B:** credenciais temporárias e MFA são preferíveis.
- **C:** identidades compartilhadas prejudicam atribuição e auditoria.
- **D:** correta; combina federação, roles, MFA, least privilege e proteção do
  root.
- **Regra reutilizável:** pessoas usam identidade individual temporária;
  workloads usam roles.
- **Variação:** root é aceitável somente durante uma tarefa que realmente o
  exige.
- **Aulas:** 25–30.
- **Referência:** [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

## B02-05 — Resposta B

- **Requisito central:** alertar sobre custo real e previsto.
- **Palavras decisivas:** *small monthly budget*, *before exceeding*.
- **A:** CPU não representa a conta inteira e não bloqueia cobrança.
- **B:** correta; Budgets monitora limites actual e forecasted, mas ainda exige
  cleanup.
- **C:** Service Quotas limita quantidades técnicas, não dólares.
- **D:** Cost Explorer analisa custos e não encerra tudo automaticamente.
- **Regra reutilizável:** limite/alerta financeiro → AWS Budgets.
- **Variação:** análise detalhada de gastos históricos pode apontar para Cost
  Explorer.
- **Aulas:** 31.
- **Referência:** [Managing costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

## B02-06 — Resposta C

- **Requisito central:** instalar e iniciar software no primeiro boot.
- **Palavras decisivas:** *first boot*, *automatically*.
- **A:** instance type seleciona capacidade, não instala aplicação.
- **B:** security group permite tráfego, mas não configura o servidor.
- **C:** correta; user data automatiza o boot, e a rede é configurada
  separadamente.
- **D:** key pair não armazena script.
- **Regra reutilizável:** bootstrap de EC2 → user data; alcance de rede →
  security group.
- **Variação:** por padrão, o script Linux normalmente não roda novamente em
  todos os reboots.
- **Aulas:** 32–35.
- **Referência:** [EC2 user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html).

## B02-07 — Answer A

- **Central requirement:** sustained CPU performance.
- **Keywords:** *CPU-intensive*, *relatively little memory*, *sustained*.
- **A:** correct; compute-optimized instances target processor-intensive work.
- **B:** memory optimized targets large in-memory data sets.
- **C:** storage optimized targets local I/O.
- **D:** burstable performance is not automatically suitable for sustained CPU
  demand.
- **Reusable rule:** choose the family from the workload bottleneck.
- **Variation:** a large in-memory data set would point to memory optimized.
- **Lessons:** 34.
- **Reference:** [EC2 instance type categories](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-type-specifications.html).

## B02-08 — Answer D

- **Central requirement:** public HTTPS and restricted SSH.
- **Keywords:** *internet users*, *only from corporate IPv4*.
- **A:** exposes SSH to every IPv4 address.
- **B:** reverses the required source scopes.
- **C:** port 80 is HTTP; port 3389 is RDP.
- **D:** correct; 443 is public and 22 is limited to one `/32` source.
- **Reusable rule:** application port follows its audience; administrative ports
  use the narrowest source.
- **Variation:** if SSH is unnecessary, omit port 22 entirely.
- **Lessons:** 35.
- **Reference:** [Security group use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html).

## B02-09 — Answer B

- **Central requirement:** response to an outbound connection.
- **Keyword:** *stateful*.
- **A:** an inbound ephemeral-port rule is unnecessary for response traffic.
- **B:** correct; stateful connection tracking permits the response.
- **C:** the external response does not originate from the instance itself.
- **D:** security groups have allow rules, not ordered explicit deny rules.
- **Reusable rule:** allowed request → response is automatically allowed.
- **Variation:** a new inbound connection still needs an applicable inbound
  rule.
- **Lessons:** 35.
- **Reference:** [EC2 security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html).

## B02-10 — Answer C

- **Central requirement:** map EC2 launch components to their functions.
- **A:** AMI supplies the image; security group controls traffic.
- **B:** instance type selects capacity; user data automates initialization.
- **C:** correct; all four mappings are accurate.
- **D:** key pair does not select Region, and Budgets does not attach storage.
- **Reusable rule:** image + capacity + network control + bootstrap are separate
  decisions.
- **Variation:** an IAM role supplies API permissions, while a subnet defines
  network placement.
- **Lessons:** 32–35.
- **Referências:** [EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html) e [EC2 user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html).

## Ação após a correção

Registre no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md):

- toda resposta errada;
- toda resposta correta com confiança baixa;
- a palavra decisiva;
- a regra de decisão;
- as datas D+2 e D+7.
