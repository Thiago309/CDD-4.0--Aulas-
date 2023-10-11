def ler(*frase):
    cont = 0
    letra = len(frase)
    for i in frase:
        if i != None:
            cont += 1

    return cont