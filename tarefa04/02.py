class musica:
    def __init__(self, id, titulo, artista, album):
        self.__id = id
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

    # Getters
    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album

    # Setters
    def set_id(self, id): self.__id = id
    def set_titulo(self, t): self.__titulo = t
    def set_artista(self, a): self.__artista = a
    def set_album(self, al): self.__album = al

    def ToString(self):
        return f"Música ID: {self.__id} | {self.__titulo} - {self.__artista} ({self.__album})"

    def __str__(self):
        return self.ToString()


class playlist:
    def __init__(self, id, nome, descricao):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao

    # Getters
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao

    # Setters
    def set_id(self, id): self.__id = id
    def set_nome(self, n): self.__nome = n
    def set_descricao(self, d): self.__descricao = d

    def ToString(self):
        return f"Playlist ID: {self.__id} | Nome: {self.__nome} | Descrição: {self.__descricao}"
    
    def __str__(self):
        return self.ToString()
    
class playlist_item:
    def __init__(self, id, id_playlist, id_musica, sequencia):
        self.__id = id
        self.__id_playlist = id_playlist
        self.__id_musica = id_musica
        self.__sequencia = sequencia

    # Getters
    def get_id(self): return self.__id
    def get_id_playlist(self): return self.__id_playlist
    def get_id_musica(self): return self.__id_musica
    def get_sequencia(self): return self.__sequencia

    # Setters
    def set_id(self, id): self.__id = id
    def set_id_playlist(self, id_p): self.__id_playlist = id_p
    def set_id_musica(self, id_m): self.__id_musica = id_m
    def set_sequencia(self, s): self.__sequencia = s

    def ToString(self):
        return f"Item ID: {self.__id} | Playlist: {self.__id_playlist} | Música: {self.__id_musica} | Ordem: {self.__sequencia}"

    def __str__(self):
        return self.ToString()
    
class ui:
    def __init__(self):
        self.__musicas = []
        self.__playlists = []
        self.__itens = []

    def menu(self):
        print("\n" + "="*40)
        print("GERENCIADOR DE PLAYLISTS")
        print("="*40)
        print("1-Cadastrar Música     4-Cadastrar Playlist")
        print("2-Listar Músicas       5-Listar Playlists")
        print("-" * 40)
        print("7-Adicionar Música na Playlist (Item)")
        print("8-Listar Itens das Playlists")
        print("0-Sair")
        return input("\nEscolha uma opção: ")

    def cadastrar_musica(self):
        id = int(input("ID da Música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        self.__musicas.append(musica(id, titulo, artista, album))

    def cadastrar_playlist(self):
        id = int(input("ID da Playlist: "))
        nome = input("Nome: ")
        desc = input("Descrição: ")
        self.__playlists.append(playlist(id, nome, desc))

    def adicionar_na_playlist(self):
        id = int(input("ID do Registro: "))
        id_p = int(input("ID da Playlist: "))
        id_m = int(input("ID da Música: "))
        seq = int(input("Sequência (Ex: 1, 2...): "))
        self.__itens.append(playlist_item(id, id_p, id_m, seq))

    def main(self):
        while True:
            op = self.menu()
            if op == "1": self.cadastrar_musica()
            elif op == "2": 
                for m in self.__musicas: print(m)
            elif op == "4": self.cadastrar_playlist()
            elif op == "5":
                for p in self.__playlists: print(p)
            elif op == "7": self.adicionar_na_playlist()
            elif op == "8":
                for i in self.__itens: print(i)
            elif op == "0":
                print("Encerrando...")
                break

if __name__ == "__main__":
    app = ui()
    app.main()