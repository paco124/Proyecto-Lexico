#Las pruebas unitarias las tienes que estar haceindo una por una
import unittest
from AnalisisLexico import lexico

class TestAnalisisLexico(unittest.TestCase):

    def setUp(self):
        # Configurar el entorno de prueba si es necesario
        pass

    def tearDown(self):
        # Limpiar el entorno de prueba después de la ejecución de las pruebas
        pass

    def test_lexico_palabra_reservada(self):
        texto = "public"
        resultado = list(lexico(texto))
        #public es una palabra reservada, regresa la palabra public y la linea donde se encuentra, es decir 1
        self.assertEqual(resultado, [('PALABRA_RESERVADA', 'public', 1)])

    def test_lexico_operador_aritmetico(self):
        texto = "+"
        resultado = list(lexico(texto))
        self.assertEqual(resultado, [('OPERADOR_ARITMETICO', '+', 1)])

    def test_lexico_comentario(self):
        texto = "// Este es un comentario"
        resultado = list(lexico(texto))
        self.assertEqual(resultado, [('COMENTARIO', '// Este es un comentario', 1)])

    # Agrega más casos de prueba según sea necesario

if __name__ == '__main__':
    unittest.main()
