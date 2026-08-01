# LAB B24 — Estratégias de DR e migração em diagrama

**Tempo:** 20 minutos<br>
**Modo:** diagrama e tabela<br>
**Custo:** USD 0,00 esperado<br>
**Capítulo:** [abrir](../03_Guia_do_Estudante/Capitulos/B24_Custos_de_Rede_DR_Migracao_e_Arquiteturas_Integradas.md)

## 1. Objetivos

1. Definir RTO e RPO.
2. Comparar quatro estratégias.
3. Desenhar pilot light.
4. Desenhar warm standby.
5. Escolher DRS, MGN ou DMS.
6. Planejar full load e CDC.
7. Criar runbook.
8. Estimar custo sem provisionar.

## 2. Resultado esperado

- Tabela DR preenchida.
- Dois diagramas.
- Matriz de migração.
- Runbook de doze passos.
- Nenhum recurso criado.
- Custo zero.

## 3. Custo

USD 0,00 esperado.
- Confira preços e Region.
- Recursos anexos podem cobrar.
- Não crie itens não previstos.
- Cleanup faz parte do laboratório.
- Não confunda read-only com ausência de recursos preexistentes.

## 4. Preflight

1. Confirme identidade não root.
2. Confirme Region.
3. Conte DMS replication resources.
4. Conte DRS source servers.
5. Conte MGN source servers.
6. Não inicie setup.
7. Não crie replication instance.
8. Não habilite staging.
9. Não copie dados.
10. Prepare cronômetro.

### Critério para prosseguir

- [ ] Identidade não root.
- [ ] Region confirmada.
- [ ] Inventário válido.
- [ ] Preço conferido.
- [ ] Cleanup reservado.

## 5. Arquitetura

- Primary Region ativa.
- Recovery Region passiva.
- DNS controlando failover.
- Dados replicados conforme RPO.
- IaC em ambas Regions.
- Identidade e chaves preparadas.
- Quotas validadas.
- Observabilidade em ambos lados.
- Runbook versionado.
- Failback planejado.

## 6. Execução


### Etapa 1 — Tabela DR

1. Crie colunas estratégia, estado, RTO, RPO e custo.
2. Preencha backup restore.
3. Preencha pilot light.
4. Preencha warm standby.
5. Preencha active active.
6. Ordene por custo.
7. Ordene por velocidade.
8. Escreva um risco por opção.

### Etapa 2 — Diagramas

1. Desenhe pilot light.
2. Mantenha dados e núcleo.
3. Marque componentes desligados.
4. Desenhe warm standby.
5. Mantenha stack completa reduzida.
6. Adicione DNS failover.
7. Adicione observabilidade.
8. Adicione failback.

### Etapa 3 — Migração

1. Servidor lift-and-shift aponta para MGN.
2. DR contínuo de servidor aponta para DRS.
3. Banco aponta para DMS.
4. Adicione schema conversion quando engine muda.
5. Adicione full load.
6. Adicione CDC.
7. Adicione validação.
8. Adicione cutover.

### Etapa 4 — Runbook

1. Declare desastre.
2. Congelar mudanças.
3. Validar réplica.
4. Promover dados.
5. Escalar compute.
6. Atualizar routing.
7. Executar smoke tests.
8. Comunicar.
9. Monitorar.
10. Planejar failback.
11. Reconciliar dados.
12. Registrar tempos.

## 7. Validação

- [ ] Tabela DR preenchida.
- [ ] Dois diagramas.
- [ ] Matriz de migração.
- [ ] Runbook de doze passos.
- [ ] Nenhum recurso criado.
- [ ] Custo zero.
- [ ] AccessDenied não virou zero.
- [ ] Nenhum dado sensível foi copiado.
- [ ] Inventário final comparado.

## 8. Cleanup

1. Nenhum recurso novo deveria existir.
2. Feche assistentes.
3. Não exclua preexistentes.
4. Repita contagens.
5. Investigue diferenças.
6. Remova notas locais sensíveis.
7. Encerre autenticação.
8. Confirme custo.
9. Registre limitações.
10. Marque cleanup.

### Checklist de cleanup

- [ ] Nenhum recurso novo.
- [ ] Preexistentes preservados.
- [ ] Inventário final válido.
- [ ] Sessão encerrada.

## 9. Tratamento de falhas

- AccessDenied é não verificado.
- Region errada exige voltar.
- Não altere preexistentes.
- Contagem mudou: investigue.
- Login expirado: renove pela mesma rota.
- Preço indisponível: permaneça read-only.
- Dúvida de propriedade: não exclua.
- Timeout: priorize cleanup.

## 10. Evidência permitida

Registre Region, modo, contagens, decisões, custo e cleanup.

Não registre:
- account ID ou ARN.
- access key, secret ou token.
- IDs, IPs ou nomes preexistentes.
- conteúdo de logs ou secrets.
- screenshots sensíveis.

## 11. Conexão com o exame

- Definir RTO e RPO.
- Comparar quatro estratégias.
- Desenhar pilot light.
- Desenhar warm standby.
- Escolher DRS, MGN ou DMS.
- Planejar full load e CDC.
- Criar runbook.
- Estimar custo sem provisionar.

Justifique a escolha e as alternativas eliminadas.

## 12. Referências oficiais

- [DR options](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
- [AWS DRS](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)
- [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
- [AWS MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

**Verificado em:** 01/08/2026.
