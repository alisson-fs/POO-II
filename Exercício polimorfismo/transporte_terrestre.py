from transporte import Transporte


class TransporteTerrestre(Transporte):
    def __init__(self,
                 nome: str,
                 altura: float,
                 comprimento: float,
                 carga: float,
                 velocidade: float,
                 motor: str,
                 rodas: str):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__rodas = rodas

    @property
    def motor(self):
        return self.__motor

    @property
    def rodas(self):
        return self.__rodas

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Altura: {self.altura} m')
        print(f'Comprimento: {self.comprimento} m')
        print(f'Carga: {self.carga} t')
        print(f'Velocidade: {self.velocidade} km/h')
        print(f'Motor: {self.motor}')
        print(f'Rodas: {self.rodas}')
