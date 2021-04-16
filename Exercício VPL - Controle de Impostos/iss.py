from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class ISS(Imposto):
    def __init__(self,
                 aliquota: float,
                 incidencia_imposto: IncidenciaImposto):
        super().__init__(aliquota, incidencia_imposto)
        self.__servicos = []

    def inclui_servico(self, nome: str):
        if isinstance(nome, str):
            self.__servicos.append(nome)

    def exclui_servico(self, nome: str):
        if isinstance(nome, str) and nome in self.__servicos:
            self.__servicos.remove(nome)

    def calcula_aliquota(self):
        aliquota = self.aliquota - (len(self.__servicos) * 0.1)
        return aliquota / 100
