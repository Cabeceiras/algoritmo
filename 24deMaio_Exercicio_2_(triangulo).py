import math

print()
print("Este programa verifica se um triângulo é retângulo.")
print()

def triangret(vet):
    if vet[0] > vet[1] and vet[0] > vet[2]:
        hip = vet[0]
        cat1 = vet[1]
        cat2 = vet[2]
    elif vet[1] > vet[0] and vet[1] > vet[2]:
        hip = vet[1]
        cat1 = vet[0]
        cat2 = vet[2]
    else:
        hip = vet[2]
        cat1 = vet[0]
        cat2 = vet[1]

    if hip == math.sqrt(cat1**2 + cat2**2):
        print()
        print ("A hipotenusa é",hip,", um cateto é", cat1,"e o outro é", cat2,".")
        return 1


    else:
        return 0

vet = [0]*3
for i in range(3):
    vet[i] = float(input("Digite um valor para um lado do triângulo: "))

if triangret(vet) == 1:
    print()
    print ("O triângulo é retângulo.")

else:
    print()
    print ("O triângulo não é retângulo.")

print()
print("****FIM****")