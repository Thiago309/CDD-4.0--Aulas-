class conta_bancaria:
    def __init__(self, n_conta, titular, tipo_conta):
        self.n_conta = n_conta
        self.saldo = 0.0
        self.dvdaCredEsp = 0.0
        self.titular = titular
        self.tipo_conta = tipo_conta
        self.status = False
        self.cred_especial = 500.00

    def depositar(self, valor_d):
        if self.status == True:
            if self.dvdaCredEsp < 0:
                self.dvdaCredEsp += valor_d
            else:
                self.saldo += valor_d
                print(self.saldo)
                return self.saldo
        else:
            print("Conta inativa, se direcione ao centro bancário mais próximo da sua residencia ")
            print("para ativar sua conta.")

    def sacar(self, valor_s):
        if self.status == True and self.saldo > 0:
            self.saldo -= valor_s
            print(self.saldo)
            return self.saldo
        elif self.saldo == 0:
            print("Não há valor em sua conta, por favor deposite...")
            print(self.saldo)
        else:
            print("Conta inativa, se direcione ao centro bancário mais próximo da sua residencia")
            print("para ativar sua conta.")
            print(self.saldo)

    def verifSaldo(self):
        if self.status == True:
            print(f"Seu saldo é R${self.saldo:.2f}")
            print(f"Seu saldo de credito especial é R${self.cred_especial:.2f}")
        else:
            print("Conta inativa, se direcione ao centro bancário mais próximo da sua residencia")
            print("para ativar sua conta.")

    def onConta(self):
        if self.status == False:
            self.status = True
            print("Conta Ativada! Seja bem vindo a nossa família !!!")
            print(self.saldo)
        else:
            print("A conta já encontra-se ativa !")

    def offConta(self):
        if self.status == True:
            self.status = False
            print("Conta Desativada! Iremos sentir sua falta, volte novamente! =(")
            print(self.saldo)
        else:
            print("A conta já encontra-se desativada !")

    def aumLimite(self, CredEsp):
        if self.status == True:
            print(f"Seu saldo atual de Credito Especial é: {self.cred_especial:.2f}.")
            print("Informe o valor o valor que você deseja solicitar para aumentar seu credito.")
            self.cred_especial += CredEsp
            return self.cred_especial
        else:
            print("Conta inativa, se direcione ao centro bancário mais próximo da sua residencia")
            print("para ativar sua conta.")

    def credEspecial(self, vCred):
        if self.status == True:
            if self.saldo < 0 and vCred <= self.cred_especial:
                self.dvdaCredEsp = (self.dvdaCredEsp + vCred) * -1
                return self.dvdaCredEsp
        else:
            print("Conta inativa, se direcione ao centro bancário mais próximo da sua residencia")
            print("para ativar sua conta.")