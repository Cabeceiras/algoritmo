vetor=[]
vetorpar=[]
vetorimpar=[]
i=0
while i<20:
    print()
    print("Este é o número",i+1,"de 20.")
    numero=eval(input("Insira um número para o vetor: "))
    vetor.append(numero)
    i=i+1
    if numero%2==0:
        vetorpar.append(numero)
    else:
        vetorimpar.append(numero)
print()
print("Vetor com os vinte números:")
print (vetor)
print("Vetor com os pares: ")
print (vetorpar)
print("Vetor com os ímpares: ")
print(vetorimpar)
