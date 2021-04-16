from mamifero import Mamifero


class Gato(Mamifero):
    def __init__(self, volume_som = 2, tamanho_passo = 2):
        super().__init__(volume_som, tamanho_passo)

    def produzir_som(self):
        return 'MAMIFERO: PRODUZ SOM: '+str(self.volume_som)+' SOM: MIAU'

    def miar(self):
        return self.produzir_som()
