import random
class Lancador:
    def __init__(self):
        self.moeda = 'cara'
        self.dado = 1

    def lanca_dado(self):
        self.dado = random.randint(1,6)
       # print(f'Voce rolou: {self.dado}')
        return f'Voce rolou: {self.dado}'

    def lanca_moeda(self):
        pass

objLancador = Lancador()
objLancador.lanca_dado()
a = Lancador()
a.lanca_dado()
