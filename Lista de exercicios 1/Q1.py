#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercicio resolvi criar 1 classe para cada tipo de conta e uma classe para o banco.
Simulei o arquimo Main com a função main() no fim do codigo, nele tentei fazer o sistema funcionar 
de forma que poderia ser utilizado em um banco para registro de clientes e contas.'''

class Banco:
    def __init__(self, nome: str, telefone: str):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self):
        return self.__telefone

class ContaCorrente:
    def __init__(self, titulares: list, saldo: float):
        self.__titulares = titulares
        self.__saldo = saldo
        self.__lista_operacoes = []

    @property
    def titulares(self):
        return self.__titulares
    
    def saque(self, quantidade):
        if self.__saldo <= 0:
            print('Saldo insuficiente.')
        elif self.__saldo - quantidade < 0:
            print('Saldo insuficiente.')
        else:
            self.__saldo -= quantidade
            self.__lista_operacoes.append(-quantidade)
    
    def deposito(self, quantidade):
        self.__saldo += quantidade
        self.__lista_operacoes.append(quantidade)

    @property
    def saldo(self):
        print(f'R${self.__saldo:.2f}')

    def extrato(self):
        print('Extrato:')
        for i in self.__lista_operacoes:
            print(f'R$ {i:.2f}')

    def resumo_conta(self):
        print('Resumo da conta:')
        print('Titulares:')
        for i in self.__titulares:
            print(f'Nome: {i.nome}  Telefone: {i.telefone}')
        print(f'Saldo: R$ {self.__saldo:.2f}')

class ContaEspecial:
    def __init__(self, titulares: list, saldo: float):
        self.__titulares = titulares
        self.__limite_especial = 50
        self.__saldo = saldo + self.__limite_especial
        self.__lista_operacoes = []

    @property
    def titulares(self):
        return self.__titulares

    def saque(self, quantidade):
        if self.__saldo <= 0:
            print('Saldo insuficiente.')
        elif self.__saldo - quantidade < 0:
            print('Saldo insuficiente.')
        else:
            self.__saldo -= quantidade
            self.__lista_operacoes.append(-quantidade)
    
    def deposito(self, quantidade):
        self.__saldo += quantidade
        self.__lista_operacoes.append(quantidade)

    @property
    def saldo(self):
        print(f'R${self.__saldo:.2f}')

    def extrato(self):
        print('Extrato:')
        for i in self.__lista_operacoes:
            print(f'R$ {i:.2f}')

    def resumo_conta(self):
        print('Resumo da conta:')
        print('Titulares:')
        for i in range(len(self.__titulares)):
            print(f'Nome: {i.nome} Telefone: {i.telefone}')
        print(f'Saldo: R$ {self.__saldo:.2f}')
        print(f'Esta conta é do tipo Especial, ela possui R${self.__limite_especial:.2f} de limite a mais que esta incluido no saldo.')

class ContaPoupanca:
    def __init__(self, titulares: list, saldo: float, tempo_conta_meses: int):
        self.__rendimento_mensal = 0.0001
        self.__tempo_conta_meses = tempo_conta_meses
        self.__rendimento_total = self.__tempo_conta_meses * self.__rendimento_mensal
        self.__titulares = titulares
        self.__saldo = saldo + (saldo * self.__rendimento_total)
        self.__lista_operacoes = []

    @property
    def titulares(self):
        return self.__titulares

    def saque(self, quantidade):
        if self.__saldo <= 0:
            print('Saldo insuficiente.')
        elif self.__saldo - quantidade < 0:
            print('Saldo insuficiente.')
        else:
            self.__saldo -= quantidade
            self.__lista_operacoes.append(-quantidade)
    
    def deposito(self, quantidade):
        self.__saldo += quantidade
        self.__lista_operacoes.append(quantidade)

    @property
    def saldo(self):
        print(f'R${self.__saldo:.2f}')

    def extrato(self):
        print('Extrato:')
        for i in self.__lista_operacoes:
            print(f'R$ {i:.2f}')

    def resumo_conta(self):
        print('Resumo da conta:')
        print('Titulares:')
        for i in range(len(self.__titulares)):
            print(f'Nome: {i.nome} Telefone: {i.telefone}')
        print('Saldo: R$')
        print(f'Rendimento mensal: {self.__rendimento_mensal}')
        print(f'Tempo da conta em meses: {self.__tempo_conta_meses}')
            
def main():
    clientes = []
    contas_corrente = []
    contas_especiais = []
    contas_poupancas = []

    while True:
        verificando_cliente_novo = True 
        acao = int(input('Escolha entre as opções 1 e 2: \n 1 - Registrar conta \n 2 - Acessar conta \n Opção:'))
        while acao != 1 and acao != 2:
            acao = int(input('Opção inválida, escolha uma as opções 1 e 2: \n 1 - Registrar conta \n 2 - Acessar conta \n Opção:'))
            
        if acao == 1:
            while verificando_cliente_novo == True:
                cliente_novo = input('Responda com SIM ou NAO. Já é cliente?').upper()
                while cliente_novo != 'SIM' and cliente_novo != 'NAO':
                    cliente_novo = input('Resposta inválida, resposnda novamente com SIM ou NAO. Já é cliente?').upper()
            
                if cliente_novo == 'NAO':
                    nome_cliente = input('Nome:').upper()
                    telefone_cliente = input('Telefone:')
                    while len(telefone_cliente) != 11:
                        telefone_cliente = input('Número inválido. digite novamente seu telefone:')
                    clientes.append(Banco(nome_cliente, telefone_cliente))
                else:
                    procurar_cliente = input('Nome:').upper()
                    for i in clientes:
                        if i.nome == procurar_cliente:
                            verificando_cliente_novo = False
                        else:
                            verificando_cliente_novo = True

            tipo_conta = int(input('Escolha entre as opções 1, 2 ou 3: \n 1 - Conta Corrente \n 2 - Conta Especial \n 3 - Conta Poupança \n Opção:'))
            while tipo_conta != 1 and tipo_conta != 2 and tipo_conta != 3:
                tipo_conta = int(input('Opção inválida, escolha entre as opções 1, 2 ou 3: \n 1 - Conta Corrente \n 2 - Conta Especial \n 3 - Conta Poupança \n Opção:'))

            titulares = []
            if tipo_conta == 1:
                qtd_titulares = int(input('Quantos titulares?'))
                for i in range(qtd_titulares):
                    add_titular = input('Cliente:').upper()
                    for j in clientes:
                        if j.nome == add_titular:
                            titulares.append(j)
                        else:
                            print('Cliente não cadastrado.')
                saldo = float(input('Saldo:'))
                contas_corrente.append(ContaCorrente(titulares, saldo))
            
            elif tipo_conta == 2:
                qtd_titulares = int(input('Quantos titulares?'))
                for i in range(qtd_titulares):
                    add_titular = input('Cliente:').upper()
                    for j in clientes:
                        if j.nome == add_titular:
                            titulares.append(j)
                        else:
                            print('Cliente não cadastrado.')
                saldo = float(input('Saldo:'))
                contas_especiais.append(ContaEspecial(titulares, saldo))

            else:
                qtd_titulares = int(input('Quantos titulares?'))
                for i in range(qtd_titulares):
                    add_titular = input('Cliente:').upper()
                    for j in clientes:
                        if j.nome == add_titular:
                            titulares.append(j)
                        else:
                            print('Cliente não cadastrado.')
                saldo = float(input('Saldo:'))
                n_meses_conta = int(input('Ja possui a conta a quantos meses?'))
                contas_poupancas.append(ContaPoupanca(titulares, saldo, n_meses_conta))

        if acao == 2:
            possui_conta = False
            um_titular = input('Nome de um titular:').upper()
            for j in clientes:
                if j.nome == um_titular:
                    tipo_conta = int(input('Escolha entre as opções 1, 2 ou 3: \n 1 - Conta Corrente \n 2 - Conta Especial \n 3 - Conta Poupança \n Opção:'))
                    while tipo_conta != 1 and tipo_conta != 2 and tipo_conta != 3:
                        tipo_conta = int(input('Opção inválida, escolha entre as opções 1, 2 ou 3: \n 1 - Conta Corrente \n 2 - Conta Especial \n 3 - Conta Poupança \n Opção:'))

                    acao_conta = int(input('Escolha entre as opções 1, 2, 3, 4 ou 5: \n 1 - Sacar \n 2 - Depositar \n 3 - Ver saldo \n 4 - Ver extrato \n 5 - Resumo da conta \n Opção:'))
                    while acao_conta != 1 and acao_conta != 2 and acao_conta != 3 and acao_conta != 4 and acao_conta != 5:
                        acao_conta = int(input('Opção inválida, escolha entre as opções 1, 2, 3, 4 ou 5: \n 1 - Sacar \n 2 - Depositar \n 3 - Ver saldo \n 4 - Ver extrato \n 5 - Resumo da conta \n Opção:'))

                    if tipo_conta == 1:
                        for i in contas_corrente:
                            for j in i.titulares:
                                if j.nome == um_titular:
                                    conta = i
                                    possui_conta = True

                        if possui_conta == True:
                            if acao_conta == 1:
                                qtd_saque = float(input('Valor do saque:'))
                                conta.saque(qtd_saque)

                            elif acao_conta == 2:
                                qtd_deposito = float(input('Valor do depósito:'))
                                conta.deposito(qtd_deposito)

                            elif acao_conta == 3:
                                conta.saldo

                            elif acao_conta == 4:
                                conta.extrato()

                            else:
                                conta.resumo_conta()
                        else:
                            print('Você não tem uma conta deste tipo.')

                    elif tipo_conta == 2:
                        for i in contas_especiais:
                            for j in i.titulares:
                                if j.nome == um_titular:
                                    conta = i
                                    possui_conta = True

                        if possui_conta == True:
                            if acao_conta == 1:
                                qtd_saque = float(input('Deseja sacar quanto?'))
                                conta.saque(qtd_saque)

                            elif acao_conta == 2:
                                qtd_deposito = float(input('Valor do depósito:'))
                                conta.deposito(qtd_deposito)

                            elif acao_conta == 3:
                                conta.saldo

                            elif acao_conta == 4:
                                conta.extrato()

                            else:
                                conta.resumo_conta()
                        else:
                            print('Você não tem uma conta deste tipo.')

                    else:
                        for i in contas_poupancas:
                            for j in i.titulares:
                                if j.nome == um_titular:
                                    conta = i
                                    possui_conta = True
                                
                        if possui_conta == True:
                            if acao_conta == 1:
                                qtd_saque = float(input('Deseja sacar quanto?'))
                                conta.saque(qtd_saque)

                            elif acao_conta == 2:
                                qtd_deposito = float(input('Valor do depósito:'))
                                conta.deposito(qtd_deposito)

                            elif acao_conta == 3:
                                conta.saldo

                            elif acao_conta == 4:
                                conta.extrato()

                            else:
                                conta.resumo_conta()
                        else:
                            print('Você não tem uma conta deste tipo.')
                else:
                    print('Cliente não cadastrado.')

main()