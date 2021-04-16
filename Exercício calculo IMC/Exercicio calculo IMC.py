import PySimpleGUI as sg


class IMC:
    def __init__(self):
        linha0 = [sg.Text('Qual seu peso?'),
                  sg.InputText('', key='peso'),
                  sg.Text('kg')]
        linha1 = [sg.Text('Qual sua altura?'),
                  sg.InputText('', key='altura'),
                  sg.Text('cm')]
        linha2 = [sg.Text('Seu IMC é'),
                  sg.Text('', key='imc', size=(6, 1))]
        linha3 = [sg.Text('Classificação:'),
                  sg.Text('', key='classificacao', size=(20, 1))]
        linha4 = [sg.Text('', size=(14, 1)),
                  sg.Button('Calcular IMC')]
        container = [linha0, linha1, linha2, linha3, linha4]

        self.__window = sg.Window('Calculadora de IMC',
                                  container,
                                  font=('Helvetica', 14))
        self.__values = None

    @property
    def window(self):
        return self.__window

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values

    def run(self):
        while True:
            event, self.values = self.window.read()
            print(self.values)
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Calcular IMC':
                imc = self.calcularIMC()
                if imc < 14.5:
                    classificacao = 'Desnutrição'
                elif imc >= 14.5 and imc < 20:
                    classificacao = 'Peso abaixo do normal'
                elif imc >= 20 and imc < 25:
                    classificacao = 'Peso normal'
                elif imc >= 25 and imc <= 29.9:
                    classificacao = 'Sobrepeso'
                elif imc >= 30 and imc <= 39.9:
                    classificacao = 'Obesidade'
                else:
                    classificacao = 'Obesidade mórbida'
                self.window.Element('imc').Update(imc)
                self.window.Element('classificacao').Update(classificacao)
        self.window.close()

    def calcularIMC(self):
        alturaSTR = self.values['altura'].replace(',', '').replace('.', '')
        peso = float(self.values['peso'])
        altura = float(alturaSTR) / 100
        imc = peso / (altura ** 2)
        return round(imc, 2)


def main():
    imc = IMC()
    imc.run()


main()
