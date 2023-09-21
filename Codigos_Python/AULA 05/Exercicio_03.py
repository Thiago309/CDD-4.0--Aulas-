C = 1
soma = 0

vezes = int(input("Você deseja calcular a média de quantas notas ? "))

while C <= vezes:
    n = float(input(f"Digite o valor {C}: "))
    soma += n
    C += 1

media = soma / C
print(f"Sua média é :{media:.2f}")