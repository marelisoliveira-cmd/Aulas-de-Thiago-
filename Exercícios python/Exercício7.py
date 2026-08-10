#7. Cálculo de IMC Peça peso e altura de uma pessoa, calcule o IMC e classifique como: abaixo do peso, normal, sobrepeso ou obesidade.

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")



