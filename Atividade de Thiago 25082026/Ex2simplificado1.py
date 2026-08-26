soma = 0

while True:
    entrada = input("Digite um número ou 'sair' para terminar: ")

    if entrada.lower() == "sair":
        break

    try:
        numero = float(entrada)
        soma += numero
    except ValueError:
        print("Digite um número válido ou 'sair'.")

print("A soma dos números é:", soma)
