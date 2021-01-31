import re

def format_tex(n, prec:int=3) -> str:
    """
    Takes a number n and convert it to a string readable by latex with a precision 
    defined by prec. The conversion is in scientific format.
    """
    s = "{:.{prec}e}".format(n, prec=prec)
    s = re.sub(r'([0-9]\.[0-9]+)(e)(\+*)(-*)(0*)([0-9]+)', r'\g<1> \\times 10^{\g<4>\g<6>}', s)
    return s


def write_to_tex(texfile, results):
    """
    The user must define a variable (dictionary) and use the command 
    \pyoutput in the tex file, defined in the preamble like this

        \newcommand{\pyoutput}[2]{#2}

    Each key in the result dictionary must correspond to the first variable of pyoutput.
    Exemple:
        Tex:
            \pyoutput{BoltzmannConstant}{}
        Python
            results.update({"BoltzmannConstant": format_tex(astropy.constant.k_B, 3)})

    running write_to_tex(file) at the end of the python script will write the result in the second argument 
    of pyoutput in the tex file (assuming it is inside a math environment).
    """
    with open(texfile, "r", encoding='utf-8') as file:
        content = file.read()
    for k,v in results.items():
        content = re.sub(r'(pyoutput)(\{%s\})(\{\$*[\\A-Za-z0-9.,\{\}^\s-]+\$*\})' % (k), r'\g<1>\g<2>{%s}' % (v), content) 
    with open(TEXFILE, "w", encoding='utf-8') as file:
        file.write(content)

