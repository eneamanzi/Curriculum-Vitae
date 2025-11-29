# [IT / EN] Curriculum Vitae written in LaTeX - Enea Manzi

This repository contains the source code for my Curriculum Vitae, managed and versioned using LaTeX and Git.


## View the Compiled Curriculum Vitae (PDF)

The CV is available in two languages. The PDF files are automatically generated and updated by GitHub Actions upon every change to the source code.

| Version | View |
| :--- | :--- |
| **Italian** | [**cv_italian.pdf**](cv_italian.pdf) |
| **English** | [**cv_english.pdf**](cv_english.pdf) |


## Structure and Automation

* **Technology:** The CV is based on the `moderncv` LaTeX class.
* **Bilingualism:** The bilingual management (Italian and English) is implemented using the `babel` package and the `\en{...}` / `\it{...}` macros.
* **Automatic Compilation:** The GitHub Actions workflow (`.github/workflows/build-latex.yml`) automatically compiles both CV versions and updates the PDF files in this repository on every push.

## Run Locally (Manual Compilation)
To clone the project and compile it locally, a complete TeX distribution is required (e.g., TeX Live or MiKTeX).

Clone the project
```bash
  git clone https://github.com/eneamanzi/curriculum-vitae.git
```

Go to the project directory
```bash
  cd curriculum-vitae
```

>Modify the CV source files in `sections/<section_name.tex>` with your own information

Compile the Italian version:
```bash
latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdflatex -jobname=cv_italian -e "\$pdflatex='pdflatex %O \def\makeitalian{1} \input{%S}'" cv.tex
```

Compile the English version:
```bash
latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdflatex -jobname=cv_english cv.tex
```

## Documentation
[moderncv – A modern curriculum vitae class](https://ctan.org/pkg/moderncv?lang=en)


## License
[MIT](https://choosealicense.com/licenses/mit/)