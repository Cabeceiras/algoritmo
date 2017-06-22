'''
8) o programa anterior, deve informar ao final o aluno com maior e menor imc.
'''

alunos=int(input("Informe a quantidade de alunos: "))

x=0
pesototal=0
alturatotal=0
imcmaior=0
imcmenor=1000

while x<alunos:

    x=x+1

    peso=float(input("Informe o peso em kg do aluno %d: " %(x)))
    altura=float(input("Informe a altura em metros do aluno %d: " %(x)))

    imcindividual=float(peso/(altura*altura))

    if imcindividual>imcmaior:
        imcmaior=imcindividual
        alunomaior=x

    if imcindividual<imcmenor:
        imcmenor=imcindividual
        alunomenor=x


    pesototal=float(pesototal+peso)
    alturatotal=float(alturatotal+altura)

mediadepeso=float(pesototal/alunos)
mediaaltura=float(alturatotal/alunos)
mediadeimc=float(mediadepeso/(mediaaltura*mediaaltura))

print("A média de altura é %2.2f metro(s)."%(mediaaltura))
print("A média de peso é %2.2f quilograma(s)."%(mediadepeso))
print("A média de IMC é %2.2f"%(mediadeimc))
print("O aluno",alunomaior,"possui o maior IMC, que é %2.2f."%(imcmaior))
print("O aluno",alunomenor,"possui o menor IMC, que é %2.2f."%(imcmenor))
