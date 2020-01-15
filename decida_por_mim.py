#projeto 5 - Decida por mim
#Faça uma pergunta para o programa e ele tera que te dar uma resposta
import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'com certeza, voce deve fazer isso!',
            'nao sei, vc que sabe',
            'nao faz isso nao!',
            'acho que ta na hora certa!'
        ]

    def Iniciar(self):
        input('Faça sua pergunta\n')
        print(random.choice(self.respostas))

decisao = DecidaPorMim()
decisao.Iniciar()