# Simulados finais — entrega privada

Este diretório público contém somente o contrato de geração e o manifesto dos
simulados autorais. As questões, respostas e relatórios ficam em
`../Simulados_Privados/`, caminho ignorado pelo Git, para que o estudante não
veja o conteúdo antes da execução.

## Pacote previsto

Cada um de `SIM-A`, `SIM-B` e `SIM-C` possui:

- 65 questões inéditas em inglês;
- 130 minutos;
- 20 questões do domínio 1, 17 do domínio 2, 15 do domínio 3 e 13 do domínio 4;
- todas as 14 tarefas, com a distribuição explícita registrada no manifesto;
- 49 questões `single`, 12 `multi-2` e 4 `multi-3`;
- gabarito comentado separado;
- relatório de resultado por domínio e tarefa.

Essa composição aproxima os pesos 30%/26%/24%/20% sem afirmar uma proporção
oficial de formatos. A AWS publica os pesos dos domínios e informa apenas que o
exame contém questões de múltipla escolha e múltiplas respostas.

O contrato aceita quatro opções/uma resposta, cinco ou seis opções/duas
respostas (`Choose TWO`) e seis opções/três respostas (`Select THREE`).

## Ordem da fase final

- **26/08 — `SIM-A`:** tentativa autoral privada agendada.
- **28/08 — Practice Udemy:** tentativa da plataforma, mantida inédita até o
  horário previsto; ela não é o `SIM-B`.
- **31/08 — `SIM-C`:** tentativa autoral privada agendada e decisão de
  prontidão.
- **`SIM-B`:** tentativa autoral privada adicional, para depois da correção do
  `SIM-C`, ou substituto somente se o practice exam da Udemy estiver
  indisponível.

Não execute Practice Udemy e `SIM-B` no mesmo dia e não abra previamente
questões ou gabaritos de nenhuma tentativa.

## Arquivos privados esperados

O gerador lê:

```text
04_Questoes_e_Revisoes/Simulados_Privados/Bancos/SIM-A.json
04_Questoes_e_Revisoes/Simulados_Privados/Bancos/SIM-B.json
04_Questoes_e_Revisoes/Simulados_Privados/Bancos/SIM-C.json
```

E grava, para cada simulado:

```text
SIM-X_Questoes.md
SIM-X_Gabarito.md
SIM-X_Relatorio.md
```

Use:

```powershell
python .\99_Ferramentas\scripts\gerar_simulados_privados.py
python .\99_Ferramentas\scripts\gerar_simulados_privados.py --validate-only
```

O segundo comando não renderiza novamente. Ambos verificam contagem, domínio,
tarefa, formato, alternativas, respostas, análise de todos os distratores,
fontes oficiais e repetição literal ou similaridade excessiva entre quaisquer
questões dos três simulados.

## Esquema mínimo de uma questão

```json
{
  "id": "SIM-A-01",
  "domain": 1,
  "task": "1.1",
  "format": "single",
  "type": "situational",
  "difficulty": "intermediate",
  "instruction": "Choose ONE.",
  "stem": "Scenario and requirements...",
  "options": {"A": "...", "B": "...", "C": "...", "D": "..."},
  "answers": ["B"],
  "rationales": {"A": "...", "B": "...", "C": "...", "D": "..."},
  "central_requirement": "...",
  "decisive_words": "...",
  "reusable_rule": "...",
  "references": ["https://docs.aws.amazon.com/..."]
}
```

## Practice exam da Udemy

O practice exam reservado da Udemy não é copiado, extraído nem reproduzido. Ele
continua inédito até 28/08. O `SIM-B` autoral é um recurso privado adicional e
não substitui o direito autoral nem o conteúdo do practice exam da plataforma.

## Referências oficiais

- [SAA-C03 — tipos de resposta e pesos](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html)
- [Domínio 1](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain1.html)
- [Domínio 2](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain2.html)
- [Domínio 3](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html)
- [Domínio 4](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain4.html)
