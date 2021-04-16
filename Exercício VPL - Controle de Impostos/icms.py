from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class ICMS(Imposto):
    def __init__(self,
                 aliquota: float,
                 incidencia_imposto: IncidenciaImposto,
                 diferenca_estado: float):
        super().__init__(aliquota, incidencia_imposto)
        self.__diferenca_estado = diferenca_estado

    @property
    def diferenca_estado(self):
        return self.__diferenca_estado

    @diferenca_estado.setter
    def diferenca_estado(self, diferenca_estado: float):
        self.__diferenca_estado = diferenca_estado

    def calcula_aliquota(self):
        aliquota = self.aliquota + self.diferenca_estado
        return aliquota / 100
