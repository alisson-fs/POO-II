#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercício criei a classe Matematica que tem todos os metodos necessários para o 
exercicio. Escolhi criar a classe sem atributos pois para fazer recursão com os metodos 
era necessário receber o valor na chamada do método.'''

class Matematica:

    def fibonacci(self, n):
        if n <= 0:
            print('Valor inválido.')
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fatorial(self, n):
        if n <= 0:
            print('Valor inválido.')
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return (n - 1) * self.fatorial(n - 1)

    def primo(self, n):
        memoria_primo = {'n': int}
        inicio = 1
        cont = 1
        while cont <= n:
            cont_divisores = 0
            for i in range(1, inicio + 1):
                if inicio % i == 0:
                    cont_divisores += 1
            if cont_divisores == 2:
                memoria_primo['n'] = inicio
                cont += 1
            inicio += 1
        return memoria_primo['n']

def main():
    mtm = Matematica()
    print(f'Fibonacci: {mtm.fibonacci(5)}')
    print(f'Fatorial: {mtm.fatorial(5)}')
    print(f'Primo: {mtm.primo(5)}')
main()