#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercício criei uma classe Biblioteca que recebe os livros que vão estar disponiveis 
e criei a classe livro, que recebe todas as cadacteristicas de cada livro.'''

class Biblioteca:
    def __init__(self, livros: list):
        self.__livros = livros
        self.__livros_emprestados = []

    def pegar_livro(self, titulo):
        for i in self.__livros:
            if i.titulo == titulo:
                self.__livros.remove(i)
                self.__livros_emprestados.append(i)
                print('Livro emprestado com sucesso!')


    def devolver_livro(self, titulo):
        for i in self.__livros_emprestados:
            if i.titulo == titulo:
                self.__livros.append(i)
                self.__livros_emprestados.remove(i)
                print('Livro devolvido com sucesso!')

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
    def __init__(self, titulo: str, autores: list, ano: int, editora: str, edicao: str, volume: int):
        self.__titulo = titulo
        self.__autores = autores
        self.__ano = ano
        self.__editora = editora 
        self.__edicao = edicao
        self.__volume = volume

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


def main():
    lista_livros = []
    lista_livros.append(Livros('Calculo', ['Descartes', 'Pitagoras', 'Arquimedes',], 2000, 'Matemática é vida', '10', 1))
    lista_livros.append(Livros('Harry Potter e a Pedra Filosofal', ['J. K. Rowling'], 1997, 'Rocco', '1', 1))
    BU = Biblioteca(lista_livros)

    BU.pegar_livro('Calculo')
    BU.pesquisar_livro('Calculo')
    BU.devolver_livro('Calculo')
    BU.pesquisar_livro('Calculo')
    BU.pesquisar_livro('Harry Potter e a Pedra Filosofal')

main()