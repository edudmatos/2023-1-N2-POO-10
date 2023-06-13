class Editora:
    def _init_(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco
        self._livros_publicados = []

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_endereco(self):
        return self._endereco

    def set_endereco(self, endereco):
        self._endereco = endereco

    def adicionar_livro_publicado(self, livro):
        self._livros_publicados.append(livro)

    def remover_livro_publicado(self, livro):
        self._livros_publicados.remove(livro)

    def listar_livros_publicados(self):
        for livro in self._livros_publicados:
            print(livro)
            
    
    
    
    # usando métodos getter e setter para obter e definir os valores dos atributos da classe Editora, 
    # exemplo a seguir:

#    editora = Editora("Nome da Editora", "Endereço da Editora")
#    print(editora.get_nome())  # Obtém o nome da editora
#    editora.set_endereco("Novo Endereço")  # Define um novo endereço para a editora


    # com a classe livro ja feita pode usar 
    # a classe Editora para adicionar, remover e listar os livros publicados pela editora, 
    # exemplo a seguir:
    
#   editora = Editora("Nome da Editora", "Endereço da Editora")

#   livro1 = Livro("Título 1", "Autor 1")
#   livro2 = Livro("Título 2", "Autor 2")

#   editora.adicionar_livro_publicado(livro1)
#   editora.adicionar_livro_publicado(livro2)

#   editora.listar_livros_publicados()

#   editora.remover_livro_publicado(livro1)

#   editora.listar_livros_publicados()