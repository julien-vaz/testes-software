from src.empty_ocorrencia_name_exception import EmptyOcorrenciaNameException
from src.funcionario_nao_autorizado_exception import FuncionarioNaoAutorizadoException



class Ocorrencia:

    def __init__(self, nome, idd, resumo, data, responsavel, projeto, tipo, prioridade):
        if nome == '':
            raise EmptyOcorrenciaNameException
        self.id = idd
        self.nome = nome
        self.resumo = resumo
        self.data = data
        self.status = True
        self.tipo = tipo
        self.prioridade = prioridade
        if responsavel not in projeto.funcionarios:
            raise FuncionarioNaoAutorizadoException
        self.projeto = projeto
        self.responsavel = responsavel



