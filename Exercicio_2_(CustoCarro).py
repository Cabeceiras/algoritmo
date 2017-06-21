'''
2. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%,
escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo
ao consumidor.
'''
print()
custofabrica=float(input("Insira o valor de fábrica do carro: "))

porcento=custofabrica/100

custo=custofabrica+(28*porcento)+(45*porcento)
print()
print("O custo do carro para o consumidor final é",custo,".")