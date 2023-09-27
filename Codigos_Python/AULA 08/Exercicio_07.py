opcao = "s"

while (opcao in "sS"):  # while opcao == "s" or opcao == "S":
    nBase = float(input("Informe o valor da base do triângulo: "))
    while nBase <= 0:
        nBase = float(input("Valor invalido, informe novamente: "))


    nAltura = float(input("Informe o valor da altura do triângulo: "))
    while nAltura <= 0:
        nAltura = float(input("Valor invalido, informe novamente: "))


    area = (nBase * nAltura) / 2
    print(f"O valor da área do triângulo é: {area:.2f}.")

    opcao = input("Você ainda deseja continuar com a calculadora ? (s/n): ")