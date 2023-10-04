# Arrays
qtd = int(input("Informe a quantidade de alunos presente em sala: "))
alunos = [" "] * qtd
e = [" "] * qtd

for i in range(qtd):
    alunos[i] = input(f"Informe o nome do aluno {i + 1}: ")

for t in range(qtd):
    print(f"{alunos[t]} está na posição {t}")

