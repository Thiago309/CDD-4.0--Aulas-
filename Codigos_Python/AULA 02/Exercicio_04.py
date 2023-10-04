tipo = input("Digite o tipo de combustivel que o cliente deseja abastecer: ")

if (tipo == "G" or tipo == "g") or (tipo == "E" or tipo == "e"):
    litros = int(input("Digite a quantidade de litros foram necessarios: "))

    valor_gas = 5.80
    valor_etanol = 4.90


    if (tipo == "G") or (tipo == "g"):
        valor_final = valor_gas * litros
        print(f"O cliente comprou {litros} litros de gasolina e deverá pagar R$ {valor_final:.2f}")

    elif(tipo == "E") or (tipo == "e"):
        valor_final = valor_etanol * litros
        print(f"O cliente comrpou {litros} litros de etanol e deverá pagar R${valor_final:.2f}")

else:
    print("Opção incorreta, por favor digite novamente com capslock ativo ou não, as seleções (G ou E).")