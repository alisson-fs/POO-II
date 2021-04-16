#Nome: Alisson Fabra da Silva       Matricula: 19200409

#1
def remover_caracteres_especiais(string):
    nova_string = ''
    caracteres_especiais = ('"', "'", '.', ',', '(', ')', ':', ';', '!', '@', '#', '$', '%', '&', '*', '-', '_', '=', '+', '[', ']', '{', '}', '?', '/', '<', '>', '|')
    for i in string:
        if i not in caracteres_especiais:
            nova_string += i
    return nova_string

texto = open('texto_Q1_dicionarios.txt')
palavras = remover_caracteres_especiais(texto.read().lower())

dicionario = {}
for palavra in palavras.split():
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

for keys, values in dicionario.items():
    print(f'{keys}: {values}')

#2
def remover_caracteres_especiais(string):
    nova_string = ''
    caracteres_especiais = ('"', "'", '.', ',', '(', ')', ':', ';', '!', '@', '#', '$', '%', '&', '*', '-', '_', '=', '+', '[', ']', '{', '}', '?', '/', '<', '>', '|')
    for i in string:
        if i not in caracteres_especiais:
            nova_string += i
    return nova_string

def remover_stopwords(dicionario):
    stopwords = open('stopwords.txt').read()
    dicionario_sem_stopwords = dicionario.copy()
    for j in dicionario:
        if j in stopwords:
            del dicionario_sem_stopwords[j]
    return dicionario_sem_stopwords

texto = open('texto_Q1_dicionarios.txt')
palavras = remover_caracteres_especiais(texto.read().lower())

dicionario = {}
for palavra in palavras.split():
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

dicionario_sem_stopwords = remover_stopwords(dicionario)
for keys, values in dicionario_sem_stopwords.items():
    print(f'{keys}: {values}')

#3
dicionario = {}
while True:
    aluno = input('Aluno: ').title()
    if aluno == '':
        break
    nota1 = float(input('Nota 1: '))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input('Valor inválido, digitenovamente a nota 1: '))
    nota2 = float(input('Nota 2: '))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input('Valor inválido, digitenovamente a nota 2: '))
    dicionario[aluno] = [nota1, nota2]
for k, v in dicionario.items():
    media = (v[0] + v[1]) / 2
    print(f'Aluno: {k} \nMédia: {media:.1f}')

#4
def melhor_volta(dicionario):
    melhor_volta_tempo = 10 ** 1000000
    melhor_volta_corredor = str
    for k, v in dicionario.items():
        for i in range(len(v)):
            if melhor_volta_tempo > v[i]:
                melhor_volta_tempo = v[i]
                melhor_volta = i + 1
                melhor_volta_corredor = k
    return melhor_volta, melhor_volta_corredor

def melhor_corredor(dicionario):
    resultado = {}
    melhor_media = 10 ** 1000000
    melhor_corredor = ''
    for k, v in dicionario.items():
        qtd_voltas = len(v)
        resultado[k] = 0
        for i in range(qtd_voltas):
            resultado[k] += v[i]
        v = resultado[k]
        media_voltas = resultado[k] / qtd_voltas
        if media_voltas < melhor_media:
            melhor_media =  media_voltas
            melhor_corredor = k
    return melhor_media, melhor_corredor

dicionario = {}
for i in range(6):
    corredor = input('Nome do corredor: ').title()
    voltas = []
    for j in range(10):
        volta = int(input(f'Tempo da volta {j + 1}: '))
        voltas.append(volta)
    dicionario[corredor] = voltas

melhor_volta1, melhor_volta_corredor1 = melhor_volta(dicionario)
print(f'A melhor volta da corrida foi a volta {melhor_volta1} do corredor {melhor_volta_corredor1}.')
print('\nClassificação: \n')
for i in range(6):
    melhor_media1, melhor_corredor1 = melhor_corredor(dicionario)
    print(f'{i + 1}º - {melhor_corredor1:<20s}Média: {melhor_media1:.0f}s')
    del dicionario[melhor_corredor1]

#5
def incluir_novo_nome(dicionario):
    nome = input('Nome completo: ').title()
    telefones = []
    continuar = 'S'
    while continuar == 'S':
        telefone = input('Telefone: ')
        telefones.append(telefone)
        continuar = input('Responda com S ou N. Adicionar mais um número?').upper()
    dicionario[nome] = telefones

def incluir_telefone(dicionario):
    nome = input('Nome completo: ').title()
    if nome in dicionario.keys():
        telefone = input('Telefone: ')
        dicionario[nome].append(telefone)
    else:
        incluir_novo_nome(dicionario)

def excluir_telefone(dicionario):
    nome = input('Nome completo: ').title()
    telefone = input('Telefone: ')
    if nome in dicionario.keys():
        if telefone in dicionario[nome]:
            dicionario[nome].remove(telefone)
        else:
            print('Telefone não cadastrado.')
    else:
        print('Pessoa não cadastrada.')

def excluir_nome(dicionario):
    nome = input('Nome completo: ').title()
    if nome in dicionario.keys():
        del dicionario[nome]
    else:
        print('Pessoa não cadastrada.')

def consulta_telefone(dicionario):
    nome = input('Nome completo: ').title()
    if nome in dicionario.keys():
        print(dicionario[nome])
    else:
        print('Pessoa não cadastrada.')

agenda = {}
while True:
    acao = int(input('Escolha uma opção pelos números: \n1- Incluir novo nome \n2- Incluir telefone \n3- Excluir telefone \n4- Excluir nome \n5- Consultar telefones \n6- Parar \nOpção: '))
    while acao < 1 and acao > 6:
        acao = int(input('Valor inválido, escolha a opção pelo número. Opção: '))
    if acao == 6:
        break
    elif acao == 1:
        incluir_novo_nome(agenda)
    elif acao == 2:
        incluir_telefone(agenda)
    elif acao == 3:
        excluir_telefone(agenda)
    elif acao == 4:
        excluir_nome(agenda)
    elif acao == 5:
        consulta_telefone(agenda)

#6
from random import randint
dicionario = {}

for _ in range(10):
    lista = []
    soma = 0
    for _ in range(30):
        x = randint(0, 100)
        lista.append(x)
        soma += x
    fset = frozenset(lista)
    dicionario[fset] = soma

for k, v in dicionario.items():
    print(f'{k}: {v}')

#7
class MeuDicionario:
    def __init__(self):
        self.__chaves = []
        self.__valores = []

    def __str__(self):
        if len(self.__chaves) == 0:
            string = '{}'
        else:
            string = ''
            for i in range(len(self.__chaves)):
                if i == 0:
                    if len(self.__chaves) == 1:
                        string += '{'+str(self.__chaves[i])+': '+str(self.__valores[i])+'}'
                    else:
                        string += '{'+str(self.__chaves[i])+': '+str(self.__valores[i])+', '
                elif i == len(self.__chaves) - 1:
                    string += str(self.__chaves[i])+': '+str(self.__valores[i])+'}'
                else:
                    string += str(self.__chaves[i])+': '+str(self.__valores[i])+', '
        return string
    
    def __getitem__(self, chave):
        for i in range(self.__chaves):
            if self.__chaves[i] == chave:
                return self.__valores[i]
    
    def __setitem__(self, chave, valor):
        if chave not in self.__chaves:
            self.__chaves.append(chave)
            self.__valores.append(valor)
        else:
            for i in range(len(self.__chaves)):
                if self.__chaves[i] == chave:
                    self.__valores[i] = valor

    def __delitem__(self, chave):
        for i in range(len(self.__chaves)):
            if self.__chaves[i] == chave:
                del self.__chaves[i]
                del self.__valores[i]

    def __contains__(self, valor):
        for i in range(len(self.__valores)):
            if self.__valores[i] == valor:
                return True

dic1 = MeuDicionario()
dic2 = MeuDicionario()

dic1['um'] = 1
dic1['dois'] = 2
print(dic1)
del dic1['dois']
print(dic1)
print(dic2)
T_F = 1 in dic1
print(T_F)

#8
class MatrizEsparsa:
    def __init__(self):
        self.__matriz = []
        self.__matriz_string = ''
        self.__dupla = tuple()
        self.__dicionario = {}
        
    def construir_matriz_dicionario(self, dupla, dicionario):
        self.__dupla = dupla
        self.__dicionario = dicionario
        for i in range(self.__dupla[0]):
            linha = []
            for j in range(self.__dupla[1]):
                linha.append(dicionario[i + 1, j + 1])
            self.__matriz.append(linha)

    def construir_matriz_string(self, matriz_string):
        self.__matriz_string = matriz_string
        linhas = self.__matriz_string.splitlines()
        for linha in linhas:
            self.__matriz.append(linha.split())
        for i in range(len(self.__matriz)):
            for j in range(len(self.__matriz[0])):
                self.__matriz[i][j] = int(self.__matriz[i][j])

    def mostrar_matriz_dicionario(self):
        for i in range(len(self.__matriz)):
            for j in range(len(self.__matriz[i])):
                if i == len(self.__matriz) - 1 and j == len(self.__matriz[0]) - 1:
                    print(f'({i + 1}, {j + 1}):{self.__matriz[i][j]}'+'}')
                elif i == 0 and j == 0:
                    print('{'+f'({i + 1}, {j + 1}):{self.__matriz[i][j]}', end=', ')
                else:
                    print(f'({i + 1}, {j + 1}):{self.__matriz[i][j]}', end=', ')

    def mostrar_matriz_string(self):
        for i in range(len(self.__matriz)):
            for j in range(len(self.__matriz[0])):
                print(self.__matriz[i][j], end=' ')
            print()


matriz1 = '''0 8 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 2 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 7 0 0 0 0 0
0 0 0 0 0 0 4 0 0'''

matriz2 = '''1 2
3 4'''
     
m1 = MatrizEsparsa()
m2 = MatrizEsparsa()
m1.construir_matriz_dicionario((2, 2), {(1, 1): 1, (1, 2): 2, (2, 1): 3, (2, 2): 4})
m2.construir_matriz_string(matriz1)
m1.mostrar_matriz_dicionario()
m1.mostrar_matriz_string()
m2.mostrar_matriz_dicionario()
m2.mostrar_matriz_string()