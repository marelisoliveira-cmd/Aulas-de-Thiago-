# Crie um programa que receba o valor de uma compra e aplique descontos de acordo as faixas 
#Até R$100 - Sem desconto 
#De R$101 até R$500 - 10% de desconto
#De R$501 até R$1000 - 15% de desconto
#Acima de R$1000 - 20% de desconto 


valor = float(input("Valor da compra: R$ "))

if valor <= 100:
    desconto = 0
elif valor <= 500:
    desconto = 10
elif valor <= 1000:
    desconto = 15
else:
    desconto = 20

final = valor - (valor * desconto / 100)

print("Valor com desconto: R$", final)











