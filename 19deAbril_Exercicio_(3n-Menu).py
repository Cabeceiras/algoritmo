'''
1)Faça um algoritmo que receba 3 números inteiros 
e o usuário decida quais das opções o sistema deve 
retornar: 
-a soma dos números 
-o maior
-o menor 
-a média 
'''

def soma(a,b,c):
    soma=a+b+c
    return(soma)

def maior(a,b,c):
    if a>=b:
        maior=a
        if c>a:
            maior=c
    else:
        maior=b
        if c>b:
            maior=c
    return(maior)

def menor(a,b,c):
    if a<=b:
        menor=a
        if c<a:
            menor=c
    else:
        menor=b
        if c<b:
            menor=c
    return(menor)

def media(a,b,c):
    media=(a+b+c)/3
    return(media)

print( )
print(">>>Informe 3 números inteiros para depois serem tratados pelas opções do programa.")
print( )

num1=int(input("Primeiro número: "))
num2=int(input("Segundo número: "))
num3=int(input("Terceiro número: "))

opcao=0

while opcao!=5:

    print( )
    print("O que deseja fazer com os números?")
    print("1 - Fazer a soma dos 3.")
    print("2 - Mostrar o número maior.")
    print("3 - Mostrar o menor número.")
    print("4 - Calcular a média dos 3 números.")
    print("5 - Sair do programa.")
    print( )
    opcao=int(input("Digite o número da opção que deseja: "))
    print( )

    if opcao==1:
        print("#####################################################")
        print("O resultado da soma é",soma(num1,num2,num3))
        print("#####################################################")
    if opcao==2:
        print("#####################################################")
        print("O maior número é",maior(num1,num2,num3))
        print("#####################################################")
    if opcao==3:
        print("#####################################################")
        print("O menor número é",menor(num1,num2,num3))
        print("#####################################################")
    if opcao==4:
        print("#####################################################")
        print("A média é",media(num1,num2,num3))
        print("#####################################################")
    if opcao==5:
        print(">>>FIM<<<")










