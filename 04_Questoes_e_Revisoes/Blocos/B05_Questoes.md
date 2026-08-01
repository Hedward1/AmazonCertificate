# B05 — Questões: EBS, instance store, EFS e HA

**Quantidade:** 10 questões inéditas<br>
**Idioma:** 6 em português e 4 em inglês<br>
**Regra:** uma resposta por questão<br>
**Tempo sugerido:** 15 minutos<br>
**Gabarito:** [arquivo separado](B05_Gabarito.md)

## Metadados

| ID | Tarefa | Tópico | Tipo | Dificuldade | Idioma |
|---|---|---|---|---|---|
| B05-01 | 3.1 | Instance store | Situacional | Básica | Português |
| B05-02 | 3.1 | EBS volume types | Situacional | Intermediária | Português |
| B05-03 | 3.1 | EBS Multi-Attach | Situacional | Avançada | Português |
| B05-04 | 1.3 | EBS encryption | Situacional | Intermediária | Português |
| B05-05 | 3.1 | EFS Regional | Situacional | Básica | Português |
| B05-06 | 2.2 | HA e escalabilidade | Fundamental | Intermediária | Português |
| B05-07 | 3.1 | EBS scope | Situacional | Básica | Inglês |
| B05-08 | 3.1 | EFS throughput | Situacional | Intermediária | Inglês |
| B05-09 | 4.1 | Storage cost | Situacional | Intermediária | Inglês |
| B05-10 | 3.4 | ELB fundamentals | Fundamental | Básica | Inglês |

## Como resolver este bloco

Para cada questão:

1. identifique se a interface pedida é bloco, arquivo ou objeto;
2. marque o domínio de falha exigido: host, AZ ou Region;
3. verifique se o dado é persistente ou reconstruível;
4. procure compartilhamento simultâneo e semântica de escrita;
5. separe IOPS, throughput e latência;
6. elimine alternativas que resolvem rede quando a pergunta é storage;
7. registre a palavra decisiva antes de selecionar a resposta.

Não use “mais rápido” como justificativa isolada. A prova descreve um padrão de
I/O e uma restrição operacional. Também não presuma que Multi-Attach adiciona
coordenação de filesystem ou que um snapshot possa ser montado diretamente.

## Cobertura intencional

- B05-01 testa efemeridade aceita.
- B05-02 testa escolha de volume por IOPS.
- B05-03 testa responsabilidade de concorrência.
- B05-04 testa controle de chave.
- B05-05 testa compartilhamento e falha de AZ.
- B05-06 separa capacidade de disponibilidade.
- B05-07 testa a fronteira zonal do EBS.
- B05-08 usa a recomendação atual de throughput EFS.
- B05-09 testa cleanup e custo residual.
- B05-10 prepara o vocabulário de ELB para o B06.

As questões em inglês mantêm os nomes usados na prova. Não traduza mentalmente
`throughput`, `scratch`, `listener` ou `Availability Zone` durante a primeira
leitura; associe cada termo diretamente à regra arquitetural.

## Questões

### B05-01
Uma frota de processamento pode repetir qualquer tarefa a partir dos objetos originais no S3. Ela precisa do menor tempo de acesso possível para arquivos temporários, e a perda desses arquivos quando uma instância é interrompida é aceitável. Qual armazenamento usar?<br>
- A. EFS Regional.
- B. Instance store.
- C. Snapshot EBS.
- D. S3 Glacier Deep Archive.

### B05-02
Um banco em EC2 exige IOPS provisionadas e latência consistente para transações críticas. Qual escolha inicial é mais adequada?<br>
- A. `sc1`.
- B. `st1`.
- C. `io2`.
- D. Instance store sem réplica.

### B05-03
Duas instâncias na mesma AZ precisam gravar simultaneamente em um volume. A equipe propõe EBS Multi-Attach com um filesystem comum que desconhece acesso concorrente. Qual avaliação está correta?<br>
- A. É seguro porque o EBS serializa qualquer filesystem.
- B. Multi-Attach funciona também entre AZs.
- C. A aplicação/filesystem precisa coordenar I/O; a proposta pode corromper
  dados.
- D. Multi-Attach converte bloco em NFS.

### B05-04
Uma empresa precisa controlar e auditar quem pode usar a chave que protege volumes EBS. Qual solução atende melhor?<br>
- A. Chave KMS gerenciada pelo cliente com política e grants adequados.
- B. Security group no volume.
- C. Bucket policy no snapshot.
- D. Elastic IP criptografado.

### B05-05
Instâncias Linux em três AZs devem compartilhar o mesmo filesystem e continuar acessando dados após a perda de uma AZ. Qual solução?<br>
- A. Um volume EBS `gp3` em Multi-Attach.
- B. Instance store replicado por reboot.
- C. EFS One Zone.
- D. EFS Regional com conectividade e mount targets apropriados.

### B05-06
Qual afirmação distingue corretamente alta disponibilidade de escalabilidade horizontal?<br>
- A. São sinônimos.
- B. HA visa continuidade diante de falhas; escala horizontal adiciona/remove
  nós e pode ajudar, mas não garante HA sozinha.
- C. HA significa apenas usar uma instância maior.
- D. Escala horizontal elimina a necessidade de health checks.

### B05-07
An EBS volume is in `us-east-1a`, and an EC2 recovery instance is in `us-east-1b`. What should an architect do?<br>
- A. Attach the existing volume across AZs.
- B. Create a snapshot, restore a new volume in `us-east-1b`, and attach it.
- C. Convert the volume to instance store.
- D. Associate the volume with an Elastic IP.

### B05-08
An EFS workload is unpredictable and highly spiky. The team does not know the throughput requirement in advance. Which current throughput mode is the best starting point?<br>
- A. Elastic throughput.
- B. Provisioned IOPS for EBS.
- C. Max I/O with Bursting is always mandatory.
- D. S3 Transfer Acceleration.

### B05-09
A development instance has been terminated, but the monthly bill still includes block storage. Which resource is the most likely cause?<br>
- A. A stopped listener rule.
- B. A released private IPv4 address.
- C. A deleted instance-store device.
- D. An available EBS data volume or retained snapshot.

### B05-10
Which Elastic Load Balancing component defines the protocol and port on which a load balancer accepts client connections?<br>
- A. Snapshot.
- B. Listener.
- C. Mount target.
- D. KMS grant.

## Registro antes de corrigir

| ID | Resposta | Confiança | Palavra decisiva |
|---|---|---|---|
| B05-01 | | | |
| B05-02 | | | |
| B05-03 | | | |
| B05-04 | | | |
| B05-05 | | | |
| B05-06 | | | |
| B05-07 | | | |
| B05-08 | | | |
| B05-09 | | | |
| B05-10 | | | |
