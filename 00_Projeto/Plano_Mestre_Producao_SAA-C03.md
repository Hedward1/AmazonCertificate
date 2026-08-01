# Plano Mestre e Especificação de Produção — AWS SAA-C03

**Projeto:** Certificação AWS Certified Solutions Architect – Associate  
**Exame-alvo:** SAA-C03  
**Período de preparação:** 25/07/2026 a 31/08/2026  
**Carga planejada:** 3 horas líquidas por dia, 6 dias por semana  
**Curso-base:** *AWS Certified Solutions Architect Associate SAA-C03*, de Stéphane Maarek, Udemy, aproximadamente 27 horas  
**Objetivo profissional:** aprovação na certificação e desenvolvimento de conhecimento aplicável a vagas internacionais.

---

## 1. Finalidade deste arquivo

Este documento é a fonte de orientação para o Codex criar e manter o material de estudo do projeto. Ele define:

- a arquitetura dos documentos;
- a hierarquia das fontes;
- a progressão pedagógica;
- a organização semanal;
- a forma de integrar as 27 horas do curso;
- as regras de produção da teoria, dos laboratórios e das questões;
- os critérios de qualidade, rastreabilidade e conclusão;
- os limites que impedem conteúdo desatualizado, superficial ou fora do escopo.

Este documento não é a apostila teórica nem o banco de questões. Ele é a especificação que governa a produção desses materiais.

---

## 2. Artefatos do projeto

O projeto terá três documentos principais e um registro auxiliar.

### Documento 1 — Plano Mestre e Especificação de Produção

É este arquivo. Sua função é organizar:

- conteúdo oficial;
- ordem de estudo;
- cronograma;
- carga horária;
- metodologia;
- regras para o Codex;
- critérios de domínio;
- controle de cobertura.

### Documento 2 — Guia do Estudante

É a apostila teórica. Deve ensinar cada tema de maneira autossuficiente, progressiva e orientada à decisão arquitetural.

Cada capítulo deverá conter:

1. identificação do tópico no Plano Mestre;
2. domínio e tarefa oficial relacionados;
3. objetivos de aprendizagem;
4. pré-requisitos;
5. aulas correspondentes do curso;
6. base e fundamentos;
7. aprofundamento;
8. aplicação arquitetural;
9. comparações entre serviços;
10. pelo menos dois cenários resolvidos quando o tema permitir;
11. laboratório, diagrama ou exercício prático;
12. mapa ou tabela de decisão;
13. armadilhas de prova;
14. resumo para revisão;
15. perguntas de recuperação ativa;
16. ligação com as questões correspondentes.

O Guia do Estudante poderá apontar para o curso, mas deverá ser compreensível sem depender do vídeo.

### Documento 3 — Apostila de Questões

É o material de treinamento e avaliação. As respostas devem ficar separadas das questões.

Cada bloco deverá conter:

- questões fundamentais;
- questões situacionais;
- questões arquiteturais integradas;
- revisão D+2;
- revisão D+7;
- simulado semanal;
- simulados finais de 65 questões;
- gabarito separado;
- explicação da resposta correta;
- análise individual das alternativas incorretas;
- identificação do tópico e domínio;
- dificuldade;
- fonte ou natureza da questão;
- classificação do erro.

### Registro auxiliar — Caderno de Erros

Deve registrar, para cada erro:

- questão e tópico;
- alternativa escolhida;
- resposta correta;
- motivo do erro;
- conceito faltante;
- palavra decisiva ignorada;
- regra de decisão correta;
- ação de correção;
- datas de revisão D+2 e D+7;
- resultado após a revisão.

Categorias mínimas do erro:

- lacuna conceitual;
- confusão entre serviços;
- interpretação do requisito;
- segurança;
- resiliência;
- desempenho;
- custo;
- esforço operacional;
- desatenção;
- informação desatualizada.

---

## 3. Hierarquia obrigatória das fontes

Quando houver conflito, usar esta ordem:

1. **Guia oficial vigente do exame SAA-C03:** define domínios, tarefas e escopo.
2. **Documentação oficial atual da AWS:** valida comportamento, limites, segurança, disponibilidade, desempenho e custos.
3. **Plano Mestre deste projeto:** define ordem, prioridade, rastreabilidade e método.
4. **Curso da Udemy:** é a sequência principal de ensino e demonstração.
5. **AWS Skill Builder, laboratórios e questões oficiais:** complementam prática e avaliação.
6. **Simulados recentes e confiáveis:** treinam o estilo da prova.
7. **Fontes secundárias de boa reputação:** somente para explicações complementares.

O curso não substitui o guia oficial. A descrição do curso contém referências antigas à SAA-C02 e registros de atualização de 2023. Antes de incorporar uma afirmação suscetível a mudança, o Codex deverá validá-la na documentação oficial vigente.

Não usar:

- dumps ou alegações de questões reais vazadas;
- respostas de fóruns sem validação;
- material antigo quando o serviço, a nomenclatura ou a recomendação tiver mudado;
- memorização de limites numéricos sem relevância demonstrável para o exame;
- conteúdo fora do escopo apenas para aumentar o tamanho da apostila.

---

## 4. Escopo oficial e pesos

O Plano Mestre deverá cobrir integralmente os quatro domínios oficiais:

| Domínio | Peso |
|---|---:|
| Projetar arquiteturas seguras | 30% |
| Projetar arquiteturas resilientes | 26% |
| Projetar arquiteturas de alto desempenho | 24% |
| Projetar arquiteturas com custos otimizados | 20% |

Esses pesos devem influenciar:

- tempo de revisão;
- número de questões;
- recorrência nos simulados;
- profundidade dos cenários;
- prioridade de correção das lacunas.

O Codex deverá criar uma matriz de cobertura com, no mínimo:

| ID | Domínio | Tarefa oficial | Tópico | Serviço | Aula | Complemento oficial | Semana | Status |
|---|---|---|---|---|---|---|---|---|

Status permitidos:

- não iniciado;
- base concluída;
- aprofundamento concluído;
- aplicação concluída;
- questões concluídas;
- revisão D+2 concluída;
- revisão D+7 concluída;
- dominado;
- requer reforço.

---

## 5. Progressão pedagógica obrigatória

Todo tópico deverá seguir esta sequência:

> **Compreender → Comparar → Aplicar → Resolver → Revisar**

### Nível 1 — Base e fundamentos

Ensinar:

- o que é;
- qual problema resolve;
- componentes principais;
- funcionamento básico;
- escopo regional, zonal ou global quando relevante;
- terminologia necessária;
- exemplo simples.

Pergunta de controle:

> O estudante consegue explicar o serviço com suas próprias palavras e reconhecer seu uso básico?

### Nível 2 — Aprofundamento

Ensinar:

- configurações relevantes;
- segurança e controle de acesso;
- alta disponibilidade;
- escalabilidade;
- desempenho;
- modelo de custo;
- limitações;
- integrações;
- alternativas semelhantes;
- falhas e comportamentos importantes.

Pergunta de controle:

> O estudante consegue comparar serviços próximos e explicar os principais trade-offs?

### Nível 3 — Aplicação arquitetural

Ensinar:

- quando escolher;
- quando não escolher;
- requisitos que direcionam a decisão;
- palavras decisivas usadas em questões;
- cenários completos;
- análise das alternativas;
- armadilhas;
- efeitos sobre segurança, resiliência, desempenho, custo e operação.

Pergunta de controle:

> O estudante consegue escolher a melhor solução entre alternativas tecnicamente possíveis e justificar a decisão?

Nenhuma questão integrada deverá ser exigida antes de o conteúdo necessário ter sido ensinado.

---

## 6. Método de decisão arquitetural

Em cada cenário, o Guia e a Apostila deverão aplicar esta ordem:

1. identificar o requisito obrigatório;
2. identificar restrições;
3. localizar palavras decisivas;
4. eliminar alternativas incompatíveis;
5. comparar as alternativas restantes;
6. escolher a solução que melhor atende ao conjunto de requisitos;
7. justificar os trade-offs.

Dimensões obrigatórias:

- segurança;
- resiliência;
- desempenho;
- custo;
- esforço operacional.

Palavras e expressões que devem ser destacadas quando aparecerem:

- menor custo;
- menor esforço operacional;
- totalmente gerenciado;
- alta disponibilidade;
- tolerância a falhas;
- desacoplamento;
- picos imprevisíveis;
- baixa latência;
- durabilidade;
- consistência;
- recuperação;
- criptografia;
- acesso privado;
- global;
- multi-AZ;
- leitura intensiva;
- gravação intensiva.

Uma alternativa que funciona não é necessariamente a melhor resposta. O foco é a solução mais adequada aos requisitos declarados.

---

## 7. Regras para o Guia do Estudante

### Conteúdo

- Escrever em português claro, preservando o nome oficial dos serviços em inglês.
- Na primeira ocorrência, explicar siglas e termos.
- Usar exemplos próximos de sistemas reais.
- Evitar transformar a apostila em catálogo de serviços.
- Priorizar relações, decisões, limites e trade-offs.
- Indicar informações que precisam de validação futura.
- Usar tabelas para comparações exatas.
- Usar diagramas somente quando esclarecerem fluxo, dependência ou arquitetura.
- Incluir custos de forma conceitual; valores exatos devem ser verificados na fonte oficial.

### Estrutura mínima de comparação

| Critério | Serviço A | Serviço B | Como decidir |
|---|---|---|---|

### Estrutura mínima de cenário resolvido

1. cenário;
2. requisitos;
3. restrições;
4. palavras decisivas;
5. alternativas possíveis;
6. decisão;
7. motivo;
8. por que as demais soluções seriam inferiores;
9. variação do cenário que mudaria a resposta.

### Laboratórios

Cada laboratório deverá informar:

- objetivo;
- serviços utilizados;
- pré-requisitos;
- estimativa de tempo;
- possível custo;
- passos;
- validação;
- limpeza obrigatória dos recursos;
- conexão com o exame.

Sempre preferir Free Tier quando adequado, sem assumir que todo recurso será gratuito. Alertar antes de criar qualquer recurso que possa gerar cobrança.

---

## 8. Regras para a Apostila de Questões

### Estilo

As questões devem seguir o estilo situacional e arquitetural da certificação AWS SAA-C03.

Devem conter:

- cenário realista;
- requisito explícito;
- restrições relevantes;
- quatro alternativas plausíveis;
- instrução clara sobre escolher uma ou mais respostas;
- uma solução inequivocamente melhor segundo os requisitos;
- ausência de pistas artificiais ou pegadinhas linguísticas ruins.

### Prioridade das fontes

1. questões e simulados oficiais da AWS;
2. simulados recentes, confiáveis e compatíveis com a SAA-C03;
3. questões inéditas produzidas a partir do guia oficial e da documentação;
4. questões antigas somente se o conceito continuar vigente.

Nunca copiar dumps. Quando uma questão for inspirada por material externo, reescrevê-la de maneira original e registrar a fonte conceitual.

### Tipos de questão

- **Fundamental:** valida um conceito necessário.
- **Situacional:** exige escolher entre serviços ou configurações.
- **Integrada:** combina múltiplos serviços e dimensões.
- **Revisão:** recupera conteúdo já estudado.
- **Simulado:** reproduz distribuição, pressão de tempo e estilo da prova.

### Quantidade

O foco é qualidade e análise, não volume:

- primeira passagem: até 10 questões essenciais por bloco;
- treino diário: aproximadamente 15 a 25 questões, conforme complexidade;
- simulado semanal: volume ajustado ao conteúdo já ensinado;
- simulado final: 65 questões;
- toda resposta errada ou incerta deve alimentar o Caderno de Erros.

### Explicação obrigatória

Para cada questão:

1. resposta;
2. requisito central;
3. palavras decisivas;
4. raciocínio;
5. análise da alternativa A;
6. análise da alternativa B;
7. análise da alternativa C;
8. análise da alternativa D;
9. regra reutilizável;
10. referência oficial para revisão.

---

## 9. Curso-base e cobertura preliminar

Os prints do curso apresentam as seções 4 a 33 sem lacunas. A seção 26 aparece em dois prints apenas por sobreposição.

Mapeamento preliminar:

| Área | Seções principais |
|---|---|
| IAM e segurança | 4, 14, 25 e 26 |
| EC2, armazenamento e escalabilidade | 5–8 |
| Bancos de dados | 9 e 21 |
| Route 53, CDN e entrega global | 10 e 15 |
| Arquiteturas clássicas | 11 |
| S3 e armazenamento | 12–16 |
| Integração e mensageria | 17 |
| Contêineres | 18 |
| Serverless | 19–20 |
| Analytics e machine learning | 22–23 |
| Monitoramento, auditoria e governança | 24 |
| VPC e redes | 27 |
| Migração e recuperação de desastre | 28 |
| Arquiteturas integradas | 20 e 29 |
| Outros serviços relevantes | 30 |
| Well-Architected e revisão | 31–32 |
| Simulado | 33 |

O Codex deverá extrair a duração real de cada seção antes de fechar o cronograma diário. A ordem das aulas poderá ser preservada para facilitar o acompanhamento, mas não deve substituir o mapeamento oficial por domínio e tarefa.

---

## 10. Carga horária

Estimativa total:

| Atividade | Horas previstas |
|---|---:|
| Curso da Udemy | 27 h |
| Guia e revisão teórica | 18–22 h |
| Laboratórios e arquiteturas | 15–18 h |
| Questões e correções | 20–25 h |
| Simulados finais | 8–10 h |
| **Total** | **88–102 h** |

Plano recomendado:

- 3 horas líquidas;
- 6 dias por semana;
- 1 dia de descanso, recuperação ou compensação;
- cerca de 90 horas até 31/08;
- ajustes semanais baseados no desempenho, sem remover conteúdo oficial.

As 27 horas de vídeo integram a carga total e não devem ser adicionadas novamente.

### Estrutura sugerida de um dia comum

| Atividade | Tempo |
|---|---:|
| Aula do curso | 60–90 min |
| Guia, notas e comparação | 35–50 min |
| Laboratório ou cenário | 25–45 min |
| Questões e correção | 30–45 min |
| Recuperação ativa | 10–15 min |

O tempo deve variar conforme o tema. A meta é aprendizagem líquida, não apenas permanência diante do material.

---

## 11. Cronograma macro até 31/08/2026

### Semana 1 — 25/07 a 02/08

Foco:

- introdução e visão do exame;
- fundamentos de nuvem;
- IAM;
- EC2;
- EBS e instâncias;
- ELB;
- Auto Scaling;
- fundamentos de alta disponibilidade.

Entregas:

- capítulos correspondentes do Guia;
- tabelas EC2/EBS/ELB/ASG;
- primeiros laboratórios;
- questões fundamentais e situacionais;
- revisão D+2 iniciada.

### Semana 2 — 03/08 a 09/08

Foco:

- RDS e Aurora;
- ElastiCache;
- Route 53;
- S3;
- classes de armazenamento;
- CloudFront;
- Global Accelerator;
- arquiteturas clássicas.

Entregas:

- mapas de decisão de armazenamento e banco;
- cenários de disponibilidade e entrega global;
- revisão D+7 da Semana 1;
- simulado parcial.

### Semana 3 — 10/08 a 16/08

Foco:

- SQS;
- SNS;
- Kinesis;
- EventBridge e Amazon MQ;
- ECS, ECR, EKS e Fargate;
- Lambda;
- API Gateway;
- DynamoDB;
- Step Functions e arquiteturas serverless.

Entregas:

- comparação de mensageria;
- comparação de contêineres e serverless;
- arquitetura desacoplada;
- revisões D+2 e D+7;
- simulado parcial.

### Semana 4 — 17/08 a 23/08

Foco:

- analytics;
- monitoramento;
- CloudWatch;
- CloudTrail;
- Config;
- segurança;
- KMS;
- Secrets Manager;
- WAF, Shield e serviços relacionados;
- VPC e redes.

Entregas:

- mapa de segurança;
- mapa de conectividade privada;
- laboratório ou desenho de VPC;
- revisão das lacunas;
- simulado parcial ponderado.

### Semana 5 — 24/08 a 27/08

Foco:

- migração;
- backup;
- recuperação de desastre;
- estratégias RTO/RPO;
- Well-Architected Framework;
- custos;
- arquiteturas integradas;
- conteúdo complementar ausente ou superficial no curso.

Entregas:

- tabela de estratégias de disaster recovery;
- revisão de custos e esforço operacional;
- auditoria integral da matriz de cobertura;
- fechamento do Guia inicial.

### Fase final — 28/08 a 31/08

Foco:

- revisão dirigida pelo Caderno de Erros;
- simulados completos de 65 questões;
- correção aprofundada;
- retomada dos tópicos fracos;
- decisão sobre prontidão para a prova.

O cronograma diário definitivo deverá ser gerado depois de registrar as durações exatas das seções 1 a 33.

---

## 12. Revisões e recuperação ativa

Todo conteúdo relevante deverá passar por:

- revisão no encerramento do bloco;
- revisão D+2;
- revisão D+7;
- recuperação em simulados;
- nova revisão quando houver erro ou baixa confiança.

A revisão não deve introduzir matéria nova.

Formatos recomendados:

- explicar sem consultar;
- responder perguntas curtas;
- completar tabelas de comparação;
- escolher serviço para um cenário;
- explicar por que uma alternativa seria inadequada;
- reconstruir uma arquitetura;
- revisar cartões derivados de erros reais.

Uma resposta correta com baixa confiança deve ser marcada para revisão.

---

## 13. Critérios de domínio

Um tópico só poderá ser marcado como **dominado** quando o estudante:

- explicar o conceito sem copiar a definição;
- identificar o problema resolvido;
- comparar com alternativas semelhantes;
- escolher o serviço em um cenário;
- justificar a escolha por requisitos;
- explicar por que opções plausíveis são inferiores;
- atingir pelo menos 80% em questões inéditas do tópico;
- concluir D+2 e D+7;
- não manter erro conceitual aberto no Caderno de Erros.

Prontidão para marcar a prova:

- cobertura integral do Plano Mestre;
- pelo menos dois ou três simulados inéditos com 80% ou mais;
- conclusão dentro do tempo;
- justificativa consciente das respostas;
- estabilidade nos quatro domínios;
- ausência de lacuna crítica em segurança, resiliência, redes, armazenamento, bancos ou custos.

Uma nota alta obtida por repetição de questões conhecidas não comprova prontidão.

---

## 14. Auditoria de qualidade

Antes de finalizar qualquer capítulo ou bloco de questões, o Codex deverá conferir:

### Cobertura

- Está vinculado a um domínio e tarefa oficial?
- O tópico está previsto no Plano Mestre?
- A profundidade é proporcional ao peso e à frequência esperada?

### Atualidade

- Os nomes dos serviços estão atuais?
- O comportamento foi validado em fonte oficial?
- Há limites, preços ou recomendações suscetíveis a mudança?

### Pedagogia

- A base vem antes do aprofundamento?
- A aplicação vem depois dos conceitos?
- Os exemplos esclarecem uma decisão?
- As comparações possuem critérios consistentes?

### Questões

- O cenário é realista?
- Existe uma resposta inequivocamente melhor?
- As alternativas são plausíveis?
- A explicação analisa todas as opções?
- A questão exige conteúdo já ensinado?
- O estilo é compatível com a SAA-C03?

### Rastreabilidade

- O capítulo aponta para as aulas?
- A questão aponta para o tópico?
- A correção aponta para a fonte oficial?
- A matriz de cobertura foi atualizada?

Se qualquer resposta for “não”, o conteúdo não deverá ser considerado concluído.

---

## 15. Instrução operacional para o Codex

Ao continuar este projeto:

1. leia este arquivo integralmente;
2. consulte o guia oficial vigente da SAA-C03;
3. crie ou atualize a matriz de cobertura;
4. registre todas as seções e durações reais do curso;
5. identifique lacunas e conteúdos desatualizados;
6. gere o cronograma diário;
7. produza o Guia do Estudante na ordem aprovada;
8. produza as questões somente após a teoria correspondente;
9. programe D+2 e D+7;
10. mantenha o Caderno de Erros;
11. faça auditoria de qualidade antes de cada entrega;
12. preserve a separação entre teoria, questões e gabarito.

Se uma informação necessária estiver ausente, o Codex deverá:

- buscar a fonte oficial quando a informação for pública e atual;
- fazer uma suposição explícita somente quando ela for reversível;
- pedir esclarecimento quando a decisão alterar materialmente o cronograma, o escopo ou a forma do material.

---

## 16. Primeiras tarefas de execução

Ordem inicial:

1. obter a lista completa das seções 1 a 33, com aulas e durações;
2. obter e registrar a versão vigente do guia oficial;
3. montar a matriz completa de domínios, tarefas, tópicos e serviços;
4. mapear cada aula do curso à matriz;
5. apontar lacunas, excessos e conteúdos que exigem atualização;
6. calcular o cronograma diário de 25/07 a 31/08;
7. criar o sumário do Guia do Estudante;
8. criar o esquema da Apostila de Questões;
9. iniciar a Semana 1;
10. revisar o plano ao final de cada semana com base em evidências.

---

## 17. Decisões já aprovadas

- A referência da prova é exclusivamente a AWS SAA-C03.
- Não usar Consulplan nem qualquer padrão de concurso público.
- Dar preferência a questões oficiais e simulados recentes e confiáveis.
- Não usar dumps.
- Usar o curso da Udemy como fonte principal de aulas, não como autoridade final de escopo.
- Separar Plano Mestre, Guia do Estudante e Apostila de Questões.
- Ensinar na progressão base → aprofundamento → aplicação arquitetural.
- Distribuir todo o conteúdo até o final de agosto de 2026.
- Contabilizar as 27 horas do curso dentro da carga total.
- Trabalhar, como referência inicial, com 3 horas líquidas por dia, 6 dias por semana.
- Usar revisões D+2 e D+7.
- Priorizar compreensão, comparação e decisão arquitetural.

---

**Estado do documento:** versão inicial pronta para validação e execução.  
**Próxima atualização necessária:** inclusão da lista exata das aulas, durações e matriz oficial completa de cobertura.

---

## 18. Estado de execução em 24/07/2026

As informações que estavam pendentes na versão inicial foram obtidas e
estruturadas.

### Perfil confirmado

- iniciante absoluto em AWS, sem experiência profissional na plataforma;
- conta AWS disponível para laboratórios;
- pequeno orçamento mensal, ainda sem teto numérico;
- domingos sem estudo;
- prova em inglês;
- data da prova ainda não informada;
- hipótese de planejamento: prova depois de 01/09/2026.

### Artefatos disponíveis

| Artefato | Arquivo | Estado |
|---|---|---|
| Perfil e premissas | [Perfil_Estudo_SAA-C03.md](Perfil_Estudo_SAA-C03.md) | Pronto |
| Guia oficial organizado | [Mapa_Oficial_SAA-C03.md](../01_Fontes/AWS_Oficial/Mapa_Oficial_SAA-C03.md) | Pronto e validado |
| Inventário do curso | [Inventario_Curso_Udemy_SAA-C03.csv](../01_Fontes/Udemy/Inventario_Curso_Udemy_SAA-C03.csv) | 425 itens validados |
| Matriz de cobertura | [Matriz_Cobertura_SAA-C03.csv](../02_Planejamento/Matriz_Cobertura_SAA-C03.csv) | Classificação inicial pronta |
| Análise de cobertura | [Analise_Inicial_Cobertura_SAA-C03.md](../02_Planejamento/Analise_Inicial_Cobertura_SAA-C03.md) | Pronta |
| Lacunas e excessos | [Lacunas_e_Excessos_SAA-C03.md](../02_Planejamento/Lacunas_e_Excessos_SAA-C03.md) | Auditoria inicial pronta |
| Cronograma diário | [Cronograma_Diario_SAA-C03.md](../02_Planejamento/Cronograma_Diario_SAA-C03.md) | 32 dias e 96 horas validados |
| Guia do Estudante | [Guia_do_Estudante_SAA-C03.md](../03_Guia_do_Estudante/Guia_do_Estudante_SAA-C03.md) | B01–B25 prontos |
| Apostila de Questões | [Apostila_de_Questoes_SAA-C03.md](../04_Questoes_e_Revisoes/Apostila_de_Questoes_SAA-C03.md) | B01–B25 com 250 questões |
| Gabarito comentado | [Gabarito_Comentado_SAA-C03.md](../04_Questoes_e_Revisoes/Gabarito_Comentado_SAA-C03.md) | B01–B25 com 250 respostas comentadas |
| Caderno de Erros | [Caderno_de_Erros_SAA-C03.md](../04_Questoes_e_Revisoes/Caderno_de_Erros_SAA-C03.md) | Pronto para uso |

### Integridade do inventário

- 33 seções;
- 425 itens;
- 396 aulas numeradas de 1 a 396, sem lacunas ou duplicações;
- 385 vídeos;
- 11 artigos;
- 28 quizzes;
- 1 simulado;
- 27 h 14 min no total consolidado das seções.

### Pendências atuais

1. iniciar o estudo pelo B01 e avançar na ordem do cronograma;
2. registrar resultados dos quizzes e simulados quando forem realizados;
3. preencher o Caderno de Erros com erros e acertos de baixa confiança;
4. definir o teto monetário mensal dos laboratórios;
5. definir a data da prova;
6. usar o desempenho real para ajustar o cronograma semanalmente;
7. adicionar as questões e os resultados dos simulados na fase final.

**Novo estado do documento:** produção de B01–B25 concluída; material pronto
para execução e acompanhamento do desempenho real.

---

## 19. Reorganização e entrega B01 em 24/07/2026

A pasta foi reorganizada por função, sem descarte de arquivos:

- `00_Projeto`: escopo, perfil e decisões;
- `01_Fontes`: AWS oficial e Udemy;
- `02_Planejamento`: cronograma e cobertura;
- `03_Guia_do_Estudante`: índice e capítulos;
- `04_Questoes_e_Revisoes`: questões, gabaritos e erros;
- `05_Laboratorios`: práticas seguras;
- `06_Progresso`: checklists, D+2 e D+7;
- `99_Ferramentas`: scripts de geração e validação.

O bloco B01 foi produzido com capítulo teórico, três cenários resolvidos,
laboratório, 10 questões autorais, gabarito comentado e revisões D+2/D+7. As
referências oficiais foram verificadas em 24/07/2026.

**Entrega seguinte àquela etapa:** B02 — concluído em 24/07/2026, conforme a
seção 20.

---

## 20. Entrega B02 em 24/07/2026

O bloco B02 foi produzido para as aulas 19–35:

- capítulo sobre AWS CLI, roles para serviços, auditoria IAM, Budgets, EC2,
  user data, instance types e security groups;
- laboratório Windows de 45 minutos, sem access keys permanentes e sem lançar
  recursos cobrados;
- 10 questões autorais, sendo 6 em português e 4 em inglês;
- gabarito comentado e revisões D+2/D+7;
- README principal e índices atualizados.

CloudShell foi mantido como conteúdo opcional e fora do escopo da prova. O
primeiro lançamento de EC2 permanece no B03 para preservar a sequência do
cronograma e o cleanup controlado.

**Entrega seguinte àquela etapa:** B03 — concluído em 24/07/2026, conforme a
seção 21.

---

## 21. Entrega B03 em 24/07/2026

O bloco B03 foi produzido para as aulas 36–46:

- capítulo sobre SSH, EC2 Instance Connect, Session Manager, instance roles,
  IMDSv2 e modelos de compra do EC2;
- comparação entre On-Demand, Savings Plans, Reserved Instances, Spot,
  Dedicated Hosts, Dedicated Instances e Capacity Reservations;
- atualização do conteúdo antigo de Spot Fleet para priorizar EC2 Auto Scaling
  ou EC2 Fleet em novos projetos;
- refinamento da matriz: SSH e EC2 Instance Connect em 1.2, e a aula 46 em 4.2;
- primeiro laboratório com uma instância Amazon Linux 2023, teto operacional de
  USD 0,25, user data, role vazia, IMDSv2, EC2 Instance Connect e cleanup
  auditado;
- 10 questões autorais, sendo 6 em português e 4 em inglês;
- gabarito comentado, revisões D+2/D+7, README e índices atualizados.

O laboratório não cria key pair, Elastic IP, NAT gateway, load balancer,
snapshot, AMI, Spot request ou compromisso financeiro. A instância deve ser
On-Demand, marcada como elegível no console, e terminada no mesmo exercício.

**Entrega seguinte àquela etapa:** B04 — concluído em 24/07/2026, conforme a
seção 22.

---

## 22. Entrega B04 em 24/07/2026

O bloco B04 foi produzido para as aulas 47–60:

- capítulo sobre private/public/Elastic IP, ENIs, cluster/partition/spread
  placement groups, hibernação, EBS, snapshots e AMIs;
- atualização de 2026 sobre precision time placement groups, mantida como
  conhecimento complementar;
- refinamento da matriz: hibernação em 4.2, AMI em 2.2 e vínculos secundários
  específicos para custo de IPv4, resiliência e storage;
- laboratório read-only de 30 minutos, com custo esperado de USD 0,00,
  inventário inicial/final e nenhuma criação, alteração ou exclusão de recursos;
- 10 questões autorais, sendo 6 em português e 4 em inglês;
- gabarito comentado, revisões D+2/D+7, README, índices e cronograma atualizados.

O projeto possui 25 blocos de conteúdo. Naquela etapa, B05–B25 ainda restavam;
a produção completa está registrada na seção 23. O cronograma mantém sete dias
de consolidação e três simulados depois dos blocos de conteúdo.

---

## 23. Entrega B05–B25 em 01/08/2026

Os 21 blocos restantes foram produzidos no mesmo pacote editorial usado nos
quatro primeiros. Cada bloco agora contém:

- capítulo ligado às aulas correspondentes da Udemy;
- laboratório com preflight, custo, validação e cleanup;
- 10 questões autorais sem exposição do gabarito;
- 10 respostas comentadas com análise de A–D;
- checklist de estudo inicial e revisões D+2/D+7.

O conjunto final contém 25 capítulos, 25 laboratórios, 250 questões, 250
respostas e 25 checklists. A progressão de idioma termina com B20–B25 totalmente
em inglês. O escopo SAA-C03, as listas de serviços e a nomenclatura Amazon Quick
Sight/Amazon Quick foram revalidados em 01/08/2026.

Um validador editorial passou sobre os 25 blocos, cobrindo estrutura, densidade,
idiomas, distribuição de respostas, datas, referências oficiais, navegação,
UTF-8 e links locais. Os simulados permanecem intencionalmente sem questões até
o momento de execução, conforme a decisão do estudante.

**Próximo passo:** começar pelo B01, registrar desempenho real e ajustar somente
as lacunas demonstradas pelos quizzes, questões, revisões e simulados.
