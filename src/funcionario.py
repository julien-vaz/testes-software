from src.empty_funcionario_name_exception import EmptyFuncionarioNameException
from src.funcionario_nao_autorizado_exception import FuncionarioNaoAutorizadoException
from src.ocorrencia_fechada_exception import OcorrenciaFechadaException
from src.ocorrencia_inexistente_exception import OcorrenciaInexistenteException


class Funcionario:

    def __init__(self, nome):
        if nome == '':
            raise EmptyFuncionarioNameException
        self.nome = nome
        self.ocorrencias = []
        self.ocorrenciasAtivas = 0

    def fecha_ocorrencia(self, ocorrencia):
        if ocorrencia not in self.ocorrencias:
            raise FuncionarioNaoAutorizadoException
        ocorrencia.status = False
        self.ocorrenciasAtivas -= 1

    def altera_prioridade(self, ocorrencia, prioridade):
        if ocorrencia not in self.ocorrencias:
            raise FuncionarioNaoAutorizadoException
        if ocorrencia.status:
            ocorrencia.prioridade = prioridade
        else:
            raise OcorrenciaFechadaException