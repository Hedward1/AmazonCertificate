# B09 — Checklist e revisões D+2/D+7

**Inicial:** 04/08/2026<br>
**D+2:** 06/08/2026<br>
**D+7:** 11/08/2026<br>
**Conteúdo:** DNS, Route 53, records, TTL, simple, weighted e latency

## 1. Estudo inicial

- [ ] [aulas 101–110](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b09);
- [ ] [capítulo](../03_Guia_do_Estudante/Capitulos/B09_DNS_Route53_Records_TTL_e_Routing.md);
- [ ] [LAB](../05_Laboratorios/LAB_B09_Observacao_DNS_e_Cenarios_Route53.md) sem criação;
- [ ] [questões](../04_Questoes_e_Revisoes/Blocos/B09_Questoes.md) antes do [gabarito](../04_Questoes_e_Revisoes/Blocos/B09_Gabarito.md);
- [ ] erros registrados.

**Autorais:** ____/10 · **Tempo:** ____ · **Confiança baixa:** ____.

### Evidência mínima

- [ ] A/AAAA/NS/SOA/MX/TXT consultados;
- [ ] TTL observado;
- [ ] fluxo recursivo desenhado;
- [ ] zone pública/privada diferenciada;
- [ ] Alias/CNAME comparados;
- [ ] canary weighted calculado;
- [ ] latency regional resolvido;
- [ ] DNS separado de load balancer;
- [ ] custos recorrentes listados;
- [ ] inventário inalterado.

## 2. D+2 — 06/08/2026

Sem consulta:

1. desenhe resolução DNS;
2. explique Alias no apex;
3. planeje migração com TTL antigo de 24h;
4. calcule pesos 9 e 1;
5. escolha latency para duas Regions;
6. explique private zone e conectividade;
7. diferencie DNS e ELB.

| Item | Correto? | Confiança | Correção |
|---:|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |

**Resultado:** ____/7. **Erro reaberto:** ____________________.

## 3. D+7 — 11/08/2026

Projete DNS para `example.com` no ALB, canary 5%, usuários entre duas Regions e
nome de banco privado. Inclua records, policies, TTL, health e custos.

- **Itens:** ____/8
- **Tempo:** ____
- **Confiança:** alta / média / baixa
- **Palavra em inglês:**
- **Armadilha repetida:**
- **Regra corrigida:**
- **Próxima ação:**

## 4. Critério de encerramento

- [ ] autorais ≥ 8/10;
- [ ] D+2 ≥ 6/7;
- [ ] D+7 ≥ 7/8;
- [ ] CNAME nunca é escolhido no apex;
- [ ] TTL é tratado como cache, não propagation mágica;
- [ ] weighted e latency não são confundidos;
- [ ] zero recurso B09.

Se falhar, revise somente o record/policy responsável e repita o cenário em 24
horas. Não registre domínio para treinar uma regra conceitual.

Antes de encerrar, explique em voz alta por que DNS seleciona um endpoint, mas
não acompanha nem encerra cada conexão de aplicação já estabelecida.
