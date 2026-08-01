# B12 — Checklist e revisões D+2/D+7

**Estudo inicial:** 07/08/2026<br>
**D+2:** 09/08/2026 cairia no domingo; revisão transferida para **10/08/2026**<br>
**D+7:** 14/08/2026<br>
**Conteúdo:** S3 encryption e proteção, CloudFront e Global Accelerator

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B12](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b12) | concluir 150–171 | [ ] |
| Quizzes Q11–Q12 | responder e registrar somente resultado/erros | [ ] |
| [Capítulo](../03_Guia_do_Estudante/Capitulos/B12_S3_Seguranca_CloudFront_e_Global_Accelerator.md) | explicar decisões sem consulta | [ ] |
| [Laboratório](../05_Laboratorios/LAB_B12_S3_Presigned_URL_CORS_e_Arquitetura_Global.md) | URL temporária, bucket privado e cleanup | [ ] |
| [Questões](../04_Questoes_e_Revisoes/Blocos/B12_Questoes.md) | responder 10 antes do gabarito | [ ] |
| [Gabarito](../04_Questoes_e_Revisoes/Blocos/B12_Gabarito.md) | justificar A–D após responder | [ ] |
| Correção | justificar A–D e registrar baixa confiança | [ ] |
| Auditoria | nenhum objeto, versão, key, distribution ou accelerator residual | [ ] |

### Resultado inicial

- **Q11:** ____% — **Q12:** ____%
- **Questões autorais:** ____ / 10
- **Baixa confiança:** ____
- **Laboratório:** concluído / diagrama / pendente
- **Recursos residuais:** zero / investigar
- **Regra mais fraca:**

### Evidência mínima

- [ ] Block Public Access permaneceu habilitado;
- [ ] URL não foi registrada nem compartilhada;
- [ ] URL comum negada e URL assinada limitada pelo prazo;
- [ ] CORS foi separado de autorização;
- [ ] OAC e origem S3 privada foram desenhados;
- [ ] CloudFront e Global Accelerator foram comparados;
- [ ] atualização de S3 Object Lambda registrada;
- [ ] cleanup confirmado.

## 2. D+2 transferido — 10/08/2026

Sem reler, em até 10 minutos:

1. Reconstrua a tabela SSE-S3/SSE-KMS/DSSE-KMS/SSE-C/client-side.
2. Explique por que `s3:GetObject` pode não bastar em SSE-KMS.
3. Diferencie CORS, bucket policy e presigned URL.
4. Compare Versioning, MFA Delete e Object Lock compliance.
5. Desenhe CloudFront + OAC + S3 privado.
6. Escolha CloudFront ou Global Accelerator para três protocolos.

| Item | Correto sem consulta? | Confiança | Correção |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |

**Resultado D+2:** ____ / 6

## 3. D+7 — 14/08/2026

### Cenário

Uma plataforma distribui vídeos privados por HTTPS, aceita uploads diretos de
browser e opera um serviço UDP em duas Regions. Objetos regulados precisam de
auditoria de chave e retenção irredutível.

Responda em até 12 minutos:

1. Qual método de encryption oferece key policy e auditoria?
2. Como o browser recebe autorização temporária de upload sem access key?
3. Qual é o papel de CORS nesse fluxo?
4. Qual modo de Object Lock impede até root de apagar durante o prazo?
5. Como manter a origem S3 do vídeo privada e reduzir carga?
6. Qual serviço fornece IPs anycast para UDP?
7. Por que Object Lambda não deve ser uma dependência nova em 2026?
8. Quais quatro custos/resíduos devem ser auditados?

- **Corretos:** ____ / 8
- **Tempo:** ____ min
- **Confiança:** alta / média / baixa
- **Erros reabertos:**
- **Próxima ação:**

## 4. Critério de encerramento

- questões ≥ 8/10;
- D+2 ≥ 5/6 e D+7 ≥ 7/8;
- nenhuma confusão entre encryption e autorização;
- CloudFront/Global Accelerator escolhidos por protocolo e cache;
- Object Lock e presigned URL explicados sem consulta;
- zero recursos esquecidos.
