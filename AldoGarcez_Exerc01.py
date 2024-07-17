while True:
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))
    if 0.6 < altura < 2.5:
        break
    else:
        print("A altura deve ser maior que 0.6 metros e menor que 2.5 metros. Tente novamente.")

while True:
    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    if 15 < peso < 250:
        break
    else:
        print("O peso deve ser maior que 15 kg e menor que 250 kg. Tente novamente.")

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("Obesidade grau I")
elif imc < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")