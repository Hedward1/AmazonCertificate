# B02 — Gabarito comentado

Abra este arquivo somente depois de responder e registrar a confiança em todas
as [questões B02](B02_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B02-01 | B | 1.1 |
| B02-02 | C | 1.2 |
| B02-03 | A,B | 1.1 |
| B02-04 | D | 1.1 |
| B02-05 | B | 4.2 |
| B02-06 | C | 3.2 |
| B02-07 | A | 3.2 |
| B02-08 | A,C | 1.2 |
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

## B02-03 — Resposta A,B

- **Requisito central:** separar auditoria de credenciais de análise de
  permissões não utilizadas.
- **Palavras decisivas:** *password/MFA/access keys* e *services not used*.
- **A:** correta; o credential report resume o estado e a idade das credenciais
  duradouras dos IAM users.
- **B:** correta; last accessed information/Access Advisor mostra quando uma
  identidade acessou serviços e ajuda a refinar permissões.
- **C:** security groups filtram tráfego de rede e não inventariam credenciais
  IAM.
- **D:** o Cost and Usage Report detalha custos e uso faturável, não o uso de
  permissões IAM.
- **E:** AWS Budgets monitora custos ou uso, não lista access keys.
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

## B02-08 — Answer A,C

- **Central requirement:** expose TLS at the public ALB while allowing private
  targets to receive application traffic only from that ALB.
- **Keywords:** *terminates HTTPS*, *private subnets*, *only from the load
  balancer*, *no inbound SSH*.
- **A:** correct; the internet-facing listener needs inbound TCP 443 from its
  public IPv4 audience.
- **B:** an internet source on the target port bypasses the intended ALB-only
  network boundary whenever a route or public address makes the instance
  reachable.
- **C:** correct; referencing the ALB security group authorizes traffic from
  load-balancer nodes without opening the target port to arbitrary sources.
- **D:** this reverses the traffic direction and puts the backend port on the
  frontend security group instead of authorizing the ALB listener.
- **E:** security groups are stateful, so response traffic for an allowed flow
  does not require a separate broad ephemeral-port ingress rule.
- **Reusable rule:** public client → listener SG; listener SG → private target
  SG on the application port.
- **Variation:** if SSH is unnecessary because Session Manager is configured,
  omit port 22 instead of opening it to an administrative CIDR.
- **Lessons:** 35.
- **Reference:** [Security group use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html).

## B02-09 — Answer B

- **Central requirement:** distinguish the stateful instance security group from
  the stateless subnet network ACL on an outbound HTTPS flow.
- **Keywords:** *initiates*, *security group outbound 443*, *network ACL inbound
  ephemeral ports*, *additional inbound rule*.
- **A:** the stateless network ACL needs the corresponding response-port path,
  but a broad inbound ephemeral rule is unnecessary on the stateful security
  group for an established outbound connection.
- **B:** correct; security-group connection tracking permits the response to the
  allowed outbound flow.
- **C:** the response source is the external service, and no self-referencing
  inbound 443 rule is required for that established flow.
- **D:** security groups contain allow rules and do not implement ordered
  explicit deny processing.
- **Reusable rule:** allowed security-group flow → return traffic is tracked;
  stateless NACLs still need both directions and the relevant response ports.
- **Variation:** a new inbound connection still needs an applicable inbound
  rule.
- **Lessons:** 35.
- **Reference:** [EC2 security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html).

## B02-10 — Answer C

- **Central requirement:** combine a reproducible image, right-sized capacity,
  tier-to-tier network authorization, and automated bootstrap without mixing
  their responsibilities.
- **Keywords:** *approved operating system*, *CPU and memory*, *HTTPS only from
  the ALB*, *automatically at first boot*.
- **A:** an AMI supplies the system image; it is not the control plane for
  runtime firewall authorization, and an instance type does not choose the OS.
- **B:** a security group filters traffic; it cannot install software, while
  user data does not choose the instance hardware.
- **C:** correct; the AMI, instance type, security group reference, and user data
  each satisfy the corresponding requirement and can evolve independently.
- **D:** a key pair authenticates supported instance access; it does not select a
  Region, and AWS Budgets neither provisions nor attaches storage.
- **Reusable rule:** image + capacity + network control + bootstrap are separate
  architectural decisions that must be composed explicitly.
- **Variation:** an IAM role supplies API permissions, while a subnet defines
  network placement.
- **Lessons:** 32–35.
- **References:** [EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html), [EC2 user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html), and [security-group referencing](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html#security-group-referencing).

## Ação após a correção

Registre no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md):

- toda resposta errada;
- toda resposta correta com confiança baixa;
- a palavra decisiva;
- a regra de decisão;
- as datas D+2 e D+7.
