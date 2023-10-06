def piram(n):
    e = 1
    while (e <= n):
        u = 1
        while (u <= e):
            print(u, end = " ")
            u += 1
        print()     # Quando o print estiver sem string, ele printa o \n,pois já é definida na biblioteca
        e += 1