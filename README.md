# Expresiones regulares
Validando expresiones regulares en python con:

```Python
import re
p = re.compile("regex")
m = p.match("string")
res = "matched" if m else "failed"
```

Correr las pruebas de test_strings.py
```Shell
python test_strings.py
```

[Docs de  're'](https://docs.python.org/3/library/re.html)
[Repo original](https://bitbucket.org/abdul_itesm/compiladores_ago2021/src/master/tarea1/)
