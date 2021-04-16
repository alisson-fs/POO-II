#Aluno: Alisson Fabra da Silva         Matricula: 19200409

'''Neste exercicio fiz a classe Aluno que recebe os dados cadastrais do aluno e a classe 
Professor que recebe os dados cadastrais do professor. Nessas duas classes coloquei os 
metodos get para conseguir acessar os atributos da classe. Criei também a classe Turma, 
que é onde recebe os dados cadastrais da turma e tem um metodo para mostrar os professores 
e seus dados, um para mostrar os alunos e seus dados e outro para preencher as informações 
de cada aluno referente a turma, como presenças e notas. '''

class Aluno:
    def __init__(self, nome: str, matricula: str):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula

class Professor:
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

class Turma:
    def __init__(self, n_turma: str, professores: list, alunos: list):
        self.__n_turma = n_turma
        self.__professores = professores
        self.__alunos = alunos
        self.__info_aluno = {}
        self.__info_alunos = []


    def alunos(self):
        print('Alunos:')
        for i in self.__info_alunos:
            print('Nome: {} \n Matricula: {} \n Notas: {} \n Presenças: {}'.format(i['nome'], i['matricula'], i['notas'], i['presencas']))

    def professores(self):
        for i in self.__professores:
            print(f'Professores: \n Nome: {i.nome} \n CPF: {i.cpf}')

    def preencher_info_aluno(self, nome_aluno, notas, presencas):
        aluno_cadastrado = False
        for i in self.__alunos:
            if i.nome == nome_aluno:
                self.__info_aluno['nome'] = i.nome
                self.__info_aluno['matricula'] = i.matricula
                self.__info_aluno['notas'] = notas
                self.__info_aluno['presencas'] = presencas
                self.__info_alunos.append(self.__info_aluno.copy())
                self.__info_aluno.clear()
                aluno_cadastrado = True

        if aluno_cadastrado == False:
            print('Aluno não cadastrado no sistema.')
        else:
            print('Informações preenchidas com sucesso.')

def main():
    alisson = Aluno('Alisson', '192001')
    daniel = Aluno('Daniel', '192002')
    mateus = Professor('Mateus', '11122233344')
    jonata = Professor('Jônata', '12312312345')
    turma1 = Turma('208', [mateus, jonata], [alisson, daniel])

    turma1.preencher_info_aluno('Alisson', [10, 9], 50)
    turma1.preencher_info_aluno('Daniel', [8, 7], 45)
    turma1.preencher_info_aluno('Joãozinho', [3, 2], 10)
    turma1.professores()
    turma1.alunos()
main()