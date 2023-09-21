media = 0
flag = 0
flag_2 = 0

while ( flag != 1):

    n1 = float(input("Digite a primeira nota: "))
    if (n1 <= 10) and (n1 >= 0):
        flag = 1
        break

print("Error! Tente novamente com os valores [0~10]")

while ( flag_2 != 1):

    n2 = float(input("Digite a segunda nota: "))
    if (n2 <= 10) and (n2 >= 0):
        flag_2 = 1
        break

print("Error! Tente novamente com os valores [0~10]")

flagLinha = flag + flag_2
media = (n1 + n2) / flagLinha

print(f"Sua média é: {media:.1f}")


#                   CORREÇÃO DO PROFESSOR

resposta = "s"
i = "n"

while (resposta != opcao):

    n1 = float(input("Informe a primeira nota: "))

    while (n1 < 0) or (n1 > 10):
        n1 = float(input("Informe a primeira nota: "))

    n2 = float(input("Informe a primeira nota: "))

    while (n2 < 0) or (n2 > 10):
        n2 = float(input("Informe a primeira nota: "))

    media = (n1 + n2) / 2
    print(media)

    opcao = input("Deseja sair da calculadora ?")
    if (reposta == opcao):
        break