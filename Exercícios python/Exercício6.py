#6. Mensagem por horário Solicite a hora atual (0 a 23) e mostre:

hora = int(input("Digite a hora: "))

if hora < 12:
    print("Bom dia")
elif hora <= 18:
    print("Boa tarde")
else:
    print("Boa noite")


