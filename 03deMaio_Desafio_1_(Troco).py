'''
(1) - Indique como um troco deve ser dado utilizando-se um número mínimo de notas.
Seu algoritmo deve ler o valor da conta ,a ser paga e o valor do pagamento efetuado
desprezandoos centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5,
2 e 1 reais, e quenenhuma delas esteja em falta no caixa
'''

print()
preco=int(input("Informe em número inteiro o preço do produto: "))
print()
pagamento=int(input("Informe em número inteiro o pagamento do cliente: "))
print()

troco=0
troco=pagamento-preco

print("O troco é",troco,".")
print()

notas50=0
notas20=0
notas10=0
notas5=0
notas2=0
notas1=0

if troco==0:
    print("Não precisa de troco. O pagamento foi igual ao valor do produto.")

if troco<0:
    print("Atenção. O pagamento foi menor que o preço do produto.")

if troco>0:


    if (troco//50)>=1:
        notas50=troco//50
        troco=troco-(notas50*50)



    if (troco//20)>=1:
        notas20=troco//20
        troco=troco-(notas20*20)


    if (troco//10)>=1:
        notas10=troco//10
        troco=troco-(notas10*10)


    if (troco//5)>=1:
        notas5=troco//5
        troco=troco-(notas5*5)


    if (troco//2)>=1:
        notas2=troco//2
        troco=troco-(notas2*2)


    if (troco//1)>=1:
        notas1=troco//1
        troco=troco-(notas1*1)


    if notas50>=1:
        print("Notas de 50 para o troco:",notas50,"nota(s).")

    if notas20>=1:
        print("Notas de 20 para o troco:",notas20,"nota(s).")

    if notas10>=1:
        print("Notas de 10 para o troco:",notas10,"nota(s).")

    if notas5>=1:
        print("Notas de 5 para o troco:",notas5,"nota(s).")

    if notas2>=1:
        print("Notas de 2 para o troco:",notas2,"nota(s).")

    if notas1>=1:
        print("Notas de 1 para o troco:",notas1,"nota(s).")
