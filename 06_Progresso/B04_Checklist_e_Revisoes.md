# B04 — Checklist e revisões D+2/D+7

**Estudo inicial:** 29/07/2026  
**D+2:** 31/07/2026  
**D+7:** 05/08/2026  
**Conteúdo:** endereçamento do EC2, ENIs, placement groups, hibernação, EBS,
snapshots e AMIs

## 1. Conclusão do estudo inicial

| Atividade | Critério | Estado |
|---|---|---|
| [Aulas B04](../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b04) | concluir 47–60 e usar o tratamento indicado no capítulo | [ ] |
| Quiz da seção 6 | fazer na Udemy e registrar somente resultado e erros | [ ] |
| [Capítulo B04](../03_Guia_do_Estudante/Capitulos/B04_IPs_ENI_Placement_Hibernation_EBS_Snapshots_e_AMI.md) | explicar os objetivos sem consulta | [ ] |
| [Laboratório B04](../05_Laboratorios/LAB_B04_Inventario_EC2_ENI_EBS_e_AMI.md) | concluir o inventário read-only e confirmar zero mudanças | [ ] |
| [Questões B04](../04_Questoes_e_Revisoes/Blocos/B04_Questoes.md) | responder as 10 antes de abrir o gabarito | [ ] |
| [Gabarito B04](../04_Questoes_e_Revisoes/Blocos/B04_Gabarito.md) | justificar por que cada alternativa está certa ou errada | [ ] |
| Caderno de Erros | registrar erros e acertos de baixa confiança | [ ] |
| Auditoria | confirmar que nenhuma operação de criação ou exclusão foi executada | [ ] |

### Resultado inicial

- **Quiz da Udemy:** ____%
- **Questões autorais:** ____ / 10
- **Respostas com confiança baixa:** ____
- **Tempo das questões:** ____ minutos
- **Laboratório concluído:** sim / não / somente diagrama
- **Inventário inicial igual ao final:** sim / não
- **Recursos criados no LAB B04:** zero / investigar
- **Tópico mais fraco:**
- **Regra que preciso recuperar:**

### Evidência mínima do laboratório

- [ ] identidade não root confirmada sem salvar account ID ou ARN;
- [ ] Region confirmada;
- [ ] inventário inicial obtido ou limitações de permissão registradas;
- [ ] nenhum comando de criação, alteração ou exclusão executado;
- [ ] placement groups resolvidos em diagrama;
- [ ] compatibilidade de hibernação inspecionada;
- [ ] escopo de volume, snapshot e AMI explicado;
- [ ] inventário final comparado ao inicial;
- [ ] sessão da CLI encerrada.

## 2. D+2 — 31/07/2026

Não releia o capítulo antes da tentativa. Use no máximo 10 minutos.

1. Complete de memória a tabela de private IPv4, public IPv4 automático,
   Elastic IP e IPv6 para reboot, stop/start, hibernate/start e terminate.
2. Explique por que uma instância com public IPv4 ainda pode não ser alcançável
   pela internet.
3. Desenhe uma ENI com private IPs, Elastic IP, security groups, MAC e
   source/destination check. O que pode ser movido para outra instância?
4. Escolha cluster, partition ou spread para HPC, Kafka e quatro instâncias
   críticas.
5. Compare reboot, stop, hibernate e terminate em relação a RAM, EBS, instance
   store e cobrança de compute.
6. Explique `DeleteOnTermination=true` no root e `false` em um data volume.
7. Por que snapshots são incrementais e, ainda assim, cada um restaura seu
   próprio ponto no tempo?
8. Explique como recuperar EBS em outra AZ e como usar uma AMI em outra Region.

### Registro D+2

| Item | Correto sem consulta? | Confiança | Correção necessária |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |
| 6 |  |  |  |
| 7 |  |  |  |
| 8 |  |  |  |

- **Resultado:** ____ / 8
- **Erros reabertos:**
- **Recursos B04 ainda iguais ao inventário inicial:** sim / não / não se aplica

## 3. D+7 — 05/08/2026

Resolva o cenário sem consultar. Use no máximo 12 minutos.

### Cenário

A company runs three EC2 workloads in one Region:

1. A tightly coupled HPC application needs the lowest possible network latency
   between its nodes in one Availability Zone.
2. A small control tier has four independent critical instances that should not
   share the same underlying hardware.
3. A stateful application is stopped every night. An external partner requires
   a fixed public IPv4 address. Its data volume must survive instance
   termination, and the company needs a recovery copy in another Availability
   Zone.

The company also wants to resume the stateful application's in-memory processes
after planned pauses and later launch its customized image in another Region.

Responda:

1. Qual placement strategy atende ao workload HPC?
2. Qual placement strategy atende ao control tier?
3. Qual limite clássico dessa segunda estratégia precisa ser lembrado?
4. Qual tipo de endereço atende à allowlist do parceiro e o que continua
   cobrando durante a pausa?
5. Que configuração preserva o data volume após terminate?
6. Como recuperar o conteúdo do volume em outra AZ?
7. Quais pré-requisitos principais permitem restaurar RAM e processos?
8. Como disponibilizar a imagem customizada em outra Region e qual resíduo deve
   ser auditado depois de deregister?

### Registro D+7

- **Itens corretos sem consulta:** ____ / 8
- **Tempo:** ____ minutos
- **Confiança:** alta / média / baixa
- **Palavras em inglês que atrasaram a leitura:**
- **Ainda confundo:**
- **Próxima ação:**

## 4. Critério de encerramento do B04

O bloco pode ser marcado como consolidado quando:

- as questões autorais atingirem pelo menos 8/10;
- o D+2 atingir pelo menos 7/8;
- o D+7 atingir pelo menos 7/8;
- não houver erro aberto sobre mudança de public IPv4 ou escopo de ENI;
- cluster, partition e spread forem escolhidos sem consulta;
- volume EBS, snapshot e AMI forem diferenciados por escopo e finalidade;
- `DeleteOnTermination` e o cleanup de snapshots estiverem claros;
- o inventário do LAB B04 não mostrar mudança provocada pelo exercício.

Se falhar, revise somente a seção correspondente, atualize o Caderno de Erros e
repita as questões erradas depois de 24 horas. Não crie uma instância apenas
para repetir um conceito que pode ser recuperado pelo diagrama.
