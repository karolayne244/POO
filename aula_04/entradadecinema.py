class EntradaCinema:
    def __init__(self, dia, horario):
        self.__dia = dia.lower() 
        self.__horario = horario  

    def calcular_inteira(self):
     
        if self.__dia == "quarta-feira":
            valor_base = 8.0  
        elif self.__dia in ["segunda-feira", "terça-feira", "quinta-feira"]:
            valor_base = 16.0 
        else: 
            valor_base = 20.0 

        if self.__horario >= 17 and self.__dia != "quarta-feira":
            valor_base *= 1.5 
            
        return valor_base

    def calcular_meia(self):
     
        return self.calcular_inteira() / 2

if __name__ == "__main__":
    print("Testando Entrada de Cinema")

    sessao = EntradaCinema("domingo", 20)
    
    print(f"Sessão: {sessao._EntradaCinema__dia} às {sessao._EntradaCinema__horario}h")
    print(f"Valor Inteira: R$ {sessao.calcular_inteira():.2f}")
    print(f"Valor Meia: R$ {sessao.calcular_meia():.2f}")

    quarta = EntradaCinema("quarta-feira", 19)
    print(f"\nSessão: quarta-feira às 19h")
    print(f"Valor Único (Quarta): R$ {quarta.calcular_inteira():.2f}")