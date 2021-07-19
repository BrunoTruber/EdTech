lista_contatos=[['Fulano','0988-0987'],('beltrano','6545-7878'),('sicrano','12345-4321')]
lista_contatos[0][0]= 'caramba'
print(lista_contatos)

#exemplos

lista1 = [1, 2, 3, "String", "String2"]
tupla1 = ("Nome","123-456")
lista3 = [("Nome","123-456"), 2, 3, "String", "String2"] # Coloquei a tupla dentro da lista, como um dos elementos dela


# Criando lista com tuplas
lista_contatos = [("Ana Paula","123-456"),("Joao","456-789"),("Fabricio","444-777"),("Ricardo","777-888"),("Bruno","999-888")]
print(len(lista_contatos))
print(type(lista_contatos))
print(lista_contatos)
print(lista_contatos[0])
print(lista_contatos[0][0])
print()

# Criando um dicionário a partir da lista acima com a função dict()
contatos = dict(lista_contatos) # dicionario = dict(lista_a_ser_convertida)
print(contatos)
print("Type de contatos:")
print(type(contatos))
print()

# Acessando um valor dentro de um dicionário
print('Acessando o valor da chave "Ana Paula"')
print(contatos.get("Ana Paula"))
print(contatos["Ana Paula"])

# print(contatos["Eurico"]) # KeyError - A chave não existe

print(contatos.get("Eurico","Nome não encontrado")) # Retorna um valor padrão caso a chave não seja encontrada

nome = input("Digite o nome: ") # Recebendo uma entrada para procurar o valor
print(contatos.get(nome,"Nome não encontrado")) 


#Criando um dicionario "na mão"


dicionario_contatos = {"Alexandre":"555-444", "Talita":"111-222", "Nadja":"666-333"}
print(dicionario_contatos)
print(len(dicionario_contatos))


telefones = [("Pedro", "1245-1250"), ("Ricardo", "536363"),
             ("Pedro", "124212"), ("Fernando", "15155465"),
             ("Eduardo", "22352235")]
print(telefones)
contatos = dict(telefones)
print(contatos)
print(contatos.get("Pedro"))

vingadores = {
    "Chris Evans": "Capitão América",
    "Mark Ruffalo": "Hulk",
    "Tom Hiddleton": "Loki",
    "Chris Hemworth": "Thor",
    "Robert Downey Jr": "Homem de Ferro",
    "Scarlett Johansson": "Viúva Negra"
}
nome = input("Digite o nome do ator")
print(vingadores.get("Chris Evans"))
print(vingadores.get(nome, "O nome não existe"))