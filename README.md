# [IT / EN] Curriculum Vitae - Enea Manzi

This repository contains the source code for my Curriculum Vitae and Cover Letter.
The project is based on the **`moderncv`** LaTeX class, but refactored to be **Data-Driven**: content is separated from presentation.

**Key Features:**
* **Single Source of Truth:** All personal data, experiences, and skills are stored in a single `data.json` file.
* **Lua Powered:** A Lua script reads the JSON and dynamically generates LaTeX commands during compilation.
* **Bilingual:** Generates both Italian and English versions from the same JSON source.
* **Automated:** GitHub Actions automatically compiles PDFs and deploys them to a separate branch (`pdf-release`).
* **Website Integration:** Automatically pushes the generated CVs to my personal website repository (`eneamanzi.github.io`) to keep the online version always up-to-date.

## View the Compiled Documents (PDF)

The PDFs are automatically generated and hosted on the `pdf-release` branch.

| Document | Version | View |
| :--- | :--- | :--- |
| **Curriculum Vitae** | **Italian** | [**cv_italian.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cv_italian.pdf) |
| **Curriculum Vitae** | **English** | [**cv_english.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cv_english.pdf) |
| **Cover Letter** | **Italian** | [**cover_letter_italian.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cover_letter_italian.pdf) |
| **Cover Letter** | **English** | [**cover_letter_english.pdf**](https://github.com/eneamanzi/curriculum-vitae/blob/pdf-release/cover_letter_english.pdf) |

## How it Works

Instead of editing scattered `.tex` files, you simply update **`data.json`**.
The file `commons/lua_data_loader.tex` uses the Lua engine built into **LuaLaTeX** to parse the JSON and populate the CV sections (Education, Work, Skills, etc.) respecting the selected language.

### Project Structure
* `data.json`: **The Database.** Contains all your info (Bio, Work, Edu, Skills, Projects).
* `cv.tex`: The main LaTeX template for the CV. It calls the Lua loader.
* `cover_letter.tex`: The main LaTeX template for the Cover Letter.
* `commons/lua_data_loader.tex`: The logic layer (Lua script) that bridges JSON and LaTeX.
* `img/`: Contains static assets (profile picture, signature).

## Run Locally

To compile this project locally, you need a TeX distribution (TeX Live, MiKTeX, or MacTeX) that includes **LuaLaTeX**.

1.  **Clone the project**
    ```bash
    git clone [https://github.com/eneamanzi/curriculum-vitae.git](https://github.com/eneamanzi/curriculum-vitae.git)
    cd curriculum-vitae
    ```

2.  **Edit your Data**
    Modify `data.json` with your personal information.

3.  **Compile**
    You must use `lualatex`. The easiest way is via `latexmk`.

    **Compile English Version (Default):**
    ```bash
    latexmk -lualatex -jobname=cv_english cv.tex
    latexmk -lualatex -jobname=cover_letter_english cover_letter.tex
    ```

    **Compile Italian Version:**
    To trigger the Italian translation, we inject the command `\def\makeitalian{1}` before inputting the file.
    ```bash
    latexmk -lualatex -jobname=cv_italian -e '$lualatex="lualatex %O \def\makeitalian{1} \input{%S}"' cv.tex
    latexmk -lualatex -jobname=cover_letter_italian -e '$lualatex="lualatex %O \def\makeitalian{1} \input{%S}"' cover_letter.tex
    ```

## License
[MIT](https://choosealicense.com/licenses/mit/)