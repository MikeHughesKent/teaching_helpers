:: Creates HTML and PDF of worksheets written in latex.

:: HTML without solutions
pandoc relativity_problems_1.tex -f latex -t html -s -o relativity_problems_1.html --mathjax --metadata title="Special Relativity Worksheet Problems 1" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent" 

:: PDF without solutions
pandoc relativity_problems_1.tex -o relativity_problems_1.pdf --pdf-engine=xelatex

:: Make solutions blue
python replace_sol.py relativity_problems_1.tex relativity_problems_1_solutions.tex

:: HTML with solutions
pandoc relativity_problems_1_solutions.tex -f latex -t html -s -o relativity_problems_1_solutions.html --mathjax --metadata title="Special Relativity Worksheet Problems 1 Solutions" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent" 

:: PDF with solutions
pandoc relativity_problems_1_solutions.tex -o relativity_problems_1_solutions.pdf --pdf-engine=xelatex

