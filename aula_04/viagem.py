class Viagem:
    def __init__(self, distancia_km, horas, minutos):
        self.__distancia_km = distancia_km 
        self.__horas = horas               
        self.__minutos = minutos           

    def get_distancia(self):
        return self.__distancia_km

    def calcular_velocidade_media(self):
     
        tempo_total_horas = self.__horas + (self.__minutos / 60)
        
        if tempo_total_horas > 0:
            return self.__distancia_km / tempo_total_horas
        return 0

if __name__ == "__main__":
    print("Testando Viagem")

    v1 = Viagem(150, 1, 30)
    
    dist = v1.get_distancia()
    vel = v1.calcular_velocidade_media()
    
    print(f"Distância percorrida: {dist} km")
    print(f"Velocidade Média: {vel:.2f} km/h")