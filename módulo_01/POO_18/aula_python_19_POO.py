class bombaCombustivel:
    def __init__(self,tipoCombustivel,valorLitro,quantiddeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantiddeCombustivel

    def abastecerPorValor(self,valor):
        temp = valor / self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - temp)
        return temp

    def abastecerPorLitro(self,qtd):
        temp = qtd * self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - qtd)
        return temp

    def alterarValor(self,valor):
        self.valorLitro = valor

    def alterarCombustivel(self, combustivel):
        self.tipoCombustivel = combustivel

    def alterarQuantidadeCombustivel(self, quantidade):
        self.quantidadeCombustivel = quantidade


gasolina = bombaCombustivel('gasolina',6.15, 500)
print(vars(gasolina))
gasolina.alterarValor(6.11)
print(vars(gasolina))
gasolina.alterarCombustivel('gaso supra')
print(vars(gasolina))
gasolina.alterarQuantidadeCombustivel(1000)
print(vars(gasolina))

litros = 50
print(f'o valor a ser pago para abastecer {litros} é R$ {gasolina.abastecerPorLitro(50):.2f}')
# gasolina = bombaCombustivel()
# alcool = bombaCombustivel()

#a = input('digite o combustivel: ')