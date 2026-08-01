# LAB B25 — Auditoria final de custos e cleanup

**Tempo:** 10 minutos<br>
**Modo:** leitura e cleanup somente de recursos comprovadamente próprios<br>
**Custo:** USD 0,00 de recursos novos<br>
**Capítulo:** [abrir](../03_Guia_do_Estudante/Capitulos/B25_CloudFormation_Operacoes_Custos_e_Well_Architected.md)

## 1. Objetivos

1. Auditar Regions usadas.
2. Revisar Bills e Cost Explorer.
3. Procurar recursos cobrados comuns.
4. Verificar stacks.
5. Entender Retain.
6. Atribuir anomalias.
7. Preservar recursos desconhecidos.
8. Fechar curso sem practice exam.

## 2. Resultado esperado

- Checklist multi-Region.
- Custos atuais registrados sem valores sensíveis.
- Recursos do curso classificados.
- Stacks do curso tratadas.
- Nenhum recurso desconhecido removido.
- Practice exam não aberto.

## 3. Custo

USD 0,00 de recursos novos.
- Confira preços e Region.
- Recursos anexos podem cobrar.
- Não crie itens não previstos.
- Cleanup faz parte do laboratório.
- Não confunda read-only com ausência de recursos preexistentes.

## 4. Preflight

1. Confirme identidade não root.
2. Liste somente Regions usadas no curso.
3. Abra Billing console.
4. Não ative serviço pago.
5. Não use API Cost Explorer sem conferir preço.
6. Tenha nomes e tags dos próprios labs.
7. Não exclua por contagem.
8. Não agende key deletion.
9. Não abra practice exam.
10. Reserve evidência mínima.

### Critério para prosseguir

- [ ] Identidade não root.
- [ ] Region confirmada.
- [ ] Inventário válido.
- [ ] Preço conferido.
- [ ] Cleanup reservado.

## 5. Arquitetura

- Billing é global com dimensões.
- Recursos são regionais ou globais conforme serviço.
- Cost Explorer analisa tendência.
- Bills detalha serviço e Region.
- Anomaly Detection alerta.
- CloudFormation gerencia stack.
- Retain pode preservar recurso.
- Tags ajudam atribuição.
- CloudTrail ajuda autoria.
- Cleanup exige prova de propriedade.

## 6. Execução


### Etapa 1 — Custos

1. Abra Bills.
2. Filtre mês atual.
3. Identifique serviço com custo não zero.
4. Identifique Region.
5. Abra Cost Explorer se já habilitado.
6. Agrupe por service.
7. Agrupe por Region.
8. Não copie account ID.

### Etapa 2 — Recursos comuns

1. Confira EC2 running.
2. Confira public IPv4 e EIP.
3. Confira NAT gateways.
4. Confira interface endpoints.
5. Confira EBS e snapshots.
6. Confira RDS e caches.
7. Confira logs e buckets.
8. Confira secrets e customer managed keys.

### Etapa 3 — CloudFormation

1. Liste stacks próprias.
2. Filtre prefixos do curso.
3. Abra Resources.
4. Leia deletion policy no template conhecido.
5. Crie lista de dependências.
6. Exclua apenas stack autorizada do curso.
7. Aguarde DELETE_COMPLETE.
8. Verifique recursos Retain.

### Etapa 4 — Encerramento

1. Compare inventário inicial e final.
2. Classifique cada diferença.
3. Registre owner.
4. Registre próxima ação.
5. Não remova desconhecidos.
6. Encerre sessões.
7. Confirme custo esperado.
8. Não abra practice exam.

## 7. Validação

- [ ] Checklist multi-Region.
- [ ] Custos atuais registrados sem valores sensíveis.
- [ ] Recursos do curso classificados.
- [ ] Stacks do curso tratadas.
- [ ] Nenhum recurso desconhecido removido.
- [ ] Practice exam não aberto.
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

- Auditar Regions usadas.
- Revisar Bills e Cost Explorer.
- Procurar recursos cobrados comuns.
- Verificar stacks.
- Entender Retain.
- Atribuir anomalias.
- Preservar recursos desconhecidos.
- Fechar curso sem practice exam.

Justifique a escolha e as alternativas eliminadas.

## 12. Referências oficiais

- [Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)
- [CloudFormation stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)
- [DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html)
- [Tagging resources](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)

**Verificado em:** 01/08/2026.
