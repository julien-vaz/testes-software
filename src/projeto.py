from src.empty_projeto_name_exception import EmptyProjetoNameException
from src.limite_ocorrencias_excedido_exception import LimiteOcorrenciasExcedidoException
from src.ocorrencia import Ocorrencia
from src.ocorrencia_fechada_exception import OcorrenciaFechadaException
from src.ocorrencia_inexistente_exception import OcorrenciaInexistenteException
from src.prioridade_invalida_exception import PrioridadeInvalidaException
from src.funcionario_nao_autorizado_exception import FuncionarioNaoAutorizadoException
from src.tipo_invalido_exception import TipoInvalidoException

class Projeto:

    def __init__(self, nome):
        if nome == '':
            raise EmptyProjetoNameException
        self.nome = nome
        self.funcionarios = []
        self.ocorrencias = []
        self.countId = 1

    def incluir_funcionarios(self, funcionarios):
        self.funcionarios = self.funcionarios + funcionarios

    def cria_ocorrencia(self, nome, resumo, data, responsavel, tipo, prioridade = 3):
        if tipo not in ["Tarefa", "Bug", "Melhoria", "Knowledge", "Killing", "Exploration", "Gathering"]:
            raise TipoInvalidoException
        if responsavel.ocorrenciasAtivas >= 10:
            raise LimiteOcorrenciasExcedidoException
        if prioridade not in [1, 2, 3]:
            raise PrioridadeInvalidaException
        newOcorrencia = Ocorrencia(nome, self.countId, resumo, data, responsavel, self, tipo, prioridade)
        responsavel.ocorrencias.append(newOcorrencia)
        responsavel.ocorrenciasAtivas += 1
        self.countId += 1
        self.ocorrencias.append(newOcorrencia)

    def altera_responsavel(self, ocorrencia, funcionario):
        if ocorrencia not in self.ocorrencias:
            raise OcorrenciaInexistenteException
        if funcionario not in self.funcionarios:
            raise FuncionarioNaoAutorizadoException
        if ocorrencia.status:
            ocorrencia.responsavel = funcionario
        else:
            raise OcorrenciaFechadaException