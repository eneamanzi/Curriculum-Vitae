#!/usr/bin/env python3
"""Dumps every data/*.json file, in filename order (which is render order,
see the numeric prefixes), as a single Markdown reference document - once
fully in English, then fully in Italian. Nothing is hand-picked or curated
per domain: the whole JSON structure of every file is walked and rendered
generically (keys as labels, lists as items), so a field added to any data
file later shows up here automatically - nothing is ever silently left out.

Not part of the automated pipeline - run by hand, locally, whenever you want
a single reference document to read/copy pieces from (e.g. filling out a
LinkedIn/Indeed profile by hand). Output is real Markdown - **bold**/*italic*
already in the source JSON is passed through as-is, untouched, since a
Markdown viewer renders it correctly; nothing here is stripped or reworded.

Usage: python3 scripts-website-data/dump_data_markdown.py [output-path]
       (defaults to cv_dump_linkedin.md at the repo root if omitted)
"""

import glob
import json
import os
import sys

REPO_ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(REPO_ROOT, "data")
DEFAULT_OUTPUT = os.path.join(REPO_ROOT, "cv_dump_linkedin.md")


def resolve(value, lang):
    """Recursively replaces every bilingual {"en": ..., "it": ...} dict with
    just the value for `lang` (falling back to whichever language is present,
    so nothing is silently dropped if one is missing) - everything else
    (plain dicts, lists, scalars) is left as-is. After this, the structure's
    dict/list/scalar shape is unambiguous - no more bilingual dicts hiding
    inside what render_value needs to treat as a plain scalar."""
    if isinstance(value, dict) and value and set(value.keys()) <= {"en", "it"}:
        return resolve(value.get(lang, value.get("en", value.get("it"))), lang)
    if isinstance(value, dict):
        return {key: resolve(val, lang) for key, val in value.items()}
    if isinstance(value, list):
        return [resolve(item, lang) for item in value]
    return value


def render_value(value, indent=""):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            if isinstance(val, (dict, list)):
                lines.append(f"{indent}- **{key}:**\n{render_value(val, indent + '  ')}")
            else:
                lines.append(f"{indent}- **{key}:** {val}")
        return "\n".join(lines)

    if isinstance(value, list):
        if not value:
            return f"{indent}_(none)_"
        lines = []
        for i, item in enumerate(value, start=1):
            if isinstance(item, dict):
                # Numbered marker so consecutive dict entries (e.g. multiple
                # "profiles") don't visually run together into one another.
                lines.append(f"{indent}- **#{i}**")
                lines.append(render_value(item, indent + "  "))
            elif isinstance(item, list):
                lines.append(render_value(item, indent))
            else:
                lines.append(f"{indent}- {item}")
        return "\n".join(lines)

    return str(value)


def render_file(path, lang):
    with open(path, encoding="utf-8") as f:
        data = resolve(json.load(f), lang)

    lines = [f"## {os.path.basename(path)}", ""]
    if isinstance(data, list):
        for i, entry in enumerate(data, start=1):
            lines.append(f"### Entry {i}")
            lines.append(render_value(entry))
            lines.append("")
    else:
        lines.append(render_value(data))
        lines.append("")
    return "\n".join(lines)


def render_language(lang, label):
    paths = sorted(glob.glob(os.path.join(DATA_DIR, "*.json")))
    sections = [render_file(path, lang) for path in paths]
    return f"# {label}\n\n" + "\n---\n\n".join(sections)


def build():
    return render_language("en", "English") + "\n\n===\n\n" + render_language("it", "Italiano") + "\n"


def main():
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(build())
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
