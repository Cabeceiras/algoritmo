maior=0
x=0
for x in range(5):
    print()
    print("Esta é a idade",x+1,"de 5.")
    idade=int(input("Insira uma idade: "))
    if idade>maior:
        maior=idade

print()
print("A maior idade é:",maior,".")

