'''
4) Altere o exercício e armazene num vetor as idades informadas.
'''

x=int(input("informe quantas idades vai inserir: "))
cont=0
maior=0
menor=1000
vetor=[]

while (cont<x):
    print()
    print("Esta é a idade",cont+1,"de",x,".")
    idade=eval(input("Digite uma idade: "))
    vetor.append(idade)
    cont=cont+1
    if (idade>maior):
        maior=idade
    if (idade<menor):
        menor=idade

print()
print("O vetor é:")
print(vetor)
print("A maior idade é",maior,".")
print("A menor idade é",menor,".")
