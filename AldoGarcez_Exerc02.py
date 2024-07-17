def calcular_imposto(salario):
    if salario <= 2259.20:
        aliquota = 0
        deducao = 0
    elif salario <= 2826.65:
        aliquota = 7.5 / 100
        deducao = 169.44
    elif salario <= 3751.05:
        aliquota = 15 / 100
        deducao = 381.44
    elif salario <= 4664.68:
        aliquota = 22.5 / 100
        deducao = 662.77
    else:
        aliquota = 27.5 / 100
        deducao = 896.00
    
    imposto = (salario * aliquota) - deducao
    return imposto

# Testando a função com quatro casos hipotéticos
salarios_teste = [2000, 2500, 3000, 5000]

for salario in salarios_teste:
    imposto = calcular_imposto(salario)
    print(f"Salário: R$ {salario:.2f} - Imposto de Renda: R$ {imposto:.2f}")