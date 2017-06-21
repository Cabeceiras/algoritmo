cigarros=int(input("Informe a quantidade de cigarros fumados por dia: "))
anos=int(input("Informe o tempo em anos desde que foi iniciada a prática de fumar: "))

cigarros=cigarros*365

cigarros=cigarros*anos

minutos=cigarros*10

vidaemdias=float(minutos/1440)

print("Tempo de vida perdida em dias é igual a %2.2f dias."%(vidaemdias))

