**English version** | [Versione italiana](README.it.md)

# Curriculum Vitae - Enea Manzi

This repository is the **single source of truth** for my Curriculum Vitae, Cover Letter, and personal website content. Everything - work experience, education, skills, projects, publications - lives once, under `data/`, and four different outputs are generated from it automatically:

1. **4 PDFs** (CV + Cover Letter, Italian + English) via LaTeX/LuaLaTeX.
2. **`resume.json`**, a JSON Resume-format file that feeds the `/cv/` page on [eneamanzi.github.io](https://github.com/eneamanzi/eneamanzi.github.io).
3. **`papers.bib`**, a BibTeX file that feeds the website's dedicated `/publications/` page.
4. **New project pages** on the website, auto-scaffolded from the same data whenever a project doesn't have one yet.

No content is ever typed twice.

## View the Compiled Documents (PDF)

The PDFs are automatically generated and hosted on the `pdf-release` branch.

| Document | Version | View |
| :--- | :--- | :--- |
| **Curriculum Vitae** | **Italian** | [**cv_italian.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cv_italian.pdf) |
| **Curriculum Vitae** | **English** | [**cv_english.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cv_english.pdf) |
| **Cover Letter** | **Italian** | [**cover_letter_italian.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cover_letter_italian.pdf) |
| **Cover Letter** | **English** | [**cover_letter_english.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cover_letter_english.pdf) |

## Architecture

```
data/*.json  (single source of truth, bilingual, Markdown emphasis)
     │
     ├──► commons/lua_data_loader.tex ──► LuaLaTeX ──► 4 PDFs ──► pushed to
     │                                                              eneamanzi.github.io
     │                                                              (assets/pdf/)
     ├──► scripts-website-data/generate_resume_json.py
     │       (validated: resume_pydantic_schema.py)
     │       └──► resume.json ─────────────────────────────────┐
     │                                                          │
     ├──► scripts-website-data/generate_socials_yml.py          │
     │       └──► socials.yml ─────────────────────────────────┤
     │                                                          │
     └──► scripts-website-data/generate_papers_bib.py           │  pushed together to
             └──► papers.bib ─────────────────────────────────  │  eneamanzi.github.io
                                                                 │  (assets/json/, _data/,
             scripts/scaffold_project_pages.py ◄─────────────────  _bibliography/)
                (the website repo's own script, run against the
                 checked-out website repo before the commit above,
                 so a new project page - if any - lands in the
                 same push; see Website Integration)
```

Two independent GitHub Actions workflows drive the CV-repo side (see [CI/CD](#cicd)) - one for the PDFs, one for everything else. `papers.bib`'s `bibtex` field per publication is citation text as-is (hand-written while a paper is only submitted, copied verbatim from the publisher once it's indexed) - the generator does not parse or reconstruct BibTeX from separate fields.

## Project Structure

* `data/`: **the database.** One JSON file per domain, numbered to reflect render order (step of 10, leaving room for future insertions):
  * `10-personal.json` - name, contact info, location, social profiles, the website bio/tagline
  * `20-education.json` - degrees, thesis, grades
  * `30-work.json` - work experience
  * `40-research.json` - research activities (has no PDF/JSON-Resume standard equivalent - see `commons/lua_data_loader.tex` and `resume_pydantic_schema.py` for how it's handled)
  * `50-projects.json` - personal/academic projects (each needs a stable `id`, `category`, and `importance` - see [Common Tasks](#common-tasks))
  * `60-publications.json` - papers (`bibtex` field is the citation text as-is - see [Common Tasks](#common-tasks))
  * `70-languages.json` - spoken languages
  * `80-skills.json` - skills, including the "Soft Skills" category (rendered as its own section everywhere)
  * `90-meta.json` - GDPR/legal boilerplate (PDF-only, never reaches the website)
* `cv.tex` / `cover_letter.tex`: the LaTeX templates. They call the Lua loader.
* `commons/lua_data_loader.tex`: the Lua script that reads `data/*.json`, converts Markdown emphasis (`**bold**`/`*italic*`) to LaTeX, and populates the document sections in the selected language.
* `scripts-website-data/generate_resume_json.py`: builds `resume.json` from `data/`, validated against `scripts-website-data/resume_pydantic_schema.py` before being written.
* `scripts-website-data/generate_socials_yml.py`: builds the website's `_data/socials.yml` (email, LinkedIn/GitHub usernames, CV PDF link) from `data/10-personal.json` - only the fields that are genuine CV facts; site-only settings (Google Scholar ID, WeChat QR, etc.) stay manually maintained on the website side.
* `scripts-website-data/generate_papers_bib.py`: builds the website's `_bibliography/papers.bib` from `data/60-publications.json`, concatenating each entry's `bibtex` field as-is and injecting `abstract` (from the structured `abstract` field, so it's never typed twice) and `abbr` (from `venueAbbr`, if set).
* `img/`: static assets (profile picture, signature).

## Common Tasks

Where to make each kind of change - every one of these is just editing a JSON file and pushing; the PDFs and the website update themselves.

**Update your bio, contact info, or social links**
Edit `data/10-personal.json`: `email`, `phone`, `location`, `profiles` (LinkedIn/GitHub/WhatsApp), `summary` (the website's "Professional Summary" bio), `websiteLabel` (the tagline shown on the website, distinct from `label` which is the PDF's document title).

**Add a job or internship**
Add an entry to the array in `data/30-work.json`: `name`, `position`, `location`, `startDate`/`endDate` (`MM/YYYY`), `summary`, `highlights` (bullet list, Markdown allowed).

**Add a research activity**
Same shape as work, in `data/40-research.json`. Renders as its own "Research" section in both the PDF and the website (a website-only template override - see [Website Integration](#website-integration)).

**Add a degree**
Add an entry to `data/20-education.json`: `institution`, `location`, `area`, `studyType`, `startDate`/`endDate`, `score` (e.g. `"Final Grade: 110/110 cum laude"` - the "Final Grade:"/"Voto:" prefix is stripped automatically for the website's dedicated `score` field). Add a `thesis: { title, supervisors }` object if there is one - it becomes two extra highlight lines ("Thesis: ...", "Supervisors: ...") automatically.

**Add a project**
Add an entry to `data/50-projects.json`:

```json
{
  "id": "some-stable-slug",       // assigned once, never changed - even if "name" changes later
  "importance": 50,                // website display order (step of 10) - independent of this array's own order
  "category": "Academic",
  "name": { "en": "...", "it": "..." },
  "course": { "en": "...", "it": "..." },
  "description": { "en": "...", "it": "..." },
  "highlights": { "en": ["..."], "it": ["..."] },
  "keywords": ["..."]
}
```

Push it, and a new `_projects/<id>.md` is auto-created on the website with no further action - see [Website Integration](#website-integration) for how the matching works and what to do if you want to expand that page with a full write-up afterward.

**Add a publication**
Add an entry to `data/60-publications.json`: `type`, `status` (`{"en": "submitted", "it": "sottomesso"}` or similar), `venue`, `year`, `date`, `authors` (plain string, e.g. `"Enea Manzi, Marco Anisetti"`), `title`, `abstract` (feeds both the PDF/`resume.json` and, injected automatically, the website's `papers.bib`).

Also write a `bibtex` field: the literal citation text, e.g.
```json
"bibtex": "@unpublished{manzi2026itadata,\n  author = {Manzi, Enea and Anisetti, Marco},\n  title  = {...},\n  year   = {2026},\n  note   = {Submitted to ITADATA 2026}\n}"
```
Write it by hand while the paper is only submitted (no DOI/pages/venue yet); once it's actually published somewhere, replace it with the ready-made BibTeX citation copied from the publisher (IEEE/Springer/ACM/...) instead of retyping it - don't reconstruct fields that are already given to you. Add extra fields the website understands (`doi`, `pdf`, `video`, `code`, `selected`, `bibtex_show`, ...) directly inside that same `bibtex` text when you actually have a real value for them - see the header of a generated `papers.bib` for the full list, or `CUSTOMIZATIONS.md` in the website repo. Optionally add `"venueAbbr": "SOME-ABBR"` for a venue badge - it needs a matching entry in the website's `_data/venues.yml` (maintained by hand there, not generated - see [Website Integration](#website-integration)).

**Add or update a skill category / language**
`data/80-skills.json` (keywords support Markdown emphasis, stripped automatically for the website since that template doesn't render it) / `data/70-languages.json`. The `"Soft Skills"` category name is special-cased everywhere (own section, per-item bold label rendering) - don't rename it.

**Emphasize text anywhere above**
Use `**bold**` / `*italic*` in any free-text field - never raw LaTeX or HTML (see [Data Conventions](#data-conventions)).

**Check your changes before pushing**
See [Run Locally](#run-locally) - compile the PDF, and/or run the `generate_*.py` scripts locally to see the exact `resume.json`/`socials.yml`/`papers.bib` that would be pushed (the first two fail loudly, listing every problem, if something in `data/` is malformed).

## Data Conventions

* **Bilingual fields** are `{"en": "...", "it": "..."}` objects; a plain string means "same in both languages" (e.g. a person's name, "APIGuard Assurance").
* **Emphasis** inside free text uses Markdown - `**bold**`, `*italic*` - never raw LaTeX or HTML. Each consumer converts it to whatever it needs (LaTeX via the Lua loader, HTML via Jekyll's `markdownify`, or stripped to plain text where a template doesn't support it - see `scripts-website-data/generate_resume_json.py`'s `strip_md`).
* **Numbering** (`10-`, `20-`, ...): reflects render order, not creation order. The step of 10 leaves room to insert a new domain later (e.g. `45-awards.json`) without renumbering everything.

## CI/CD

Two independent GitHub Actions workflows watch `data/**` - independent so that a failure in one never blocks the other:

* **`build-latex.yml`** - compiles all 4 PDFs, publishes them to the `pdf-release` branch, and pushes the two CVs (not the cover letters) to the website's `assets/pdf/`.
* **`generate-website-data.yml`** - runs `generate_resume_json.py`, `generate_socials_yml.py`, and `generate_papers_bib.py`; validates the JSON Resume output (Pydantic) and formats it with Prettier (matching the website's own `.prettierrc` via `--print-width 150`, since that config file lives in the other repo); then, in the same job, checks out the website repo, copies the three generated files in, runs *the website's own* `scripts/scaffold_project_pages.py` against that checkout (so a newly-needed project page lands in the same commit instead of triggering a separate push from the website side), and pushes everything in one commit to `assets/json/`, `_data/`, and `_bibliography/`. On a pull request it only validates, it never touches the website.

Both need the `API_TOKEN_GITHUB` repository secret (a PAT with write access to `eneamanzi.github.io`) to push cross-repo.

## Website Integration

`eneamanzi.github.io` is a separate repository; this one only pushes files into it, it never contains its logic. Things worth knowing if you're debugging the website side:

* `_includes/cv/render.liquid`, `skills.liquid`, and `languages.liquid` are **local overrides** of the `al_folio_cv` gem's templates (Jekyll's `includes_load_paths` mechanism lets a site-local file take precedence). They add a "Research" section (no standard JSON Resume equivalent) and fix a couple of upstream cosmetic bugs (empty `()`/icons when a field is blank). If the gem updates upstream, these need a manual diff/re-sync.
* `scripts/scaffold_project_pages.py` (in the website repo's own `scripts/` folder, unrelated to this repo's `scripts-website-data/`) is invoked directly by this repo's `generate-website-data.yml` (see [CI/CD](#cicd)), against the website checkout, before the commit - so it never needs a separate push of its own. For any project with no matching page yet, it creates one under `_projects/<id>.md`, seeded with the CV's summary and highlights under a "Summary (from CV)" heading. It matches by the project's stable `cv_id` frontmatter field, not by title, so renaming a project's display name or a page's title later never causes a duplicate page. The website's own `scaffold-projects.yml` workflow (triggered by a push touching `resume.json`) still exists as a dormant safety net - in the normal case it finds nothing left to do.
* `_bibliography/papers.bib` is generated (see above) - never edit it in the website repo. `_data/coauthors.yml` and `_data/venues.yml` are the opposite: they stay **manually maintained in the website repo**, since they're rendering preferences (which URL to link a coauthor's name to, what color a venue badge gets), not CV facts. See `CUSTOMIZATIONS.md` in the website repo (section "Publications") for a real build-crash this surfaced (a commented-out BibTeX-shaped example is not actually inert to the parser in use) and the full list of extra fields the publications template supports.

## Run Locally

### Compiling the PDFs

Requires a TeX distribution (TeX Live, MiKTeX, or MacTeX) that includes **LuaLaTeX**.

```bash
git clone https://github.com/eneamanzi/curriculum-vitae.git
cd curriculum-vitae
```

Edit the JSON files under `data/` with your own information (start with `data/10-personal.json`).

**English (default):**
```bash
latexmk -lualatex -jobname=cv_english cv.tex
latexmk -lualatex -jobname=cover_letter_english cover_letter.tex
```

**Italian:** the Italian translation is triggered by injecting `\def\makeitalian{1}` before the file is read.
```bash
latexmk -lualatex -jobname=cv_italian -e '$lualatex="lualatex %O \def\makeitalian{1} \input{%S}"' cv.tex
latexmk -lualatex -jobname=cover_letter_italian -e '$lualatex="lualatex %O \def\makeitalian{1} \input{%S}"' cover_letter.tex
```

### Testing the Website Data Generators

Requires Python 3 and the packages in `scripts-website-data/requirements.txt` (just `pydantic`):

```bash
pip install -r scripts-website-data/requirements.txt
python3 scripts-website-data/generate_resume_json.py /tmp/resume.json
python3 scripts-website-data/generate_socials_yml.py /tmp/socials.yml
python3 scripts-website-data/generate_papers_bib.py /tmp/papers.bib
```

The first two exit with a non-zero status and a full list of validation errors if `data/` produces something malformed - nothing is ever written half-broken. `generate_papers_bib.py` has no schema to validate against (each `bibtex` field is free text) - inspect `/tmp/papers.bib` by eye, or run it through a real BibTeX parser (e.g. Python's `bibtexparser`) if you want to double-check it.

## License
[MIT](https://choosealicense.com/licenses/mit/)
