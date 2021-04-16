from imposto import Imposto
from incidencia_imposto import IncidenciaImposto


class IPI(Imposto):
    def __init__(self,
                 aliquota: float,
                 incidencia_imposto: IncidenciaImposto,
                 aliquota_adicional: bool):
        super().__init__(aliquota, incidencia_imposto)
        self.__aliquota_adicional = aliquota_adicional

    def calcula_aliquota(self):
        if self.__aliquota_adicional:
            aliquota = self.aliquota * 1.1
        else:
            aliquota = self.aliquota
        return aliquota / 100
