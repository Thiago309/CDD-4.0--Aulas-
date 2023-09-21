resp = "s"
i = "n"

while (resp in "sS"):

    n1 = float(input("Informe a primeira nota: "))

    while (n1 < 0) or (n1 > 10):
        n1 = float(input("Informe a primeira nota: "))

    n2 = float(input("Informe a primeira nota: "))

    while (n2 < 0) or (n2 > 10):
        n2 = float(input("Informe a primeira nota: "))

    media = (n1 + n2) / 2
    print(media)

    resp = input("Deseja continuar (s/n)?: ")