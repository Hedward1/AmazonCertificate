# B07 — Gabarito comentado

Abra depois das [questões B07](B07_Questoes.md).

## Resultado rápido

| ID | Resposta | Tarefa |
|---|---|---|
| B07-01 | B | 3.4 |
| B07-02 | A | 3.4 |
| B07-03 | B | 2.2 |
| B07-04 | D | 3.2 |
| B07-05 | A | 3.2 |
| B07-06 | C | 3.2 |
| B07-07 | B | 3.2 |
| B07-08 | D | 2.2 |
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

## B07-03 — Resposta B

- **Requisito central:** concluir requests durante remoção do target.
- **Palavras decisivas:** *scale-in*, *downloads ativos*, *não imediatamente*.
- **A:** DNS TTL não controla conexão já encaminhada ao target.
- **B:** correta; draining e shutdown precisam respeitar deregistration delay.
- **C:** snapshot protege disco, não request em andamento.
- **D:** rotação KMS não coordena target removal.
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

## B07-08 — Answer D

- **Requisito central:** replace an application-unhealthy target.
- **Palavras decisivas:** *EC2-healthy*, *fails ELB health*, *ASG uses ELB*.
- **A:** a load balancer never creates a database replica.
- **B:** ACM does not renew AMIs.
- **C:** the maximum is configuration, not an automatic permanent reaction.
- **D:** correct; the ASG can mark the instance unhealthy and replace it.
- **Regra reutilizável:** application health should drive replacement → enable
  appropriate ELB health integration.
- **Variação:** grace period avoids replacing a target during valid bootstrap.
- **Aulas:** 83–84.
- **Referência:** [ASG health checks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html).

## B07-09 — Answer C

- **Requisito central:** roll out a new immutable image safely.
- **Palavras decisivas:** *new AMI*, *existing fleet*, *safest rollout*.
- **A:** manual drift is not repeatable or fleet-wide.
- **B:** reboot does not replace an instance with another AMI.
- **C:** correct; versioned launch template plus controlled instance refresh is
  auditable and supports health criteria.
- **D:** a running instance's source AMI is not replaced by editing an ID.
- **Regra reutilizável:** new image → new template version → instance refresh.
- **Variação:** define minimum healthy percentage, checkpoints and rollback.
- **Aulas:** 83–84.
- **Referência:** [Instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-refresh.html).

## B07-10 — Answer A

- **Requisito central:** preserve required state while instances are replaced.
- **Palavras decisivas:** *state only in memory*, *horizontal scaling*.
- **A:** correct; external state lets instances remain disposable.
- **B:** ASG does not copy RAM.
- **C:** stickiness routes a client but does not recover state after failure.
- **D:** TLS protects transport and does not replicate session data.
- **Regra reutilizável:** elastic compute should be stateless; externalize
  durable/session state appropriately.
- **Variação:** use a database/cache based on consistency and durability needs.
- **Aulas:** 83–86.
- **Referência:** [Reliability design principles](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html).

## Ação após a correção

Registre erro ou baixa confiança no
[Caderno de Erros](../Caderno_de_Erros_SAA-C03.md). Classifique a causa como
TLS, temporizador, capacidade, política de scaling, health ou estado.
