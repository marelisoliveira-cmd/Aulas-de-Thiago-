# Crie um programa que receba o valor de uma compra e aplique descontos de acordo as faixas 
#Até R$100 - Sem desconto 
#De R$101 até R$500 - 10% de desconto
#De R$501 até R$1000 - 15% de desconto
#Acima de R$1000 - 20% de desconto 



valor = float(input("Digite o valor da compra: R$ "))

if valor <= 100:
    desconto = 0
elif valor <= 500:
    desconto = 0.10
elif valor <= 1000:
    desconto = 0.15
else:
    desconto = 0.20

valor_desconto = valor * desconto
valor_final = valor - valor_desconto

print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")











