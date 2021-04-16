from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    @property
    def elevador(self):
        return self.__elevador

    def subir(self) -> str:
        return self.__elevador.subir()

    def descer(self) -> str:
        return self.__elevador.descer()

    def entraPessoa(self) -> str:
        return self.__elevador.entraPessoa()

    def saiPessoa(self) -> str:
        return self.__elevador.saiPessoa()

    def inicializarElevador(self,
                            andarAtual: int,
                            totalAndaresPredio: int,
                            capacidade: int,
                            totalPessoas: int):
        if isinstance(andarAtual, int) and\
                isinstance(totalAndaresPredio, int) and\
                isinstance(capacidade, int) and\
                isinstance(totalPessoas, int):
            if andarAtual >= 0 and\
                    totalAndaresPredio >= 0 and\
                    capacidade >= 0 and\
                    totalPessoas >= 0 and\
                    andarAtual < totalAndaresPredio and\
                    totalPessoas <= capacidade:
                self.__elevador = Elevador(capacidade,
                                           totalPessoas,
                                           totalAndaresPredio,
                                           andarAtual)
            else:
                raise ComandoInvalidoException
        else:
            raise ComandoInvalidoException
