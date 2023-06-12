class Emprestimo:
    def _init_(self, livro, usuario, data_emprestimo, data_devolucao):
        self._livro = livro
        self._usuario = usuario
        self._data_emprestimo = data_emprestimo
        self._data_devolucao = data_devolucao

    def get_livro(self):
        return self._livro

    def set_livro(self, livro):
        self._livro = livro

    def get_usuario(self):
        return self._usuario

    def set_usuario(self, usuario):
        self._usuario = usuario

    def get_data_emprestimo(self):
        return self._data_emprestimo

    def set_data_emprestimo(self, data_emprestimo):
        self._data_emprestimo = data_emprestimo

    def get_data_devolucao(self):
        return self._data_devolucao

    def set_data_devolucao(self, data_devolucao):
        self._data_devolucao = data_devolucao
       
       
#     podemos obter e definir os valores dos atributos da classe Emprestimo utilizando os seguintes metodos:
#     emprestimo = Emprestimo(livro, usuario, data_emprestimo, data_devolucao)
#     print(emprestimo.get_livro())  # Obtém o livro do empréstimo
#     emprestimo.set_data_devolucao(nova_data_devolucao)  # Define uma nova data de devolução