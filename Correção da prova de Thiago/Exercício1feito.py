
#Exercício1
#Crie um programa que simule um sistema de login
#• Se o usuário for "Adm e a senha "1234", o sistema
#deve mostrar bem-sucedido
#• Se o usuário for "adm" mas a senha estiver errada,
#deve mostrar " senha incorreta"
#• Se o usuário não for " adm", deve mostrar "usuário não
# encontrado"

#EXERCÍCIO DA PROVA ERRADO 
#nome = imput ("Digite o usuário:")
#senha = int(imput ("Digite a senha:"))

#IF o nome for "adm":
    #print("bem-sucedido")
#ELSE: 
    #print("usuário não encontrado")
#ELIF a senha for 1234
    #print("bem-sucedido")
#ELSE: 
    #print("senha incorreta")

#observação: if
#elif
#elif
#else

#Nunca
#if
#else
#elif  ❌

#E lembre que em Python é input, if, else e elif,
#tudo em minúsculo.

#EXERCÍCIO COM CORREÇÃO 

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

#EXERCÍCIO COM CORREÇÃO SIMPLIFICADO 
#nome = input("Digite o usuário: ")
#senha = int(input("Digite a senha: "))

#if nome == "adm":
    #if senha == 1234:
        #print("bem-sucedido")
    #else:
        #print("senha incorreta")
#else:
    #print("usuário não encontrado")