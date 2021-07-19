# Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# tamanho da lista.
# maior valor da lista.
# menor valor da lista.
# soma de todos os elementos da lista.
# lista em ordem crescente.
# lista em ordem decrescente. 
lista = [5, 7, 2, 9, 4, 1, 3] 
print('Tamanho da lista:',len(lista))
print('Maior valor da lista:',max(lista))
print('Menor valor da lista:', min(lista))
print('Soma de todos os valores da lista:', sum(lista))
lista.sort()
print('Ordem crescente:',lista)
lista.reverse()
print('Ordem decrescente:',lista)

#exercicio 2

# Faça um jogo da forca. O programa terá uma lista de palavras lidas de
# um arquivo texto e escolherá uma aleatoriamente. O jogador poderá
# errar 6 vezes antes de ser enforcado.  

import random
lista = input('Digite uma lista de palavras separadas por espaço:')
lista = (lista.strip()).split(' ')

#indice = random.randrange(0,len(lista))
#palavra = lista[indice]
if len(lista) == 1:
    palavra = lista[0].upper()
else:
    palavra = random.choice(lista).upper()

palavra_forca = ['_' for i in palavra]
# palavra_forca = ['_','_','_','_','_','_','_']
# " ".join(palavra_forca) =>  _ _ _ _ _ _ _
chance = 0

print('A palavra é: ',end=' ')
print('     '.join(palavra_forca))

maximo = len(palavra) + 6 # comprimento da palavra + 6 chances para errar
# for i in range(13):

for i in range(maximo):
    # verificar condições de parada: GANHOU ou PERDEU
    if palavra_forca.count('_') == 0 or chance == 6: break
    letra = input('Digite uma letra: ').upper()
    if letra in palavra_forca:
        print('Você já digitou esta letra antes. A palavra é: ', end=' ')
        print(' '.join(palavra_forca))
        continue
    if letra in palavra:
        print('A palavra é:', end=' ')
        for n in range(len(palavra)):
            if letra == palavra[n]:
                del palavra_forca[n]
                palavra_forca.insert(n, letra)
                 # palavra_forca[n] = letra
        print(' '.join(palavra_forca))
    else:
        chance += 1
        if chance != 6:
            print('Você errou pela' + str(chance) + ' vez.Tente novamente!')

if palavra_forca.count('_') == 0:
    print('Parabéns! Você acertou a palavra!')
else:
    print('Você errou pela 6° vez\nFORCA! VOCÊ PERDEU')

    #exercicio 3
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"  
# O programa deve no final emitir uma classificação sobre a participação da pessoa  no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

r1 = int(input('Telefonou para a vítima? [1] Sim [0] Não:'))
r2 = int(input('Esteve no local co crime? [1] Sim [0] Não:'))
r3 = int(input('Mora perto da vítima? [1] Sim [0] Não:'))
r4 = int(input('Devia para a vítima? [1] Sim [0] Não:'))
r5 = int(input('Já trabalhou com a vítima? [1] Sim [0] Não:'))

lista = [r1,r2,r3,r4,r5]

if sum(lista) == 2:
    print('SENTENÇA:SUSPEITO!')
elif sum(lista) == 3 and sum(lista) == 4:
    print('SENTENÇA:CÚMPLICE!')
elif sum(lista) == 5:
    print('SENTENÇA:ASSASSINO!')
else:
    print('SENTENÇA:INOCENTE!')

#exercicio 4
#Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco),
#   conte quantas vezes aparece uma vogal.
# cont = 0
# frase = str(input('Digite uma frase:'))
# for x in range(len(frase)):
#     print(x+1)
#     cont +=1

frase = input("Digite uma frase: ")
vogais = []

cont = 0

for item in frase:
    if item in 'aeiou':
        # num_vogais += 1
        vogais.append(item)
        cont += 1
print(f'Vogais:{vogais}')
print(f'Quantidade:{cont}')

#exercicio 5
#Desenvolva um código que pergunte um número n para o usuário  e exiba todos seus divisores.
#  Caso seja um número primo, o programa ainda deve informar que se trata de um número primo! 
cont = 0
n = int(input('Digite um número:'))
for x in range(1,n+1):
    if n % x == 0:
        print('{} é divisivel por:{}'.format(n, n/x))
        cont += 1
if cont == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')

#exercicio 6
#Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal. 

frase = input("Digite uma frase: ")
consoantes = []
cont = 0

for item in frase:
    if item not in 'aeiou':
        consoantes.append(item)
        cont += 1
print(f'Consoantes:{consoantes}')
print(f'Quantidade:{cont}')