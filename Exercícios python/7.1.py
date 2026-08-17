peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")

