perguntas = [
    "Qual é o maior país do mundo?",
    "Qual é a capital do Brasil?",
    "Quantos continentes exsitem no mundo?",
    "Qual país tem a maior população do mundo?",
    "Qual o oceano é o maior do mundo?",
    "Qual é o menor país do mundo?",
    "Qual é o continente mais populoso do mundo?",
    "Qual é o maior rio do mundo?",
    "Qual país é conhecido como Terra do Sol Nascente?",
    "Qual é o deserto mais quente do mundo?"
]

opcoes = [
    ["A) Estados Unidos", "B) China", "C) Rússia", "D) Brasil"],
    ["A) Brasília", "B) Acre", "C) Berlim", "D) Natal", "E) Recife"],
    ["A) 5", "B) 6", "C) 7", "D) 8"],
    ["A) Índia", "B) China", "C) Brasil", "D) Japão", "E) Espanha"],
    ["A) Pacífico", "B) Ártico", "C) Atlântico", "D) Nenhuma das respostas anteriores"],
    ["A) Vaticano", "B) Mônaco", "C) Malta", "D) Luxemburgo"],
    ["A) Europa", "B) África", "C) Ásia", "D) América"],
    ["A) Nilo", "B) Amazonas", "C) Mississipi", "D) Yangtzé"],
    ["A) China", "B) Japão", "C) Coreia do Sul", "D) Tailândia"],
    ["A) Saara", "B) Atacama", "C) Kalahari", "D) Gobi"]
]

respostas = [
    "C", "A", "C", "A", "A", "A", "C", "A", "B", "A"
]

pontuacao = 0

print("=== GeoQuiz: Desafio Global ===\n")

for i in range(len(perguntas)):
    print(perguntas[i])

    for opcao in opcoes[i]:
        print(opcao)

    usuario = input("Digite sua resposta: ").upper()

    if usuario == respostas[i]:
        print("✔️ Acertou!\n")
        pontuacao += 1 
    
    else:
        print(f"❌ Errado! Resposta correta: {respostas[i]}\n")

print(f"🎯 Você fez {pontuacao} acertos de {len(perguntas)} perguntas!")