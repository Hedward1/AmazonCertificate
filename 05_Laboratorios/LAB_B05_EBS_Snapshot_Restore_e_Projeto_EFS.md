# LAB B05 — EBS, snapshot, restauração e projeto EFS

**Tempo líquido:** 45 minutos<br>
**Aulas:** 61–71<br>
**Capítulo:** [B05](../03_Guia_do_Estudante/Capitulos/B05_EBS_Instance_Store_EFS_e_Fundamentos_de_HA.md)<br>
**Modo:** criação controlada de EC2/EBS; EFS somente em diagrama<br>
**Custo esperado:** pequeno, variável por Region; limite operacional sugerido: **menos de USD 1** com cleanup no mesmo dia

## 1. Resultado esperado

Criar um volume EBS criptografado pequeno, anexá-lo a uma instância temporária, gravar um arquivo, criar snapshot, restaurar outro volume e validar o conteúdo. Depois, remover todos os recursos e desenhar EFS Regional sem provisioná-lo.

Ao terminar, você deverá ter:

- comprovado a restrição de mesma AZ para attach de EBS;
- diferenciado volume montável de snapshot regional;
- validado a propagação da criptografia na restauração;
- comparado hash do arquivo original e restaurado;
- desenhado EFS Regional com mount targets e security groups;
- removido todos os recursos criados pelo laboratório;
- registrado evidências sem identificadores sensíveis.

## 2. Conexão com o exame

| Decisão observada | Tarefa SAA-C03 |
|---|---|
| bloco persistente e tipo de volume | 3.1 |
| restauração entre AZs | 2.2 |
| encryption e KMS | 1.3 |
| storage compartilhado e custo | 3.1 / 4.1 |

O objetivo não é memorizar cliques. Em cada etapa, diga em voz alta qual
restrição arquitetural explica a escolha.

## 3. Preflight obrigatório (5 min)

- [ ] usar uma Region única e anotar somente o nome dela;
- [ ] confirmar identidade não root e orçamento/alertas ativos;
- [ ] abrir [preços do EBS](https://aws.amazon.com/ebs/pricing/) e estimar volume + snapshot;
- [ ] confirmar que a conta permite EC2, EBS e KMS;
- [ ] inventariar instâncias, volumes, snapshots e AMIs antes de criar;
- [ ] criar tags `Project=SAAC03`, `Lab=B05` e `Expires=AAAA-MM-DD`, substituindo
  `AAAA-MM-DD` pela data planejada para o cleanup (preferencialmente o mesmo dia);
- [ ] escolher uma instância pequena elegível ao benefício vigente ou a menor opção permitida;
- [ ] nunca reutilizar nem excluir recursos sem a tag `Lab=B05`.

Se o console não mostrar estimativa aceitável, faça o modo diagrama: desenhe cada estado e execute apenas `Describe*`.

## 4. Arquitetura

```text
EC2 temporária ── EBS A criptografado ── snapshot S
                                           └── EBS B restaurado (mesma AZ da EC2)

Projeto sem criação: EC2 AZ-a ─┐
                               ├─ NFS 2049 ─ EFS Regional
                    EC2 AZ-b ──┘             + mount targets
```

## 5. Procedimento (25 min)

1. Lance uma instância Amazon Linux 2023 temporária na configuração mínima autorizada, sem porta SSH pública; prefira Session Manager se a role já existir. A instância e o novo volume devem ficar na mesma AZ.
2. Crie um volume `gp3` pequeno com encryption habilitada e tags do laboratório. Anexe como data volume.
3. No sistema, identifique o device com `lsblk`. Não assuma que o nome exibido no console será idêntico.
4. Se for um volume vazio, crie filesystem `xfs`, monte em `/mnt/b05` e grave `evidencia-b05.txt` com texto não sensível. **Nunca formate um device que já contenha filesystem.**
5. Execute `sync`, desmonte o filesystem e crie um snapshot do volume A. Aguarde estado `completed` antes de depender dele.
6. Crie o volume B a partir do snapshot **na AZ da instância**. Anexe, monte em `/mnt/b05-restore` sem formatar e leia o arquivo.
7. Registre apenas: tipo, tamanho, criptografado sim/não, AZ igual/diferente e hash do arquivo. Não registre account ID, ARN, IP ou resource ID.
8. No papel, projete EFS Regional: duas AZs, um mount target por AZ usada, SG do EFS permitindo TCP 2049 somente do SG dos clientes, access point e lifecycle para IA. Não crie o filesystem.

### Pontos de parada

- Se `lsblk -f` mostrar filesystem no device, não execute `mkfs`.
- Se a AZ do volume diferir da instância, não tente contornar; recrie na AZ
  correta.
- Se o snapshot ainda estiver `pending`, não conte a restauração como validada.
- Se a KMS key não estiver autorizada, não altere sua policy para “fazer
  funcionar”; registre a barreira.
- Se a estimativa ultrapassar o orçamento, passe ao modo diagrama.

## 6. Validação (5 min)

- [ ] hash do arquivo original igual ao restaurado;
- [ ] volume e instância na mesma AZ;
- [ ] snapshot criou volume novo, não moveu o anterior;
- [ ] ambos os volumes marcados como criptografados;
- [ ] diagrama EFS contém mount targets, SG e porta 2049;
- [ ] consigo explicar por que o snapshot não é um volume montável.

## 7. Cleanup seguro (10 min)

1. Desmonte os dois filesystems.
2. Termine somente a instância marcada `Lab=B05`.
3. Aguarde volumes ficarem `available`; exclua somente volumes `Lab=B05`, inclusive o restaurado.
4. Exclua o snapshot `Lab=B05` depois de confirmar que não será usado.
5. Se uma AMI foi criada por engano, desregistre-a e avalie separadamente os snapshots associados.
6. Compare o inventário final ao inicial. O número de recursos B05 deve ser zero.
7. Encerre a sessão autenticada/CLI.

**Parada de segurança:** se qualquer recurso não tiver a tag esperada ou a propriedade estiver ambígua, não exclua; registre o achado.

## 8. Evidência e reflexão

| Evidência não sensível | Resultado |
|---|---|
| estimativa aprovada | |
| hash original = restaurado | |
| volumes/snapshots B05 após cleanup | deve ser 0 |
| EFS criado | não |

Explique: por que a restauração pode ocorrer em outra AZ, mas o attach não; quando `io2` venceria `gp3`; por que Multi-Attach não atende ao diagrama EFS.

## 9. Solução de problemas

| Sintoma | Verificação segura |
|---|---|
| volume não aparece para attach | confirme AZ e estado `available` |
| device não tem o nome esperado | use `lsblk`; Nitro pode apresentar NVMe |
| mount falha | confirme filesystem, device e diretório |
| hash diverge | confirme que montou o volume restaurado e usou `sync` |
| delete do volume falha | desmonte, detach e aguarde `available` |
| snapshot não pode ser excluído | verifique dependências e ownership; não force |

## 10. Referências oficiais

- [Create an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html)
- [Attach an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-attaching-volume.html)
- [Create an EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-snapshot.html)
- [Restore an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-restoring-volume.html)
- [EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html)
- [EFS network access](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-access.html)
