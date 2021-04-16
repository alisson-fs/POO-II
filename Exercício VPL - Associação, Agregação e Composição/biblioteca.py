from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    @property
    def livros(self):
        return self.__livros

    def incluirLivro(self, livro: Livro):
        if isinstance(livro, Livro):
            livro_incluso = False
            for i in self.__livros:
                if i.codigo == livro.codigo:
                    livro_incluso = True
            if not livro_incluso:
                self.__livros.append(livro)
            else:
                print('O livro ja estava incluso.')
        else:
            print('Livro invalido.')

    def excluirLivro(self, livro: Livro):
        if isinstance(livro, Livro):
            livro_incluso = False
            for i in self.__livros:
                if i.codigo == livro.codigo:
                    self.__livros.remove(i)
                    livro_incluso = True
            if not livro_incluso:
                print('O livro nao estava incluso.')
        else:
            print('Livro invalido.')
