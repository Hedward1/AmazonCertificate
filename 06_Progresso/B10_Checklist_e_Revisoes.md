# B10 — Checklist e revisões D+2/D+7

**Inicial:** 05/08/2026<br>
**D+2:** 07/08/2026<br>
**D+7:** 12/08/2026<br>
**Conteúdo:** Route 53 avançado, DNS híbrido, arquiteturas e Beanstalk

## 1. Estudo inicial

- [ ] [aulas 111–127 + Q07/Q08](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b10);
- [ ] [capítulo](../03_Guia_do_Estudante/Capitulos/B10_Route53_Avancado_Arquiteturas_Classicas_e_Beanstalk.md);
- [ ] [LAB](../05_Laboratorios/LAB_B10_Failover_DNS_Hibrido_e_Beanstalk.md) sem criação;
- [ ] [questões](../04_Questoes_e_Revisoes/Blocos/B10_Questoes.md) antes do [gabarito](../04_Questoes_e_Revisoes/Blocos/B10_Gabarito.md);
- [ ] Caderno de Erros atualizado.

**Q07:** ____% · **Q08:** ____% · **Autorais:** ____/10 · **Tempo:** ____.

### Evidência mínima

- [ ] primary/secondary e TTL;
- [ ] health check público versus alarm;
- [ ] geo/geo-proximity/IP-based/multivalue;
- [ ] delegação NS externa;
- [ ] inbound e outbound desenhados;
- [ ] arquitetura stateless Multi-AZ;
- [ ] bootstrap por AMI/user data/storage;
- [ ] web e worker Beanstalk;
- [ ] recursos subjacentes/custos;
- [ ] inventário inalterado.

## 2. D+2 — 07/08/2026

Sem consulta:

1. resolva active-passive;
2. compare quatro policies avançadas;
3. explique multivalue versus ELB;
4. delegue registrar externo;
5. desenhe inbound;
6. desenhe outbound;
7. decomponha arquitetura clássica;
8. explique Beanstalk web/worker.

| Item | Correto? | Confiança | Correção |
|---:|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

**Resultado:** ____/8. **Erro reaberto:** ____________________.

## 3. D+7 — 12/08/2026

Projete aplicação global com failover, conteúdo por país, DNS híbrido on-prem e
web tier Beanstalk Multi-AZ. Inclua health, TTL, state, backup, deployment e
custos.

- **Itens:** ____/10
- **Tempo:** ____
- **Confiança:** alta / média / baixa
- **Direção DNS que errei:**
- **Policy que confundi:**
- **Custo residual:**
- **Próxima ação:**

## 4. Critério de encerramento

- [ ] autorais ≥ 8/10;
- [ ] D+2 ≥ 7/8;
- [ ] D+7 ≥ 9/10;
- [ ] inbound/outbound corretos;
- [ ] policy escolhida pela palavra decisiva;
- [ ] Beanstalk não é tratado como gratuito/serverless;
- [ ] zero recurso B10.

Se falhar, revise apenas a policy/direção responsável e repita em 24 horas. Não
crie Resolver endpoint ou environment para corrigir vocabulário.

Antes de encerrar, narre o caminho completo de uma consulta on-premises até uma
private hosted zone e o caminho inverso de uma workload na VPC até
`corp.local`. Em seguida, liste os recursos cobrados que um environment
load-balanced do Beanstalk provisionaria na conta.
