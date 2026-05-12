class time:
    def __init__ (self, id, nome, estado):
        self.__id = id
        self.__nome = nome
        self.__estado = estado

# Métodos Get (Recuperar)
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_estado(self): return self.__estado

# Métodos Set (Alterar)
    def set_nome(self, nome): self.__nome = nome
    def set_estado(self, estado): self.__estado = estado
    def set_id(self, id): self.__id = id

# Método ToString
    def ToString(self): return (f"ID: {self.get_id()} - Nome: {self.get_nome()} - Estado: {self.get_estado()}")
    def __str__(self): return self.ToString()

class jogador:
    def __init__(self, i, it, n, v):
        self.__id = i
        self.__id_time = it
        self.__nome = n
        self.__camisa = v

# Métodos Get
    def get_id(self): return self.__id
    def get_id_time(self): return self.__id_time
    def get_nome(self): return self.__nome
    def get_camisa(self): return self.__camisa

# Métodos Set
    def set_id(self, id): self.__id = id
    def set_id_time(self, id_time): self.__id_time = id_time
    def set_nome(self, nome): self.__nome = nome
    def set_camisa(self, camisa): self.__camisa = camisa

# Método ToString
    def ToString(self): return (f"ID: {self.get_id()} - ID Time: {self.get_id_time()} - Nome: {self.get_nome()} - Camisa: {self.get_camisa()}")
    def __str__(self): return self.ToString()

class ui:
    def __init__(self):
        self.__times = []
        self.__jogadores = []

    def menu(self):
        print("\n" + "="*40)
        print("SISTEMA DE GESTÃO")
        print("="*40)
        print("1-Inserir Time      5-Inserir Jogador")
        print("2-Listar Times      6-Listar Jogadores")
        print("3-Atualizar Time    7-Atualizar Jogador")
        print("4-Excluir Time      8-Excluir Jogador")
        print("-" * 40)
        print("9-Jogadores de um Time  10-Transferir Jogador")
        print("0-Sair")
        print("="*40)
        return input("Opção:")
    
# Métodos de suporte para encontrar objetos nas listas
    def buscar_time(self, id):
        for t in self.__times:
            if t.get_id() == id: return t
        return None
    
    def buscar_jogador(self, id):
        for j in self.__jogadores:
            if j.get_id() == id: return j
        return None
    
# Implementação das operações
    def inserir_time(self):
        id = int(input("ID: "))
        nome = input("Nome: ")
        estado = input("Estado: ")
        self.__times.append(time(id, nome, estado))

    def listar_times(self):
        for t in self.__times: print(t)

    def inserir_jogador(self):
        id = int(input("ID: "))
        id_time = int(input("ID do Time: "))
        nome = input("Nome: ")
        camisa = int(input("Camisa: "))
        self.__jogadores.append(jogador(id, id_time, nome, camisa))

    def listar_jogadores(self):
        for j in self.__jogadores: print(j)

    def listar_jogadores_do_time(self):
        id_t = int(input("ID do Time para listar jogadores: "))
        for j in self.__jogadores:
            if j.get_id_time() == id_t: print(j)

    def transferir_jogador(self):
        id_j = int(input("ID do Jogador: "))
        novo_id_t = int(input("Novo ID do Time: "))
        jog = self.buscar_jogador(id_j)
        if jog:
            jog.set_id_time(novo_id_t)
            print("Transferência concluída!")
        else:
            print("Jogador não encontrado.")

    def main(self):
        while True:
            op = self.menu()
            if op == "0": break
            elif op == "1": self.inserir_time()
            elif op == "2": self.listar_times()
            elif op == "5": self.inserir_jogador()
            elif op == "6": self.listar_jogadores()
            elif op == "9": self.listar_jogadores_do_time()
            elif op == "10": self.transferir_jogador()

# Para iniciar a aplicação
if __name__ == "__main__":
    ui = ui()
    ui.main()