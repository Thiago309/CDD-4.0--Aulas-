n = 0
soma = 0
media = 0

qtd = int(input("Informe a quantidade de vezes para repetir: "))

for i in range(qtd):
    n = float(input(f"Digite o valor {i + 1}: "))
    soma += n

media = soma / qtd
print(f"A sua média é: {media:.2f}")


# opcao = "s"
# c = 0
#
#
# while (c != 4):
#     n1 = float(input("Digite o valor da nota (1): "))
#     while (n1 <= 0) and (n1 > 10):
#         n1 = float(input("Valor da nota (1), incorreto. Digite novamente valores entre [0 ~ 10]: "))
#
#     opcao = input("Você ainda deseja continuar com a calculadora ? (s/n): ")