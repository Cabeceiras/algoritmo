from random import randint
numero=randint(0,4)

login=[["José","Carlos","Breno","Tadeu","Vitor"],[1990,1972,2011,1983,2002]]

print()
print("O login é",login[0][numero],". Sua senha corresponde a um ano.")
print("**************************************************")
print("Atenção. Você somente poderá errar a senha 3 vezes.")
print("***************************************************")

acabou="não"
erros=0

senha=login[1][numero]

while erros<3 and acabou=="não":

    print()
    print("Login:",login[0][numero])
    palpite=int(input("Digite a senha: "))


    if palpite==senha:
        print()
        print("##############")
        print("Senha correta!")
        print("##############")
        acabou="sim"
    else:
        print()
        erros=erros+1
        print("Senha incorreta. Você possui",erros,"erro(s).")

print()
print("****FIM****")