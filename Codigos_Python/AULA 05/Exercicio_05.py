password = ("4321")
t = 2
n = 0

while (n != password):
    n = input("Digite a sua  senha: ")

    if(n != password) and (t != 0):
        print(f"Senha invalida tente novamente, você tem mais {t}")

    elif(n != password) and (t == 0):
        print("Acesso bloqueado, vá para sua agência bancaria e desbloquei seu acesso !")
        break

    t -= 1

else:
    print("Acesso liberado, seja bem vindo!")


    # modo do professor.

secreta = 1234
senha = input("Informe sua senha: ")
cont = 1

while senha != secreta:
    senha = input("Senha errada! Informe sua senha: ")
    