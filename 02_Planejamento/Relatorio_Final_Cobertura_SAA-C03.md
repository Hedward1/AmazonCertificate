# Relatório final de cobertura — AWS SAA-C03

**Branch auditada:** `agent/adicionar-roteiro-diario-udemy`

**Data da validação:** 01/08/2026
**Guia de referência:** [AWS Certified Solutions Architect – Associate
(SAA-C03)](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html)

## Decisão executiva

**O material está pronto para iniciar e sustentar o plano de estudo, mas o
estudante ainda não está pronto para realizar a prova hoje.**

O pacote cobre os 189 itens individuais de Knowledge/Skills do guia vigente,
contém teoria, aplicação, questões e revisão, e oferece três simulados autorais
com pesos próximos aos domínios oficiais. A decisão sobre marcar a prova depende
agora de evidência pessoal: concluir os laboratórios, manter o Caderno de Erros e
atingir resultado estável nas tentativas sem consulta. Como o perfil inicial é de
quem nunca trabalhou com AWS, a existência do material não substitui a prática.

Critério recomendado para mudar a decisão para **pronto para a prova**:

- concluir B01–B25 e os laboratórios previstos, sempre validando o cleanup;
- realizar SIM-A e SIM-C em 130 minutos, sem consulta, usando SIM-B como extra
  ou substituto conforme o fluxo planejado;
- obter pelo menos 80% em dois simulados consecutivos e nenhum domínio abaixo
  de 75%;
- revisar todos os erros e acertos de baixa confiança em D+2 e D+7.

Esse limiar é uma regra pedagógica do projeto, não uma pontuação oficial da AWS.

## Cobertura do guia oficial

A [matriz de competências](Matriz_Competencias_Oficiais_SAA-C03.csv) foi gerada
diretamente das quatro páginas oficiais do exame. Cada linha representa um item
individual de `Knowledge of` ou `Skills in`.

| Domínio | Peso oficial | Knowledge | Skills | Total | Cobertura completa | Parcial |
|---:|---:|---:|---:|---:|---:|---:|
| 1 — Secure Architectures | 30% | 15 | 17 | 32 | 32 | 0 |
| 2 — Resilient Architectures | 26% | 28 | 15 | 43 | 43 | 0 |
| 3 — High-Performing Architectures | 24% | 28 | 22 | 50 | 50 | 0 |
| 4 — Cost-Optimized Architectures | 20% | 36 | 28 | 64 | 64 | 0 |
| **Total** | **100%** | **107** | **82** | **189** | **189** | **0** |

`cobertura completa` só foi atribuída quando a linha possui teoria, aplicação,
evidência de questão e revisão D+2/D+7. Aplicação pode ser demonstrada por uma
comparação, um cenário resolvido ou um laboratório semanticamente pertinente.
Questões transversais podem servir a outra tarefa, mas somente quando o corpo da
questão cobre a competência — o rótulo primário da questão não basta. A matriz
também registra bloco, capítulo, seção, comparação, cenário, laboratório,
formatos de questão, fonte oficial, data e lacuna.

### Cobertura por tipo de competência

| Tipo | Total | Cobertura completa | Parcial |
|---|---:|---:|---:|
| Knowledge | 107 | 107 | 0 |
| Skill | 82 | 82 | 0 |
| **Total** | **189** | **189** | **0** |

### Cobertura por tarefa

| Tarefa | Knowledge | Skills | Total | Completas | Lacunas |
|---:|---:|---:|---:|---:|---:|
| 1.1 | 5 | 6 | 11 | 11 | 0 |
| 1.2 | 6 | 4 | 10 | 10 | 0 |
| 1.3 | 4 | 7 | 11 | 11 | 0 |
| 2.1 | 16 | 7 | 23 | 23 | 0 |
| 2.2 | 12 | 8 | 20 | 20 | 0 |
| 3.1 | 3 | 2 | 5 | 5 | 0 |
| 3.2 | 6 | 4 | 10 | 10 | 0 |
| 3.3 | 8 | 5 | 13 | 13 | 0 |
| 3.4 | 4 | 4 | 8 | 8 | 0 |
| 3.5 | 7 | 7 | 14 | 14 | 0 |
| 4.1 | 11 | 10 | 21 | 21 | 0 |
| 4.2 | 9 | 6 | 15 | 15 | 0 |
| 4.3 | 9 | 5 | 14 | 14 | 0 |
| 4.4 | 7 | 7 | 14 | 14 | 0 |

### Lacunas por dimensão

| Dimensão exigida | Competências sem evidência pertinente |
|---|---:|
| Teoria | 0 |
| Aplicação | 0 |
| Questão | 0 |
| Revisão D+2/D+7 | 0 |

Durante a auditoria, as parciais se concentraram inicialmente em dois padrões:
associações transversais que o roteamento não reconhecia e quatro lacunas
editoriais reais — segurança no ponto de ingestão, dimensionamento de storage,
Outposts/hybrid compute e disponibilidade por criticidade de workload. As
associações foram corrigidas sem fallback genérico; as quatro lacunas receberam
teoria, aplicação e questão próprias antes de mudar para `cobertura completa`.

## Banco autoral B01–B25

### Formato, tipo, dificuldade e idioma

| Dimensão | Categoria | Quantidade | Percentual |
|---|---|---:|---:|
| Formato | `single` | 190 | 76,0% |
| Formato | `multi-2` — `Choose TWO` | 45 | 18,0% |
| Formato | `multi-3` — `Select THREE` | 15 | 6,0% |
| Tipo | fundamental | 50 | 20,0% |
| Tipo | situacional | 113 | 45,2% |
| Tipo | integrada | 87 | 34,8% |
| Dificuldade | básica | 40 | 16,0% |
| Dificuldade | intermediária | 118 | 47,2% |
| Dificuldade | avançada | 92 | 36,8% |
| Idioma | português | 81 | 32,4% |
| Idioma | inglês | 169 | 67,6% |

As 60 questões multi-answer representam 24% do banco. Essa proporção e a
distribuição 20%/45%/35% são decisões pedagógicas internas; a AWS não publica
uma proporção oficial de formatos. Todas as questões multi-answer possuem cinco
ou seis alternativas, conjunto de respostas explícito e análise de cada opção.

### Distribuição por domínio e tarefa

| Domínio | Questões | Percentual do banco |
|---:|---:|---:|
| 1 | 59 | 23,6% |
| 2 | 50 | 20,0% |
| 3 | 118 | 47,2% |
| 4 | 23 | 9,2% |

| Tarefa | Associações de questão |
|---:|---:|
| 1.1 | 23 |
| 1.2 | 25 |
| 1.3 | 11 |
| 2.1 | 18 |
| 2.2 | 32 |
| 3.1 | 16 |
| 3.2 | 24 |
| 3.3 | 11 |
| 3.4 | 41 |
| 3.5 | 27 |
| 4.1 | 4 |
| 4.2 | 14 |
| 4.3 | 2 |
| 4.4 | 3 |

Uma questão associada a `2.1/3.4` é contabilizada nas duas tarefas; por isso a
tabela de tarefas soma 251 associações para 250 questões. O banco B01–B25 segue
a progressão do curso e é mais concentrado no domínio 3; ele não deve ser usado
como amostra estatística do exame. Os simulados finais corrigem essa assimetria
com os pesos oficiais aproximados.

## Lacunas prioritárias fechadas

| Serviço | Bloco | Evidência adicionada |
|---|---:|---|
| AWS AppSync | B17 | cápsula de decisão e questão situacional |
| AWS X-Ray | B20 | tracing, comparação e migração para OpenTelemetry |
| AWS Security Hub | B20 | agregação/correlação de findings e armadilhas |
| AWS Artifact | B20 | documentos do provedor versus evidência do cliente |
| AWS Audit Manager | B20 | assessment e coleta de evidências |
| AWS Resource Access Manager | B21 | compartilhamento de recursos entre contas/OUs |
| Amazon Detective | B22 | investigação e behavior graph |
| AWS Client VPN | B23 | acesso de usuários versus conexão de redes |
| AWS Compute Optimizer | B25 | rightsizing baseado em utilização |
| AWS Cost and Usage Report 2.0 | B25 | dados granulares via AWS Data Exports |

**Serviços prioritários faltantes:** nenhum dos dez itens solicitados.

Cada cápsula informa o problema resolvido, quando escolher, quando não escolher,
serviço semelhante, armadilha, cenário com resposta e referência oficial.

## Atualizações e afirmações voláteis revalidadas

| Tema | Estado validado em 01/08/2026 | Tratamento no material |
|---|---|---|
| Amazon QuickSight | o guia do exame agora cita Amazon QuickSuite; Quick Sight preserva as capacidades de BI | nomenclatura atualizada, mantendo o título histórico da aula |
| Lambda Durable Functions | execução durável com checkpoint/replay por até um ano | atualização relevante; não confundir com timeout normal de 15 minutos |
| Lambda MicroVMs | ambiente isolado, stateful e suspensível por até 8 horas | conteúdo profissional opcional; não memorizar APIs/quotas |
| Regional NAT Gateway | NAT regional expande por AZ e pode levar até 60 minutos para alcançar uma nova AZ | atualização relevante; núcleo continua sendo a decisão de egress/HA |
| Amazon Pinpoint | sem novos clientes desde 20/05/2025; suporte termina em 30/10/2026 | atualização relevante, com destinos de migração atuais |
| AWS Snowball Edge | sem novos clientes desde 07/11/2025; suporte comercial termina em 31/12/2026 | atualização relevante; não recomendar como solução nova genérica |
| Data Transfer Terminal | instalação física para clientes Enterprise, com dispositivos próprios e local suportado | corrigido; não é equipamento enviado nem substituto universal do Snowball |
| AWS X-Ray SDK/daemon | maintenance mode desde 25/02/2026 | recomendar OpenTelemetry para instrumentação nova |
| RDS Custom for Oracle | suporte termina em 31/03/2027 | aviso registrado no B08 |

Fontes oficiais principais:

- [Guia do domínio 3 — Amazon QuickSuite](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html)
- [Lambda Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms-launching.html)
- [Regional NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html)
- [Amazon Pinpoint end of support](https://docs.aws.amazon.com/pinpoint/latest/userguide/migrate.html)
- [Snowball Edge availability](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html)
- [Snowball end of support](https://aws.amazon.com/snowball/)
- [AWS Data Transfer Terminal](https://docs.aws.amazon.com/datatransferterminal/latest/userguide/what-is-dtt.html)
- [X-Ray SDK/daemon timeline](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-daemon-timeline.html)
- [RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html)

Datas, disponibilidade regional, preços e encerramentos devem ser conferidos
novamente perto da prova porque são fatos voláteis.

## Simulados finais

O [manifesto público](../04_Questoes_e_Revisoes/Simulados/manifesto_simulados.json)
define SIM-A, SIM-B e SIM-C. Cada simulado tem:

- 65 questões autorais em inglês e 130 minutos;
- 20/17/15/13 questões nos domínios 1/2/3/4;
- 49 `single`, 12 `multi-2` e 4 `multi-3`;
- 13 fundamentais, 29 situacionais e 23 integradas;
- 10 básicas, 35 intermediárias e 20 avançadas;
- todas as 14 tarefas, gabarito separado e relatório por domínio/tarefa.

Os bancos, cadernos, gabaritos e relatórios estão organizados e versionados em
`04_Questoes_e_Revisoes/Simulados/`. O README oferece navegação separada para
cada artefato e alerta contra spoilers. O practice exam da Udemy não foi
copiado nem exposto e continua reservado até a data do cronograma.

## Resultado dos validadores

Comandos de auditoria:

```powershell
python .\99_Ferramentas\scripts\gerar_matriz_competencias_oficiais.py --check
python .\99_Ferramentas\scripts\gerar_simulados.py --validate-only
python .\99_Ferramentas\scripts\validar_material_completo.py
```

**Resultado final: aprovado após as correções da auditoria.** A revisão
identificou e eliminou roteamento por simples substring, fallback genérico de
evidência, bloqueio indevido de evidência transversal e quatro lacunas
editoriais reais: segurança no ponto de ingestão, dimensionamento de storage,
Outposts/hybrid compute e disponibilidade por criticidade de workload.

No estado final, foram validados 25 blocos, 250 questões e respostas, 189
competências com cobertura completa e zero lacunas em teoria, aplicação,
questão ou revisão D+2/D+7, além de três simulados/195 questões autorais, 785
links locais, 145 arquivos editoriais, o cronograma e as marcações de conteúdo
opcional. O validador não usa número de linhas ou palavras como evidência de
cobertura. Ele também rejeita formatos de múltipla resposta inconsistentes,
títulos ou chaves duplicados, análise vazia de qualquer alternativa, perguntas
sobre o procedimento do curso, classificação integrada/avançada sem cenário
técnico suficiente e similaridade elevada entre quaisquer questões do banco.

A revisão para publicação também encontrou um viés crítico nos gabaritos: uma
estratégia cega pelas letras modais acertaria 86,2% do SIM-B e 96,9% do SIM-C.
As alternativas foram reordenadas, distratores excessivamente curtos foram
aprimorados e os três bancos passaram a ter posições simples balanceadas,
conjuntos múltiplos variados e limite para a pista de comprimento. O gerador
agora rejeita regressões desse tipo, usa hash JSON canônico independente de
CRLF/LF e confirma que questões, gabaritos e relatórios correspondem aos bancos.

## Riscos restantes

- Os relatórios de SIM-A/B/C ainda começam em branco; falta evidência real de
  desempenho do estudante.
- Como gabaritos e bancos estão publicados, abrir esses arquivos antes da
  tentativa compromete a validade do resultado; use somente `Questoes.md`.
- Os laboratórios precisam ser executados na conta do estudante e ter cleanup
  conferido; o pequeno orçamento mensal não autoriza deixar recursos ociosos.
- O domínio 4 é pouco representado no banco sequencial B01–B25. Use os três
  simulados calibrados e a matriz oficial para evitar esse viés.
- Nenhum banco autoral garante equivalência psicométrica com a prova real.

## Conclusão

**Prontidão do material: pronto.**

**Prontidão atual do estudante para realizar a prova: não pronto, pendente de
estudo, prática e resultados nos simulados.**
