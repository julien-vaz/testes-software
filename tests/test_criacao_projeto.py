import unittest
from src.empty_projeto_name_exception import EmptyProjetoNameException
from src.projeto import Projeto


class TestCriacaoProjeto(unittest.TestCase):

    def test_criacao_projeto_human_instrumentalization(self): # Teste-08
        HI = Projeto('Human Instrumentalization')
        assert(HI.nome == 'Human Instrumentalization')

    def test_criacao_projeto_vazio(self): # Teste-09
        with self.assertRaises(EmptyProjetoNameException):
            HI = Projeto('')

if __name__ == "__test_criacao_projeto__":
    unittest.main()
