import unittest
from src.funcionario import Funcionario

class TestCriacaoFuncionario(unittest.TestCase):

    def test_criacao_funcionario_hanako(self):
        hanako = Funcionario('Hanako')
        assert(hanako.nome == 'Hanako')

    def test_criacao_funcionario_vazio(self):
        with self.assertRaises(ValueError):
            funcionario = Funcionario('')

if __name__ == "__test_criacao_funcionario__":
    unittest.main()
