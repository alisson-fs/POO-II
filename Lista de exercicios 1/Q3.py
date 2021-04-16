#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercício crei apenas criei apenas a classe polinomio e fiz todas as relações que 
o polinomio deve ter como metodo da classe. Fiz todas as ações pensando em logicas com a 
lista de coeficientes.'''

class Polinomio:
    def __init__(self, coeficientes: list):
        self.__coeficientes = coeficientes

    @property
    def coeficientes(self):
        return self.__coeficientes

    def printar(self):
        print('Polinômio = ', end='')
        for i in range(len(self.__coeficientes)):
            if i == 0:
                print(f'{self.__coeficientes[i]}', end=' + ')
            elif i == len(self.__coeficientes) - 1:
                print(f'{self.__coeficientes[i]}*x^{i}')
            else:
                print(f'{self.__coeficientes[i]}*x^{i}', end=' + ')

    def grau(self):
        print(f'O grau do poliômio é {len(self.__coeficientes) - 1}')

    def resultado(self, x):
        resultado = 0
        for i in range(len(self.__coeficientes)):
            resultado += self.__coeficientes[i] * (x ** i)
        print(f'Resultado = {resultado}')

    def somar(self, polinomio2, printar = True, pol_somado = 0):
        maior = max(len(self.__coeficientes),len(polinomio2.coeficientes))
        coeficientes_somados = []

        if maior != len(self.__coeficientes):
            coeficientes_somados = polinomio2.coeficientes[:]
            for i in range(len(self.__coeficientes)):
                coeficientes_somados[i] += self.__coeficientes[i]
        else:
            coeficientes_somados = self.__coeficientes[:]
            for i in range(len(polinomio2.coeficientes)):
                coeficientes_somados[i] += polinomio2.coeficientes[i]

        pol = Polinomio(coeficientes_somados)

        if printar == True:
            pol.printar()
        else:
            return pol

    def multiplicar(self, polinomio2, pol_somado, recursao = False, grau = 1):
        coeficientes1 = []
        coeficientes2 = []
        pol_somado1 = pol_somado


        if len(self.__coeficientes) >= 2 and recursao == False:
            for i in range(2):
                for j in range(len(polinomio2.coeficientes)):
                    if i == 0:
                        coeficientes1.append(self.__coeficientes[i] * polinomio2.coeficientes[j])
                    else:
                        coeficientes2.append(self.__coeficientes[i] * polinomio2.coeficientes[j])
            coeficientes2.insert(0, 0)

            pol1 = Polinomio(coeficientes1)
            pol2 = Polinomio(coeficientes2)
            if len(self.__coeficientes) == 2:
                pol_somado = pol1.somar(pol2)
            else:
                pol_somado = pol1.somar(pol2, False)
            del self.__coeficientes[0]
            del self.__coeficientes[1]
            grau += 1
            self.multiplicar(polinomio2, pol_somado, True, grau)
            
            
        elif len(self.__coeficientes) >= 1 and recursao == True:
            for j in range(len(polinomio2.coeficientes)):
                coeficientes1.append(self.__coeficientes[0] * polinomio2.coeficientes[j]) 
            for k in range(grau):
                coeficientes1.insert(0, 0)
            pol1 = Polinomio(coeficientes1)
            if len(self.__coeficientes) == 1:
                pol_somado.somar(pol1)
            else:
                pol_somado = pol1.somar(pol_somado1, False)
                grau +=1
                self.multiplicar(polinomio2, pol_somado, True, grau)
            del self.__coeficientes[0]

        elif len(self.__coeficientes) == 1 and recursao == False:
            for j in range(len(polinomio2.coeficientes)):
                coeficientes1.append(self.__coeficientes[0] * polinomio2.coeficientes[j])
            pol1 = Polinomio(coeficientes1)
            print(f'Resultado = {pol1.printar()}')

def main():

    polinomio1 = Polinomio([1, 1, 1])
    polinomio2 = Polinomio([1, 2, 3])

    polinomio1.printar()
    polinomio2.printar()
    polinomio1.grau()
    polinomio1.resultado(2)
    polinomio1.somar(polinomio2)
    polinomio1.multiplicar(polinomio2, Polinomio([]))

main()