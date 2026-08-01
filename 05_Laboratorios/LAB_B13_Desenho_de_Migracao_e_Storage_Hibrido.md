# LAB B13 — Desenho de migração e storage híbrido

**Timebox:** 27 minutos<br>
**Modo:** diagrama e inspeção read-only<br>
**Custo esperado:** zero<br>
**Objetivo:** selecionar storage e migração por interface, prazo e continuidade<br>
**Capítulo:** [B13 — storage híbrido e migração](../03_Guia_do_Estudante/Capitulos/B13_Storage_Hibrido_FSx_DataSync_Transfer_e_Snow.md)<br>
**Proibido neste LAB:** provisionar FSx, Transfer Family server, Storage Gateway,
DataSync agent/task ou dispositivo físico

## 1. Preflight — 3 min

- [ ] Confirmar que não há dados reais ou identificadores sensíveis no desenho.
- [ ] Abrir as páginas oficiais de serviços e preços da Region pretendida.
- [ ] Se entrar no console, usar identidade não root e executar somente `List/Describe`.
- [ ] Registrar inventário inicial: FSx __; gateways __; DataSync tasks __; Transfer servers __.

## 2. Caso-base — 3 min

Uma empresa possui:

- 80 TB em NFS e 5 TB novos por mês;
- link dedicado com throughput efetivo de 500 Mbit/s por 12 h/dia;
- render farm que precisa processar parte dos dados com alto throughput;
- aplicação antiga que continuará lendo arquivos localmente por NFS;
- parceiros que enviam arquivos por SFTP;
- retenção de backup em “fitas” por sete anos.

Defina RPO/RTO e marque o que é migração pontual ou integração contínua.

## 3. Cálculo da janela — 4 min

Calcule o limite otimista:

```text
80 TB × 8 / 0,5 Gbit/s = __________ segundos = __________ dias contínuos
Com janela de 12 h/dia = aproximadamente __________ dias
```

Adicione 25% de margem para overhead/retries e compare com a data-limite. Como
a conta é nova em 2026, não presuma que Snowball pode ser solicitado; registre
DataSync, Data Transfer Terminal/parceiro e aumento temporário de link como
alternativas a validar.

## 4. Diagrama — 9 min

Complete e justifique cada seta:

```text
NFS on-prem --DataSync/alternativa física--> S3 (fonte durável)
      |                                      |
      +-- S3 File Gateway/cache <------------+
                                             |
                                             +-- FSx for Lustre -- render farm

parceiros --SFTP--> Transfer Family --> S3/prefixo por parceiro

software de backup --iSCSI VTL--> Tape Gateway --> archive
```

Para cada componente, anote:

| Componente | Protocolo | Dados principais | Cache/staging | Encryption/identity | Custo |
|---|---|---|---|---|---|
| DataSync |  |  |  |  |  |
| S3 File Gateway |  |  |  |  |  |
| FSx for Lustre |  |  |  |  |  |
| Transfer Family |  |  |  |  |  |
| Tape Gateway |  |  |  |  |  |

## 5. Testes de decisão — 5 min

Troque um requisito por vez:

1. SMB + ACLs Windows + AD → ____________________
2. migração NetApp preservando recursos ONTAP → ____________________
3. NFS compartilhado Linux elástico, sem engine especializada → __________
4. cópia única de milhões de arquivos, com verificação → __________________
5. volume iSCSI com working set local e dados primários na AWS → __________
6. novo cliente solicita Snowball em 2026 → _______________________________
7. novo cliente pede cache local para FSx for Windows → ____________________

## 6. Segurança, custo e cleanup — 3 min

- Separe role do DataSync, role do Transfer user e acesso do filesystem.
- Marque TLS, encryption at rest, logs e checksum/verificação.
- Liste custos por hora, GB, request, backup e transferência entre AZ/Region.
- Defina alarmes/budget antes de uma futura PoC.
- Faça inventário final; deve ser idêntico ao inicial.

```text
Recursos criados: zero / investigar
Inventário final igual ao inicial: sim / não
Serviço com maior risco de custo ocioso: ____________________
Decisão que requer validar disponibilidade comercial: ____________________
```

## Validação e resultado esperado

O desenho distingue interface, movimentação e armazenamento; explica cada
serviço por requisito; incorpora as mudanças da Snow Family e do FSx File
Gateway; inclui segurança, janela, custo e zero recursos provisionados.

## Conexão com o exame

O exercício converte palavras decisivas em interface e serviço: SMB/AD,
Lustre/HPC, VTL, cópia online e SFTP. A prova oferece serviços que parecem
“mover ou armazenar”, mas somente um preserva o protocolo e o padrão de
operação solicitado.

## Referências oficiais

- [Decisão de storage](https://docs.aws.amazon.com/pdfs/decision-guides/latest/storage-on-aws-how-to-choose/storage-on-aws-how-to-choose.pdf)
- [DataSync on-premises](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-on-premises-storage.html)
- [Storage Gateway](https://docs.aws.amazon.com/storagegateway/)
- [Mudança do FSx File Gateway](https://docs.aws.amazon.com/filegateway/latest/filefsxw/create-file-gateway.html)
- [Mudança do Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html)
