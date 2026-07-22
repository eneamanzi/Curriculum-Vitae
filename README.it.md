[English version](README.md) | **Versione Italiana**

# Curriculum Vitae - Enea Manzi

Questo repository è la **single source of truth** del mio Curriculum Vitae, Lettera di Presentazione, e di parte del contenuto del mio sito personale. Tutto - esperienze lavorative, istruzione, competenze, progetti, pubblicazioni - vive una volta sola, sotto `data/`, e da lì vengono generati automaticamente quattro output diversi:

1. **4 PDF** (CV + Lettera di Presentazione, italiano + inglese) via LaTeX/LuaLaTeX.
2. **`resume.json`**, un file in formato JSON Resume che alimenta la pagina `/cv/` su [eneamanzi.github.io](https://github.com/eneamanzi/eneamanzi.github.io).
3. **`papers.bib`**, un file BibTeX che alimenta la pagina dedicata `/publications/` del sito.
4. **Nuove pagine progetto** sul sito, generate automaticamente dagli stessi dati quando un progetto non ne ha ancora una.

Nessun contenuto viene mai scritto due volte.

## Visualizza i Documenti Compilati (PDF)

I PDF vengono generati automaticamente e sono disponibili sul branch `pdf-release`.

| Documento | Versione | Visualizza |
| :--- | :--- | :--- |
| **Curriculum Vitae** | **Italiano** | [**cv_italian.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cv_italian.pdf) |
| **Curriculum Vitae** | **Inglese** | [**cv_english.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cv_english.pdf) |
| **Lettera di Presentazione** | **Italiana** | [**cover_letter_italian.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cover_letter_italian.pdf) |
| **Lettera di Presentazione** | **Inglese** | [**cover_letter_english.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cover_letter_english.pdf) |

## Architettura

```
data/*.json  (single source of truth, bilingue, enfasi in Markdown)
     │
     ├──► commons/lua_data_loader.tex ──► LuaLaTeX ──► 4 PDF ──► pushati su
     │                                                              eneamanzi.github.io
     │                                                              (assets/pdf/)
     ├──► scripts-website-data/generate_resume_json.py
     │       (validato con: resume_pydantic_schema.py)
     │       └──► resume.json ─────────────────────────────────┐
     │                                                          │
     ├──► scripts-website-data/generate_socials_yml.py          │
     │       └──► socials.yml ─────────────────────────────────┤
     │                                                          │
     └──► scripts-website-data/generate_papers_bib.py           │  pushati insieme su
             └──► papers.bib ─────────────────────────────────  │  eneamanzi.github.io
                                                                 │  (assets/json/, _data/,
             scripts/scaffold_project_pages.py ◄─────────────────  _bibliography/)
                (lo script è del repo del sito, eseguito contro
                 quel checkout prima del commit qui sopra, così
                 un'eventuale pagina progetto nuova finisce nello
                 stesso push; vedi Integrazione con il Sito)
```

Due workflow GitHub Actions indipendenti guidano il lato repo-CV (vedi [CI/CD](#cicd)) - uno per i PDF, uno per tutto il resto. Il campo `bibtex` di ogni pubblicazione in `papers.bib` è il testo della citazione così com'è (scritto a mano finché il paper è solo sottomesso, copiato verbatim dal publisher una volta indicizzato) - il generatore non fa parsing né ricostruzione del BibTeX da campi separati.

## Struttura del Progetto

* `data/`: **il database.** Un file JSON per dominio, numerato secondo l'ordine di rendering (a step di 10, per lasciare spazio a inserimenti futuri):
  * `10-personal.json` - nome, contatti, località, profili social, bio/tagline del sito
  * `20-education.json` - lauree, tesi, voti
  * `30-work.json` - esperienze lavorative
  * `40-research.json` - attività di ricerca (nessun equivalente standard nel PDF/JSON Resume - vedi come viene gestita in `commons/lua_data_loader.tex` e `resume_pydantic_schema.py`)
  * `50-projects.json` - progetti personali/accademici (ognuno richiede un `id` stabile, `category`, e `importance` - vedi [Attività Comuni](#attività-comuni))
  * `60-publications.json` - pubblicazioni (il campo `bibtex` è il testo della citazione così com'è - vedi [Attività Comuni](#attività-comuni))
  * `70-languages.json` - lingue parlate
  * `80-skills.json` - competenze, inclusa la categoria "Soft Skills" (renderizzata come sezione a sé ovunque)
  * `90-meta.json` - testo GDPR/legale (solo-PDF, non arriva mai al sito)
* `cv.tex` / `cover_letter.tex`: i template LaTeX. Richiamano il loader Lua.
* `commons/lua_data_loader.tex`: lo script Lua che legge `data/*.json`, converte l'enfasi Markdown (`**grassetto**`/`*corsivo*`) in LaTeX, e popola le sezioni del documento nella lingua selezionata.
* `scripts-website-data/generate_resume_json.py`: costruisce `resume.json` da `data/`, validato contro `scripts-website-data/resume_pydantic_schema.py` prima di essere scritto.
* `scripts-website-data/generate_socials_yml.py`: costruisce `_data/socials.yml` del sito (email, username LinkedIn/GitHub, link al PDF del CV) da `data/10-personal.json` - solo i campi che sono fatti reali del CV; le impostazioni solo-sito (ID Google Scholar, QR WeChat, ecc.) restano mantenute a mano lato sito.
* `scripts-website-data/generate_papers_bib.py`: costruisce `_bibliography/papers.bib` del sito da `data/60-publications.json`, concatenando il campo `bibtex` di ogni voce così com'è e iniettando `abstract` (dal campo strutturato `abstract`, così non si scrive mai due volte) e `abbr` (da `venueAbbr`, se presente).
* `img/`: asset statici (foto profilo, firma).

## Attività Comuni

Dove intervenire per ogni tipo di modifica - ognuna di queste è semplicemente modificare un file JSON e fare push; PDF e sito si aggiornano da soli.

**Aggiornare bio, contatti, o link social**
Modifica `data/10-personal.json`: `email`, `phone`, `location`, `profiles` (LinkedIn/GitHub/WhatsApp), `summary` (la bio "Professional Summary" del sito), `websiteLabel` (il tagline mostrato sul sito, diverso da `label` che è il titolo del documento PDF).

**Aggiungere un lavoro o tirocinio**
Aggiungi una voce all'array in `data/30-work.json`: `name`, `position`, `location`, `startDate`/`endDate` (`MM/YYYY`), `summary`, `highlights` (lista puntata, Markdown ammesso).

**Aggiungere un'attività di ricerca**
Stessa forma del lavoro, in `data/40-research.json`. Viene renderizzata come sezione "Research" a sé sia nel PDF che sul sito (override di template solo-sito - vedi [Integrazione con il Sito](#integrazione-con-il-sito)).

**Aggiungere una laurea**
Aggiungi una voce a `data/20-education.json`: `institution`, `location`, `area`, `studyType`, `startDate`/`endDate`, `score` (es. `"Final Grade: 110/110 cum laude"` - il prefisso "Final Grade:"/"Voto:" viene tolto automaticamente per il campo `score` dedicato del sito). Aggiungi un oggetto `thesis: { title, supervisors }` se c'è una tesi - diventa automaticamente due righe extra negli highlights ("Thesis: ...", "Supervisors: ...").

**Aggiungere un progetto**
Aggiungi una voce a `data/50-projects.json`:

```json
{
  "id": "uno-slug-stabile",         // assegnato una volta sola, mai più cambiato - anche se "name" cambia dopo
  "importance": 50,                  // ordine di visualizzazione sul sito (step di 10) - indipendente dall'ordine di questo array
  "category": "Academic",
  "name": { "en": "...", "it": "..." },
  "course": { "en": "...", "it": "..." },
  "description": { "en": "...", "it": "..." },
  "highlights": { "en": ["..."], "it": ["..."] },
  "keywords": ["..."]
}
```

Fai il push, e una nuova `_projects/<id>.md` viene creata in automatico sul sito senza altre azioni - vedi [Integrazione con il Sito](#integrazione-con-il-sito) per come funziona il confronto e cosa fare se vuoi poi espandere quella pagina con un approfondimento completo.

**Aggiungere una pubblicazione**
Aggiungi una voce a `data/60-publications.json`: `type`, `status` (`{"en": "submitted", "it": "sottomesso"}` o simile), `venue`, `year`, `date`, `authors` (stringa semplice, es. `"Enea Manzi, Marco Anisetti"`), `title`, `abstract` (alimenta sia il PDF/`resume.json` sia, iniettato automaticamente, il `papers.bib` del sito).

Scrivi anche un campo `bibtex`: il testo letterale della citazione, es.
```json
"bibtex": "@unpublished{manzi2026itadata,\n  author = {Manzi, Enea and Anisetti, Marco},\n  title  = {...},\n  year   = {2026},\n  note   = {Submitted to ITADATA 2026}\n}"
```
Scrivilo a mano finché il paper è solo sottomesso (nessun DOI/pagine/venue ancora); quando verrà effettivamente pubblicato da qualche parte, sostituiscilo con la citazione BibTeX già pronta copiata dal publisher (IEEE/Springer/ACM/...) invece di riscriverla a mano - non ricostruire campi che ti vengono già dati. Aggiungi i campi extra che il sito capisce (`doi`, `pdf`, `video`, `code`, `selected`, `bibtex_show`, ...) direttamente dentro quello stesso testo `bibtex` quando hai davvero un valore reale - vedi l'intestazione di un `papers.bib` generato per l'elenco completo, oppure `CUSTOMIZATIONS.md` nel repo del sito. Facoltativo: aggiungi `"venueAbbr": "QUALCHE-ABBR"` per un badge venue - serve una voce corrispondente in `_data/venues.yml` del sito (mantenuto a mano lì, non generato - vedi [Integrazione con il Sito](#integrazione-con-il-sito)).

**Aggiungere o aggiornare una categoria di competenze / una lingua**
`data/80-skills.json` (le keyword supportano l'enfasi Markdown, spogliata automaticamente per il sito dato che quel template non la renderizza) / `data/70-languages.json`. Il nome categoria `"Soft Skills"` è gestito come caso speciale ovunque (sezione propria, rendering a etichetta-in-grassetto per ogni voce) - non rinominarlo.

**Aggiungere enfasi al testo in uno qualsiasi dei campi sopra**
Usa `**grassetto**` / `*corsivo*` in qualsiasi campo di testo libero - mai LaTeX o HTML grezzo (vedi [Convenzioni sui Dati](#convenzioni-sui-dati)).

**Controllare le modifiche prima di pushare**
Vedi [Esecuzione Locale](#esecuzione-locale) - compila il PDF, e/o esegui in locale gli script `generate_*.py` per vedere esattamente il `resume.json`/`socials.yml`/`papers.bib` che verrebbero pushati (i primi due falliscono rumorosamente, elencando ogni problema, se qualcosa in `data/` è malformato).

## Convenzioni sui Dati

* I **campi bilingue** sono oggetti `{"en": "...", "it": "..."}`; una stringa semplice significa "uguale in entrambe le lingue" (es. il nome di una persona, "APIGuard Assurance").
* L'**enfasi** nel testo libero usa Markdown - `**grassetto**`, `*corsivo*` - mai LaTeX o HTML grezzo. Ogni consumer la converte in ciò che gli serve (LaTeX tramite il loader Lua, HTML tramite `markdownify` di Jekyll, o testo semplice dove un template non la supporta - vedi `strip_md` in `scripts-website-data/generate_resume_json.py`).
* La **numerazione** (`10-`, `20-`, ...) riflette l'ordine di rendering, non l'ordine di creazione. Lo step di 10 lascia spazio per inserire un nuovo dominio in futuro (es. `45-awards.json`) senza rinumerare tutto.

## CI/CD

Due workflow GitHub Actions indipendenti osservano `data/**` - indipendenti apposta, così che un fallimento nell'uno non blocchi mai l'altro:

* **`build-latex.yml`** - compila tutti e 4 i PDF, li pubblica sul branch `pdf-release`, e pusha i due CV (non le lettere di presentazione) su `assets/pdf/` del sito.
* **`generate-website-data.yml`** - esegue `generate_resume_json.py`, `generate_socials_yml.py` e `generate_papers_bib.py`; valida l'output JSON Resume (Pydantic) e lo formatta con Prettier (stesso `.prettierrc` del sito, replicato via `--print-width 150` dato che quel file di config vive nell'altro repo); poi, nello stesso job, fa il checkout del repo del sito, ci copia dentro i tre file generati, esegue *lo script del sito stesso* `scripts/scaffold_project_pages.py` contro quel checkout (così un'eventuale pagina progetto nuova finisce nello stesso commit invece di generare un push separato lato sito), e pusha tutto in un unico commit su `assets/json/`, `_data/` e `_bibliography/`. Su una pull request valida soltanto, non tocca mai il sito.

Entrambi richiedono il secret `API_TOKEN_GITHUB` (un PAT con permessi di scrittura su `eneamanzi.github.io`) per pushare tra repository diversi.

## Integrazione con il Sito

`eneamanzi.github.io` è un repository separato; questo repo si limita a pusharci dei file dentro, non ne contiene la logica. Cose utili da sapere se si sta facendo debug lato sito:

* `_includes/cv/render.liquid`, `skills.liquid`, e `languages.liquid` sono **override locali** dei template del gem `al_folio_cv` (Jekyll permette a un file locale del sito di avere precedenza, tramite il meccanismo `includes_load_paths`). Aggiungono una sezione "Research" (nessun equivalente standard in JSON Resume) e correggono un paio di bug estetici del gem originale (parentesi/icone vuote quando un campo è vuoto). Se il gem si aggiorna a monte, questi file vanno risincronizzati a mano.
* `scripts/scaffold_project_pages.py` (nella cartella `scripts/` propria del repo del sito, non correlata a `scripts-website-data/` di questo repo) viene invocato direttamente da `generate-website-data.yml` di questo repo (vedi [CI/CD](#cicd)), contro il checkout del sito, prima del commit - quindi non ha mai bisogno di un push proprio. Per ogni progetto senza ancora una pagina, ne crea una sotto `_projects/<id>.md`, precompilata con il summary e gli highlights del CV sotto un'intestazione "Summary (from CV)". Il confronto avviene sul campo stabile `cv_id` nel frontmatter, non sul titolo - così rinominare in futuro il nome di un progetto o il titolo di una pagina non genera mai una pagina duplicata. Il workflow proprio del sito `scaffold-projects.yml` (attivato da un push che tocca `resume.json`) esiste ancora come rete di sicurezza inerte - nel caso normale non trova più nulla da fare.
* `_bibliography/papers.bib` è generato (vedi sopra) - non editarlo mai a mano nel repo del sito. `_data/coauthors.yml` e `_data/venues.yml` sono l'opposto: restano **mantenuti a mano nel repo del sito**, perché sono preferenze di rendering (a quale URL linkare il nome di un coautore, che colore per un badge venue), non fatti del CV. Vedi `CUSTOMIZATIONS.md` nel repo del sito (sezione "Publications") per un crash reale della build che questo ha fatto emergere (un esempio BibTeX commentato non è affatto inerte per il parser in uso) e l'elenco completo dei campi extra supportati dal template delle pubblicazioni.

## Esecuzione Locale

### Compilare i PDF

Richiede una distribuzione TeX (TeX Live, MiKTeX o MacTeX) che includa **LuaLaTeX**.

```bash
git clone https://github.com/eneamanzi/curriculum-vitae.git
cd curriculum-vitae
```

Modifica i file JSON sotto `data/` con le tue informazioni (parti da `data/10-personal.json`).

**Inglese (default):**
```bash
latexmk -lualatex -jobname=cv_english cv.tex
latexmk -lualatex -jobname=cover_letter_english cover_letter.tex
```

**Italiano:** la traduzione italiana si attiva iniettando `\def\makeitalian{1}` prima che il file venga letto.
```bash
latexmk -lualatex -jobname=cv_italian -e '$lualatex="lualatex %O \def\makeitalian{1} \input{%S}"' cv.tex
latexmk -lualatex -jobname=cover_letter_italian -e '$lualatex="lualatex %O \def\makeitalian{1} \input{%S}"' cover_letter.tex
```

### Testare i Generatori di Dati per il Sito

Richiede Python 3 e i pacchetti in `scripts-website-data/requirements.txt` (solo `pydantic`):

```bash
pip install -r scripts-website-data/requirements.txt
python3 scripts-website-data/generate_resume_json.py /tmp/resume.json
python3 scripts-website-data/generate_socials_yml.py /tmp/socials.yml
python3 scripts-website-data/generate_papers_bib.py /tmp/papers.bib
```

I primi due terminano con stato diverso da zero ed elencano tutti gli errori di validazione se `data/` produce qualcosa di malformato - non viene mai scritto nulla di parzialmente rotto. `generate_papers_bib.py` non ha uno schema contro cui validare (ogni campo `bibtex` è testo libero) - ispeziona `/tmp/papers.bib` a occhio, oppure passalo per un vero parser BibTeX (es. `bibtexparser` in Python) se vuoi ricontrollarlo.

## Licenza
[MIT](https://choosealicense.com/licenses/mit/)
