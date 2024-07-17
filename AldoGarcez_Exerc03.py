def obter_dimensoes_deposito():
    """Solicita as dimensões do depósito ao usuário e retorna como uma tupla de floats."""
    while True:
        try:
            comprimento = float(input("Digite o comprimento do depósito (em cm): "))
            largura = float(input("Digite a largura do depósito (em cm): "))
            altura = float(input("Digite a altura do depósito (em cm): "))
            return comprimento, largura, altura
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

def selecionar_tipo_bola():
    """Permite ao usuário selecionar um tipo predefinido de bola ou inserir um diâmetro personalizado."""
    tipos_bola = {
        1: ("Bola de Basquete Adulto", 24),
        2: ("Bola de Basquete Infantil", 22),
        3: ("Bola de Futebol Oficial", 22),
        4: ("Bola de Vôlei", 21),
        5: ("Bola de Handball", 19),
        6: ("Bola de Futebol de Salão", 20),
        7: ("Outro tamanho de bola", None)
    }

    print("Selecione o tipo de bola:")
    for key, value in tipos_bola.items():
        print(f"{key} - {value[0]}")

    while True:
        try:
            escolha = int(input("Digite o número correspondente ao tipo de bola: "))
            if escolha in tipos_bola:
                if escolha == 7:
                    diametro = float(input("Digite o diâmetro da bola (em cm): "))
                else:
                    diametro = tipos_bola[escolha][1]
                return diametro
            else:
                print("Por favor, selecione uma opção válida.")
        except ValueError:
            print("Por favor, insira um número válido.")

def calcular_volume_deposito(comprimento, largura, altura):
    """Calcula o volume do depósito."""
    return comprimento * largura * altura

def calcular_volume_bola(diametro):
    """Calcula o volume de uma bola (considerada como um cubo com lados iguais ao diâmetro)."""
    # Aqui, consideramos o volume do cubo circunscrito à bola para simplificação.
    lado = diametro
    return lado ** 3

def estimar_quantidade_bolas(volume_deposito, volume_bola):
    """Estima a quantidade de bolas que caberiam no depósito."""
    return volume_deposito // volume_bola

def exibir_resultado(quantidade_bolas):
    """Exibe o resultado ao usuário."""
    print(f"Quantidade aproximada de bolas que cabem no depósito: {quantidade_bolas}")

def main():
    """Função principal que executa o programa."""
    comprimento, largura, altura = obter_dimensoes_deposito()
    diametro_bola = selecionar_tipo_bola()
    volume_deposito = calcular_volume_deposito(comprimento, largura, altura)
    volume_bola = calcular_volume_bola(diametro_bola)
    quantidade_bolas = estimar_quantidade_bolas(volume_deposito, volume_bola)
    exibir_resultado(quantidade_bolas)

if __name__ == "__main__":
    main()

