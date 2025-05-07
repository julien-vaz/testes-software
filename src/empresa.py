class Empresa:

    def __init__(self, nome):
        if nome == '':
            raise ValueError
        self.nome = nome
        self.funcionarios = []

    def incluir_funcionario(self, func):
        self.funcionarios.append(func)

