'''
5) o sistema deve perguntar a medida dos 3 lados de um triangulo,
o sistema deve informar o tipo de triangulo: equilatero, isosceles
ou escaleno.
'''

lado1=float(input("Informe medida do primeiro lado do triângulo: "))
lado2=float(input("Informe medida do segundo lado do triângulo: "))
lado3=float(input("Informe medida do terceiro lado do triângulo: "))

if lado1==lado2==lado3:
    print("O triângulo é equilátero")
else:
    if lado1==lado2 or lado2==lado3 or lado1==lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
