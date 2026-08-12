# 2. Somatório de números 
soma = 0

numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número (0 para parar): "))

print("Total:", soma)

