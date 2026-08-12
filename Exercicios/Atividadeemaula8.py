# 8. Contagem de Vogais

palavra = input("Digite uma palavra: ")

vogais = "aeiouáéíóúâêôãõ"
contador = 0

for letra in palavra.lower():
    if letra in vogais:
        contador += 1

print("Quantidade de vogais:", contador)


