class Projeto:

    def __init__(self, nome):
        if nome == '':
            raise ValueError
        self.nome = nome
        self.funcionarios = []

    def incluir_funcionarios(self, funcionarios):
        self.funcionarios = self.funcionarios + funcionarios

