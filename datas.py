class Data:
    def __int__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        return "{}/{}/{}".format(self.dia, self.mes, self.ano)