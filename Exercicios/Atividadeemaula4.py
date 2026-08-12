# 4. Tabuada Interativa 

numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
    
#Como funciona:
#input() → pede o número ao usuário.
#int() → transforma o que foi digitado em número inteiro.
#for i in range(1, 11) → repete de 1 até 10.
#numero * i → calcula cada multiplicação.
#print() → mostra a tabuada.

#range() = sequência de números
#i = variável que recebe cada número dessa sequência


