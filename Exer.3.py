nota = -1

while nota < 0 or nota > 10:
    nota = int(input("Informe uma nota entre 0 e 10: "))


    if nota < 0 or nota > 10:
        print("Valor inválido, por favor tente novamente.")
