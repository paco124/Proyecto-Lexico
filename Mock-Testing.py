#Este no pude hacer que funcionara

import unittest
from unittest.mock import patch
from LectorLexico import analizar_texto

class TestAnalisisLexico(unittest.TestCase):

    #@patch('main_app.lexico')
    def test_analizar_texto_con_mock(self, mock_lexico):
        # Configurar el comportamiento del mock
        mock_lexico.return_value = [('COMENTARIO', '//mock_valor', 1)]

        # Ejecutar la función que utiliza el mock
        analizar_texto("//mock_valor")

        # Verificar que la función haya sido llamada correctamente
        mock_lexico.assert_called_once_with("//mock_valor")

if __name__ == '__main__':
    unittest.main()
