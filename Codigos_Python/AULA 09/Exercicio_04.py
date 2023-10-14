n = [" "] * 5
soma = 0
a = 0
r = 0

for i in range(5):
    n[i] = float(input(f"Digite a nota do aluno {i + 1}: "))

for m in range(5):
    soma = soma + n[m]

media = soma / 5
for t in range(5):
    if n[t] >= media:
        a += 1

    elif n[t] < media:
        r += 1

print(f"\nAs notas da turma foram {n}")
print(f"A média geral da turma é: {media}")
print(f"Foram aprovados {a} alunos e {r} reprovados...")