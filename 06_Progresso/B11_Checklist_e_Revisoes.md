# B11 — Checklist e revisões D+2/D+7

**Inicial:** 06/08/2026<br>
**D+2:** 08/08/2026<br>
**D+7:** 13/08/2026<br>
**Conteúdo:** S3, policy, versioning, replication, classes, lifecycle e eventos

## 1. Estudo inicial

- [ ] [aulas 128–149 + Q09/Q10](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b11);
- [ ] [capítulo](../03_Guia_do_Estudante/Capitulos/B11_S3_Seguranca_Versioning_Replication_Classes_e_Eventos.md);
- [ ] [LAB](../05_Laboratorios/LAB_B11_S3_Versioning_Lifecycle_e_Cleanup.md) com cleanup;
- [ ] [questões](../04_Questoes_e_Revisoes/Blocos/B11_Questoes.md) antes do [gabarito](../04_Questoes_e_Revisoes/Blocos/B11_Gabarito.md);
- [ ] Caderno de Erros atualizado.

**Q09:** ____% · **Q10:** ____% · **Autorais:** ____/10 · **Tempo:** ____.

### Evidência mínima

- [ ] BPA/ownership privados;
- [ ] duas versions e marker observados;
- [ ] marker removido/restauração validada;
- [ ] lifecycle current/noncurrent/multipart;
- [ ] SRR/CRR/Batch comparados;
- [ ] classes por acesso/retrieval/AZ/custo;
- [ ] evento idempotente desenhado;
- [ ] Batch/Lens explicados;
- [ ] todas as versions/markers removidos;
- [ ] zero bucket B11.

## 2. D+2 — 08/08/2026

Sem consulta:

1. resolva allow/deny/BPA;
2. recupere key com delete marker;
3. escolha CRR e Batch Replication;
4. compare oito classes;
5. escreva lifecycle version-aware;
6. explique Requester Pays;
7. desenhe evento idempotente;
8. diferencie Batch Operations/Storage Lens.

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

## 3. D+7 — 13/08/2026

Projete data lake com acesso privado, versioning, CRR para novos/históricos,
classes/lifecycle, notifications e job de tags em bilhões de objects. Inclua
falha de AZ, duplicação de evento e cleanup.

- **Itens:** ____/10
- **Tempo:** ____
- **Confiança:** alta / média / baixa
- **Classe que confundi:**
- **Resíduo de versioning:**
- **Regra de idempotência:**
- **Próxima ação:**

## 4. Critério de encerramento

- [ ] autorais ≥ 8/10;
- [ ] D+2 ≥ 7/8;
- [ ] D+7 ≥ 9/10;
- [ ] bucket/object actions e ARNs corretos;
- [ ] live replication e Batch não confundidos;
- [ ] lifecycle inclui noncurrent;
- [ ] cleanup version-aware confirmado;
- [ ] zero recurso B11.

Se falhar, revise somente a dimensão responsável e repita em 24 horas. Não deixe
bucket versionado como “temporário”; confirme versions e markers vazios.
