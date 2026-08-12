
    #Eu preciso que você some e mais um numero que eu vou digitar 
    #Se eu digitar 0 ele para de contabilizar e soma o total de números diferentes de 0
    
soma = 0
numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número (0 para parar): "))

print("Soma total:", soma)

