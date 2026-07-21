#!/usr/bin/env python3
"""Generates the website's JSON Resume (assets/json/resume.json in eneamanzi.github.io)
from this repo's single source of truth in data/*.json.

Usage: python3 scripts/generate_resume_json.py <output-path>
"""

import json
import os
import re
import sys

from resume_pydantic_schema import Resume

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def read_data(filename):
    with open(os.path.join(DATA_DIR, filename), encoding="utf-8") as f:
        return json.load(f)


def en(node):
    """Bilingual {en, it} node -> English string/list. Plain strings/lists pass through."""
    if node is None:
        return node
    if isinstance(node, (str, list)):
        return node
    if isinstance(node, dict) and "en" in node:
        return node["en"]
    return node


def iso_date(mm_yyyy):
    """"12/2025" -> "2025-12-01" (ISO), so the site's Liquid templates (which extract
    the year via `| split: '-' | first`) show clean "2025 - 2026" badges instead of
    "12/2025 - 07/2026"."""
    if not mm_yyyy:
        return ""
    mm, yyyy = mm_yyyy.split("/")
    return f"{yyyy}-{mm}-01"


def strip_md(s):
    """Strips **bold**/*italic* markers without converting to HTML - used only for
    skills.keywords, the one field the site's skills.liquid does NOT markdownify."""
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", s)
    s = re.sub(r"\*(.*?)\*", r"\1", s)
    return s


def strip_score_prefix(s):
    """Removes a known label prefix ("Final Grade: " / "Voto: ") so the dedicated
    `score` field holds just the grade, matching the site's existing convention."""
    return re.sub(r"^(Final Grade|Voto):\s*", "", s)


def build_basics():
    p = read_data("10-personal.json")
    return {
        "name": f"{p['name']} {p['surname']}",
        "label": en(p["websiteLabel"]),
        "image": "",
        "email": p["email"],
        "phone": p["phone"],
        "summary": en(p["summary"]),
        "location": {
            "address": "",
            "postalCode": "",
            "city": p["location"]["city"],
            "countryCode": p["location"]["countryCode"],
            "region": p["location"]["region"],
        },
        "profiles": [
            {"network": prof["network"], "username": prof["username"], "url": prof["url"]}
            for prof in p["profiles"]
            if prof["url"]
        ],
    }


def build_education():
    entries = []
    for edu in read_data("20-education.json"):
        highlights = []
        if "thesis" in edu:
            highlights.append(f"Thesis: {en(edu['thesis']['title'])}")
            highlights.append(f"Supervisors: {edu['thesis']['supervisors']}")
        highlights.append(en(edu["score"]))
        entries.append(
            {
                "institution": en(edu["institution"]),
                "location": en(edu["location"]),
                "area": en(edu["area"]),
                "studyType": en(edu["studyType"]),
                "startDate": iso_date(edu["startDate"]),
                "endDate": iso_date(edu["endDate"]),
                "score": strip_score_prefix(en(edu["score"])),
                "courses": [],
                "highlights": highlights,
            }
        )
    return entries


def build_work():
    return [
        {
            "name": en(w["name"]),
            "position": en(w["position"]),
            "location": en(w["location"]),
            "startDate": iso_date(w["startDate"]),
            "endDate": iso_date(w["endDate"]),
            "summary": en(w["summary"]),
            "highlights": en(w["highlights"]),
        }
        for w in read_data("30-work.json")
    ]


def build_research():
    return [
        {
            "name": en(r["name"]),
            "location": en(r["location"]),
            "startDate": iso_date(r["startDate"]),
            "endDate": iso_date(r["endDate"]),
            "summary": en(r["summary"]),
            "highlights": en(r["highlights"]),
        }
        for r in read_data("40-research.json")
    ]


def build_projects():
    return [
        {
            "name": en(proj["name"]),
            # The PDF shows the course/context right above the description;
            # projects.liquid has no dedicated field for it, so it's folded in here.
            "summary": f"{en(proj['course'])}\n\n{en(proj['description'])}",
            "highlights": en(proj["highlights"]),
            "keywords": proj.get("keywords", []),
            # Non-standard fields (ignored by the CV page's Liquid templates), kept
            # separate here so the website's project-page scaffolder has clean,
            # structured data instead of having to re-parse them out of `summary`.
            "course": en(proj["course"]),
            "category": proj.get("category", "Academic"),
            # Stable identity for the website's project-page scaffolder, assigned
            # once in data/50-projects.json and never changed afterwards - lets
            # both the CV's `name` and the page's `title` be edited freely later
            # without breaking the "does this project already have a page" check.
            "id": proj["id"],
            # Website display-order for the project-page scaffolder, independent
            # of this array's own order (which reflects CV/PDF-relevant priority).
            "importance": proj["importance"],
        }
        for proj in read_data("50-projects.json")
    ]


def build_publications():
    entries = []
    for pub in read_data("60-publications.json"):
        is_submitted = en(pub["status"]) == "submitted"
        entries.append(
            {
                "title": en(pub["title"]),
                "publisher": f"Submitted to {pub['venue']}" if is_submitted else pub["venue"],
                "releaseDate": pub["year"],
                "summary": f"**{pub['authors']}**\n\n{en(pub['abstract'])}",
            }
        )
    return entries


def _skill_entry(s):
    return {
        "name": en(s["name"]),
        "level": "",
        "icon": "",
        "keywords": [strip_md(en(k)) for k in s["keywords"]],
    }


def build_skills():
    # "Soft Skills" is its own section in the PDF (print_skills in the Lua loader
    # special-cases it too), so it's split out here rather than left as just
    # another category inside the main Skills list.
    return [_skill_entry(s) for s in read_data("80-skills.json") if en(s["name"]) != "Soft Skills"]


def build_soft_skills():
    return [_skill_entry(s) for s in read_data("80-skills.json") if en(s["name"]) == "Soft Skills"]


def build_languages():
    return [
        {"language": en(lang["language"]), "fluency": en(lang["fluency"]), "icon": ""}
        for lang in read_data("70-languages.json")
    ]


def build():
    # Key order mirrors the CV's actual presentation order (Education, Work,
    # Research, Projects, Publications, Languages, Skills, Soft Skills), not the
    # conventional JSON Resume field order - the empty, unused sections trail at
    # the end.
    return {
        "_generated": (
            "AUTO-GENERATED by generate_resume_json.py in the Curriculum-Vitae "
            "repo. Do not edit this file directly - it is overwritten on every "
            "push to data/**. Edit data/*.json there instead."
        ),
        "basics": build_basics(),
        "education": build_education(),
        "work": build_work(),
        "research": build_research(),
        "projects": build_projects(),
        "publications": build_publications(),
        "languages": build_languages(),
        "skills": build_skills(),
        "softSkills": build_soft_skills(),
        "volunteer": [],
        "awards": [],
        "certificates": [],
        "interests": [],
        "references": [],
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/generate_resume_json.py <output-path>", file=sys.stderr)
        sys.exit(1)
    output_path = sys.argv[1]
    resume = build()
    # Full structural validation (types, required fields, ISO date format,
    # no unexpected keys) via resume_pydantic_schema.Resume - not a hand-picked partial
    # check. Raises pydantic.ValidationError listing every violation if the
    # build script or the source data produced something malformed.
    Resume.model_validate(resume, by_name=True)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(resume, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
