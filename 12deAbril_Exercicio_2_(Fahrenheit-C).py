resposta="sim"

while resposta=="sim":

    fahr=float(input("Informe a temperatura em Fahrenheit: "))

    celsius=(fahr-32)/1.8

    print("A temperatura em Celsius é %2.2f"%(celsius))

    resposta=input("Deseja inserir mais uma temperatura em Fahrenheit? Digite sim ou não: ")