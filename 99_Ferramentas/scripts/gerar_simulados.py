#!/usr/bin/env python3
"""Valida e renderiza os três simulados autorais versionados no projeto.

Os bancos JSON, cadernos de questões, gabaritos e relatórios ficam organizados
em ``04_Questoes_e_Revisoes/Simulados``. O conteúdo do practice exam da Udemy
não é lido, copiado nem reproduzido por este script.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import date
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
ANSWER_KEY_QUALITY_CONTROLS = {
    "single_position_spread_max": 1,
    "single_unique_longest_ratio_max": 0.55,
    "multi_2_same_set_max": 2,
    "multi_3_sets_must_be_unique": True,
    "multi_2_common_letter_frequency_min": 4,
    "multi_3_common_letter_frequency_min": 2,
    "multi_answer_letter_frequency_max": 8,
    "blind_modal_score_max": 16,
}
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
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def write_text_lf(path: Path, value: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(value)


def canonical_json_sha256(path: Path) -> str:
    """Hash JSON semantics independently of formatting and line endings."""
    canonical = json.dumps(
        read_json(path),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


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
    bank: dict[str, Any],
    spec: dict[str, Any],
    errors: list[str],
    quality_controls: dict[str, Any] = ANSWER_KEY_QUALITY_CONTROLS,
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

    valid_questions: list[dict[str, Any]] = []
    for number, question in enumerate(questions, start=1):
        if not isinstance(question, dict):
            errors.append(f"{sim_id}-{number:02d}: questão não é um objeto JSON")
            continue
        valid_questions.append(question)
        validate_question(question, sim_id, number, errors)

    distributions = {
        "domain_counts": Counter(
            str(question.get("domain")) for question in valid_questions
        ),
        "task_counts": Counter(question.get("task") for question in valid_questions),
        "format_counts": Counter(question.get("format") for question in valid_questions),
        "type_counts": Counter(question.get("type") for question in valid_questions),
        "difficulty_counts": Counter(
            question.get("difficulty") for question in valid_questions
        ),
    }
    for key, actual in distributions.items():
        expected = Counter(spec[key])
        if actual != expected:
            errors.append(f"{sim_id}: {key}={dict(actual)}; esperado {dict(expected)}")

    represented_tasks = {question.get("task") for question in valid_questions}
    missing_tasks = VALID_TASKS - represented_tasks
    if missing_tasks:
        errors.append(f"{sim_id}: tarefas sem questão {sorted(missing_tasks)}")
    validate_answer_position_bias(valid_questions, sim_id, quality_controls, errors)
    return valid_questions


def validate_answer_position_bias(
    questions: list[dict[str, Any]],
    sim_id: str,
    quality_controls: dict[str, Any],
    errors: list[str],
) -> None:
    """Reject answer-position and option-length shortcuts in a simulator."""
    def first_answer(question: dict[str, Any]) -> str | None:
        answers = question.get("answers")
        return answers[0] if isinstance(answers, list) and answers else None

    single = [question for question in questions if question.get("format") == "single"]
    if len(single) == 49:
        single_counts = Counter(first_answer(question) for question in single)
        counts = [single_counts.get(letter, 0) for letter in "ABCD"]
        if max(counts) - min(counts) > quality_controls["single_position_spread_max"]:
            errors.append(
                f"{sim_id}: posições corretas das questões single desbalanceadas "
                f"{dict(zip('ABCD', counts))}"
            )

        uniquely_longest = 0
        for question in single:
            options = question.get("options", {})
            answers = question.get("answers", [])
            if (
                not isinstance(options, dict)
                or not isinstance(answers, list)
                or len(answers) != 1
            ):
                continue
            answer = answers[0]
            lengths = {letter: len(str(text).strip()) for letter, text in options.items()}
            if answer in lengths and lengths[answer] > max(
                (length for letter, length in lengths.items() if letter != answer),
                default=-1,
            ):
                uniquely_longest += 1
        longest_ratio_max = quality_controls["single_unique_longest_ratio_max"]
        if uniquely_longest / len(single) > longest_ratio_max:
            errors.append(
                f"{sim_id}: resposta correta é a única alternativa mais longa em "
                f"{uniquely_longest}/{len(single)} questões single; "
                f"máximo {longest_ratio_max:.0%}"
            )

    multi_groups: dict[str, list[tuple[str, ...]]] = {"multi-2": [], "multi-3": []}
    for question in questions:
        question_format = question.get("format")
        if question_format in multi_groups:
            answers = question.get("answers")
            multi_groups[question_format].append(
                tuple(answers) if isinstance(answers, list) else ()
            )

    multi_two_counts = Counter(multi_groups["multi-2"])
    multi_two_max = quality_controls["multi_2_same_set_max"]
    if multi_two_counts and max(multi_two_counts.values()) > multi_two_max:
        errors.append(
            f"{sim_id}: um mesmo conjunto correto de multi-2 aparece mais de "
            f"{multi_two_max} vezes"
        )
    multi_three_counts = Counter(multi_groups["multi-3"])
    if (
        quality_controls["multi_3_sets_must_be_unique"]
        and multi_three_counts
        and max(multi_three_counts.values()) > 1
    ):
        errors.append(
            f"{sim_id}: os quatro conjuntos corretos de multi-3 devem ser distintos"
        )

    for question_format, control_key in (
        ("multi-2", "multi_2_common_letter_frequency_min"),
        ("multi-3", "multi_3_common_letter_frequency_min"),
    ):
        formatted_questions = [
            question
            for question in questions
            if question.get("format") == question_format
            and isinstance(question.get("options"), dict)
        ]
        common_letters = (
            set.intersection(
                *(set(question["options"]) for question in formatted_questions)
            )
            if formatted_questions
            else set()
        )
        answer_letter_counts = Counter(
            letter for answer_set in multi_groups[question_format] for letter in answer_set
        )
        minimum = quality_controls[control_key]
        underrepresented = {
            letter: answer_letter_counts.get(letter, 0)
            for letter in sorted(common_letters)
            if answer_letter_counts.get(letter, 0) < minimum
        }
        if underrepresented:
            errors.append(
                f"{sim_id}: letras sub-representadas em {question_format} "
                f"{underrepresented}; mínimo {minimum}"
            )

    multi_letter_counts = Counter(
        letter
        for answer_set in multi_groups["multi-2"] + multi_groups["multi-3"]
        for letter in answer_set
    )
    multi_letter_max = quality_controls["multi_answer_letter_frequency_max"]
    if multi_letter_counts and max(multi_letter_counts.values()) > multi_letter_max:
        errors.append(
            f"{sim_id}: uma posição aparece em mais de {multi_letter_max} das "
            "36 respostas múltiplas "
            f"{dict(sorted(multi_letter_counts.items()))}"
        )

    if single and multi_two_counts and multi_three_counts:
        blind_modal_score = (
            max(Counter(first_answer(question) for question in single).values())
            + max(multi_two_counts.values())
            + max(multi_three_counts.values())
        )
        blind_modal_max = quality_controls["blind_modal_score_max"]
        if blind_modal_score > blind_modal_max:
            errors.append(
                f"{sim_id}: estratégia cega pelas posições modais acertaria "
                f"{blind_modal_score}/65; máximo {blind_modal_max}"
            )


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
    specs = manifest.get("simulators")
    if not isinstance(specs, list):
        return loaded, ["manifesto: simulators deve ser uma lista"]
    if len(specs) != 3 or {
        spec.get("id") for spec in specs if isinstance(spec, dict)
    } != {"SIM-A", "SIM-B", "SIM-C"}:
        errors.append("manifesto: esperado exatamente SIM-A, SIM-B e SIM-C")
    if manifest.get("visibility") != "public-versioned":
        errors.append("manifesto: visibility deve ser public-versioned")
    if manifest.get("answer_key_quality_controls") != ANSWER_KEY_QUALITY_CONTROLS:
        errors.append("manifesto: controles de qualidade do gabarito divergentes")
    required_spec_keys = {
        "id",
        "questions",
        "duration_minutes",
        "language",
        "domain_counts",
        "task_counts",
        "format_counts",
        "type_counts",
        "difficulty_counts",
        "source",
        "outputs",
    }
    for spec in specs:
        if not isinstance(spec, dict):
            errors.append("manifesto: cada simulado deve ser um objeto")
            continue
        sim_id = spec.get("id")
        missing_keys = sorted(required_spec_keys - set(spec))
        if missing_keys:
            errors.append(f"{sim_id}: chaves obrigatórias ausentes {missing_keys}")
            continue
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
    if errors:
        return loaded, errors

    for spec in specs:
        source = ROOT / str(spec["source"])
        if not source.is_file():
            errors.append(f"{spec['id']}: banco autoral ausente em {spec['source']}")
            continue
        try:
            bank = read_json(source)
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f"{spec['id']}: não foi possível ler o banco: {exc}")
            continue
        if not isinstance(bank, dict):
            errors.append(f"{spec['id']}: banco JSON deve ser um objeto")
            continue
        questions = validate_bank(
            bank, spec, errors, manifest["answer_key_quality_controls"]
        )
        all_questions.extend(questions)
        loaded.append((spec, bank, source))
    if len(loaded) == 3:
        validate_simulator_similarity(all_questions, errors)
    return loaded, errors


def validate_rendered_state(
    manifest: dict[str, Any],
    loaded: list[tuple[dict[str, Any], dict[str, Any], Path]],
    errors: list[str],
) -> None:
    """Confirm manifest hashes and generated Markdown match their JSON banks."""
    if manifest.get("status") != "validated-versioned":
        errors.append("manifesto: status deve ser validated-versioned")
    for spec, bank, source in loaded:
        if spec.get("validated") is not True:
            errors.append(f"{spec['id']}: campo validated deve ser true")
        digest = canonical_json_sha256(source)
        if spec.get("source_sha256") != digest:
            errors.append(f"{spec['id']}: hash canônico diverge do banco")
        expected_renderings = [
            render_questions(bank),
            render_answers(bank),
            render_report(bank),
        ]
        for output, expected_text in zip(spec["outputs"], expected_renderings):
            output_path = ROOT / output
            if not output_path.is_file():
                errors.append(f"{spec['id']}: saída versionada ausente {output}")
                continue
            try:
                actual_text = output_path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                errors.append(f"{spec['id']}: falha ao ler {output}: {exc}")
                continue
            if actual_text != expected_text:
                errors.append(f"{spec['id']}: saída desatualizada {output}")


def render_questions(bank: dict[str, Any]) -> str:
    sim_id = bank["id"]
    lines = [
        f"# {sim_id} — Questions",
        "",
        "**Navigation:** [Simulators index](../README.md) | "
        "[Result report](Relatorio.md)",
        "",
        "- **Time:** 130 minutes",
        "- **Language:** English",
        "- **Rules:** Closed book. Complete all 65 questions before opening the answer key.",
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
        "**Navigation:** [Questions](Questoes.md) | "
        "[Commented answer key](Gabarito.md) | [Result report](Relatorio.md)",
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
        "**Navigation:** [Simulators index](../README.md) | "
        "[Questions](Questoes.md)",
        "",
        "- **Date:** ____-__-__",
        "- **Time used:** ___ / 130 minutes",
        "- **Correct answers:** ___ / 65",
        "- **Score:** ___%",
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
        write_text_lf(output_paths[0], render_questions(bank))
        write_text_lf(output_paths[1], render_answers(bank))
        write_text_lf(output_paths[2], render_report(bank))
        spec["source_sha256"] = canonical_json_sha256(source)
        spec["validated"] = True
    manifest["validation_date"] = date.today().isoformat()
    manifest["status"] = "validated-versioned"
    write_json(MANIFEST_PATH, manifest)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Valida os bancos versionados sem reescrever os cadernos ou o manifesto.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        manifest = read_json(MANIFEST_PATH)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"FALHA: manifesto inválido ou ilegível: {exc}", file=sys.stderr)
        return 1
    if not isinstance(manifest, dict):
        print("FALHA: manifesto deve ser um objeto JSON.", file=sys.stderr)
        return 1
    loaded, errors = load_and_validate(manifest)
    if not errors and args.validate_only:
        validate_rendered_state(manifest, loaded, errors)
    if errors:
        print(f"FALHA: {len(errors)} problema(s) nos simulados autorais.", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    if not args.validate_only:
        render_all(manifest, loaded)
        validate_rendered_state(manifest, loaded, errors)
        if errors:
            print("FALHA: renderização não ficou sincronizada.", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 1
    total = sum(len(bank["questions"]) for _, bank, _ in loaded)
    action = "validadas" if args.validate_only else "validadas e renderizadas"
    print(
        f"OK: {len(loaded)} simulados, {total} questões autorais {action}; "
        "pacote versionável validado."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
