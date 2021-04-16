#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercício reutilizei a classe Fração ja utilizada nesta lista de exercicio e 
reutilizei também a logica do fatorial. No metodo de permutação contrui uma logica 
considerando repetições. Nos metodos de arranjos e combinações coloquei a opção de com 
ou sem repetioção como uma variabel booleana.'''

import random

class Fracao:
    def __init__(self, numerador: int, denominador: int):
        self.__numerador = numerador
        self.__denominador = denominador

    def numero_real(self):
        real = self.__numerador / self.__denominador
        return real

class Fatorial:
    def fatorar(self, n):
        if n <= 0:
            print('Valor inválido.')
        elif n == 1:
            return 1
        else:
            return n * self.fatorar(n - 1)

class AnaliseCombinatoria:
    def __init__(self, elementos: list, p: int):
        self.__elementos = elementos
        self.__p = p
        self.__n = len(self.__elementos)
    
    def permutacao(self, fatorial):
        caracteres_repetidos = {}
        repeticoes = []
        for caracter in self.__elementos:
            if caracter not in caracteres_repetidos.keys():
                caracteres_repetidos[caracter] = 1
            else:
                caracteres_repetidos[caracter] += 1

        for caracter in caracteres_repetidos.keys():
            if caracteres_repetidos[caracter] > 1:
                repeticoes.append(caracteres_repetidos[caracter])

        denominador_final = 1
        for repeticao in repeticoes:
            denominador_parcial = fatorial.fatorar(repeticao)
            denominador_final = denominador_final * denominador_parcial

        random.shuffle(self.__elementos)
        print(f'Uma das permutações: {self.__elementos}')

        return fatorial.fatorar(self.__n) / denominador_final

    def arranjo(self, repeticao):
        if repeticao == True:
            arranjo_aleatorio = []
            for i in range(self.__p):
                arranjo_aleatorio.append(random.choice(self.__elementos)) 
            print(f'Arranjo com repetição aleatório: {arranjo_aleatorio}')

            return self.__n ** self.__p
        else:
            numerador = Fatorial().fatorar(self.__n)
            denominador = Fatorial().fatorar(self.__n - self.__p)

            arranjo_aleatorio = [] 
            elementos = self.__elementos[:]
            for _ in range(self.__p):
                elemento_aleatorio = random.choice(elementos)
                arranjo_aleatorio.append(elemento_aleatorio)
                elementos.remove(elemento_aleatorio)
            print(f'Arranjo sem repetição aleatório: {arranjo_aleatorio}')

            return Fracao(numerador, denominador).numero_real()      

    def combinacao(self, repeticao):
        if repeticao == True:
            numerador = Fatorial().fatorar(self.__n + self.__p - 1)
            denominador = Fatorial().fatorar(self.__p) * Fatorial().fatorar(self.__n - 1)

            combinacao_aleatoria = []
            for i in range(self.__p):
                combinacao_aleatoria.append(random.choice(self.__elementos)) 
            print(f'Combinação com repetição aleatório: {combinacao_aleatoria}')

            return Fracao(numerador, denominador).numero_real()    
        else:
            numerador = Fatorial().fatorar(self.__n)
            denominador = Fatorial().fatorar(self.__p) * Fatorial().fatorar(self.__n - self.__p)

            combinacao_aleatoria = [] 
            elementos = self.__elementos[:]
            for _ in range(self.__p):
                elemento_aleatorio = random.choice(elementos)
                combinacao_aleatoria.append(elemento_aleatorio)
                elementos.remove(elemento_aleatorio)
            print(f'Combinação sem repetição aleatório: {combinacao_aleatoria}')

            return Fracao(numerador, denominador).numero_real()

def main():
    ac = AnaliseCombinatoria(list('AMAR'), 4)
    ac1 = AnaliseCombinatoria(list('ABCD'), 2)
    fatorial = Fatorial()

    print(f'Número de permutações: {ac.permutacao(fatorial)}')
    print(f'Número de arranjos sem repetições: {ac1.arranjo(False)}')
    print(f'Número de arranjos com repetições: {ac1.arranjo(True)}')
    print(f'Número de combinações sem repetições: {ac1.combinacao(False)}')
    print(f'Número de combinações com repetições: {ac1.combinacao(True)}')

main()