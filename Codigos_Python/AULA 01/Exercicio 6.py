nome_colab = input("Digite seu nome: ") # nome do colaborador da empresa.
idade_colab = int(input("Digite sua idade:"))
salario = float(input("Digite seu salário: "))
valor_acres = float(input("Digite o valor em porcentagem (%) do acrescimo a ser acrescentado no salario: "))

salario_acres = salario * (1 + (valor_acres / 100))


print(f"\nNome do colaborador: {nome_colab}\nSua idade é: {idade_colab}\nSeu salario é: R${salario} com acrescimo: R${salario_acres}")