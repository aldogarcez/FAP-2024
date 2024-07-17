def classifica(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 11:
        return "Infantil B"
    elif idade >= 12 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    elif idade >= 18:
        return "Adultos"
    else:
        return "Idade fora das categorias"

# Solicita a idade do nadador
try:
    idade = int(input("Digite a idade do nadador: "))
    categoria = classifica(idade)
    print(f"A categoria do nadador é: {categoria}")
except ValueError:
    print("Por favor, insira um número válido para a idade.")
