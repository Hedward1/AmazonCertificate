# LAB B21 — Avaliação de políticas, KMS e Parameter Store

**Tempo:** 20 minutos<br>
**Modo:** simulação e leitura<br>
**Custo:** USD 0,00 esperado<br>
**Capítulo:** [abrir](../03_Guia_do_Estudante/Capitulos/B21_Organizations_IAM_Avancado_KMS_e_Parameter_Store.md)

## 1. Objetivos

1. Resolver implicit deny.
2. Resolver explicit deny.
3. Aplicar SCP conceitual.
4. Distinguir policies.
5. Analisar cross-account.
6. Desenhar envelope encryption.
7. Inspecionar KMS e parâmetros.
8. Evitar criar keys.

## 2. Resultado esperado

- Três cadeias de autorização.
- Fluxo cross-account.
- Envelope encryption.
- Contagens KMS e Parameter Store.
- Nenhuma key, parameter ou role criada.
- Custo esperado zero.

## 3. Custo

USD 0,00 esperado.
- Confira preços e Region.
- Recursos anexos podem cobrar.
- Não crie itens não previstos.
- O cleanup faz parte do laboratório.
- Não confunda recurso básico com conta gratuita.

## 4. Preflight

1. Confirme identidade não root.
2. Confirme Region.
3. Conte customer managed keys sem IDs.
4. Conte parameters sem nomes.
5. Não abra Create key.
6. Não crie Organization.
7. Não salve policy real.
8. Use recursos fictícios.
9. Não agende key deletion.
10. Não abra valores SecureString.

### Critério para prosseguir

- [ ] Identidade não root.
- [ ] Region confirmada.
- [ ] Inventário válido.
- [ ] Preço conferido.
- [ ] Cleanup reservado.

## 5. Arquitetura

- Principal faz request.
- Identity policy pode conceder.
- Resource policy pode conceder.
- Trust policy permite assume role.
- Boundary limita.
- SCP limita member account.
- Session policy limita sessão.
- Explicit Deny prevalece.
- Key policy controla KMS.
- CloudTrail audita.

## 6. Execução


### Etapa 1 — Allow e implicit deny

1. Considere role com S3 GetObject.
2. Considere bucket policy neutra.
3. Considere SCP permitindo.
4. Considere ausência de Deny.
5. Conclua Allow no resource correto.
6. Troque o resource.
7. Conclua implicit deny.
8. Registre palavra decisiva.

### Etapa 2 — Explicit deny

1. Considere AdministratorAccess.
2. Adicione SCP Deny para terminate.
3. Avalie a ação.
4. Conclua Deny.
5. Adicione outro Allow.
6. Confirme que não muda.
7. Explique que SCP não concede.
8. Registre member account.

### Etapa 3 — Cross-account

1. Desenhe conta A.
2. Desenhe role na conta B.
3. Adicione AssumeRole na origem.
4. Adicione trust no destino.
5. Adicione permissions mínima.
6. Use sessão temporária.
7. Restrinja conditions.
8. Evite access key.

### Etapa 4 — KMS e parâmetros

1. Desenhe data key.
2. Cifre dados com data key.
3. Cifre data key com KMS key.
4. Descarte plaintext key.
5. Conte keys.
6. Conte parameters.
7. Não abra SecureString.
8. Compare Secrets Manager.

## 7. Validação

- [ ] Três cadeias de autorização.
- [ ] Fluxo cross-account.
- [ ] Envelope encryption.
- [ ] Contagens KMS e Parameter Store.
- [ ] Nenhuma key, parameter ou role criada.
- [ ] Custo esperado zero.
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

- Resolver implicit deny.
- Resolver explicit deny.
- Aplicar SCP conceitual.
- Distinguir policies.
- Analisar cross-account.
- Desenhar envelope encryption.
- Inspecionar KMS e parâmetros.
- Evitar criar keys.

Justifique a escolha e as alternativas eliminadas.

## 12. Referências oficiais

- [IAM evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
- [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

**Verificado em:** 01/08/2026.
