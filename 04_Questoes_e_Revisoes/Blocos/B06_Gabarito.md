# B06 — Gabarito comentado

Abra depois de responder às [questões B06](B06_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B06-01 | B | 3.4 |
| B06-02 | B | 3.4 |
| B06-03 | C | 3.4 |
| B06-04 | B | 2.2 |
| B06-05 | B | 3.4 |
| B06-06 | D | 3.4 |
| B06-07 | C | 3.4 |
| B06-08 | A | 2.2 |
| B06-09 | D | 3.4 |
| B06-10 | A | 4.2 |

## B06-01 — Resposta B

- **Requisito central:** rotear HTTPS por hostname e path usando um endpoint.
- **Palavras decisivas:** *HTTPS*, *host*, *path*, *único endpoint*.
- **A:** NLB não interpreta condições HTTP nem possui regra de path.
- **B:** correta; ALB avalia condições L7 e encaminha a target groups distintos.
- **C:** GWLB insere appliances de rede, não roteia URLs de aplicação.
- **D:** EFS compartilha arquivos e não distribui requisições HTTP.
- **Regra reutilizável:** host, path, header, method ou query → ALB.
- **Variação:** cada target group pode ter porta e health path próprios.
- **Aulas:** 72–74.
- **Referência:** [ALB listeners and rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html).

## B06-02 — Resposta B

- **Requisito central:** publicar UDP com baixa latência e IPs estáticos.
- **Palavras decisivas:** *UDP*, *IP estático por AZ*, *allowlist*.
- **A:** ALB atende protocolos de aplicação HTTP/HTTPS/gRPC, não UDP.
- **B:** correta; NLB opera em L4, suporta UDP e endereçamento zonal apropriado.
- **C:** GWLB é destinado a appliances transparentes.
- **D:** private hosted zone não publica endpoint na internet nem balanceia o
  fluxo.
- **Regra reutilizável:** TCP/UDP/TLS, alta performance ou IP fixo → NLB.
- **Variação:** EIP por subnet é opção para NLB internet-facing compatível.
- **Aulas:** 75–76.
- **Referência:** [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html).

## B06-03 — Resposta C

- **Requisito central:** inserir e escalar firewalls virtuais transparentes.
- **Palavras decisivas:** *appliance*, *transparente*, *caminho de rede*.
- **A:** ALB termina tráfego L7 e não é gateway transparente.
- **B:** NLB publica um serviço L4, mas não oferece o padrão completo de
  inserção de appliances.
- **C:** correta; GWLB, endpoints e route tables formam o caminho de inspeção.
- **D:** uma NAT instance sem rotas não recebe o tráfego e cria ponto único.
- **Regra reutilizável:** firewall/IDS/IPS fleet → GWLB + endpoints + rotas.
- **Variação:** GWLB troca tráfego com appliances por GENEVE porta 6081.
- **Aulas:** 77.
- **Referência:** [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html).

## B06-04 — Resposta B

- **Requisito central:** diagnosticar diferença entre estado EC2 e saúde no TG.
- **Palavras decisivas:** *running*, *unhealthy*, *não recebe tráfego*.
- **A:** snapshot não testa a resposta atual da aplicação.
- **B:** correta; path, porta, success code, aplicação e SG formam o health path.
- **C:** password policy não controla o health check.
- **D:** storage compartilhado não corrige endpoint unhealthy.
- **Regra reutilizável:** EC2 `running` não implica target `healthy`.
- **Variação:** valide também NACL, rota e AZ habilitada.
- **Aulas:** 72–74.
- **Referência:** [ALB target health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html).

## B06-05 — Resposta B

- **Requisito central:** avaliar afinidade de sessão e seus limites.
- **Palavras decisivas:** *sticky sessions*, *trade-off*.
- **A:** stickiness normalmente depende de cookies no ALB.
- **B:** correta; afinidade pode concentrar tráfego e não torna estado durável.
- **C:** um atributo não muda o tipo de load balancer.
- **D:** ELB não replica dados do banco.
- **Regra reutilizável:** use stickiness para compatibilidade; externalize estado
  para elasticidade e recuperação.
- **Variação:** falha do target perde sessão mantida somente em sua memória.
- **Aulas:** 78.
- **Referência:** [Sticky sessions](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#sticky-sessions).

## B06-06 — Resposta D

- **Requisito central:** distribuir tráfego entre targets de AZs desiguais.
- **Palavras decisivas:** *ALB*, *dois e oito targets*, *todos os targets*.
- **A:** ALB usa cross-zone no nível do load balancer.
- **B:** cross-zone muda escopo de distribuição, não estado de saúde.
- **C:** GWLB não é necessário para balanceamento web.
- **D:** correta; o ALB mantém cross-zone ligado no nível do load balancer e há
  controle suportado no target group.
- **Regra reutilizável:** confirme default por tipo e nível de configuração.
- **Variação:** desabilitar no target group também afeta suporte a stickiness.
- **Aulas:** 79.
- **Referência:** [Cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#cross-zone-load-balancing).

## B06-07 — Answer C

- **Requisito central:** obtain the original client IP behind an ALB.
- **Palavras decisivas:** *ALB*, *client IP*, *logging*.
- **A:** EBS device names contain storage information.
- **B:** a target group ARN identifies configuration, not a client.
- **C:** correct; ALB forwards client information in HTTP headers such as
  `X-Forwarded-For`.
- **D:** KMS encryption context is not request addressing.
- **Regra reutilizável:** ALB creates a backend connection; trust forwarded
  headers only through a controlled proxy boundary.
- **Variação:** never accept a spoofable forwarded header directly from an
  untrusted internet path.
- **Aulas:** 72.
- **Referência:** [X-Forwarded headers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/x-forwarded-headers.html).

## B06-08 — Answer A

- **Requisito central:** let in-flight requests finish during target removal.
- **Palavras decisivas:** *deployment*, *finish*, *removed*.
- **A:** correct; deregistration delay keeps the target draining for the
  configured period.
- **B:** DNS TTL does not drain backend requests.
- **C:** EFS lifecycle changes file storage classes.
- **D:** snapshot archive changes recovery economics.
- **Regra reutilizável:** graceful target removal → deregistration delay.
- **Variação:** the application shutdown timeout must align with the delay.
- **Aulas:** 82 (preparação para o B07).
- **Referência:** [Deregistration delay](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#modify-target-group-health-settings).

## B06-09 — Answer D

- **Requisito central:** define the role of a target group.
- **Palavras decisivas:** *destinations*, *health-check configuration*.
- **A:** a hosted zone contains DNS records.
- **B:** a target group can contain multiple compatible targets.
- **C:** ELB routes connections and does not replicate application data.
- **D:** correct; rules/listeners forward to target groups, which organize
  targets and health settings.
- **Regra reutilizável:** listener accepts; rule selects; target group delivers
  and checks health.
- **Variação:** instance, IP, Lambda and ALB target types vary by load balancer
  and protocol compatibility.
- **Aulas:** 72–77.
- **Referência:** [ALB target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html).

## B06-10 — Answer A

- **Requisito central:** identify cost from an idle test load balancer.
- **Palavras decisivas:** *no targets*, *no traffic*, *cost*.
- **A:** correct; time and capacity dimensions can still generate charges.
- **B:** empty does not mean free.
- **C:** load balancers do not expose an EC2-style stop state.
- **D:** cleanup never grants authority over unrelated EIPs.
- **Regra reutilizável:** delete unused ELB resources and audit dependencies
  separately.
- **Variação:** public IPv4, data processing and appliance licenses can add
  costs depending on design.
- **Aulas:** 73–79.
- **Referência:** [Elastic Load Balancing pricing](https://aws.amazon.com/elasticloadbalancing/pricing/).

## Ação após a correção

Registre erros e acertos de baixa confiança no
[Caderno de Erros](../Caderno_de_Erros_SAA-C03.md). Reescreva a palavra decisiva
e desenhe o fluxo listener → rule → target group → health check.
