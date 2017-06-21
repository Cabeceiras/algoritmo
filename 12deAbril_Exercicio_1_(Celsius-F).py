resposta="sim"

while resposta=="sim":

    celsius=float(input("Informe a temperatura em Celsius: "))

    fahr=(celsius*1.8)+32
    print("A temperatura em Fahrenheit é %2.2f"%(fahr))

    resposta=input("Deseja inserir mais uma temperatura em Celsius? Digite sim ou não: ")