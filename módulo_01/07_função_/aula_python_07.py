# exercicio 1
# Escreva uma função que recebe dois parâmetros (números) 
# e imprime o menor dos dois. Se eles forem iguais, 
# imprima que são valores idênticos
def numeros(num1,num2):
  if num1 < num2:
    print('num1 é menor')
  elif num2 < num1:
    print('num2 é menor')
  else:
    print('São iguais')

num1=float(input('digite num1: '))
num2=float(input('digite num2: '))
numeros(num1,num2)

#exercicio 2
# Escreva uma função que recebe dois números (a e b) 
# como parâmetro e retorna True caso a soma dos dois 
# seja maior que um terceiro parâmetro, chamado limite.
def fgv(a,b):
    limite = 20
    soma = a + b
    if soma > limite:
        return True 
    else:
        return False

limite = int(input('digte: '))
bb = int(input('digte: '))
bra = int(input('digte: '))
puc = fgv(bb,bra)
print(puc)

#exercicio 3
# Crie uma função que receba uma string como argumento
#  e retorne a mesma string em letras maiúsculas.
#   Faça uma chamada à função,
#  passando como parâmetro uma string.
def go(cerveja):
   print('Você gosta de',cerveja)
   return cerveja

ir=input('digite o que você mais gosta: ').upper()
ir= go(ir)

#exercicio 4
# Crie um programa que tenha uma função chamada voto ()
#  que vai receber como parâmetro o ano de nascimento de
#   uma pessoa, retornando um valor literal indicando se 
#   uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas 
#   eleições. Para resolver esse exercício,
#  pesquise sobre a função date da biblioteca Datetime.
import datetime

def voto(ano_nascimento):

    ano_ = datetime.date.today().year
    ano_nas = ano_ - int(ano_nascimento)
    if ano_nas < 18:
      print('VOTO NEGADO')
    elif ano_nas >= 18 and ano_nas <= 70:
      print('VOTO OBRIGATORIO')
    elif ano_nas >70:
      print('VOTO OPCIONAL')
      return ano_nas

dt = input('digite o ano do seu nascimento: ')
dt= voto(dt)

#exercicio 5
# Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros:
#  o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
#  mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>',gol=0):
  print(f'o jogador {jog} fez {gol} gols no campeonato')

n = input('nome: ')
g = input('gols: ')

if g.isnumeric():
  g= int(g)
else:
  g=0
if n.strip() == '':
  ficha(gol=g)
else:
  ficha(n,g)

#exercicio 6
# Um professor, muito legal, fez 3 provas durante um semestre
#  mas só vai levar em conta as duas notas mais altas para calcular a média.
# Faça uma aplicação que peça o valor das 3 notas, mostre como seria a
#  média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

def provas(a,b,c):
  primeira = n1
  if n2 > n1 and n2 > n3:
    primeira = n2
  elif n3 > n1 and n3 > n2:
    primeira = n3

  segunda = n2
  if n3 < n2 and n3 > n1:
    segunda = n3
  elif n1 < n2 and n1 >n3:
    segunda = n1

  if n1 < n2 and n1 <n3:
    terceira = n1
  elif n2 < n1 and n2 < n3:
    terceira= n2
  else:
    terceira = n3

  media3 = (n1+n2+n3)/3

  media_maior = (primeira+segunda)/2
  print('''Media com as 3 notas :{:.2f} 
  A maior nota:{}
  A menor nota:{}'''.format(media3,primeira,segunda,media_maior,primeira,terceira))
  return f'media com as 3 notas:{media3:.2f}'
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
print(provas(n1,n2,n3))
