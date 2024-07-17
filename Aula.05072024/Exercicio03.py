def classificar_respostas(respostas_positivas):
    if respostas_positivas == 0 or respostas_positivas == 1:
        return "Inocente"
    elif respostas_positivas == 2:
        return "Suspeita"
    elif respostas_positivas == 3 or respostas_positivas == 4:
        return "Cúmplice"
    elif respostas_positivas == 5:
        return "Assassino"

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas_positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").strip().lower()
    while resposta not in ("sim", "não"):
        print("Resposta inválida! Por favor, responda com 'sim' ou 'não'.")
        resposta = input(pergunta + " (sim/não): ").strip().lower()
    
    if resposta == "sim":
        respostas_positivas += 1

print(f"A classificação da pessoa é: {classificar_respostas(respostas_positivas)}")
