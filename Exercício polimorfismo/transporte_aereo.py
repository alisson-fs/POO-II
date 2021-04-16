from transporte import Transporte


class TransporteAereo(Transporte):
    def __init__(self,
                 nome: str,
                 altura: float,
                 comprimento: float,
                 carga: float,
                 velocidade: float,
                 autonomia: float,
                 envergadura: float):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura

    @property
    def autonomia(self):
        return self.__autonomia

    @property
    def envergadura(self):
        return self.__envergadura
        
    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Altura: {self.altura} m')
        print(f'Comprimento: {self.comprimento} m')
        print(f'Carga: {self.carga} t')
        print(f'Velocidade: {self.velocidade} km/h')
        print(f'Autonomia: {self.autonomia} km')
        print(f'Envergadura: {self.envergadura} m')
