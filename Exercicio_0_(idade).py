'''
0. Faça um algoritmo que leia a data de nascimento(dia, mês e ano), e informe a idade correta
'''
data=input("Informe a data de nascimento no formato [dd/mm/aaaa]:")
atual=input("Informe a data atual no formato [dd/mm/aaaa]:")

ano_nas=int(data[6:10])
mes_nas=int(data[3:5])
dia_nas=int(data[0:2])

ano_atual=int(atual[6:10])
mes_atual=int(atual[3:5])
dia_atual=int(atual[0:2])

idade=ano_atual-ano_nas

if mes_atual>mes_nas:
    print("Já fez aniversário neste ano")
else:
    if mes_atual==mes_nas:
        if dia_nas>dia_atual:
            idade=idade-1
            print("Não fez aniversário neste ano")
        else:
            print("Já fez aniversário neste ano")
    else:
        print("Não fez aniversário neste ano")
        idade=idade-1
print("A idade é", idade)
