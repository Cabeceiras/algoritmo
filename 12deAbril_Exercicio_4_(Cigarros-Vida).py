'''
4)sistema deve perguntar quantos cigarros a pessoa fuma por dia 
e por quantos anos ela já fuma. Sabendo que cada cigarro se perde
10min de vida sistema deve calcular quantos dias de vida o fumante 
perderá
'''

cigarros=int(input("Informe a quantidade de cigarros fumados por dia: "))
anos=int(input("Informe o tempo em anos desde que foi iniciada a prática de fumar: "))

cigarros=cigarros*365

cigarros=cigarros*anos

minutos=cigarros*10

vidaemdias=float(minutos/1440)

print("Tempo de vida perdida em dias é igual a %2.2f dias."%(vidaemdias))

