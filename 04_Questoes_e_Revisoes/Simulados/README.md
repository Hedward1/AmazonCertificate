# Simulados finais — pacote autoral versionado

Este diretório contém os três simulados autorais completos. Questões,
gabaritos, relatórios e bancos estruturados estão no GitHub por decisão do
estudante.

> **Evite spoilers:** para realizar uma tentativa válida, abra somente
> `Questoes.md`. Deixe `Gabarito.md` e o banco JSON fechados até terminar os
> 130 minutos e registrar suas respostas.

## Acesso rápido

| Simulado | Uso planejado | Questões | Relatório |
|---|---|---|---|
| SIM-A | 26/08 — tentativa agendada | [Iniciar](SIM-A/Questoes.md) | [Preencher](SIM-A/Relatorio.md) |
| SIM-B | Extra após SIM-C ou substituto da Udemy | [Iniciar](SIM-B/Questoes.md) | [Preencher](SIM-B/Relatorio.md) |
| SIM-C | 31/08 — tentativa e decisão de prontidão | [Iniciar](SIM-C/Questoes.md) | [Preencher](SIM-C/Relatorio.md) |

<details>
<summary><strong>Depois da tentativa: gabaritos e bancos estruturados</strong></summary>

| Simulado | Gabarito comentado | Banco JSON |
|---|---|---|
| SIM-A | [Abrir](SIM-A/Gabarito.md) | [JSON](Bancos/SIM-A.json) |
| SIM-B | [Abrir](SIM-B/Gabarito.md) | [JSON](Bancos/SIM-B.json) |
| SIM-C | [Abrir](SIM-C/Gabarito.md) | [JSON](Bancos/SIM-C.json) |

</details>

O [manifesto auditável](manifesto_simulados.json) registra caminhos, hashes,
distribuições e estado de validação.

## Composição de cada simulado

- 65 questões inéditas em inglês;
- 130 minutos;
- 20 questões do domínio 1, 17 do domínio 2, 15 do domínio 3 e 13 do domínio 4;
- cobertura das 14 tarefas oficiais;
- 49 questões `single`, 12 `multi-2` e 4 `multi-3`;
- 13 fundamentais, 29 situacionais e 23 integradas;
- 10 básicas, 35 intermediárias e 20 avançadas;
- gabarito comentado com análise individual de todas as alternativas;
- relatório por domínio, tarefa e questão.

Essa composição aproxima os pesos 30%/26%/24%/20% sem apresentar uma
proporção de formatos como oficial. A AWS publica os pesos dos domínios e
informa que o exame contém questões de múltipla escolha e múltiplas respostas.

## Ordem da fase final

- **26/08 — SIM-A:** primeira tentativa autoral agendada.
- **28/08 — Practice Udemy:** tentativa da plataforma; ela não é o SIM-B.
- **31/08 — SIM-C:** segunda tentativa autoral agendada e decisão de prontidão.
- **SIM-B:** tentativa adicional depois da correção do SIM-C, ou substituto
  somente se o practice exam da Udemy estiver indisponível.

Não execute Practice Udemy e SIM-B no mesmo dia.

## Organização

```text
Simulados/
├── README.md
├── manifesto_simulados.json
├── Bancos/
│   ├── SIM-A.json
│   ├── SIM-B.json
│   └── SIM-C.json
├── SIM-A/{Questoes,Gabarito,Relatorio}.md
├── SIM-B/{Questoes,Gabarito,Relatorio}.md
└── SIM-C/{Questoes,Gabarito,Relatorio}.md
```

## Geração e validação

Execute a partir da raiz:

```powershell
python .\99_Ferramentas\scripts\gerar_simulados.py
python .\99_Ferramentas\scripts\gerar_simulados.py --validate-only
python .\99_Ferramentas\scripts\validar_material_completo.py
```

Os validadores conferem contagens, domínios, tarefas, formatos, alternativas,
respostas, análises, fontes oficiais, hashes e semelhança entre as 195
questões. Também rejeitam concentração previsível das letras corretas,
conjuntos repetitivos em múltiplas respostas e excesso de alternativas
corretas identificáveis apenas por serem as mais longas.

## Practice exam da Udemy

O practice exam reservado da Udemy não foi copiado, extraído nem reproduzido.
A publicação deste diretório abrange somente SIM-A, SIM-B e SIM-C, produzidos
para este projeto a partir do escopo oficial.

## Referências oficiais

- [SAA-C03 — tipos de resposta e pesos](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html)
- [Domínio 1](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html)
- [Domínio 2](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html)
- [Domínio 3](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html)
- [Domínio 4](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html)
