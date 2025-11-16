# My Personal Curriculum Vitae (progetto LaTeX)

Questo repository contiene la versione principale del mio curriculum vitae (CV) realizzata con LaTeX.

Struttura del progetto
- `cv.tex` — file principale che importa le singole sezioni (`sections/1-personal-data.tex`, `2-education.tex`, ...).
- `sections/` — sezioni del CV (dati personali, istruzione, esperienza, lingue, competenze, ecc.).


## Run Locally
Prerequisiti 
- Python 3
- Distribuzione TeX completa (fornisce il comando `latexmk` per compilazioni automatiche: `latexmk -v`)
  - Windows: MiKTeX o TeX Live
  - Linux: TeX Live

Clone the project

```bash
  git clone https://github.com/eneamanzi/curriculum-vitae.git
```

Go to the project directory

```bash
  cd curriculum-vitae
```
Modificare i file che compongono il CV in `sections/<section_name.tex>` con le proprie informazioni

Compile cv.tex locally

```bash
    python locally-build-cv.py
```

## Documentation

[moderncv – A modern curriculum vitae class](https://ctan.org/pkg/moderncv?lang=en)


## License

[MIT](https://choosealicense.com/licenses/mit/)