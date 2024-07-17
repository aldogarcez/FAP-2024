import random

numero = random.randint(0,100)
tentativas = 0

while True:
    try:
        valor = int(input("Digite um número inteiro entre 0 e 100: "))
        
        if  0 < valor > 100:
            print("Por favor, digite um número entre 0 e 100.")
        elif  valor > numero:
            print("Você digitou um valor MAIOR que o número secreto")
        elif valor < numero:
            print("Você digitou um valor MENOR que o número secreto")
        else:
            break;
        
        tentativas += 1
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

print(f"Você acertou em {tentativas} tentativas")