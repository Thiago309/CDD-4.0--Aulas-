entrada_1h = 3          #primeira entrada horas
entrada_1m = 45         #primeira entrada minutos

entrada_2h = 14         #segunda hora
entrada_2m = 20         #segundo minuto


if entrada_1m >= 60:
    minuto_a = entrada_1m - 60
    flag = 1

if entrada_2m >= 60:
    minuto_b = entrada_1m - 60
    flag = 1

if entrada_1h > 12:
    conversor_1 = entrada_1h - 12

if entrada_2h > 12:
    conversor_2 = entrada_2h - 12

hora_a = flag + conversor_1 + conversor_2
minutos_a =conversor_1 + conversor_2

print(f"{hora_a}:{minuto_a}")

if (entrada_1h < 24):
    print(f"{hora}:{minutos}")
