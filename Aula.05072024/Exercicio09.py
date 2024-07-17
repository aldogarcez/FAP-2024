def intercalar_listas(lista1, lista2):
    if len(lista1) != 10 or len(lista2) != 10:
        raise ValueError("Ambas as listas devem conter exatamente 10 elementos.")
    
    lista_intercalada = []
    
    for i in range(10):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])
    
    return lista_intercalada

# Exemplo de uso
lista1 = list(range(1, 20, 2))
lista2 = list(range(2, 21, 2))

print("Lista intercalada:", intercalar_listas(lista1, lista2))
