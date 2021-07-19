# revisao função

def somar(numA,numB,operador):
    print('o primeiro numero é:',numA)
    print(f'o segundo numero é:{numB}')
    resultado = ''
    if operador == '+':
        resultado = numA + numB
    elif operador == '-':
        resultado = numA - numB
    elif operador == '*':
        resultado = numA * numB
    elif operador == '/':
        resultado = numA/numB
    else:
        print('invalido')
    print('resultao é:',resultado)
num1 = float(input('digite um numero: '))
num2 = float(input('digite um numero: '))
op = input('digite o operador: ')
somar(num1,num2,op)
    
#exercicio 1
# Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6,
# 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes
# aos quadrados desses números.
# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}

lista = [1, 4, 5, 6, 7, 9]
dicionario = {}

for i in lista:
    dicionario[i] = i**2
print(dicionario)

#exercicio 2
# Crie um dicionário em que suas chaves correspondem a números
# inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

dicionario = {}
for i in range(1, 11):
    dicionario[i] = i**2
print(dicionario)

#exercicio 3
# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo sa estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado

qtdAlunos = int(input("Digite a quantidade de alunos: "))
mediaAlunos = {
    "nome": [],
    "media": [],
    "situacao": []
}

for i in range(qtdAlunos):
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média do aluno: "))
    situacao = ""
    if media >= 7:
        situacao = "Aprovado"
    elif 5 > media <= 6.9:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    mediaAlunos["nome"].append(nome)
    mediaAlunos["media"].append(media)
    mediaAlunos["situacao"].append(situacao)

print(mediaAlunos)

#exercicio 4
# Crie um programa em que 4 jogadores, joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado. Dicas: procure
# sobre a função randint(), sleep() e itemgetter da bliblioteca operator.
import time
import random
import operator
resultados = []
for i in range(1, 5):
    resultadoDado = random.randint(1, 6)
    print(f'Jogador {i} jogou o dado..')
    time.sleep(random.uniform(0.0, 1.0))
    print(f'O resultado é...')
    time.sleep(random.uniform(0.0, 1.0))
    print(f'É...')
    time.sleep(random.uniform(0.0, 1.0))
    print(f'O jogador {i} tirou {resultadoDado} no dado.')
    resultados.append((i, resultadoDado))
    time.sleep(2)
resultadoRanking = dict(sorted(resultados, key=operator.itemgetter(1)))
print(resultadoRanking)

#exercicio 5
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0,
# o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente , além da idade, com quantos anos a pessoa vai se aposentar.
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

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
