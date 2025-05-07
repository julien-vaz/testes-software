from src.funcionario import Funcionario
from src.empresa import Empresa
from src.projeto import Projeto
import unittest


class TestInclusaoProjeto(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa("W")

    def test_inclusao_projeto_backrooms(self):
        backrooms = Projeto('Backrooms')
        self.empresa.incluir_projeto(backrooms)
        assert(len(self.empresa.projetos) == 1)

    def test_inclusao_projeto_duplicado(self):
        backrooms = Projeto('Backrooms')
        self.empresa.incluir_projeto(backrooms)
        with self.assertRaises(DuplicateProjetoExpection):
            self.empresa.incluir_projeto(backrooms)



if __name__ == "__name__":
    unittest.main()
