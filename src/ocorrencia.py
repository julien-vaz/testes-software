class Ocorrencia:

    def __init__(self, nome, idd, resumo, data, responsavel, projeto, tipo, prioridade):
        if nome == '':
            raise ValueError
        self.id = idd
        self.nome = nome
        self.resumo = resumo
        self.data = data
        self.status = True
        self.tipo = tipo
        self.prioridade = prioridade
        if responsavel not in projeto.funcionarios:
            raise ValueError
        self.projeto = projeto
        self.responsavel = responsavel



