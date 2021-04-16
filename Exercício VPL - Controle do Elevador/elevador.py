from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self,
                 capacidade: int,
                 totalPessoas: int,
                 totalAndaresPredio: int,
                 andarAtual: int):
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas
        self.__totalAndaresPredio = totalAndaresPredio
        self.__andarAtual = andarAtual

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def totalPessoas(self) -> int:
        return self.__totalPessoas

    @property
    def totalAndaresPredio(self) -> int:
        return self.__totalAndaresPredio

    @property
    def andarAtual(self) -> int:
        return self.__andarAtual

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
        self.__totalAndaresPredio = totalAndaresPredio

    def entraPessoa(self) -> str:
        if self.__totalPessoas == self.__capacidade:
            raise ElevadorCheioException
        else:
            self.__totalPessoas += 1
            return 'Entrou uma pessoa!'

    def saiPessoa(self) -> str:
        if self.__totalPessoas == 0:
            raise ElevadorJahVazioException
        else:
            self.__totalPessoas -= 1
            return 'Saiu uma pessoa!'

    def subir(self) -> str:
        if self.__andarAtual == self.__totalAndaresPredio - 1:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.__andarAtual += 1
            return 'Elevador subiu!'

    def descer(self) -> str:
        if self.__andarAtual == 0:
            raise ElevadorJahNoTerreoException
        else:
            self.__andarAtual -= 1
            return 'Elevador desceu!'
