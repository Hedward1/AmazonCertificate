# B22 — Segredos, proteção de aplicações e fundamentos de VPC

**Data planejada:** 19/08/2026<br>
**Nível:** iniciante absoluto<br>
**Comece pelas aulas da Udemy:** [roteiro B22 — aulas 301–326](../../02_Planejamento/Roteiro_de_Aulas_por_Dia_SAA-C03.md#b22); Nenhuma aula é pulada.<br>
**Quizzes:** Q23<br>
**Domínios oficiais:** 1 — Secure; 3 — High-Performing<br>
**Tarefas:** 1.2, 1.3 e 3.4 principais; 2.2 e 4.4 secundárias<br>
**Pré-requisito:** B21 — IAM avançado e KMS

## 1. Objetivos de aprendizagem

1. Escolher Secrets Manager.
2. Distinguir ACM, KMS e CloudHSM.
3. Posicionar WAF e Shield.
4. Reconhecer Firewall Manager.
5. Comparar GuardDuty, Inspector e Macie.
6. Calcular blocos CIDR.
7. Explicar VPC, subnet, route table e IGW.
8. Distinguir subnet pública de recurso público.
9. Desenhar saída privada por NAT.
10. Comparar security group e NACL.

## 2. Como estudar as aulas deste bloco

| Aulas | Tratamento |
|---|---|
| 301–312 | Segredos, certificados e serviços de proteção |
| 313–321 | CIDR, VPC, subnets, IGW e route tables |
| 322–325 | Bastion e NAT instance; entender trade-offs |
| 326 | NAT Gateway; estudar preço e não criar |
| Q23 | Fazer ao final |

Use as aulas para o primeiro mapa, este capítulo para consolidar decisões, o laboratório para praticar e as questões para diagnosticar lacunas.

## 3. Vocabulário essencial

| Termo | Significado no cenário |
|---|---|
| secret | credencial ou valor sensível |
| rotation | substituição controlada de secret |
| certificate | identidade TLS |
| HSM | hardware de proteção de chaves |
| web ACL | conjunto de regras WAF |
| CIDR | rede e tamanho de prefixo |
| subnet | faixa de VPC em uma AZ |
| route table | decisão de caminho |
| IGW | gateway de internet da VPC |
| ephemeral ports | portas de retorno em fluxos stateless |

## 4. Modelo mental

Para cada cenário, siga esta sequência:

1. identifique o requisito principal;
2. marque restrições e superlativos;
3. determine escopo regional, zonal ou global;
4. avalie segurança e resiliência;
5. avalie performance e escala;
6. compare operação e custo;
7. elimine opções que violam uma restrição;
8. escolha serviço e configuração.

## 5. Fundamentos e decisões

### 5.1 Ponto 1

Secrets Manager armazena secrets cifrados.
### 5.2 Ponto 2

Secrets Manager suporta versionamento e rotação.
### 5.3 Ponto 3

Use Secrets Manager quando rotação gerenciada é requisito.
### 5.4 Ponto 4

Parameter Store serve configuração e segredo simples.
### 5.5 Ponto 5

ACM provisiona e renova certificados para integrações compatíveis.
### 5.6 Ponto 6

ACM não substitui KMS.
### 5.7 Ponto 7

CloudHSM oferece HSM single-tenant sob controle do cliente.
### 5.8 Ponto 8

KMS é a resposta padrão para integração criptográfica AWS.
### 5.9 Ponto 9

WAF filtra HTTP e HTTPS na camada 7.
### 5.10 Ponto 10

WAF pode usar IP, URI, header, padrões e rate rules.
### 5.11 Ponto 11

Shield Standard oferece proteção DDoS básica automática.
### 5.12 Ponto 12

Shield Advanced é assinatura paga com recursos adicionais.
### 5.13 Ponto 13

Firewall Manager aplica políticas centralmente em organização.
### 5.14 Ponto 14

GuardDuty detecta ameaças por sinais de conta e rede.
### 5.15 Ponto 15

Inspector identifica vulnerabilidades e exposição em workloads suportados.
### 5.16 Ponto 16

Macie descobre dados sensíveis no S3.
### 5.17 Ponto 17

CloudTrail continua sendo registro de atividade de API.
### 5.18 Ponto 18

Uma VPC é regional.
### 5.19 Ponto 19

Uma subnet pertence a uma Availability Zone.
### 5.20 Ponto 20

Um prefixo /24 contém 256 endereços totais.
### 5.21 Ponto 21

A AWS reserva cinco endereços IPv4 em cada subnet.
### 5.22 Ponto 22

CIDRs sobrepostos impedem várias conectividades.
### 5.23 Ponto 23

A rota local atende comunicação interna da VPC.
### 5.24 Ponto 24

Subnet pública tem rota ao Internet Gateway.
### 5.25 Ponto 25

Instância em subnet pública ainda precisa de IP e security controls.
### 5.26 Ponto 26

Internet Gateway anexado sem rota não cria acesso.
### 5.27 Ponto 27

No modo de disponibilidade **zonal** (o modo clássico e padrão), um NAT Gateway público fica em subnet pública e usa Elastic IP.
### 5.28 Ponto 28

No desenho zonal, a route table privada aponta a saída IPv4 para o NAT Gateway da mesma AZ; um NAT por AZ evita dependência entre zonas e cobrança de tráfego inter-AZ.
### 5.29 Ponto 29

O **Regional NAT Gateway**, disponível desde 2025, é associado à VPC em vez de a uma subnet, não exige subnet pública e expande automaticamente a capacidade pelas AZs onde há workloads; atualmente ele oferece conectividade pública, não private NAT.
### 5.30 Ponto 30

Nenhum dos modos de NAT Gateway aceita conexão iniciada da internet. NAT instance continua sendo uma alternativa autogerenciada em EC2 e exige source/destination check desabilitado.
### 5.31 Ponto 31

Security group é stateful e contém allow.
### 5.32 Ponto 32

NACL é stateless, usa allow e deny por ordem.
### 5.33 Ponto 33

Retorno em NACL precisa de regra e portas apropriadas.
### 5.34 Ponto 34

Session Manager pode eliminar bastion quando pré-requisitos existem.

## 6. Tabela de decisão

| Requisito dominante | Escolha inicial | Motivo |
|---|---|---|
| Rotação de senha RDS | Secrets Manager | lifecycle de secret |
| TLS em ALB | ACM | certificado gerenciado |
| HSM single-tenant | CloudHSM | controle dedicado |
| SQL injection | WAF | camada HTTP |
| DDoS básico | Shield Standard | proteção automática |
| Política em contas | Firewall Manager | administração central |
| Threat detection | GuardDuty | sinais gerenciados |
| Vulnerabilidade | Inspector | workload e CVE |
| PII no S3 | Macie | classificação de dados |
| Saída IPv4 privada | NAT Gateway zonal ou regional | NAT gerenciado; escolher o modo conforme resiliência e topologia |

## 7. Cenários resolvidos


### Cenário resolvido 1 — Credencial RDS

- **Contexto:** Aplicação busca senha em runtime.
- **Requisito:** Rotação automática e auditoria.
- **Decisão:** Secrets Manager com IAM e KMS mínimos.
- **Por quê:** Oferece lifecycle específico de secrets.
- **Por que não:** Parâmetro String em template expõe valor.
- **Trade-off:** Há cobrança por secret e chamadas.
- **Validação:** Testar aplicação com versões durante rotação.
- **Custo/cleanup:** Excluir apenas secret criado e considerar janela de recovery.
- **Variação:** Parameter Store cabe sem rotação gerenciada.

### Cenário resolvido 2 — Aplicação web

- **Contexto:** Ataques incluem SQL injection e alto volume.
- **Requisito:** Filtrar padrões HTTP e mitigar DDoS.
- **Decisão:** WAF na integração e Shield conforme nível exigido.
- **Por quê:** Cada controle atua em risco diferente.
- **Por que não:** Security group não inspeciona SQL injection.
- **Trade-off:** Regras gerenciadas e Shield Advanced custam.
- **Validação:** Usar count mode antes de block em regra nova.
- **Custo/cleanup:** Web ACL, rules e requests geram cobrança.
- **Variação:** Firewall Manager centraliza em múltiplas contas.

### Cenário resolvido 3 — Três camadas

- **Contexto:** ALB público, aplicação e banco privados.
- **Requisito:** Entrada controlada e saída IPv4 da aplicação.
- **Decisão:** IGW e public subnets para ALB; para a saída da aplicação, escolher NAT zonal por AZ ou Regional NAT Gateway.
- **Por quê:** Rotas separam entrada e saída.
- **Por que não:** IGW na VPC não torna banco público.
- **Trade-off:** No modo zonal, um NAT por AZ melhora resiliência e evita tráfego inter-AZ, mas aumenta o número de gateways; o modo regional simplifica a alta disponibilidade e dispensa subnet pública para o NAT, mantendo cobrança de NAT e tráfego.
- **Validação:** Traçar ida e volta, SGs e NACLs.
- **Custo/cleanup:** Não criar NAT no laboratório.
- **Variação:** Gateway endpoint evita NAT para S3 e DynamoDB.

## 8. Fluxo de projeto

1. Escolher CIDR sem sobreposição.
2. Dividir subnets por AZ e função.
3. Associar route tables.
4. Anexar IGW se necessário.
5. Criar rota pública apenas onde necessário.
6. Desenhar NAT sem provisionar.
7. Aplicar SG por camada.
8. Usar NACL como guardrail.
9. Evitar inbound administrativo.
10. Usar Secrets Manager para credenciais rotacionadas.
11. Adicionar WAF no ponto HTTP compatível.
12. Validar todo caminho de ida e volta.

## 9. Custos e cleanup

- Secrets Manager pode cobrar.
- Private CA e CloudHSM são caros.
- WAF e Shield Advanced cobram.
- GuardDuty, Inspector e Macie podem cobrar.
- NAT Gateway, zonal ou regional, cobra por hora e dados processados; confirme a tabela de preços da Região antes de provisionar.
- VPC e estruturas básicas não cobram por hora por si.
- Public IPv4 gera cobrança.
- Não criar NAT Gateway no LAB.

Faça inventário antes e depois. Exclua somente recursos criados por você e identificados pelo bloco. Nunca tente zerar a conta removendo recursos preexistentes.

## 10. Armadilhas de prova

- Subnet pública não torna instância pública.
- IGW sem rota não basta.
- NAT não recebe conexão iniciada externamente.
- Não generalize que todo NAT Gateway fica em subnet pública: isso descreve o NAT zonal público; o Regional NAT Gateway é associado à VPC.
- SG é stateful e sem deny.
- NACL é stateless e ordenada.
- ACM não é KMS.
- Macie não procura CVE.
- Inspector não classifica PII.
- Shield Standard e Advanced não são iguais.
- Cinco IPv4 são reservados por subnet.

## 11. Checklist de domínio

- [ ] Consigo explicar os objetivos sem consultar.
- [ ] Reconstruo a tabela de decisão.
- [ ] Resolvo os três cenários.
- [ ] Sei justificar duas alternativas erradas.
- [ ] Conheço custos residuais.
- [ ] Completei o laboratório.
- [ ] Respondi às dez questões antes do gabarito.
- [ ] Registrei erros e baixa confiança.
- [ ] Agendei D+2 e D+7.

## 12. Recuperação ativa

1. Compare Parameter Store e Secrets Manager.
2. Compare KMS e CloudHSM.
3. Posicione WAF, Shield e Firewall Manager.
4. Associe GuardDuty, Inspector e Macie.
5. Calcule /24, /26 e /28.
6. Explique subnet pública.
7. Desenhe NAT IPv4.
8. Compare SG e NACL.
9. Explique portas efêmeras.
10. Liste custos da arquitetura.

## 13. Ligações com outros blocos

- A identidade limita quem inicia a operação.
- A rede limita por onde o dado passa.
- A criptografia protege conteúdo e chaves.
- A observabilidade prova comportamento e mudanças.
- Resiliência deve corresponder ao objetivo do negócio.
- Custo deve incluir recursos ociosos e tráfego.
- Operação gerenciada reduz tarefas, mas não remove responsabilidade.
- Os simulados combinam estes conceitos.

## 14. Referências oficiais AWS

- [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [ACM](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)
- [CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)
- [AWS WAF and Shield](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)
- [GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
- [Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [VPC subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
- [Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
- [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
- [Regional NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html)
- [SG versus NACL](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)

**Referências verificadas em:** 01/08/2026.

## 15. Continue o bloco

- [Laboratório B22](../../05_Laboratorios/LAB_B22_VPC_Publica_Privada_sem_NAT_Gateway.md)
- [Questões B22](../../04_Questoes_e_Revisoes/Blocos/B22_Questoes.md)
- [Gabarito B22](../../04_Questoes_e_Revisoes/Blocos/B22_Gabarito.md)
- [Checklist e revisões B22](../../06_Progresso/B22_Checklist_e_Revisoes.md)
