# B05 — EBS, instance store, EFS e fundamentos de alta disponibilidade

**Data planejada:** 30/07/2026<br>
**Nível:** iniciante absoluto<br>
**Comece pelas aulas da Udemy:** [roteiro B05 — aulas 061–071](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b05); assista `061–071` e faça `Q04`<br>
**Domínios oficiais:** 1 — Design Secure Architectures; 2 — Design Resilient Architectures; 3 — Design High-Performing Architectures; 4 — Design Cost-Optimized Architectures<br>
**Tarefas principais:** 3.1 — Determine high-performing and/or scalable storage solutions; 1.3 — Determine appropriate data security controls; 2.2 — Design highly available and/or fault-tolerant architectures<br>
**Tarefas secundárias:** 4.1 — Design cost-optimized storage solutions; 3.4 — Determine high-performing and/or scalable network architectures<br>
**Pré-requisito:** [B04 — IPs, ENIs, EBS, snapshots e AMIs](B04_IPs_ENI_Placement_Hibernation_EBS_Snapshots_e_AMI.md)

## 1. Objetivos de aprendizagem

Ao terminar, você deverá conseguir:

1. escolher entre EBS, instance store e EFS pela interface, persistência, escopo e compartilhamento;
2. selecionar `gp3`, `io2`, `st1` ou `sc1` pelo padrão de I/O;
3. explicar IOPS, throughput e latência sem tratá-los como sinônimos;
4. reconhecer limites e responsabilidade do EBS Multi-Attach;
5. explicar a cadeia de criptografia EBS com AWS KMS;
6. selecionar EFS Regional ou One Zone e um throughput mode;
7. distinguir escalabilidade vertical/horizontal e alta disponibilidade;
8. dimensionar capacidade, crescimento, headroom, IOPS e throughput sem
   superprovisionar storage;
9. reconhecer o papel inicial de um Elastic Load Balancer.

## 2. Aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 61 — AMI Hands On | acompanhe o ciclo e audite snapshots residuais |
| 62 — EC2 Instance Store | alta prioridade: efêmero e ligado ao host |
| 63–65 — tipos, Multi-Attach e encryption do EBS | estudar integralmente |
| 66–68 — EFS e comparação com EBS | estudar integralmente; atualize o modelo de performance com este capítulo |
| 69 — cleanup | reproduzir depois do LAB B05 |
| Q04 | fazer antes das questões autorais |
| 70–71 — HA, scalability e ELB | base conceitual para B06–B07 |

## 3. Fundamentos: interface, escopo e vida útil

```text
EC2 ── bloco ── EBS volume (uma AZ; persiste independentemente)
EC2 ── bloco ── instance store (disco do host; efêmero)
EC2/ECS/Lambda ── NFS ── EFS (filesystem compartilhado; Regional ou One Zone)
```

- **EBS** é block storage. O sistema operacional cria filesystem e monta o volume. Volume e instância devem estar na mesma AZ. Snapshot é regional e permite recriar o volume em outra AZ.
- **Instance store** fornece blocos em discos fisicamente ligados ao host. É excelente para buffer, cache e scratch reconstruível. Os dados não sobrevivem a stop, hibernate, terminate ou falha do disco/host; reboot normalmente não os apaga.
- **EFS** é um filesystem NFS elástico compartilhável por vários clientes compatíveis. Mount targets fornecem presença de rede nas AZs escolhidas. Security groups e permissões POSIX continuam relevantes.

| Requisito dominante | Escolha inicial | Motivo |
|---|---|---|
| boot volume ou banco em uma instância | EBS | bloco persistente, baixa latência |
| scratch muito rápido e descartável | instance store | armazenamento local ao host |
| mesmos arquivos em várias instâncias Linux/AZs | EFS Regional | NFS compartilhado e Multi-AZ |
| filesystem compartilhado, custo menor, falha de AZ aceitável | EFS One Zone | cópias dentro de uma AZ |
| objetos via API, sem filesystem | S3 | não confundir objeto com bloco/NFS |

## 4. Como ler desempenho

- **IOPS:** operações por segundo; importante para I/O pequeno e aleatório.
- **Throughput:** MiB/s; importante para leituras e gravações sequenciais grandes.
- **Latência:** tempo de uma operação; requisito de resposta individual.
- O limite efetivo é o menor entre volume, instância, configuração e workload.

### 4.1 Tipos EBS

| Tipo | SSD/HDD | Decisão de prova |
|---|---|---|
| `gp3` | SSD | uso geral; tamanho, IOPS e throughput configuráveis de forma independente dentro dos limites |
| `io2` | SSD | IOPS provisionadas, desempenho consistente e workloads críticos; opção de maior durabilidade |
| `st1` | HDD | throughput alto para dados grandes e sequenciais; não aceita boot |
| `sc1` | HDD | dados frios, sequenciais e baixo custo; não aceita boot |

Tipos anteriores podem aparecer em migração, mas novas decisões normalmente começam em `gp3`, `io2`, `st1` ou `sc1`. Consulte limites atuais antes de dimensionar.

### 4.2 Multi-Attach não é filesystem distribuído

Multi-Attach permite anexar volumes compatíveis a múltiplas instâncias compatíveis **na mesma AZ**. A aplicação deve coordenar gravações e usar filesystem cluster-aware. Um filesystem comum montado simultaneamente pode corromper dados. Para compartilhamento Linux simples entre AZs, pense primeiro em EFS.

### 4.3 Dimensionamento econômico de capacidade — tarefa 4.1

Dimensionar storage não é copiar o tamanho do disco atual nem comprar o máximo
“para garantir”. Comece com dados medidos e com a data da próxima revisão:

```text
capacidade projetada = uso atual + (crescimento por período × períodos até a revisão)
capacidade planejada = capacidade projetada × (1 + headroom justificado)
```

O **headroom** absorve variação e o tempo necessário para reagir. Ele não é um
percentual universal: depende da volatilidade do crescimento, dos alarmes, do
tempo para expandir ou migrar e do impacto de ficar sem espaço. Arredonde para
cima e registre as hipóteses, mas não confunda margem justificada com anos de
capacidade ociosa.

Depois dimensione cada eixo separadamente:

| Eixo | Evidência | Decisão |
|---|---|---|
| capacidade | GiB usados, retenção, crescimento e janela de revisão | tamanho que cobre projeção + headroom |
| IOPS | pico sustentado, tamanho e padrão das operações | IOPS provisionadas e tipo SSD/HDD adequado |
| throughput | MiB/s sustentados e tamanho médio de I/O | throughput provisionado e limite do caminho |
| latência | percentis e sensibilidade da aplicação | classe de volume e arquitetura compatíveis |

No `gp3`, tamanho, IOPS e throughput podem ser provisionados separadamente
dentro das relações e limites vigentes. Portanto, não aumente GiB apenas para
obter desempenho. Também valide o limite agregado e a largura de banda EBS da
instância: o desempenho efetivo continua sendo o menor limite do caminho.

O custo mensal comparável inclui capacidade provisionada, IOPS e throughput
acima do baseline quando cobrados, snapshots e retenção. Subdimensionar pode
causar indisponibilidade; superdimensionar cobra espaço e desempenho sem valor.
Monitore uso, fila, latência, IOPS e throughput e revise periodicamente. EBS
Elastic Volumes permite aumentar tamanho e ajustar desempenho em configurações
compatíveis, mas não reduz o tamanho de um volume diretamente; reduzir exige
criar um volume menor e migrar os dados.

## 5. Criptografia EBS

EBS encryption usa AWS KMS e protege dados em repouso, I/O entre instância e volume e snapshots derivados. A operação é transparente para aplicações em tipos atuais e existe para todos os tipos de volume.

```text
KMS key autorizada
  └── data key protegida
       ├── volume criptografado
       └── snapshot criptografado → novos volumes criptografados
```

- habilitar **encryption by default** reduz criação acidental sem criptografia;
- uma chave gerenciada pelo cliente oferece controle de política, grants, rotação e auditoria, com custo e responsabilidade adicionais;
- perder acesso à KMS key torna os dados inutilizáveis;
- para criptografar dados originados em snapshot não criptografado, copie o snapshot habilitando criptografia ou crie um volume criptografado conforme o fluxo suportado.

## 6. EFS atual: tipo, classes e throughput

| Decisão | Opções | Regra prática |
|---|---|---|
| filesystem type | Regional / One Zone | Regional para resiliência a AZ; One Zone se o risco for aceito |
| performance mode | General Purpose / Max I/O | documentação atual recomenda General Purpose; Max I/O é geração anterior e aumenta latência por operação |
| throughput mode | Elastic / Provisioned / Bursting | Elastic para carga imprevisível; Provisioned para necessidade conhecida; Bursting acompanha dados em Standard |
| storage class | Standard / IA / Archive | lifecycle move arquivos frios; considere latência, acesso e duração mínima |

EFS não é automaticamente público. O cliente precisa de caminho de rede ao mount target, DNS, porta NFS `2049`, security groups e permissões. Access points ajudam a impor identidade POSIX e diretório raiz por aplicação.

## 7. HA e escalabilidade

- **Escala vertical:** instância maior; simples, mas possui teto e pode exigir indisponibilidade.
- **Escala horizontal:** mais instâncias; exige distribuição de tráfego e estado externo/replicado.
- **Alta disponibilidade:** continuar servindo quando um componente falha.
- **Fault tolerance:** mascarar falhas com interrupção mínima ou imperceptível; costuma custar mais.
- **Elasticidade:** adicionar e remover capacidade conforme a demanda.

O ELB recebe tráfego por listeners, avalia regras quando aplicável e encaminha apenas a targets saudáveis em target groups. Ele não corrige uma aplicação stateful, não cria réplicas de banco e não substitui a implantação em múltiplas AZs.

## 8. Cenários resolvidos

### Cenário resolvido 1 — processamento temporário

Uma frota Spot transforma vídeos. Os arquivos originais e resultados ficam no S3; cada nó precisa de scratch com altíssimo I/O e pode refazer o trabalho. **Decisão:** instance store. A perda no encerramento é aceitável porque a fila e os objetos são duráveis. EBS agregaria persistência não exigida.

### Cenário resolvido 2 — conteúdo compartilhado

Dez instâncias Linux em três AZs precisam editar e ler os mesmos arquivos. **Decisão:** EFS Regional com mount target nas AZs usadas. EBS comum é zonal e não oferece compartilhamento NFS; Multi-Attach não atravessa AZ e exigiria software cluster-aware.

### Cenário resolvido 3 — banco com IOPS previsíveis

Um banco em EC2 exige latência consistente e IOPS provisionadas. **Decisão:** começar pela família `io2`, validar limite da instância e criar snapshots. `st1` favorece throughput sequencial; instance store sozinho viola persistência.

## 9. Custos e cleanup

EBS cobra capacidade provisionada e, conforme o tipo, IOPS/throughput adicionais; volumes continuam cobrando sem instância. Snapshots cobram armazenamento incremental. EFS cobra armazenamento por classe, acesso às classes frias e possivelmente throughput. Instance store integra o preço da instância, mas a duplicação necessária para durabilidade pode custar mais.

Após o laboratório, confirme: instância terminada, volumes de dados excluídos, snapshots excluídos, AMIs de laboratório desregistradas e snapshots correspondentes removidos. Não crie EFS somente para ver o console. Verifique sempre as páginas de preço da Region.

## 10. Armadilhas de prova

- reboot não equivale a stop; instance store normalmente sobrevive ao reboot, não ao stop;
- EBS volume é zonal; snapshot é regional;
- Multi-Attach não transforma EBS em EFS;
- Multi-Attach exige coordenação de escrita pela aplicação;
- EFS One Zone não oferece resiliência à perda completa da AZ;
- Multi-AZ e autoscaling resolvem problemas diferentes;
- ELB distribui tráfego; não persiste sessão por padrão nem replica dados.

## 11. Decisões em camadas

Em questões longas, separe a decisão em quatro perguntas:

1. **Qual interface a aplicação espera?** Bloco, filesystem ou API de objetos.
2. **Qual falha precisa sobreviver?** Processo, instância, host, AZ ou Region.
3. **Quem acessa ao mesmo tempo?** Uma instância, várias na mesma AZ ou uma
   frota Multi-AZ.
4. **Qual dimensão de desempenho domina?** Latência, IOPS ou throughput.

Só depois compare preço. A opção nominalmente mais barata pode custar mais se
exigir replicação artesanal, licenças ou operação contínua.

### Exemplo de decomposição

Uma aplicação pede “disco compartilhado muito rápido”. A frase é insuficiente.
Pergunte se o software usa NFS, se os escritores são concorrentes, se precisa
sobreviver à perda de AZ e se “rápido” significa baixa latência por operação ou
grandes transferências sequenciais. As respostas podem levar a EFS, EBS com
software cluster-aware ou até a uma mudança para S3; não existe um vencedor
universal.

## 12. Comparação de falhas

| Evento | EBS | Instance store | EFS Regional | EFS One Zone |
|---|---|---|---|---|
| reboot da instância | permanece | normalmente permanece | permanece | permanece |
| stop da instância | permanece | perde dados | permanece | permanece |
| terminate | depende de `DeleteOnTermination` | perde dados | permanece | permanece |
| perda do host | permanece como serviço zonal | perde dados locais | permanece | permanece |
| perda completa da AZ | restaurar/replicar em outra AZ | perde cópia local | projetado para Multi-AZ | pode perder disponibilidade/dados |

Essa tabela não dispensa backup. Alta disponibilidade mantém serviço; backup
fornece um ponto de recuperação contra exclusão, corrupção ou erro lógico.

## 13. Tradução de palavras de prova

```text
ephemeral / scratch / buffer       -> instance store
boot / block / low-latency volume  -> EBS
shared Linux file system / NFS     -> EFS
provisioned IOPS / critical OLTP   -> io2
large sequential scans             -> st1
cold sequential data               -> sc1
unpredictable NFS throughput       -> EFS Elastic throughput
survive complete AZ loss           -> não escolher variante One Zone sozinha
```

“Shared storage” não basta: S3, EFS e um banco são compartilháveis, mas expõem
interfaces e semânticas diferentes. A resposta correta deve encaixar a
aplicação sem uma reescrita que o cenário não autoriza.

## 14. Checklist e recuperação ativa

- [ ] Consigo escolher EBS, EFS e instance store sem usar “mais rápido” como única justificativa.
- [ ] Sei quando IOPS ou throughput domina.
- [ ] Calculo crescimento até a próxima revisão e justifico o headroom.
- [ ] Dimensiono GiB, IOPS e throughput como eixos distintos e comparo seu
  custo.
- [ ] Explico por que Multi-Attach pode corromper um filesystem comum.
- [ ] Sei o efeito de uma KMS key indisponível.
- [ ] Distingo EFS Regional de One Zone.
- [ ] Explico HA, fault tolerance, escalabilidade e elasticidade.

Sem consultar: (1) desenhe o escopo dos três storages; (2) escolha o tipo EBS para OLTP, logs sequenciais e arquivo frio; (3) liste três controles necessários para montar EFS; (4) explique por que ELB sozinho não cria HA.

## 15. Ligações e referências oficiais

- Próximo: [B06 — ALB, NLB e GWLB](B06_ALB_NLB_GWLB_Target_Groups_e_Cross_Zone.md)
- Prática: [LAB B05](../../05_Laboratorios/LAB_B05_EBS_Snapshot_Restore_e_Projeto_EFS.md)
- Avaliação: [questões B05](../../04_Questoes_e_Revisoes/Blocos/B05_Questoes.md)
- Correção: [gabarito B05](../../04_Questoes_e_Revisoes/Blocos/B05_Gabarito.md)
- Progresso: [checklist e revisões B05](../../06_Progresso/B05_Checklist_e_Revisoes.md)
- [Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html)
- [EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- [General Purpose SSD `gp3`](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html)
- [Create an inventory of EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-data-inventory.html)
- [Select the correct resource type, size and number](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/select-the-correct-resource-type-size-and-number.html)
- [EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html)
- [EBS Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html)
- [EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Amazon EFS features](https://docs.aws.amazon.com/efs/latest/ug/features.html)
- [EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
- [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)
