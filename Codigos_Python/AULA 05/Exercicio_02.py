C = 1
soma = 0
#media = 0

while C <= 2:

    n = float(input(f"Digite o valor {C} desejado: "))
    soma += n
    C += 1

media = soma/C
print(f"A sua média é: {media:.2f}")
