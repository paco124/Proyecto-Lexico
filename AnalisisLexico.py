import re

from Tokens import token_regexp


def lexico(texto):
    linea = 1
    for mo in re.finditer(token_regexp, texto):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 20:
            yield kind, value, linea
        elif kind == 29:
            linea += 1
        else:
            yield kind, value, linea
