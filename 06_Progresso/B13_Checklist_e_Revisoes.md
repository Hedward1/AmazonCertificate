# B13 — Checklist e revisões D+2/D+7

**Estudo inicial:** 08/08/2026<br>
**D+2:** 10/08/2026<br>
**D+7:** 15/08/2026<br>
**Conteúdo:** Snow, FSx, Storage Gateway, Transfer Family e DataSync

## 1. Estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b13) | 172–181 e Q13 | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B13_Storage_Hibrido_FSx_DataSync_Transfer_e_Snow.md) | reconstruir matriz de decisão | [ ] |
| [Laboratório](../05_Laboratorios/LAB_B13_Desenho_de_Migracao_e_Storage_Hibrido.md) | diagrama, cálculo e zero recursos | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B13_Questoes.md) | 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B13_Gabarito.md) | justificar A–D depois da tentativa | [ ] |
| Caderno de Erros | registrar erro e baixa confiança | [ ] |

- **Q13:** ____%
- **Questões:** ____ / 10
- **Mini-simulado do cronograma:** ____ / ____
- **Recursos criados:** zero / investigar
- **Maior confusão:**

### Evidência

- [ ] quatro famílias FSx comparadas;
- [ ] quatro tipos de gateway comparados;
- [ ] DataSync separado de Transfer Family;
- [ ] janela de rede calculada;
- [ ] mudança da Snow Family explicada;
- [ ] restrição do FSx File Gateway para novos clientes explicada;
- [ ] custos ociosos identificados;
- [ ] inventário final igual ao inicial.

## 2. D+2 — 10/08/2026

Sem consulta, em até 10 minutos:

1. Escolha FSx para Windows, HPC, NetApp e ZFS.
2. Escolha gateway para NFS/SMB, iSCSI cached/stored e VTL, distinguindo a
   restrição comercial específica do FSx File Gateway.
3. Compare DataSync e Transfer Family.
4. Explique quando a rede torna transferência física relevante.
5. Diga o que um novo cliente deve fazer ao considerar Snow em 2026.
6. Liste custos residuais de uma PoC híbrida.

| Item | Correto? | Confiança | Correção |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

**Resultado:** ____ / 6

## 3. D+7 — 15/08/2026

Uma empresa tem shares SMB/AD, render farm sobre S3, parceiros SFTP, software de
backup VTL e 100 TB em NFS para migrar. Responda:

1. Serviço para SMB/AD?
2. Serviço para processamento paralelo do dataset S3?
3. Serviço para parceiros SFTP?
4. Gateway para VTL?
5. Serviço para a cópia online NFS→S3?
6. Que cálculo antecede uma solução física?
7. Quais mudanças de disponibilidade afetam Snow Family e FSx File Gateway?
8. Que componentes devem ser excluídos após uma PoC?

- **Corretos:** ____ / 8
- **Tempo:** ____ min
- **Erros reabertos:**
- **Próxima ação:**

## 4. Critério de encerramento

Consolidado quando questões ≥ 8/10, D+2 ≥ 5/6, D+7 ≥ 7/8, todas as escolhas
são justificadas por interface e acesso, as atualizações da Snow Family e do
FSx File Gateway estão claras e nenhum recurso de storage caro foi criado.
