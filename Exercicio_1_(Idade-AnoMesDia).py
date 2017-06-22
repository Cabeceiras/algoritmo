'''
1) Faça um algoritmo que leia a data de nascimento de uma pessoa  
e mostre-a expressa em anos, meses e dias.
'''
data=input("Informe a data de nascimento no formato [dd/mm/aaaa]: ")
atual=input("Informe a data atual no formato [dd/mm/aaaa]: ")

ano_nas=int(data[6:10])
mes_nas=int(data[3:5])
dia_nas=int(data[0:2])

ano_atual=int(atual[6:10])
mes_atual=int(atual[3:5])
dia_atual=int(atual[0:2])

idade=ano_atual-ano_nas

if mes_atual<mes_nas:
    idade=idade-1
    
if mes_atual==mes_nas:
        if dia_nas>dia_atual:
            idade=idade-1

idade_mes=(mes_nas-mes_atual)

if idade_mes<0:
    idade_mes=idade_mes+12
    
print("A idade do indíviduo é",idade,"anos, ",idade_mes,"mes(es) e",dia_atual,"dia(s).")

