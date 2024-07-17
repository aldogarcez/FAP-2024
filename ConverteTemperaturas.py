def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def converter_temperatura():
    opcao = input("Você utiliza Celsius (C) ou Fahrenheit(F)?")
    
    if opcao not in ['C', 'F']:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return
    
    temperatura = float(input("Digite a temperatura que deseja converter: "))
    
    if opcao == 'C':
        resultado = celsius_para_fahrenheit(temperatura)
        print(f"{temperatura}°C é igual a {resultado}°F.")
    else:
        resultado = fahrenheit_para_celsius(temperatura)
        print(f"{temperatura}°F é igual a {resultado}°C.")

# Inicia o conversor de temperatura
converter_temperatura()
