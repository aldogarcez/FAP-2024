intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0

while True:
    try:
        numero = int(input("Digite um número positivo (ou um número negativo para encerrar): "))

        if numero < 0:
            break

        if 0 <= numero <= 25:
            intervalo_1 += 1
        elif 26 <= numero <= 50:
            intervalo_2 += 1
        elif 51 <= numero <= 75:
            intervalo_3 += 1
        elif 76 <= numero <= 100:
            intervalo_4 += 1

    except ValueError:
        print("Por favor, insira um número inteiro válido.")

print(f"Quantidade de números no intervalo [  0 -  25]: {intervalo_1}")
print(f"Quantidade de números no intervalo [ 26 -  50]: {intervalo_2}")
print(f"Quantidade de números no intervalo [ 51 -  75]: {intervalo_3}")
print(f"Quantidade de números no intervalo [ 76 - 100]: {intervalo_4}")
