class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

    def emitirSom(self):
        print(f"O {self.nome} fazendo barulho...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)

    def comer(self):
        print(f"O {self.nome} foi comer ração...")

    def emitirSom(self):
        print(f"O {self.nome} está miando...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)

    def comer(self):
        print(f"O {self.nome} foi comer ração...")

    def emitirSom(self):
        print(f"O {self.nome} está latindo...")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)

    def comer(self):
        print(f"O {self.nome} foi comer cenoura...")

    def emitirSom(self):
        print(f"O {self.nome} está pulando...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)

    def comer(self):
        print(f"O {self.nome} foi comer grama...")

    def emitirSom(self):
        print(f"O {self.nome} mugi...")