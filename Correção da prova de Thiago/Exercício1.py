usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "Adm" and senha == "1234":
    print("Login bem-sucedido")
elif usuario == "adm":
    print("Senha incorreta")
else:
    print("Usuário não encontrado")

