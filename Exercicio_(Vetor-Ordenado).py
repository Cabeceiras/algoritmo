vetor=[]


numero1=eval(input("Insira o primeiro número: "))
vetor.append(numero1)
numero2=eval(input("Insira o segundo número: "))
vetor.append(numero2)
numero3=eval(input("Insira o terceiro número: "))
vetor.append(numero3)


if numero1>numero2:
    vetor[0]=numero1
    vetor[1]=numero2
    if numero2>numero3:
        vetor[2]=numero3
    else:
        if numero3>numero1:
            vetor[0]=numero3
            vetor[1]=numero1
            vetor[2]=numero2
        else:
            vetor[1]=numero3
            vetor[2]=numero2
else:
    vetor[0]=numero2
    vetor[1]=numero1
    if numero1>numero3:
        vetor[2]=numero3
    else:
        if numero3>numero2:
            vetor[0]=numero3
            vetor[1]=numero2
            vetor[2]=numero1
        else:
            vetor[1]=numero3
            vetor[2]=numero1
print("A ordem decrescente dos números é:", vetor[0],",", vetor[1],"e",vetor[2])

