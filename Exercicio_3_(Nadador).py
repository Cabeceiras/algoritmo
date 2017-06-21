'''
3.  Elabore um algoritmo que dada a idade de um nadador classifica-o
em uma das seguintes categorias:
infantil A = 5 - 7 anos
infantil B = 8 -10 anos
juvenil A = 11 -13 anos
juvenil B = 14 -17 anos
adulto = maiores de 18 anos
'''
print()
idade=int(input("Insira a idade do nadador: "))
print()
if idade<5:
    print ("O nadador está abaixo da menor categoria existente.")
if idade>=5 and idade<=7:
    print ("O nadador está na categoria infantil A.")
if idade>=8 and idade<=10:
    print ("O nadador está na categoria infantil B.")
if idade>=11 and idade<=13:
    print ("O nadador está na categoria juvenil A.")
if idade>=14 and idade<=17:
    print ("O nadador está na categoria juvenil B.")
if idade>=18:
    print ("O nadador está na categoria adulto.")