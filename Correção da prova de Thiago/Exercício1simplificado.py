usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario != "Adm":
    print("Usuário não encontrado")
elif senha != "1234":
    print("Senha incorreta")
else:
    print("Login bem-sucedido")