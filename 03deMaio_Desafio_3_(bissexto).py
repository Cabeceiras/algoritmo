'''
3) - Determine se um ano é bissexto:para ser bissexto, o ano deve ser:
Divisível  4. Sendo assim, a divisão é exata com o resto igual a zero; 
Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja,
deixa resto diferente de zero; Pode ser que seja divisível por 400. 
Caso seja divisível por 400, a divisão deve ser exata, deixando o resto 
igual a zero.
'''

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
