# Arrays
qtd = int(input("Informe a quantidade de alunos presente em sala: "))
alunos = [" "] * qtd

proc = " "

for i in range(qtd):
    alunos[i] = input(f"Informe o nome do aluno {i}: ")

proc = input("Digite o nome do aluno para descobrir sua posição: ")
for t in range(qtd):
    if proc in alunos[t]:
        print(f"O {alunos[t]} se encontra na posição {t}.")