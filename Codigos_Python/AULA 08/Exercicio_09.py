n1 = float(input("Digite o valor 1: "))
n2 = float(input("Digite o valor 2: "))

if (n1 > n2):
    sub = (n1 - n2)

elif (n1 < n2):
    sub = (n2 - n1)

else:
    print("Valores semelhantes, o calculo só poderá ser realizado com valores distinstos!")


print(f"O valor da sua subtração é: {sub:.1f}")