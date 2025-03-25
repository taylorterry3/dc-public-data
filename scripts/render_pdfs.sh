# scratchpad for rendering pdfs

for file in *.md; do
    output_file="${file%.md}.pdf"
    pandoc "$file" \
    -V geometry:margin=1in \
    -V mainfont="Helvetica" \
    -V fontsize=11pt \
    -V colorlinks=true \
    -V linkcolor=blue \
    -V urlcolor=blue \
    -V table-style=1 \
    -V papersize=letter \
    --highlight-style=tango \
    --pdf-engine=xelatex \
    -o "$output_file"
done
