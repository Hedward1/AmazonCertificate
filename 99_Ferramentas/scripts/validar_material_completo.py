#!/usr/bin/env python3
"""Valida a integridade editorial e estrutural do material SAA-C03."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
CHAPTERS = ROOT / "03_Guia_do_Estudante" / "Capitulos"
LABS = ROOT / "05_Laboratorios"
QUESTION_BLOCKS = ROOT / "04_Questoes_e_Revisoes" / "Blocos"
PROGRESS = ROOT / "06_Progresso"

EXPECTED_LANGUAGES = {
    **{block: (6, 4) for block in range(1, 8)},
    **{block: (5, 5) for block in range(8, 11)},
    **{block: (4, 6) for block in range(11, 14)},
    **{block: (2, 8) for block in range(14, 20)},
    **{block: (0, 10) for block in range(20, 26)},
}

EXPECTED_DATES = {
    1: ("25/07/2026", "27/07/2026", "01/08/2026"),
    2: ("27/07/2026", "29/07/2026", "03/08/2026"),
    3: ("28/07/2026", "30/07/2026", "04/08/2026"),
    4: ("29/07/2026", "31/07/2026", "05/08/2026"),
    5: ("30/07/2026", "01/08/2026", "06/08/2026"),
    6: ("31/07/2026", "03/08/2026", "07/08/2026"),
    7: ("01/08/2026", "03/08/2026", "08/08/2026"),
    8: ("03/08/2026", "05/08/2026", "10/08/2026"),
    9: ("04/08/2026", "06/08/2026", "11/08/2026"),
    10: ("05/08/2026", "07/08/2026", "12/08/2026"),
    11: ("06/08/2026", "08/08/2026", "13/08/2026"),
    12: ("07/08/2026", "10/08/2026", "14/08/2026"),
    13: ("08/08/2026", "10/08/2026", "15/08/2026"),
    14: ("10/08/2026", "12/08/2026", "17/08/2026"),
    15: ("11/08/2026", "13/08/2026", "18/08/2026"),
    16: ("12/08/2026", "14/08/2026", "19/08/2026"),
    17: ("13/08/2026", "15/08/2026", "20/08/2026"),
    18: ("14/08/2026", "17/08/2026", "21/08/2026"),
    19: ("15/08/2026", "17/08/2026", "22/08/2026"),
    20: ("17/08/2026", "19/08/2026", "24/08/2026"),
    21: ("18/08/2026", "20/08/2026", "25/08/2026"),
    22: ("19/08/2026", "21/08/2026", "26/08/2026"),
    23: ("20/08/2026", "22/08/2026", "27/08/2026"),
    24: ("21/08/2026", "24/08/2026", "28/08/2026"),
    25: ("22/08/2026", "24/08/2026", "29/08/2026"),
}

LOCAL_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
QUESTION_HEADING_RE = re.compile(r"^### (B\d{2}-\d{2})$", re.MULTILINE)
ANSWER_HEADING_RE = re.compile(
    r"^## (B\d{2}-\d{2}) — (?:Resposta|Answer)\b", re.MULTILINE
)
ANSWER_KEY_RE = re.compile(
    r"^## (B\d{2}-\d{2}) — (?:Resposta|Answer) ([A-D])$", re.MULTILINE
)
METADATA_ROW_RE = re.compile(
    r"^\| (B\d{2}-\d{2}) \|.*\| (Português|Inglês) \|$", re.MULTILINE
)
OFFICIAL_AWS_RE = re.compile(r"https://(?:docs\.aws\.amazon\.com|aws\.amazon\.com)/")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def word_count(text: str) -> int:
    """Conta palavras Unicode para evitar arquivos inflados apenas com linhas vazias."""
    return len(re.findall(r"\b[\w`-]+\b", text, flags=re.UNICODE))


def one_file(directory: Path, pattern: str, label: str, errors: list[str]) -> Path | None:
    matches = sorted(directory.glob(pattern))
    if len(matches) != 1:
        errors.append(f"{label}: esperado 1 arquivo para {pattern}; encontrado {len(matches)}")
        return None
    return matches[0]


def require_terms(
    text: str, path: Path, groups: tuple[tuple[str, ...], ...], errors: list[str]
) -> None:
    lowered = text.casefold()
    for alternatives in groups:
        if not any(term.casefold() in lowered for term in alternatives):
            errors.append(f"{path.relative_to(ROOT)}: seção ausente ({' / '.join(alternatives)})")


def validate_question_sections(
    text: str, block_code: str, path: Path, errors: list[str]
) -> set[str]:
    matches = list(QUESTION_HEADING_RE.finditer(text))
    ids = {match.group(1) for match in matches}
    expected = {f"{block_code}-{number:02d}" for number in range(1, 11)}
    if ids != expected or len(matches) != 10:
        errors.append(f"{path.relative_to(ROOT)}: IDs de questão diferentes de {block_code}-01..10")
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.end() : end]
        alternatives = re.findall(r"^- ([A-D])\.", section, re.MULTILINE)
        if alternatives != ["A", "B", "C", "D"]:
            errors.append(f"{path.relative_to(ROOT)}: {match.group(1)} não possui A–D exatamente uma vez")
    return ids


def validate_answer_sections(
    text: str,
    block_code: str,
    path: Path,
    errors: list[str],
    *,
    strict: bool,
) -> set[str]:
    matches = list(ANSWER_HEADING_RE.finditer(text))
    ids = {match.group(1) for match in matches}
    expected = {f"{block_code}-{number:02d}" for number in range(1, 11)}
    if ids != expected or len(matches) != 10:
        errors.append(f"{path.relative_to(ROOT)}: respostas diferentes de {block_code}-01..10")
    answer_key = ANSWER_KEY_RE.findall(text)
    if len(answer_key) != 10 or {item_id for item_id, _ in answer_key} != expected:
        errors.append(f"{path.relative_to(ROOT)}: chave de respostas incompleta")
    elif strict:
        counts = {letter: sum(answer == letter for _, answer in answer_key) for letter in "ABCD"}
        if sum(count > 0 for count in counts.values()) < 3 or max(counts.values()) > 4:
            errors.append(
                f"{path.relative_to(ROOT)}: distribuição previsível de respostas {counts}"
            )
    quick_rows = re.findall(
        rf"^\| ({block_code}-\d{{2}}) \| ([A-D]) \|", text, re.MULTILINE
    )
    if len(quick_rows) != 10 or {item_id for item_id, _ in quick_rows} != expected:
        errors.append(f"{path.relative_to(ROOT)}: tabela de respostas rápidas incompleta")
    elif dict(quick_rows) != dict(answer_key):
        errors.append(
            f"{path.relative_to(ROOT)}: tabela rápida e títulos das respostas divergem"
        )
    if not strict:
        return ids
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.end() : end]
        for label in ("A", "B", "C", "D"):
            if not re.search(rf"^- \*\*{label}:\*\*", section, re.MULTILINE):
                errors.append(f"{path.relative_to(ROOT)}: {match.group(1)} sem análise da alternativa {label}")
        require_terms(
            section,
            path,
            (
                ("Requisito central", "Central requirement"),
                ("Palavras decisivas", "Decisive words"),
                ("Regra reutilizável", "Reusable rule"),
                ("Aulas", "Lessons"),
                ("Referência", "Reference"),
            ),
            errors,
        )
    return ids


def validate_block(block: int, errors: list[str]) -> dict[str, Path] | None:
    code = f"B{block:02d}"
    chapter = one_file(CHAPTERS, f"{code}_*.md", code + " capítulo", errors)
    lab = one_file(LABS, f"LAB_{code}_*.md", code + " laboratório", errors)
    questions = QUESTION_BLOCKS / f"{code}_Questoes.md"
    answers = QUESTION_BLOCKS / f"{code}_Gabarito.md"
    checklist = PROGRESS / f"{code}_Checklist_e_Revisoes.md"
    required = (chapter, lab, questions, answers, checklist)
    if chapter is None or lab is None:
        return None
    for path in required:
        if path is not None and not path.is_file():
            errors.append(f"arquivo ausente: {path.relative_to(ROOT)}")
    if any(path is None or not path.is_file() for path in required):
        return None

    chapter_text = read_text(chapter)
    lab_text = read_text(lab)
    question_text = read_text(questions)
    answer_text = read_text(answers)
    checklist_text = read_text(checklist)

    if not chapter_text.startswith(f"# {code} — "):
        errors.append(f"{chapter.relative_to(ROOT)}: H1 fora do padrão '# {code} —'")
    if not lab_text.startswith(f"# LAB {code} — "):
        errors.append(f"{lab.relative_to(ROOT)}: H1 fora do padrão '# LAB {code} —'")
    route_fragment = f"Roteiro_de_Aulas_por_Dia_SAA-C03.md#{code.casefold()}"
    if route_fragment not in chapter_text:
        errors.append(f"{chapter.relative_to(ROOT)}: link ausente para o roteiro {code}")

    minimum_lines = {
        chapter: 200,
        lab: 100,
        questions: 140,
        answers: 150,
        checklist: 75,
    }
    for path, minimum in minimum_lines.items():
        count = len(read_text(path).splitlines())
        if count < minimum:
            errors.append(f"{path.relative_to(ROOT)}: {count} linhas; mínimo editorial {minimum}")

    if block >= 5:
        minimum_words = {
            chapter: 1300,
            lab: 500,
            questions: 550,
            answers: 900,
            checklist: 300,
        }
        for path, minimum in minimum_words.items():
            count = word_count(read_text(path))
            if count < minimum:
                errors.append(
                    f"{path.relative_to(ROOT)}: {count} palavras; mínimo editorial {minimum}"
                )
        scenario_count = len(
            re.findall(r"^###? .*Cenário resolvido", chapter_text, re.MULTILINE | re.IGNORECASE)
        )
        if scenario_count < 2:
            errors.append(
                f"{chapter.relative_to(ROOT)}: {scenario_count} cenário(s) resolvido(s); mínimo 2"
            )
        require_terms(
            chapter_text,
            chapter,
            (
                ("Objetivos de aprendizagem",),
                ("Como estudar", "Aulas deste bloco"),
                ("Cenário resolvido",),
                ("Tabela de decisão", "Comparação"),
                ("Armadilhas",),
                ("Custos", "Custo"),
                ("Recuperação ativa",),
                ("Referências oficiais",),
            ),
            errors,
        )
        require_terms(
            lab_text,
            lab,
            (
                ("Resultado esperado", "Objetivo"),
                ("Custo",),
                ("Preflight", "Pré-requisitos"),
                ("Validação",),
                ("Cleanup", "Limpeza"),
                ("Conexão com o exame",),
                ("Referências oficiais",),
            ),
            errors,
        )
    require_terms(
        checklist_text,
        checklist,
        (("D+2",), ("D+7",), ("Critério de encerramento",)),
        errors,
    )
    for date in EXPECTED_DATES[block]:
        if date not in checklist_text:
            errors.append(f"{checklist.relative_to(ROOT)}: data esperada ausente ({date})")

    question_ids = validate_question_sections(question_text, code, questions, errors)
    answer_ids = validate_answer_sections(
        answer_text, code, answers, errors, strict=block >= 5
    )
    if question_ids != answer_ids:
        errors.append(f"{code}: conjunto de questões e respostas não coincide")

    metadata = METADATA_ROW_RE.findall(question_text)
    metadata_ids = {item_id for item_id, _ in metadata}
    if metadata_ids != question_ids or len(metadata) != 10:
        errors.append(f"{questions.relative_to(ROOT)}: tabela de metadados incompleta")
    portuguese = sum(language == "Português" for _, language in metadata)
    english = sum(language == "Inglês" for _, language in metadata)
    if (portuguese, english) != EXPECTED_LANGUAGES[block]:
        errors.append(
            f"{questions.relative_to(ROOT)}: idiomas PT/EN={portuguese}/{english}; "
            f"esperado {EXPECTED_LANGUAGES[block][0]}/{EXPECTED_LANGUAGES[block][1]}"
        )

    for path, text in ((chapter, chapter_text), (lab, lab_text), (answers, answer_text)):
        if not OFFICIAL_AWS_RE.search(text):
            errors.append(f"{path.relative_to(ROOT)}: nenhuma referência oficial AWS")

    expected_links = {
        chapter: (lab.name, questions.name, answers.name, checklist.name),
        lab: (chapter.name,),
        questions: (answers.name,),
        answers: (questions.name,),
        checklist: (chapter.name, lab.name, questions.name, answers.name),
    }
    for path, names in expected_links.items():
        text = read_text(path)
        for name in names:
            if name not in text:
                errors.append(f"{path.relative_to(ROOT)}: link ausente para {name}")

    return {
        "chapter": chapter,
        "lab": lab,
        "questions": questions,
        "answers": answers,
        "checklist": checklist,
    }


def validate_local_links(errors: list[str]) -> int:
    checked = 0
    for path in ROOT.rglob("*.md"):
        parts = set(path.relative_to(ROOT).parts)
        if ".git" in parts or "html do curso" in path.as_posix():
            continue
        text = read_text(path)
        for match in LOCAL_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "data:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            checked += 1
            resolved = (path.parent / unquote(target)).resolve()
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: link local quebrado -> {target}"
                )
    return checked


def validate_schedule(errors: list[str]) -> None:
    path = ROOT / "02_Planejamento" / "Cronograma_Diario_SAA-C03.md"
    text = read_text(path)
    day_matches = list(re.finditer(r"^#### .+$", text, re.MULTILINE))
    cards = re.findall(r"^> \*\*(?:Comece pelas aulas|Udemy):", text, re.MULTILINE)
    if len(day_matches) != 32 or len(cards) != 32:
        errors.append("cronograma: esperado 32 dias e 32 cartões da Udemy")
    for index, match in enumerate(day_matches):
        end = day_matches[index + 1].start() if index + 1 < len(day_matches) else len(text)
        section = text[match.start() : end]
        minutes = sum(
            int(value)
            for value in re.findall(r"^- \*\*[^*]+ — (\d+) min:", section, re.MULTILINE)
        )
        if minutes != 180:
            errors.append(f"cronograma: {match.group(0)} soma {minutes} minutos")


def validate_indexes(blocks: list[dict[str, Path]], errors: list[str]) -> None:
    """Confirma que os índices principais expõem todos os 25 pacotes."""
    index_expectations = {
        ROOT / "README.md": ("chapter", "lab", "questions", "checklist"),
        CHAPTERS / "README.md": ("chapter",),
        LABS / "README.md": ("lab",),
        QUESTION_BLOCKS / "README.md": ("questions", "answers"),
        PROGRESS / "README.md": ("checklist",),
        ROOT / "04_Questoes_e_Revisoes" / "Apostila_de_Questoes_SAA-C03.md": (
            "questions",
        ),
        ROOT / "04_Questoes_e_Revisoes" / "Gabarito_Comentado_SAA-C03.md": (
            "answers",
        ),
    }
    for index, kinds in index_expectations.items():
        text = read_text(index)
        for block in blocks:
            for kind in kinds:
                name = block[kind].name
                if name not in text:
                    errors.append(f"{index.relative_to(ROOT)}: índice sem {name}")


def validate_duplicate_questions(
    blocks: list[dict[str, Path]], errors: list[str]
) -> None:
    """Detecta questões copiadas integralmente entre blocos."""
    seen: dict[str, str] = {}
    for block in blocks:
        text = read_text(block["questions"])
        matches = list(QUESTION_HEADING_RE.finditer(text))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            section = text[match.end() : end]
            section = section.split("\n## Registro", 1)[0]
            normalized = re.sub(r"\s+", " ", section).strip().casefold()
            previous = seen.get(normalized)
            if previous:
                errors.append(
                    f"questões duplicadas integralmente: {previous} e {match.group(1)}"
                )
            else:
                seen[normalized] = match.group(1)


def validate_text_files(errors: list[str]) -> int:
    checked = 0
    for directory in (CHAPTERS, LABS, QUESTION_BLOCKS, PROGRESS):
        for path in directory.glob("*.md"):
            checked += 1
            try:
                lines = read_text(path).splitlines()
            except UnicodeDecodeError:
                errors.append(f"{path.relative_to(ROOT)}: UTF-8 inválido")
                continue
            for number, line in enumerate(lines, start=1):
                trailing = re.search(r"[ \t]+$", line)
                if trailing and trailing.group(0) != "  ":
                    errors.append(f"{path.relative_to(ROOT)}:{number}: whitespace final")
    return checked


def main() -> int:
    errors: list[str] = []
    complete = 0
    blocks: list[dict[str, Path]] = []
    for block in range(1, 26):
        validated = validate_block(block, errors)
        if validated:
            complete += 1
            blocks.append(validated)
    local_links = validate_local_links(errors)
    validate_schedule(errors)
    if len(blocks) == 25:
        validate_indexes(blocks, errors)
        validate_duplicate_questions(blocks, errors)
    text_files = validate_text_files(errors)

    if errors:
        print(f"FALHA: {len(errors)} problema(s) encontrado(s).", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "OK: "
        f"{complete} blocos, 25 capítulos, 25 laboratórios, "
        "250 questões, 250 respostas, 25 checklists, "
        f"{local_links} links locais e {text_files} arquivos editoriais validados."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
