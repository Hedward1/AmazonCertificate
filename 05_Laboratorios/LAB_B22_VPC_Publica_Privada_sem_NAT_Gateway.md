# LAB B22 — VPC pública e privada sem NAT Gateway

**Tempo:** 25 minutos<br>
**Modo:** criação controlada<br>
**Custo:** USD 0,00 esperado para estruturas básicas<br>
**Capítulo:** [abrir](../03_Guia_do_Estudante/Capitulos/B22_Segredos_Protecao_de_Aplicacoes_e_Fundamentos_VPC.md)

## 1. Objetivos

1. Criar VPC dedicada.
2. Criar duas subnets.
3. Anexar IGW.
4. Criar route tables.
5. Criar security group.
6. Criar NACL.
7. Provar ausência de NAT.
8. Excluir tudo.

## 2. Resultado esperado

- VPC saa-b22-lab temporária.
- Public subnet com rota ao IGW.
- Private subnet sem default route.
- Nenhuma EC2, EIP ou NAT.
- Controles com prefixo saa-b22.
- Todos os recursos removidos.

## 3. Custo

USD 0,00 esperado para estruturas básicas.
- Confira preços e Region.
- Recursos anexos podem cobrar.
- Não crie itens não previstos.
- O cleanup faz parte do laboratório.
- Não confunda recurso básico com conta gratuita.

## 4. Preflight

1. Confirme identidade não root.
2. Escolha Region com duas AZs.
3. Valide CIDR 10.22.0.0/16.
4. Confira preços VPC.
5. Conte VPCs e NAT gateways.
6. Use tag Lab B22.
7. Use prefixo saa-b22.
8. Não use VPC preexistente.
9. Não crie EC2, EIP, endpoint ou NAT.
10. Reserve dez minutos para cleanup.

### Critério para prosseguir

- [ ] Identidade não root.
- [ ] Region confirmada.
- [ ] Inventário válido.
- [ ] Preço conferido.
- [ ] Cleanup reservado.

## 5. Arquitetura

- VPC 10.22.0.0/16.
- Public subnet 10.22.1.0/24.
- Private subnet 10.22.2.0/24.
- IGW anexado.
- Public route 0.0.0.0/0 para IGW.
- Private route somente local.
- SG sem inbound amplo.
- Custom NACL na private subnet.
- Nenhuma rota NAT.
- Nenhum public IPv4.

## 6. Execução


### Etapa 1 — Rede

1. Crie VPC saa-b22-lab.
2. Use 10.22.0.0/16.
3. Desabilite criação automática de NAT.
4. Crie saa-b22-public-a.
5. Use 10.22.1.0/24.
6. Crie saa-b22-private-b.
7. Use 10.22.2.0/24.
8. Não habilite auto-assign public IPv4.

### Etapa 2 — Internet e rotas

1. Crie saa-b22-igw.
2. Anexe à VPC do lab.
3. Crie saa-b22-public-rt.
4. Associe à public subnet.
5. Adicione default para IGW.
6. Crie saa-b22-private-rt.
7. Associe à private subnet.
8. Não adicione default privada.

### Etapa 3 — Controles

1. Crie saa-b22-app-sg.
2. Não adicione inbound internet.
3. Não crie workload.
4. Crie saa-b22-private-nacl.
5. Adicione regras somente se compreendidas.
6. Associe à private subnet.
7. Identifique default NACL.
8. Não crie WAF ou firewall.

### Etapa 4 — Validar

1. Abra resource map.
2. Confirme duas subnets.
3. Confirme rota pública.
4. Confirme ausência de rota NAT.
5. Confirme zero NAT B22.
6. Confirme zero EIP novo.
7. Confirme zero EC2 nova.
8. Inicie cleanup.

## 7. Validação

- [ ] VPC saa-b22-lab temporária.
- [ ] Public subnet com rota ao IGW.
- [ ] Private subnet sem default route.
- [ ] Nenhuma EC2, EIP ou NAT.
- [ ] Controles com prefixo saa-b22.
- [ ] Todos os recursos removidos.
- [ ] AccessDenied não virou zero.
- [ ] Nenhum segredo foi copiado.
- [ ] Inventário final comparado.

## 8. Cleanup

1. Reassocie a private subnet à default NACL.
2. Exclua saa-b22-private-nacl.
3. Exclua saa-b22-app-sg.
4. Desassocie route tables customizadas.
5. Exclua saa-b22-private-rt.
6. Exclua saa-b22-public-rt.
7. Destaque saa-b22-igw.
8. Exclua saa-b22-igw.
9. Exclua as duas subnets.
10. Exclua saa-b22-lab.
11. Aguarde confirmações.
12. Compare VPCs e NAT gateways ao inventário.

### Checklist de cleanup

- [ ] Recursos do lab removidos ou nenhum criado.
- [ ] Preexistentes preservados.
- [ ] Inventário final válido.
- [ ] Sessão encerrada.

## 9. Tratamento de falhas

- AccessDenied é não verificado.
- Region errada exige voltar.
- Não altere preexistentes.
- Dependência: remova só a dependência do lab.
- Contagem externa mudou: registre.
- Login expirado: renove pela mesma rota.
- Preço indisponível: permaneça read-only.
- Dúvida de propriedade: não exclua.

## 10. Evidência permitida

Registre Region, modo, contagens, decisões, custo e cleanup.

Não registre:
- account ID ou ARN.
- access key, secret ou token.
- IDs, IPs ou nomes preexistentes.
- conteúdo de logs ou secrets.
- screenshots sensíveis.

## 11. Conexão com o exame

- Criar VPC dedicada.
- Criar duas subnets.
- Anexar IGW.
- Criar route tables.
- Criar security group.
- Criar NACL.
- Provar ausência de NAT.
- Excluir tudo.

Justifique a escolha e as alternativas eliminadas.

## 12. Referências oficiais

- [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
- [Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
- [NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
- [SG e NACL](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)

**Verificado em:** 01/08/2026.
