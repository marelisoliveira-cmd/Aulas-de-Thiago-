#7. Cálculo de IMC Peça peso e altura de uma pessoa, calcule o IMC e classifique como: abaixo do peso, normal, sobrepeso ou obesidade.

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura: "))
unidade = input("Digite a unidade (km, hm, dam, m, dm, cm, mm): ").lower()

if unidade == "km":
    altura = altura * 1000
elif unidade == "hm":
    altura = altura * 100
elif unidade == "dam":
    altura = altura * 10
elif unidade == "m":
    altura = altura
elif unidade == "dm":
    altura = altura / 10
elif unidade == "cm":
    altura = altura / 100
elif unidade == "mm":
    altura = altura / 1000
else:
    print("Unidade inválida.")

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



