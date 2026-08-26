#Faça uma programação que o digitar um número ele retorna dizendo se é menor que 10 ou maior que 20


numero = int(input("Digite o número:"))

if numero < 10 or numero > 20:
    print("o numero está fora do intervalo entre 10 e 20")
else :
    print("o numero está dentro do intervalo")