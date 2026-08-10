#4. Desconto em compras Solicite o valor de uma compra e aplique desconto:

valor = float(input("Digite o valor: "))

if valor >= 200:
    print("Desconto de 20%")
elif valor >= 100:
    print("Desconto de 10%")
else:
    print("Desconto de 5%")


