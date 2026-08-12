# 7. Notas de Alunos

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))

    if nota < 0 or nota > 10:
        print("Nota inválida. Programa encerrado.")
        break

    print(f"Nota registrada: {nota}")
