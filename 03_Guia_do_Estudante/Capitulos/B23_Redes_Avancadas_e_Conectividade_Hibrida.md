# B23 — Redes avançadas, endpoints, conectividade híbrida e IPv6

**Data planejada:** 20/08/2026<br>
**Nível:** iniciante absoluto<br>
**Comece pelas aulas da Udemy:** [roteiro B23 — aulas 327–345](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b23); Nenhuma aula é pulada.<br>
**Quizzes:** Nenhum; Q24 fica no B24<br>
**Domínios oficiais:** 3 — High-Performing; 1 — Secure<br>
**Tarefas:** 3.4 principal; 1.2, 2.2 e 4.4 secundárias<br>
**Pré-requisito:** B22 — segurança e fundamentos de VPC

## 1. Objetivos de aprendizagem

1. Traçar um pacote de ponta a ponta.
2. Reforçar SG e NACL.
3. Explicar peering não transitivo.
4. Comparar endpoints gateway e interface.
5. Interpretar VPC Flow Logs.
6. Comparar VPN e Direct Connect.
7. Escolher Transit Gateway.
8. Reconhecer Traffic Mirroring.
9. Projetar dual-stack.
10. Usar egress-only Internet Gateway.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 327–330 | NAT, SG e NACL |
| 331–336 | Peering, endpoints e Flow Logs |
| 337–341 | VPN, Direct Connect e Transit Gateway; somente arquitetura |
| 342 | Traffic Mirroring |
| 343–345 | IPv6 e egress-only IGW |
| Q24 | Não fazer ainda; seção termina no B24 |

Use aulas, capítulo, laboratório e questões nessa ordem. Não copie credenciais nem crie recursos pagos para reproduzir telas.

## 3. Vocabulário essencial

| Termo | Significado |
|---|---|
| longest prefix match | rota mais específica |
| peering | ligação privada entre duas VPCs |
| transitive routing | rotear por um terceiro domínio |
| PrivateLink | acesso privado a serviço por interface endpoint |
| Flow Logs | metadados de fluxos |
| customer gateway | representação AWS do roteador do cliente |
| virtual interface | VIF de Direct Connect |
| attachment | conexão com Transit Gateway |
| dual-stack | IPv4 e IPv6 juntos |
| egress-only | somente conexões IPv6 iniciadas internamente |

## 4. Modelo mental

1. Identifique o requisito.
2. Marque restrições.
3. Determine escopo.
4. Avalie segurança.
5. Avalie resiliência.
6. Avalie performance.
7. Compare operação e custo.
8. Elimine violações.

## 5. Fundamentos e decisões

### 5.1 Ponto 1

Route table escolhe o target da rota mais específica.
### 5.2 Ponto 2

Security controls não criam rota.
### 5.3 Ponto 3

O caminho de retorno também precisa existir.
### 5.4 Ponto 4

DNS, rota, NACL, SG e serviço devem estar coerentes.
### 5.5 Ponto 5

Peering conecta duas VPCs por endereços privados.
### 5.6 Ponto 6

Cada lado do peering precisa de rotas.
### 5.7 Ponto 7

Peering não oferece transitive routing.
### 5.8 Ponto 8

CIDRs IPv4 sobrepostos impedem peering.
### 5.9 Ponto 9

Peering é simples para poucas relações.
### 5.10 Ponto 10

Uma malha de peerings cresce rapidamente.
### 5.11 Ponto 11

Gateway endpoint usa route table.
### 5.12 Ponto 12

Gateway endpoints clássicos atendem S3 e DynamoDB.
### 5.13 Ponto 13

Gateway endpoint não cobra por hora.
### 5.14 Ponto 14

Interface endpoint cria ENIs privadas.
### 5.15 Ponto 15

Interface endpoint usa security groups.
### 5.16 Ponto 16

Interface endpoint cobra por hora e dados.
### 5.17 Ponto 17

Endpoint policy não substitui IAM ou resource policy.
### 5.18 Ponto 18

Flow Logs podem existir em VPC, subnet ou ENI.
### 5.19 Ponto 19

Flow Logs mostram metadados como IP, porta e ACCEPT ou REJECT.
### 5.20 Ponto 20

Flow Logs não capturam payload.
### 5.21 Ponto 21

Traffic Mirroring copia pacotes para target de análise.
### 5.22 Ponto 22

Site-to-Site VPN usa IPsec sobre a internet.
### 5.23 Ponto 23

Uma conexão VPN normalmente fornece dois túneis.
### 5.24 Ponto 24

Direct Connect oferece conectividade dedicada.
### 5.25 Ponto 25

Direct Connect não fornece IPsec automaticamente.
### 5.26 Ponto 26

Direct Connect e VPN podem ser combinados.
### 5.27 Ponto 27

Virtual private gateway é associado à VPC.
### 5.28 Ponto 28

Direct Connect gateway amplia associações suportadas.
### 5.29 Ponto 29

Transit Gateway é hub regional.
### 5.30 Ponto 30

Transit Gateway oferece roteamento transitivo.
### 5.31 Ponto 31

TGW route tables permitem segmentação.
### 5.32 Ponto 32

Attachments e dados processados geram cobrança.
### 5.33 Ponto 33

IPv6 em VPC usa endereços globalmente únicos.
### 5.34 Ponto 34

Internet Gateway permite caminho IPv6 bidirecional.
### 5.35 Ponto 35

Egress-only IGW bloqueia novas conexões IPv6 iniciadas externamente.
### 5.36 Ponto 36

Dual-stack exige rotas e regras para as duas pilhas.

### Cápsula de decisão — AWS Client VPN

- **Problema que resolve:** fornecer acesso remoto seguro e gerenciado para usuários individuais alcançarem recursos em uma VPC ou na rede on-premises.
- **Tarefas SAA-C03 relacionadas:** 1.1 e 3.4 — controlar acesso seguro e selecionar conectividade híbrida adequada ao consumidor.
- **Quando escolher:** funcionários ou prestadores conectam notebooks de qualquer local com cliente baseado em OpenVPN e precisam de autenticação e autorização por rede ou grupo.
- **Quando não escolher:** para conectar uma rede corporativa inteira à VPC; nesse caso, Site-to-Site VPN ou Direct Connect costuma representar melhor o requisito.
- **Serviço semelhante:** Site-to-Site VPN liga redes por túneis IPsec; Client VPN termina sessões de usuários e usa TLS/OpenVPN.
- **Armadilha:** autenticar o usuário não basta. O destino precisa de rota, regra de autorização explícita e security groups compatíveis; por padrão não há regras de autorização e o acesso é negado.
- **Questão situacional extra (fora do banco de 250):** cem funcionários remotos precisam acessar subnets privadas usando seus notebooks, com autenticação federada e permissão diferente por grupo. Qual serviço atende com menor operação?
- **Resposta curta:** AWS Client VPN, configurando endpoint, target network, rotas e regras de autorização por grupo.
- **Referência oficial:** [What is AWS Client VPN?](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html) e [authorization rules](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html)

## 6. Tabela de decisão

| Requisito | Escolha | Motivo |
|---|---|---|
| Duas VPCs simples | VPC peering | ligação direta |
| Muitas VPCs transitivas | Transit Gateway | hub regional |
| S3 privado | Gateway endpoint | rota e sem hora |
| Serviço por private IP | Interface endpoint | PrivateLink |
| Metadados ACCEPT REJECT | Flow Logs | registro de fluxo |
| Cópia de pacote | Traffic Mirroring | inspeção profunda |
| IPsec rápido | Site-to-Site VPN | internet cifrada |
| Usuários remotos individuais | AWS Client VPN | acesso gerenciado baseado em OpenVPN |
| Link dedicado | Direct Connect | conectividade previsível |
| Dedicado e IPsec | DX mais VPN | requisitos combinados |
| Saída IPv6 | Egress-only IGW | entrada não iniciada |

## 7. Cenários resolvidos


### Cenário resolvido 1 — Muitas VPCs

- **Contexto:** Dezenas de VPCs e dois datacenters.
- **Requisito:** Roteamento transitivo e segmentado.
- **Decisão:** Transit Gateway com route tables separadas.
- **Por quê:** Hub reduz malha e permite política por attachment.
- **Por que não:** Peering não é transitivo.
- **Trade-off:** TGW cobra attachments e dados.
- **Validação:** Testar rotas de ida e volta por segmento.
- **Custo/cleanup:** Diagrama apenas no laboratório.
- **Variação:** Cloud WAN pode entrar em desenho global mais amplo.

### Cenário resolvido 2 — S3 privado

- **Contexto:** Instâncias privadas acessam apenas S3.
- **Requisito:** Evitar internet e NAT para esse caminho.
- **Decisão:** Gateway endpoint de S3.
- **Por quê:** Adiciona target a route tables sem NAT.
- **Por que não:** Interface endpoint pode funcionar em casos específicos, mas cobra e não é a escolha padrão da pista.
- **Trade-off:** Endpoint, IAM e bucket policies precisam alinhar.
- **Validação:** Validar DNS, rota e policy.
- **Custo/cleanup:** Gateway endpoint não cobra por hora.
- **Variação:** DynamoDB também suporta gateway endpoint.

### Cenário resolvido 3 — Dedicado e cifrado

- **Contexto:** Datacenter exige caminho dedicado.
- **Requisito:** Performance previsível e IPsec.
- **Decisão:** Direct Connect combinado com VPN compatível.
- **Por quê:** DX atende dedicação e VPN adiciona IPsec.
- **Por que não:** DX sozinho não cifra com IPsec.
- **Trade-off:** Mais componentes e tempo de implantação.
- **Validação:** Testar ambos túneis e failover.
- **Custo/cleanup:** Portas, transferência e VPN cobram.
- **Variação:** VPN pela internet pode ser backup.

## 8. Fluxo de projeto

1. Resolver DNS.
2. Escolher rota mais específica.
3. Validar target.
4. Validar rota de retorno.
5. Validar NACL de ida.
6. Validar portas efêmeras de retorno.
7. Validar security groups.
8. Validar serviço ouvindo.
9. Validar endpoint policy.
10. Validar IAM e resource policy.
11. Usar Flow Logs para metadados.
12. Usar packet capture apenas quando necessário.

## 9. Custos e cleanup

- NAT Gateway cobra hora e dados.
- Interface endpoint cobra hora e dados.
- Transit Gateway cobra attachment e processamento.
- VPN cobra conexão e transferência.
- Direct Connect cobra porta e transferência.
- Flow Logs geram custo de entrega e consulta.
- Traffic Mirroring gera processamento e targets.
- Não provisionar nenhum desses itens no laboratório.

Faça inventário antes e depois. Exclua apenas recursos criados pelo bloco.

## 10. Armadilhas

- Peering não é transitivo.
- SG não cria rota.
- Gateway endpoint não serve qualquer serviço.
- Interface endpoint usa SG.
- Flow Logs não captura payload.
- Direct Connect não é IPsec automático.
- Configure os dois túneis VPN.
- Egress-only IGW é IPv6.
- NAT Gateway é pista IPv4.
- Uma pilha dual-stack não garante a outra.

## 11. Checklist

- [ ] Objetivos explicados sem consulta.
- [ ] Tabela reconstruída.
- [ ] Três cenários resolvidos.
- [ ] Trade-offs justificados.
- [ ] Custos identificados.
- [ ] Laboratório concluído.
- [ ] Dez questões respondidas.
- [ ] Erros registrados.
- [ ] D+2 e D+7 agendados.

## 12. Recuperação ativa

1. Trace um pacote entre VPCs.
2. Explique A-B, B-C e A-C.
3. Compare endpoints.
4. Compare Flow Logs e Mirroring.
5. Compare VPN e DX.
6. Desenhe DX mais VPN.
7. Desenhe TGW segmentado.
8. Explique dual-stack.
9. Explique egress-only IGW.
10. Liste custos por hop.

## 13. Ligações

- Identidade limita o principal.
- Rede limita o caminho.
- Criptografia protege dados.
- Observabilidade fornece evidência.
- Resiliência atende objetivos.
- Performance deve ser medida.
- Custo inclui recursos ociosos.
- Simulados integram blocos.

## 14. Referências oficiais AWS

- [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html)
- [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html)
- [Gateway endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-endpoints.html)
- [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
- [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)
- [Client VPN authorization rules](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html)
- [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
- [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
- [Traffic Mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html)
- [Egress-only IGW](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html)

**Referências verificadas em:** 01/08/2026.

## 15. Continue o bloco

- [Laboratório B23](../../05_Laboratorios/LAB_B23_Roteamento_VPC_e_Hibrido_em_Diagrama.md)
- [Questões B23](../../04_Questoes_e_Revisoes/Blocos/B23_Questoes.md)
- [Gabarito B23](../../04_Questoes_e_Revisoes/Blocos/B23_Gabarito.md)
- [Checklist e revisões B23](../../06_Progresso/B23_Checklist_e_Revisoes.md)
