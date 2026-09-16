#Imagine que você quer verificar se uma pessoa pode entrar em um evento. A regra é: ela pode entrar se tiver convite OU se for maior de 18 anos 

idade = int(input("Digite sua idade: "))
convite = input("Você tem convite? (sim/não): ")

if convite == "sim" or idade > 18:
    print("Pode entrar")
else:
    print("Não pode entrar")





    
