'''
2) Escreva um algoritmo para ler as dimensões de um 
retângulo (base e altura), calcular e escrever a área 
do retângulo, e caso seja um quadrado, exibir a frase: 
área de um quadrado
'''

base_ret=input("Informe base do retângulo em centimetros: ")
altura_ret=input("Informe altura do retângulo em centimetros: ")

area_ret=int(base_ret)*int(altura_ret)

print ("A área em centimetros é:",area_ret)

if base_ret==altura_ret:
    print("A área é de um quadrado.")
