class Ocorrencia:

    def __init__(self, nome, id, resumo, data, responsavel, projeto):
        self.id = id
        self.nome = nome
        self.resumo = resumo
        self.data = data
        if responsavel not in projeto.funcionarios:
            raise ValueError
        self.projeto = projeto
        self.responsavel = responsavel


