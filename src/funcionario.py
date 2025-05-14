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

    def altera_prioridade(self, ocorrencia, prioridade):
        if ocorrencia not in self.ocorrencias:
            raise ValueError
        if ocorrencia.status:
            ocorrencia.prioridade = prioridade
        else:
            raise ValueError