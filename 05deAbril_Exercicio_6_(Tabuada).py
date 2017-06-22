'''
6) Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

	Tabuada de 5:	
	5 X 1 = 5
	5 X 2 = 10
	...
	5 X 10 = 50
    
'''

tabuada=int(input("Insira um valor inteiro para a tabuada de multiplicação de 1 a 10: "))

x=0

while x<10:
    x=x+1
    resultado=tabuada*x
    print (tabuada,"x",x,"=",resultado)
