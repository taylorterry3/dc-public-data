#!/bin/bash

# Create reports directory if it doesn't exist
mkdir -p reports

# Change to reports directory
cd reports

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
    -V header-includes="\usepackage{ragged2e} \raggedright \usepackage{ulem} \usepackage{graphicx} \usepackage{float} \let\underline\uline \AtBeginDocument{\floatplacement{figure}{H}} \usepackage{placeins} \usepackage{etoolbox} \AtBeginEnvironment{figure}{\FloatBarrier} \AtEndEnvironment{figure}{\FloatBarrier} \usepackage{array} \usepackage{booktabs} \renewcommand{\arraystretch}{1.2} \setlength{\arrayrulewidth}{0.5pt} \renewcommand{\arraystretch}{1.2} \setlength{\tabcolsep}{10pt} \usepackage{colortbl} \renewcommand{\toprule}{\hline\hline} \renewcommand{\bottomrule}{\hline\hline} \renewcommand{\midrule}{\hline} \renewcommand{\arrayrulewidth}{0.8pt}" \
    --from markdown+raw_tex \
    --embed-resources \
    --standalone \
    --shift-heading-level-by=0 \
    -o "$output_file"
done

# Return to original directory
cd ..
