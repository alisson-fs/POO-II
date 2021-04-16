from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__tipoChamados = []
        self.__chamados = []

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        count = 0
        for i in self.__chamados:
            if i.tipo.codigo == tipo.codigo:
                count += 1
        return count

    def incluiChamado(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado) -> Chamado:
        if isinstance(cliente, Cliente) and\
            isinstance(tecnico, Tecnico) and\
                isinstance(tipo, TipoChamado):
            chamado_incluso = False
            for i in self.__chamados:
                if data == i.data and\
                    cliente.codigo == i.cliente.codigo and\
                        tecnico.codigo == i.tecnico.codigo and\
                        tipo.codigo == i.tipo.codigo:
                    chamado_incluso = True
            if not chamado_incluso:
                novo = Chamado(
                    data,
                    cliente,
                    tecnico,
                    titulo,
                    descricao,
                    prioridade,
                    tipo)
                self.__chamados.append(novo)
                return novo
            else:
                print('Chamado ja estava incluso.')
        else:
            print('Tipo invalido.')

    def incluiTipoChamado(
            self,
            codigo: int,
            nome: str,
            descricao: str) -> TipoChamado:
        tipo_incluso = False
        for i in self.__tipoChamados:
            if codigo == i.codigo:
                tipo_incluso = True
        if not tipo_incluso:
            novo = TipoChamado(codigo, descricao, nome)
            self.__tipoChamados.append(novo)
            return novo
        else:
            print('Tipo ja estava incluso.')

    @property
    def tipoChamados(self):
        return self.__tipoChamados
