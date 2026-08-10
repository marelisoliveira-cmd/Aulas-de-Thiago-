# EXERCÍCIOS — IF / ELSE

#2. Classificação por idade Solicite a idade de uma pessoa e classifique como criança, adolescente, adulto ou idoso.

idade = int(input("Digite a idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")


