import unittest
from src.funcionario import Funcionario

class TestCriacaoFuncionario(unittest.TestCase):

    def test_criacao_funcionario_hanako(self):
        funcionario = Funcionario('Hanako')
        assert(funcionario.nome == 'Hanako')

if __name__ == "__test_criacao_funcionario__":
    unittest.main()
