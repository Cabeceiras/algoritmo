print()
print("Atenção. Este programa, somente pode ser usado logo após o tanque ser abastecido.")
print()


print("Primeiro abastecimento (de dois) para efetuar cálculo do consumo médio.")
print("***********************************************************************")
print()
print()
km=int(input("Digite os kilomêtros (usando um número inteiro) que marcam no odômetro do carro: "))
litro=int(input("Digite quantos litros (com um número inteiro) foram usados para completar o tanque: "))
print()
print()
print("Segundo abastecimento (último) para efetuar cálculo do consumo médio.")
print("*********************************************************************")
print()
km2=int(input("Digite os kilomêtros (usando um número inteiro) que marcam no odômetro do carro: "))
litro2=int(input("Digite quantos litros (com um número inteiro) foram usados para completar o tanque: "))

consumomedio=(km2-km)/litro2

print()
print("O consumo médio é de %2.2f Km/L"%(consumomedio))
print()
print("*****FIM*****")