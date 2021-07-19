
# lista1 = [4, 3, 2, 1, 0]
# lista2 = ["A", "B", "C"]
# lista3 = [1, 2, "um", "dois"]
# lista4 = [10, 20, [30, 40]]

# lista5 = [10, 20, [30, 40, [50, 60]]]
#índice 2 = [30, 40, [50, 60]]
#índice 2 do índice 2 = [50, 60]


# print(lista1[0]) # Printa apenas o indíce 0 da lista1
# print(lista2[2])
# print(lista3)
# print(lista3[0])
# print(lista3[3])
# soma = lista3[0] + lista3[1] # Soma os valores dos índices indicados
# print(soma)

# print(lista4)
# print(lista4[0])
# print(lista4[1])
# print(lista4[2])
# print(lista4[2][0]) #Printa o indíce 0 da lista que está no indíce 2
# print(lista5[2])
# print(lista5[2][2])
# print(lista5[2][2][0])

# print(lista1)
# lista1[0] = 8
# print(lista1)
# print(lista4)
# lista4[2][1] = 80
# print(lista4)
# lista4[2] = 80
# print(lista4)

# print(len(lista1)) # Exibe o tamanho da lista (quantidade de valores)
# print(len(lista3))
# print(len(lista5))

# var_a = 100
# print(lista1)
# lista1.append("Leo") # Adiciona um novo valor ao final da lista
# print(lista1)
# lista1[0] = "Leo" # Atribui um novo valor ao indíce indicado. Esse valor substitui o original!
# print(lista1)
# lista1[1] = var_a
# print(lista1)

# print(max(lista2)) # Exibe o valor máximo entre os valores da lista
# print(min(lista2)) # Exibe o valor máximo entre os valores da lista
#print(max(lista3)) # Erro - comparando int e str

# print(lista1)
# del lista1[1] # Exclui o valor do índice indicado
# print(lista1)
# lista1.remove(1) # Exclui o valor indicado, não importa o índice que esteja
# print(lista1)
# print(lista3)
# lista3.append("dois")
# print(lista3)
# lista3.append(2)
# print(lista3)
# lista3.remove("dois")
# print(lista3)
# lista3.remove(2)
# print(lista3)

# print(4 in lista1) # Verifica se o valor pedido (4) está em lista1, retorno booleano (True/False)
# print("casa" in lista1) 

# print(lista1)
# print(lista2)
# lista1a = lista1 + lista2 # Concatena duas listas
# print(lista1a)
# lista1b = lista1 * 3 # Repete a lista o número de vezes indicado (3)
# print(lista1b)

# print(lista1)
# print(lista1[1:3]) # Fatiamento - Mostra apenas os valores dos indíces de 1 - 2 (o 3 não é incluso)
# print(lista1[:2]) # Mostra os valores do índice 0 até 1 (o 2 não é incluso)
# print(lista1[2:]) # Mostra os valores a partir do índice 2 (o 2 é incluso)
# print(lista1[:-2])

# lista_r1 = list(range(5)) # Função list() cria uma lista com a função range(), que retorna os valores de 0 até o número específicado (5)
# print(lista_r1)
# lista_r2 = list(range(2,5)) # Retorna os valores de 2 a 5
# print(lista_r2)
# lista_r3 = list(range(-10,13,3)) # Retorna os valores de -10 a 13, incrementando de 3 em 3
# print(lista_r3)

# Criando as funções: 
# "Ensinando" ao programa o que ele deve fazer quando a função for chamada
# Importante lembrar que nesse momento a função não é executada, apenas criada! 
# Para executar, eu preciso chamar a função pelo nome dela no programa 

# def testa_idade(idade=18):
#     print(idade)
#     if idade >= 18:
#        print("Maior de idade\n")
#     else:
#        print("Menor de idade\n")

# def soma_tudo_do_sangue(hema, plaq, leuco):
#     sangue_total = hema + plaq + leuco
#     print("O sangue total é: ", sangue_total)
#     return sangue_total


# sangue = soma_tudo_do_sangue(10, 5, 30) #Armazena na var sangue o que foi retornado pela função chamada
# #print("O sangue total é:", sangue)
# #print(soma_tudo_do_sangue(8, 8, 8)) # Printa o retorno da função
# #soma_tudo_do_sangue(7, 7, 7) # Apenas executa a função.


# print("   SEMANA 1:\n")
# sangue = soma_tudo_do_sangue(10, 5, 30)


# if sangue > 300:
#     print("Cuidado, você vai morrer\n\n")
# else:
#     print("Toma cuidado mesmo assim.\n\n")

# print("   SEMANA 2:\n")
# sangue = soma_tudo_do_sangue(180, 200, 2)


# if sangue > 300:
#     print("Cuidado, você vai morrer\n")
# else:
#     print("Toma cuidado mesmo assim.\n")

# print("   SEMANA 3:\n")
# h = int(input("Digite valor H: "))
# p = int(input("Digite valor P: "))
# l = int(input("Digite valor L: "))

# sangue = soma_tudo_do_sangue(h, p, l)

# if sangue > 300:
#     print("Cuidado, você vai morrer\n")
# else:

# lista1 = [4, 3, 2, 1, 0]
# lista2 = ["A", "B", "C"]
# lista3 = [1, 2, "um", "dois"]
# lista4 = [10, 20, [30, 40]]

# lista5 = [10, 20, [30, 40, [50, 60]]]
#índice 2 = [30, 40, [50, 60]]
#índice 2 do índice 2 = [50, 60]


# print(lista1[0]) # Printa apenas o indíce 0 da lista1
# print(lista2[2])
# print(lista3)
# print(lista3[0])
# print(lista3[3])
# soma = lista3[0] + lista3[1] # Soma os valores dos índices indicados
# print(soma)

# print(lista4)
# print(lista4[0])
# print(lista4[1])
# print(lista4[2])
# print(lista4[2][0]) #Printa o indíce 0 da lista que está no indíce 2
# print(lista5[2])
# print(lista5[2][2])
# print(lista5[2][2][0])

# print(lista1)
# lista1[0] = 8
# print(lista1)
# print(lista4)
# lista4[2][1] = 80
# print(lista4)
# lista4[2] = 80
# print(lista4)

# print(len(lista1)) # Exibe o tamanho da lista (quantidade de valores)
# print(len(lista3))
# print(len(lista5))

# var_a = 100
# print(lista1)
# lista1.append("Leo") # Adiciona um novo valor ao final da lista
# print(lista1)
# lista1[0] = "Leo" # Atribui um novo valor ao indíce indicado. Esse valor substitui o original!
# print(lista1)
# lista1[1] = var_a
# print(lista1)

# print(max(lista2)) # Exibe o valor máximo entre os valores da lista
# print(min(lista2)) # Exibe o valor máximo entre os valores da lista
#print(max(lista3)) # Erro - comparando int e str

# print(lista1)
# del lista1[1] # Exclui o valor do índice indicado
# print(lista1)
# lista1.remove(1) # Exclui o valor indicado, não importa o índice que esteja
# print(lista1)
# print(lista3)
# lista3.append("dois")
# print(lista3)
# lista3.append(2)
# print(lista3)
# lista3.remove("dois")
# print(lista3)
# lista3.remove(2)
# print(lista3)

# print(4 in lista1) # Verifica se o valor pedido (4) está em lista1, retorno booleano (True/False)
# print("casa" in lista1) 

# print(lista1)
# print(lista2)
# lista1a = lista1 + lista2 # Concatena duas listas
# print(lista1a)
# lista1b = lista1 * 3 # Repete a lista o número de vezes indicado (3)
# print(lista1b)

# print(lista1)
# print(lista1[1:3]) # Fatiamento - Mostra apenas os valores dos indíces de 1 - 2 (o 3 não é incluso)
# print(lista1[:2]) # Mostra os valores do índice 0 até 1 (o 2 não é incluso)
# print(lista1[2:]) # Mostra os valores a partir do índice 2 (o 2 é incluso)
# print(lista1[:-2])

# lista_r1 = list(range(5)) # Função list() cria uma lista com a função range(), que retorna os valores de 0 até o número específicado (5)
# print(lista_r1)
# lista_r2 = list(range(2,5)) # Retorna os valores de 2 a 5
# print(lista_r2)
# lista_r3 = list(range(-10,13,3)) # Retorna os valores de -10 a 13, incrementando de 3 em 3
# print(lista_r3)

# Criando as funções: 
# "Ensinando" ao programa o que ele deve fazer quando a função for chamada
# Importante lembrar que nesse momento a função não é executada, apenas criada! 
# Para executar, eu preciso chamar a função pelo nome dela no programa 

# def testa_idade(idade=18):
#     print(idade)
#     if idade >= 18:
#        print("Maior de idade\n")
#     else:
#        print("Menor de idade\n")

# def soma_tudo_do_sangue(hema, plaq, leuco):
#     sangue_total = hema + plaq + leuco
#     print("O sangue total é: ", sangue_total)
#     return sangue_total


# sangue = soma_tudo_do_sangue(10, 5, 30) #Armazena na var sangue o que foi retornado pela função chamada
#print("O sangue total é:", sangue)
#print(soma_tudo_do_sangue(8, 8, 8)) # Printa o retorno da função
#soma_tudo_do_sangue(7, 7, 7) # Apenas executa a função.


# print("   SEMANA 1:\n")
# sangue = soma_tudo_do_sangue(10, 5, 30)


# if sangue > 300:
#     print("Cuidado, você vai morrer\n\n")
# else:
#     print("Toma cuidado mesmo assim.\n\n")

# print("   SEMANA 2:\n")
# sangue = soma_tudo_do_sangue(180, 200, 2)


# if sangue > 300:
#     print("Cuidado, você vai morrer\n")
# else:
#     print("Toma cuidado mesmo assim.\n")

# print("   SEMANA 3:\n")
# h = int(input("Digite valor H: "))
# p = int(input("Digite valor P: "))
# l = int(input("Digite valor L: "))

# sangue = soma_tudo_do_sangue(h, p, l)

# if sangue > 300:
#     print("Cuidado, você vai morrer\n")
# else:
#     print("Toma cuidado mesmo assim.\n")