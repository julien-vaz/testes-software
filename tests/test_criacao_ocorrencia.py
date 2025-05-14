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
        larkspur = Funcionario("Larkspur")
        with self.assertRaises(ValueError):
            self.projeto.cria_ocorrencia("Straddling Worlds", "Consult at the Athenaeum of Speculation and Scrutiny.", datetime.date.today(), larkspur)

    def test_criacao_ocorrencia_sem_nome(self):
        with self.assertRaises(ValueError):
            self.projeto.cria_ocorrencia("", "[REDACTED]", datetime.date.today(), self.joon)

    def test_criacao_ocorrencia_ids_funcionando(self):
        self.projeto.cria_ocorrencia("God Botherer", "Meet with a god.", datetime.date.today(), self.joon)
        ocorrenciaGod = self.projeto.ocorrencias[-1]
        self.projeto.cria_ocorrencia("Comfort Zone", "Leave the city of Comfort.", datetime.date.today(), self.joon)
        ocorrenciaComfort = self.projeto.ocorrencias[-1]

        self.assertNotEqual(ocorrenciaGod.id, ocorrenciaComfort.id)

    def test_criacao_funcionario_mais_de_10_ocorrencias(self):
        self.projeto.cria_ocorrencia("Seven Bells for Seven Hells", "Acquire Seven Souls. (0/7)", datetime.date.today(), self.joon)
        self.projeto.cria_ocorrencia("Straddling Worlds", "Consult at the Athenaeum of Speculation and Scrutiny.", datetime.date.today(), self.joon)
        self.projeto.cria_ocorrencia("God Botherer", "Meet with a god.", datetime.date.today(), self.joon)
        self.projeto.cria_ocorrencia("Comfort Zone", "Leave the city of Comfort.", datetime.date.today(), self.joon)
        self.projeto.cria_ocorrencia("The Lost King, Found?", "Find Uther Penndraig.", datetime.date.today(), self.joon)

        self.projeto.cria_ocorrencia("Out of the Frying Pan", "Get inside Silmar City.", datetime.date.today(), self.joon)
        self.projeto.cria_ocorrencia("Into the Fryer", "Get the Teleportation Key inside the research facility before Mary's Friends show up.", datetime.date.today(), self.joon)
        self.projeto.cria_ocorrencia("Mothballs", "Get inside Mary's ancestral home and find her inherited riches.", datetime.date.today(), self.joon)
        self.projeto.cria_ocorrencia("Exit Strategy", "You are stranded in the deserte with limited food, no access to magic, and a wounded party member, you need to escape.", datetime.date.today(), self.joon)
        self.projeto.cria_ocorrencia("Your Princess is in Another Castle", "Mary has been kidnapped by the gold mage of Barren Jewel, find her and rescue her.", datetime.date.today(), self.joon)

        with self.assertRaises(ValueError):
            self.projeto.cria_ocorrencia("Boneitis", "You used up the magic in your bones, and it's not going to come back, find a way to replenish it.", datetime.date.today(), self.joon)

    def test_criacao_ocorrencia_fechada(self):
        self.projeto.cria_ocorrencia("Heading Off the Skin Mage", "Defeat Leonold before he kills you.", datetime.date.today(), self.fenn)
        ocorrencia = self.projeto.ocorrencias[-1]
        self.fenn.fecha_ocorrencia(ocorrencia)

        self.assertEqual(False, ocorrencia.status)

    def test_criacao_ocorrencia_fechada_nao_autorizado(self):
        self.projeto.cria_ocorrencia("Summer's End", "Return to the place where Fenn received her scars and bring justice to the elves.", datetime.date.today(), self.fenn)
        ocorrencia = self.projeto.ocorrencias[-1]
        with self.assertRaises(ValueError):
            self.mary.fecha_ocorrencia(ocorrencia)

    def test_modifica_responsavel_por_ocorrencia(self):
        self.projeto.cria_ocorrencia("Unihorn", "Travel to the Aon Adharc Glen and kill a unicorn.", datetime.date.today(), self.fenn)
        ocorrencia = self.projeto.ocorrencias[-1]
        self.projeto.altera_responsavel(ocorrencia, self.mary)

    def test_modifica_responsavel_por_ocorrencia_projeto_invalido(self):
        self.projeto.cria_ocorrencia("They Say You Can't Go Home Again", "Find out about the life your body had before you.", datetime.date.today(), self.fenn)
        newProjeto = Projeto("Book II")
        ocorrencia = self.projeto.ocorrencias[-1]
        with self.assertRaises(ValueError):
            newProjeto.altera_responsavel(ocorrencia, self.joon)

    def test_modifica_responsavel_por_ocorrencia_projeto_invalido(self):
        grak = Funcionario("Grakhuil")
        self.projeto.cria_ocorrencia("All That Glitters", "Return to Darili Irid with Grakhuil once da has gathered enough gold to statisfy da nad self-imposed penance to da nad former clan.", datetime.date.today(), self.mary)
        ocorrencia = self.projeto.ocorrencias[-1]
        with self.assertRaises(ValueError):
            self.projeto.altera_responsavel(ocorrencia, grak)

    def test_modifica_responsavel_por_ocorrencia_projeto_invalido(self):
        doe = Funcionario("Six-Eyed-Doe")
        self.projeto.incluir_funcionarios([doe])
        self.projeto.cria_ocorrencia("Gone to Seed", "There is a place on Aerb considered worse than the first four thousand hells. Defeat Fel Seed.", datetime.date.today(), doe)
        ocorrencia = self.projeto.ocorrencias[-1]
        doe.fecha_ocorrencia(ocorrencia)

        with self.assertRaises(ValueError):
            self.projeto.altera_responsavel(ocorrencia, self.joon)



if __name__ == "__test_criacao_funcionario__":
    unittest.main()
