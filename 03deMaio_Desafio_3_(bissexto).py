opcao=1
while opcao==1:

    print()
    ano=int(input("Insira um ano para verificar se é bissexto: "))

    resto4 = ano%4
    resto100 = ano%100
    resto400 = ano%400

    if resto4==0:

        if resto100==0:

            if resto400==0:

                print()
                print("O ano",ano,"é bissexto!")
            else:

                print()
                print("O ano",ano,"NÃO é bissexto!")

        else:

            print()
            print("O ano",ano,"é bissexto!")
    else:
        print()
        print("O ano",ano,"NÃO é bissexto!")


    print()
    opcao=int(input("Digite 1 para verficar mais um ano ou digite outro valor para sair: "))
    print()
