# B06 — Questões: ALB, NLB, GWLB e distribuição

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 6 em português e 4 em inglês<br>
**Regra:** selecione uma resposta<br>
**Tempo sugerido:** 15 minutos<br>
**Gabarito:** [arquivo separado](B06_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B06-01 | 3.4 | ALB rules | Situacional | Básica | Português |
| B06-02 | 3.4 | NLB | Situacional | Intermediária | Português |
| B06-03 | 3.4 | GWLB | Situacional | Intermediária | Português |
| B06-04 | 2.2 | Health check | Diagnóstico | Intermediária | Português |
| B06-05 | 3.4 | Stickiness | Fundamental | Básica | Português |
| B06-06 | 3.4 | Cross-zone | Situacional | Avançada | Português |
| B06-07 | 3.4 | ALB client IP | Diagnóstico | Intermediária | Inglês |
| B06-08 | 2.2 | Deregistration | Situacional | Básica | Inglês |
| B06-09 | 3.4 | Target groups | Fundamental | Intermediária | Inglês |
| B06-10 | 4.2 | ELB cost | Situacional | Básica | Inglês |

## Como resolver

1. Circule o protocolo: HTTP/HTTPS/gRPC, TCP/UDP/TLS ou tráfego IP.
2. Procure condições L7: host, path, header ou método.
3. Diferencie publicar aplicação de inserir appliance.
4. Separe estado da instância e estado do target group.
5. Para cross-zone, conte targets em cada AZ.
6. Para source IP, identifique onde a conexão é terminada.
7. Para cleanup, trate load balancer, target groups e EIPs separadamente.

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

Qual serviço foi projetado para esse padrão?

- A. ALB com Lambda targets.
- B. NLB com listener HTTP.
- C. GWLB, endpoints e rotas correspondentes.
- D. NAT instance única sem alteração de rotas.

### B06-04

Uma instância aparece como `running`, mas não recebe tráfego do ALB. No target
group ela aparece como `unhealthy`.

Qual investigação deve ocorrer primeiro?

- A. Restaurar um snapshot do root volume.
- B. Validar health path/porta, resposta da aplicação e regras de SG.
- C. Alterar a IAM password policy.
- D. Habilitar EBS Multi-Attach.

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

Which setting is most relevant?

- A. Deregistration delay.
- B. DNS TTL of the instance hostname.
- C. EFS lifecycle management.
- D. Snapshot archive tier.

### B06-09

Which statement about Elastic Load Balancing target groups is correct?

- A. A target group is a Route 53 hosted zone.
- B. A target group always contains exactly one EC2 instance.
- C. A target group creates application data replicas.
- D. A target group defines compatible destinations and their health-check
  configuration for listener/rule forwarding.

### B06-10

A test load balancer has no targets and receives no traffic.

What should the team assume?

- A. It can still incur time/capacity-related charges and should be deleted
  when unused.
- B. It is always free while its target groups are empty.
- C. It can be stopped like an EC2 instance to pause billing.
- D. Deleting it automatically releases every unrelated Elastic IP.

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
