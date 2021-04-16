from abc import ABC, abstractmethod
from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__mao = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def mao(self) -> list:
        return self.__mao

    def baixa_carta_da_mao(self) -> Carta:
        carta = random.choice(self.__mao)
        self.__mao.remove(carta)
        return carta

    def inclui_carta_na_mao(self, carta:Carta):
        if isinstance(carta, Carta):
            self.__mao.append(carta)
