y=input("Verificar nova média? Digite sim ou não: ")

while y=="sim":
    n=input("Digite seu nome: ")
    n1=int(input("Digite Nota 1: "))
    n2=int(input("Digite Nota 2: "))
    n3=int(input("Digite Nota 3: "))
    n4=int(input("Digite Nota 4: "))

    m=(n1+n2+n3+n4)/4
    print("Olá %s, sua média foi %3.2f"%(n,m))

    x=input("Verificar situação dessa média? Digite sim ou não: ")

    while x=="sim":
        if m<6:
            print("Insuficiente")
        elif m<7:
            print("Suficiente")
        elif m<9:
            print("Bom")
        else:
            print("Ótimo")
        x=input("Verificar situação dessa média? Digite sim ou não: ")
    y=input("Verificar nova média? Digite sim ou não: ")



