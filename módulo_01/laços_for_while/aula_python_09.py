#exercicio 1

#Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida 
#imprima essa tabuada. 

n = int(input('Digite qual tabuada você quer ver:'))
for x in range(1,n+1):
    print('='*10)
    print(f'{n} x {x} = {n*x}')
#exercicio 2
#Crie um código em Python para exibir a contagem de dígitos de um número inteiro positivo informado pelo usuário
num = int(input('Digite um número:'))
for x in range(1,num + 1):
    print(f'{x}', end=' ')

#exercicio 3
# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a
# metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
# contratado para desenvolver o programa que monta a tabela de preços de pães, de 1
# até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo 
# abaixo:

preço = float(input('Digite o preço do pão R$:'))
print('Preço do pão:{:.2f}'.format(preço))
print('Panificadora de Pão - Tabela de preço')
for x in range(1,51):
    print('{} - R${:.2f}'.format(x, preço*x))

# exercicio 4
# Crie um código em Python que receba uma lista de nomes informados pelo usuário
# com tamanho indefinido (a lista deve ser encerrada quando o usuário digitar 0) e, na
# sequência, receba um nome para que seja verificado se este consta na lista ou não.
# Observação: ignorar diferenças entre maiúsculas e minúsculas.

listaNomes = []

for c in range(1000):
    nome = str(input('Adicione um nome a lista:')).upper()
    if nome == '0':
        break
    else:
        listaNomes.append(nome)
    print(listaNomes)

buscar = str(input('Busque um nome na lista:')).upper()
if buscar in listaNomes:
    print(f'{buscar} está na lista!')
else:
    print(f'{buscar} não está na lista!')

#exercicio 5
#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
#  Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
#  de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final
#  da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
#  então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
#  a próxima compra. A saída deve ser conforme o exemplo abaixo:
from time import sleep

print('='*30)
print('PARANÁ STORE')
print('='*30)
listaProdutos = []
numero_de_produtos = 1

while True:
    valor = float(input(f'Digite o valor do produto {numero_de_produtos}:'))
    print('='*30)
    numero_de_produtos += 1
    listaProdutos.append(valor)
    if valor == 0: break

Total = sum(listaProdutos)
print(f'TOTAL R$:{Total:.2f} reais')
dinheiro = float(input('Digite o quanto você irá pagar:'))
troco = dinheiro - Total

print('IMPRIMINDO NOTA FISCAL')
sleep(2)

print(f'''
NOTA FISCAL
Total de produtos:{numero_de_produtos}
Valor total R$:{Total:.2f} reais
Dinheiro R$:{dinheiro:.2f} reais
Troco R$:{troco:.2f} reias
''')

#exercicio 6
#Faça um script que peça ao usuário o número de matérias da escola, ou seja,
#um inteiro positivo. Em seguida, ele vai digitando o valor de cada nota, 
#de cada matéria e isso será armazenado numa lista. Ao final, seu script 
#deverá fornecer a média geral do aluno.

materias = int(input('Digite o número de máterias:'))
listaMedia = []

for c in range(1, materias + 1):
    nota = int(input(f'Nota da matéria {c}:'))
    listaMedia.append(nota)

somaMedia = sum(listaMedia)
media = somaMedia / materias
print(f'A média total das notas é:{media:.2f}')

#desafio 1
#(DESAFIO) Desenvolva um código em Python que gere um número aleatório de 1 a 100 e dê ao usuário 10 chances para acertá-lo. A cada tentativa, deve ser impressa a quantidade de tentativas restantes e se o número aleatório é maior ou menor do que o número inserido na tentativa atual. Se o usuário não acertar em 10 tentativas, informe qual o número aleatório. [Dica: use a função randint para gerar o número aleatório]

from random import randint
aleatorio = randint(1,100)
tentativas = 10

while True:
    print('='*20)
    numero = int(input('\033[33mDigite um número:'))
    print('='*20)
    tentativas -= 1
    if numero == aleatorio:
        print('\033[32mPárabens, você acertou!')
        break
    elif tentativas < 1:
        print('\033[31mPoxa, Você perdeu!')
        break
    else:
        if numero < aleatorio:
            print('\033[33mUM POUCO MAIS')
        else:
            print('\033[33mUM POUCO MENOS')
    print(f'\033[33mFaltam {tentativas} tentativas!')

    #exercicio 2
    #(DESAFIO) Escreva um programa que determine todos os números de 4 algarismos que possam ser separados em dois números de dois algarismos que somados e elevando-se a soma ao quadrado obtenha-se o próprio número.

# Exemplo: 3025 = 55 e 55**2 é igual á 3025

for c in range(1000,10000):
    p1 = c // 100
    p2 = c % 100
    if (p1+p2)**2 == c:
        print(c)