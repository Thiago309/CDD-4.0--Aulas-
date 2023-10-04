nota_1 = float(input("Por favor, digite a Primeira nota:"))
nota_2 = float(input("Por favor, digite a Segunda nota:"))
nota_3 = float(input("Por favor, digite a Terceira nota:"))

Media = 7.0

Calc_media = (nota_1 + nota_2 + nota_3) / 3

if (nota_1 or nota_2 or nota_3) > 10 or (nota_1 or nota_2 or nota_3) < 0:
    print("Alguma nota foi digitada incorretamente. Por favor, tente nomamente com valores entre ( 0 ~ 10 )")

else:
    if Calc_media < Media:
        if Calc_media < 4:
            print(f"Aluno reprovado por média, sua nota geral foi {Calc_media:.2f}, media para aprovação insuficiente...")

        else:
            print(
                f"Sua média: {Calc_media:.2f}. É insuficiente para aprovação do aluno, porém o aluno poderar fazer a avaliação RECUPERATIVA para ser aprovado.")

    else:
        print(f"Parabéns aluno, sua média é {Calc_media:.2f}, você foi aprovado por média !!!")