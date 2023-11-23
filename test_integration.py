#Las pruebas de integracion se hacen todo junto, no como las pruebas
#unitarias aqui mandamos todo en lugar de uno por uno
import unittest
from AnalisisLexico import lexico

class TestIntegracion(unittest.TestCase):

    def test_analizar_texto_con_lexico(self):
        texto = "public int x = 42;"
        resultado = list(lexico(texto))

        # Verificar que el análisis léxico funcione correctamente
        self.assertEqual(resultado, [
            ('PALABRA_RESERVADA', 'public', 1),
            ('SKIP', ' ', 1),
            ('PALABRA_RESERVADA', 'int', 1),
            ('SKIP', ' ', 1),
            ('IDENTIFICADOR', 'x', 1),
            ('SKIP', ' ', 1),
            ('OPERADOR_RELACIONAL', '=', 1),
            ('SKIP', ' ', 1),
            ('CONSTANTE_ENTERA', '42', 1),
            ('CARACTER', ';', 1)
        ])

if __name__ == '__main__':
    unittest.main()