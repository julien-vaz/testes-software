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

    def test_criacao_ocorrencia_seven_bells(self): # Teste-14
        self.projeto.cria_ocorrencia("Seven Bells for Seven Hells", "Acquire Seven Souls. (0/7)", datetime.date.today(), self.joon, "Gathering")
        newOcorrencia = self.projeto.ocorrencias[-1]
        assert("Seven Bells for Seven Hells" == newOcorrencia.nome)

    def test_criacao_ocorrencia_funcionario_nao_projeto(self): # Teste-15
        larkspur = Funcionario("Larkspur")
        with self.assertRaises(ValueError):
            self.projeto.cria_ocorrencia("Straddling Worlds", "Consult at the Athenaeum of Speculation and Scrutiny.", datetime.date.today(), larkspur, "Knowledge")

    def test_criacao_ocorrencia_sem_nome(self): # Teste-16
        with self.assertRaises(ValueError):
            self.projeto.cria_ocorrencia("", "[REDACTED]", datetime.date.today(), self.joon, "[REDACTED]")

    def test_criacao_ocorrencia_ids_funcionando(self): # Teste-17
        self.projeto.cria_ocorrencia("God Botherer", "Meet with a god.", datetime.date.today(), self.joon, "Knowledge")
        ocorrenciaGod = self.projeto.ocorrencias[-1]
        self.projeto.cria_ocorrencia("Comfort Zone", "Leave the city of Comfort.", datetime.date.today(), self.joon, "Exploration")
        ocorrenciaComfort = self.projeto.ocorrencias[-1]

        self.assertNotEqual(ocorrenciaGod.id, ocorrenciaComfort.id)

    def test_criacao_funcionario_mais_de_10_ocorrencias(self): # Teste-18
        self.projeto.cria_ocorrencia("Seven Bells for Seven Hells", "Acquire Seven Souls. (0/7)", datetime.date.today(), self.joon, "Gathering")
        self.projeto.cria_ocorrencia("Straddling Worlds", "Consult at the Athenaeum of Speculation and Scrutiny.", datetime.date.today(), self.joon, "Knowledge")
        self.projeto.cria_ocorrencia("God Botherer", "Meet with a god.", datetime.date.today(), self.joon, "Knowledge")
        self.projeto.cria_ocorrencia("Comfort Zone", "Leave the city of Comfort.", datetime.date.today(), self.joon, "Exploration")
        self.projeto.cria_ocorrencia("The Lost King, Found?", "Find Uther Penndraig.", datetime.date.today(), self.joon, "Exploration")

        self.projeto.cria_ocorrencia("Out of the Frying Pan", "Get inside Silmar City.", datetime.date.today(), self.joon, "Exploration")
        self.projeto.cria_ocorrencia("Into the Fryer", "Get the Teleportation Key inside the research facility before Mary's Friends show up.", datetime.date.today(), self.joon, "Gathering")
        self.projeto.cria_ocorrencia("Mothballs", "Get inside Mary's ancestral home and find her inherited riches.", datetime.date.today(), self.joon, "Gathering")
        self.projeto.cria_ocorrencia("Exit Strategy", "You are stranded in the deserte with limited food, no access to magic, and a wounded party member, you need to escape.", datetime.date.today(), self.joon, "Exploration")
        self.projeto.cria_ocorrencia("Your Princess is in Another Castle", "Mary has been kidnapped by the gold mage of Barren Jewel, find her and rescue her.", datetime.date.today(), self.joon, "Killing")

        with self.assertRaises(ValueError):
            self.projeto.cria_ocorrencia("Boneitis", "You used up the magic in your bones, and it's not going to come back, find a way to replenish it.", datetime.date.today(), self.joon, "Knowledge")

    def test_criacao_ocorrencia_fechada(self): # Teste-19
        self.projeto.cria_ocorrencia("Heading Off the Skin Mage", "Defeat Leonold before he kills you.", datetime.date.today(), self.fenn, "Killing")
        ocorrencia = self.projeto.ocorrencias[-1]
        self.fenn.fecha_ocorrencia(ocorrencia)

        self.assertEqual(False, ocorrencia.status)

    def test_criacao_ocorrencia_fechada_nao_autorizado(self): # Teste-20
        self.projeto.cria_ocorrencia("Summer's End", "Return to the place where Fenn received her scars and bring justice to the elves.", datetime.date.today(), self.fenn, "Killing")
        ocorrencia = self.projeto.ocorrencias[-1]
        with self.assertRaises(ValueError):
            self.mary.fecha_ocorrencia(ocorrencia)

    def test_modifica_responsavel_por_ocorrencia(self): # Teste-21
        self.projeto.cria_ocorrencia("Unihorn", "Travel to the Aon Adharc Glen and kill a unicorn.", datetime.date.today(), self.fenn, "Killing")
        ocorrencia = self.projeto.ocorrencias[-1]
        self.projeto.altera_responsavel(ocorrencia, self.mary)

    def test_modifica_responsavel_por_ocorrencia_projeto_invalido(self): # Teste-22
        self.projeto.cria_ocorrencia("They Say You Can't Go Home Again", "Find out about the life your body had before you.", datetime.date.today(), self.fenn, "Knowledge")
        newProjeto = Projeto("Book II")
        ocorrencia = self.projeto.ocorrencias[-1]
        with self.assertRaises(ValueError):
            newProjeto.altera_responsavel(ocorrencia, self.joon)

    def test_modifica_responsavel_por_ocorrencia_funcionario_de_fora(self): # Teste-23
        grak = Funcionario("Grakhuil")
        self.projeto.cria_ocorrencia("All That Glitters", "Return to Darili Irid with Grakhuil once da has gathered enough gold to statisfy da nad self-imposed penance to da nad former clan.", datetime.date.today(), self.mary, "Gathering")
        ocorrencia = self.projeto.ocorrencias[-1]
        with self.assertRaises(ValueError):
            self.projeto.altera_responsavel(ocorrencia, grak)

    def test_modifica_responsavel_por_ocorrencia_fechada(self): # Teste-24
        doe = Funcionario("Six-Eyed-Doe")
        self.projeto.incluir_funcionarios([doe])
        self.projeto.cria_ocorrencia("Gone to Seed", "There is a place on Aerb considered worse than the first four thousand hells. Defeat Fel Seed.", datetime.date.today(), doe, "Killing")
        ocorrencia = self.projeto.ocorrencias[-1]
        doe.fecha_ocorrencia(ocorrencia)

        with self.assertRaises(ValueError):
            self.projeto.altera_responsavel(ocorrencia, self.joon)

    def test_ocorrencia_com_tipos(self): # Teste-25
        self.projeto.cria_ocorrencia("The Slayer of Horrors", "Kill all the worst creatures of Aerb. (0/13)", datetime.date.today(), self.joon, "Killing")
        ocorrencia = self.projeto.ocorrencias[-1]

        self.assertEqual("Killing", ocorrencia.tipo)

    def test_ocorrencia_com_tipos_nao_definidos(self): # Teste-26
        with self.assertRaises(ValueError):
            self.projeto.cria_ocorrencia("Through the Lashing Glass", "Find the treasures in the glass palace, inside the Glassy Fields Exclusion Zone.", datetime.date.today(), self.joon, "Gathreirng")

    def test_ocorrencia_com_prioridade(self): # Teste-27
        self.projeto.cria_ocorrencia("A room of One's Own", "inside the Boundless Pit, a mile wide, and infinitely deep, you'll find the Kuum Doona, a secure home awaiting to be lighted up once more.", datetime.date.today(), self.joon, "Gathering", 1)


    def test_ocorrencia_com_prioridade_alterada(self): # Teste-28
        self.projeto.cria_ocorrencia("Murder in Duplicate", "Doris Finch is the only person in the world that has the power to duplicate herself countless times, to close her exclusion zone, you will need to kill each clone. (0/9513912)", datetime.date.today(), self.joon, "Gathering", 1)
        ocorrencia = self.projeto.ocorrencias[-1]
        self.joon.altera_prioridade(ocorrencia, 3)

    def test_ocorrencia_com_prioridade_definida_errada(self): # Teste-29
        solace = Funcionario("Solace")
        self.projeto.incluir_funcionarios([solace])
        with self.assertRaises(ValueError):
            self.projeto.cria_ocorrencia("Taking Root", "The world has but a single druid, tending to but a single locus, find a way to help them so the world druids can stalk the world once more.", datetime.date.today(), solace, "Gathering", 0)

    def test_modifica_prioridade_por_ocorrencia_fechada(self): # Teste-30
        doe = Funcionario("Six-Eyed-Doe")
        self.projeto.incluir_funcionarios([doe])
        self.projeto.cria_ocorrencia("Gone to Seed", "There is a place on Aerb considered worse than the first four thousand hells. Defeat Fel Seed.", datetime.date.today(), doe, "Killing", 1)
        ocorrencia = self.projeto.ocorrencias[-1]
        doe.fecha_ocorrencia(ocorrencia)

        with self.assertRaises(ValueError):
            doe.altera_prioridade(ocorrencia, 3)

    def test_ocorrencia_altera_prioridade_nao_responsavel(self): # Teste-31
        self.projeto.cria_ocorrencia("Crimes Against the Soul", "Journey to the autonomous prison on Sulid Isle and retreve the criminal Fallatehr Whiteshell.", datetime.date.today(), self.mary, "Knowledge", 1)
        ocorrencia = self.projeto.ocorrencias[-1]
        with self.assertRaises(ValueError):
            self.joon.altera_prioridade(ocorrencia, 3)


    # Criar teste pra 10 ocorrencias onde elas não estão ativas.

if __name__ == "__test_criacao_funcionario__":
    unittest.main()
