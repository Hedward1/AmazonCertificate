# B06 — Questões: ALB, NLB, GWLB e distribuição

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 6 em português e 4 em inglês<br>
**Formato:** questões single-answer e multi-answer; siga a instrução de cada questão<br>
**Tempo sugerido:** 15 minutos<br>
**Gabarito:** [arquivo separado](B06_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Formato | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|---|
| B06-01 | 3.4 | ALB rules | single | fundamental | básica | Português |
| B06-02 | 3.4 | NLB | single | fundamental | básica | Português |
| B06-03 | 3.4 | GWLB | multi-2 | fundamental | intermediária | Português |
| B06-04 | 2.2 | Health check | single | integrada | avançada | Português |
| B06-05 | 3.4 | Stickiness | single | situacional | intermediária | Português |
| B06-06 | 3.4 | Cross-zone | single | situacional | intermediária | Português |
| B06-07 | 3.4 | ALB client IP | single | situacional | intermediária | Inglês |
| B06-08 | 2.2 | Deregistration | multi-2 | integrada | avançada | Inglês |
| B06-09 | 3.4 | Target groups | single | situacional | intermediária | Inglês |
| B06-10 | 4.2 | ELB cost | single | integrada | avançada | Inglês |

## Questões

### B06-01

Uma empresa quer usar um único endpoint HTTPS para enviar requisições de
`api.exemplo.com` ao serviço A e requisições de
`loja.exemplo.com/imagens/*` ao serviço B.

Qual solução atende ao requisito?

- A. NLB com duas EIPs e uma regra de path.
- B. ALB com regras por host/path e target groups distintos.
- C. GWLB com dois appliances GENEVE.
- D. EFS com dois access points.

### B06-02

Um serviço usa UDP, exige latência muito baixa e precisa fornecer IP público
estático por Availability Zone para uma allowlist externa.

Qual balanceador deve ser escolhido?

- A. Application Load Balancer.
- B. Network Load Balancer.
- C. Gateway Load Balancer.
- D. Route 53 private hosted zone isoladamente.

### B06-03

Uma organização quer inserir uma frota escalável de firewalls virtuais de forma
transparente no caminho de rede entre consumidores e aplicações.

Quais componentes são necessários para implementar esse padrão?

**Choose TWO.**

- A. Um Application Load Balancer com Lambda targets para encapsular todo o
  tráfego de rede.
- B. Um Gateway Load Balancer com os appliances registrados em seu target
  group.
- C. Um Network Load Balancer com listener HTTP para substituir os firewalls.
- D. Gateway Load Balancer endpoints e route tables que direcionem o tráfego
  pelo caminho de inspeção.
- E. Uma NAT instance única sem qualquer alteração nas route tables.

### B06-04

Após uma nova implantação, uma instância aparece como `running`, mas o ALB não
envia tráfego a ela porque o target está `unhealthy`. Outros targets do mesmo
grupo continuam saudáveis. A aplicação deveria responder `200` em `/health` na
porta 8080, e o acesso direto pela internet às instâncias deve continuar
bloqueado.

Qual investigação deve ocorrer primeiro?

- A. Aumentar o deregistration delay do target group para que o ALB considere o
  target saudável durante mais tempo.
- B. Validar protocolo, porta e path do health check, confirmar a resposta da
  aplicação e permitir a porta 8080 no SG da instância a partir do SG do ALB.
- C. Habilitar stickiness no listener para fixar novos clientes no target
  `unhealthy` durante a investigação.
- D. Criar um registro weighted no Route 53 que aponte diretamente para o IP
  privado da instância.

### B06-05

Uma aplicação legada habilitará sticky sessions no ALB.

Qual é o principal trade-off?

- A. A afinidade elimina completamente o uso de cookies.
- B. Ela mantém afinidade, mas pode desequilibrar carga e não substitui um
  store de sessão durável.
- C. Ela converte o ALB em NLB.
- D. Ela replica automaticamente o banco da aplicação.

### B06-06

Um ALB possui dois targets na AZ A e oito na AZ B. A equipe deseja distribuir
requisições entre todos os targets habilitados e saudáveis.

Qual afirmação atual está correta?

- A. ALB nunca suporta cross-zone.
- B. Cross-zone transforma qualquer target unhealthy em healthy.
- C. É obrigatório substituir o ALB por GWLB.
- D. Cross-zone fica ligado no nível do ALB; o comportamento suportado também
  pode ser configurado no nível do target group.

### B06-07

An application behind an ALB needs the original client IP address for trusted
access logging.

Where should the application obtain it?

- A. From the EBS device name.
- B. From the target group ARN.
- C. From forwarded HTTP headers such as `X-Forwarded-For`, applying a trusted
  proxy boundary.
- D. From a KMS encryption context only.

### B06-08

During a deployment, targets must finish in-flight requests before they are
removed from service.

Which actions support graceful target removal?

**Choose TWO.**

- A. Configure the target group's deregistration delay for the expected
  request duration.
- B. Increase the DNS TTL of the instance hostname.
- C. Move related EBS snapshots to the archive tier.
- D. Keep the application process alive during draining and align its shutdown
  timeout with the deregistration delay.
- E. Configure EFS lifecycle management for the target logs.

### B06-09

An Application Load Balancer uses host- and path-based listener rules to send
`api.example.com/v2/*` to IP targets in one service and static requests to EC2
instances in another service. Each service needs its own port, health-check path,
and deployment lifecycle, and an unhealthy destination must stop receiving new
requests without changing DNS.

Which statement correctly describes the component that connects these listener
rules to the two backend services?

- A. A target group is a Route 53 hosted zone that changes authoritative DNS
  whenever one application process fails.
- B. One target group must always contain exactly one EC2 instance, so IP targets
  and independent service deployments are not supported.
- C. A target group creates application-data replicas before a listener can
  forward a request.
- D. A target group defines a compatible target type and destinations together
  with their port and health-check configuration; listener rules forward to the
  appropriate group.

### B06-10

A cost review finds an internet-facing Application Load Balancer left from a
retired test environment. Its target groups are empty and traffic metrics are
zero, but a Route 53 record and security groups still reference the old design.
The team must stop avoidable spend without deleting resources that belong to
other environments.

Which conclusion and action are correct?

- A. The load balancer can still incur time/capacity-related charges; verify its
  dependencies, remove the obsolete DNS reference, and delete the unused load
  balancer explicitly.
- B. Scale any associated Auto Scaling group to zero but retain the load
  balancer and DNS record indefinitely; empty target groups suspend all
  load-balancer charges.
- C. Change the Route 53 record weight to zero and retain the provisioned load
  balancer for rollback; receiving no DNS traffic removes its hourly and
  capacity-related charges.
- D. Delete the load balancer, its hosted zone, and every similarly named
  security group immediately, without checking whether another environment
  shares those resources.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B06-01 | | | |
| B06-02 | | | |
| B06-03 | | | |
| B06-04 | | | |
| B06-05 | | | |
| B06-06 | | | |
| B06-07 | | | |
| B06-08 | | | |
| B06-09 | | | |
| B06-10 | | | |

Não abra o gabarito antes de preencher todas as linhas, inclusive nos acertos de
baixa confiança.
