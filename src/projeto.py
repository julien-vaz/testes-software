class Projeto:

    def __init__(self, nome):
        if nome == '':
            raise ValueError
        self.nome = nome
