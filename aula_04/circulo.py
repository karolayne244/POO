class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.raio

if __name__ == "__main__":
    print("--- Teste da Classe Círculo ---")
 
    meu_circulo = Circulo(5.0)

    print(f"Raio inicial: {meu_circulo.raio}")
    print(f"Área: {meu_circulo.area():.2f}")
    print(f"Perímetro: {meu_circulo.perimetro():.2f}")
      