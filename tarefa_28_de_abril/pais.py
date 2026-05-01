class Pais:
    def __init__(self, n, p, a):
        # Atributos encapsulados (privados com __)
        self.__nome = n
        self.__populacao = p
        self.__area = a

    # Métodos de acesso (Getters e Setters)
    def get_nome(self): return self.__nome
    def set_nome(self, valor): self.__nome = valor

    def get_populacao(self): return self.__populacao
    def set_populacao(self, valor):
        if valor >= 0: self.__populacao = valor

    def get_area(self): return self.__area
    def set_area(self, valor):
        if valor > 0: self.__area = valor

    # Cálculo da densidade demográfica (Habitantes / Área)
    def densidade(self):
        return self.__populacao / self.__area

    # Representação em string do objeto
    def __str__(self):
        return f"País: {self.__nome} | População: {self.__populacao} hab | Área: {self.__area} km²"

class PaisUI:
    @staticmethod
    def menu():
        print("\n--- Sistema de Densidade Demográfica ---")
        print("1 – Calcular")
        print("2 – Fim")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return 0

    @staticmethod
    def calculo():
        # Solicita os dados ao utilizador
        nome = input("Introduza o nome do país: ")
        pop = int(input("Introduza a população (nº de habitantes): "))
        area = float(input("Introduza a área (km²): "))

        # Cria o objeto da classe Pais
        p = Pais(nome, pop, area)

        # Mostra os dados armazenados e o cálculo final
        print("\n--- Resultado ---")
        print(p) # Chama o método __str__
        print(f"Densidade Demográfica: {p.densidade():.2f} hab/km²")

    @staticmethod
    def main():
        opcao = 0
        while opcao != 2:
            opcao = PaisUI.menu()
            if opcao == 1:
                PaisUI.calculo()
            elif opcao == 2:
                print("A encerrar o programa...")
            else:
                print("Opção inválida!")

# Inicia a aplicação
if __name__ == "__main__":
    PaisUI.main()