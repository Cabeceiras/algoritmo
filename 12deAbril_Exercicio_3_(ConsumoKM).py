'''
3)Um programa que o usuário informe a Km percorrida e a quantidade 
de litros abastecidas, o sistema informe o consumo do veículo.
'''

litros=float(input("Informe com quantos litros o carro foi abastecido: "))
km=float(input("Informe quantos quilomêtros o carro percorreu até a acabar o combustível: "))

consumo=km/litros

print("O carro percorre %2.2f quilomêtro(s) por litro consumido."%(consumo))
