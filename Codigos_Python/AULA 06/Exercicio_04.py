n = int(input("Digite a quantidade: "))
e = 0
u = 0

while (e != n+1):
    e = e + 1
    while (u != e+1 ):
        print(u * str(e), end = " ")
        u = u + 1
print()