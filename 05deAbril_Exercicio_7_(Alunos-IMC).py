alunos=int(input("Informe a quantidade de alunos: "))

x=0
pesototal=0
alturatotal=0

while x<alunos:
    x=x+1
    peso=float(input("Informe o peso em kg do aluno %d: " %(x)))
    altura=float(input("Informe a altura em metros10 do aluno %d: " %(x)))
    pesototal=float(pesototal+peso)
    alturatotal=float(alturatotal+altura)

mediadepeso=float(pesototal/alunos)
mediaaltura=float(alturatotal/alunos)

mediadeimc=float(mediadepeso/(mediaaltura*mediaaltura))

print("A média de altura é",mediaaltura,"metro(s).")
print("A média de peso é",mediadepeso,"quilograma(s).")
print("A média de IMC é",mediadeimc)