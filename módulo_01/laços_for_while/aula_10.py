#revisao for
# lista =[1]
# for a in range(50):
#     lista.append(a)
#     #print(lista) printa o a cada vez que repete
# print(lista) # printa uma vez só
#lista =[]
# qtd = int(input('digite uma qtd: '))
# for a in range(qtd):
#     lista.append(input('digite algo: '))
#     print(lista)
# senha = '123456'
# entrada= input('digite uma senha: ')
# while entrada != senha:
#     print('erro')
#     entrada= input('digite uma senha: ')
# else:
#     entrada == senha
#     print('liberou')

#exercicio 1
# Crie um laço while que vai pedir para o usuário dois números e faça a soma dos dois. Enquanto a soma não for 50, ele deve continuar repetindo.
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
soma = n1+n2
while soma != 50:
    print('AINDA NÃO!')
    n1 = int(input('Digite novamente outro número:'))
    n2 = int(input('Digite novamente outro número:'))
    soma = n1+n2
print('Conseguiu!')

#exercicio 2
#
# Exercício 1 - Escreva um programa que pede a senha ao usuário, e só sai do
# looping quando digitarem corretamente a senha. 

senha = "9856321"

digitada = input("Digite sua senha: ")
while digitada != senha:
    print("Senha incorreta, digite novamente!")
    digitada = input("Digite sua senha: ")
print(f'Você digitou a senha correta!')

#exercicio 3
"""Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura em
centímetros.  Encontre o aluno mais alto e o mais baixo. Mostre o número do
aluno mais alto e o número do aluno mais baixo, junto com suas alturas. """

numero = []
altura = []
conjuntos = 0
maisAlto = 0
maisBaixo = 0
while conjuntos < 10:
    al = int(input("Digite a altura em centimetros: "))
    if conjuntos == 0:
        maisAlto = al
        maisBaixo = al
    altura.append(al)
    numero.append(len(numero) + 1)
    conjuntos += 1
    if al > maisAlto:
        maisAlto = al
    if al < maisBaixo:
        maisBaixo = al
indexAlto = altura.index(maisAlto)
indexBaixo = altura.index(maisBaixo)

print(
    f'O aluno mais alto é: Número: {numero[indexAlto]} Altura: {altura[indexAlto]}cm')
print(
    f'O aluno mais baixo é: Número: {numero[indexBaixo]} Altura: {altura[indexBaixo]}cm')

#exercicio 4
opcoes = [1, 2, 3, 5, 6]
nomes = ["Jose", "João", "Pedro", "Voto Nulo", "Voto em Branco"]
votos = [0, 0, 0, 0, 0]  # Armazena votos em lista, todos iniciados com 0.

while True:
    print("Escolha sua opção de voto, ou digite 0 para sair: ")
    for op in range(len(opcoes)):
        print(f'{opcoes[op]} - {nomes[op]}')
    voto = int(input("Digite o número do seu voto: "))
    if voto != 0 and voto in opcoes:
        indexVoto = opcoes.index(voto)
        votos[indexVoto] += 1
    else:
        print("Votação encerrada.")
        break
for op in range(len(opcoes)):
    print(f'{nomes[op]} - {votos[op]} votos')
print(f'Porcentagem de votos nulos sobre o total: {votos[3]/sum(votos)*100}%')
print(
    f'Porcentagem de votos em branco sobre o total: {votos[4]/sum(votos)*100}%')

#exercicio 5
""" Codifique um jogo da FORCA. A pessoa digita uma palavra e tem que acertar a 
palavra digitada. """

palavra = input("Digite a palavra do jogo")
palavraOculta = ""
tentativas = []
for letra in palavra:
    palavraOculta += "_ "

while "_" in palavraOculta:
    print(f' Palavra a ser acertada: {palavraOculta} ')
    palpite = input("Digite uma letra para tentar completar a palavra: ")
    
# while palpite in tentativas:

