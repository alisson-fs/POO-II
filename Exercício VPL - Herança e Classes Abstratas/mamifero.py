from abc import ABC, abstractmethod
from animal import Animal


class Mamifero(Animal, ABC):
    def __init__(self, volume_som: int, tamanho_passo: int):
        super().__init__(tamanho_passo)
        self.__volume_som = volume_som

    @property
    def volume_som(self):
        return self.__volume_som

    @volume_som.setter
    def volume_som(self, volume_som):
        self.__volume_som = volume_som

    @abstractmethod
    def produzir_som(self):
        pass
