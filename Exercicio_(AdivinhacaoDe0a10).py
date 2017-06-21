from random import *
numero=randint(0,10)

print()
adivinhe=int(input("Informe o número de 1 a 10 que você acha que o computador forneceu: "))
tentativas=int(1)

while adivinhe!=numero:
    if adivinhe>numero:
        print()
        print("Número maior do que o gerado pelo computador.")
    else:
        print()
        print("Número menor do que o gerado pelo computador.")
    print()
    adivinhe=int(input("Informe o número de 1 a 10 que você acha que o computador forneceu: "))
    tentativas=int(tentativas+1)
print()
print("Você acertou, mizerávi!")
print("Após tentar",tentativas,"vez(es)")