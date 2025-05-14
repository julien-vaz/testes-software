import unittest
from src.ocorrencia import Ocorrencia
from src.empresa import Empresa
from src.funcionario import Funcionario
from src.projeto import Projeto
import datetime

class TestCriacaoOcorrencia(unittest.TestCase):

    def setUp(self):
        self.empresa = Empresa("Council of Arches")
        self.projeto = Projeto("Book I")
        self.joon = Funcionario('Joon')
        self.mary = Funcionario('Mary')
        self.fenn = Funcionario('Fenn')
        self.projeto.incluir_funcionarios([self.joon, self.mary, self.fenn])

    def test_criacao_ocorrencia_seven_bells(self):
        self.projeto.cria_ocorrencia("Seven Bells for Seven Hells", "Acquire Seven Souls. (0/7)", datetime.date.today(), self.joon)
        newOcorrencia = self.projeto.ocorrencias[-1]
        assert("Seven Bells for Seven Hells" == newOcorrencia.nome)

    def test_criacao_ocorrencia_funcionario_nao_projeto(self):
        self.larkspur = Funcionario("Larkspur")
        with self.assertRaises(ValueError):
            self.projeto.cria_ocorrencia("Straddling Worlds", "Consult at the Athenaeum of Speculation and Scrutiny.", datetime.date.today(), self.larkspur)

if __name__ == "__test_criacao_funcionario__":
    unittest.main()
