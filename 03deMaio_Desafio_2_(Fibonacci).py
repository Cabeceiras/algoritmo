'''
2) - A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 
Sua regra deformação é simples: os dois primeiros elementos são 1; a partir de então,
cada elemento é asoma dos dois anteriores. Faça um algoritmo que leia um número inteiro
calcule o seu númerode Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
'''

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
