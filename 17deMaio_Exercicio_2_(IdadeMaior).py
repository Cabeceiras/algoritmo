x=int(input("informe quantas idades vai inserir: "))
cont=0
m=0

while (cont<x):
    i=int(input("digite a idade: "))
    cont=cont+1
    if (i>m):
        m=i

print("A maior idade é",m)
