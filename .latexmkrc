# Cartella dove vanno i file ausiliari (.aux, .log, .fls, .synctex.gz, ecc.)
$aux_dir = '.temp';

# Il PDF finale resta nella root del progetto (richiesto dalla CI in .github/workflows/build-latex.yml,
# che cerca cv_english.pdf, cv_italian.pdf, cover_letter_english.pdf, cover_letter_italian.pdf in root)
$out_dir = '.';
$pdf_dir = '.';
