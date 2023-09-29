# opc = int(input("Digite qual função vocÊ deseja usar [1 ~ Antecessor], [2 ~ Sucessor] & [3 ~ Sair]: "))
#
# a = 0
# b = 0
# c = 0
# while (opc != 3):
#     if (c != 0):
#         opc = int(input("Digite qual função você deseja usar [1 ~ Antecessor], [2 ~ Sucessor] & [3 ~ Sair]: "))
#
#     n = int(input("Digite o valor que deseja calcular: "))
#
#     if (opc == 1):
#         a = n - 1
#         print("Função [Antecessor] selecionada !!!")
#         print(f"O antecessor de {n} é: {a}")
#         c += 1
#
#     elif (opc == 2):
#         s = n + 1
#         print("Função [Sucessor] selecionada !!!")
#         print(f"O sucessor de {n} é: {s}")
#         c += 1
#
#     else:
#         print("Opção invalida, tente novamente !")
#         c += 1
#
# print("Obrigado(a) por usar nossos serviços, até a próxima !")

a = 0
b = 0
c = 0
while True:

    n = int(input("Digite o valor que deseja calcular: "))
    opc = int(input("Digite qual função você deseja usar [1 ~ Antecessor], [2 ~ Sucessor] & [3 ~ Sair]: "))


    if (opc == 1):
        a = n - 1
        print("Função [Antecessor] selecionada !!!")
        print(f"O antecessor de {n} é: {a}")

    elif (opc == 2):
        s = n + 1
        print("Função [Sucessor] selecionada !!!")
        print(f"O sucessor de {n} é: {s}")

    else:
        print("Obrigado(a) por usar nossos serviços, até a próxima !")
        break