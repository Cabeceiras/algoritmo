opcao=1
print("### Este programa calcula a quantidade de latas necessárias para pintar uma determinada área. ###")
while opcao==1:

    print()
    metros=int(input("Insira com um número inteiro a área em metros quadrados que será pintada: "))

    litros=metros//3

    if (metros%3)!=0:
        litros=litros+1

    latas=litros//18

    if (litros%18)!=0:
        latas=latas+1

    precototal=latas*80

    print()
    print("Você precisará de",latas,"latas, que custam no total R$",precototal,"(cada uma custa R$ 80)")


    print()
    opcao=int(input("Digite 1 para verficar uma nova área ou digite outro valor para sair: "))
    print()


