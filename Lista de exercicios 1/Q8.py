#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercício só criei a classe JogoForca que recebe a palavra que deverá ser adivinhada. 
Nessa classe criei o metodo jogar que será o que dará o inicio nas tentativas, continuará neste 
metodo por conta while True que roda até que o jogo chegue ao fim. Neste metodo é chamado o metodo 
palavra que printa a situação da palavra que o jogador deve acertar. Também é chamado o metodo 
tentativa, que é onde é solicidada o chute do jogador e também chama o metodo boneco, que é 
utilizado para printar a situação atual do boneco enforcado que esta na forca. Se chegar o número 
máximo de erros o boneco ficará completo e o jogador perderá.'''

class JogoForca:
    def __init__(self, palavra: str):
       self.__palavra = palavra
       self.__digitadas = []
       self.__acertos = []
       self.__erros = 0

    def jogar(self):
        while True:
            senha = self.palavra()
            if senha == self.__palavra:
                print('Você acertou!')
                break
            self.tentativa()
            self.boneco()
            if self.__erros == 6:
                print('Enforcado!')
                break

    def boneco(self):
        linha1 = ''
        linha2 = ''
        linha3 = ''
        print('X==:==\nX  :   ')
        if self.__erros >= 1:
            linha1 = 'X  O  '
            print(linha1)
        else:
            linha1 = 'X'
            print(linha1)
        if self.__erros == 2:
            linha2 = 'X  |  '
            print(linha2)
        elif self.__erros == 3:
            linha2 = 'X \|  '
            print(linha2)
        elif self.__erros >= 4:
            linha2 = 'X \|/ '
            print(linha2)
        else:
            linha2 = 'X'
            print(linha2)
        if self.__erros == 5:
            linha3 = 'X /   '
            print(linha3)
        elif self.__erros >= 6:
            linha3 = 'X / \ '
            print(linha3)
        else:
            linha3 = 'X'
            print(linha3)
        print("X\n===========")

    def palavra(self):
        senha = ''
        for letra in self.__palavra:
            senha += letra if letra in self.__acertos else '.'
        print(senha)
        return senha

    def tentativa(self):
        tentativa = input('\nDigite uma letra:').upper().strip()
        while tentativa in self.__digitadas:
            print("Você já tentou esta letra!")
            tentativa = input('\nDigite uma letra:').upper().strip()
        else:
            self.__digitadas += tentativa
            if tentativa in self.__palavra:
                self.__acertos += tentativa
            else:
                self.__erros += 1
                print('Você errou!')

def main():
    palavra = input('Digite a palavra secreta:').upper().strip()
    jf = JogoForca(palavra)
    for i in range(50):
        print()
    jf.jogar()

main()