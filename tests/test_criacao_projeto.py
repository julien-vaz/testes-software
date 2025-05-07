import unittest
from src.funcionario import Funcionario
from src.empresa import Empresa
from src.projeto import Projeto


class TestCriacaoProjeto(unittest.TestCase):

    def test_criacao_projeto_human_instrumentalization(self):
        HI = Projeto('Human Instrumentalization')
        assert(HI.nome == 'Human Instrumentalization')


if __name__ == "__test_criacao_projeto__":
    unittest.main()
