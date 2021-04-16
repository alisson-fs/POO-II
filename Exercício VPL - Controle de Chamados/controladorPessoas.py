from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return self.__clientes

    @property
    def tecnicos(self):
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        cliente_incluso = False
        for i in self.__clientes:
            if i.codigo == codigo:
                cliente_incluso = True
        if not cliente_incluso:
            novo = Cliente(nome, codigo)
            self.__clientes.append(novo)
            return novo
        else:
            print('Cliente ja estava incluso.')

    def incluiTecnico(self, codigo: int, nome:str) -> Tecnico:
        tecnico_incluso = False
        for i in self.__tecnicos:
            if i.codigo == codigo:
                tecnico_incluso = True
        if not tecnico_incluso:
            novo = Tecnico(nome, codigo)
            self.__tecnicos.append(novo)
            return novo
        else:
            print('Tecnico ja estava incluso.')
