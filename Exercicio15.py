def comprimir(texto):
    
    resultado = ""
    contador = 1

    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            contador += 1
        else:
            resultado += str(contador) + texto[i - 1]
            contador = 1

    # Adiciona o último conjunto de caracteres
    resultado += str(contador) + texto[-1]

    return resultado

# Exemplo de uso
string = "aabbbccccddddd"

print(f"String original: {string}")
print(f"String comprimida: {comprimir(string)}")
