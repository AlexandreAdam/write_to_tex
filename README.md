# write_to_tex
A small script to write output of python computations and write them to tex file


## Installation
git clone the repository and install with
```
python setup.py install
```

## Use
Full example
python script:
```
from astropy.constants import k_B
from wtt import format_tex, write_to_tex
results = {"BoltzmannConstant": format_tex(k_B, 3)}
# >>> {"BoltzmannConstant": "1.381 \\times 10^ {-23} J / K"}
write_to_tex(path_to_tex, results)
```
In the tex file, simply define
```latex
        \newcommand{\pyoutput}[2]{#2}
```
in the preambule. Then, use it like so
```latex
$$
	k_B = \pytouput{BoltzmannConstant}{}
$$
```
after running the python script, you should see the content of the 
second braces changed to
```latex
$$
	k_B = \pytouput{BoltzmannConstant}{1.381 \times 10^ {-23} J / K}
$$
```


