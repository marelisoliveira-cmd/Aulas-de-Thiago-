#Faça uma programação para somar numero até digitar sair 

#Os espaços em branco (_____) são lugares onde você vai escrever algo. O resto do texto já está pronto, só falta preencher os espaços.
#O f no Python faz exatamente a mesma coisa! Ele cria um texto com "espaços em branco" (as chaves {}) e você preenche com o valor de uma variável.

#COM f
#nome = "João"
#idade = 20
#print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")

#SEM f
#nome = "João"
#idade = 20
#print("Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos.")
# ou print("Meu nome é", nome, "e tenho", idade, "anos.")


soma = 0

while True:
    # 1. Recebe como texto (string)
    numero = input("Digite um número ou digite 'sair' para encerrar: ")
    
    # 2. Verifica se o usuário quer sair
    if numero == 'sair':
        break
    
    # 3. Se não for 'sair', converte para float e soma
    soma += float(numero)

print(f"A soma total dos números digitados foi: {soma}")
               
                     
