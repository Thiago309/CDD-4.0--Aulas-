# class Pessoa:
#
#     def __init__(self, nome, peso, idade):
#         self.nome = nome
#         self.peso = peso
#         self.idade = idade
#
#     def comer(self, tipoComida):
#         print(f"{self.nome} foi comer {tipoComida}.")
#
#     def dormir(self):
#         print(f"{self.nome} foi dormir.")
#
#     def falar(self, falando):
#
#         while True:
#             if falando in "sS":
#                 print(f"{self.nome} está falando.")
#                 break
#
#     def pararfalar(self, falando):
#         while True:
#             if falando in "nN":
#                 print(f"{self.nome}, parou de falar.")
#                 break
#             else:
#                 print(f"{self.nome} ainda continua falando...")
#                 continue


# CORREÇÃO PROFESSOR

class Pessoa:

    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comedo = False
        self.dormir = False
        self.falar = False

    def comer(self, tipo):
        if self.comendo == True:
            print(f"{self.nome} já está comendo {tipo}.")
        else:
            print(f"{self.nome} foi comer agora {tipo}.")
            self.comendo = True

    def pararComer(self):
        if self.comendo == True:
            self.comendo = False
        else:
            print("Eu não estou comendo.")

    def dormir(self):
        if self.dormir == True:
            print(f"{self.nome} já está dormindo.")
        else:
            print(f"{self.nome} foi dormir agora.")

    def acordar(self):
        if self.dormir == True:
            print("Acordei !!!")
        else:
            print("Já estou acordado !")

    def falar(self):
        if self.comendo == False:
            if self.falar == True:
                print(f"{self.nome} já está falando.")
            else:
                print(f"{self.nome} falou agora.")
        else:
            print("Não posso falar, estou comendo. Eu tenho educação, não sou cavalo pra comer de boca cheia !")

    def pararFalar(self):
        if self.falar == False:
            print("Eu não estou falando")
        else:
            print("Parei de falar")