class Viagem:
    def __init__(self, destino, distancia, litros):
        # Atributos encapsulados (privados com __)
        self.__destino = destino
        self.__distancia = distancia
        self.__litros = litros

    # Métodos de acesso (Getters e Setters)
    def get_destino(self): return self.__destino
    def set_destino(self, valor): self.__destino = valor

    def get_distancia(self): return self.__distancia
    def set_distancia(self, valor):
        if valor > 0: self.__distancia = valor

    def get_litros(self): return self.__litros
    def set_litros(self, valor):
        if valor > 0: self.__litros = valor

    # Cálculo do consumo médio
    def consumo(self):
        return self.__distancia / self.__litros

    # Representação em string do objeto
    def __str__(self):
        return f"Viagem para {self.__destino} ({self.__distancia}km com {self.__litros}L)"

class ViagemUI:
    @staticmethod
    def menu():
        print("\n1 - Calcular\n2 - Fim")
        return int(input("Escolha uma opção: "))

    @staticmethod
    def calculo():
        # Solicita os dados ao usuário
        dest = input("Destino: ")
        dist = float(input("Distância (km): "))
        litros = float(input("Combustível gasto (litros): "))

        # Cria o objeto da classe Viagem
        v = Viagem(dest, dist, litros)

        # Mostra os dados e o resultado
        print(f"\nDados da Viagem: {v}")
        print(f"Consumo médio: {v.consumo():.2 f} km/l")

    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1:
                ViagemUI.calculo()
        print("Programa encerrado.")

# Inicia o programa
if __name__ == "__main__":
    ViagemUI.main()