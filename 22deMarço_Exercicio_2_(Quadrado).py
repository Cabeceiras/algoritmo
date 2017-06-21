base_ret=input("Informe base do retângulo em centimetros: ")
altura_ret=input("Informe altura do retângulo em centimetros: ")

area_ret=int(base_ret)*int(altura_ret)

print ("A área em centimetros é:",area_ret)

if base_ret==altura_ret:
    print("A área é de um quadrado.")