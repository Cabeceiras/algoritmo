'''
4) Faça um algoritmo para efetuar o cálculo do IMC. Sabendo que é feito
dividindo o peso (em quilogramas) pela altura (em metros) ao quadrado.
'''
print()
peso=float(input("Informe o peso em kg da pessoa: "))
altura=float(input("Informe a altura em metros da pessoa: "))

imc=float(peso/(altura*altura))

print()
print("O imc da pessoa é %2.2f."%(imc))