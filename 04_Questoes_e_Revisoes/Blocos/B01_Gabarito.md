# B01 — Gabarito comentado

Abra este arquivo somente depois de responder e registrar a confiança em todas
as [questões B01](B01_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B01-01 | B | 2.2 |
| B01-02 | C | 2.1/3.4 |
| B01-03 | B,E | 1.1 |
| B01-04 | D | 1.1 |
| B01-05 | A | 1.1 |
| B01-06 | C | 1.1 |
| B01-07 | B | 1.1 |
| B01-08 | A,B | 1.1 |
| B01-09 | A | 1.1 |
| B01-10 | C | 1.1 |

## B01-01 — Resposta B

- **Requisito central:** tolerar falha de uma localização sem exigir outra
  Region.
- **Palavras decisivas:** *isolated location*, *low latency*, *no other Region*.
- **Raciocínio:** múltiplas AZs eliminam a dependência de uma única AZ e mantêm
  os componentes na rede regional de baixa latência.
- **A:** subnets diferentes na mesma AZ ainda compartilham a falha zonal.
- **B:** correta; distribui o workload pelo domínio de falha exigido.
- **C:** edge location não é local de backup ou origem completa da aplicação.
- **D:** uma única instância continua sendo single point of failure.
- **Regra reutilizável:** falha de AZ → Multi-AZ; falha regional → considere
  Multi-Region.
- **Variação:** *survive a regional outage* mudaria o desenho para Multi-Region.
- **Aulas:** 8–10.
- **Referência:** [Regions and Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html).

## B01-02 — Resposta C

- **Requisito central:** cache global perto dos usuários sem várias origens.
- **Palavras decisivas:** *static content*, *cache*, *global users*.
- **A:** subnets na origem não aproximam conteúdo dos usuários.
- **B:** funcionaria com muito mais complexidade e não atende ao pedido de evitar
  origens completas.
- **C:** correta; CloudFront usa uma rede de edge locations.
- **D:** uma Local Zone atende uma área, não forma uma rede global de cache.
- **Regra reutilizável:** conteúdo com cache e baixa latência global → CloudFront.
- **Variação:** computação que precisa estar próxima de uma única área
  metropolitana pode levar à análise de Local Zones.
- **Aulas:** 8–10.
- **Referência:** [How CloudFront delivers content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html).

## B01-03 — Resposta B,E

- **Requisito central:** identificar duas responsabilidades do cliente em EC2.
- **Palavras decisivas:** *guest operating system*, *security groups*, *data*.
- **A:** hardware físico é responsabilidade da AWS.
- **B:** correta; o cliente administra e aplica patches ao guest OS da
  instância.
- **C:** a camada de virtualização é responsabilidade da AWS.
- **D:** segurança física das instalações é responsabilidade da AWS.
- **E:** correta; o cliente configura acessos e protege os dados da aplicação.
- **Regra reutilizável:** em EC2, AWS cuida do host; cliente cuida do guest.
- **Variação:** um serviço mais gerenciado transfere mais operação à AWS, mas não
  transfere dados e permissões do cliente.
- **Aulas:** 8–11.
- **Referência:** [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

## B01-04 — Resposta D

- **Requisito central:** reconhecer o que continua com o cliente em um serviço
  gerenciado.
- **Palavras decisivas:** *confidential documents*, *permissions*, *encryption*.
- **A:** o sistema operacional dos servidores que executam o Amazon S3 faz parte
  da infraestrutura gerenciada pela AWS.
- **B:** a substituição dos dispositivos físicos de armazenamento é
  responsabilidade da AWS.
- **C:** a segurança física dos data centers é responsabilidade da AWS.
- **D:** correta; classificação, acessos e escolhas de proteção dos dados
  continuam com o cliente.
- **Regra reutilizável:** serviço gerenciado reduz operação, não a
  responsabilidade sobre dados e configuração.
- **Variação:** em EC2, o cliente também cuidaria do guest OS.
- **Aulas:** 8–11.
- **Referência:** [Shared responsibility — Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/shared-responsibility.html).

## B01-05 — Resposta A

- **Requisito central:** proteger e reduzir o uso do root.
- **Palavras decisivas:** *new account*, *daily activities*.
- **A:** correta; reúne MFA, ausência de access keys e identidade diária separada.
- **B:** privilégio total não é justificativa para uso cotidiano.
- **C:** compartilhar credenciais elimina atribuição individual e eleva o risco.
- **D:** rotação não torna seguras access keys do root.
- **Regra reutilizável:** root fica protegido e reservado às tarefas root-only.
- **Variação:** uma tarefa que exija root justifica login pontual, nunca seu uso
  como identidade diária.
- **Aulas:** 3, 11–17.
- **Referência:** [Root user best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html).

## B01-06 — Resposta C

- **Requisito central:** acesso comum, restrito e fácil de administrar.
- **Palavras decisivas:** *legacy IAM users*, *read only*, *team changes*.
- **A:** `AdministratorAccess` viola least privilege.
- **B:** uma role não funciona como grupo de membros.
- **C:** correta; o group centraliza a policy e mudanças de equipe.
- **D:** IAM groups não são principals de resource-based policies.
- **Regra reutilizável:** permissões comuns a IAM users → group; acesso temporário
  ou delegação → role.
- **Variação:** sem a limitação legada, acesso humano federado seria preferível.
- **Aulas:** 11–15.
- **Referência:** [IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html).

## B01-07 — Answer B

- **Central requirement:** avoid long-term credentials on EC2.
- **Keywords:** *EC2 workload*, *avoid storing*, *temporary credentials*.
- **A:** root keys must never be distributed to a workload.
- **B:** correct; an instance profile exposes temporary role credentials.
- **C:** an AMI containing keys copies a reusable secret.
- **D:** public access violates the access-control requirement.
- **Reusable rule:** AWS compute calling AWS APIs → use an IAM role.
- **Variation:** an external workload requires another temporary-credential
  mechanism, such as federation or Roles Anywhere.
- **Lessons:** 11–18.
- **Reference:** [Programmatic access alternatives](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html).

## B01-08 — Answer A,B

- **Central requirement:** configure temporary, limited, cross-account access.
- **Keywords:** *occasionally*, *production account*, *temporary*, *no duplicate
  credentials*.
- **A:** correct; the role permissions policy defines the allowed S3 actions and
  resources.
- **B:** correct; the trust relationship and the caller's `sts:AssumeRole`
  permission establish who can obtain a temporary session.
- **C:** creates duplicate long-term identities in production.
- **D:** root credentials must not be shared or used for deployment.
- **E:** public access violates the limited-access requirement.
- **Reusable rule:** cross-account delegation → role + trust + permissions.
- **Variation:** direct resource-based access could be valid for a supported
  service, but it must still trust the external principal.
- **Lessons:** 11–18; roles are completed in B02.
- **Reference:** [Cross-account IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html).

## B01-09 — Answer A

- **Central requirement:** grant one assumed workload role read access to known
  object keys in one prefix without adding discovery or mutation permissions.
- **Keywords:** *approved manifest*, *only `quarterly/`*, *never lists*, *KMS
  separately scoped*.
- **A:** correct; `GetObject` is the required data-plane action and the object ARN
  limits it to the exact prefix.
- **B:** every S3 action on every resource violates both action and resource
  least privilege.
- **C:** the bucket ARN names the bucket itself; `GetObject` requires object ARNs
  that include a key, wildcard, or the required prefix path.
- **D:** `ListBucket` is a bucket-level discovery action and neither retrieves an
  object nor matches the stated manifest-driven access pattern.
- **Reusable rule:** least privilege aligns principal, action, resource ARN, and
  conditions; add a separate KMS permission only when the encryption path needs it.
- **Variation:** if the application needed to discover keys, add a restricted
  `ListBucket` statement with an appropriate prefix condition.
- **Lessons:** 14–15.
- **Reference:** [Amazon S3 policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-policies-s3.html).

## B01-10 — Answer C

- **Central requirement:** centralized human access to multiple accounts with
  temporary credentials.
- **Keywords:** *corporate identity provider*, *multiple accounts*, *workforce*.
- **A:** root is not a shared workforce identity.
- **B:** multiplies long-term credentials and operational risk.
- **C:** correct; Identity Center integrates workforce identities, permission
  sets and temporary role sessions.
- **D:** groups are account-specific permission containers, not cross-account
  principals.
- **Reusable rule:** workforce + multiple accounts → IAM Identity Center.
- **Variation:** a workload, rather than a person, normally receives a workload
  role instead of workforce access.
- **Lessons:** 11–18; IAM avançado será retomado nas aulas 282–291.
- **Reference:** [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

## Ação após a correção

Registre no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md):

- toda resposta errada;
- toda resposta correta com confiança baixa;
- a palavra decisiva ignorada;
- a regra reutilizável;
- as datas da revisão D+2 e D+7.
