
vet = [0]*30
for i in range(30):
    print("Posição",i+1,"(de 30) do vetor.")
    vet[i] = int(input("Insira um valor qualquer, negativo ou positivo: "))
    print()

print (vet)
print()
print("O vetor terá seus valores positivos substituídos por 1 e negativos por 0:")
def troca(vet):
    for i in range(30):
        if vet[i] > 0:
            vet[i] = 1
        else:
            vet[i] = 0
    return vet

print()
print(troca(vet))
print()
print("*****FIM*****")
