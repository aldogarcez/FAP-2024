def remover_vogais(texto):
    vogais = "aeiouAEIOU"
    texto_novo = ""
    for char in texto:
        if char not in vogais:
            texto_novo += char
    return texto_novo

# Exemplo de uso
texto = "Aldo Martins Garcez"
texto_novo = remover_vogais(texto)
print("Texto original:", texto)
print("Texto sem vogais:", texto_novo)