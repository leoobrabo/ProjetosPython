#projeto 5 - Decida por mim
#Faça uma pergunta para o programa e ele tera que te dar uma resposta
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'com certeza, voce deve fazer isso!',
            'nao sei, vc que sabe',
            'nao faz isso nao!',
            'acho que ta na hora certa!'
        ]

    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Faça sua Pergunta', size=(39,0))],
            [sg.Input(size=(30,10))],
            [sg.Output(size=(27,10))],
            [sg.Button('Decida por mim')]

        ]
        # criar a janela
        self.janela = sg.Window('Decida por mim!', layout=layout)
        while True:
            # ler os valores
            self.eventos, self.valores = self.janela.Read()
            # fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
                

decisao = DecidaPorMim()
decisao.Iniciar()