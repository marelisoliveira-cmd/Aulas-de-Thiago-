#9. Conceito de notas Peça a nota de um aluno e atribua conceito:

nota = float(input("Digite a nota: "))
if nota >= 9: 
    print("A") 
elif nota >= 7: 
    print("B")
elif nota >= 5: 
    print("C") 
else: print("D")