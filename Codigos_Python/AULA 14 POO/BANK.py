class conta_bancaria:
    def __init__(self, n_conta, titular, tipo_conta):
        self.n_conta = n_conta
        self.saldo = 0.0
        self.titular = titular
        self.tipo_conta = tipo_conta
        self.status = False
        self.limite = 500.00

    def depositar(self, valor_d):
        if self.status == True:
            self.saldo += valor_d
            return self.saldo
        else:
            print("Conta inativa, se direcione ao centro bancário mais próximo da sua residencia\n")
            print("para ativar sua conta.")

    def sacar(self, valor_s):
        if self.status == True and self.saldo > 0:
            self.saldo -= valor_s
            return self.saldo
        elif self.saldo == 0:
            print("Não há valor em sua conta, por favor deposite...")
        else:
            print("Conta inativa, se direcione ao centro bancário mais próximo da sua residencia\n")
            print("para ativar sua conta.")

    def verifSaldo(self):
        if self.status == True:
            print(f"Seu saldo é R${self.saldo:.2f}")
        else:
            print("Conta inativa, se direcione ao centro bancário mais próximo da sua residencia\n")
            print("para ativar sua conta.")

    def onConta(self):
        if self.status == False:
            self.satus == True
            print("Conta Ativada! Seja bem vindo a nossa família !!!")
        else:
            print("A conta já encontra-se ativa !")

    def offConta(self):
        if self.status == True:
            self.status == False
            print("Conta Desativada! Iremos sentir sua falta, volte novamente! =(")
        else:
            print("A conta já encontra-se desativada !")
