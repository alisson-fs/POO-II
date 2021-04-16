from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagems = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagems

    def inclui_personagem_na_lista(self,
                                   energia: int,
                                   habilidade: int,
                                   velocidade: int,
                                   resistencia: int,
                                   tipo: Tipo) -> Personagem:
        if isinstance(energia and
                      habilidade and
                      velocidade and
                      resistencia, int) and \
                isinstance(tipo, Tipo):
            personagem = Personagem(energia,
                                    habilidade,
                                    velocidade,
                                    resistencia,
                                    tipo)
            self.__personagems.append(personagem)
            return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        if isinstance(personagem, Personagem):
            carta = Carta(personagem)
            self.__baralho.append(carta)
            return carta

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador):
        if isinstance(jogador1 and jogador2, Jogador):
            for _ in range(5):
                carta = random.choice(self.__baralho)
                jogador1.inclui_carta_na_mao(carta)
                self.__baralho.remove(carta)
            for _ in range(5):
                carta = random.choice(self.__baralho)
                jogador2.inclui_carta_na_mao(carta)
                self.__baralho.remove(carta)

    def jogada(self, mesa: Mesa) -> Jogador:
        if isinstance(mesa, Mesa):
            carta1 = mesa.carta_jogador1
            carta2 = mesa.carta_jogador2
            soma1 = carta1.valor_total_carta()
            soma2 = carta2.valor_total_carta()
            if soma1 > soma2:
                mesa.jogador1.inclui_carta_na_mao(carta1)
                mesa.jogador1.inclui_carta_na_mao(carta2)
            elif soma1 < soma2:
                mesa.jogador2.inclui_carta_na_mao(carta1)
                mesa.jogador2.inclui_carta_na_mao(carta2)
            else:
                mesa.jogador1.inclui_carta_na_mao(carta1)
                mesa.jogador2.inclui_carta_na_mao(carta2)
            if len(mesa.jogador1.mao) == 0:
                return mesa.jogador2
            elif len(mesa.jogador2.mao) == 0:
                return mesa.jogador1
            return None
