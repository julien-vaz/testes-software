class Ocorrencia:

    def __init__(self, nome, idd, resumo, data, responsavel, projeto):
        if nome == '':
            raise ValueError
        self.id = idd
        self.nome = nome
        self.resumo = resumo
        self.data = data
        if responsavel not in projeto.funcionarios:
            raise ValueError
        self.projeto = projeto
        self.responsavel = responsavel


