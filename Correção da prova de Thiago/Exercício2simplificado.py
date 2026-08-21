#Exercício 2
#• Crie um programa que receba a nota do aluno
#e classifique o desempenho
#Nota maior ou igual a 9 -> excelente
#• Nota 7 a 8,9 - bom
#• Nota 5 e 6,9 - Regular
#• Nota menor que 5 - Reprovado

nota = float(input("Digite a nota: "))

if nota >= 9:
    print("Excelente")

elif nota >= 7:
    print("Bom")

elif nota >= 5:
    print("Regular")

else:
    print("Reprovado")