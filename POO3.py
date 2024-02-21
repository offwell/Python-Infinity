class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}"
        else:
            return "Quantidade de combustível insuficiente na bomba"
    
    def abastecer_por_litro(self, litros_abastecidos):
        valor_pagar = litros_abastecidos * self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Valor a ser pago: R${valor_pagar:.2f}"
        else:
            return "Quantidade de combustível insuficiente na bomba"
    
    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro
    
    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
    
    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade



bomba = BombaCombustivel("Gasolina", 5.50, 1000)  
print(bomba.abastecer_por_valor(55))  
print(bomba.abastecer_por_litro(20))  
bomba.alterar_valor(6.00)  
print(bomba.abastecer_por_valor(66))  
bomba.alterar_combustivel("Álcool")  
print(bomba.abastecer_por_litro(15))  
bomba.alterar_quantidade_combustivel(1500)  
