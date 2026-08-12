# 9. Caixa eletrônico

valor = int(input("Digite o valor para sacar: R$ "))

notas_50 = valor // 50
restante = valor % 50

print("Notas de R$ 50:", notas_50)
print("Restante:", restante)
