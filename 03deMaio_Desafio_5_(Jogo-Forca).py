'''
5) - Faça um jogo de forca...o sistema deve escolher aleatoriamente 
uma lista de nomes, como por exemplo, nome dos meses..O usuário 
só poderá errar 6 vezes, E o programa encerraa cada acerto deve 
aparecer a letra na posição correspondente do nome.quando for digitada 
todas as letras do nome o sistema deve informar a mensagem: VENCEDOR!
'''

from random import *
numero=randint(0,11)

if numero==0:

    letras=7
    vetor_da_adivinhacao=list(range(7))
    vetor_da_palavra=list(range(7))
    vetor_da_palavra[0]="j"
    vetor_da_palavra[1]="a"
    vetor_da_palavra[2]="n"
    vetor_da_palavra[3]="e"
    vetor_da_palavra[4]="i"
    vetor_da_palavra[5]="r"
    vetor_da_palavra[6]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"
    vetor_da_adivinhacao[5]="_"
    vetor_da_adivinhacao[6]="_"


if numero==1:

    letras=9
    vetor_da_adivinhacao=list(range(9))
    vetor_da_palavra=list(range(9))
    vetor_da_palavra[0]="f"
    vetor_da_palavra[1]="e"
    vetor_da_palavra[2]="v"
    vetor_da_palavra[3]="e"
    vetor_da_palavra[4]="r"
    vetor_da_palavra[5]="e"
    vetor_da_palavra[6]="i"
    vetor_da_palavra[7]="r"
    vetor_da_palavra[8]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"
    vetor_da_adivinhacao[5]="_"
    vetor_da_adivinhacao[6]="_"
    vetor_da_adivinhacao[7]="_"
    vetor_da_adivinhacao[8]="_"


if numero==2:

    letras=5
    vetor_da_adivinhacao=list(range(5))
    vetor_da_palavra=list(range(5))
    vetor_da_palavra[0]="m"
    vetor_da_palavra[1]="a"
    vetor_da_palavra[2]="r"
    vetor_da_palavra[3]="ç"
    vetor_da_palavra[4]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"


if numero==3:

    letras=5
    vetor_da_adivinhacao=list(range(5))
    vetor_da_palavra=list(range(5))
    vetor_da_palavra[0]="a"
    vetor_da_palavra[1]="b"
    vetor_da_palavra[2]="r"
    vetor_da_palavra[3]="i"
    vetor_da_palavra[4]="l"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"

if numero==4:

    letras=4
    vetor_da_adivinhacao=list(range(4))
    vetor_da_palavra=list(range(4))
    vetor_da_palavra[0]="m"
    vetor_da_palavra[1]="a"
    vetor_da_palavra[2]="i"
    vetor_da_palavra[3]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"


if numero==5:

    letras=5
    vetor_da_adivinhacao=list(range(5))
    vetor_da_palavra=list(range(5))
    vetor_da_palavra[0]="j"
    vetor_da_palavra[1]="u"
    vetor_da_palavra[2]="n"
    vetor_da_palavra[3]="h"
    vetor_da_palavra[4]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"

if numero==6:

    letras=5
    vetor_da_adivinhacao=list(range(5))
    vetor_da_palavra=list(range(5))
    vetor_da_palavra[0]="j"
    vetor_da_palavra[1]="u"
    vetor_da_palavra[2]="l"
    vetor_da_palavra[3]="h"
    vetor_da_palavra[4]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"


if numero==7:

    letras=6
    vetor_da_adivinhacao=list(range(6))
    vetor_da_palavra=list(range(6))
    vetor_da_palavra[0]="a"
    vetor_da_palavra[1]="g"
    vetor_da_palavra[2]="o"
    vetor_da_palavra[3]="s"
    vetor_da_palavra[4]="t"
    vetor_da_palavra[5]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"
    vetor_da_adivinhacao[5]="_"


if numero==8:

    letras=8
    vetor_da_adivinhacao=list(range(8))
    vetor_da_palavra=list(range(8))
    vetor_da_palavra[0]="s"
    vetor_da_palavra[1]="e"
    vetor_da_palavra[2]="t"
    vetor_da_palavra[3]="e"
    vetor_da_palavra[4]="m"
    vetor_da_palavra[5]="b"
    vetor_da_palavra[6]="r"
    vetor_da_palavra[7]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"
    vetor_da_adivinhacao[5]="_"
    vetor_da_adivinhacao[6]="_"
    vetor_da_adivinhacao[7]="_"


if numero==9:

    letras=7
    vetor_da_adivinhacao=list(range(7))
    vetor_da_palavra=list(range(7))
    vetor_da_palavra[0]="o"
    vetor_da_palavra[1]="u"
    vetor_da_palavra[2]="t"
    vetor_da_palavra[3]="u"
    vetor_da_palavra[4]="b"
    vetor_da_palavra[5]="r"
    vetor_da_palavra[6]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"
    vetor_da_adivinhacao[5]="_"
    vetor_da_adivinhacao[6]="_"


if numero==10:

    letras=8
    vetor_da_adivinhacao=list(range(8))
    vetor_da_palavra=list(range(8))
    vetor_da_palavra[0]="n"
    vetor_da_palavra[1]="o"
    vetor_da_palavra[2]="v"
    vetor_da_palavra[3]="e"
    vetor_da_palavra[4]="m"
    vetor_da_palavra[5]="b"
    vetor_da_palavra[6]="r"
    vetor_da_palavra[7]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"
    vetor_da_adivinhacao[5]="_"
    vetor_da_adivinhacao[6]="_"
    vetor_da_adivinhacao[7]="_"


if numero==11:

    letras=8
    vetor_da_adivinhacao=list(range(8))
    vetor_da_palavra=list(range(8))
    vetor_da_palavra[0]="d"
    vetor_da_palavra[1]="e"
    vetor_da_palavra[2]="z"
    vetor_da_palavra[3]="e"
    vetor_da_palavra[4]="m"
    vetor_da_palavra[5]="b"
    vetor_da_palavra[6]="r"
    vetor_da_palavra[7]="o"
    vetor_da_adivinhacao[0]="_"
    vetor_da_adivinhacao[1]="_"
    vetor_da_adivinhacao[2]="_"
    vetor_da_adivinhacao[3]="_"
    vetor_da_adivinhacao[4]="_"
    vetor_da_adivinhacao[5]="_"
    vetor_da_adivinhacao[6]="_"
    vetor_da_adivinhacao[7]="_"


print()
print("A palavra que deve ser adivinhada nomeia um mês do ano e possui",letras,"letras.")
print("*************************************************************************")
print("Atenção. Neste jogo de forca, você só poderá errar 6 vezes")
print("**********************************************************")

acabou="não"
erros=0

while erros<6 and acabou=="não":

    print()
    print()
    palpite=input("Digite uma letra que você pensa estar na palavra: ")

    errado=1

    for x in range(letras):

        if palpite==vetor_da_palavra[x]:

            vetor_da_adivinhacao[x]=palpite
            print()
            print()
            print("Acertou uma letra!")
            print()
            errado=0
            for y in range(letras):
                print(vetor_da_adivinhacao[y], end=' ')

    if errado==1:
        print()
        print()
        erros=erros+1
        print("Letra errada, ela não consta na palavra. Você possui",erros,"erro(s).")


        if erros==6:
            print()
            print("Perdeu o jogo! Errou 6 vezes.")

    if vetor_da_adivinhacao==vetor_da_palavra:
        print()
        print()
        print("VENCEDOR! Você acertou a palavra.")
        acabou="sim"

print()
print("########################")
print("Fim! Obrigado por jogar.")
print("########################")
