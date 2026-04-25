class Viagem:
    def __init__(self, distancia_km, horas, minutos):
        self.distancia_km = distancia_km
        self.horas = horas
        self.minutos = minutos
        
    def calcular_velocidade_media(self):
        tempo_total_horas = self.horas + self.minutos / 60
        if tempo_total_horas > 0:
            velocidade_media = self.distancia_km / tempo_total_horas
            return velocidade_media
        else:
            return 0