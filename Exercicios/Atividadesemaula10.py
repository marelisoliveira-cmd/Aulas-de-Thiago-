# 10. Jogo de Adivinhação

import random

numero_secreto = random.randint(1, 100)

palpite = int(input("Tente adivinhar o número (1 a 100): "))

while palpite != numero_secreto:
    if palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

    palpite = int(input("Tente novamente: "))

print("Parabéns! Você acertou!")
