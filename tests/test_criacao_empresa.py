import unittest
from src.empresa import Empresa
from src.empty_empresa_name_exception import EmptyEmpresaNameException

class TestCriacaoEmpresa(unittest.TestCase):

    def test_criacao_empresa_w(self): # Teste-01
        empresa = Empresa('W')
        assert(empresa.nome == 'W')

    def test_criacao_empresa_vazia(self): # Teste-04
        with self.assertRaises(EmptyEmpresaNameException):
            empresa = Empresa('')

    def test_case_sensitive_criar_empresa(self): # Teste-05
        empresa = Empresa('W')

        value = empresa.getName()

        assert('w' != value)

if __name__ == "__test_criacao_empresa__":
    unittest.main()
