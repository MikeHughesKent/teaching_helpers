"""
Runs through a latex file and removes the \sol{ tag  and replaces
it with \textcolor{blue}{.
                         
Used because pandoc cannot handle the macro used in latex to do this. 

If pandoc is run on the latex without running this script then everything 
inside the \sol{} tag is ignoed. So run pandoc on original file to produce
question sheet and run pandoc on output of this script to produce version
with solutions.

Usage: python replace_sol.py <input file> <output file>

e.g. python replace_sol.py input.tex output.tex

"""

import sys

def replace_sol(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace \sol{ with {
    content = content.replace(r'\sol{', r'\textcolor{blue}{')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python replace_sol.py <input file> <output file>, e.g. python replace_sol.py input.tex output.tex")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    replace_sol(input_path, output_path)
    print(f"Replaced '\\sol{{' with '{{' in {input_path} and saved to {output_path}")
