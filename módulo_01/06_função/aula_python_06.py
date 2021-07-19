#exercicio 1
# Faça um programa, com uma função que necessite de três argumentos,
#  e que forneça a soma desses três argumentos
def soma(a,b,c):
  return a+b+c
f = soma(2,2,2) 
print(f)

#exercicio 2
# Faça um programa, com uma função que necessite de um
#  argumento. A função retorna o valor de caractere ‘P’,
#   se seu argumento for positivo
# , ‘N’, se seu argumento for negativo e ‘0’ se for 0.
def funcao(aa):
  if aa > 0:
    print('positivo')
  elif aa < 0:
    print('negativo')
  elif aa == 0:
    print('é igual a',0)
  return aa
aa = int(input('digite: '))
aa = funcao(aa)

#exercicio 3
# Faça um programa com uma função chamada somaImposto.
#  A função possui dois parâmetros formais: taxaImposto, 
#  que é a quantia de imposto sobre vendas expressa em 
#  porcentagem e custo, que é o custo de um item antes do 
#  imposto. A função “altera” o valor de custo para incluir
#   o imposto sobre vendas.
def somaImposto(taxaImposto,custo):
  custototal = (custo * taxaImposto) / 100 + custo
  return custototal
taxaImposto= float(input('digite a porcentagem do imposto: '))
custo= float(input('digte o valor do custo: '))
custototal= somaImposto(taxaImposto,custo)
print(custototal)

#exercicio 4
# Faça um programa que calcule o salário de um colaborador 
# na empresa XYZ. O salário é pago conforme a quantidade
#  de horas trabalhadas. Quando um funcionário trabalha
#   mais de 40 horas ele recebe um adicional de 1.5 
# nas horas extras trabalhadas.
def calcular_pagamento(qtd_horas,valor_hora):
  horas = float(qtd_horas)
  taxa  = float(valor_hora)
  if horas <= 40:
    salario = horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario

str_horas = input('digite as horas: ')
str_taxa = input('digite a taxa: ')
total_salario = calcular_pagamento(str_horas,str_taxa)
print('tota de rendimentos',total_salario)

#exercicio 5
# Escreva uma função que, dado um número nota 
# representando a nota de um estudante, converte o 
# valor de nota 
# para um conceito (A, B, C, D, E e F).
def notas(aa):
  if aa >= 9:
    print('A')
  elif aa >= 8.0:
    print('B')
  elif aa >= 7.0:
    print('C')
  elif aa >= 6.0:
    print('D')
  elif aa <= 4.0:
    print('F')
  else:
    print('invalido')

qq= float(input('digite a nota: '))
total= notas(qq)

#exercicio 6
# Escreva uma função que recebe dois parâmetros e 
# imprime o menor dos dois. Se eles forem iguais, 
# imprima que eles são iguais.
def soma(num1,num2):
   #num1=
   #num2=
  if num1 < num2:
    print('num1 é menor')
  elif num2 < num1:
    print('num2 é menor')
  else:
    print('São iguais')

num1=float(input('digite num1: '))
num2=float(input('digite num2: '))
soma(num1,num2)

#exercicio 7
# Faça um programa que calcule através de uma função o IMC 
# de uma pessoa que tenha 1,68 e pese 75kg.
def imc(peso,altura):
   # peso = 75
   # altura=1.68
    IMC = peso/(altura **2)
    print('imc é',IMC)
p= float(input('digite o peso: '))
a = float(input('digite a altura: '))
total= imc(p,a)

#exercicio 8
def testa_idade():
  idade= 30
  if idade >= 18:
    print('maior de idade')
  else:
    print('menor de idade')
testa_idade()

# exemplo listas
lista1 = [1,2,3]
lista2 = [1,'um','dois','tres']
lista3 = [4,5,6]
lista4 = [7,8,9,[10,11,12]]
lista5 = [13,14,15,[16,17,18,[19,20,21]]]

'''''''''praticando sem olhar'''''''''
#exercicio 1
def soma(a,b,c):
  return a+b+c
f = soma(2,2,2) 
print(f)

#exercicio 2
def funcao(aa):
  if aa > 0:
    print('positivo')
  elif aa < 0:
    print('negativo')
  elif aa == 0:
    print('é igual a',0)
  return aa
aa = int(input('digite: '))
aa = funcao(aa)

#exercicio 3
def somaImposto(taxaImposto,custo):
  custototal = (custo * taxaImposto) / 100 + custo
  return custototal
taxaImposto= float(input('digite a porcentagem do imposto: '))
custo= float(input('digte o valor do custo: '))
custototal= somaImposto(taxaImposto,custo)
print(custototal)

#exercicio 4
def calcular_pagamento(qtd_horas,valor_hora):
  horas = float(qtd_horas)
  taxa  = float(valor_hora)
  if horas <= 40:
    salario = horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario
#exercicio 5
str_horas = input('digite as horas: ')
str_taxa = input('digite a taxa: ')
total_salario = calcular_pagamento(str_horas,str_taxa)
print('tota de rendimentos',total_salario)

#exercicio 6
def notas(aa):
  if aa >= 9:
    print('A')
  elif aa >= 8.0:
    print('B')
  elif aa >= 7.0:
    print('C')
  elif aa >= 6.0:
    print('D')
  elif aa <= 4.0:
    print('F')
  else:
    print('invalido')

qq= float(input('digite a nota: '))
total= notas(qq)

#exercicio 7
def soma(num1,num2):
   #num1=
   #num2=
  if num1 < num2:
    print('num1 é menor')
  elif num2 < num1:
    print('num2 é menor')
  else:
    print('São iguais')

num1=float(input('digite num1: '))
num2=float(input('digite num2: '))
soma(num1,num2)

#exercicio 8
def imc(peso,altura):
   # peso = 75
   # altura=1.68
    IMC = peso/(altura **2)
    print('imc é',IMC)
p= float(input('digite o peso: '))
a = float(input('digite a altura: '))
total= imc(p,a)

#exercicio 9
def testa_idade():
  idade= 30
  if idade >= 18:
    print('maior de idade')
  else:
    print('menor de idade')
testa_idade()

# exemplo listas
lista1 = [1,2,3]
lista2 = [1,'um','dois','tres']
lista3 = [4,5,6]
lista4 = [7,8,9,[10,11,12]]
lista5 = [13,14,15,[16,17,18,[19,20,21]]]
print(lista1[0]+lista2[0])