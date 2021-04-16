#Nome: Alisson Fabra da Silva       Matricula: 19200409

#1
vetor = [1, 2, 3, 4, 5]
print(vetor)

#2
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(vetor[::-1])

#3
notas = [6, 8, 10, 4]
soma = 0
for i in range(len(notas)):
    print(f'Nota {i + 1}: {notas[i]}')
    soma += notas[i]
print(f'Média = {soma / len(notas)}')

#4
vetor = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 0]
consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
consoantes_vetor = []
count_consoantes = 0
for i in vetor:
    if i in consoantes:
        if i not in consoantes_vetor:
            consoantes_vetor.append(i)
            count_consoantes += 1
print(f'Quantidade de consoantes: {count_consoantes} \nConsoantes: {consoantes_vetor}')

#5
inteiros = []
pares = []
impares = []
for i in range(20):
    valor = int(input('Número:'))
    inteiros.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'Inteiros: {inteiros} \nPares: {pares} \nImpares: {impares}')

#6
from random import randint
media_alunos = []
count_media7 = 0
for i in range(10):
    soma = 0
    for j in range(4):
        soma += randint(0,10)
    media_alunos.append(soma/4)
for k in media_alunos:
    if k >= 7:
        count_media7 += 1
print(f'Número de alunos com nota maior ou igual a 7: {count_media7}')
print(media_alunos)

#7
vetor = [1, 2, 3, 4, 5]
soma = 0
multiplicacao = 1
for i in vetor:
    soma += i
    multiplicacao *= i
print(f'Soma: {soma} \nMultiplicação: {multiplicacao} \nNúmeros: {vetor}')

#8
idades = []
alturas = []
for i in range(5):
    print(f'Pessoa {i + 1}')
    idade = int(input('Idade:'))
    altura = float(input('Altura:'))
    idades.append(idade)
    alturas.append(altura)
print(f'Idades na ordem inversa: {idades[::-1]}')
print(f'Alturas na ordem inversa: {alturas[::-1]}')

#9
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for i in A:
    soma += i ** 2
print(f'Soma dos quadrados dos elementos de A: {soma}')

#10
vetor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print(f'Vetor 1: {vetor1} \nVetor 2: {vetor2} \nVetor 3: {vetor3}')

#11
vetor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetor3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
vetor4 = []
for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])
print(f'Vetor 1: {vetor1} \nVetor 2: {vetor2} \nVetor 3: {vetor3} \nVetor 4: {vetor4}')

#12
idades = []
alturas = []
soma_alturas = 0
qtd_alunos_menores = 0
for i in range(30):
    print(f'Aluno {i + 1}')
    idade = int(input('Idade:'))
    altura = float(input('Altura:'))
    idades.append(idade)
    alturas.append(altura)
    soma_alturas += altura
media_altura = soma_alturas / 30
for i in range(30):
    if idades[i] > 13:
        if alturas[i] < media_altura:
            qtd_alunos_menores += 1
print(f'Quantidade de alunos com mais de 13 anos que possuem altura inferior à media de altura dos alunos: {qtd_alunos_menores}')

#13
medias_temperaturas = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
soma_medias = 0
for i in meses:
    temp_media = float(input(f'Média de temperatura de {i}:'))
    medias_temperaturas.append(temp_media)
    soma_medias += temp_media
media_medias = soma_medias / len(meses)
print('\nMeses que tiveram temperatura acima da média anual:\n')
for i in range(len(meses)):
    if medias_temperaturas[i] > media_medias:
        print(f'{meses[i]} - Média: {medias_temperaturas[i]}')

#14
count = 0
print('Responda as seguintes perguntas com S ou N')
p1 = input('Telefonou para a vítima?').upper()
p2 = input('Esteve no local do crime?').upper()
p3 = input('Mora perto da vítima?').upper()
p4 = input('Devia para a vítima?').upper()
p5 = input('Já trabalhou com a vítima?').upper()
respostas = [p1, p2, p3, p4, p5]
for i in respostas:
    if i == 'S':
        count += 1
if count == 2:
    print('Suspeita')
elif count >= 3 and count <= 4:
    print('Cúmplice')
elif count == 5:
    print('Assassino')
else:
    print('Inocente')

#15
valores = []
soma = 0
qtd_valores_acima_media = 0
qtd_valores_abaixo_7 = 0
while True:
    valor = int(input('Nota:'))
    if valor == -1:
        break
    else:
        valores.append(valor)
print(f'Quantidade de valores: {len(valores)}')
for i in range(len(valores)):
    if i != len(valores) - 1:
        print(valores[i], end=', ')
    else:
        print(f'{valores[i]}.')
    soma += valores[i]
for j in range(len(valores) - 1, -1, -1):
    print(valores[j])
print(f'Soma: {soma}')
media = soma / len(valores)
print(f'Média: {media}')
for k in valores:
    if k > media:
        qtd_valores_acima_media += 1
    if k < 7:
        qtd_valores_abaixo_7 += 1
print(f'Quantidade de valores acima da média calculada: {qtd_valores_acima_media}')
print(f'Quantidade de valores abaixo de sete: {qtd_valores_abaixo_7}')
print('Encerrando programa.')

#16
vendedores_intervalos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    valor_vendas = int(input('Valor vendas brutas da semana:'))
    salario = 200 + (valor_vendas * 0.09)
    if valor_vendas == -1:
        break
    if salario >= 200 and salario <= 299:
        vendedores_intervalos[0] += 1
    elif salario >= 300 and salario <= 399:
        vendedores_intervalos[1] += 1
    elif salario >= 400 and salario <= 499:
        vendedores_intervalos[2] += 1
    elif salario >= 500 and salario <= 599:
        vendedores_intervalos[3] += 1
    elif salario >= 600 and salario <= 699:
        vendedores_intervalos[4] += 1
    elif salario >= 700 and salario <= 799:
        vendedores_intervalos[5] += 1
    elif salario >= 800 and salario <= 899:
        vendedores_intervalos[6] += 1
    elif salario >= 900 and salario <= 999:
        vendedores_intervalos[7] += 1
    elif salario >= 100:
        vendedores_intervalos[8] += 1
print(f'Vendedores com salario entre R$200 - R$299: {vendedores_intervalos[0]}')
print(f'Vendedores com salario entre R$300 - R$399: {vendedores_intervalos[1]}')
print(f'Vendedores com salario entre R$400 - R$499: {vendedores_intervalos[2]}')
print(f'Vendedores com salario entre R$500 - R$599: {vendedores_intervalos[3]}')
print(f'Vendedores com salario entre R$600 - R$699: {vendedores_intervalos[4]}')
print(f'Vendedores com salario entre R$700 - R$799: {vendedores_intervalos[5]}')
print(f'Vendedores com salario entre R$800 - R$899: {vendedores_intervalos[6]}')
print(f'Vendedores com salario entre R$900 - R$999: {vendedores_intervalos[7]}')
print(f'Vendedores com salario de R$1000 em diante: {vendedores_intervalos[8]}')

#17
while True:
    nome = input('Atleta:').title()
    if nome == '':
        break
    print()
    saltos = []
    soma = 0
    for i in range(5):
        salto = float(input(f'{i + 1}º Salto: '))
        saltos.append(salto)
        soma += salto
    media = soma / 5
    print()
    print(f'Resultado final: \nAtleta: {nome} \nSaltos: {saltos[0]} - {saltos[1]} - {saltos[2]} - {saltos[3]} - {saltos[4]} \nMédia dos saltos: {media:.1f}')

#18
def status_melhor_jogador(jogadores, count):
    pont_max = max(jogadores)
    jogador = jogadores.index(pont_max)
    votos_porcentagem = (pont_max / count) * 100

    return pont_max, jogador, votos_porcentagem

jogadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0
print('Enquete: Quem foi o melhor jogador?\n')
while True:
    numero = int(input('Número do jogador: '))
    while numero < 0 or numero > 23:
        numero = int(input('Informe um valor entre 1 e 23 ou 0 para sair! \nNúmero do jogador: '))
    if numero == 0:
        break
    jogadores[numero - 1] += 1
    count += 1
maior_pontuacao, melhor_jogador, maior_pontuacao_porcentagem = status_melhor_jogador(jogadores, count)
print('\nResultado da votação:')
print(f'\nForam computados {count} votos.')
print('\nJogador      Votos               %')
for i in range(count):
    pont_max, jogador, votos_porcentagem = status_melhor_jogador(jogadores, count)
    if pont_max != 0:
        print(f'{jogador + 1:<15d}{pont_max:<15d}{votos_porcentagem:.1f}%')
    jogadores[jogador] = 0

print(f'O melhor jogador foi o número {melhor_jogador + 1}, com {maior_pontuacao} votos, correspondendo a {maior_pontuacao_porcentagem:.1f}% do total de votos.\n')

#19
def status_melhor_SO(opcoes, count):
    pont_max = max(opcoes)
    SO = opcoes.index(pont_max)
    votos_porcentagem = (pont_max / count) * 100

    return pont_max, SO, votos_porcentagem

opcoes = [0, 0, 0, 0, 0, 0]
opcoes_nome = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
count = 0
print('Qual o melhor Sistema Opepracional para uso em servidores?\n')
print('As possiveis respostas são:\n')
print('1- Windows Server \n2- Unix \n3- Linux \n4- Netware \n5- Mac OS \n6- Outro \nEscolha um valor entre 1 e 6 ou 0 para sair!')
while True:
    resposta = int(input('Resposta: '))
    while resposta < 0 or resposta > 6:
        resposta = int(input('Escolha um valor entre 1 e 6 ou 0 para sair! \nResposta: '))
    if resposta == 0:
        break
    opcoes[resposta - 1] += 1
    count += 1
maior_pontuacao, melhor_SO, maior_pontuacao_porcentagem = status_melhor_SO(opcoes, count)
print('\nSistema Operacional     Votos     % \n-------------------     -----     ----')
for i in range(count):
    pont_max, posicao_SO, votos_porcentagem = status_melhor_SO(opcoes, count)
    if pont_max != 0:
        print(f'{opcoes_nome[posicao_SO]:<25s}{pont_max:<9d}{votos_porcentagem:.1f}%')
    opcoes[posicao_SO] = 0
print('-------------------     -----     ----')
print(f'Total{count:>20d}')
print(f'O Sistema Operacional mais votado foi o {melhor_SO}, com {maior_pontuacao} votos, correspondendo a {votos_porcentagem:.1f}% dos votos.')

#20
class MinhaLista:
    def __init__(self):
        self.__tupla = tuple()

    def __str__(self):
        if len(self.__tupla) == 0:
            string = '[]'
        else:
            string = ''
        for i in range(len(self.__tupla)):
            try: 
                int(self.__tupla[i])
                tipo = True
            except ValueError:
                tipo = False
            if tipo:
                if i == 0:
                    if len(self.__tupla) == 1:
                        string += '['+str(self.__tupla[i])+']'
                    else:
                        string += '['+str(self.__tupla[i])+', '
                elif i == len(self.__tupla) - 1:
                    string += str(self.__tupla[i])+']'
                else:
                    string += str(self.__tupla[i])+', '
            else:
                if i == 0:
                    if len(self.__tupla) == 1 and tipo == False:
                        string += '['+"'"+str(self.__tupla[i])+"'"+']'
                    else:
                        string += '['+"'"+str(self.__tupla[i])+"'"+', '
                elif i == len(self.__tupla) - 1:
                    string += "'"+str(self.__tupla[i])+"'"+']'
                else:
                    string += "'"+str(self.__tupla[i])+"'"+', '
        return string

    @property
    def tupla(self):
        return self.__tupla
    
    @tupla.setter
    def tupla(self, nova_tupla):
        self.__tupla = nova_tupla

    def append(self, item):
        self.__tupla += tuple(str(item))

    def remove(self, item):
        lista_auxiliar = MinhaLista()
        for i in self.__tupla:
            if str(item) != i:
                lista_auxiliar.append(i)
        self.__tupla = lista_auxiliar.tupla
    
    def sort(self):
        lista_ordenada = MinhaLista()
        lista_auxiliar = MinhaLista()
        lista_auxiliar.tupla = self.__tupla[:]
        for _ in range(len(self.__tupla)):
            lista_ordenada.append(min(lista_auxiliar.tupla))
            lista_auxiliar.remove(min(lista_auxiliar.tupla))
        self.__tupla = lista_ordenada.tupla
    
    def reverse(self):
        nova_tupla = self.__tupla[::-1]
        self.__tupla = nova_tupla

    def pop(self, index):
        for i in range(len(self.__tupla)):
            if index - 1 == i:
                item = self.__tupla[i]
        self.remove(item)

lista = MinhaLista()
lista.append('B')
lista.append('A')
lista.append('C')
lista.append(1)
print(lista)
lista.remove('A')
print(lista)
lista.append('A')
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)
lista.reverse()
print(lista)
lista.pop(2)
print(lista)
lista1 = MinhaLista()
lista1.append(1)
print(lista1)
lista1.remove(1)
print(lista1)