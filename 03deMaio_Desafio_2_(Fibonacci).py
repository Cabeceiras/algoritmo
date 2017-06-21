limite=int(input("Insira o número natural que será o limite da sequência de Fibonacci: "))

fibo=1
sequencia=list(range(limite))
sequencia[0]=fibo
sequencia[1]=fibo
posicao=2

while fibo<=limite:

    fibo=sequencia[posicao-1]+sequencia[posicao-2]
    sequencia[posicao]=fibo

    posicao=posicao+1

for x in range ((posicao-1)):
    numero=x
    print("O elemento da posição",numero,"é >>>>",sequencia[x])

print("Fim da sequência até o limite.")