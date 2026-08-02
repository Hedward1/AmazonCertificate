# B03 — Gabarito comentado

Abra este arquivo somente depois de responder e registrar a confiança em todas
as [questões B03](B03_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B03-01 | C | 1.2 |
| B03-02 | A | 1.2 |
| B03-03 | A,D | 1.2 |
| B03-04 | B | 1.1 |
| B03-05 | C | 4.2 |
| B03-06 | B | 4.2 |
| B03-07 | D | 4.2 |
| B03-08 | A,D | 4.2 |
| B03-09 | C | 4.2 |
| B03-10 | B | 4.2 |

## B03-01 — Resposta C

- **Requisito central:** restabelecer SSH com a menor exposição de rede.
- **Palavras decisivas:** *SSH convencional*, *security group somente HTTPS*,
  *IPv4 do administrador*.
- **A:** expõe SSH para toda a internet; MFA ou uma chave não eliminam o risco
  dessa origem ampla, e o usuário padrão normalmente não é `root`.
- **B:** TCP 3389 é usado normalmente por RDP em Windows, não por SSH em Linux.
- **C:** correta; SSH usa TCP 22, e a origem `/32` limita o acesso ao endereço
  informado. A chave e o usuário da AMI também precisam estar corretos.
- **D:** a sessão é iniciada em direção à instância, portanto é necessária uma
  inbound rule aplicável; somente liberar saída não resolve.
- **Regra reutilizável:** porta administrativa → protocolo correto e origem mais
  restrita possível.
- **Variação:** se a instância não tiver IPv4 público, será necessário outro
  caminho, como VPN, EC2 Instance Connect Endpoint ou Session Manager.
- **Aulas:** 36–41.
- **Referência:** [Connect to a Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html).

## B03-02 — Resposta A

- **Requisito central:** acesso Linux autorizado pelo IAM sem distribuir uma
  chave SSH permanente compartilhada.
- **Palavras decisivas:** *EC2 Instance Connect*, *sem distribuir
  permanentemente*.
- **A:** correta; a API envia a chave pública aos metadados por 60 segundos para
  iniciar a conexão. A sessão estabelecida pode continuar, mas ainda depende de
  alcance de rede para SSH.
- **B:** EC2 Instance Connect não grava uma chave privada permanente na AMI.
- **C:** o mecanismo continua usando SSH; uma conexão direta precisa alcançar a
  porta 22, ou usar um EC2 Instance Connect Endpoint para o caminho privado.
- **D:** o caso de uso é acesso SSH a sistemas compatíveis, não RDP exclusivo de
  Windows.
- **Regra reutilizável:** EC2 Instance Connect → IAM autoriza o envio temporário
  da chave pública; rede e SSH continuam necessários.
- **Variação:** para uma instância somente com IPv4 privado, o endpoint permite
  estabelecer o túnel sem adicionar um IPv4 público.
- **Aulas:** 42.
- **Referência:** [EC2 Instance Connect methods](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html).

## B03-03 — Resposta A,D

- **Requisito central:** shell em instância privada sem inbound administrative
  ports nem bastion.
- **Palavras decisivas:** *sem IP público*, *proíbe portas de entrada*,
  *IAM-controlled shell*.
- **A:** correta; SSM Agent e uma instance role adequada tornam a instância
  gerenciável pelo Systems Manager.
- **B:** contradiz a ausência de IP público e a proibição de portas
  administrativas de entrada.
- **C:** Dedicated Host trata de hardware dedicado e posicionamento, não cria um
  canal administrativo.
- **D:** correta; o managed node precisa alcançar os endpoints do Systems
  Manager por um caminho de saída.
- **E:** Session Manager inicia a comunicação a partir do managed node; não
  requer liberar HTTPS de entrada da internet.
- **Regra reutilizável:** administração privada sem porta de entrada → Session
  Manager com managed node e IAM.
- **Variação:** conectividade aos serviços pode ser fornecida por NAT ou
  interface VPC endpoints apropriados.
- **Aulas:** 37–42.
- **Referência:** [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html).

## B03-04 — Resposta B

- **Requisito central:** workload em EC2 chamar uma API sem access key
  permanente.
- **Palavras decisivas:** *application on EC2*, *avoid storage and manual
  rotation*.
- **A:** credenciais do root não devem ser criadas ou armazenadas na instância.
- **B:** correta; o instance profile disponibiliza credenciais temporárias da
  role, que o SDK pode obter e renovar automaticamente.
- **C:** user data não é armazenamento seguro de secrets; chaves permanentes
  continuariam expostas e exigiriam rotação.
- **D:** EC2 key pair autentica acesso ao sistema operacional e não assina
  chamadas IAM para o DynamoDB.
- **Regra reutilizável:** aplicação em EC2 → instance role com least privilege,
  não access keys no código.
- **Variação:** restrinja a policy às ações do DynamoDB e ao ARN da tabela
  realmente necessários.
- **Aulas:** 43.
- **Referências:** [IAM role for applications on EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) e [role credentials from instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-security-credentials.html).

## B03-05 — Resposta C

- **Requisito central:** financiar somente a disponibilidade exigida por cada
  classe sem aplicar o risco de desenvolvimento à produção nem o custo de
  produção ao ambiente descartável.
- **Palavras decisivas:** *99,95%*, *RTO*, *RPO*, *perda de uma AZ*, *dados
  sintéticos*, *reconstruído*, *aceita interrupções*.
- **A:** inverte as necessidades: uma única Spot não atende a produção nem à
  falha de AZ, enquanto desenvolvimento recebe capacidade cara e ociosa.
- **B:** a arquitetura pode exceder o objetivo de desenvolvimento, mas não é a
  alternativa de menor custo apropriado porque ignora horário, reconstrução e
  tolerância a interrupção.
- **C:** correta; produção recebe redundância, capacidade estável e proteção de
  dados compatíveis com seus objetivos, enquanto agenda, scale-to-zero e Spot
  exploram somente a flexibilidade comprovada de desenvolvimento.
- **D:** hardware dedicado atende isolamento ou licenciamento, não substitui
  redundância entre AZs, failover nem uma estratégia de dados para o RPO.
- **Regra reutilizável:** criticidade + objetivo/SLA + RTO + RPO + escopo de
  falha determinam disponibilidade; depois escolha o modelo de compute de menor
  custo que preserve esses limites.
- **Variação:** homologação pode precisar temporariamente de topologia semelhante
  à produção para validar failover, mesmo sendo classificada como não produção.
- **Aulas:** 44–46.
- **Referências:** [understanding availability needs](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/understanding-availability-needs.html) e [Spot interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html).

## B03-06 — Resposta B

- **Requisito central:** desconto por compromisso com máxima flexibilidade entre
  compute services.
- **Palavras decisivas:** *USD por hora*, *Regions*, *Fargate ou Lambda*.
- **A:** uma Standard RI depende de atributos EC2 correspondentes e não acompanha
  a migração para Fargate ou Lambda.
- **B:** correta; Compute Savings Plans aceitam compromisso de uso por um ou
  três anos e se aplicam com flexibilidade a EC2, Fargate e Lambda.
- **C:** preserva flexibilidade, mas não oferece o desconto solicitado em troca
  do compromisso.
- **D:** EC2 Instance Savings Plans ficam vinculados a uma família de instância
  em uma Region e não cobrem a migração descrita.
- **Regra reutilizável:** compromisso de gasto com mudança entre família,
  Region ou compute service → Compute Savings Plan.
- **Variação:** se família e Region permanecerem fixas, um EC2 Instance Savings
  Plan pode oferecer desconto maior com menos flexibilidade.
- **Aulas:** 44, 46.
- **Referência:** [Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html).

## B03-07 — Answer D

- **Central requirement:** minimize cost for an interruption-tolerant batch
  workload without depending on one Spot pool.
- **Keywords:** *checkpoints*, *retried*, *flexible*, *reducing likelihood of
  interruption together*.
- **A:** On-Demand avoids Spot interruptions but does not provide the requested
  Spot-level savings; one AZ also limits placement choices.
- **B:** Dedicated Hosts address isolation and licensing rather than cheap,
  interruption-tolerant batch processing.
- **C:** one capacity pool creates dependency on that pool, and AWS does not
  recommend lowest-price-only because it can increase interruption risk.
- **D:** correct; multiple instance types and AZs expand eligible pools, while
  price-capacity-optimized considers capacity availability and price. Notices
  allow graceful checkpoint handling.
- **Reusable rule:** fault-tolerant flexible batch → diversified Spot capacity
  plus interruption handling.
- **Variation:** a small On-Demand base can be combined with Spot when some
  baseline capacity must remain stable.
- **Lessons:** 45.
- **References:** [Spot Instance interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html) and [Fleet allocation strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html).

## B03-08 — Answer A,D

- **Central requirement:** distinguish a Zonal RI, which couples discount and
  zonal capacity, from an On-Demand Capacity Reservation, which separates the
  capacity decision from an eligible billing discount.
- **Keywords:** *specific Availability Zone*, *discount and capacity*,
  *coupled or separate*.
- **A:** correct; a matching Zonal Reserved Instance provides a billing discount
  and reserves capacity in the selected AZ.
- **B:** a Compute Savings Plan discounts eligible usage but does not reserve
  EC2 capacity.
- **C:** a Regional RI provides a discount and AZ flexibility within the Region,
  but it does not reserve capacity.
- **D:** correct; an On-Demand Capacity Reservation supplies capacity separately,
  while eligible usage can still receive an applicable Savings Plan or RI
  billing discount.
- **E:** Spot capacity can be interrupted and is not a three-year capacity
  guarantee, regardless of request persistence.
- **Reusable rule:** a Zonal RI couples discount and zonal capacity; an
  On-Demand Capacity Reservation separates the capacity guarantee from the
  billing-discount mechanism.
- **Variation:** a Regional RI favors AZ flexibility and discount but does not
  reserve capacity in one Availability Zone.
- **Lessons:** 44, 46.
- **Reference:** [Regional and zonal Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-scope.html).

## B03-09 — Answer C

- **Central requirement:** physical host visibility and placement control for
  socket/core-bound licensing.
- **Keywords:** *physical sockets and cores*, *identify host*, *control
  placement*.
- **A:** Dedicated Instances provide single-tenant hardware but no host ID,
  socket/core visibility, host affinity, or targeted placement.
- **B:** shared tenancy does not provide the required hardware dedication or
  physical-host information.
- **C:** correct; Dedicated Hosts expose host and hardware information, support
  placement control and provide comprehensive BYOL capabilities.
- **D:** a placement group controls relative placement for performance or fault
  goals; it does not supply the requested host licensing visibility.
- **Reusable rule:** per-socket/per-core BYOL or host affinity → Dedicated Host.
- **Variation:** isolation without host-level control can point to Dedicated
  Instances instead.
- **Lessons:** 44, 46.
- **Reference:** [Amazon EC2 Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html).

## B03-10 — Answer B

- **Central requirement:** hardware isolated from other accounts, without
  host-level control, billed per instance.
- **Keywords:** *must not share*, *does not need visibility or affinity*,
  *per-instance billing*.
- **A:** a placement group does not change shared tenancy into single-tenant
  hardware.
- **B:** correct; Dedicated Instances run on hardware dedicated to one customer
  account, do not expose host placement controls, and use per-instance billing.
- **C:** Dedicated Hosts also isolate hardware but add unnecessary host
  visibility, placement features, BYOL support, and per-host billing.
- **D:** Savings Plans alter eligible compute pricing, not physical tenancy.
- **Reusable rule:** isolation only → Dedicated Instance; host visibility,
  affinity or socket/core BYOL → Dedicated Host.
- **Variation:** verify whether the compliance rule requires account-level
  isolation or explicit control of a named physical server.
- **Lessons:** 44, 46.
- **Reference:** [Amazon EC2 Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html).

## Ação após a correção

Registre no [Caderno de Erros](../Caderno_de_Erros_SAA-C03.md):

- toda resposta errada;
- toda resposta correta com confiança baixa;
- a palavra decisiva;
- a regra de decisão;
- as datas D+2 e D+7.
