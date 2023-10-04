time_1 = input("Digite o nome do primeiro time: ")
qtd_time1 = int(input("Digite o numero de gols que o time marcou: "))

time_2 = input("Digite o nome do segundo time: ")
qtd_time2 = int(input("Digite o numero de gols que o time marcou: "))


if qtd_time1 == qtd_time2:
    print("EMPATE")

else:
    if qtd_time1 > qtd_time2:
        print(f"O time do {time_1} marcou {qtd_time1} e venceu a partida, parabéns !!!")
    else:
        print(f"O time do {time_2} marcou {qtd_time2} e venceu a partida, parabéns !!!")