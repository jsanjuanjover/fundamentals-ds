"""Revisa los notebooks de apuntes antes de hacer commit.

Uso:
    uv run python scripts/check_notebooks.py [NOTEBOOK ...] [--no-exec]

Sin argumentos, revisa todos los notebooks del repositorio. Termina con código 1
si encuentra algún ERROR; los AVISOS se muestran pero no hacen fallar la revisión.
"""

import argparse
import re
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_HEADINGS = [f"## {i}." for i in range(1, 7)]

LOCAL_PATH_PATTERNS = [
    r"/home/",
    r"/Users/",
    r"[A-Za-z]:\\",
    r"~/",
    r"\.\./data",
]

# Restos de enunciados, material del curso o trabajo sin terminar
FORBIDDEN_TERMS = [
    r"\bUOC\b",
    r"\bPEC\d*\b",
    r"\bEjercicio\s*[\d:]",
    r"\bEnunciado\b",
    r"\(\s*\d+(?:[.,]\d+)?\s*puntos?\s*\)",
    r"<strong>\s*(?:Ejercicio|Pregunta|Análisis|Debate)",
    r"\bTODO\b",
    r"\bFIXME\b",
    r"@uoc\.edu",
]

MAX_OUTPUT_BYTES = 500_000
MAX_NOTEBOOK_BYTES = 5_000_000
MAX_TEXT_OUTPUT_LINES = 50
EXEC_TIMEOUT = 600


def find_notebooks() -> list[Path]:
    return sorted(
        p
        for p in REPO_ROOT.rglob("*.ipynb")
        if ".ipynb_checkpoints" not in p.parts and ".venv" not in p.parts
    )


def check_execution(nb, path: Path, errors: list[str]) -> None:
    client = NotebookClient(
        nb,
        timeout=EXEC_TIMEOUT,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
    )
    try:
        client.execute()
    except CellExecutionError as exc:
        plain = re.sub(r"\x1b\[[0-9;]*m", "", str(exc))  # quita colores ANSI
        lines = plain.strip().splitlines()
        errors.append(f"falla la ejecución: {lines[-1] if lines else 'error'}")


def check_sources(nb, errors: list[str]) -> None:
    for idx, cell in enumerate(nb.cells):
        for pattern in LOCAL_PATH_PATTERNS:
            if re.search(pattern, cell.source):
                errors.append(f"celda {idx}: ruta local ({pattern!r})")
        for pattern in FORBIDDEN_TERMS:
            if re.search(pattern, cell.source):
                errors.append(f"celda {idx}: término prohibido ({pattern!r})")


def check_headings(nb, errors: list[str]) -> None:
    markdown = [c.source for c in nb.cells if c.cell_type == "markdown"]
    positions = []
    for heading in REQUIRED_HEADINGS:
        pos = next(
            (i for i, src in enumerate(markdown)
             if re.search(rf"^{re.escape(heading)}", src, re.MULTILINE)),
            None,
        )
        if pos is None:
            errors.append(f"falta la sección '{heading} ...'")
        else:
            positions.append(pos)
    if positions != sorted(positions):
        errors.append("las secciones no están en orden")


def output_text(out) -> str:
    text = out.get("text") or out.get("data", {}).get("text/plain", "")
    return "".join(text) if isinstance(text, list) else text


def check_outputs(nb, warnings: list[str]) -> None:
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        for out in cell.get("outputs", []):
            size = len(nbformat.writes(nbformat.v4.new_notebook(
                cells=[nbformat.v4.new_code_cell(outputs=[out])])))
            if size > MAX_OUTPUT_BYTES:
                warnings.append(f"celda {idx}: salida de {size / 1e3:.0f} KB")
            text = output_text(out)
            n_lines = text.count("\n")
            if n_lines > MAX_TEXT_OUTPUT_LINES:
                warnings.append(f"celda {idx}: salida de texto de {n_lines} líneas")
            if re.search(r"/home/|/Users/", text):
                warnings.append(f"celda {idx}: la salida contiene una ruta local")

    total = len(nbformat.writes(nb))
    if total > MAX_NOTEBOOK_BYTES:
        warnings.append(f"el notebook ocupa {total / 1e6:.1f} MB")


def check_notebook(path: Path, execute: bool) -> bool:
    nb = nbformat.read(path, as_version=4)
    errors: list[str] = []
    warnings: list[str] = []

    check_sources(nb, errors)
    check_headings(nb, errors)
    check_outputs(nb, warnings)  # salidas guardadas en el fichero
    if execute:
        check_execution(nb, path, errors)

    rel = path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
    status = "FALLO" if errors else ("AVISO" if warnings else "OK")
    print(f"[{status}] {rel}")
    for msg in errors:
        print(f"    ERROR {msg}")
    for msg in warnings:
        print(f"    AVISO {msg}")
    return not errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("notebooks", nargs="*", type=Path)
    parser.add_argument("--no-exec", action="store_true", help="no ejecutar los notebooks")
    args = parser.parse_args()

    paths = [p.resolve() for p in args.notebooks] or find_notebooks()
    if not paths:
        print("No se han encontrado notebooks.")
        return 0

    results = [check_notebook(p, execute=not args.no_exec) for p in paths]
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
