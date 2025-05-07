import unittest
from src.funcionario import Funcionario

class TestCriacaoFuncionario(unittest.TestCase):

    def test_criacao_funcionario_hanako(self): # Teste-02
        hanako = Funcionario('Hanako')
        assert(hanako.nome == 'Hanako')

    def test_criacao_funcionario_vazio(self): # Teste-06
        with self.assertRaises(ValueError):
            funcionario = Funcionario('')

if __name__ == "__test_criacao_funcionario__":
    unittest.main()
