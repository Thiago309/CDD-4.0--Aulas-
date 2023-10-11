def texto(a):
    cont = 0
    for x in a:
        if x not in " ":
            cont += 1
    print(cont)

    for i in range(len(a)-1, -1, -1):
        print(a[i], end = "")