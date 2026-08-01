# B13 — Storage híbrido, FSx, DataSync, Transfer Family e Snow

**Data planejada:** 08/08/2026<br>
**Nível:** iniciante<br>
**Comece pelas aulas:** [roteiro B13 — aulas 172–181](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b13); assista `172–181` e faça `Q13`<br>
**Domínio principal:** 3 — Design High-Performing Architectures<br>
**Tarefas principais:** 3.1 — Determine high-performing and/or scalable storage solutions; 3.5 — Determine high-performing data ingestion and transformation solutions<br>
**Tarefas secundárias:** 2.2 e 4.1<br>
**Pré-requisito:** B11–B12 — S3, classes, segurança e entrega

## 1. Objetivos de aprendizagem

Ao concluir, você deverá conseguir:

1. escolher storage por interface: object, block, file ou tape;
2. separar migração pontual de integração híbrida contínua;
3. comparar FSx for Windows, Lustre, NetApp ONTAP e OpenZFS;
4. selecionar S3 File, FSx File, Volume ou Tape Gateway;
5. escolher DataSync para transferência online automatizada;
6. escolher Transfer Family quando parceiros precisam SFTP/FTPS/FTP/AS2;
7. reconhecer o uso histórico da Snow Family e a mudança vigente;
8. estimar janela de rede e considerar transferência física;
9. prever custos de filesystem, gateway, requests e transferência;
10. evitar provisionar serviços caros somente para treinamento.

## 2. Aulas deste bloco e atualização de 2026

| Aulas | Tratamento |
|---|---|
| 172–174 | entenda Snow como padrão de decisão; aplique a atualização abaixo |
| 175–176 | compare as quatro famílias FSx; hands-on somente walkthrough |
| 177–178 | escolha o gateway pelo protocolo legado; não implante appliance |
| 179 | Transfer Family para protocolos de parceiros |
| 180 | DataSync para cópia online acelerada e verificável |
| 181 | consolide a matriz única de storage |

### Mudança que invalida uma escolha automática do curso

- **`núcleo SAA-C03`:** reconhecer o padrão de decisão entre transferência
  online, transporte físico e compute em local desconectado, além de calcular a
  janela com throughput efetivo.
- **`atualização relevante`:** Snowball Edge não aceita novos clientes desde
  **07/11/2025** e a AWS encerrará o suporte aos dispositivos nas Regions
  comerciais em **31/12/2026**. Clientes existentes precisam planejar a saída;
  não trate o serviço como escolha nova.
- **`conteúdo profissional opcional`:** para projetos atuais, compare DataSync
  ou Direct Connect para transferência online, Data Transfer Terminal ou
  parceiros para transporte físico e Outposts para edge compute.

`Conteúdo profissional opcional` não é para memorizar; ele serve para corrigir
uma decisão real atual. Se uma questão
SAA-C03 ainda apresentar Snowball como opção sem contexto temporal, reconheça o
padrão histórico; em arquitetura real, aplique as datas e valide a alternativa
disponível para o cliente e o local.

Há uma segunda mudança relevante: **Amazon FSx File Gateway não está disponível
para novos clientes desde 28 de outubro de 2024**. Clientes existentes podem
continuar usando. Em um projeto novo, avalie acesso direto ao FSx for Windows
File Server por VPN/Direct Connect; se o cache local for indispensável, avalie
as opções de cache do FSx for NetApp ONTAP. Não confunda essa restrição com S3
File Gateway, Tape Gateway ou Volume Gateway.

## 3. Comece pela interface

```text
API HTTP + objetos, data lake, durabilidade -> S3
disco de uma instância/AZ                 -> EBS
NFS compartilhado Linux multi-AZ          -> EFS
SMB/Windows/AD                             -> FSx for Windows
HPC e processamento de dados S3           -> FSx for Lustre
recursos NetApp, multiprotocolo            -> FSx for NetApp ONTAP
semântica ZFS e snapshots/clones           -> FSx for OpenZFS
protocolo legado on-prem + backend AWS     -> Storage Gateway
cópia online agendada/verificada           -> DataSync
endpoint SFTP/FTPS/FTP/AS2 gerenciado       -> Transfer Family
```

Não escolha pelo nome “storage”. Descubra simultaneamente protocolo, padrão de
acesso, latência, consistência, compartilhamento, localidade e duração.

## 4. Amazon FSx

| Família | Interface/compatibilidade | Melhor sinal | Integrações importantes |
|---|---|---|---|
| FSx for Windows File Server | SMB, Windows, Microsoft AD | Windows shares, NTFS, DFS | AD, VSS, Multi-AZ conforme deployment |
| FSx for Lustre | POSIX/Lustre | HPC, ML e alto throughput | ligação com S3, scratch ou persistent |
| FSx for NetApp ONTAP | NFS, SMB, iSCSI | migração NetApp e multiprotocolo | snapshots, clones, tiering, SnapMirror |
| FSx for OpenZFS | NFS | workloads Linux/ZFS e baixa latência | snapshots e clones eficientes |

**FSx não é uma única tecnologia.** A família selecionada define protocolo,
semântica, deployment e custo. FSx é provisionado: capacidade, throughput,
backups e eventualmente SSD/cache continuam cobrando até exclusão.

### Cenário resolvido 1 — render farm e S3

Uma render farm Linux processa um dataset no S3 com altíssimo throughput e
depois devolve resultados ao bucket. Escolha **FSx for Lustre** ligado ao S3.
EFS oferece NFS general purpose, mas a palavra decisiva é processamento paralelo
de alto desempenho. Para trabalho temporário e regenerável, uma opção scratch
pode reduzir custo; dados duráveis continuam no S3.

### Cenário resolvido 2 — aplicações Windows e AD

Usuários Windows precisam de SMB, ACLs do Windows e integração ao Active
Directory. Escolha **FSx for Windows File Server**, avaliando Multi-AZ para alta
disponibilidade. EFS usa NFS e não satisfaz a semântica pedida; S3 não é um file
share SMB nativo.

## 5. Storage Gateway: continuidade de protocolo

Storage Gateway conecta um appliance on-premises ao armazenamento AWS:

| Gateway | Interface para o cliente | Destino/uso |
|---|---|---|
| S3 File Gateway | NFS/SMB | arquivos apresentados localmente, objetos no S3 |
| FSx File Gateway | SMB | legado para clientes existentes: cache local para FSx for Windows; indisponível a novos clientes |
| Volume Gateway — cached | iSCSI block | dados principais na AWS, working set local |
| Volume Gateway — stored | iSCSI block | dados principais locais, snapshots assíncronos na AWS |
| Tape Gateway | iSCSI VTL | substituir fitas físicas; archive no Glacier |

O gateway é **híbrido contínuo**, não apenas uma ferramenta de copiar uma pasta
uma vez. Cache local melhora leitura, mas não elimina planejamento de banda,
discos, disponibilidade do appliance e recuperação.

### Cenário resolvido 3 — software de backup espera fitas

O software certificado só fala VTL/iSCSI e a empresa quer parar de transportar
cartuchos. Escolha **Tape Gateway**. Transfer Family recebe arquivos por
protocolos externos, e DataSync copia datasets; nenhum emula a biblioteca de
fitas exigida.

## 6. DataSync, Transfer Family e transferência física

### 6.1 DataSync

DataSync automatiza transferências online entre storage on-prem/self-managed e
S3, EFS ou FSx, além de localizações AWS compatíveis. O agent acessa NFS, SMB,
HDFS ou object storage conforme a origem. Tarefas incluem agendamento,
criptografia em trânsito, filtros, verificação e métricas.

Sinais: *move millions of files*, *online*, *scheduled*, *preserve metadata*,
*verification*, *accelerate migration*. Não é filesystem para a aplicação após
a cópia.

### 6.2 Transfer Family

Transfer Family fornece endpoints gerenciados para SFTP, FTPS, FTP e AS2 com
dados no S3 ou EFS. É a resposta quando parceiros não mudarão seu cliente de
transferência. Você ainda decide identity provider, endpoint público/VPC,
logging, roles e isolamento por prefixo.

### 6.3 Online versus física

Estimativa inicial:

```text
tempo mínimo (s) ≈ bytes × 8 / throughput efetivo (bit/s)
```

Use throughput **efetivo**, janela disponível e crescimento diário. Se a carga
inicial levar meses ou saturar o link, considere transporte físico disponível
para aquele cliente/local. Após a seed, DataSync ou replicação pode transportar
o delta. Nunca escolha um dispositivo Snow para uma conta nova sem verificar a
mudança de disponibilidade.

### Cenário resolvido 4 — fornecedor só usa SFTP

Cem fornecedores depositam arquivos por SFTP; a empresa quer S3 como destino e
não quer administrar servidores. Escolha **Transfer Family** com SFTP, identity
provider e roles que isolam prefixes. DataSync seria adequado para uma origem
de storage controlada pela empresa, não para expor um endpoint SFTP multiusuário.

## 7. Tabela de decisão consolidada

| Requisito dominante | Serviço | Por que não o vizinho |
|---|---|---|
| objetos e data lake | S3 | não fornece filesystem POSIX/SMB geral |
| block de baixa latência para EC2 | EBS | zonal; não é share multi-AZ comum |
| NFS elástico multi-AZ | EFS | não é SMB/Windows nativo |
| filesystem especializado | família FSx correta | exige capacity/throughput e escolha de engine |
| manter protocolo local continuamente | Storage Gateway | appliance/cache são parte da solução |
| copiar dados online | DataSync | não vira endpoint da aplicação |
| receber protocolo de parceiro | Transfer Family | cobra endpoint/uso e requer identity design |
| bulk físico | opção atualmente disponível | logística, prazo e disponibilidade comercial |

## 8. Custos, segurança e cleanup

- FSx cobra filesystem, SSD/HDD, throughput, backups e transferência.
- Storage Gateway pode envolver appliance/EC2, cache EBS, snapshots e requests.
- DataSync cobra dados transferidos e infraestrutura do agent.
- Transfer Family pode cobrar endpoint/hora e dados processados mesmo ocioso.
- S3/EFS/FSx continuam cobrando o armazenamento de destino.
- Transferência entre AZs/Regions e saída para internet pode ser cobrada.

Segurança: TLS, roles de serviço mínimas, encryption at rest, controle de
prefixo/share, AD/identity provider, logs e checksum/verificação. Para dados
físicos, inclua cadeia de custódia e encryption.

Cleanup: excluir tarefas/locations/agents que não serão reutilizados, servers e
users do Transfer Family, filesystems FSx e backups finais indesejados,
gateways/EC2/EBS e dados de teste. Neste bloco, **não crie** nenhum desses
recursos: diagrama e inspeção de preço bastam.

## 9. Armadilhas

- DataSync move dados; Storage Gateway mantém uma interface híbrida.
- Transfer Family é endpoint de protocolo, não acelerador genérico de storage.
- File Gateway não monta S3 como filesystem POSIX perfeito; objetos e arquivos
  têm semânticas diferentes.
- FSx for Lustre é o sinal de HPC/S3; FSx for Windows é SMB/AD.
- Tape Gateway emula VTL; não é Snowball.
- Snow Family não está aberta a novos clientes em 2026.
- FSx File Gateway também não aceita novos clientes; os demais tipos de gateway
  não herdaram essa restrição.
- EFS, FSx, EBS e S3 não são intercambiáveis por “todos armazenam dados”.

## 10. Checklist e recuperação ativa

Para cada cenário, anote: interface, origem, destino, volume, prazo, banda,
continuidade, RPO/RTO, segurança, custo ocioso e cleanup.

Sem consulta:

1. Faça uma tabela das quatro famílias FSx.
2. Compare os quatro tipos de Storage Gateway.
3. Dê um caso para DataSync e outro para Transfer Family.
4. Calcule quanto 100 TB levariam a 1 Gbit/s antes de overhead.
5. Explique a mudança da Snow Family e duas alternativas atuais.
6. Cite cinco recursos que podem continuar cobrando após uma PoC.

## 11. Ligações

- Anterior: B11–B12 — S3, ciclo de vida e segurança.
- Próximo: B14 — desacoplamento com SQS/SNS.
- [Laboratório B13](../../05_Laboratorios/LAB_B13_Desenho_de_Migracao_e_Storage_Hibrido.md)
- [Questões B13](../../04_Questoes_e_Revisoes/Blocos/B13_Questoes.md)
- [Gabarito B13](../../04_Questoes_e_Revisoes/Blocos/B13_Gabarito.md)
- [Checklist e revisões B13](../../06_Progresso/B13_Checklist_e_Revisoes.md)

## 12. Referências oficiais

- [Guia de decisão de storage](https://docs.aws.amazon.com/pdfs/decision-guides/latest/storage-on-aws-how-to-choose/storage-on-aws-how-to-choose.pdf)
- [Amazon FSx](https://docs.aws.amazon.com/fsx/)
- [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/)
- [Mudança de disponibilidade do FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/create-file-gateway.html)
- [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
- [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html)
- [Mudança de disponibilidade do Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html)
- [Histórico oficial da mudança do Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html)
- [Encerramento do suporte ao Snowball](https://aws.amazon.com/snowball/)
