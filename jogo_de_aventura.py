#Projeto 7 - Jogo de Aventura
#um jogo de decisoes onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas
#chegar a finais diferentes, de acordo com as respostas que eu passe para o programa
#qual o cenario: estamos em uma guerra entre duas naçoes, onde somente uma saira vencedora, entao temos que tomar a decisao correta pra chegar ate a vitoria 
class JogoDeAventura:
    def __init__(self):
        self.cena1 = "Voce nasceu no norte ou no sul? (n/s)\n" # norte = LadoA, SUL = LadoB
        self.cena2 = "Voce prefere a espada ou escudo? (espada/escudo)\n" #espada = LadoA, escudo = LadoB
        self.cena3 = "Qual sua especialidade?(frente/tatico)\n" #linha de frente = LadoA, tatico = LadoB
        
        self.final1 ="Você será um HEROI na linha de frente!"
        self.final2 ="Você será um HEROI protegendo nossas tropas!"
        self.final3 ="Voce FALHARA nesta batalha\nVocê e fraco lhe falta ODIO!"
        self.final4 ="Você FALHARA nos defendedo!"
        self.final5 ="Voçê e um LIDER nato na linha de frente!"
        self.final6 ="Você E UM ESTRATEGISTA nato!"
        self.final7 ="Voçê FALHARA na LIDERANÇA da linha de frente!"
        self.final8 ="Você FALHARAE na sua Estrategia!"

    def Iniciar(self):
        cena1 = input(self.cena1)
        if cena1 == 'n':
            cena1 = input(self.cena2)
            if cena1 == 'espada':
                print(self.final1)
            if cena1 == 'escudo':
                print(self.final2)
            cena2 = input(self.cena3)
            if cena2 == 'frente':
                print(self.final5)
            if cena2 == 'tatico':
                print(self.final6)
        if cena1 == 's':
            cena1 = input(self.cena2)
            if cena1 == 'espada':
                print(self.final3)
            if cena1 == 'escudo':
                print(self.final2)
            cena2 = input(self.cena3)
            if cena2 == 'frente':
                print(self.final7)
            if cena2 == 'tatico':
                print(self.final8)
            

jogo = JogoDeAventura()
jogo.Iniciar()
