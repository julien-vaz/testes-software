from src.funcionario import Funcionario
from src.empresa import Empresa
from src.projeto import Projeto
from src.duplicate_projeto_exception import DuplicateProjetoException
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
        with self.assertRaises(DuplicateProjetoException):
            self.empresa.incluir_projeto(backrooms)

    def delegate_criacao_funcionario_e_projeto(self):
        fenn = Funcionario("Fenn")
        outer = Projeto('Outer Reaches')
        self.empresa.incluir_funcionario(fenn)
        self.empresa.incluir_projeto(outer)

    def test_incluir_funcionario_projeto(self):
        self.delegate_criacao_funcionario_e_projeto()

        outer = self.empresa.getProjeto('Outer Reaches')
        fenn = self.empresa.getFuncionario('Fenn')

        outer.incluir_funcionarios([fenn])

        assert(len(outer.funcionarios) == 1)




if __name__ == "__name__":
    unittest.main()
