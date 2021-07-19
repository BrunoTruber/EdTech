#exercício 1
# "Faça um Programa que leia três números inteiros, 
# em seguida mostre o maior e o menor deles

num1= 2
num2= 4
num3= 6
if num1 <= 2:
   print(num1,'menor de todos')
   if num2 >= 4:
     print(num2)
     if num3 >= 6:
       print(num3,'maior de todos')


#exercício 2
#Faça um programa que peça dois números e imprima o maior deles.

num1= float(input('digite um numero: '))
num2= float(input('digite um numero: '))
if num1 > num2:
  print(num1,'é maior')
elif num1 < num2:
    print(num2,'é maior')
else :
  print('São iguais')


#exercicio 3
#Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

num1= float(input('digite um numero: '))
if num1 > 0:
  print('positivo')
elif num1 < 0:
    print('negativo')
else:
  print('Caractere invalido!')

#exercício4
#Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

nome=input('digite M ou F para descrever seu genero: ')
if nome.upper()=='M':
  print('Genero masculino')
elif nome.upper()== 'F':
    print('Genero feminino')
else:
  print('Caractere invalido')


#exercício 5
#Crie um programa em Python que peça a nota do aluno, que deve ser um float entre 0.00 e 10.0

nota= float(input('digite a nota do aluno: '))
if nota < 6:
  print('F')
elif nota >= 6 and nota <= 7:
  print('D')
elif nota > 7 and nota <= 8:
  print('C')
elif nota > 8 and nota <= 9:
  print('B')
elif nota > 9 and nota <= 10:
  print('A')
else:
  print('Nota invalida')

#exercício 6
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letras= input('digite uma letra: ')
if letras.upper()== 'A':
  print("Vogal")
elif letras.upper()== 'E':
    print('Vogal')
elif letras.upper()== 'I':
    print('Vogal')
elif letras.upper()== 'O':
  print('Vogal')
elif letras.upper()== 'U':
  print('Vogal')
else:
  print('consoante')

#forma 2
letra= input('digite uma letra: ').upper()

if letra != 'A' and letra != 'E' and letra!= 'I' and letra!= 'O' and letra != 'U':
  print ('Consoante')
else:
  print('Vogal')

# projeto 1
# Escreva um programa que receba uma string digitada pelo usuário;
# Caso a string seja "medieval", exiba no console "espada";
# Caso contrário, se a string for "futurista", exiba no console "sabre de luz";
# Caso contrário, exiba no console "Tente novamente"

armas=input('Digite o nome da arma: ')
if armas.upper()=='MEDIEVAL':
  print('ESPADA')
elif armas.upper()=='FUTURISTA':
  print('SABRE DE LUZ')
else:
  print('Tente novamente')

#continuação do projeto 1
# Escreva um programa que receba um ataque de espada ou sabre digitada pelo usuário;
# Caso o ataque seja "espada", exiba no console "VOCÊ AINDA NÃO MATOU O CHEFÃO";
# Caso contrário, se o ataque for "sabre", exiba no console "VOCÊ DERROTOU O CHEFÃO COM O SABRE DE LUZ";
# Caso contrário, exiba no console "ATAQUE NOVAMENTE"

print('Escolha sua arma: Sabre ou espada!')
ataque=input('Com qual arma você quer atacar: ')
if ataque.lower()=='espada':
  print('VOCÊ AINDA NÃO MATOU O CHEFÃO')
elif ataque.lower() == 'sabre':
  print('VOCÊ DERROTOU O CHEFÃO COM O SABRE DE LUZ')
else:
  print('ATAQUE NOVAMENTE!')

#DESAFIO 1
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento."

salario1 = float(input("Valor do salario: "))
reajuste= input('Porcentagem do rejuste: ')
reajusteescrito = (float(reajuste.replace("%", ""))/100)+1
novosalario = salario1 * reajusteescrito
print(f'Salario antes do reajuste {salario1:.2f}')
#print('Porcentagem do reajuste',reajuste)
print(f'Valor do aumento {novosalario-salario1:.2f}')
print(f'Seu novo salario R$ {novosalario:.2f}')

#caixa eletronico
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor= int(input('digite um valor para saque: '))
if valor >= 10 and valor <= 600:
  notas_100= valor // 100
  valor = valor % 100

  notas_50= valor // 50
  valor= valor % 50

  notas_10= valor // 10
  valor= valor % 10

  notas_5= valor // 5
  valor= valor % 5

  notas_1= valor
  
  print(f'Notas de 100: {notas_100}')
  print(f'Notas de 50: {notas_50}')
  print(f'Notas de 10: {notas_10}')
  print(f'Notas de 5: {notas_5}')
  print(f'Notas de 1: {notas_1}')
else:
  print('invalido')


#exercício 1
num1= 2
num2= 4
num3= 6
if num1 <= 2:
   print(num1,'menor de todos')
   if num2 >= 4:
     print(num2)
     if num3 >= 6:
       print(num3,'maior de todos')


#exercício 2
num1= float(input('digite um numero: '))
num2= float(input('digite um numero: '))
if num1 > num2:
  print(num1,'é maior')
elif num1 < num2:
    print(num2,'é maior')
else :
  print('São iguais')


#exercicio 3
num1= float(input('digite um numero: '))
if num1 > 0:
  print('positivo')
elif num1 < 0:
    print('negativo')
else:
  print('Caractere invalido!')

#exercício4
nome=input('digite M ou F para descrever seu genero: ')
if nome.upper()=='M':
  print('Genero masculino')
elif nome.upper()== 'F':
    print('Genero feminino')
else:
  print('Caractere invalido')


#exercício 5
nota= float(input('digite a nota do aluno: '))
if nota < 6:
  print('F')
elif nota >= 6 and nota <= 7:
  print('D')
elif nota > 7 and nota <= 8:
  print('C')
elif nota > 8 and nota <= 9:
  print('B')
elif nota > 9 and nota <= 10:
  print('A')
else:
  print('Nota invalida')

#exercício 6
letras= input('digite uma letra: ')
if letras.upper()== 'A':
  print("Vogal")
elif letras.upper()== 'E':
    print('Vogal')
elif letras.upper()== 'I':
    print('Vogal')
elif letras.upper()== 'O':
  print('Vogal')
elif letras.upper()== 'U':
  print('Vogal')
else:
  print('consoante')

#forma 2
letra= input('digite uma letra: ').upper()

if letra != 'A' and letra != 'E' and letra!= 'I' and letra!= 'O' and letra != 'U':
  print ('Consoante')
else:
  print('Vogal')

# projeto 1
armas=input('Digite o nome da arma: ')
if armas.upper()=='MEDIEVAL':
  print('ESPADA')
elif armas.upper()=='FUTURISTA':
  print('SABRE DE LUZ')
else:
  print('Tente novamente')

#continuação do projeto 1
print('Escolha sua arma: Sabre ou espada!')
ataque=input('Com qual arma você quer atacar: ')
if ataque.lower()=='espada':
  print('VOCÊ AINDA NÃO MATOU O CHEFÃO')
elif ataque.lower() == 'sabre':
  print('VOCÊ DERROTOU O CHEFÃO COM O SABRE DE LUZ')
else:
  print('ATAQUE NOVAMENTE!')

#DESAFIO 1
salario1 = float(input("Valor do salario: "))
reajuste= input('Porcentagem do rejuste: ')
reajusteescrito = (float(reajuste.replace("%", ""))/100)+1
novosalario = salario1 * reajusteescrito
print(f'Salario antes do reajuste {salario1:.2f}')
#print('Porcentagem do reajuste',reajuste)
print(f'Valor do aumento {novosalario-salario1:.2f}')
print(f'Seu novo salario R$ {novosalario:.2f}')

#caixa eletronico
valor= int(input('digite um valor para saque: '))
if valor >= 10 and valor <= 600:
  notas_100= valor // 100
  valor = valor % 100

  notas_50= valor // 50
  valor= valor % 50

  notas_10= valor // 10
  valor= valor % 10

  notas_5= valor // 5
  valor= valor % 5

  notas_1= valor
  
  print(f'Notas de 100: {notas_100}')
  print(f'Notas de 50: {notas_50}')
  print(f'Notas de 10: {notas_10}')
  print(f'Notas de 5: {notas_5}')
  print(f'Notas de 1: {notas_1}')
else:
  print('invalido')


