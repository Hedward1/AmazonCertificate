# B24 — Custos de rede, disaster recovery, migração e arquiteturas integradas

**Data planejada:** 21/08/2026<br>
**Nível:** iniciante absoluto<br>
**Comece pelas aulas da Udemy:** [roteiro B24 — aulas 346–366](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b24); Nenhuma aula é pulada.<br>
**Quizzes:** Q24, Q25 e Q26<br>
**Domínios oficiais:** 2 — Resilient; 3 — High-Performing; 4 — Cost-Optimized<br>
**Tarefas:** 2.2, 3.5 e 4.4 principais; tarefas integradas secundárias<br>
**Pré-requisito:** B23 — redes avançadas

## 1. Objetivos de aprendizagem

1. Definir RTO e RPO.
2. Comparar quatro estratégias de DR.
3. Escolher AWS DRS.
4. Escolher DMS e seus modos.
5. Escolher MGN.
6. Explicar AWS Backup.
7. Planejar migração de grande dataset.
8. Avaliar custos de rede.
9. Posicionar Network Firewall.
10. Integrar eventos, cache, HPC e HA.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 346–350 | Concluir VPC, custos e Network Firewall |
| 351–361 | DR e migração; somente arquitetura |
| 362–366 | Arquiteturas integradas |
| Q24–Q26 | Fazer no timebox; excedente vai ao início do B25 |

Use aulas, capítulo, laboratório e questões nessa ordem. Não copie credenciais nem crie recursos pagos para reproduzir telas.

**Atualização da aula 360:** trate Snowball Edge como conteúdo legado. O serviço não aceita novos clientes desde 07/11/2025 e terá suporte encerrado nas Regions comerciais após 31/12/2026. Para uma decisão nova, avalie DataSync/Direct Connect para transferência online e, para transporte físico, Data Transfer Terminal (clientes Enterprise e locais suportados) ou uma solução AWS Partner.

## 3. Vocabulário essencial

| Termo | Significado |
|---|---|
| RTO | tempo máximo para restaurar |
| RPO | perda de dados aceitável medida em tempo |
| failover | mudança para ambiente de recuperação |
| failback | retorno controlado |
| pilot light | núcleo ativo, aplicação exige ações |
| warm standby | cópia completa reduzida e funcional |
| CDC | captura contínua de mudanças |
| cutover | troca definitiva para destino |
| recovery point | cópia recuperável |
| data plane | operações que servem tráfego |

## 4. Modelo mental

1. Identifique o requisito.
2. Marque restrições.
3. Determine escopo.
4. Avalie segurança.
5. Avalie resiliência.
6. Avalie performance.
7. Compare operação e custo.
8. Elimine violações.

## 5. Fundamentos e decisões

### 5.1 Ponto 1

RTO mede tempo de recuperação.
### 5.2 Ponto 2

RPO mede perda de dados aceitável.
### 5.3 Ponto 3

RTO guia capacidade pronta e automação.
### 5.4 Ponto 4

RPO guia frequência de backup ou replicação.
### 5.5 Ponto 5

Backup and restore tem menor custo e maior recuperação.
### 5.6 Ponto 6

Pilot light mantém núcleo e dados ativos.
### 5.7 Ponto 7

Pilot light precisa ligar ou implantar componentes no evento.
### 5.8 Ponto 8

Warm standby já funciona em escala reduzida.
### 5.9 Ponto 9

Multi-site active active serve tráfego em ambos ambientes.
### 5.10 Ponto 10

Menor RTO e RPO tende a maior custo e complexidade.
### 5.11 Ponto 11

Multi-AZ não é o mesmo que multi-Region DR.
### 5.12 Ponto 12

Backup concluído não prova restore.
### 5.13 Ponto 13

Testes de failover e failback são essenciais.
### 5.14 Ponto 14

Elastic Disaster Recovery replica servidores para staging.
### 5.15 Ponto 15

DRS atende recuperação contínua de servidores.
### 5.16 Ponto 16

Application Migration Service atende lift-and-shift para EC2.
### 5.17 Ponto 17

DMS migra e replica dados de bancos e data stores.
### 5.18 Ponto 18

DMS full load move o estado inicial.
### 5.19 Ponto 19

DMS CDC replica mudanças contínuas.
### 5.20 Ponto 20

Full load mais CDC reduz downtime.
### 5.21 Ponto 21

Conversão de engine exige schema e código avaliados.
### 5.22 Ponto 22

DMS não converte magicamente toda stored procedure.
### 5.23 Ponto 23

AWS Backup centraliza plans, vaults e retenção.
### 5.24 Ponto 24

Recovery points podem sobreviver ao recurso original.
### 5.25 Ponto 25

DataSync automatiza transferências de storage suportado.
### 5.26 Ponto 26

Para novos projetos em 2026, Data Transfer Terminal atende transferência em local físico de alta velocidade para clientes Enterprise elegíveis; AWS Partners podem atender outros casos offline. Snowball Edge é legado e está em encerramento.
### 5.27 Ponto 27

Tempo de rede depende de bits e throughput efetivo.
### 5.28 Ponto 28

Direct Connect pode melhorar previsibilidade de migração.
### 5.29 Ponto 29

Custos podem existir em cross-AZ e cross-Region.
### 5.30 Ponto 30

NAT, TGW, endpoints e firewall processam e cobram dados.
### 5.31 Ponto 31

Gateway endpoint pode evitar NAT para S3 e DynamoDB.
### 5.32 Ponto 32

Network Firewall é firewall stateful gerenciado da VPC.
### 5.33 Ponto 33

Network Firewall não substitui WAF HTTP.
### 5.34 Ponto 34

EventBridge roteia, SQS bufferiza e consumidores processam.
### 5.35 Ponto 35

CloudFront e ElastiCache atendem camadas de cache diferentes.
### 5.36 Ponto 36

HPC pode usar cluster placement e EFA.
### 5.37 Ponto 37

EC2 HA usa múltiplas AZs e estado externo.

## 6. Tabela de decisão

| Requisito | Escolha | Motivo |
|---|---|---|
| Horas e baixo custo | Backup restore | infraestrutura no evento |
| Núcleo ativo | Pilot light | ligar aplicação |
| Cópia reduzida funcional | Warm standby | apenas escalar |
| Quase zero RTO RPO | Multi-site | ambos ativos |
| DR de servidores | AWS DRS | replicação contínua |
| Lift-and-shift | AWS MGN | migração de servidor |
| Banco com CDC | AWS DMS | dados e mudanças |
| Política de backup | AWS Backup | governança central |
| Dispositivos portáteis e rede insuficiente | Data Transfer Terminal | instalação física de alta velocidade; validar elegibilidade e local |
| Firewall stateful VPC | Network Firewall | inspeção de rede |

## 7. Cenários resolvidos


### Cenário resolvido 1 — RTO de oito horas

- **Contexto:** Aplicação tolera horas de indisponibilidade.
- **Requisito:** RPO de quatro horas e menor custo.
- **Decisão:** Backup cross-Region, IaC e restore testado.
- **Por quê:** Objetivos relaxados permitem backup and restore.
- **Por que não:** Warm standby custa sem necessidade.
- **Trade-off:** RTO depende de quotas, deploy e restore.
- **Validação:** Executar game day e medir o tempo.
- **Custo/cleanup:** Backups, cópias e storage cobram.
- **Variação:** Automação reduz RTO sem manter compute.

### Cenário resolvido 2 — Oracle para Aurora

- **Contexto:** Empresa muda de engine.
- **Requisito:** Downtime mínimo.
- **Decisão:** Conversão de schema mais DMS full load e CDC.
- **Por quê:** Move estado e mudanças enquanto origem opera.
- **Por que não:** DMS sozinho não converte todo código.
- **Trade-off:** Heterogeneidade exige testes funcionais.
- **Validação:** Reconciliar contagens, dados e lag antes de cutover.
- **Custo/cleanup:** Replication compute e transferência cobram.
- **Variação:** Migração homogênea pode usar ferramentas nativas gerenciadas.

### Cenário resolvido 3 — Minutos de RTO

- **Contexto:** Comércio precisa recuperar rapidamente.
- **Requisito:** Cópia completa capaz de servir carga reduzida.
- **Decisão:** Warm standby.
- **Por quê:** Ambiente já está funcional e só precisa escalar.
- **Por que não:** Pilot light exige mais ações.
- **Trade-off:** Capacidade permanente custa.
- **Validação:** Testar DNS, escala, dados e failback.
- **Custo/cleanup:** Compute e dados de réplica contínuos.
- **Variação:** Active active reduz mais RTO com maior complexidade.

## 8. Fluxo de projeto

1. Definir evento de desastre.
2. Definir RTO.
3. Definir RPO.
4. Classificar dependências.
5. Escolher estratégia.
6. Mapear dados e replicação.
7. Mapear identidade e chaves.
8. Mapear DNS e tráfego.
9. Verificar quotas na Region de DR.
10. Criar runbook.
11. Executar game day.
12. Medir e corrigir.

## 9. Custos e cleanup

- Não criar DMS replication instance.
- Não criar DRS ou MGN staging.
- Não criar Network Firewall.
- Não duplicar ambiente multi-Region.
- Replicação e cross-Region cobram.
- Standby cobra capacidade ativa.
- Backups e recovery points persistem.
- Inclua testes periódicos no custo.

Faça inventário antes e depois. Exclua apenas recursos criados pelo bloco.

## 10. Armadilhas

- RTO e RPO não são sinônimos.
- HA e DR não são sinônimos.
- Warm standby já funciona.
- Pilot light exige ações.
- DMS move dados; MGN move servidores.
- DRS não é ferramenta de schema.
- Backup sem restore testado é insuficiente.
- DX não converte banco.
- Menor RTO custa mais.
- Network Firewall não é WAF.

## 11. Checklist

- [ ] Objetivos explicados sem consulta.
- [ ] Tabela reconstruída.
- [ ] Três cenários resolvidos.
- [ ] Trade-offs justificados.
- [ ] Custos identificados.
- [ ] Laboratório concluído.
- [ ] Dez questões respondidas.
- [ ] Erros registrados.
- [ ] D+2 e D+7 agendados.

## 12. Recuperação ativa

1. Defina RTO e RPO.
2. Ordene quatro estratégias.
3. Compare pilot light e warm.
4. Compare DRS, MGN e DMS.
5. Explique full load e CDC.
6. Desenhe failover e failback.
7. Estime tempo de 100 TB.
8. Liste hops cobrados.
9. Compare WAF e Network Firewall.
10. Projete HA EC2 multi-AZ.

## 13. Ligações

- Identidade limita o principal.
- Rede limita o caminho.
- Criptografia protege dados.
- Observabilidade fornece evidência.
- Resiliência atende objetivos.
- Performance deve ser medida.
- Custo inclui recursos ociosos.
- Simulados integram blocos.

## 14. Referências oficiais AWS

- [DR options](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
- [AWS DRS](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)
- [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
- [AWS MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
- [AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html)
- [Snowball Edge availability change](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html)
- [Snowball end-of-support notice](https://aws.amazon.com/snowball/)
- [Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
- [Data transfer pricing](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer)

**Referências verificadas em:** 01/08/2026.

## 15. Continue o bloco

- [Laboratório B24](../../05_Laboratorios/LAB_B24_Estrategias_DR_e_Migracao_em_Diagrama.md)
- [Questões B24](../../04_Questoes_e_Revisoes/Blocos/B24_Questoes.md)
- [Gabarito B24](../../04_Questoes_e_Revisoes/Blocos/B24_Gabarito.md)
- [Checklist e revisões B24](../../06_Progresso/B24_Checklist_e_Revisoes.md)
