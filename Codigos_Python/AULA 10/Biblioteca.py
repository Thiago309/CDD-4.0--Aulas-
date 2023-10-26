def soma (n1, n2):
    r = n1 + n2
    print(f"Sua soma é: {r:.2f}")

def sub (n1 , n2):
    r = n1 - n2
    print(f"Sua subtração é: {r:.2f}")

def mult (n1, n2):
    r = n1 * n2
    print(f"Sua multiplicação é: {r:.2f}")

def div (n1,n2):
    r = n1 / n2
    print(f"Sua divisão é: {r:.2f}")

def piram(n):
    e = 1
    while (e <= n):
        u = 1
        while (u <= e):
            print(u, end = " ")
            u += 1
        print()     # Quando o print estiver sem string, ele printa o \n,pois já é definida na biblioteca
        e += 1

def Piramide(n):
    n = 0
    for e in range(1, n+1):
        print(str(e) * e)

def rall(n):
    for e in range(n+1):
        for u in range(1, e + 1):
            print(u, end = " ")
        print()

def totalVogais(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont += 1
    print(f"O total de vogais é {cont}")

def estoque(produto, quantidade, valor):
    vTotal = quantidade * valor
    return vTotal

def vogais(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont += 1