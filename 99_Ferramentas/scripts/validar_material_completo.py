#!/usr/bin/env python3
"""Valida cobertura técnica, questões, simulados e navegação do material SAA-C03."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
import gerar_matriz_competencias_oficiais as competency_matrix_model

CHAPTERS = ROOT / "03_Guia_do_Estudante" / "Capitulos"
LABS = ROOT / "05_Laboratorios"
QUESTION_BLOCKS = ROOT / "04_Questoes_e_Revisoes" / "Blocos"
PROGRESS = ROOT / "06_Progresso"
SIMULATOR_MANIFEST = (
    ROOT / "04_Questoes_e_Revisoes" / "Simulados" / "manifesto_simulados.json"
)
COMPETENCY_MATRIX = (
    ROOT / "02_Planejamento" / "Matriz_Competencias_Oficiais_SAA-C03.csv"
)

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
VALID_TASKS = {
    "1.1",
    "1.2",
    "1.3",
    "2.1",
    "2.2",
    "3.1",
    "3.2",
    "3.3",
    "3.4",
    "3.5",
    "4.1",
    "4.2",
    "4.3",
    "4.4",
}
FORMAT_RULES = {
    "single": ((4,), 1, None),
    "multi-2": ((5, 6), 2, "Choose TWO"),
    "multi-3": ((6,), 3, "Select THREE"),
}
EXPECTED_FORMAT_COUNTS = Counter({"single": 190, "multi-2": 45, "multi-3": 15})
EXPECTED_TYPE_COUNTS = Counter(
    {"fundamental": 50, "situacional": 113, "integrada": 87}
)
ALLOWED_DIFFICULTIES = {"básica", "intermediária", "avançada"}
EXPECTED_COMPETENCY_COUNT = 189
EXPECTED_COMPETENCY_BREAKDOWN = {
    "1.1": {"knowledge": 5, "skill": 6},
    "1.2": {"knowledge": 6, "skill": 4},
    "1.3": {"knowledge": 4, "skill": 7},
    "2.1": {"knowledge": 16, "skill": 7},
    "2.2": {"knowledge": 12, "skill": 8},
    "3.1": {"knowledge": 3, "skill": 2},
    "3.2": {"knowledge": 6, "skill": 4},
    "3.3": {"knowledge": 8, "skill": 5},
    "3.4": {"knowledge": 4, "skill": 4},
    "3.5": {"knowledge": 7, "skill": 7},
    "4.1": {"knowledge": 11, "skill": 10},
    "4.2": {"knowledge": 9, "skill": 6},
    "4.3": {"knowledge": 9, "skill": 5},
    "4.4": {"knowledge": 7, "skill": 7},
}
LOCAL_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
QUESTION_HEADING_RE = re.compile(r"^### (B\d{2}-\d{2})$", re.MULTILINE)
ANSWER_HEADING_RE = re.compile(
    r"^## (B\d{2}-\d{2}) — (?:Resposta|Answer) ([A-F](?:,[A-F]){0,2})$",
    re.MULTILINE,
)
OFFICIAL_AWS_RE = re.compile(r"https://(?:docs\.aws\.amazon\.com|aws\.amazon\.com)/")
WORD_RE = re.compile(r"[a-zà-öø-ÿ0-9][a-zà-öø-ÿ0-9+./-]*", re.IGNORECASE)
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "de",
    "do",
    "e",
    "em",
    "for",
    "from",
    "in",
    "is",
    "o",
    "of",
    "on",
    "or",
    "os",
    "para",
    "que",
    "should",
    "the",
    "to",
    "um",
    "uma",
    "use",
    "using",
    "which",
    "with",
}
COURSE_RULE_RE = re.compile(
    r"practice exam|checklist|cronograma|study schedule|study plan|"
    r"udemy|não abra|não abrir|reserved practice|learner is tempted|"
    r"before moving on|record (?:the |your )?(?:decisive words|confidence)|"
    r"after (?:a|the) (?:lab|laboratory)|laboratory exercise|"
    r"mark (?:the )?checklist|study procedure",
    re.IGNORECASE,
)
DIRECT_IDENTIFICATION_RE = re.compile(
    r"\b(?:which|what|qual)\s+(?:aws\s+)?"
    r"(?:service|component|object|statement|list|feature|construct)\b",
    re.IGNORECASE,
)
PRIORITY_CAPSULES = {
    "AWS X-Ray": "B20_*.md",
    "AWS Resource Access Manager": "B21_*.md",
    "AWS Security Hub": "B20_*.md",
    "Amazon Detective": "B22_*.md",
    "AWS Artifact": "B20_*.md",
    "AWS Audit Manager": "B20_*.md",
    "AWS Compute Optimizer": "B25_*.md",
    "AWS Cost and Usage Report": "B25_*.md",
    "AWS Client VPN": "B23_*.md",
    "AWS AppSync": "B17_*.md",
}
OPTIONAL_CLASSIFICATIONS = (
    ("B16_*.md", "Lambda Durable Functions", "atualização relevante"),
    ("B16_*.md", "Lambda MicroVMs", "conteúdo profissional opcional"),
    ("B22_*.md", "Regional NAT Gateway", "atualização relevante"),
    ("B13_*.md", "Snowball", "atualização relevante"),
    ("B24_*.md", "Snowball", "atualização relevante"),
    ("B25_*.md", "Pinpoint", "atualização relevante"),
)
MATRIX_FIELDS = [
    "domínio",
    "peso",
    "tarefa",
    "knowledge ou skill",
    "competência",
    "bloco",
    "capítulo",
    "seção",
    "comparação",
    "cenário resolvido",
    "laboratório",
    "questão fundamental",
    "questão integrada",
    "questão de múltipla resposta",
    "D+2",
    "D+7",
    "referência oficial",
    "data de validação",
    "status",
    "lacuna",
]


@dataclass
class QuestionRecord:
    question_id: str
    domain: int
    task: str
    language: str
    question_format: str
    question_type: str
    difficulty: str
    body: str
    options: list[str]
    answers: list[str]
    answer_body: str
    question_path: Path
    answer_path: Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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
            errors.append(
                f"{path.relative_to(ROOT)}: seção ausente ({' / '.join(alternatives)})"
            )


def parse_metadata_table(text: str, path: Path, errors: list[str]) -> dict[str, dict[str, str]]:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("| ID |"):
            continue
        headers = [value.strip() for value in line.strip("|").split("|")]
        required = {
            "ID",
            "Tarefa",
            "Idioma",
            "Formato",
            "Tipo",
            "Dificuldade",
        }
        missing = required - set(headers)
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: metadados sem {sorted(missing)}")
        result: dict[str, dict[str, str]] = {}
        for row in lines[index + 2 :]:
            if not row.startswith("|"):
                break
            values = [value.strip() for value in row.strip("|").split("|")]
            if len(values) != len(headers):
                errors.append(f"{path.relative_to(ROOT)}: linha de metadados malformada")
                continue
            record = dict(zip(headers, values))
            question_id = record.get("ID", "")
            if question_id in result:
                errors.append(f"{path.relative_to(ROOT)}: metadado duplicado {question_id}")
            result[question_id] = record
        return result
    errors.append(f"{path.relative_to(ROOT)}: tabela de metadados ausente")
    return {}


def question_sections(text: str, path: Path, errors: list[str]) -> dict[str, str]:
    matches = list(QUESTION_HEADING_RE.finditer(text))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        question_id = match.group(1)
        if question_id in result:
            errors.append(
                f"{path.relative_to(ROOT)}: título de questão duplicado {question_id}"
            )
            continue
        result[question_id] = text[match.end() : end]
    return result


def answer_sections(
    text: str, path: Path, errors: list[str]
) -> tuple[dict[str, tuple[list[str], str]], dict[str, list[str]]]:
    matches = list(ANSWER_HEADING_RE.finditer(text))
    sections: dict[str, tuple[list[str], str]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        question_id = match.group(1)
        if question_id in sections:
            errors.append(
                f"{path.relative_to(ROOT)}: título de gabarito duplicado {question_id}"
            )
            continue
        sections[question_id] = (
            match.group(2).split(","),
            text[match.end() : end],
        )
    quick: dict[str, list[str]] = {}
    for question_id, answer in re.findall(
        r"^\| (B\d{2}-\d{2}) \| ([A-F](?:,[A-F]){0,2}) \|",
        text,
        re.MULTILINE,
    ):
        if question_id in quick:
            errors.append(
                f"{path.relative_to(ROOT)}: resposta rápida duplicada {question_id}"
            )
            continue
        quick[question_id] = answer.split(",")
    return sections, quick


def validate_question_bank_pair(
    code: str,
    question_path: Path,
    answer_path: Path,
    errors: list[str],
) -> list[QuestionRecord]:
    question_text = read_text(question_path)
    answer_text = read_text(answer_path)
    metadata = parse_metadata_table(question_text, question_path, errors)
    questions = question_sections(question_text, question_path, errors)
    answers, quick = answer_sections(answer_text, answer_path, errors)
    expected_ids = {f"{code}-{number:02d}" for number in range(1, 11)}

    for label, actual in (
        ("questões", set(questions)),
        ("metadados", set(metadata)),
        ("gabaritos", set(answers)),
        ("respostas rápidas", set(quick)),
    ):
        if actual != expected_ids:
            errors.append(
                f"{question_path.relative_to(ROOT)}: {label} não coincide com {code}-01..10"
            )

    records: list[QuestionRecord] = []
    for question_id in sorted(expected_ids):
        body = questions.get(question_id, "")
        record = metadata.get(question_id, {})
        question_format = record.get("Formato", "")
        if question_format not in FORMAT_RULES:
            errors.append(f"{question_id}: formato inválido {question_format!r}")
            continue
        allowed_option_counts, answer_count, instruction = FORMAT_RULES[question_format]
        options = re.findall(r"^- ([A-Z])\.", body, re.MULTILINE)
        option_count = len(options)
        expected_letters = [chr(ord("A") + index) for index in range(option_count)]
        if option_count not in allowed_option_counts:
            expected_counts = " ou ".join(map(str, allowed_option_counts))
            errors.append(
                f"{question_id}: formato {question_format} exige {expected_counts} alternativas; "
                f"encontrado {option_count}"
            )
        if options != expected_letters:
            errors.append(
                f"{question_id}: alternativas devem ser sequenciais a partir de A; "
                f"encontrado {','.join(options)}"
            )
        if instruction and instruction.casefold() not in body.casefold():
            errors.append(f"{question_id}: instrução explícita {instruction!r} ausente")
        if question_format == "single" and re.search(
            r"Choose TWO|Select THREE", body, re.IGNORECASE
        ):
            errors.append(f"{question_id}: single contém instrução de múltipla resposta")

        answer_letters, answer_body = answers.get(question_id, ([], ""))
        if len(answer_letters) != answer_count or len(set(answer_letters)) != answer_count:
            errors.append(
                f"{question_id}: {question_format} exige {answer_count} resposta(s) distinta(s)"
            )
        if answer_letters != sorted(answer_letters):
            errors.append(f"{question_id}: respostas devem estar ordenadas")
        if set(answer_letters) - set(expected_letters):
            errors.append(f"{question_id}: gabarito referencia alternativa inexistente")
        if quick.get(question_id) != answer_letters:
            errors.append(f"{question_id}: tabela rápida diverge do título do gabarito")
        analyzed: list[str] = []
        analysis_matches = re.findall(
            r"^- \*\*([^*]+):\*\*\s*(.*?)"
            r"(?=^- \*\*[^*]+:\*\*|\Z)",
            answer_body,
            re.MULTILINE | re.DOTALL,
        )
        for label, explanation in analysis_matches:
            normalized_label = (
                label.upper()
                .replace(" AND ", ",")
                .replace(" E ", ",")
                .replace(" & ", ",")
            )
            if re.fullmatch(r"[A-F](?:\s*,\s*[A-F])*", normalized_label):
                letters = re.findall(r"[A-F]", normalized_label)
                if len(letters) != 1:
                    errors.append(
                        f"{question_id}: alternativas devem ser analisadas individualmente, "
                        f"não em grupo ({label})"
                    )
                analyzed.extend(letters)
                if len(token_set(explanation)) < 2:
                    errors.append(
                        f"{question_id}: análise da alternativa {letters[0]} está vazia ou insuficiente"
                    )
        if Counter(analyzed) != Counter(expected_letters):
            errors.append(
                f"{question_id}: análise deve cobrir {','.join(expected_letters)} exatamente uma vez"
            )
        if int(code[1:]) >= 5:
            require_terms(
                answer_body,
                answer_path,
                (
                    ("Requisito central", "Central requirement"),
                    ("Palavras decisivas", "Decisive words", "Keywords", "Keyword"),
                    ("Regra reutilizável", "Reusable rule"),
                    ("Aulas", "Lessons"),
                    ("Referência", "Reference"),
                ),
                errors,
            )

        task = record.get("Tarefa", "")
        task_values = [value.strip() for value in task.split("/") if value.strip()]
        domain_text = record.get("Domínio", "").strip()
        try:
            domain = int(domain_text) if domain_text else int(task_values[0].split(".")[0])
        except (ValueError, IndexError):
            domain = 0
        language = record.get("Idioma", "")
        question_type = record.get("Tipo", "")
        difficulty = record.get("Dificuldade", "")
        if domain not in {1, 2, 3, 4}:
            errors.append(f"{question_id}: domínio inválido {domain}")
        if (
            not task_values
            or any(value not in VALID_TASKS for value in task_values)
            or (domain_text and all(not value.startswith(f"{domain}.") for value in task_values))
        ):
            errors.append(f"{question_id}: tarefa inválida ou fora do domínio ({task})")
        if language not in {"Português", "Inglês"}:
            errors.append(f"{question_id}: idioma inválido {language!r}")
        if question_type not in EXPECTED_TYPE_COUNTS:
            errors.append(f"{question_id}: tipo inválido {question_type!r}")
        if difficulty not in ALLOWED_DIFFICULTIES:
            errors.append(f"{question_id}: dificuldade inválida {difficulty!r}")
        if question_type == "fundamental" and difficulty == "avançada":
            errors.append(f"{question_id}: questão fundamental direta não pode ser avançada")
        if question_type == "integrada" and difficulty == "básica":
            errors.append(f"{question_id}: questão integrada não pode ser básica")
        question_core = body.split("\n## ", 1)[0]
        stem_before_options = question_core.split("\n- A.", 1)[0]
        if difficulty == "avançada" and re.search(
            r"(?:Which|What) AWS service|Qual serviço", stem_before_options, re.IGNORECASE
        ) and len(WORD_RE.findall(stem_before_options)) < 45:
            errors.append(f"{question_id}: identificação direta foi rotulada avançada")
        if (
            question_type == "integrada"
            and difficulty == "avançada"
            and DIRECT_IDENTIFICATION_RE.search(stem_before_options)
            and len(WORD_RE.findall(stem_before_options)) < 55
        ):
            errors.append(
                f"{question_id}: identificação direta curta não sustenta integrada/avançada"
            )
        if COURSE_RULE_RE.search(question_core):
            errors.append(f"{question_id}: avalia regra interna do curso, não decisão AWS")

        records.append(
            QuestionRecord(
                question_id=question_id,
                domain=domain,
                task=task,
                language=language,
                question_format=question_format,
                question_type=question_type,
                difficulty=difficulty,
                body=question_core,
                options=options,
                answers=answer_letters,
                answer_body=answer_body,
                question_path=question_path,
                answer_path=answer_path,
            )
        )
    return records


def validate_block(block: int, errors: list[str]) -> tuple[dict[str, Path], list[QuestionRecord]] | None:
    code = f"B{block:02d}"
    chapter = one_file(CHAPTERS, f"{code}_*.md", code + " capítulo", errors)
    lab = one_file(LABS, f"LAB_{code}_*.md", code + " laboratório", errors)
    questions = QUESTION_BLOCKS / f"{code}_Questoes.md"
    answers = QUESTION_BLOCKS / f"{code}_Gabarito.md"
    checklist = PROGRESS / f"{code}_Checklist_e_Revisoes.md"
    if chapter is None or lab is None:
        return None
    paths = {
        "chapter": chapter,
        "lab": lab,
        "questions": questions,
        "answers": answers,
        "checklist": checklist,
    }
    for path in paths.values():
        if not path.is_file():
            errors.append(f"arquivo ausente: {path.relative_to(ROOT)}")
    if any(not path.is_file() for path in paths.values()):
        return None

    chapter_text = read_text(chapter)
    lab_text = read_text(lab)
    checklist_text = read_text(checklist)
    if not chapter_text.startswith(f"# {code} — "):
        errors.append(f"{chapter.relative_to(ROOT)}: H1 fora do padrão '# {code} —'")
    if not lab_text.startswith(f"# LAB {code} — "):
        errors.append(f"{lab.relative_to(ROOT)}: H1 fora do padrão '# LAB {code} —'")
    route_fragment = f"Roteiro_de_Aulas_por_Dia_SAA-C03.md#{code.casefold()}"
    if route_fragment not in chapter_text:
        errors.append(f"{chapter.relative_to(ROOT)}: link ausente para o roteiro {code}")

    # B01–B04 são módulos introdutórios deliberadamente mais curtos. A partir
    # de B05, todos os capítulos e laboratórios seguem o contrato editorial
    # completo usado pelo restante do curso.
    if block >= 5:
        require_terms(
            chapter_text,
            chapter,
            (
                ("Objetivos de aprendizagem",),
                ("Como estudar", "Aulas deste bloco"),
                ("Cenário resolvido",),
                ("Tabela de decisão", "Comparação", "trade-off"),
                ("Armadilhas",),
                ("Custos", "Custo"),
                ("Recuperação ativa",),
                ("Referências oficiais", "Referência oficial"),
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
                ("Referências oficiais", "Referência oficial"),
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
    for path, text in ((chapter, chapter_text), (lab, lab_text), (answers, read_text(answers))):
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

    records = validate_question_bank_pair(code, questions, answers, errors)
    portuguese = sum(record.language == "Português" for record in records)
    english = sum(record.language == "Inglês" for record in records)
    if (portuguese, english) != EXPECTED_LANGUAGES[block]:
        errors.append(
            f"{questions.relative_to(ROOT)}: idiomas PT/EN={portuguese}/{english}; "
            f"esperado {EXPECTED_LANGUAGES[block][0]}/{EXPECTED_LANGUAGES[block][1]}"
        )
    return paths, records


def normalize_question(text: str) -> str:
    return " ".join(WORD_RE.findall(text.casefold()))


def token_set(text: str) -> set[str]:
    return {token for token in WORD_RE.findall(text.casefold()) if token not in STOPWORDS}


def similarity(left: str, right: str) -> float:
    left_normalized = normalize_question(left)
    right_normalized = normalize_question(right)
    left_tokens = token_set(left)
    right_tokens = token_set(right)
    if not left_tokens or not right_tokens:
        return 0.0
    jaccard = len(left_tokens & right_tokens) / len(left_tokens | right_tokens)
    sequence = SequenceMatcher(None, left_normalized, right_normalized).ratio()
    return max(jaccard, sequence)


def validate_question_distributions(records: list[QuestionRecord], errors: list[str]) -> dict[str, Counter]:
    task_values = [
        task
        for record in records
        for task in (value.strip() for value in record.task.split("/"))
        if task
    ]
    distributions = {
        "domains": Counter(record.domain for record in records),
        "tasks": Counter(task_values),
        "formats": Counter(record.question_format for record in records),
        "types": Counter(record.question_type for record in records),
        "difficulties": Counter(record.difficulty for record in records),
        "languages": Counter(record.language for record in records),
    }
    if len(records) != 250:
        errors.append(f"banco: {len(records)} questões; esperado 250")
    if distributions["formats"] != EXPECTED_FORMAT_COUNTS:
        errors.append(
            f"banco: formatos {dict(distributions['formats'])}; "
            f"esperado {dict(EXPECTED_FORMAT_COUNTS)}"
        )
    if distributions["types"] != EXPECTED_TYPE_COUNTS:
        errors.append(
            f"banco: tipos {dict(distributions['types'])}; "
            f"esperado {dict(EXPECTED_TYPE_COUNTS)}"
        )
    missing_tasks = VALID_TASKS - set(task_values)
    if missing_tasks:
        errors.append(f"banco: tarefas sem questão {sorted(missing_tasks)}")
    for domain in range(1, 5):
        if distributions["domains"][domain] == 0:
            errors.append(f"banco: domínio {domain} sem questão")
    total = max(len(records), 1)
    for difficulty in ALLOWED_DIFFICULTIES:
        ratio = distributions["difficulties"][difficulty] / total
        if ratio < 0.10:
            errors.append(
                f"banco: dificuldade {difficulty} representa apenas {ratio:.1%}"
            )
    return distributions


def validate_duplicate_and_similar_questions(records: list[QuestionRecord], errors: list[str]) -> None:
    exact_questions: dict[str, str] = {}
    exact_answers: dict[str, str] = {}
    for record in records:
        normalized = normalize_question(record.body)
        previous = exact_questions.get(normalized)
        if previous:
            errors.append(f"questões duplicadas integralmente: {previous} e {record.question_id}")
        else:
            exact_questions[normalized] = record.question_id
        normalized_answer = normalize_question(record.answer_body)
        previous_answer = exact_answers.get(normalized_answer)
        if previous_answer:
            errors.append(
                f"respostas comentadas duplicadas: {previous_answer} e {record.question_id}"
            )
        else:
            exact_answers[normalized_answer] = record.question_id

    for left, right in combinations(records, 2):
        # Compare os enunciados de todo o banco, não apenas questões rotuladas
        # na mesma tarefa. Metadados incorretos não podem ocultar uma paráfrase.
        left_stem = left.body.split("\n- A.", 1)[0]
        right_stem = right.body.split("\n- A.", 1)[0]
        score = similarity(left_stem, right_stem)
        if score >= 0.86:
            errors.append(
                f"questões semanticamente muito parecidas ({score:.0%}): "
                f"{left.question_id} e {right.question_id}"
            )


def validate_priority_capsules(errors: list[str]) -> None:
    required_labels = (
        ("problema resolvido", "problema que resolve"),
        ("quando escolher",),
        ("quando não escolher",),
        ("serviço semelhante",),
        ("armadilha",),
        ("questão situacional",),
        ("resposta curta", "resposta"),
    )
    for service, pattern in PRIORITY_CAPSULES.items():
        path = one_file(CHAPTERS, pattern, service, errors)
        if path is None:
            continue
        text = read_text(path)
        heading_match = re.search(
            rf"^#{{2,4}} .*{re.escape(service)}.*$(.*?)(?=^#{{2,4}} |\Z)",
            text,
            re.MULTILINE | re.IGNORECASE | re.DOTALL,
        )
        if not heading_match:
            errors.append(f"{path.relative_to(ROOT)}: cápsula ausente para {service}")
            continue
        section = heading_match.group(0).casefold()
        for alternatives in required_labels:
            if not any(label in section for label in alternatives):
                errors.append(
                    f"{path.relative_to(ROOT)}: cápsula {service} sem "
                    f"{' / '.join(alternatives)}"
                )
        if not OFFICIAL_AWS_RE.search(heading_match.group(0)):
            errors.append(f"{path.relative_to(ROOT)}: cápsula {service} sem fonte AWS oficial")


def validate_optional_classification(errors: list[str]) -> None:
    for pattern, term, classification in OPTIONAL_CLASSIFICATIONS:
        path = one_file(CHAPTERS, pattern, term, errors)
        if path is None:
            continue
        text = read_text(path)
        occurrences = [match.start() for match in re.finditer(re.escape(term), text, re.IGNORECASE)]
        if not occurrences:
            errors.append(f"{path.relative_to(ROOT)}: conteúdo volátil ausente ({term})")
            continue
        if not any(
            classification.casefold() in text[max(0, index - 500) : index + 700].casefold()
            for index in occurrences
        ):
            errors.append(
                f"{path.relative_to(ROOT)}: {term} sem classificação '{classification}'"
            )


def validate_data_transfer_terminal(errors: list[str]) -> None:
    path = one_file(CHAPTERS, "B24_*.md", "Data Transfer Terminal", errors)
    if path is None:
        return
    text = read_text(path).casefold()
    requirements = {
        "instalação física": ("instalação física", "local físico", "physical location"),
        "equipamento próprio": ("próprios equipamentos", "próprios dispositivos", "seus dispositivos"),
        "clientes Enterprise": ("clientes enterprise", "enterprise customers"),
        "locais suportados": ("locais suportados", "local suportado"),
        "não é enviado": ("não é um equipamento enviado", "não envia equipamento", "não é enviado"),
        "não substitui Snowball universalmente": (
            "não substitui universalmente",
            "não é substituto universal",
            "não substitui snowball edge universalmente",
        ),
    }
    for label, alternatives in requirements.items():
        if not any(value in text for value in alternatives):
            errors.append(f"{path.relative_to(ROOT)}: Data Transfer Terminal sem {label}")
    if "https://docs.aws.amazon.com/datatransferterminal/" not in text:
        errors.append(f"{path.relative_to(ROOT)}: Data Transfer Terminal sem fonte oficial")


def validate_competency_matrix(
    questions: list[QuestionRecord], errors: list[str]
) -> dict[str, Counter | int]:
    if not COMPETENCY_MATRIX.is_file():
        errors.append("matriz de competências oficiais ausente")
        return {"rows": 0, "status": Counter(), "domain": Counter(), "task": Counter(), "kind": Counter()}
    with COMPETENCY_MATRIX.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != MATRIX_FIELDS:
            errors.append(
                f"matriz de competências: colunas {reader.fieldnames}; esperado {MATRIX_FIELDS}"
            )
        rows = list(reader)
    if len(rows) != EXPECTED_COMPETENCY_COUNT:
        errors.append(
            f"matriz de competências: {len(rows)} linhas; esperado {EXPECTED_COMPETENCY_COUNT}"
        )
    unique = {(row.get("tarefa"), row.get("knowledge ou skill"), row.get("competência")) for row in rows}
    if len(unique) != len(rows):
        errors.append("matriz de competências: competências duplicadas")
    tasks = {row.get("tarefa") for row in rows}
    if tasks != VALID_TASKS:
        errors.append(f"matriz de competências: tarefas inesperadas {sorted(tasks)}")
    breakdown = Counter(
        (row.get("tarefa", ""), row.get("knowledge ou skill", "")) for row in rows
    )
    expected_breakdown = Counter(
        {
            (task, kind): count
            for task, kinds in EXPECTED_COMPETENCY_BREAKDOWN.items()
            for kind, count in kinds.items()
        }
    )
    if breakdown != expected_breakdown:
        errors.append(
            "matriz de competências: contagem Knowledge/Skills por tarefa diverge "
            "do guia oficial vigente"
        )
    routing_failures = competency_matrix_model.validate_routing_model()
    for failure in routing_failures:
        errors.append(f"matriz de competências: regressão de roteamento: {failure}")

    questions_by_id = {question.question_id: question for question in questions}
    for number, row in enumerate(rows, start=2):
        competency = row.get("competência", "")
        task = row.get("tarefa", "")
        status = row.get("status", "")
        block_text = row.get("bloco", "")
        block_match = re.fullmatch(r"B(\d{2})", block_text)
        block = int(block_match.group(1)) if block_match else 0
        expected_block = competency_matrix_model.choose_block(task, competency)
        block_valid = block == expected_block
        if not block_match or not block_valid:
            errors.append(
                f"matriz de competências:{number}: bloco {block_text!r}; "
                f"roteamento semântico exige B{expected_block:02d}"
            )

        expected_chapter = competency_matrix_model.chapter_for(expected_block)
        chapter_value = row.get("capítulo", "")
        chapter_path = ROOT / chapter_value if chapter_value else None
        chapter_valid = bool(
            chapter_path
            and chapter_path.is_file()
            and chapter_path.resolve() == expected_chapter.resolve()
        )
        if not chapter_valid:
            errors.append(
                f"matriz de competências:{number}: capítulo não corresponde ao bloco semântico"
            )

        def relevant_section(field: str) -> bool:
            heading = row.get(field, "")
            if not heading or not chapter_valid or chapter_path is None:
                return False
            section = competency_matrix_model.section_for_heading(chapter_path, heading)
            if section is None:
                errors.append(
                    f"matriz de competências:{number}: {field} inexistente no capítulo: {heading!r}"
                )
                return False
            expected_role = {
                "seção": competency_matrix_model.is_theory_section,
                "comparação": competency_matrix_model.is_comparison_section,
                "cenário resolvido": competency_matrix_model.is_scenario_section,
            }[field]
            if not expected_role(section):
                errors.append(
                    f"matriz de competências:{number}: {field} usa evidência de outra dimensão: {heading!r}"
                )
                return False
            if competency_matrix_model.evidence_relevance_score(
                competency, section.evidence_text
            ) <= 0:
                errors.append(
                    f"matriz de competências:{number}: {field} sem pertinência semântica: {heading!r}"
                )
                return False
            return True

        section_relevant = relevant_section("seção")
        comparison_relevant = relevant_section("comparação")
        scenario_relevant = relevant_section("cenário resolvido")
        theory = chapter_valid and section_relevant

        lab_value = row.get("laboratório", "")
        lab_path = ROOT / lab_value if lab_value else None
        labs_root = (ROOT / "05_Laboratorios").resolve()
        lab_relevant = bool(
            lab_path
            and lab_path.is_file()
            and labs_root in lab_path.resolve().parents
            and competency_matrix_model.evidence_relevance_score(
                competency, read_text(lab_path)
            )
            > 0
        )
        if lab_value and not lab_relevant:
            errors.append(
                f"matriz de competências:{number}: laboratório sem pertinência semântica"
            )
        # Aplicação pode ser demonstrada por comparação, cenário resolvido ou
        # laboratório pertinente, inclusive transversal a outro bloco.
        application = comparison_relevant or scenario_relevant or lab_relevant

        question_rules = (
            ("questão fundamental", lambda question: question.question_type == "fundamental"),
            ("questão integrada", lambda question: question.question_type == "integrada"),
            (
                "questão de múltipla resposta",
                lambda question: question.question_format in {"multi-2", "multi-3"},
            ),
        )
        relevant_questions = 0
        for field, format_rule in question_rules:
            question_id = row.get(field, "")
            if not question_id:
                continue
            question_record = questions_by_id.get(question_id)
            if question_record is None:
                errors.append(
                    f"matriz de competências:{number}: questão inexistente {question_id}"
                )
                continue
            # ``Tarefa`` no banco é a classificação primária. Uma questão pode
            # servir como evidência transversal de outra tarefa quando o corpo
            # cobre semanticamente a competência da linha.
            if not format_rule(question_record):
                errors.append(
                    f"matriz de competências:{number}: {question_id} incompatível com a coluna {field}"
                )
                continue
            if competency_matrix_model.evidence_relevance_score(
                # A última questão do arquivo é seguida pela tabela editorial
                # ``## Registro``. Essa tabela descreve o bloco inteiro e não
                # pode ser aceita como evidência semântica da questão citada.
                competency, question_record.body.split("\n## ", 1)[0]
            ) <= 0:
                errors.append(
                    f"matriz de competências:{number}: {question_id} sem pertinência semântica"
                )
                continue
            relevant_questions += 1
        question = relevant_questions > 0

        expected_review_prefix = f"06_Progresso/B{expected_block:02d}_Checklist_e_Revisoes.md"
        review = all(
            row.get(field, "").startswith(expected_review_prefix)
            for field in ("D+2", "D+7")
        )
        complete = theory and application and question and review
        expected_status = "cobertura completa" if complete else "cobertura parcial"
        if status != expected_status:
            errors.append(
                f"matriz de competências:{number}: status {status!r}; esperado {expected_status!r}"
            )
        expected_missing: list[str] = []
        if not theory:
            expected_missing.append("teoria pertinente")
        if not application:
            expected_missing.append("aplicação pertinente")
        if not question:
            expected_missing.append("questão pertinente")
        if not review:
            expected_missing.append("revisão")
        expected_gap = "; ".join(expected_missing) if expected_missing else "—"
        if row.get("lacuna", "") != expected_gap:
            errors.append(
                f"matriz de competências:{number}: lacuna {row.get('lacuna')!r}; "
                f"esperado {expected_gap!r}"
            )
        if not OFFICIAL_AWS_RE.search(row.get("referência oficial", "")):
            errors.append(f"matriz de competências:{number}: referência oficial inválida")
    return {
        "rows": len(rows),
        "status": Counter(row.get("status") for row in rows),
        "domain": Counter(row.get("domínio") for row in rows),
        "task": Counter(row.get("tarefa") for row in rows),
        "kind": Counter(row.get("knowledge ou skill") for row in rows),
    }


def validate_simulators(errors: list[str]) -> dict[str, int | str]:
    if not SIMULATOR_MANIFEST.is_file():
        errors.append("manifesto dos simulados ausente")
        return {"simulators": 0, "questions": 0, "status": "ausente"}
    try:
        manifest = json.loads(read_text(SIMULATOR_MANIFEST))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"manifesto dos simulados inválido: {exc}")
        return {"simulators": 0, "questions": 0, "status": "inválido"}
    if not isinstance(manifest, dict):
        errors.append("manifesto dos simulados deve ser um objeto JSON")
        return {"simulators": 0, "questions": 0, "status": "inválido"}
    if manifest.get("visibility") != "public-versioned":
        errors.append("manifesto: visibility deve ser public-versioned")
    specs = manifest.get("simulators", [])
    if not isinstance(specs, list):
        errors.append("manifesto: simulators deve ser uma lista")
        return {"simulators": 0, "questions": 0, "status": "inválido"}
    if any(not isinstance(spec, dict) for spec in specs):
        errors.append("manifesto: cada simulado deve ser um objeto")
        return {"simulators": len(specs), "questions": 0, "status": "inválido"}
    if len(specs) != 3 or {spec.get("id") for spec in specs} != {"SIM-A", "SIM-B", "SIM-C"}:
        errors.append("manifesto: esperado SIM-A, SIM-B e SIM-C")
    for spec in specs:
        sim_id = spec.get("id")
        if spec.get("questions") != 65 or spec.get("duration_minutes") != 130:
            errors.append(f"{spec.get('id')}: quantidade ou duração incorreta")
        if spec.get("language") != "English":
            errors.append(f"{spec.get('id')}: idioma deve ser English")
        if spec.get("domain_counts") != {"1": 20, "2": 17, "3": 15, "4": 13}:
            errors.append(f"{spec.get('id')}: pesos de domínio incorretos")
        if spec.get("task_counts") != {
            "1.1": 7, "1.2": 7, "1.3": 6,
            "2.1": 9, "2.2": 8,
            "3.1": 3, "3.2": 3, "3.3": 3, "3.4": 3, "3.5": 3,
            "4.1": 4, "4.2": 3, "4.3": 3, "4.4": 3,
        }:
            errors.append(f"{spec.get('id')}: distribuição por tarefa incorreta")
        if spec.get("format_counts") != {"single": 49, "multi-2": 12, "multi-3": 4}:
            errors.append(f"{spec.get('id')}: distribuição de formatos incorreta")
        if spec.get("type_counts") != {
            "fundamental": 13,
            "situational": 29,
            "integrated": 23,
        }:
            errors.append(f"{spec.get('id')}: distribuição pedagógica incorreta")
        if spec.get("difficulty_counts") != {
            "basic": 10,
            "intermediate": 35,
            "advanced": 20,
        }:
            errors.append(f"{spec.get('id')}: distribuição de dificuldade incorreta")
        expected_source = (
            f"04_Questoes_e_Revisoes/Simulados/Bancos/{sim_id}.json"
        )
        expected_outputs = [
            f"04_Questoes_e_Revisoes/Simulados/{sim_id}/Questoes.md",
            f"04_Questoes_e_Revisoes/Simulados/{sim_id}/Gabarito.md",
            f"04_Questoes_e_Revisoes/Simulados/{sim_id}/Relatorio.md",
        ]
        if spec.get("source") != expected_source:
            errors.append(f"{sim_id}: caminho do banco fora do layout público")
        if spec.get("outputs") != expected_outputs:
            errors.append(f"{sim_id}: saídas fora do layout público")
    sources = [ROOT / spec.get("source", "") for spec in specs]
    sources_present = bool(sources) and all(path.is_file() for path in sources)
    if not sources_present:
        errors.append("um ou mais bancos autorais versionados estão ausentes")
    if sources_present:
        try:
            from gerar_simulados import (
                ANSWER_KEY_QUALITY_CONTROLS,
                load_and_validate,
                validate_rendered_state,
            )
        except ImportError as exc:
            errors.append(f"não foi possível carregar o validador de simulados: {exc}")
        else:
            if manifest.get("answer_key_quality_controls") != ANSWER_KEY_QUALITY_CONTROLS:
                errors.append("manifesto: controles de qualidade do gabarito divergentes")
            loaded, simulator_errors = load_and_validate(manifest)
            errors.extend(f"simulados: {error}" for error in simulator_errors)
            if not simulator_errors:
                rendered_errors: list[str] = []
                validate_rendered_state(manifest, loaded, rendered_errors)
                errors.extend(f"simulados: {error}" for error in rendered_errors)
    return {
        "simulators": len(specs),
        "questions": sum(
            value
            for spec in specs
            if isinstance((value := spec.get("questions")), int)
            and not isinstance(value, bool)
        ),
        "status": "versionados e validados" if sources_present else "ausentes",
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
                errors.append(f"{path.relative_to(ROOT)}: link local quebrado -> {target}")
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
    index_expectations = {
        ROOT / "README.md": ("chapter", "lab", "questions", "checklist"),
        CHAPTERS / "README.md": ("chapter",),
        LABS / "README.md": ("lab",),
        QUESTION_BLOCKS / "README.md": ("questions", "answers"),
        PROGRESS / "README.md": ("checklist",),
        ROOT / "04_Questoes_e_Revisoes" / "Apostila_de_Questoes_SAA-C03.md": ("questions",),
        ROOT / "04_Questoes_e_Revisoes" / "Gabarito_Comentado_SAA-C03.md": ("answers",),
    }
    for index, kinds in index_expectations.items():
        text = read_text(index)
        for block in blocks:
            for kind in kinds:
                name = block[kind].name
                if name not in text:
                    errors.append(f"{index.relative_to(ROOT)}: índice sem {name}")
    simulator_index = ROOT / "04_Questoes_e_Revisoes" / "README.md"
    if "Simulados/README.md" not in read_text(simulator_index):
        errors.append(f"{simulator_index.relative_to(ROOT)}: índice sem mecanismo de simulados")


def validate_text_files(errors: list[str]) -> int:
    checked = 0
    directories = (
        CHAPTERS,
        LABS,
        QUESTION_BLOCKS,
        PROGRESS,
        ROOT / "02_Planejamento",
        SIMULATOR_MANIFEST.parent,
    )
    for directory in directories:
        for path in directory.rglob("*.md"):
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-private", action="store_true", help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    blocks: list[dict[str, Path]] = []
    records: list[QuestionRecord] = []
    for block in range(1, 26):
        validated = validate_block(block, errors)
        if validated:
            paths, block_records = validated
            blocks.append(paths)
            records.extend(block_records)

    distributions = validate_question_distributions(records, errors)
    if len(records) == 250:
        validate_duplicate_and_similar_questions(records, errors)
    validate_priority_capsules(errors)
    validate_optional_classification(errors)
    validate_data_transfer_terminal(errors)
    matrix = validate_competency_matrix(records, errors)
    simulators = validate_simulators(errors)
    local_links = validate_local_links(errors)
    validate_schedule(errors)
    if len(blocks) == 25:
        validate_indexes(blocks, errors)
    text_files = validate_text_files(errors)

    if errors:
        print(f"FALHA: {len(errors)} problema(s) encontrado(s).", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "OK: "
        f"{len(blocks)} blocos; {len(records)} questões "
        f"({dict(distributions['formats'])}); tipos {dict(distributions['types'])}; "
        f"dificuldades {dict(distributions['difficulties'])}; "
        f"domínios {dict(distributions['domains'])}; tarefas {len(distributions['tasks'])}; "
        f"{matrix['rows']} competências ({dict(matrix['status'])}); "
        f"{simulators['simulators']} simulados/{simulators['questions']} questões autorais "
        f"({simulators['status']}); {local_links} links e {text_files} arquivos editoriais."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
