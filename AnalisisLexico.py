import re

from Tokens import token_regexp


def lexico(texto):
    print(f'Llamada a lexico con texto: {texto}')
    linea = 1
    for mo in re.finditer(token_regexp, texto):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'COMENTARIO':
            yield kind, value, linea
        elif kind == 'NEWLINE':
            linea += 1
        else:
            yield kind, value, linea
