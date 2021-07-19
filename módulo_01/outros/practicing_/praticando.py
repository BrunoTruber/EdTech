# lista = [5,7,2,9,4,1,3]
# print('tamanho da lista:',len(lista))
# print('maior valor da lista:',max(lista))
# print('menor valor daa lista:',min(lista))
# print('soma de todos os valores da listas:',sum(lista))
# lista.sort()
# print('ordem crescente:',lista)
# lista.reverse()
# print('ordem decrescente:',lista)


# #forca
# import random
# lista = input('digite uma palavra: ')
# lista = (lista.strip()).split(' ')

# if len(lista) == 1:
#     palavra = lista[0].upper()
# else:
#     palavra = random.choice(lista).upper()

# palavra_forca = ['_' for i in palavra]
# chance = 0

# print('a palavra é: ',end=' ')
# print('        '.join(palavra_forca))

# maximo = len(palavra)+ 6

# for i in range(maximo):
#     if palavra_forca.count('_')== 0 or chance == 6 : break
#     letra = input('digite uma letra: ').upper()
#     if letra in palavra_forca:
#         print('voce esta letra antes. A palavra é: ',end=' ')
#         print(' '.join(palavra_forca))
#         continue
#     if letra in palavra:
#         print('a palavra é: ',end=' ')
#         for n in range(len(palavra)):
#             if letra == palavra[n]:
#                 del palavra_forca[n]
#                 palavra_forca.insert(n,letra)
#             print(' '.join(palavra_forca))
#     else:
#         chance += 1
#         if chance != 6:
#             print('voce errou pela' + str(chance) + 'vez. Tente novamente!')

# if palavra_forca.count('_') == 0:
#     print('parabens! Voce acertou')
# else:
#     print('voce errou pela 6 vez. Voce perdeu')

# # perguntas para um suspeito
# r1 = int(input('telefonou para a vitima? [1]sim [0] nao: '))
# r2 = int(input('esteve no local do crime? [1]sim [0] nao: '))
# r3 = int(input('mora perto da vitima? [1]sim [0] nao: '))
# r4 = int(input('devia para a vitima? [1]sim [0] nao: '))
# r5 = int(input('ja trabalhou com a vitima? [1]sim [0] nao: '))

# lista = [r1,r2,r3,r4,r5]

# if sum(lista)== 2:
#     print('suspeito')
# elif sum(lista)== 3 and sum(lista) ==4:
#     print('cumplice')
# elif sum(lista)== 5:
#     print('assassino')
# else:
#     print('inocente')

#exercicio 2 e exercicio 5
def fgv(frase='bruno'):
   # frase = input('digite uma frase: ')
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
    print(f'vogais:{vogais}')
    print(f'quantidade: {cont}')
    print(f'frase sem vogais: {recebe}')
fgv()


# lista_pares = []
# numeros = int(input("Até qual número? "))
# for n in range(1,numeros,2):
#     print(n+1)