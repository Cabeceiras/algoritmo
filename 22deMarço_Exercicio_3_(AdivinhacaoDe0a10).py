'''
3) faça um algoritmo uma pessoa informa um número aleatório 
entre 0 e 10 e outra pessoa irá tentar acertar o numero.
o sistema deve informar se o numero da tentativa é maior 
ou menor que o numero indicado pelo usuário inicialmente.
o programa so termina quando adivinhar
-mudança 1:
o sistema deve gerar o numero aleatório
-mudança 2:
 exibir no final quantas tentativas foram necessárias 
 até acertar
'''

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
