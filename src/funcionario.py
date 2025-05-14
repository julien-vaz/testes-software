class Funcionario:

    def __init__(self, nome):
        if nome == '':
            raise ValueError
        self.nome = nome
        self.ocorrencias = []

    def fecha_ocorrencia(self, ocorrencia):
        if ocorrencia not in self.ocorrencias:
            raise ValueError
        ocorrencia.status = False