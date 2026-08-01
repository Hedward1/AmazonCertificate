#!/usr/bin/env python3
"""Valida e renderiza os três simulados autorais mantidos fora do Git.

O repositório é público. Por isso, este script e o manifesto são versionados,
mas os bancos JSON, cadernos de questões, gabaritos e relatórios permanecem na
pasta ``Simulados_Privados``, ignorada pelo Git.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = (
    ROOT / "04_Questoes_e_Revisoes" / "Simulados" / "manifesto_simulados.json"
)
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
    "single": ((4,), 1, "choose one"),
    "multi-2": ((5, 6), 2, "choose two"),
    "multi-3": ((6,), 3, "select three"),
}
QUESTION_TYPES = {"fundamental", "situational", "integrated"}
DIFFICULTIES = {"basic", "intermediate", "advanced"}
OFFICIAL_REFERENCE_RE = re.compile(
    r"^https://(?:docs\.aws\.amazon\.com|aws\.amazon\.com)/"
)
WORD_RE = re.compile(r"[a-z0-9][a-z0-9+./-]*")
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "have",
    "in",
    "is",
    "it",
    "must",
    "of",
    "on",
    "or",
    "should",
    "that",
    "the",
    "their",
    "to",
    "use",
    "uses",
    "using",
    "which",
    "with",
}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize(text: str) -> str:
    return " ".join(WORD_RE.findall(text.casefold()))


def meaningful_tokens(text: str) -> set[str]:
    return {token for token in WORD_RE.findall(text.casefold()) if token not in STOPWORDS}


def semantic_similarity(left: str, right: str) -> float:
    left_normalized = normalize(left)
    right_normalized = normalize(right)
    left_tokens = meaningful_tokens(left)
    right_tokens = meaningful_tokens(right)
    if not left_tokens or not right_tokens:
        return 0.0
    jaccard = len(left_tokens & right_tokens) / len(left_tokens | right_tokens)
    sequence = SequenceMatcher(None, left_normalized, right_normalized).ratio()
    return max(jaccard, sequence)


def question_body(question: dict[str, Any]) -> str:
    options = " ".join(str(value) for value in question.get("options", {}).values())
    return f"{question.get('stem', '')} {options}"


def require_text(
    question: dict[str, Any], field: str, minimum: int, label: str, errors: list[str]
) -> None:
    value = question.get(field)
    if not isinstance(value, str) or len(value.strip()) < minimum:
        errors.append(f"{label}: campo {field!r} ausente ou curto (mínimo {minimum})")


def validate_question(
    question: dict[str, Any], sim_id: str, number: int, errors: list[str]
) -> None:
    expected_id = f"{sim_id}-{number:02d}"
    question_id = question.get("id")
    label = str(question_id or expected_id)
    if question_id != expected_id:
        errors.append(f"{label}: ID esperado {expected_id}")

    domain = question.get("domain")
    task = question.get("task")
    if domain not in {1, 2, 3, 4}:
        errors.append(f"{label}: domínio inválido {domain!r}")
    if task not in VALID_TASKS:
        errors.append(f"{label}: tarefa inválida {task!r}")
    elif domain in {1, 2, 3, 4} and not task.startswith(f"{domain}."):
        errors.append(f"{label}: tarefa {task} não pertence ao domínio {domain}")

    question_format = question.get("format")
    if question_format not in FORMAT_RULES:
        errors.append(f"{label}: formato inválido {question_format!r}")
        return
    allowed_option_counts, answer_count, instruction_fragment = FORMAT_RULES[question_format]

    instruction = str(question.get("instruction", "")).strip().casefold()
    if instruction_fragment not in instruction:
        errors.append(
            f"{label}: instrução deve conter {instruction_fragment.title()!r}"
        )

    options = question.get("options")
    option_count = len(options) if isinstance(options, dict) else 0
    expected_letters = [chr(ord("A") + index) for index in range(option_count)]
    if (
        not isinstance(options, dict)
        or option_count not in allowed_option_counts
        or list(options) != expected_letters
    ):
        expected_counts = " or ".join(map(str, allowed_option_counts))
        errors.append(
            f"{label}: {question_format} requires {expected_counts} sequential options from A"
        )
        options = options if isinstance(options, dict) else {}
    for letter, option in options.items():
        if not isinstance(option, str) or len(option.strip()) < 12:
            errors.append(f"{label}: alternativa {letter} ausente ou curta")

    answers = question.get("answers")
    if not isinstance(answers, list):
        errors.append(f"{label}: answers deve ser uma lista")
        answers = []
    if len(answers) != answer_count or len(set(answers)) != answer_count:
        errors.append(
            f"{label}: esperado(s) {answer_count} acerto(s) distinto(s); recebido {answers}"
        )
    if answers != sorted(answers):
        errors.append(f"{label}: respostas devem estar ordenadas")
    unknown_answers = set(answers) - set(expected_letters)
    if unknown_answers:
        errors.append(f"{label}: respostas fora das alternativas {sorted(unknown_answers)}")

    rationales = question.get("rationales")
    if not isinstance(rationales, dict) or set(rationales) != set(expected_letters):
        errors.append(f"{label}: análise deve cobrir todas as alternativas")
        rationales = rationales if isinstance(rationales, dict) else {}
    for letter in expected_letters:
        rationale = rationales.get(letter)
        if not isinstance(rationale, str) or len(rationale.strip()) < 25:
            errors.append(f"{label}: análise da alternativa {letter} ausente ou curta")

    if question.get("type") not in QUESTION_TYPES:
        errors.append(f"{label}: tipo inválido {question.get('type')!r}")
    if question.get("difficulty") not in DIFFICULTIES:
        errors.append(f"{label}: dificuldade inválida {question.get('difficulty')!r}")
    if question.get("type") == "fundamental" and question.get("difficulty") == "advanced":
        errors.append(f"{label}: identificação fundamental não pode ser avançada")

    require_text(question, "stem", 100, label, errors)
    require_text(question, "central_requirement", 20, label, errors)
    require_text(question, "decisive_words", 8, label, errors)
    require_text(question, "reusable_rule", 25, label, errors)

    references = question.get("references")
    if not isinstance(references, list) or not references:
        errors.append(f"{label}: referência oficial ausente")
    else:
        for reference in references:
            if not isinstance(reference, str) or not OFFICIAL_REFERENCE_RE.match(reference):
                errors.append(f"{label}: referência não oficial ou inválida {reference!r}")


def validate_bank(
    bank: dict[str, Any], spec: dict[str, Any], errors: list[str]
) -> list[dict[str, Any]]:
    sim_id = spec["id"]
    if bank.get("id") != sim_id:
        errors.append(f"{sim_id}: banco declara ID {bank.get('id')!r}")
    if bank.get("duration_minutes") != spec["duration_minutes"]:
        errors.append(f"{sim_id}: duração diferente de 130 minutos")
    if str(bank.get("language", "")).casefold() != "english":
        errors.append(f"{sim_id}: idioma deve ser English")

    questions = bank.get("questions")
    if not isinstance(questions, list):
        errors.append(f"{sim_id}: questions deve ser uma lista")
        return []
    if len(questions) != spec["questions"]:
        errors.append(
            f"{sim_id}: {len(questions)} questões; esperado {spec['questions']}"
        )

    for number, question in enumerate(questions, start=1):
        if not isinstance(question, dict):
            errors.append(f"{sim_id}-{number:02d}: questão não é um objeto JSON")
            continue
        validate_question(question, sim_id, number, errors)

    distributions = {
        "domain_counts": Counter(str(question.get("domain")) for question in questions),
        "task_counts": Counter(question.get("task") for question in questions),
        "format_counts": Counter(question.get("format") for question in questions),
        "type_counts": Counter(question.get("type") for question in questions),
        "difficulty_counts": Counter(
            question.get("difficulty") for question in questions
        ),
    }
    for key, actual in distributions.items():
        expected = Counter(spec[key])
        if actual != expected:
            errors.append(f"{sim_id}: {key}={dict(actual)}; esperado {dict(expected)}")

    represented_tasks = {question.get("task") for question in questions}
    missing_tasks = VALID_TASKS - represented_tasks
    if missing_tasks:
        errors.append(f"{sim_id}: tarefas sem questão {sorted(missing_tasks)}")
    return questions


def validate_simulator_similarity(
    all_questions: list[dict[str, Any]], errors: list[str]
) -> None:
    exact: dict[str, str] = {}
    for question in all_questions:
        question_id = question.get("id", "sem-id")
        normalized = normalize(question_body(question))
        previous = exact.get(normalized)
        if previous:
            errors.append(f"questões literalmente repetidas: {previous} e {question_id}")
        else:
            exact[normalized] = question_id

    for left, right in combinations(all_questions, 2):
        left_id = str(left.get("id", ""))
        right_id = str(right.get("id", ""))
        left_body = question_body(left)
        right_body = question_body(right)
        similarity = semantic_similarity(left_body, right_body)
        if similarity >= 0.84:
            errors.append(
                f"questões semanticamente muito parecidas ({similarity:.0%}): "
                f"{left_id} e {right_id}"
            )


def load_and_validate(
    manifest: dict[str, Any]
) -> tuple[list[tuple[dict[str, Any], dict[str, Any], Path]], list[str]]:
    errors: list[str] = []
    loaded: list[tuple[dict[str, Any], dict[str, Any], Path]] = []
    all_questions: list[dict[str, Any]] = []
    for spec in manifest.get("simulators", []):
        source = ROOT / spec["source"]
        if not source.is_file():
            errors.append(f"{spec['id']}: banco privado ausente em {spec['source']}")
            continue
        try:
            bank = read_json(source)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{spec['id']}: não foi possível ler o banco: {exc}")
            continue
        questions = validate_bank(bank, spec, errors)
        all_questions.extend(questions)
        loaded.append((spec, bank, source))
    if len(loaded) == 3:
        validate_simulator_similarity(all_questions, errors)
    return loaded, errors


def render_questions(bank: dict[str, Any]) -> str:
    sim_id = bank["id"]
    lines = [
        f"# {sim_id} — Questions",
        "",
        "**Time:** 130 minutes  ",
        "**Language:** English  ",
        "**Rules:** Closed book. Complete all 65 questions before opening the answer key.",
        "",
        "## Question metadata",
        "",
        "| ID | Domain | Task | Format | Type | Difficulty |",
        "|---|---:|---:|---|---|---|",
    ]
    for question in bank["questions"]:
        lines.append(
            f"| {question['id']} | {question['domain']} | {question['task']} | "
            f"{question['format']} | {question['type']} | {question['difficulty']} |"
        )
    for question in bank["questions"]:
        lines.extend(
            [
                "",
                f"## {question['id']}",
                "",
                f"**{question['instruction']}**",
                "",
                question["stem"].strip(),
                "",
            ]
        )
        for letter, option in question["options"].items():
            lines.append(f"- {letter}. {option}")
    return "\n".join(lines).rstrip() + "\n"


def render_answers(bank: dict[str, Any]) -> str:
    sim_id = bank["id"]
    lines = [
        f"# {sim_id} — Commented answer key",
        "",
        "Open this file only after completing the timed attempt.",
        "",
        "## Quick answer table",
        "",
        "| ID | Answer | Domain | Task |",
        "|---|---|---:|---:|",
    ]
    for question in bank["questions"]:
        answer = ",".join(question["answers"])
        lines.append(
            f"| {question['id']} | {answer} | {question['domain']} | {question['task']} |"
        )
    for question in bank["questions"]:
        answer = ",".join(question["answers"])
        lines.extend(
            [
                "",
                f"## {question['id']} — Answer {answer}",
                "",
                f"- **Central requirement:** {question['central_requirement']}",
                f"- **Decisive words:** {question['decisive_words']}",
            ]
        )
        for letter in question["options"]:
            lines.append(f"- **{letter}:** {question['rationales'][letter]}")
        lines.append(f"- **Reusable rule:** {question['reusable_rule']}")
        links = ", ".join(f"[AWS]({url})" for url in question["references"])
        lines.append(f"- **Official reference:** {links}")
    return "\n".join(lines).rstrip() + "\n"


def render_report(bank: dict[str, Any]) -> str:
    sim_id = bank["id"]
    domain_counts = Counter(question["domain"] for question in bank["questions"])
    task_counts = Counter(question["task"] for question in bank["questions"])
    lines = [
        f"# {sim_id} — Result report",
        "",
        "**Date:** ____-__-__  ",
        "**Time used:** ___ / 130 minutes  ",
        "**Correct answers:** ___ / 65  ",
        "**Score:** ___%  ",
        "",
        "A multi-response question counts as correct only when the entire answer set matches.",
        "",
        "## Result by domain",
        "",
        "| Domain | Questions | Correct | Percentage | Main gap |",
        "|---:|---:|---:|---:|---|",
    ]
    for domain in range(1, 5):
        lines.append(f"| {domain} | {domain_counts[domain]} |  |  |  |")
    lines.extend(
        [
            "",
            "## Result by task",
            "",
            "| Task | Questions | Correct | Percentage | Review action |",
            "|---:|---:|---:|---:|---|",
        ]
    )
    for task in sorted(VALID_TASKS, key=lambda value: tuple(map(int, value.split(".")))):
        lines.append(f"| {task} | {task_counts[task]} |  |  |  |")
    lines.extend(
        [
            "",
            "## Question-level triage",
            "",
            "Record every incorrect answer and every low-confidence correct answer in the error notebook.",
            "",
            "| ID | Correct? | Confidence | Error cause | D+2 | D+7 |",
            "|---|---|---|---|---|---|",
        ]
    )
    for question in bank["questions"]:
        lines.append(f"| {question['id']} |  |  |  |  |  |")
    return "\n".join(lines).rstrip() + "\n"


def render_all(
    manifest: dict[str, Any],
    loaded: list[tuple[dict[str, Any], dict[str, Any], Path]],
) -> None:
    for spec, bank, source in loaded:
        output_paths = [ROOT / value for value in spec["outputs"]]
        for output in output_paths:
            output.parent.mkdir(parents=True, exist_ok=True)
        output_paths[0].write_text(render_questions(bank), encoding="utf-8")
        output_paths[1].write_text(render_answers(bank), encoding="utf-8")
        output_paths[2].write_text(render_report(bank), encoding="utf-8")
        spec["source_sha256"] = sha256(source)
        spec["validated"] = True
    manifest["status"] = "validated-private"
    write_json(MANIFEST_PATH, manifest)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Valida os bancos privados sem reescrever os cadernos ou o manifesto.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = read_json(MANIFEST_PATH)
    loaded, errors = load_and_validate(manifest)
    if errors:
        print(f"FALHA: {len(errors)} problema(s) nos simulados privados.", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if not args.validate_only:
        render_all(manifest, loaded)
    total = sum(len(bank["questions"]) for _, bank, _ in loaded)
    action = "validadas" if args.validate_only else "validadas e renderizadas"
    print(f"OK: 3 simulados, {total} questões privadas {action}; nenhum conteúdo foi publicado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
