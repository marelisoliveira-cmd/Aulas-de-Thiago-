#Exercício1
#Crie um programa que simule um sistema de login
#• Se o usuário for "Adm e a senha "1234", o sistema
#deve mostrar bem-sucedido
#• Se o usuário for "adm" mas a senha estiver errada,
#deve mostrar " senha incorreta"
#• Se o usuário não for " adm", deve mostrar "usuário não
# encontrado"



nome = input("Digite o usuário: ")
senha = int(input("Digite a senha: "))

if nome == "adm" and senha == 1234:
    print("bem-sucedido")

elif nome == "adm" and senha != 1234:
    print("senha incorreta")

else:
    print("usuário não encontrado")

