# Teaching Helpers
Utilities to help with teaching preparation for physics at University of Kent.

## make_scorm.py
Command line tool for creating a SCORM package from html files. If uploaded to Moodle, these files will then be accessible from within
a single SCORM item. Packages all html files in current folder and all files in `<images path>`.

Usage: 
```
python make_scorm.py title images_path
```
Example:
```
python make_scorm.py "Lecture Notes" "images"
```

## replace_sol.py
Runs through a latex file and removes the `\sol{` tag and replaces it with `\textcolor{blue}{`.

Used because pandoc cannot handle the macro used in latex to do this. 

If pandoc is run on the latex without running this script then everything 
inside the \sol{} tag is ignoed. So run pandoc on original file to produce
question sheet and run pandoc on output of this script to produce version
with solutions.

Usage: 
```
python replace_sol.py input_file output_file
```
Example:
```
python replace_sol.py input.tex output.tex
```

## compile_notes.bat and compile_worksheet.bat
Example windows batch files with workflow for using pandoc to build HTML and SCORM pacackages from latex notes,
and html and PDF from latex worksheets (with and without solutions, assuming solutions are unside `\sol{` tag.
