#!/usr/bin/env python3
"""Extrai e valida o inventário curricular de uma página salva da Udemy."""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterator


HTML_RELATIVO = (
    Path("01_Fontes")
    / "Udemy"
    / "html do curso"
    / "Course_ Ultimate AWS Certified Solutions Architect Associate 2026 _ Udemy.html"
)
CSV_RELATIVO = (
    Path("01_Fontes") / "Udemy" / "Inventario_Curso_Udemy_SAA-C03.csv"
)

TAGS_VAZIAS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


@dataclass
class No:
    tag: str
    atributos: dict[str, str | None] = field(default_factory=dict)
    filhos: list["No | str"] = field(default_factory=list)
    pai: "No | None" = None

    def descendentes(self) -> Iterator["No"]:
        pilha = [filho for filho in reversed(self.filhos) if isinstance(filho, No)]
        while pilha:
            atual = pilha.pop()
            yield atual
            pilha.extend(
                filho
                for filho in reversed(atual.filhos)
                if isinstance(filho, No)
            )

    def texto(self) -> str:
        partes: list[str] = []
        pilha: list[No | str] = list(reversed(self.filhos))
        while pilha:
            atual = pilha.pop()
            if isinstance(atual, str):
                partes.append(atual)
            else:
                pilha.extend(reversed(atual.filhos))
        return normalizar_espacos(" ".join(partes))


class ParserHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.raiz = No("documento")
        self.pilha = [self.raiz]

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        tag = tag.lower()
        no = No(tag, dict(attrs), pai=self.pilha[-1])
        self.pilha[-1].filhos.append(no)
        if tag not in TAGS_VAZIAS:
            self.pilha.append(no)

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        no = No(tag.lower(), dict(attrs), pai=self.pilha[-1])
        self.pilha[-1].filhos.append(no)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        for indice in range(len(self.pilha) - 1, 0, -1):
            if self.pilha[indice].tag == tag:
                del self.pilha[indice:]
                return

    def handle_data(self, data: str) -> None:
        if data:
            self.pilha[-1].filhos.append(data)


def normalizar_espacos(valor: str) -> str:
    return re.sub(r"\s+", " ", valor).strip()


def primeiro_descendente(no: No, predicado) -> No | None:
    return next((candidato for candidato in no.descendentes() if predicado(candidato)), None)


def atributo_data_purpose(no: No) -> str:
    return no.atributos.get("data-purpose") or ""


def minutos_do_texto(valor: str) -> int | None:
    valor = normalizar_espacos(valor).lower()
    horas = re.search(r"(\d+)\s*h", valor)
    minutos = re.search(r"(\d+)\s*(?:m|min)\b", valor)
    if not horas and not minutos:
        return None
    return (int(horas.group(1)) * 60 if horas else 0) + (
        int(minutos.group(1)) if minutos else 0
    )


def encontrar_ancestral(no: No, tag: str) -> No | None:
    atual = no.pai
    while atual is not None:
        if atual.tag == tag:
            return atual
        atual = atual.pai
    return None


def extrair_inventario(html: str) -> list[dict[str, object]]:
    parser = ParserHTML()
    parser.feed(html)
    parser.close()

    secoes: list[tuple[int, No]] = []
    for no in parser.raiz.descendentes():
        correspondencia = re.fullmatch(r"section-panel-(\d+)", atributo_data_purpose(no))
        if correspondencia:
            secoes.append((int(correspondencia.group(1)), no))
    secoes.sort(key=lambda parte: parte[0])

    inventario: list[dict[str, object]] = []

    for indice_secao_zero, no_secao in secoes:
        botao_titulo = primeiro_descendente(
            no_secao,
            lambda no: no.tag == "button"
            and (no.atributos.get("id") or "").startswith("accordion-panel-title--"),
        )
        if botao_titulo is None:
            raise ValueError(f"Título não encontrado na seção {indice_secao_zero + 1}.")

        titulo_com_prefixo = botao_titulo.texto()
        titulo_secao = re.sub(
            rf"^Seção\s+{indice_secao_zero + 1}\s*:\s*",
            "",
            titulo_com_prefixo,
            flags=re.IGNORECASE,
        )

        itens_secao: list[tuple[int, No]] = []
        for no in no_secao.descendentes():
            correspondencia = re.fullmatch(
                rf"curriculum-item-{indice_secao_zero}-(\d+)",
                atributo_data_purpose(no),
            )
            if correspondencia:
                itens_secao.append((int(correspondencia.group(1)), no))
        itens_secao.sort(key=lambda parte: parte[0])

        indices_locais = [indice for indice, _ in itens_secao]
        if indices_locais != list(range(len(itens_secao))):
            raise ValueError(
                f"Índices locais inválidos na seção {indice_secao_zero + 1}: "
                f"{indices_locais}"
            )

        for _, no_item in itens_secao:
            no_titulo = primeiro_descendente(
                no_item, lambda no: atributo_data_purpose(no) == "item-title"
            )
            if no_titulo is None:
                raise ValueError(
                    f"Item sem título na seção {indice_secao_zero + 1}."
                )

            titulo_original = no_titulo.texto()
            correspondencia_aula = re.fullmatch(r"(\d+)\.\s*(.+)", titulo_original)
            if correspondencia_aula:
                numero_aula: int | str = int(correspondencia_aula.group(1))
                titulo = correspondencia_aula.group(2)
            else:
                numero_aula = ""
                titulo = titulo_original

            referencias_icones = {
                no.atributos.get("xlink:href")
                for no in no_item.descendentes()
                if no.tag == "use"
            }
            if "#icon-video" in referencias_icones:
                tipo = "vídeo"
            elif "#icon-article" in referencias_icones:
                tipo = "artigo"
            elif re.match(r"^Teste\s+\d+\s*:", titulo_original, re.IGNORECASE):
                tipo = "quiz"
            elif re.match(r"^Simulado\s+\d+\s*:", titulo_original, re.IGNORECASE):
                tipo = "simulado"
            else:
                raise ValueError(f"Tipo não reconhecido: {titulo_original}")

            no_metadados = primeiro_descendente(
                no_item,
                lambda no: "curriculum-item-link--metadata"
                in (no.atributos.get("class") or ""),
            )
            duracao = minutos_do_texto(no_metadados.texto()) if no_metadados else None

            controle_progresso = primeiro_descendente(
                no_item,
                lambda no: no.tag == "input"
                and atributo_data_purpose(no) == "progress-toggle-button",
            )
            concluido = bool(
                controle_progresso is not None
                and "checked" in controle_progresso.atributos
            )

            item_lista = encontrar_ancestral(no_item, "li")
            aula_atual = bool(
                item_lista is not None
                and item_lista.atributos.get("aria-current") == "true"
            )

            inventario.append(
                {
                    "secao": indice_secao_zero + 1,
                    "titulo_secao": titulo_secao,
                    "indice_item": len(inventario) + 1,
                    "numero_aula": numero_aula,
                    "titulo": titulo,
                    "tipo": tipo,
                    "duracao_minutos": duracao if duracao is not None else "",
                    "concluido": "sim" if concluido else "não",
                    "aula_atual": "sim" if aula_atual else "não",
                }
            )

    return inventario


def validar(inventario: list[dict[str, object]]) -> None:
    secoes = {int(item["secao"]) for item in inventario}
    if secoes != set(range(1, 34)):
        raise ValueError(f"Esperadas 33 seções numeradas de 1 a 33; obtidas {secoes}.")

    if len(inventario) != 425:
        raise ValueError(f"Esperados 425 itens; obtidos {len(inventario)}.")

    indices = [int(item["indice_item"]) for item in inventario]
    if indices != list(range(1, 426)):
        raise ValueError("Os índices globais dos itens não formam a sequência 1–425.")

    numeros_aulas = [
        int(item["numero_aula"])
        for item in inventario
        if item["numero_aula"] != ""
    ]
    if numeros_aulas != list(range(1, 397)):
        ausentes = sorted(set(range(1, 397)) - set(numeros_aulas))
        duplicados = sorted(
            numero for numero in set(numeros_aulas) if numeros_aulas.count(numero) > 1
        )
        raise ValueError(
            "A numeração das aulas não corresponde a 1–396 em ordem. "
            f"Ausentes: {ausentes}; duplicados: {duplicados}."
        )

    contagem_tipos = {
        tipo: sum(1 for item in inventario if item["tipo"] == tipo)
        for tipo in ("vídeo", "artigo", "quiz", "simulado")
    }
    esperado = {"vídeo": 385, "artigo": 11, "quiz": 28, "simulado": 1}
    if contagem_tipos != esperado:
        raise ValueError(
            f"Contagem por tipo divergente: {contagem_tipos}; esperado: {esperado}."
        )

    concluidos = sum(1 for item in inventario if item["concluido"] == "sim")
    if concluidos != 13:
        raise ValueError(f"Esperados 13 itens concluídos; obtidos {concluidos}.")

    atuais = [item for item in inventario if item["aula_atual"] == "sim"]
    if len(atuais) != 1 or atuais[0]["numero_aula"] != 14:
        raise ValueError(f"A aula atual esperada é a 14; obtido: {atuais}.")

    for item in inventario:
        tem_duracao = item["duracao_minutos"] != ""
        if item["tipo"] in {"vídeo", "artigo"} and not tem_duracao:
            raise ValueError(f"Conteúdo sem duração: {item}")
        if item["tipo"] in {"quiz", "simulado"} and tem_duracao:
            raise ValueError(f"Avaliação com duração inesperada: {item}")


def gravar_csv(destino: Path, inventario: list[dict[str, object]]) -> None:
    colunas = [
        "secao",
        "titulo_secao",
        "indice_item",
        "numero_aula",
        "titulo",
        "tipo",
        "duracao_minutos",
        "concluido",
        "aula_atual",
    ]
    with destino.open("w", encoding="utf-8-sig", newline="") as arquivo:
        escritor = csv.DictWriter(
            arquivo, fieldnames=colunas, extrasaction="raise", lineterminator="\n"
        )
        escritor.writeheader()
        escritor.writerows(inventario)


def main() -> int:
    workspace = Path(__file__).resolve().parents[2]
    origem = workspace / HTML_RELATIVO
    destino = workspace / CSV_RELATIVO

    if not origem.is_file():
        raise FileNotFoundError(f"HTML não encontrado: {origem}")

    inventario = extrair_inventario(origem.read_text(encoding="utf-8"))
    validar(inventario)
    gravar_csv(destino, inventario)

    print(f"CSV criado: {destino}")
    print("Validação: 33 seções; 425 itens; aulas 1–396 sem lacunas/duplicações.")
    print("Tipos: 385 vídeos; 11 artigos; 28 quizzes; 1 simulado.")
    print("Progresso: 13 concluídos; aula atual: 14. IAM Policies.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as erro:
        print(f"ERRO: {erro}", file=sys.stderr)
        raise
