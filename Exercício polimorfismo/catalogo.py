from transporte import Transporte


class Catalogo:
    def __init__(self):
        self.__veiculos = []
        
    @property
    def veiculos(self):
        return self.__veiculos
        
    def insercao(self, veiculo):
        if isinstance(veiculo, Transporte):
            self.veiculos.append(veiculo)
        else:
            print('Veiculo invalido.')

    def apresentacao(self):
        for i in self.__veiculos:
            i.apresentar()
            print()
