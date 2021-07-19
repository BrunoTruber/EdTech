# exemplos
# del lista[chave]
# lista.pop(chave,'mensagem padrao')
# lista.popitem()

#exercicio 1
aniversario = dict()
while True:
    nome = input('digite um nome de celebridade ou 0 pram sair: ')
    if nome == '0': break
    data = input('digite a data de nascimento da celebridade: ')
    sexo = input('digite o sexo dsa celebridade: ')
    aniversario[nome]= [data, sexo]

for k, v in aniversario.itens:# key - value ->dicionario [key] = value
    print(f'{k}-{v}')


print()
nome = input('digite um nome a sewr pesquisado: ')
print(aniversario.get(nome,'nome nao encontrdo'))



#exercicio 2
jogador ={}
gol_por_partida = []
jogador ['nome'] = input('digite o nome do jogador: ')
total = int(input('digite a qtd de partida '))
for i in range(total):
    gol_por_partida.append(int(input(f'digite a qtd de gols na partida {i+1}')))
jogador['gols'] = gol_por_partida[:]
jogador['total'] = sum(gol_por_partida)

print('*-=-*'*10)
print('nome do jogador:',jogador['nome'])
print('*-=-*'*10)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
print('*-=-*'*10)


#for k, v in enumerate(jogador['gols'])




#exercicio 3
estoque_fixo = {"tomate": 1000, "alface": 500, "batata": 2001, "feijão": 100}
etotal = 0
estoque = dict()

print('*-=-*'*10)
print('SUPERMERCADO DO ZÉ')
print('*-=-*'*10)

produto = input('digite o nome do produto: ')
while produto != 0:
    qtd= int(input('digite a qtd do '))
estoque ={}
total = 0
while True:
    prod = input('diigte um produto para ser adquirido ou fim pra sdair: ')
    if prod == "FIM": break
    if prod in estoque:
        qtd = int(input('digite a qtd deste produto: '))
        if qtd <= estoque[prod][0]:
            preco_unit = estoque[prod][1]
            custo = qtd*preco_unit
            print(f"{prod}: {qtd}  {preco_unit} {custo}")
            estoque[prod][0] -= qtd
            total += custo
        elif estoque [prod][0] == 0:
            print('produto indisponivel')
        else:
            print('qtd nao disponivel')
    else:
        print('produ uinvalido')

print('*-=-*'*10)
print('compras realizaDAs')
for k, v in estoque.items():
    if v[0] != estoque_fixo[k]:
        qtd = estoque_fixo[k] - v[0]
        custo = qtd*v[1]
        print(f"{k}:\t\t{qtd}\tx\tR$ {v[1]:6.2f}\t=\tR$ {custo:4.2f}")
print("*-=-*"*10)
print(f"Valor total da compra: R$ {total:6.2f}")

#exercício 4
def menu():
    while True:
        print("*-=-*"*10)
        print("ESCOLA DO FUTURO!")
        print("*-=-*"*10)
        print(" 0. Sair")
        print(" 1. Exibir lista de alunos com suas notas")
        print(" 2. Inserir aluno e nota")
        print(" 3. Alterar a nota de um aluno")
        print(" 4. Consultar nota de um aluno específico")
        print(" 5. Apagar um aluno da lista")
        print(" 6. Exibir a média da turma")
        print("*-=-*"*10)
        op = input("Digite a opção desejada: ")
        if op == '0':
            break
        if op == '1':
            exibir()
        elif op == '2':
            inserir()
        elif op == '3':
            alterar()
        elif op == '4':
            consultar()
        elif op == '5':
            apagar()
        elif op == '6':
            exibir_media()
        else:
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!")

def exibir():
    if len(alunos) > 0:
        for aluno in alunos:
            print(f"\tNome: {aluno}\t-\tNota: {alunos[aluno]}")
    else:
        print("\tLISTA DE ALUNOS VAZIA!")

def inserir():
    aluno = input("\tDigite o nome do aluno: ")        
    nota = float(input("\tDigite a nota do aluno: "))
    if alunos.get(aluno):
        print("\tAluno já consta na lista. Caso deseje alterar a nota, selecione a opção correta.")
    else:
        alunos.update({aluno:nota})
        print(f"\tAluno {aluno} inserido com sucesso!")

def alterar():
    aluno = input("\tDigite o nome do aluno: ")        
    nota = float(input("\tDigite a nota do aluno: "))
    if (aluno not in alunos):
        print("\tAluno não consta na lista. Caso deseje inserir a nota, selecione a opção correta.")
    else:
        alunos.update({aluno:nota})
        print(f"\tAluno {aluno} alterado com sucesso!")

def consultar():
    aluno = input("\tDigite o nome do aluno: ")
    if (aluno not in alunos):
        print("\tAluno não consta na lista. Caso deseje inserir a nota, selecione a opção correta.")
    else:
        print(f"\tNome: {aluno}\t-\tNota: {alunos[aluno]}")

def apagar():
    aluno = input("\tDigite o nome do aluno: ")
    if (aluno not in alunos):
        print("\tAluno não consta na lista. Caso deseje inserir a nota, selecione a opção correta.")
    else:
        alunos.pop(aluno)
        print(f"\tAluno {aluno} apagado com sucesso!")

def exibir_media():
    soma = 0
    for nota in alunos.values():
        soma += nota
    if len(alunos) > 0:
        media = soma/len(alunos)
    else:
        media = 0.0
    print(f"\tA média da turma é {media:.2f}.")

alunos = dict()
menu()