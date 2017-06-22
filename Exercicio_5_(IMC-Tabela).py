'''
5)apos calcular o IMC informe, o de acordo com o sexo informe a situação de acordo com a tabela a seguir:

Condição					IMC em Mulheres	IMC em Homens
abaixo do peso				< 19,1	        < 20,7
no peso normal				19,1 - 25,8	    20,7 - 26,4
marginalmente acima do peso	25,8 - 27,3	    26,4 - 27,8
acima do peso ideal			27,3 - 32,3	    27,8 - 31,
'''

print()
peso=float(input("Informe o peso em kg da pessoa: "))
altura=float(input("Informe a altura em metros da pessoa: "))
print()

genero=input("A pessoa é homem ou mulher? Insira h ou m: ")
print()
imc=float(peso/(altura*altura))

if genero=="h" or genero=="homem":
    if imc < 20.7:
        print("O imc desse homem é %2.2f e ele está abaixo do peso."%(imc))
    if imc>=20.7 and imc<26.4:
        print("O imc desse homem é %2.2f e ele está no peso normal."%(imc))
    if imc>=26.4 and imc<27.8:
        print("O imc desse homem é %2.2f e ele está marginalmente acima do peso."%(imc))
    if imc>=27.8 and imc<31:
        print("O imc desse homem é %2.2f e ele está acima do peso ideal."%(imc))
    if imc>=31:
        print("O imc desse homem é %2.2f e ele está acima da tabela."%(imc))

if genero=="m" or genero=="mulher":
    if imc < 19.1:
        print("O imc dessa mulher é %2.2f e ela está abaixo do peso."%(imc))
    if imc>=19.1 and imc<25.8:
        print("O imc dessa mulher é %2.2f e ela está no peso normal."%(imc))
    if imc>=25.8 and imc<27.3:
        print("O imc dessa mulher é %2.2f e ela está marginalmente acima do peso."%(imc))
    if imc>=27.3 and imc<32.3:
        print("O imc dessa mulher é %2.2f e ela está acima do peso ideal."%(imc))
    if imc>=32.3:
        print("O imc dessa mulher é %2.2f e ela está acima da tabela."%(imc))
