import subprocess
import re
from pathlib import Path
import os
import shutil
import sys
import argparse  # Aggiunto per gli argomenti da riga di comando

# --- Configurazione Globale ---
# Imposta la directory di lavoro a quella dello script
try:
    BASE_DIR = Path(__file__).parent.resolve()
    os.chdir(BASE_DIR)
except NameError:
    BASE_DIR = Path(".").resolve()
    print(f"Warning: __file__ non definito. Uso la directory corrente: {BASE_DIR}")

# Nomi dei file basati su costanti
CV_FILE_BASENAME = "cv"
CV_TEX = Path(f"{CV_FILE_BASENAME}.tex")
CV_PDF = Path(f"{CV_FILE_BASENAME}.pdf")  # PDF generato da latexmk
BACKUP_TEX = Path(f"{CV_FILE_BASENAME}.tex.bak")

# Definizioni per le versioni
PDF_ENGLISH = Path("cv_english.pdf")
LOG_ENGLISH = Path("build_english.log")
PDF_ITALIAN = Path("cv_italian.pdf")
LOG_ITALIAN = Path("build_italian.log")

# La lista TEMP_EXTENSIONS non è più necessaria!
# 'latexmk -c' la sostituisce.

# --- Funzioni di Compilazione e Pulizia ---

def run_latex_compiler(texfile, logfile_path):
    """
    Esegue latexmk per compilare il documento, gestendo automaticamente le passate.
    Salva stdout+stderr in logfile_path.
    """
    # Usiamo latexmk:
    # -pdf:              Genera PDF (usando pdflatex)
    # -interaction=...:  Non fermarsi per errori
    # -file-line-error:  Mostra errori in formato "file:line:error"
    # -outdir=.:         Assicura che output e log finiscano qui
    cmd = [
        "latexmk",
        "-pdf",
        "-interaction=nonstopmode",
        "-file-line-error",
        f"-outdir={BASE_DIR.as_posix()}", # Specifica la directory di output
        str(texfile)
    ]

    with open(logfile_path, "w", encoding="utf-8") as logf:
        print(f"  running latexmk (log: {logfile_path.name})...")
        logf.write(f"=== latexmk cmd: {' '.join(cmd)} ===\n")
        
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                text=True, encoding="utf-8", errors="replace")
        
        # Stream output
        for line in proc.stdout:
            logf.write(line)
            # Stampa solo l'output rilevante per non inondare la console
            if line.startswith("Latexmk") or line.startswith("Running"):
                print("  " + line.rstrip())
        
        proc.wait()
        
        if proc.returncode != 0:
            logf.write(f"\nEXIT CODE: {proc.returncode}\n")
            # Stampa l'ultima parte del log per diagnosi rapida
            with open(logfile_path, "r", encoding="utf-8") as r:
                lines = r.readlines()
                # Cerca l'errore effettivo
                tail = [l for l in lines[-200:] if "!" in l or "Error" in l]
                if not tail: # Se non trova, stampa solo le ultime righe
                    tail = lines[-20:]
                print("\n--- Last part of latexmk log (Errors) ---")
                for l in tail:
                    print("  " + l.rstrip())
                print("--- End log tail ---\n")
            raise subprocess.CalledProcessError(proc.returncode, cmd)

def clean_temp_files():
    """Rimuove i file ausiliari di LaTeX usando 'latexmk -c'."""
    print("\n--- Cleaning temporary LaTeX files ---")
    try:
        # -c: pulisce tutti i file tranne .pdf e .dvi
        subprocess.run(["latexmk", "-c"], capture_output=True, text=True, check=True)
        print("  (cleaned using 'latexmk -c')")
    except Exception as e:
        print(f"  Could not run 'latexmk -c': {e}")
        print("  (Potrebbe essere necessario pulire manualmente)")

def safe_rename(src, dest):
    """Rinomina in modo sicuro src in dest, sovrascondo dest se esiste."""
    dest_path = Path(dest)
    if not src.exists():
        print(f"  *** Warning: Source file {src} not found for renaming. ***")
        return
    if dest_path.exists():
        dest_path.unlink()
    src.rename(dest_path)

# --- Funzioni di Backup e Ripristino ---

def backup_tex():
    """Salva una copia di backup di cv.tex."""
    if not CV_TEX.exists():
        print(f"*** Error: {CV_TEX.name} not found! Cannot proceed. ***")
        sys.exit(1)
        
    print(f"--- Backing up {CV_TEX.name} to {BACKUP_TEX.name} ---")
    shutil.copy2(CV_TEX, BACKUP_TEX)

def restore_tex():
    """Ripristina cv.tex dal backup."""
    if BACKUP_TEX.exists():
        print(f"--- Restoring {CV_TEX.name} from {BACKUP_TEX.name} ---")
        shutil.move(BACKUP_TEX, CV_TEX)
    else:
        print(f"--- Warning: Backup {BACKUP_TEX.name} not found. Cannot restore. ---")

# --- Funzioni di Modifica e Compilazione Versioni ---

def switch_language(target_primary):
    """
    Modifica cv.tex per impostare la lingua principale di babel.
    Idempotente: imposta lo stato desiderato indipendentemente da quello di partenza.
    """
    print(f"\n=== Ensuring Babel order for {target_primary} version ===")
    
    if target_primary == "english":
        replacement = r"\\usepackage[italian,english]{babel}"
        expected = "English-primary"
    elif target_primary == "italian":
        replacement = r"\\usepackage[english,italian]{babel}"
        expected = "Italian-primary"
    else:
        raise ValueError(f"Unknown language target: {target_primary}")

    # Regex che matcha *entrambe* le combinazioni
    pattern_to_find = re.compile(r"\\usepackage\[(italian,english|english,italian)\]\{babel\}")

    try:
        tex = CV_TEX.read_text(encoding="utf-8")
        
        if replacement in tex:
            print(f"  (cv.tex already set to {expected})")
            return

        tex_new, count = pattern_to_find.subn(replacement, tex)
        
        if count > 0:
            CV_TEX.write_text(tex_new, encoding="utf-8")
            print(f"→ Updated babel order to {expected} in {CV_TEX.name}")
        else:
            print(f"  *** Warning: Could not find babel pattern to switch in {CV_TEX.name}! ***")
            
    except Exception as e:
        print(f"  Error switching to {target_primary}: {e}")
        raise

def compile_version(language_name, log_path, output_pdf_path):
    """
    Funzione generalizzata per compilare una versione specifica.
    Gestisce lo switch, la compilazione e la pulizia.
    """
    print(f"--- Starting build for: {language_name} ---")
    
    if language_name == "English":
        switch_language("english")
    elif language_name == "Italian":
        switch_language("italian")
    
    try:
        # 1. Compila
        run_latex_compiler(CV_TEX, log_path)
        # 2. Rinomina il PDF (latexmk produce "cv.pdf")
        safe_rename(CV_PDF, output_pdf_path)
        print(f"→ Created {output_pdf_path.name}")
    except subprocess.CalledProcessError:
        print(f"\n*** Build failed for {language_name}. See {log_path.name} for details. ***")
        raise # Rilancia l'errore per fermare 'all'
    finally:
        # 3. Pulisce i file temporanei dopo ogni tentativo
        clean_temp_files() 


# --- Esecuzione Principale con argparse ---

def main():
    # 1. Definisci gli argomenti che lo script accetta
    parser = argparse.ArgumentParser(
        description="Compilatore CV multi-lingua (Inglese/Italiano).",
        epilog="Esempio: 'python build.py all' (compila entrambi)"
    )
    parser.add_argument(
        "target",
        nargs="?", # '?' = 0 o 1 argomento. 
        default="all", # Se non dai argomenti, esegue 'all'
        choices=["all", "en", "it", "clean"],
        help="Target da compilare: 'en' (inglese), 'it' (italiano), 'all' (entrambi), 'clean' (pulisci i file temporanei)."
    )
    args = parser.parse_args()

    # 2. Esegui le azioni richieste
    
    if args.target == "clean":
        clean_temp_files()
        if BACKUP_TEX.exists():
            BACKUP_TEX.unlink()
            print(f"  removed backup {BACKUP_TEX.name}")
        print("\n=== Clean complete ===")
        sys.exit(0)

    # Per 'en', 'it', o 'all', eseguiamo il processo di build
    try:
        backup_tex()
        
        if args.target == "en":
            compile_version("English", LOG_ENGLISH, PDF_ENGLISH)
        
        elif args.target == "it":
            compile_version("Italian", LOG_ITALIAN, PDF_ITALIAN)
            
        elif args.target == "all":
            print("--- Building ALL versions ---")
            compile_version("English", LOG_ENGLISH, PDF_ENGLISH)
            compile_version("Italian", LOG_ITALIAN, PDF_ITALIAN)
            
        print("\n=== Build successful ===")
        
    except Exception as e:
        print(f"\n*** Build failed: {e} ***")
        # Il ripristino avviene nel blocco 'finally'
        sys.exit(1)
    finally:
        # Ripristina sempre il file .tex originale
        restore_tex()
        print("--- Process complete ---")


if __name__ == "__main__":
    main()