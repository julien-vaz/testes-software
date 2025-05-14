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
        newOcorrencia = Ocorrencia(nome, id, resumo, data, responsavel, self)
        self.countId += 1
        self.ocorrencias.append(newOcorrencia)
