# LAB B12 — S3 privado, URL pré-assinada, CORS e arquitetura global

**Timebox:** 20 minutos<br>
**Modo:** console ou AWS CLI; CloudFront e Global Accelerator somente em diagrama<br>
**Custo esperado:** centavos ou zero dentro das franquias; confirme preços da sua Region<br>
**Objetivo:** delegar um `GET` temporário sem tornar o bucket público e explicar CORS, OAC e aceleração global

**Capítulo:** [B12 — segurança do S3 e entrega global](../03_Guia_do_Estudante/Capitulos/B12_S3_Seguranca_CloudFront_e_Global_Accelerator.md)

## 1. Preflight — 3 min

- [ ] Entrar com identidade administrativa de laboratório, nunca root.
- [ ] Confirmar a Region e o orçamento/alerta de cobrança.
- [ ] Usar bucket descartável sem dados reais; não usar customer managed KMS key.
- [ ] Manter **Block Public Access** habilitado.
- [ ] Não copiar a URL pré-assinada para chat, Git, histórico compartilhado ou captura.

Registre sem salvar account ID/ARN:

```text
Region: __________
Identidade não root confirmada: sim / não
Bucket existente de laboratório: ____________________
Objetos/versões antes: __________
```

Se não houver bucket descartável, crie um bucket general purpose vazio com nome
globalmente único, Object Ownership `Bucket owner enforced`, Block Public
Access habilitado e default SSE-S3. Não desative controles para “fazer funcionar”.

## 2. Objeto e encryption — 4 min

1. Crie localmente `b12-teste.txt` com texto não sensível.
2. Faça upload para o prefixo `b12/`.
3. Em **Properties**, confirme `Server-side encryption: Amazon S3 managed keys`.
4. Em **Permissions**, confirme que o objeto e o bucket não são públicos.
5. Tente abrir o object URL comum em janela anônima: deve receber negação.

Evidência:

```text
Chave: b12/b12-teste.txt
Encryption observada: __________
Block Public Access: habilitado / investigar
Object URL anônima: negada / investigar
```

## 3. URL pré-assinada — 5 min

No CloudShell ou terminal autenticado, sem imprimir outras credenciais:

```powershell
$LabBucket = "SEU-BUCKET-DE-LAB"
$LabKey = "b12/b12-teste.txt"
aws s3 presign "s3://$LabBucket/$LabKey" --expires-in 120
```

Abra a URL apenas no navegador privado, confirme o download, espere dois
minutos e confirme que a mesma URL expira. Feche a aba e limpe o histórico. Não
registre a query string; anote somente sucesso/falha e horário.

```text
GET antes da expiração: sucesso / falha
GET depois da expiração: negado / investigar
A URL comum tornou-se pública? não / investigar
```

## 4. Revisão de CORS — 3 min

Não é preciso salvar uma configuração. Na aba **Permissions → CORS**, escreva
em rascunho o mínimo para um frontend fictício `https://app.example.com` fazer
`PUT` com uma URL pré-assinada:

```json
[
  {
    "AllowedOrigins": ["https://app.example.com"],
    "AllowedMethods": ["PUT"],
    "AllowedHeaders": ["content-type"],
    "ExposeHeaders": ["ETag"],
    "MaxAgeSeconds": 300
  }
]
```

Explique: quem autoriza o `PUT` é a assinatura/policy; CORS apenas permite que o
navegador exponha a resposta ao JavaScript da origin indicada.

## 5. Arquitetura — 2 min

Complete sem criar recursos:

```text
site/vídeos HTTP repetidos -> CloudFront -> OAC -> bucket S3 privado
jogo UDP multi-Region      -> Global Accelerator -> endpoints regionais
```

Marque: cache, protocolo, endpoint do cliente, health check e custo residual.

## 6. Cleanup e validação — 3 min

1. Exclua `b12/b12-teste.txt` e qualquer versão/delete marker criado.
2. Se o bucket foi criado exclusivamente para este LAB, esvazie todas as
   versões e exclua-o.
3. Remova CORS ou bucket policy que tenha salvado durante o teste.
4. Confirme que não há distribution, accelerator, access point ou KMS key nova.
5. Exclua o arquivo local `b12-teste.txt` e qualquer cópia baixada pelo teste.

```text
Objeto/versões removidos: sim / não
Bucket temporário removido ou reutilizável documentado: sim / não
CloudFront/Global Accelerator/KMS criados: zero / investigar
URL não foi registrada: confirmado / investigar
Arquivos locais de teste removidos: sim / não
```

## Critério de sucesso

- bucket permaneceu privado;
- URL funcionou somente no prazo;
- encryption foi identificada;
- CORS foi separado de autorização;
- CloudFront e Global Accelerator foram escolhidos corretamente;
- inventário final não contém recursos esquecidos.

## Conexão com o exame

O laboratório treina a distinção central dos cenários SAA-C03: CORS não é
autorização; encryption não torna um bucket privado; OAC protege a origem S3;
CloudFront é CDN HTTP com cache; Global Accelerator entrega IPs estáticos e
acelera TCP/UDP. Na correção, sublinhe o requisito que decidiu cada escolha.

## Referências oficiais

- [Presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
- [CORS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html)
- [OAC](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
