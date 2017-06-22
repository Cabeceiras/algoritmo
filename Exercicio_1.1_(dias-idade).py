'''
1.1) FAÇA UM PROGRAMA QUE O USUÁRIO INFORME QUANTOS DIAS DE VIDA ELE TEM 
e o sistema mostre-a expressa em anos, meses e dias de vida.
'''
idade_dias=input("Informe sua idade em dias: ")

idade_meses=int(int(idade_dias)/30)

sobra_dias=int(idade_dias)%30

idade_anos=int(idade_meses/12)

sobra_meses=int(idade_meses%12)

print("Sua idade é", idade_anos, "anos,", sobra_meses, "meses e", sobra_dias, "dias")
