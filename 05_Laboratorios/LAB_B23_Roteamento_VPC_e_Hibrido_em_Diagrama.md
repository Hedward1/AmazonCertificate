# LAB B23 — Roteamento VPC e conectividade híbrida em diagrama

**Tempo:** 25 minutos<br>
**Modo:** diagrama e simulação<br>
**Custo:** USD 0,00 esperado<br>
**Capítulo:** [abrir](../03_Guia_do_Estudante/Capitulos/B23_Redes_Avancadas_e_Conectividade_Hibrida.md)

## 1. Objetivos

1. Traçar ida e volta.
2. Comparar peering e TGW.
3. Comparar endpoints.
4. Ler Flow Logs conceituais.
5. Desenhar VPN.
6. Desenhar Direct Connect.
7. Desenhar dual-stack.
8. Concluir sem recursos.

## 2. Resultado esperado

- Três route tables simuladas.
- Matriz endpoints.
- Topologia híbrida.
- Fluxo IPv6 egress-only.
- Nenhum recurso criado.
- Custo zero.

## 3. Custo

USD 0,00 esperado.
- Confira preços e Region.
- Recursos anexos podem cobrar.
- Não crie itens não previstos.
- Cleanup faz parte do laboratório.
- Não confunda read-only com ausência de recursos preexistentes.

## 4. Preflight

1. Confirme identidade não root.
2. Confirme Region.
3. Conte NAT gateways.
4. Conte interface endpoints.
5. Conte TGW e VPN.
6. Não clique em Create.
7. Não crie endpoint.
8. Não crie Flow Logs.
9. Não crie TGW ou VPN.
10. Prepare editor local.

### Critério para prosseguir

- [ ] Identidade não root.
- [ ] Region confirmada.
- [ ] Inventário válido.
- [ ] Preço conferido.
- [ ] Cleanup reservado.

## 5. Arquitetura

- VPC A 10.10.0.0/16.
- VPC B 10.20.0.0/16.
- VPC C 10.30.0.0/16.
- Peering A-B.
- Peering B-C.
- Sem trânsito A-C.
- Gateway endpoint S3.
- Interface endpoint conceitual.
- TGW como alternativa hub.
- Egress-only IGW para IPv6.

## 6. Execução


### Etapa 1 — Peering

1. Desenhe A-B.
2. Adicione rotas nos dois lados.
3. Desenhe B-C.
4. Adicione rotas nos dois lados.
5. Tente A-C.
6. Marque que peering não é transitivo.
7. Verifique ausência de sobreposição.
8. Substitua malha por TGW.

### Etapa 2 — Endpoints

1. Liste S3 e DynamoDB.
2. Escolha gateway endpoint.
3. Ligue a route table.
4. Adicione endpoint policy.
5. Escolha serviço PrivateLink.
6. Desenhe interface endpoint.
7. Adicione security group.
8. Compare custo.

### Etapa 3 — Híbrido

1. Desenhe customer gateway.
2. Desenhe dois túneis VPN.
3. Desenhe virtual private gateway.
4. Desenhe Direct Connect.
5. Adicione virtual interface.
6. Combine DX e VPN.
7. Adicione TGW.
8. Marque rotas de ida e volta.

### Etapa 4 — IPv6 e diagnóstico

1. Adicione CIDR IPv6.
2. Desenhe rota pública ao IGW.
3. Desenhe private route ao egress-only IGW.
4. Adicione SG.
5. Adicione NACL.
6. Liste DNS e rota.
7. Liste serviço ouvindo.
8. Escolha Flow Logs para metadados.

## 7. Validação

- [ ] Três route tables simuladas.
- [ ] Matriz endpoints.
- [ ] Topologia híbrida.
- [ ] Fluxo IPv6 egress-only.
- [ ] Nenhum recurso criado.
- [ ] Custo zero.
- [ ] AccessDenied não virou zero.
- [ ] Nenhum dado sensível foi copiado.
- [ ] Inventário final comparado.

## 8. Cleanup

1. Nenhum recurso novo deveria existir.
2. Feche assistentes.
3. Não exclua preexistentes.
4. Repita contagens.
5. Investigue diferenças.
6. Remova notas locais sensíveis.
7. Encerre autenticação.
8. Confirme custo.
9. Registre limitações.
10. Marque cleanup.

### Checklist de cleanup

- [ ] Nenhum recurso novo.
- [ ] Preexistentes preservados.
- [ ] Inventário final válido.
- [ ] Sessão encerrada.

## 9. Tratamento de falhas

- AccessDenied é não verificado.
- Region errada exige voltar.
- Não altere preexistentes.
- Contagem mudou: investigue.
- Login expirado: renove pela mesma rota.
- Preço indisponível: permaneça read-only.
- Dúvida de propriedade: não exclua.
- Timeout: priorize cleanup.

## 10. Evidência permitida

Registre Region, modo, contagens, decisões, custo e cleanup.

Não registre:
- account ID ou ARN.
- access key, secret ou token.
- IDs, IPs ou nomes preexistentes.
- conteúdo de logs ou secrets.
- screenshots sensíveis.

## 11. Conexão com o exame

- Traçar ida e volta.
- Comparar peering e TGW.
- Comparar endpoints.
- Ler Flow Logs conceituais.
- Desenhar VPN.
- Desenhar Direct Connect.
- Desenhar dual-stack.
- Concluir sem recursos.

Justifique a escolha e as alternativas eliminadas.

## 12. Referências oficiais

- [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
- [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html)
- [Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
- [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
- [Egress-only IGW](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html)

**Verificado em:** 01/08/2026.
