c = 1
e = 0
div = 0

n1 = float(input("Digite o valor 1: "))

while (n2 == 0):
    n2 = float(input("Digite o valor 2: "))
    if(c >= 5):
        break

    c += 1

else:
    div = n1 / n2
    print(f"{div:.2f}")

print("Programa finalizado.")