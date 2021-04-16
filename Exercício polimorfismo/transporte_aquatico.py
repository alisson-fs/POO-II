from transporte import Transporte


class TransporteAquatico(Transporte):
    def __init__(self,
                 nome: str,
                 altura: float,
                 comprimento: float,
                 carga: float,
                 velocidade: float,
                 boca: float,
                 calado: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    @property
    def boca(self):
        return self.__boca

    @property
    def calado(self):
        return self.__calado
        
    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Altura: {self.altura} m')
        print(f'Comprimento: {self.comprimento} m')
        print(f'Carga: {self.carga} t')
        print(f'Velocidade: {self.velocidade} km/h')
        print(f'Boca: {self.boca} m')
        print(f'Calado: {self.calado} m')
