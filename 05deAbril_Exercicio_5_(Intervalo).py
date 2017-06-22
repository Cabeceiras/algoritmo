'''
5) Faça um programa que receba dois números inteiros 
e gere os números inteiros que estão no intervalo 
compreendido por eles.
'''

inteiro1=int(input("Informe o primeiro número inteiro: "))
inteiro2=int(input("Informe o segundo número inteiro: "))

if inteiro2<inteiro1:
    receba=int(inteiro1)
    inteiro1=int(inteiro2)
    inteiro2=int(receba)

intervalo=inteiro1

while intervalo<inteiro2-1:
    intervalo=intervalo+1
    print(intervalo)
