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