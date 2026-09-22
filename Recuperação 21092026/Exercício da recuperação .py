#Crie uma programação que deverá retornar todos os números pares.
#Por exemplo, se o usuário digitar 10, o programa deverá
#retornar 2, 4, 6, 8, 10. Utilize o comando while em python.


numero = int(input("Digite um número:"))

i = 2 

while i <= numero:
    print(i)
    i += 2