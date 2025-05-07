import unittest
from src.empresa import Empresa

class TestCriacaoEmpresa(unittest.TestCase):

    def test_criacao_empresa_w(self):
        empresa = Empresa('W')
        assert(empresa.nome == 'W')

if __name__ == "__test_criacao_empresa__":
    unittest.main()
