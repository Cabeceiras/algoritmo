'''
3) Altere o algoritmo anterior e informe a maior e menor idade.
'''

x=int(input("informe quantas idades vai inserir: "))
cont=0
maior=0
menor=1000

while (cont<x):
    idade=int(input("digite a idade: "))
    cont=cont+1
    if (idade>maior):
        maior=idade
    if (idade<menor):
        menor=idade

print("A maior idade é",maior)
print("A menor idade é",menor)
