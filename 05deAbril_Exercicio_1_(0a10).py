numero=int(input("Insira número de 0 a 10: "))

while numero<0 or numero>10:
    print("Número inválido")
    numero=int(input("Insira número de 0 a 10: "))

print ("Número válido.")