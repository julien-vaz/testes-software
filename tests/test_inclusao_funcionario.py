from src.funcionario import Funcionario
from src.empresa import Empresa
import unittest


class TestInclusaoFuncionario(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa("W")

    def test_inclusao_funcionario_hanako(self):
        hanako = Funcionario('Hanako')
        self.empresa.incluir_funcionario(hanako)
        assert(len(self.empresa.funcionarios) == 1)

if __name__ == "__name__":
    unittest.main()
