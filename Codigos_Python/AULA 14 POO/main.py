from BANK import *

opc = "s"

C1 = conta_bancaria("98664", "Jhonny", "Corrente")
while opc in "sS":
    opc2 = int(input('''Informe a opção que deseja utilizar:
                    1 - Depositar;
                    2 - Sacar;
                    3 - Verificar o Saldo;
                    4 - Ativ. a Conta;
                    5 - Desativ. a Conta; 
                    6 - Aum. Limite Cred. Especial;
                    7 - Usar Cred. Especial;
                    8 - Sair.\n
                        Informe: '''))

    if opc2 == 1:
        valor_d = float(input("Informe o valor que você deseja depositar em R$: "))
        C1.depositar(valor_d)
    elif opc2 == 2:
        valor_s = float(input("Informe o valor que você deseja sacar em R$: "))
        C1.sacar(valor_s)
    elif opc2 == 3:
        C1.verifSaldo()
    elif opc2 == 4:
        C1.onConta()
    elif opc2 == 5:
        C1.offConta()
    elif opc2 == 6:
        CredEsp = float(input("Informe o valor que você deseja solicitar para o aumento do limite: "))
        C1.aumLimite(CredEsp)
    elif opc2 == 7:
        vCred = float(input("Informe o valor do credito especial que você deseja usar: "))
        C1.credEspecial(vCred)
    elif opc2 == 8:
        opc = input("Ainda deseja continuar a utilizar nossos serviços (s/n)? ")