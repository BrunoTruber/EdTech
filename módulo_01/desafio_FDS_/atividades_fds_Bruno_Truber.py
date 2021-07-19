#01 - Utilizando estruturas condicionais faça um programa que 
# pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da 
   # divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

num1 = float(input('digite um numero: ').replace(',','.'))
num2 = float(input('digite um numero: ').replace(',','.'))

# as operações
resultadoA = num1 + num2
resultadoB = num1 * num2
resultadoC = num1 // num2
print(f'resultado A: {resultadoA}\n resultado B: {resultadoB}\n resultado C: {resultadoC}')

# qual o maior
if num1 > num2:
    print('"num1" É MAIOR')
elif num1< num2:
        print('"num2" É MAIOR')
else:
    print('SÃO IGUAIS')

# par ou impar
if resultadoA%2 == 0:
    print('A SOMA É PAR')
else:
    print('A SOMA É IMPAR')

# maior ou igual a 40
if resultadoC == 0.0:
    print('"resultado C" NÃO PODE SER O DIVISOR!')
elif resultadoB >= 40:
    print('QUANDO A MULTIPLICAÇÃO FOR MAIOR QUE 40: ',resultadoB / resultadoC)
else:
    print('A MULTIPLICAÇÃO NÃO FOI MAIOR QUE 40!')


#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma 
# string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e
#  mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

frase = input('digite uma frase ou palavra: ')
vogais =[]
cont= 0
for i in frase:
    if i in 'aeiou':
        vogais.append(i)
        cont +=1
recebe = frase
tira = 'aeiou'
for letras in tira:
    if letras in recebe:
        recebe = recebe.replace(letras,'')
print(f'Vogais: {vogais}')
print(f'Quantidade: {cont}')
print(f'Frase sem vogais: {recebe}')



#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar 
# seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar
#  dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai
#  “pensar” em um número inteiro entre 0 e 20. O jogador vai tentar adivinhar qual número foi 
# escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador 
# é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer
from random import randint
senha = "blue2021"
entrada = input("Digite a senha: ")

while entrada != senha:
    print("Senha incorreta!")
    entrada = input("Digite a senha: ")
print("Agora sim! Acesso liberado.")
print('#*#'*18)
print('Bem vindo ao jogo da advinhação!')
print('#*#'*18)
print('Vou pensar em um numero de 0 a 20. Tente advinhar...')

computador = randint(0,20)
pass_ = False
tentativas = 0
while  not pass_:
   jogador  = int(input('Em que numero eu pensei? '))
   tentativas += 1
   if jogador == computador:
      pass_ = True
   else:
      if jogador < computador:
         print('Um pouco mais...')
      elif jogador > computador:
         print('um pouco menos...')
print('Acertou com {} tentativas'.format(tentativas))

#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma 
# string no formato D de mesPorExtenso de AAAA. Valide a data e retorne NULL caso a data seja inválida.
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')

def mesPorExtenso(com_string):
    
    try:
        datetime.strptime(com_string, '%d/%m/%Y')
    except ValueError:
        print('NULL')
        return None
        
    else:
        data_ = datetime.strptime(com_string, '%d/%m/%Y')
        return datetime.strftime(data_, '%d de %B de %Y')
dt = input('digite a data no formato DD/MM/AAAA: ')
dt_str = mesPorExtenso(dt)

if dt_str is not None:
    print(dt_str)

#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e
#  retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras
#  foram retiradas da frase original.
def fgv():
   frase = input('digite uma frase ou palavra: ')
   vogais =[]
   cont= 0
   for i in frase:
        if i in 'aeiou':
            vogais.append(i)
            cont +=1
   recebe = frase
   tira = 'aeiou'
#    for letras in tira:
#         if letras in recebe:
#             recebe = recebe.replace(letras,'')
  # print(f'Vogais: {vogais}')
   print(f'Quantidade de vogais retiradas: {cont}')
  # print(f'Frase sem vogais: {recebe}')
fgv()


#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".
pergunta_1 = int(input('Telefonou para a vítima? [1] Sim [0] Não: '))
pergunta_2 = int(input('Esteve no local co crime? [1] Sim [0] Não: '))
pergunta_3 = int(input('Mora perto da vítima? [1] Sim [0] Não: '))
pergunta_4 = int(input('Devia para a vítima? [1] Sim [0] Não: '))
pergunta_5 = int(input('Já trabalhou com a vítima? [1] Sim [0] Não: '))

lista_perguntas = [pergunta_1,pergunta_2,pergunta_3,pergunta_4,pergunta_5]

if sum(lista_perguntas) == 2:
    print('Você me parece um tanto suspeito!')
elif sum(lista_perguntas) == 3 and sum(lista_perguntas) == 4:
    print('Você o ajudou no crime!')
elif sum(lista_perguntas) == 5:
    print('Você é o assassino!')
else:
    print('Inocente! Se livrou de uma hein...')


#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
# em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.
# print('Bem vindo ao separador de números pares e ímpares!')
numeros = [[], []]
valores = 0
for c in range(1, 8):
   valores = int(input('digite um numero: '))
   if valores % 2 == 0:
      numeros[0].append(valores)
   else:
      numeros[1].append(valores)
print('_'*45)
numeros[0].sort()
numeros[1].sort()
print('Todos os valores pares são:',numeros[0])
print('Todos os valores ímpares são:',numeros[1])

#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os 
# (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá 
# também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos
#  a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('carteira de Trabalho (0 não tem: '))
if dados['ctps'] != 0:
   dados['contratação'] = int(input('Ano de contratação: '))
   dados['salario'] = float(input('Salário: R$'))
   dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
   print(f'_ {k} {v}')