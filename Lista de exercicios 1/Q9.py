#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercicio fiz apenas uma classe que possui o metodo jogar que é onde inicia o 
jogo e chama todos os outros metodos da classe. O metodo montar campo define as posições 
das bombas, o metodo printar_campo mostra printa a situação atual do campo, o metodo 
escolher_casa solicita uma casa para o jogador, o metodo conta_bombas define quantas 
bombas tem ao redor da casa que o jgoador escolheu e o metodo fim printa o campo mostrando 
as bombas. O metodo jogar tem um while True que roda até o fim do jogo, ele é parado se o 
jogador escolher uma casa com bomba ou se o jogador acertar todas as casas sem bomba.'''

import random

class CampoMinado:

    def __init__(self):
        self.__campo_jogador = []
        self.__campo_bombas = []
        self.__opcoes = ['[B]', '[B]', '[B]', '[B]', '[B]', '[B]', '[B]', '[B]', '[B]', '[B]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']
        self.__tentativas = []

    def jogar(self):
        self.montar_campo()
        while True:
            self.printar_campo()
            linha, coluna = self.escolher_casa()
            self.__campo_jogador[linha][coluna] = self.__campo_bombas[linha][coluna]
            if self.__campo_bombas[linha][coluna] == '[B]':
                print('BUUUUUUUUUUUUUM!!! \nVocê perdeu!')
                self.fim()
                break
            else:
                self.__tentativas.append([linha + 1, coluna + 1])
                self.__campo_jogador[linha][coluna] = f'[{self.conta_bomba(self.__campo_bombas, linha, coluna)}]'
            if len(self.__tentativas) == 71:
                print('Você ganhou!!!')
                self.fim()
                break

    def fim(self):
        for i in range(9):
            for j in range(9):
                if self.__campo_bombas[i][j] == '[B]':
                    self.__campo_jogador[i][j] = self.__campo_bombas[i][j]
        self.printar_campo()
    
    
    def montar_campo(self):
        random.shuffle(self.__opcoes)
        for i in range(9):
            campo = []
            for j in range(9):
                campo.append(self.__opcoes[0])
                del self.__opcoes[0]
            self.__campo_bombas.append(campo)

        for i in range(9):
            campo = []
            for j in range(9):
                campo.append('[ ]')
            self.__campo_jogador.append(campo)

    def escolher_casa(self):
        print('Escolha uma linha e uma coluna de 1 a 9:')
        linha = int(input('Linha:'))
        coluna = int(input('Coluna:'))
        while [linha, coluna] in self.__tentativas:
            print('Você ja escolheu esta casa. Escolha uma linha e uma coluna novamente de 1 a 9:')
            linha = int(input('Linha:'))
            coluna = int(input('Coluna:'))
        return linha - 1, coluna - 1


    def conta_bomba(self, campo_bombas, linha, coluna):
        posicoes_com_bomba = 0
        if linha > 0 and campo_bombas[linha - 1][coluna] == '[B]':
            posicoes_com_bomba += 1
        if linha < len(campo_bombas) - 1 and campo_bombas[linha + 1][coluna] == '[B]':
            posicoes_com_bomba += 1
        if coluna > 0 and campo_bombas[linha][coluna - 1] == '[B]':
            posicoes_com_bomba += 1
        if coluna < len(campo_bombas[0]) - 1 and campo_bombas[linha][coluna + 1] == '[B]':
            posicoes_com_bomba += 1
        if linha > 0 and coluna > 0 and campo_bombas[linha - 1][coluna - 1] == '[B]':
            posicoes_com_bomba += 1
        if linha > 0 and coluna < len(campo_bombas[0]) - 1 and campo_bombas[linha - 1][coluna + 1] == '[B]':
            posicoes_com_bomba += 1
        if linha < len(campo_bombas) - 1 and coluna > 0 and campo_bombas[linha + 1][coluna - 1] == '[B]':
            posicoes_com_bomba += 1
        if linha < len(campo_bombas) - 1 and coluna < len(campo_bombas[0]) - 1 and campo_bombas[linha + 1][coluna + 1] == '[B]':
            posicoes_com_bomba += 1
              
        return posicoes_com_bomba

    def printar_campo(self):
        for i in range(9):
            for j in range(9):
                print(self.__campo_jogador[i][j], end=' ')
            print()

def main():
    cm = CampoMinado()
    cm.jogar()
main()