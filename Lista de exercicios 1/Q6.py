#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercício criei apenas a classe baralho que recebe uma lista de cartas, para que 
possa ser utilizado para qualquer tipo de baralho. Criei um metodo para distribuir as 
cartas e outro para mostrar a carta de cada jogador.'''

from random import randint

class Baralho:
    def __init__(self, cartas: list):
        self.__cartas = cartas
        
    def distribuir(self, quantidade_cartas, quantidade_jogadores):
        cartas_distribuidas = []
        jogador = []
        for i in range(quantidade_jogadores):
            for j in range(quantidade_cartas):
                carta_aleatoria = randint(0, len(self.__cartas))
                jogador.append(self.__cartas[carta_aleatoria])
                del self.__cartas[carta_aleatoria]
            cartas_distribuidas.append(jogador)
            jogador = []
        return cartas_distribuidas

    def mostrar_cartas(self, jogador, cartas_distribuidas):
        print(f'Jogador {jogador}: {cartas_distribuidas[jogador - 1]}')

        
def main():
    naipes = ['OURO', 'ESPADA', 'COPAS', 'PAUS']
    numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cartas = []

    for i in naipes:
        for j in numeros:
            cartas.append([f'{i} - {j}'])
    copag = Baralho(cartas)
    cartas_distribuidas = copag.distribuir(3, 5)
    copag.mostrar_cartas(1, cartas_distribuidas)
    copag.mostrar_cartas(2, cartas_distribuidas)
    copag.mostrar_cartas(3, cartas_distribuidas)
    copag.mostrar_cartas(4, cartas_distribuidas)
    copag.mostrar_cartas(5, cartas_distribuidas)

main()