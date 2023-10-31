from BANK import *

opc = "n"
C1 = conta_bancaria("98664", "Jhonny", "Corrente")

while opc in "sS":
    opc = input('''Informe a opção que deseja utilizar:
                    1 - Depositar;
                    2 - Sacar;
                    3 - Verificar o Saldo;
                    4 - Ativ. a Conta;
                    5 - Desativ. a Conta.''')

    if opc == 1:
        valor_d = float(input("Informe o valor que você deseja depositar em R$:"))
        C1.depositar(valor_d)

    elif opc == 2:
        valor_s = float(input("Informe o valor que você deseja sacar em R$: "))
        C1.sacar(valor_s)

    elif opc == 3:
        C1.verifSaldo()

    elif opc == 4:
        C1.onConta()

    elif opc == 5:
        C1.offConta()


    opc = input("Ainda deseja continuar a utilizar nossos serviços (s/n) ?")