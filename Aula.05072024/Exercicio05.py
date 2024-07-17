def gerar_intervalo(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1  # Garantir que num1 seja menor ou igual a num2
    return list(range(num1, num2 + 1))

# Solicitar os dois números inteiros ao usuário
try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    
    intervalo = gerar_intervalo(num1, num2)
    print(f"Os números inteiros no intervalo entre {num1} e {num2} são: {intervalo}")
except ValueError:
    print("Por favor, insira números inteiros válidos.")
