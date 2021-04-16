#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercício reutilizei as classes biblioteca e livro e criei uma classe usuário 
que é utilizada para chamar os metodos da classe biblioteca.'''

class Usuário:
    def __init__(self, usuario: str, senha: str):
        self.__usuario = usuario
        self.__senha = senha
        self.__livro = object
        self.__pagina_atual = 0

    def alterar_senha(self, senha_atual, senha_nova):
        if senha_atual != self.__senha:
            print('Senha atual incorreta.')
        else:
            self.__senha = senha_nova
            print('Senha alterada com sucesso.')
    
    def pegar_livro(self, biblioteca, titulo):
        self.__livro = biblioteca.pegar_livro(titulo)

    def devolver_livro(self, biblioteca, titulo):
        self.__livro = ''
        biblioteca.devolver_livro(titulo)

    def passar_pagina(self):
        self.__pagina_atual += 1
        if self.__pagina_atual == self.__livro.n_paginas:
            print('Você terminou de ler este livro.')


    def voltar_pagina(self):
        if self.__pagina_atual == 0:
            print('Esta é a primeira página, não existem páginas anteriores a esta.')
        else:
            self.__pagina_atual -= 1

    def mostrar_pagina(self):
        print(f'Página atual: {self.__pagina_atual}')

    def livro_atual(self):
        print(f'Livro atual: {self.__livro.titulo}')

class Biblioteca:
    def __init__(self, livros: list):
        self.__livros = livros
        self.__livros_emprestados = []

    def pegar_livro(self, titulo):
        possui_livro = False
        for i in self.__livros:
            if i.titulo == titulo:
                self.__livros.remove(i)
                self.__livros_emprestados.append(i)
                print('Livro emprestado com sucesso!')
                possui_livro = True
                return i
        if possui_livro == False:
            print('Não possuimos este livro no momento.')


    def devolver_livro(self, titulo):
        possui_livro = False
        for i in self.__livros_emprestados:
            if i.titulo == titulo:
                self.__livros.append(i)
                self.__livros_emprestados.remove(i)
                print('Livro devolvido com sucesso!')
                possui_livro = True
        if possui_livro == False:
            print('Este livro não é registrado no sistema.')

    def pesquisar_livro(self, titulo):
        possui_livro = False
        for i in self.__livros:
            if i.titulo == titulo:
                possui_livro =  True
                print(f'Titulo: {i.titulo}')
                print('Autores:', end=' ')
                for j in range(len(i.autores)):
                    if j < len(i.autores) - 1:
                        print(f'{i.autores[j]}', end=', ')
                    else:
                        print(f'{i.autores[j]}.')
                print(f'Ano: {i.ano} \n Editora: {i.editora} \n Edição: {i.edicao} \n Volume: {i.volume}')
        if possui_livro == False:
            print('Não possuimos este livro.')
                

class Livros:
    def __init__(self, titulo: str, autores: list, ano: int, editora: str, edicao: str, volume: int, n_paginas: int):
        self.__titulo = titulo
        self.__autores = autores
        self.__ano = ano
        self.__editora = editora 
        self.__edicao = edicao
        self.__volume = volume
        self.__n_paginas = n_paginas

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autores(self):
        return self.__autores
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def editora(self):
        return self.__editora

    @property
    def edicao(self):
        return self.__edicao

    @property
    def volume(self):
        return self.__volume

    @property
    def n_paginas(self):
        return self.__n_paginas


def main():
    lista_livros = []
    lista_livros.append(Livros('Calculo', ['Descartes', 'Pitagoras', 'Arquimedes',], 2000, 'Matemática é vida', '10', 1, 400))
    lista_livros.append(Livros('Harry Potter e a Pedra Filosofal', ['J. K. Rowling'], 1997, 'Rocco', '1', 1, 200))
    BU = Biblioteca(lista_livros)

    alisson = Usuário('alisson', '321')
    alisson.alterar_senha('321', '123')
    alisson.pegar_livro(BU, 'Calculo')
    BU.pesquisar_livro('Calculo')
    alisson.livro_atual()
    alisson.mostrar_pagina()
    alisson.passar_pagina()
    alisson.mostrar_pagina()
    alisson.voltar_pagina()
    alisson.mostrar_pagina()
    alisson.devolver_livro(BU, 'Calculo')
    BU.pesquisar_livro('Calculo')

main()