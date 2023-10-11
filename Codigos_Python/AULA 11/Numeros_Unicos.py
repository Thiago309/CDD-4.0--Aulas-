def repeticao(A):
    A = [1, 2, 2, 3, 4, 4, 5, 3, 6, 7, 6, 8]
    B = []

    for x in A:
        if x not in B:
            B.append(x)

    return B

# Cai bastantes em processos seletivos.