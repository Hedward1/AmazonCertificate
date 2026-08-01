# LAB B08 — Projeto RDS privado, Aurora, Proxy e cache

**Tempo:** 35 minutos<br>
**Aulas:** 87–100<br>
**Capítulo:** [B08](../03_Guia_do_Estudante/Capitulos/B08_RDS_Aurora_RDS_Proxy_e_ElastiCache.md)<br>
**Modo:** diagrama e console read-only; criação somente com estimativa aceita<br>
**Custo esperado do modo recomendado:** USD 0,00

## 1. Resultado esperado

Ao terminar, você deverá ter:

- diagrama de aplicação e banco em subnets privadas;
- comparação Single-AZ, Multi-AZ, read replica e Aurora;
- plano de backup/PITR e teste de restore;
- ficha de RDS Proxy e Secrets Manager;
- estratégia cache-aside com TTL e invalidação;
- inventário inicial e final igual;
- nenhum banco/cache criado no modo recomendado.

## 2. Conexão com o exame

| Evidência | Tarefa |
|---|---|
| banco por workload | 3.3 |
| Multi-AZ/failover/backup | 2.2 |
| KMS, SG e segredo | 1.3 |
| right-sizing/cache | 4.3 |

## 3. Preflight (5 min)

- [ ] identidade não root e Region confirmadas;
- [ ] orçamento e alertas ativos;
- [ ] inventário de RDS, Aurora, Proxy e ElastiCache;
- [ ] preços de RDS/Proxy/cache consultados;
- [ ] nenhuma credencial real será anotada;
- [ ] nenhuma tela `Create` será concluída no modo recomendado;
- [ ] recursos preexistentes são somente leitura.

Se optar por criação, confirme explicitamente na tela elegibilidade, backup,
storage, IPv4, monitoring e retenção. Um “free tier” pode não cobrir todos os
recursos associados.

## 4. Arquitetura (8 min)

```text
ALB public subnets
  → ASG application private subnets AZ-a/AZ-b
      → optional RDS Proxy
          → RDS Multi-AZ private DB subnet group
      → ElastiCache private subnet group
```

Regras:

- SG app recebe somente do ALB;
- SG DB recebe porta do motor somente do SG app/proxy;
- SG cache recebe 6379/11211 somente do SG app;
- DB subnet group cobre duas AZs;
- `Publicly accessible = No`;
- KMS encryption e TLS previstos;
- segredo referenciado, nunca embutido no user data.

## 5. Quatro cartões de decisão (10 min)

### Cartão A — RDS Multi-AZ

- motor: PostgreSQL;
- objetivo: failover;
- endpoint: estável logicamente;
- read no standby clássico: não;
- backup retention e janela: justificar;
- RTO/RPO: escrever requisito, não promessa.

### Cartão B — Read replica

- workload: relatórios;
- consistência: eventual/lag aceitável;
- endpoint próprio;
- promoção: consequência e reconexão;
- cross-Region: custo e DR.

### Cartão C — Aurora

- writer endpoint;
- reader endpoint;
- duas replicas em AZs diferentes;
- Serverless v2 min/max ACU conceitual;
- failover tier/prioridade;
- custo versus RDS tradicional.

### Cartão D — Proxy + cache

- Lambda abre conexões curtas → RDS Proxy;
- query repetida de catálogo → cache-aside;
- TTL: 5 min, com justificativa;
- invalidar após atualização;
- cache miss/stampede e fallback ao DB;
- pinning a observar no Proxy.

## 6. Walkthrough read-only (7 min)

Abra **RDS → Create database** e localize, sem concluir: engine, template,
availability, credentials, instance class, storage, connectivity, KMS, backup e
deletion protection. Abra telas de Aurora, Proxy e ElastiCache e identifique
subnet groups/SG. Cancele todas.

Não copie endpoint, ARN, VPC ID, account ID ou secret. Registre somente opções e
nomes genéricos.

## 7. Validação (3 min)

- [ ] Multi-AZ não foi descrito como read scaling clássico;
- [ ] replica lag foi considerado;
- [ ] restore cria recurso/endpoint novo;
- [ ] Proxy resolve conexões, cache resolve leituras repetidas;
- [ ] nenhuma porta está aberta à internet;
- [ ] inventário não mudou.

## 8. Cleanup seguro (2 min)

No modo recomendado, feche telas e sessão: nada a excluir. Se algo B08 foi
criado acidentalmente, pare, confirme tags e dependências, desabilite deletion
protection somente no recurso de laboratório e exclua sem snapshot final apenas
se não houver dado. Depois audite snapshots manuais/automáticos retidos, Proxy,
Secrets, subnet/parameter groups e cache. Nunca exclua recurso preexistente.

## 9. Solução de problemas

| Sintoma | Verificação |
|---|---|
| app não conecta | DNS, SG, rota, porta, TLS e credencial |
| failover demora no cliente | DNS caching, reconnect/backoff, transação |
| reader mostra dado antigo | replica lag |
| Proxy não multiplexa | session pinning/transação |
| cache sobrecarrega DB | TTL simultâneo, stampede, hot key |
| exclusão bloqueada | deletion protection/ownership |

## 10. Referências oficiais

- [Creating an RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)
- [Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html)
- [Aurora endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoints.html)
- [RDS security](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html)
- [RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)
- [ElastiCache caching strategies](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html)
