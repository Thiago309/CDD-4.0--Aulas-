from Biblioteca import * # Poderia ser tambem: import soma, mult, div e etc ...

opcao = ""

while True:
    opcao = input("Digite:\n\t [1] - Somar\n\t [2] - Subtrair\n\t [3] - Multiplicar\n\t [4] - Divisão\n\t [s] - Para sair da calculadora: ")

    if (opcao != "s") or (opcao == 1) or ( opcao == 2) or (opcao == 3):
        n1 = float(input("Informe o primeiro valor: "))
        n2 = float(input("Informe o segundo valor: "))

        if opcao == "1":
            soma(n1, n2)

        elif opcao == "2":
            sub(n1, n2)

        elif opcao == "3":
            mult(n1, n2)

        elif opcao == "4":
            div(n1, n2)

    elif opcao == "s":
        print("Fim !!!")
        break

    elif (opcao != 1) or (opcao != 2) or (opcao != 3):
        print("Opção invalida, tente novamente !!!")