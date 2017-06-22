'''
Faça um algoritmo que o usuário informe a quantidade de linhas 
e colunas que a matriz deve ter.O sistema deve criar a matriz 
atribuindo zero para cada campo.
'''

print("Este programa faz uma matriz com zeros.")
print("***************************************")
print()
linha=int(input("Insira o número de linhas da matriz: "))
colunas=int(input("Insira o número de colunas da matriz: "))
print()
m = [0]*linha
for i in range(linha):
    m[i] = [0]*colunas
print(m)
print()
print("*****FIM*****")
