from Produtos import *

prod = input(("Insira o nome do produto: "))
qtd = int(input("Informe a quantidade do produto armazenada no estoque: "))
preco = float(input("Informe o valor unitario do produto: "))

r = estoque(prod, qtd, preco)

print(f"O valor do {r[0]} é R${r[1]:.2f}")