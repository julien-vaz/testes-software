from src.duplicate_funcionario_exception import DuplicateFuncionarioException

class Empresa:

    def __init__(self, nome):
        if nome == '':
            raise ValueError
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def incluir_funcionario(self, func):
        if func in self.funcionarios:
            raise DuplicateFuncionarioException
        self.funcionarios.append(func)

    def incluir_projeto(self, proj):
        self.projetos.append(proj)

    def getName(self):
        return self.nome