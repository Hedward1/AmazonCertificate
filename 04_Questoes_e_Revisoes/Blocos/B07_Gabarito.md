# B07 — Gabarito comentado

Abra depois das [questões B07](B07_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B07-01 | B | 3.4 |
| B07-02 | A | 3.4 |
| B07-03 | A,C | 2.2 |
| B07-04 | D | 3.2 |
| B07-05 | A | 3.2 |
| B07-06 | C | 3.2 |
| B07-07 | B | 3.2 |
| B07-08 | B,E | 2.2 |
| B07-09 | C | 3.2 |
| B07-10 | A | 4.2 |

## B07-01 — Resposta B

- **Requisito central:** associar certificado válido a um ALB regional.
- **Palavras decisivas:** *ALB*, *eu-west-1*, *hostname*.
- **A:** `us-east-1` é o requisito conhecido para certificado do CloudFront, não
  de todo ALB.
- **B:** correta; o certificado fica na Region do ALB e cobre o nome acessado.
- **C:** certificado ACM integrado não é instalado no EBS do target.
- **D:** certificados ACM não são recursos globais.
- **Regra reutilizável:** certificado ACM na Region do recurso integrado e nome
  presente no SAN/CN.
- **Variação:** DNS validation deve permanecer válida para renovação gerenciada.
- **Aulas:** 80–81.
- **Referência:** [ACM concepts](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html).

## B07-02 — Resposta A

- **Requisito central:** criptografar front-end e back-end.
- **Palavras decisivas:** *também entre ALB e targets*.
- **A:** correta; HTTPS nos dois trechos atende criptografia em trânsito de ponta
  a ponta arquitetural.
- **B:** HTTP interno deixa o segundo trecho sem TLS.
- **C:** EIP/EBS não configura transporte do load balancer.
- **D:** health checks não controlam criptografia.
- **Regra reutilizável:** requisito end-to-end → listener HTTPS e backend HTTPS.
- **Variação:** terminação somente no ALB pode bastar quando a política aceita a
  rede interna sem recriptografia.
- **Aulas:** 80–81.
- **Referência:** [ALB HTTPS listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html).

## B07-03 — Resposta A,C

- **Requisito central:** concluir requests durante remoção do target.
- **Palavras decisivas:** *scale-in*, *downloads ativos*, *não imediatamente*.
- **A:** correta; o deregistration delay mantém o target em draining pelo
  período configurado.
- **B:** DNS TTL não controla conexão já encaminhada ao target.
- **C:** correta; com o target group associado, o Auto Scaling deregistra o
  target e aguarda as requisições em andamento ou o timeout antes de terminar a
  instância.
- **D:** snapshot protege disco, não request em andamento.
- **E:** rotação KMS não coordena target removal.
- **Regra reutilizável:** scale-in/deploy gracioso → deregistration delay mais
  shutdown alinhado.
- **Variação:** requests que excedem o delay ainda podem ser interrompidos.
- **Aulas:** 82.
- **Referência:** [Deregistration delay](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/edit-target-group-attributes.html#modify-target-group-health-settings).

## B07-04 — Resposta D

- **Requisito central:** interpretar os três limites de capacidade.
- **Palavras decisivas:** *min=2*, *desired=4*, *max=8*, *agora*.
- **A:** min é piso, não alvo enquanto desired está acima dele.
- **B:** max é teto, não capacidade desejada.
- **C:** os valores não são somados.
- **D:** correta; desired é a capacidade buscada no momento.
- **Regra reutilizável:** `min ≤ desired ≤ max`; desired representa o alvo atual.
- **Variação:** uma policy altera desired, mas nunca além dos limites vigentes.
- **Aulas:** 83–84.
- **Referência:** [ASG capacity limits](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html).

## B07-05 — Resposta A

- **Requisito central:** manter métrica proporcional perto de um alvo.
- **Palavras decisivas:** *imprevisível*, *manter CPU em 50%*.
- **A:** correta; target tracking funciona como um termostato.
- **B:** scheduled responde a calendário, não à variação imprevisível.
- **C:** lifecycle hook pausa transições de instância.
- **D:** termination policy escolhe membros durante scale-in.
- **Regra reutilizável:** “manter métrica em X” → target tracking.
- **Variação:** use margem razoável e default warmup coerente.
- **Aulas:** 85–86.
- **Referência:** [Target tracking](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html).

## B07-06 — Resposta C

- **Requisito central:** antecipar pico calendarizado com lead time de boot.
- **Palavras decisivas:** *toda sexta*, *18:00*, *dez minutos*.
- **A:** esperar falha chega tarde e aumentar max não define desired.
- **B:** snapshot não adiciona capacidade de serving.
- **C:** correta; scheduled prepara capacidade e a dinâmica cobre variação.
- **D:** afinidade não cria instâncias.
- **Regra reutilizável:** pico conhecido → scheduled antes do pico; dinâmica pode
  coexistir.
- **Variação:** scheduled action pode definir desired, min e max.
- **Aulas:** 85–86.
- **Referência:** [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html).

## B07-07 — Answer B

- **Requisito central:** prevent bootstrap metrics from corrupting decisions.
- **Palavras decisivas:** *warmup*, *representative traffic*.
- **A:** warmup does not encrypt an AMI.
- **B:** correct; it prevents premature use of startup metrics and protects
  against early scale-in.
- **C:** Elastic IP allocation is independent.
- **D:** DNS TTL is unrelated to ASG metric aggregation.
- **Regra reutilizável:** default warmup ≈ time until capacity contributes
  representative metrics.
- **Variação:** a value that is too long delays scale-in; too short causes
  oscillation or over-scaling.
- **Aulas:** 85–86.
- **Referência:** [Default instance warmup](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-default-instance-warmup.html).

## B07-08 — Answer B,E

- **Requisito central:** replace an application-unhealthy target.
- **Palavras decisivas:** *EC2-healthy*, *fails ELB health*, *ASG uses ELB*.
- **A:** a load balancer never creates a database replica.
- **B:** correct; after the grace period, an ELB health failure can cause the
  ASG to mark and replace the instance.
- **C:** ACM does not renew AMIs.
- **D:** maximum capacity is configuration, not an automatic permanent reaction
  to one failed health check.
- **E:** correct; the grace period gives a newly launched application time to
  become healthy before replacement decisions.
- **Regra reutilizável:** application health should drive replacement → enable
  appropriate ELB health integration.
- **Variação:** grace period avoids replacing a target during valid bootstrap.
- **Aulas:** 83–84.
- **Referência:** [ASG health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html).

## B07-09 — Answer C

- **Requisito central:** replace a Multi-AZ fleet with an immutable image while
  preserving healthy capacity and providing observable rollback.
- **Palavras decisivas:** *90% healthy*, *auditable*, *checkpoints*, *CloudWatch
  alarm*, *rollback*.
- **A:** a separate blue/green group can be valid, but an all-at-once shift based
  only on EC2 status omits the required staged health checkpoints and automatic
  alarm rollback.
- **B:** setting the launch-template default affects future launches; waiting for
  organic replacement does not replace the entire fleet within an auditable
  rollout.
- **C:** correct; a versioned launch template and instance refresh provide the
  immutable desired state, controlled replacement, health thresholds,
  checkpoints, and rollback integration.
- **D:** in-place patching creates mutable fleet drift and does not prove that all
  serving instances were replaced from the approved immutable image.
- **Regra reutilizável:** new image → versioned template → controlled refresh →
  health/alarm rollback policy.
- **Variação:** a blue/green deployment using a separate group can provide
  stronger isolation when the release requires independent capacity validation.
- **Aulas:** 83–84.
- **Referência:** [Instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html).

## B07-10 — Answer A

- **Requisito central:** preserve cart state across load balancing, scale-out,
  deregistration, replacement, and Availability Zone failure.
- **Palavras decisivas:** *Multi-AZ ASG*, *state only in memory*, *different
  target*, *disposable*.
- **A:** correct; a shared durable database makes cart state independent of any
  compute target. A cache can improve latency, but it remains optional and is
  not the sole durable system of record.
- **B:** stickiness and draining can preserve affinity temporarily while a target
  is healthy; they do not recover RAM after replacement or zonal failure.
- **C:** a nonpersistent cache can evict or lose entries and therefore cannot be
  the only copy of business data that must be recoverable.
- **D:** peer replication to local root volumes couples state durability to a
  custom pair of replaceable instances and does not provide the required shared
  durable system of record.
- **Regra reutilizável:** elastic compute should be stateless; choose the external
  state service from consistency, durability, latency, and failure-scope needs.
- **Variação:** if state is truly disposable and reconstructible, a cache alone
  may fit; durable cart semantics require a database-backed design.
- **Aulas:** 83–86.
- **Referência:** [Reliability design principles](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html).

## Ação após a correção

Registre erro ou baixa confiança no
[Caderno de Erros](../Caderno_de_Erros_SAA-C03.md). Classifique a causa como
TLS, temporizador, capacidade, política de scaling, health ou estado.
