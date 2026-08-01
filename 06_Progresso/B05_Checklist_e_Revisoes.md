# B05 — Checklist e revisões D+2/D+7

**Estudo inicial:** 30/07/2026<br>
**D+2:** 01/08/2026<br>
**D+7:** 06/08/2026<br>
**Conteúdo:** AMI prática, instance store, EBS, EFS, HA e introdução ao ELB

## 1. Estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B05](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b05) | aulas 61–71 e Q04 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B05_EBS_Instance_Store_EFS_e_Fundamentos_de_HA.md) | explicar objetivos sem consulta | [ ] |
| [LAB B05](../05_Laboratorios/LAB_B05_EBS_Snapshot_Restore_e_Projeto_EFS.md) | validar restore e zerar recursos | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B05_Questoes.md) | responder 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B05_Gabarito.md) | justificar A–D | [ ] |
| Caderno de Erros | registrar erro/baixa confiança | [ ] |

**Resultados:** Q04 ____%; autorais ____/10; confiança baixa ____; LAB completo/diagrama ____; recursos B05 restantes ____.

### Evidência mínima do laboratório

- [ ] identidade não root e Region confirmadas;
- [ ] estimativa de custo aceita antes da criação;
- [ ] recursos marcados exclusivamente com `Lab=B05`;
- [ ] AZ de volume e instância comparada;
- [ ] arquivo original criado e sincronizado;
- [ ] snapshot aguardado até `completed`;
- [ ] volume restaurado montado sem formatação;
- [ ] hash original igual ao restaurado;
- [ ] desenho EFS contém mount targets, SG e TCP 2049;
- [ ] instância, volumes e snapshot removidos;
- [ ] inventário final comparado ao inicial;
- [ ] nenhuma evidência contém ID, ARN, IP ou dado pessoal.

### Registro inicial detalhado

| Dimensão | Resultado |
|---|---|
| Diferença entre bloco e filesystem | |
| Tipo EBS escolhido para OLTP | |
| Risco do Multi-Attach | |
| EFS Regional versus One Zone | |
| Custo residual encontrado | |
| Tópico enviado ao Caderno de Erros | |

## 2. D+2 — 01/08/2026

Sem reler, em até 10 minutos:

1. desenhe EBS, instance store e EFS com escopo e persistência;
2. associe `gp3`, `io2`, `st1`, `sc1` a quatro workloads;
3. explique o risco de Multi-Attach com filesystem comum;
4. descreva encryption by default e customer managed KMS key;
5. escolha EFS Regional/One Zone e Elastic/Provisioned/Bursting;
6. diferencie HA, fault tolerance, escala horizontal e vertical.

**Resultado:** ____/6. **Erros reabertos:** ____________________. **Cleanup confirmado:** sim/não.

### Registro D+2

| Item | Correto sem consulta? | Confiança | Correção |
|---:|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

## 3. D+7 — 06/08/2026

Uma aplicação Linux roda em três AZs, compartilha arquivos, usa um banco crítico em EC2 e uma frota Spot com scratch reconstruível. Sem consulta, escolha storage para cada parte, tipo EBS do banco, modo/tipo EFS e plano de snapshot entre AZs. Explique custos residuais e por que Multi-Attach não substitui EFS.

**Itens corretos:** ____/8. **Tempo:** ____ min. **Regra ainda fraca:** ____________________.

Responda também:

1. O que ocorre com instance store em reboot e stop?
2. Como levar dados EBS a outra AZ?
3. Por que uma KMS key faz parte da disponibilidade?
4. Qual throughput mode EFS começa melhor para carga imprevisível?
5. Que recursos continuam cobrando depois de terminar EC2?

### Registro D+7

- **Confiança:** alta / média / baixa
- **Palavras em inglês que atrasaram:**
- **Erro repetido:**
- **Correção aplicada:**
- **Próxima recuperação:**

## 4. Critério de encerramento

- [ ] autorais ≥ 8/10;
- [ ] D+2 ≥ 5/6 e cenário D+7 ≥ 7/8;
- [ ] nenhuma confusão sobre escopo zonal do EBS;
- [ ] nenhuma confusão entre bloco, filesystem e objeto;
- [ ] cleanup final mostra zero recurso `Lab=B05`.

Se algum critério falhar, releia somente a seção correspondente, atualize o
Caderno de Erros e repita as questões erradas depois de 24 horas. Não recrie
recursos apenas para repetir cliques; use o diagrama quando a lacuna for
conceitual.
