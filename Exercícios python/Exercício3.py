# EXERCÍCIOS — IF / ELSE

#3. Login simples Peça um nome de usuário e senha. Se forem iguais a valores pré-definidos, mostre “Login bem-sucedido”, senão mostre “Usuário ou senha
#inválidos”.

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido")
else:
    print("Usuário ou senha inválidos")
