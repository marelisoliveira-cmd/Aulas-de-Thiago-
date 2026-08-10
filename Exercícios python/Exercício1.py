# EXERCÍCIOS — IF / ELSE

#1. Notas escolares Peça a nota de um aluno e mostre se ele está aprovado (nota ≥ 7), em recuperação (nota entre 5 e 6,9) ou reprovado (nota &lt; 5).

nota = float(input("Digite a nota: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")



