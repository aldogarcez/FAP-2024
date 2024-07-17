def criptografar(frase):
    resultado = ""
    for char in frase:
        if  char in minusculo:
            indice = minusculo.index(char)

            if  indice >= 23:
                indice = indice - 26

            nova_posicao = indice + 3

            novo_char = minusculo[nova_posicao]

            resultado += novo_char
        elif char in maiusculo:
            indice = maiusculo.index(char)

            if  indice >= 23:
                indice = indice - 26

            nova_posicao = indice + 3

            novo_char = maiusculo[nova_posicao]

            resultado += novo_char
        else:
            resultado += char
    return resultado

# Exemplo de uso
minusculo = 'abcdefghijklmnopqrstuvwxyz'
maiusculo = minusculo.upper()

frase = input("Digite uma frase para criptografar: ")
frase_criptografada = criptografar(frase)
print("Frase original:", frase)
print("Frase criptografada:", frase_criptografada)
