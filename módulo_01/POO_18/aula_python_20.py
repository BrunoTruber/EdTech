from typing import AwaitableGenerator


class Pessoa:
    def __init__(self,nome,idade,cpf,telefone):
        self.__nome =nome
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone

class Advogado(Pessoa):
        def __init__(self,nome,idade,cpf,telefone,oab):
            self.__oab = oab

advo= Advogado('bb')
#     # get = pegar, receber
#     def mostrarNome(self):
#         return self.__nome

#     # set = alterar
# pessoa = Pessoa('Bruno',23,'123456765-88','4391206408')

# print(pessoa.mostrarNome())
# listaConvidados = []
# listaConvidados.append(pessoa.mostrarNome())
