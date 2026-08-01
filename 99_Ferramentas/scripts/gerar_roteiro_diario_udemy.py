#!/usr/bin/env python3
"""Gera o roteiro diário da Udemy a partir do inventário consolidado.

O mapeamento usa ``numero_aula`` para as aulas e a seção para os quizzes.
``indice_item`` serve apenas como identidade e ordenação, pois deixa de
coincidir com o número da aula depois do primeiro quiz.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INVENTORY_PATH = (
    PROJECT_ROOT
    / "01_Fontes"
    / "Udemy"
    / "Inventario_Curso_Udemy_SAA-C03.csv"
)
OUTPUT_PATH = (
    PROJECT_ROOT
    / "02_Planejamento"
    / "Roteiro_de_Aulas_por_Dia_SAA-C03.md"
)


@dataclass(frozen=True)
class Block:
    code: str
    date: str
    sections: str
    first_lesson: int
    last_lesson: int
    reserved_minutes: int
    quiz_sections: tuple[int, ...]
    watch: str
    consult: str = ""
    skip: str = ""
    notes: tuple[str, ...] = ()


BLOCKS = (
    Block(
        "B01",
        "25/07/2026",
        "seções 1–3 e seção 4 parcial",
        1,
        18,
        63,
        (),
        "`008`, `010–012` e `014–018`",
        "`003–004`, `007` e `009`",
        "`001–002`, `005–006` e `013`",
        (
            "Como `001–013` já aparecem concluídas, tente recuperar `008` e "
            "`010–012` sem consulta e reassista somente o que não conseguir explicar.",
            "O quiz de IAM fica para o B02, depois do término da seção 4.",
        ),
    ),
    Block(
        "B02",
        "27/07/2026",
        "fim da seção 4 e início da seção 5",
        19,
        35,
        59,
        (4,),
        "`019`, `022` e `025–035`",
        "`020–021`, pois mostram a CLI em outros sistemas operacionais",
        "`023–024`, pois CloudShell está explicitamente fora do escopo",
        (
            "Na aula `018`, do bloco anterior, estude access keys e AWS CLI; "
            "trate SDK apenas como contexto.",
            "Transfira o tempo economizado nas aulas puladas para recuperação ativa "
            "ou questões; o dia continua com 180 minutos líquidos.",
        ),
    ),
    Block(
        "B03",
        "28/07/2026",
        "fim da seção 5",
        36,
        46,
        62,
        (5,),
        "`036–037`, `040` e `042–046`",
        "`038–039` e `041`, por serem alternativas de sistema operacional ou troubleshooting",
    ),
    Block(
        "B04",
        "29/07/2026",
        "seção 6 e início da seção 7",
        47,
        60,
        53,
        (6,),
        "`047–060`",
    ),
    Block(
        "B05",
        "30/07/2026",
        "fim da seção 7 e início da seção 8",
        61,
        71,
        51,
        (7,),
        "`061–071`",
    ),
    Block(
        "B06",
        "31/07/2026",
        "seção 8 parcial",
        72,
        79,
        46,
        (),
        "`072–079`",
        notes=("O quiz de ELB/ASG fica para o B07, depois do término da seção 8.",),
    ),
    Block(
        "B07",
        "01/08/2026",
        "fim da seção 8",
        80,
        86,
        37,
        (8,),
        "`080–086`",
    ),
    Block(
        "B08",
        "03/08/2026",
        "seção 9 completa",
        87,
        100,
        70,
        (9,),
        "`087–100`",
    ),
    Block(
        "B09",
        "04/08/2026",
        "seção 10 parcial",
        101,
        110,
        51,
        (),
        "`101–110`",
        notes=("O quiz de Route 53 fica para o B10, depois do término da seção 10.",),
    ),
    Block(
        "B10",
        "05/08/2026",
        "fim da seção 10 e seção 11 completa",
        111,
        127,
        77,
        (10, 11),
        "`111–127`",
    ),
    Block(
        "B11",
        "06/08/2026",
        "seções 12–13 completas",
        128,
        149,
        80,
        (12, 13),
        "`128–149`",
    ),
    Block(
        "B12",
        "07/08/2026",
        "seções 14–15 completas",
        150,
        171,
        86,
        (14, 15),
        "`150–171`",
    ),
    Block(
        "B13",
        "08/08/2026",
        "seção 16 completa",
        172,
        181,
        37,
        (16,),
        "`172–181`",
    ),
    Block(
        "B14",
        "10/08/2026",
        "seção 17 parcial",
        182,
        190,
        44,
        (),
        "`182–190`",
        notes=("O quiz de mensageria fica para o B15, depois do término da seção 17.",),
    ),
    Block(
        "B15",
        "11/08/2026",
        "fim da seção 17 e início da seção 18",
        191,
        202,
        68,
        (17,),
        "`191–202`",
    ),
    Block(
        "B16",
        "12/08/2026",
        "fim da seção 18 e início da seção 19",
        203,
        216,
        53,
        (18,),
        "`203–216`",
    ),
    Block(
        "B17",
        "13/08/2026",
        "fim da seção 19",
        217,
        225,
        48,
        (19,),
        "`217–225`",
    ),
    Block(
        "B18",
        "14/08/2026",
        "seções 20–21 e início da seção 22",
        226,
        244,
        66,
        (20, 21),
        "`226–244`",
        notes=("O quiz de Data & Analytics fica para o B19, depois do término da seção 22.",),
    ),
    Block(
        "B19",
        "15/08/2026",
        "fim da seção 22 e seção 23 completa",
        245,
        263,
        49,
        (22, 23),
        "`245–260` e `262–263`",
        skip="`261`, pois Amazon Personalize está explicitamente fora do escopo",
        notes=(
            "A aula 245 usa o nome histórico QuickSight. O [guia oficial SAA-C03]"
            "(https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03-domain3.html) "
            "cita **Amazon QuickSuite**; a [documentação atual do produto]"
            "(https://docs.aws.amazon.com/quick/) usa **Amazon Quick**, e **Amazon "
            "Quick Sight** é seu componente de BI e visualização.",
            "O quiz de Machine Learning continua útil; desconsidere somente uma "
            "eventual questão exclusivamente sobre Personalize.",
            "Transfira os 2 minutos economizados para recuperação ativa ou questões.",
        ),
    ),
    Block(
        "B20",
        "17/08/2026",
        "seção 24 completa e início da seção 25",
        264,
        282,
        86,
        (24,),
        "`264–282`",
        notes=("O quiz de IAM avançado fica para o B21, depois do término da seção 25.",),
    ),
    Block(
        "B21",
        "18/08/2026",
        "fim da seção 25 e início da seção 26",
        283,
        300,
        88,
        (25,),
        "`283–300`",
        notes=("O quiz de segurança e criptografia fica para o B22.",),
    ),
    Block(
        "B22",
        "19/08/2026",
        "fim da seção 26 e início da seção 27",
        301,
        326,
        89,
        (26,),
        "`301–326`",
        notes=("O quiz de VPC fica para o B24, depois do término da seção 27.",),
    ),
    Block(
        "B23",
        "20/08/2026",
        "seção 27 parcial",
        327,
        345,
        87,
        (),
        "`327–345`",
        notes=("A seção 27 e o quiz de VPC terminam no B24.",),
    ),
    Block(
        "B24",
        "21/08/2026",
        "fim da seção 27 e seções 28–29 completas",
        346,
        366,
        95,
        (27, 28, 29),
        "`346–366`",
        notes=(
            "Os três quizzes pertencem ao B24. Se o timebox terminar, conclua-os "
            "no início do B25 sem refazê-los.",
        ),
    ),
    Block(
        "B25",
        "22/08/2026",
        "seções 30–33, sem o practice exam",
        367,
        396,
        89,
        (30, 31),
        "`367–385` e `387–388`",
        "`386` e `389–393`; reveja os itens administrativos perto da prova",
        "`394–396`, por serem encerramento, trilhas e bônus",
        (
            "O practice exam não pertence ao B25; ele está reservado ao evento "
            "**Practice Udemy** de 28/08. Não confundir com o banco autoral privado "
            "`SIM-B`, que é um recurso adicional e permanece fechado durante essa tentativa.",
        ),
    ),
)


SKIP_LESSONS = {
    1,
    2,
    5,
    6,
    13,
    23,
    24,
    261,
    394,
    395,
    396,
}
CONSULT_LESSONS = {
    3,
    4,
    7,
    20,
    21,
    38,
    39,
    41,
    386,
    389,
    390,
    391,
    392,
    393,
}
ACCELERATE_LESSONS = {9}
EXPLICITLY_OUT_OF_SCOPE = {23, 24, 261}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="valida o inventário e confirma que o arquivo gerado está atualizado",
    )
    return parser.parse_args()


def read_inventory() -> list[dict[str, str]]:
    with INVENTORY_PATH.open("r", encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


def lesson_number(item: dict[str, str]) -> int | None:
    raw = item["numero_aula"].strip()
    return int(raw) if raw.isdigit() else None


def item_index(item: dict[str, str]) -> int:
    return int(item["indice_item"])


def section_number(item: dict[str, str]) -> int:
    return int(item["secao"])


def block_items(
    inventory: list[dict[str, str]], block: Block
) -> list[dict[str, str]]:
    selected = []
    for item in inventory:
        number = lesson_number(item)
        if number is not None and block.first_lesson <= number <= block.last_lesson:
            selected.append(item)
        elif (
            item["tipo"] == "quiz"
            and section_number(item) in block.quiz_sections
        ):
            selected.append(item)
    return sorted(selected, key=item_index)


def treatment(item: dict[str, str]) -> str:
    if item["tipo"] == "quiz":
        return "QUIZ"
    number = lesson_number(item)
    if number in SKIP_LESSONS:
        return "PULAR"
    if number in CONSULT_LESSONS:
        return "CONSULTAR"
    if number in ACCELERATE_LESSONS:
        return "ACELERAR"
    return "ASSISTIR"


def escape_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ").strip()


def item_label(item: dict[str, str]) -> str:
    number = lesson_number(item)
    if number is not None:
        return f"`{number:03d}`"
    match = re.match(r"Teste\s+(\d+)", item["titulo"])
    if match:
        return f"`Q{int(match.group(1)):02d}`"
    return f"`I{item_index(item):03d}`"


def quiz_summary(items: list[dict[str, str]]) -> str:
    quizzes = [item for item in items if item["tipo"] == "quiz"]
    if not quizzes:
        return "nenhum neste bloco"
    return "; ".join(
        f"{item_label(item)} — {escape_cell(item['titulo'])}" for item in quizzes
    )


def validate_inventory(inventory: list[dict[str, str]]) -> None:
    problems = []
    indices = [item_index(item) for item in inventory]
    if len(inventory) != 425 or sorted(indices) != list(range(1, 426)):
        problems.append("o inventário deve conter os índices 1–425 exatamente uma vez")

    numbered = [lesson_number(item) for item in inventory]
    numbered = [number for number in numbered if number is not None]
    if sorted(numbered) != list(range(1, 397)):
        problems.append("as aulas numeradas devem formar o intervalo 1–396")

    quizzes = [item for item in inventory if item["tipo"] == "quiz"]
    if len(quizzes) != 28 or sorted(map(section_number, quizzes)) != list(
        range(4, 32)
    ):
        problems.append("devem existir 28 quizzes, um para cada seção 4–31")

    simulations = [item for item in inventory if item["tipo"] == "simulado"]
    if len(simulations) != 1 or item_index(simulations[0]) != 422:
        problems.append("o único simulado deve ser o item 422")

    assigned_indices = []
    for block in BLOCKS:
        assigned_indices.extend(item_index(item) for item in block_items(inventory, block))
    if len(assigned_indices) != 424 or len(set(assigned_indices)) != 424:
        problems.append("B01–B25 devem receber 424 itens únicos")
    if set(indices) - set(assigned_indices) != {422}:
        problems.append("somente o simulado I422 pode ficar fora de B01–B25")

    if EXPLICITLY_OUT_OF_SCOPE - set(numbered):
        problems.append("as aulas 23, 24 e 261 devem existir no inventário")

    if problems:
        raise ValueError("; ".join(problems))


def render_block(inventory: list[dict[str, str]], block: Block) -> list[str]:
    items = block_items(inventory, block)
    lines = [
        f'<a id="{block.code.lower()}"></a>',
        "",
        f"## {block.code} — {block.date}",
        "",
        f"**Escopo bruto:** {block.sections}; aulas "
        f"`{block.first_lesson:03d}–{block.last_lesson:03d}`.  ",
        f"**Tempo reservado no cronograma:** {block.reserved_minutes} minutos de curso.  ",
        f"**Assistir/praticar:** {block.watch}.  ",
    ]
    if block.consult:
        lines.append(f"**Acelerar/consultar:** {block.consult}.  ")
    if block.skip:
        lines.append(f"**Pular:** {block.skip}.  ")
    lines.append(f"**Quiz:** {quiz_summary(items)}.")
    for note in block.notes:
        lines.extend(["", f"> {note}"])
    lines.extend(
        [
            "",
            "<details>",
            f"<summary>Títulos e tratamento dos {len(items)} itens deste bloco</summary>",
            "",
            "| Aula/item | Tratamento | Tipo | Título original do curso |",
            "|---:|---|---|---|",
        ]
    )
    for item in items:
        lines.append(
            f"| {item_label(item)} | `{treatment(item)}` | "
            f"{escape_cell(item['tipo'])} | {escape_cell(item['titulo'])} |"
        )
    lines.extend(["", "</details>", ""])
    return lines


def render(inventory: list[dict[str, str]]) -> str:
    lines = [
        "# Roteiro diário das aulas da Udemy — AWS SAA-C03",
        "",
        "**Finalidade:** mostrar exatamente quais aulas, artigos e quizzes acompanham "
        "cada bloco do material.  ",
        "**Fonte:** inventário local de 425 itens extraído do curso.  ",
        "**Cobertura:** 396 aulas numeradas + 28 quizzes + 1 practice exam, sem "
        "lacunas ou duplicações.",
        "",
        "## Como usar",
        "",
        "1. Abra o bloco do dia pelo cronograma.",
        "2. Assista somente os itens marcados como `ASSISTIR`; use os hands-on como "
        "demonstração ou junto do laboratório do bloco.",
        "3. Use `CONSULTAR` e `ACELERAR` apenas conforme a necessidade indicada.",
        "4. Não gaste tempo de prova com itens `PULAR`.",
        "5. Faça o `QUIZ` no tempo **Q** do cronograma e registre erros; ele não entra "
        "novamente no tempo reservado ao curso.",
        "",
        "> `PULAR` não tem sempre o mesmo motivo. As aulas 023, 024 e 261 estão "
        "explicitamente fora do escopo oficial. Os demais itens com essa marca são "
        "administrativos, encerramento ou conteúdo dispensável para a prova.",
        "",
        "> Os tempos diários usam os totais consolidados do curso. A soma das "
        "durações inteiras de cada linha do CSV fica 15 minutos maior por causa do "
        "arredondamento item a item; isso não representa aula ausente.",
        "",
        "## Índice dos blocos",
        "",
        " | ".join(
            f"[{block.code}](#{block.code.lower()})" for block in BLOCKS
        ),
        "",
    ]
    for block in BLOCKS:
        lines.extend(render_block(inventory, block))

    simulation = next(item for item in inventory if item["tipo"] == "simulado")
    lines.extend(
        [
            '<a id="fase-final"></a>',
            "",
            "## Fase final — 24/08 a 31/08/2026",
            "",
            "- **24/08:** nenhuma aula nova; consolidação e correção.",
            "- **25/08:** nenhuma aula nova; revisão por domínio.",
            "- **26/08 — SIM A:** nenhuma aula nova; simulado autoral.",
            "- **27/08:** nenhuma aula nova; correção aprofundada.",
            f"- **28/08 — Practice Udemy:** {item_label(simulation)} — "
            f"{escape_cell(simulation['titulo'])}; o `SIM-B` autoral fica reservado "
            "como tentativa adicional.",
            "- **29/08:** nenhuma aula nova; correção do Practice Udemy.",
            "- **31/08 — SIM C:** nenhuma aula nova; simulado autoral e decisão de "
            "prontidão.",
            "",
            "O `SIM-B` autoral privado pode ser usado depois da correção do SIM C "
            "ou como substituto somente se o practice exam da Udemy estiver "
            "indisponível. Não realize os dois no mesmo dia e não abra previamente "
            "nenhum dos bancos.",
            "",
            "> O practice exam aparece somente no evento Practice Udemy de 28/08. "
            "Ele não deve ser aberto durante o B25 nem durante a revisão anterior.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    inventory = read_inventory()
    validate_inventory(inventory)
    expected = render(inventory)

    if args.check:
        if not OUTPUT_PATH.exists():
            print(f"ERRO: arquivo ausente: {OUTPUT_PATH}", file=sys.stderr)
            return 1
        current = OUTPUT_PATH.read_text(encoding="utf-8")
        if current != expected:
            print(
                "ERRO: o roteiro está desatualizado; execute o script sem --check",
                file=sys.stderr,
            )
            return 1
        print("OK: 425 itens mapeados; roteiro atualizado.")
        return 0

    current = OUTPUT_PATH.read_text(encoding="utf-8") if OUTPUT_PATH.exists() else None
    if current == expected:
        print(f"Sem alterações: {OUTPUT_PATH}")
        return 0
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="\n") as target:
        target.write(expected)
    print(f"Gerado: {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
