usuario=input("Digite o nome de usuário: ")
senha=input("Digite a senha: ")

while senha==usuario:
    print("Senha e nome não podem ser iguais. Informe outros.")
    usuario=input("Digite o nome de usuário: ")
    senha=input("Digite a senha: ")
print("login informado corretamente")