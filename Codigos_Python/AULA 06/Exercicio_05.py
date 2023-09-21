    # n = int(input("Digite a quantidade: "))
    # e = 0
    # u = 0
    #
    # while (e != n+1):
    #     e = e + 1
    #     while (u != e+1):
    #         print(u * str(e))
    #         u = u + 1
    # print()

n = int(input("Digite a quantidade: "))
e = 1

while (e <= n):
    u = 1
    while ( u <= e):
        print(u, end = " ")
        u += 1
    print()     # Quando o print estiver sem string, ele printa o \n,pois já é definida na biblioteca
    e += 1