import time #biblioteca com função para dar uma pausa no jogo
import random  #biblioteca com funçao para gerar um número aleatório

class Evento:
    def __init__(self, numero):
        self.numero = numero
    
class EventoSorte(Evento):  #criando uma subclasse chamada "evento sorte" para os eventos em que ele ganha dinheiro
    def __init__(self, numero):
        self.numero = numero
        self.presente= 0
        super().__init__(numero)
    
    def ganhaValor(self):
        if self.numero == 1:
            print("Parabéns você ganhou na mega sena!!")
            premio = 1000000
            self.presente = premio
        elif self.numero == 2:
            print("Que sorte, você achou 50 reais!!")
            achado = 50
            self.presente = achado
        elif self.numero == 3:
            print("Os casos de violência aumentaram e você foi assaltado!!")
            self.presente = -50 
            return self.presente

class EventoAzar(Evento):  #criando uma subclasse "evento Azar" para o evento em que ele perde dinheiro
    def __init__(self, numero):
        self.numero = numero
        self.presente = 0
        super().__init__(numero)
    
    def perdeValor (self):
        if self.numero == 4:
            print("Os casos de violência aumentaram e você foi assaltado!!")
            self.presente = -50
            return self.presente     

class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))

class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.dinheiro = 0
        self.salario = 100
    
    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False

class PersonagemNoite (Personagem):  #criando uma subclasse para o Personagem da Noite
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.salario = 100
        super().__init__()
    
    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação."


class Casa:
    def __init__(self):
        self.remedios = 1
        self.comida = 5

if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    personagem_noite = PersonagemNoite()    #criando o objeto personagem da noite
    casa = Casa()
    cafe_da_manha = False
    turno = "dia"
    jantar= False
    parada = True
    print ("*=*"*40)
    print("\t \t \t \t \t \tBEM VINDO(A) AO JOGO DA VIDA!!")
    print ("*=*"*40)    
    while parada:
        while turno == "dia":
            print("---")
            print("São "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até às 07:00.")
            print(personagem)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Fazer café da manhã")
            print("3 - Pedir café da manhã")
            print("4 - Tomar café da manhã")
            print("5 - Tomar remédio")
            print("6 - Comprar remédio")
            print("7 - Ir trabalhar")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if(opcao == "1"):
                personagem.sujo = False
                relogio.avancaTempo(20)
            elif(opcao == "2"):
                if(casa.comida > 0):
                    casa.comida -= 1
                    cafe_da_manha = True
                else:
                    print("Não há comida em casa.")
                relogio.avancaTempo(15)
            elif(opcao == "3"):
                if(personagem.dinheiro >= 15):
                    personagem.dinheiro -= 15
                    cafe_da_manha = True
                else:
                    print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
                relogio.avancaTempo(5)
            elif(opcao == "4"):
                if(cafe_da_manha):
                    personagem.fome = False
                    cafe_da_manha = False
                    relogio.avancaTempo(15)
                else:
                    print("Não tem café da manhã na sua casa.")
                    relogio.avancaTempo(5)
            elif(opcao == "5"):
                if(casa.remedios > 0):
                    casa.remedios -= 1
                    personagem.medicado = True
                else:
                    print("Não tem remédio na sua casa")
                relogio.avancaTempo(5)
            elif(opcao == "6"):
                if(personagem.dinheiro >= 20):
                    casa.remedios += 10
                    personagem.dinheiro -= 20
                    relogio.avancaTempo(10)
                else:
                    print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
                    relogio.avancaTempo(5)
            elif(opcao == "7"):
                print("-=-=-")
                print("Você foi trabalhar.")
                print(personagem)
                print("-=-=-")
                evento = random.randint (1 , 4)  #Fazendo o evento aleatório acontecer   
                if evento == 1:
                    print("Você zerou o jogo!")
                    parada = False
                    break  #no caso de ganhar na mega sena, o jogador zera o jogo e ele acaba
                evento_sorte_dia = EventoSorte(evento)
                evento_azar_dia = EventoAzar(evento)
                evento_sorte_dia.ganhaValor()
                evento_azar_dia.perdeValor()
                recebido = personagem.salario
                print("-=-=-")
                if(not personagem.medicado):
                    print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
                    recebido = 0
                elif(personagem.sujo):
                    print("Como você estava sujo, seus colegas reclamaram para seu chefe, e você levou uma advertência.")
                    recebido *= 0.9
                elif(personagem.fome):
                    print("Como você estava com fome, você trabalhou metade do que consegue trabalhar.")
                    recebido *= 0.5
                elif(relogio.atrasado()):
                    print("Como você chegou atrasado, você produziu menos do que de costume.")
                    recebido *= 0.8 
                
                recebido += evento_sorte_dia.presente #somando o dinheiro ganho ou perdido durante o evento aleatório
                recebido += evento_azar_dia.presente
                personagem.dinheiro += recebido #se adiciona o recebido do dia ao dinheiro total do personagem          
                print("-=-=-")
                print("Você recebeu "+str(recebido)+" hoje.")
                print("-=-=-")
                turno="noite"
            elif(opcao == "0"):
                break
            else:
                print("Opção inválida!")
                Relogio.avancaTempo(5)
        while turno == "noite":
            print("---")
            print("Uffa Voce chegou em casa !!!")
            print(personagem_noite)
            print("")
            print("Ações:")
            print("1 - Tomar banho ")
            print("2 - Fazer jantar")
            print("3 - Pedir marmitex")
            print("4 - Jantar")
            print("5 - Tomar remédio")
            print("6 - Comprar remédio")
            print("7 - Ir dormir")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if(opcao == "1"):
                personagem_noite.sujo = False
                relogio.avancaTempo(20)
            elif(opcao == "2"):
                if(casa.comida > 0):
                    casa.comida -= 1
                    jantar = True
                else:
                    print("Não há comida em casa.")
                relogio.avancaTempo(15)
            elif(opcao == "3"):
                if(personagem.dinheiro >= 35):
                    personagem.dinheiro -= 35
                    jantar = True
                else:
                    print("O jantar custa 35 reais, você não tem dinheiro suficiente.")
                relogio.avancaTempo(5)
            elif(opcao == "4"):
                if(jantar):
                    personagem_noite.fome = False
                    jantar = False
                    relogio.avancaTempo(15)
                else:
                    print("Não tem jantar na sua casa.")
                    relogio.avancaTempo(5)
            elif(opcao == "5"):
                if(casa.remedios > 0):
                    casa.remedios -= 1
                    personagem_noite.medicado = True
                else:
                    print("Não tem remédio na sua casa")
                relogio.avancaTempo(5)
            elif(opcao == "6"):
                if(personagem.dinheiro >= 20):
                    casa.remedios += 10
                    personagem.dinheiro -= 20
                    relogio.avancaTempo(10)
                else:
                    print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
                    relogio.avancaTempo(5)
            elif(opcao == "7"):
                print("-=-=-")
                print("Boa noite! bons sonhos até amanhã.")                        
                personagem.dormir() 
                relogio = Relogio()
                turno = "dia" #o personagem dorme e a noite vira dia 
                dia+=1
            elif(opcao == "0"): #identando o break para dentro do while da noite
                break
            else:
                print("Opção inválida!")
                Relogio.avancaTempo(5)