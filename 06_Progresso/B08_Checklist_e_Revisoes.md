# B08 — Checklist e revisões D+2/D+7

**Estudo inicial:** 03/08/2026<br>
**D+2:** 05/08/2026<br>
**D+7:** 10/08/2026<br>
**Conteúdo:** RDS, Aurora, backup, segurança, Proxy e ElastiCache

## 1. Estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B08](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b08) | 87–100 + Q06 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B08_RDS_Aurora_RDS_Proxy_e_ElastiCache.md) | explicar objetivos | [ ] |
| [LAB](../05_Laboratorios/LAB_B08_Projeto_RDS_Privado_Aurora_Proxy_e_Cache.md) | diagrama e zero criação | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B08_Questoes.md) | 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B08_Gabarito.md) | justificar A–D | [ ] |
| Caderno de Erros | registrar baixa confiança | [ ] |

**Q06:** ____% · **Autorais:** ____/10 · **Tempo:** ____ · **Confiança baixa:** ____.

### Evidência mínima

- [ ] Multi-AZ clássico sem read no standby;
- [ ] read replica com endpoint/lag;
- [ ] Aurora writer/reader endpoints;
- [ ] PITR para recurso novo;
- [ ] SG-to-SG e DB privado;
- [ ] RDS Proxy separado de cache;
- [ ] TTL/invalidação definidos;
- [ ] portas reconhecidas;
- [ ] custos listados;
- [ ] inventário final igual ao inicial.

## 2. D+2 — 05/08/2026

Sem consulta, em 10 minutos:

1. compare Multi-AZ DB instance, Multi-AZ DB cluster e read replica;
2. desenhe endpoints Aurora;
3. explique PITR após exclusão lógica;
4. desenhe SG app → Proxy → DB;
5. escolha Proxy para connection storm;
6. implemente cache-aside verbalmente;
7. associe seis portas.

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

## 3. D+7 — 10/08/2026

Projete um banco de e-commerce com HA, relatórios, recuperação às 14:57,
conexões Lambda e catálogo cacheado. Selecione topologias, endpoints, segurança,
backup, Proxy/cache, TTL e cleanup.

- **Itens corretos:** ____/9
- **Tempo:** ____ min
- **Confiança:** alta / média / baixa
- **Palavra em inglês que atrasou:**
- **Trade-off de custo:**
- **Regra ainda fraca:**
- **Próxima ação:**

## 4. Critério de encerramento

- [ ] autorais ≥ 8/10;
- [ ] D+2 ≥ 6/7;
- [ ] D+7 ≥ 8/9;
- [ ] HA e read scaling nunca são trocados;
- [ ] restore, Proxy e cache têm funções distintas;
- [ ] portas não substituem autenticação;
- [ ] zero recurso B08.

Se falhar, revise somente a seção responsável, atualize o Caderno de Erros e
repita as questões em 24 horas. Não crie RDS/Aurora/cache pago para corrigir uma
lacuna conceitual.
