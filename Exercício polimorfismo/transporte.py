class Transporte:
    def __init__(self,
                 nome: str,
                 altura: float,
                 comprimento: float,
                 carga: float,
                 velocidade: float):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self):
        return self.__nome

    @property
    def altura(self):
        return self.__altura

    @property
    def comprimento(self):
        return self.__comprimento

    @property
    def carga(self):
        return self.__carga

    @property
    def velocidade(self):
        return self.__velocidade

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Altura: {self.altura} m')
        print(f'Comprimento: {self.comprimento} m')
        print(f'Carga: {self.carga} t')
        print(f'Velocidade: {self.velocidade} km/h')
