nota = float(input("Digite a nota: "))

if nota < 5:
    print("Reprovado")
elif nota < 7:
    print("Regular")
elif nota < 9:
    print("Bom")
else:
    print("Excelente")