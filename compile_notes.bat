:: Make HTML

pandoc ch1.tex -f latex -t html -s -o ch1.html --mathjax --metadata title="Section 1 - Galilean Relativity and the Ether" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent"

pandoc ch2.tex -f latex -t html -s -o ch2.html --mathjax --metadata title="Section 2 - The Lorentz Transformations" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent"

pandoc ch3.tex -f latex -t html -s -o ch3.html --mathjax --metadata title="Section 3 - Time Dilation and Length Contraction" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent"

pandoc ch4.tex -f latex -t html -s -o ch4.html --mathjax --metadata title="Section 4 - Spacetime and the Relativity of Simultaneity" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent"

pandoc ch5.tex -f latex -t html -s -o ch5.html --mathjax --metadata title="Section 5 - Relativistic Doppler Effect" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent"

pandoc ch6.tex -f latex -t html -s -o ch6.html --mathjax --metadata title="Section 6 - Relativistic Velocity" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent"

pandoc ch7.tex -f latex -t html -s -o ch7.html --mathjax --metadata title="Section 7 - Relativistic Momentum" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent"

pandoc ch8.tex -f latex -t html -s -o ch8.html --mathjax --metadata title="Section 8 - Relativistic Energy" --metadata author="Mike Hughes" --metadata date="Physics and Astronomy, University of Kent"


:: Make SCORM Package
python make_scorm.py "Lecture Notes" "pictures"

