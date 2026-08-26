#Faça uma programação para somar numero até digitar sair 


soma = 0

while True:
    
    n = input("Digite um número ou sair:")

    if n == "sair":
        break
    else:
        soma += int(n)
#sem o else também funciona

print(soma)





