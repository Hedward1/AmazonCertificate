# LAB B20 — CloudWatch, CloudTrail e Config sem alterações

**Tempo:** 20 minutos<br>
**Modo:** read-only<br>
**Custo:** USD 0,00 esperado<br>
**Capítulo:** [abrir](../03_Guia_do_Estudante/Capitulos/B20_Observabilidade_Auditoria_Config_e_Organizations.md)

## 1. Objetivos

1. Inspecionar métricas padrão.
2. Explicar ausência de memória padrão.
3. Inspecionar alarms sem alterar.
4. Consultar Event history.
5. Distinguir trail de history.
6. Verificar Config sem habilitar.
7. Desenhar regra EventBridge.
8. Concluir sem mudanças.

## 2. Resultado esperado

- Métrica padrão identificada.
- Atividade de API classificada.
- Tabela CloudWatch, CloudTrail e Config.
- Regra EventBridge desenhada.
- Nenhum alarm, trail ou Config criado.
- Inventário final igual ao inicial.

## 3. Custo

USD 0,00 esperado.
- Confira preços e Region.
- Recursos anexos podem cobrar.
- Não crie itens não previstos.
- O cleanup faz parte do laboratório.
- Não confunda recurso básico com conta gratuita.

## 4. Preflight

1. Confirme identidade não root.
2. Selecione a Region.
3. Conte alarms, trails e Config rules.
4. Não habilite Config.
5. Não crie trail.
6. Não habilite data events.
7. Não inicie Live Tail.
8. Não consulte logs volumosos.
9. Não copie eventos sensíveis.
10. Reserve tempo para validação.

### Critério para prosseguir

- [ ] Identidade não root.
- [ ] Region confirmada.
- [ ] Inventário válido.
- [ ] Preço conferido.
- [ ] Cleanup reservado.

## 5. Arquitetura

- CloudWatch Metrics mede comportamento.
- CloudWatch Logs armazena logs.
- Alarm avalia janela.
- EventBridge reage a eventos.
- CloudTrail registra API.
- Event history cobre management events recentes.
- Trail entrega eventos.
- Config registra estado.
- Config rule avalia compliance.
- Organizations agrega contas.

## 6. Execução


### Etapa 1 — CloudWatch

1. Abra Metrics.
2. Escolha namespace existente.
3. Observe statistic e period.
4. Identifique dimensions sem copiar valores.
5. Procure memória EC2 padrão.
6. Explique necessidade de agent.
7. Conte alarms.
8. Não crie nem edite.

### Etapa 2 — CloudTrail

1. Abra Event history.
2. Mantenha management events.
3. Escolha evento benigno.
4. Identifique event name.
5. Identifique event source.
6. Observe read-only.
7. Conte trails.
8. Não crie trail.

### Etapa 3 — Config

1. Abra Config sem setup.
2. Verifique recorder.
3. Conte rules.
4. Saia do wizard se não configurado.
5. Não aceite defaults.
6. Não crie conformance pack.
7. Não crie aggregator.
8. Marque não verificado quando necessário.

### Etapa 4 — EventBridge

1. Escolha evento EC2 stopped.
2. Defina source.
3. Defina bus.
4. Escreva pattern.
5. Escolha target conceitual.
6. Adicione retry.
7. Adicione DLQ.
8. Registre permission necessária.

## 7. Validação

- [ ] Métrica padrão identificada.
- [ ] Atividade de API classificada.
- [ ] Tabela CloudWatch, CloudTrail e Config.
- [ ] Regra EventBridge desenhada.
- [ ] Nenhum alarm, trail ou Config criado.
- [ ] Inventário final igual ao inicial.
- [ ] AccessDenied não virou zero.
- [ ] Nenhum segredo foi copiado.
- [ ] Inventário final comparado.

## 8. Cleanup

1. Nenhum recurso deveria ter sido criado.
2. Feche assistentes.
3. Não exclua preexistentes.
4. Repita contagens.
5. Investigue diferenças.
6. Remova rascunhos locais sensíveis.
7. Encerre autenticação.
8. Confirme custo zero.
9. Registre limitações.
10. Marque cleanup.

### Checklist de cleanup

- [ ] Recursos do lab removidos ou nenhum criado.
- [ ] Preexistentes preservados.
- [ ] Inventário final válido.
- [ ] Sessão encerrada.

## 9. Tratamento de falhas

- AccessDenied é não verificado.
- Region errada exige voltar.
- Não altere preexistentes.
- Dependência: remova só a dependência do lab.
- Contagem externa mudou: registre.
- Login expirado: renove pela mesma rota.
- Preço indisponível: permaneça read-only.
- Dúvida de propriedade: não exclua.

## 10. Evidência permitida

Registre Region, modo, contagens, decisões, custo e cleanup.

Não registre:
- account ID ou ARN.
- access key, secret ou token.
- IDs, IPs ou nomes preexistentes.
- conteúdo de logs ou secrets.
- screenshots sensíveis.

## 11. Conexão com o exame

- Inspecionar métricas padrão.
- Explicar ausência de memória padrão.
- Inspecionar alarms sem alterar.
- Consultar Event history.
- Distinguir trail de history.
- Verificar Config sem habilitar.
- Desenhar regra EventBridge.
- Concluir sem mudanças.

Justifique a escolha e as alternativas eliminadas.

## 12. Referências oficiais

- [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)
- [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)

**Verificado em:** 01/08/2026.
