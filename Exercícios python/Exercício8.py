#8. Ano bissexto Solicite um ano e informe se ele é bissexto ou não bissexto.

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("Ano bissexto")
else:
    print("Ano não bissexto")

