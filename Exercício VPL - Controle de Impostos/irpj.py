from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class IRPJ(Imposto):
    def __init__(self,
                 aliquota: float,
                 incidencia_imposto: IncidenciaImposto, desconto: float):
        super().__init__(aliquota, incidencia_imposto)
        self.__desconto = desconto

    def calcula_aliquota(self):
        aliquota = self.aliquota - self.__desconto
        return aliquota / 100
