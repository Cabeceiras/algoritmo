'''
4) Altere o exercício e armazene num vetor as idades informadas.
'''

x=int(input("informe quantas idades vai inserir: "))
cont=0
maior=0
menor=1000
idade=[]

while (cont<x):
    idade.append=int(input("digite a idade: "))
    cont=cont+1
    if (idade>maior):
        maior=idade
    if (idade<menor):
        menor=idade

print("A maior idade é",maior)
print("A menor idade é",menor)
