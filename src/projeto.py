from src.ocorrencia import Ocorrencia

class Projeto:

    def __init__(self, nome):
        if nome == '':
            raise ValueError
        self.nome = nome
        self.funcionarios = []
        self.ocorrencias = []
        self.countId = 1

    def incluir_funcionarios(self, funcionarios):
        self.funcionarios = self.funcionarios + funcionarios

    def cria_ocorrencia(self, nome, resumo, data, responsavel):
        if len(responsavel.ocorrencias) >= 10:
            raise ValueError
        newOcorrencia = Ocorrencia(nome, self.countId, resumo, data, responsavel, self)
        responsavel.ocorrencias.append(newOcorrencia)
        self.countId += 1
        self.ocorrencias.append(newOcorrencia)

    def altera_responsavel(self, ocorrencia, funcionario):
        if ocorrencia not in self.ocorrencias:
            raise ValueError
        if funcionario not in self.funcionarios:
            raise ValueError
        ocorrencia.responsavel = funcionario