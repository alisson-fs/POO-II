#Aluno: Alisson Fabra da Silva         Matricula: 19200409

#Questão 1:
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

#Questão 2:
class Televisao:
    def __init__(self, tamanho: float, marca: str):
        self.tamanho = tamanho
        self.marca = marca
        self.ligada = False
        self.canal = 2

tv1  = Televisao(40, 'Samsung')
tv2 = Televisao(50, 'LG')

print(f'Tamanho: {tv1.tamanho}, marca: {tv1.marca}')
print(f'Tamanho: {tv2.tamanho}, marca: {tv2.marca}')

#Questão 3:
class Televisao:
    def __init__(self, tamanho: float, marca: str, canal: 2):
        self.tamanho = tamanho
        self.marca = marca
        self.ligada = False
        self.canal = canal

    def muda_canal_para_cima(self):
        self.canal += 1

    def muda_canal_para_baixo(self):
        self.canal -= 1

#Questão 4:
class Televisao:
    def __init__(self, tamanho: float, marca: str, canal: 2):
        self.tamanho = tamanho
        self.marca = marca
        self.ligada = False
        self.canal = canal
        self.canal_minimo = 1
        self.canal_maximo = 99

    def muda_canal_para_cima(self):
        if self.canal == 99:
            self.canal = 1
        else:
            self.canal += 1

    def muda_canal_para_baixo(self):
        if self.canal == 1:
            self.canal = 99
        else:
            self.canal -= 1

#Questão 5:
class Televisao:
    def __init__(self, tamanho: float, marca: str, canal_minimo: 2, canal_maximo: 14, canal: 2):
        self.tamanho = tamanho
        self.marca = marca
        self.ligada = False
        self.canal = canal
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo

    def muda_canal_para_cima(self):
        if self.canal == 99:
            self.canal = 1
        else:
            self.canal += 1

    def muda_canal_para_baixo(self):
        if self.canal == 1:
            self.canal = 99
        else:
            self.canal -= 1

#Questão 6:
class Televisao:
    def __init__(self, tamanho: float, marca: str, canal_minimo: 2, canal_maximo: 14, canal: 2):
        self.tamanho = tamanho
        self.marca = marca
        self.ligada = False
        self.canal = canal
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo

    def muda_canal_para_cima(self):
        if self.canal == 99:
            self.canal = 1
        else:
            self.canal += 1

    def muda_canal_para_baixo(self):
        if self.canal == 1:
            self.canal = 99
        else:
            self.canal -= 1

tv1 = Televisao(40, 'Samsung', 1, 99, 12)
tv2 = Televisao(50, 'LG', 3, 49, 4)

#Questão 7:
class Cidade:
    def __init__(self, nome: str, populacao: int):
        self.nome = nome
        self.populacao = populacao

class Estado:
    def __init__(self, nome: str, sigla: str, cidades: list):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
        self.cidades_list = cidades

        for i in range(0, len(self.cidades_list), 2):
            self.cidades.append(Cidade(self.cidades_list[i], self.cidades_list[i+1]))

    def calcular_populacao(self):
        populacao_total = 0
        for i in self.cidades:
            populacao_total += i.populacao

        print(f'A população do estado {self.nome} é {populacao_total}.')

estado1 = Estado('Santa Catarina', 'SC', ['Florianópolis', 1000000, 'Palhoça', 10000])
estado2 = Estado('Rio de Janeiro', 'RJ', ['Rio de Janeiro', 9000000, 'Niteroi', 90000])
estado3 = Estado('São Paulo', 'SP', ['São Paulo', 9900000, 'Campinas', 7000000])

estado1.calcular_populacao()
estado2.calcular_populacao()
estado3.calcular_populacao()

#Questão 8
import math

class Coordenada:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def mostrar_coordenadas(self):
        print(f'Coordenada({self.__x},{self.__x})')

    def distancia_coordenadas(self, ponto_aleatorio):
        distancia = (((ponto_aleatorio.__x - self.__x) ** 2) + ((ponto_aleatorio.__y - self.__y) ** 2)) ** 0.5
        print(f'A distância entre as coordenadas é {distancia:.2f}')

    def comparar_coordenadas(self, ponto_aleatorio):
        if self.__x == ponto_aleatorio.__x and self.__y == ponto_aleatorio.__y:
            print('As coordenadas são iguais.')
        else:
            print('As coordenaads são diferentes.')

    def coordenada_polar(self):
        radial = ((self.__x ** 2) + (self.__y ** 2)) ** 0.5
        print(f'Radial = {radial:.2f}')
        if self.__x > 0:
            angular = math.atan(self.__y / self.__x)
            print(f'Angular = {angular:.2f}')
        elif self.__x < 0 and self.__y >= 0:
            angular = math.atan(self.__y / self.__x) * math.pi
            print(f'Angular = {angular:.2f}')
        elif self.__x < 0 and self.__y < 0:
            angular = math.atan(self.__y / self.__x) * (- math.pi)
            print(f'Angular = {angular:.2f}')
        elif self.__x == 0 and self.__y > 0:
            angular = math.pi / 2
            print(f'Angular = {angular:.2f}')
        elif self.__x == 0 and self.__y < 0:
            angular = - (math.pi / 2)
            print(f'Angular = {angular:.2f}')
        elif self.__x == 0 and self.__y == 0:
            print('Angular indefiniido')

p1 = Coordenada(1, 1)
p2 = Coordenada(4, 4)

p1.mostrar_coordenadas()
p2.mostrar_coordenadas()
p1.distancia_coordenadas(p2)
p1.comparar_coordenadas(p2)
p1.coordenada_polar()
p2.coordenada_polar()

#Questão 9:
import math

class Quadrado:
    def __init__(self, lado: int):
        self.__lado = lado

    def area(self):
        print(f'Área do quadrado = {self.__lado ** 2}')

class Retangulo:
    def __init__(self, base: int, altura: int):
        self.__base = base
        self.__altura = altura

    def area(self):
        print(f'Área do retangulo = {self.__base * self.__altura}')

class Circulo:
    def __init__(self, raio: float):
        self.__raio = raio

    def area(self):
        print(f'Área do circulo = {math.pi * (self.__raio ** 2)}')

form1 = Quadrado(2)
form2 = Retangulo(2, 4)
form3 = Circulo(2)

form1.area()
form2.area()
form3.area()

#Questão 10:
import math

def mmc(x1, x2):
    menor = min(x1, x2)
    while True:
        if menor % x1 == 0 and menor % x2 ==0:
            return menor
        else:
            menor += min(x1, x2)


class Fracao:
    def __init__(self, numerador: int, denominador: int):
        self.__numerador = numerador
        self.__denominador = denominador

#a
    def soma_fracao(self, fracao2):
        num = int(((mmc(self.__denominador, fracao2.__denominador) / self.__denominador) * self.__numerador) + ((mmc(self.__denominador, fracao2.__denominador) / fracao2.__denominador) * fracao2.__numerador))
        den = int(mmc(self.__denominador, fracao2.__denominador))
        print(f'{num}/{den}')


    def subtracao_fracao(self, fracao2):
        num = int(((mmc(self.__denominador, fracao2.__denominador) / self.__denominador) * self.__numerador) - ((mmc(self.__denominador, fracao2.__denominador) / fracao2.__denominador) * fracao2.__numerador))
        den = int(mmc(self.__denominador, fracao2.__denominador))
        print(f'{num}/{den}')

    def multiplicacao_fracao(self, fracao2):
        num = self.__numerador * fracao2.__numerador
        den = self.__denominador * fracao2.__denominador
        print(f'{num}/{den}')

    def divisao_fracao(self, fracao2):
        num = self.__numerador * fracao2.__denominador
        den = self.__denominador * fracao2.__numerador
        print(f'{num}/{den}')
#b
    def imprime_fracao(self):
        print(f'{self.__numerador}/{self.__denominador}')

#c
    def inverte_fracao(self):
        invertida = Fracao(self.__denominador, self.__numerador)
        invertida.imprime_fracao()

#d
    def numero_real(self):
        real = self.__numerador / self.__denominador
        print(f'Número real: {real}')

#e
def cria_fracao(n_real):
    n_real_str = str(n_real)
    n_real_separado = n_real_str.split('.')
    
    denominador = int(10 * len(n_real_separado[1]))
    numerador = int(n_real * denominador)

    return Fracao(numerador, denominador)

fracao1 = cria_fracao(0.5)
fracao2 = Fracao(1, 3)

fracao1.imprime_fracao()
fracao2.imprime_fracao()

fracao1.soma_fracao(fracao2)
fracao1.subtracao_fracao(fracao2)
fracao1.multiplicacao_fracao(fracao2)
fracao1.divisao_fracao(fracao2)

fracao1.inverte_fracao()
fracao1.numero_real()