#Faça uma programação para somar numero até digitar sair 


soma =0 

numero = float(input("Digite um número ou digite 'sair' para encerrar:"))

while True:
    if numero == 'sair':
        break
    else:
        soma += numero
        numero = float(input("Digite um número ou digite 'sair' para encerrar:"))
               
                     