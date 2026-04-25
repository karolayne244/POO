class EntradaCinema:
    def __init__(self, dia, horario, valor, idade):
        self.dia = dia
        self.horario = horario
        self.valor = valor
        self.idade = idade

    def calcular_desconto(self):
        desconto = 0

        if self.dia() == "quarta-feira":
            desconto += 0.5  
            #50% de desconto às quartas-feiras

        if self.horario >= 14 and self.horario < 18:
            desconto += 0.2  
            #20% de desconto para sessões entre 14h e 18h

        if self.idade < 12:
            desconto += 0.3  
            #30% de desconto para crianças menores de 12 anos

        elif self.idade >= 60:
            desconto += 0.4  
            #40% de desconto para idosos com 60 anos ou mais

        return min(desconto, 1) * self.valor  
        #O desconto máximo é o valor total da entrada