from src.duplicate_funcionario_exception import DuplicateFuncionarioException
from src.duplicate_projeto_exception import DuplicateProjetoException

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
        if proj in self.projetos:
            raise DuplicateProjetoException
        self.projetos.append(proj)

    def getName(self):
        return self.nome

    def getFuncionario(self, name):
        for func in self.funcionarios:
            if func.nome == name:
                return func

    def getProjeto(self, name):
        for proj in self.projetos:
            if proj.nome == name:
                return proj

        return "No Projeto with that Name"