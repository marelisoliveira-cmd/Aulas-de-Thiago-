# 6. Simulação de saldo bancário 

saldo = float(input("Digite o saldo inicial: R$ "))

while saldo > 0:
    saque = float(input("Digite o valor do saque: R$ "))

    saldo -= saque

    print(f"Saldo atual: R$ {saldo:.2f}")

print("O saldo chegou a zero ou ficou negativo.")



