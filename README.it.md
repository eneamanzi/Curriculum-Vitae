[English version](README.md) | **Versione Italiana**

# [IT / EN] Curriculum Vitae - Enea Manzi

Questo repository contiene il codice sorgente del mio Curriculum Vitae e della mia Lettera di Presentazione.
Il progetto è basato sulla classe LaTeX **`moderncv`**, ma è stato rifattorizzato per essere **Data-Driven**: il contenuto è separato dalla presentazione.

**Caratteristiche Principali:**
* **Single Source of Truth:** Tutti i dati personali, le esperienze e le competenze sono memorizzati in formato JSON, un file per dominio sotto `data/`, con Markdown leggero (`**grassetto**`/`*corsivo*`) per l'enfasi invece di LaTeX grezzo.
* **Lua Powered:** Uno script Lua legge il JSON, converte l'enfasi Markdown in LaTeX e genera dinamicamente i comandi LaTeX durante la compilazione.
* **Bilingue:** Genera sia la versione italiana che quella inglese dalla stessa sorgente JSON.
* **Automatizzato:** GitHub Actions compila automaticamente i PDF e li distribuisce su un branch separato (`pdf-release`).
* **Integrazione con il Sito Web:** Pubblica automaticamente i CV generati, e un `resume.json` (formato JSON Resume, generato dalla stessa sorgente `data/` da `scripts/generate_resume_json.py`), sul repository del mio sito personale (`eneamanzi.github.io`) per mantenere la versione online sempre aggiornata.

## Visualizza i Documenti Compilati (PDF)

I PDF vengono generati automaticamente e sono disponibili sul branch `pdf-release`.

| Documento | Versione | Visualizza |
| :--- | :--- | :--- |
| **Curriculum Vitae** | **Italiano** | [**cv_italian.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cv_italian.pdf) |
| **Curriculum Vitae** | **Inglese** | [**cv_english.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cv_english.pdf) |
| **Lettera di Presentazione** | **Italiana** | [**cover_letter_italian.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cover_letter_italian.pdf) |
| **Lettera di Presentazione** | **Inglese** | [**cover_letter_english.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cover_letter_english.pdf) |

## Come Funziona

Invece di modificare file `.tex` sparsi, è sufficiente aggiornare i file JSON sotto **`data/`**.
Il file `commons/lua_data_loader.tex` utilizza il motore Lua integrato in **LuaLaTeX** per analizzare il JSON e popolare le sezioni del CV (Istruzione, Esperienze, Competenze, ecc.) rispettando la lingua selezionata.

### Struttura del Progetto
* `data/`: **Il Database.** Un file JSON per dominio, numerato secondo l'ordine di rendering (a step di 10, per lasciare spazio a inserimenti futuri): `10-personal.json`, `20-education.json`, `30-work.json`, `40-research.json`, `50-projects.json`, `60-publications.json`, `70-languages.json`, `80-skills.json`, `90-meta.json`.
* `cv.tex`: Il template LaTeX principale per il CV. Richiama il loader Lua.
* `cover_letter.tex`: Il template LaTeX principale per la Lettera di Presentazione.
* `commons/lua_data_loader.tex`: Il livello logico (script Lua) che fa da ponte tra JSON e LaTeX, inclusa la conversione Markdown-to-LaTeX.
* `scripts/generate_resume_json.py`: Converte `data/` in un `resume.json` conforme allo schema JSON Resume per la pagina `/cv/` del sito.
* `img/`: Contiene gli asset statici (foto profilo, firma).

## Esecuzione Locale

Per compilare questo progetto in locale, è necessaria una distribuzione TeX (TeX Live, MiKTeX o MacTeX) che includa **LuaLaTeX**.

1.  **Clona il progetto**
```bash
    git clone [https://github.com/eneamanzi/curriculum-vitae.git](https://github.com/eneamanzi/curriculum-vitae.git)
    cd curriculum-vitae
```

2.  **Modifica i tuoi Dati**
    Modifica i file JSON sotto `data/` con le tue informazioni personali (parti da `data/10-personal.json`). Usa `**grassetto**`/`*corsivo*` per l'enfasi nel testo libero — viene convertito automaticamente in LaTeX (e, per il sito, in HTML).

3.  **Compilazione**
    È necessario utilizzare `lualatex`. Il modo più semplice è tramite `latexmk`.

    **Compilazione Versione Inglese (Default):**
```bash
    latexmk -lualatex -jobname=cv_english cv.tex
    latexmk -lualatex -jobname=cover_letter_english cover_letter.tex
```

    **Compilazione Versione Italiana:**
    Per attivare la traduzione italiana, il comando `\def\makeitalian{1}` viene iniettato prima dell'inclusione del file.
```bash
    latexmk -lualatex -jobname=cv_italian -e '$lualatex="lualatex %O \def\makeitalian{1} \input{%S}"' cv.tex
    latexmk -lualatex -jobname=cover_letter_italian -e '$lualatex="lualatex %O \def\makeitalian{1} \input{%S}"' cover_letter.tex
```

## Licenza
[MIT](https://choosealicense.com/licenses/mit/)