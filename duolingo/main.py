import random

palavras = [
    {"english": "the", "portugues": "o/a"},
    {"english": "be", "portugues": "ser/estar"},
    {"english": "to", "portugues": "para"},
    {"english": "of", "portugues": "de"},
    {"english": "and", "portugues": "e"},
    {"english": "a", "portugues": "um/uma"},
    {"english": "in", "portugues": "em"},
    {"english": "that", "portugues": "que"},
    {"english": "have", "portugues": "ter"},
    {"english": "I", "portugues": "eu"},
    {"english": "it", "portugues": "isso/ele/ela"},
    {"english": "for", "portugues": "para"},
    {"english": "not", "portugues": "não"},
    {"english": "on", "portugues": "em"},
    {"english": "with", "portugues": "com"},
    {"english": "he", "portugues": "ele"},
    {"english": "as", "portugues": "como"},
    {"english": "you", "portugues": "você"},
    {"english": "do", "portugues": "fazer"},
    {"english": "at", "portugues": "em"},
    {"english": "this", "portugues": "isto/esse"},
    {"english": "but", "portugues": "mas"},
    {"english": "his", "portugues": "dele"},
    {"english": "by", "portugues": "por"},
    {"english": "from", "portugues": "de"},
    {"english": "they", "portugues": "eles/elas"},
    {"english": "we", "portugues": "nós"},
    {"english": "say", "portugues": "dizer"},
    {"english": "her", "portugues": "dela"},
    {"english": "she", "portugues": "ela"},
    {"english": "or", "portugues": "ou"},
    {"english": "an", "portugues": "um/uma"},
    {"english": "will", "portugues": "irá"},
    {"english": "my", "portugues": "meu/minha"},
    {"english": "one", "portugues": "um"},
    {"english": "all", "portugues": "todos"},
    {"english": "would", "portugues": "iria"},
    {"english": "there", "portugues": "lá"},
    {"english": "their", "portugues": "deles/delas"},
    {"english": "what", "portugues": "o que"},
    {"english": "so", "portugues": "então"},
    {"english": "up", "portugues": "para cima"},
    {"english": "out", "portugues": "fora"},
    {"english": "if", "portugues": "se"},
    {"english": "about", "portugues": "sobre"},
    {"english": "who", "portugues": "quem"},
    {"english": "get", "portugues": "obter"},
    {"english": "which", "portugues": "qual"},
    {"english": "go", "portugues": "ir"},
    {"english": "me", "portugues": "mim"},
    {"english": "when", "portugues": "quando"},
    {"english": "make", "portugues": "fazer"},
    {"english": "can", "portugues": "poder"},
    {"english": "like", "portugues": "gostar"},
    {"english": "time", "portugues": "tempo"},
    {"english": "no", "portugues": "não"},
    {"english": "just", "portugues": "apenas"},
    {"english": "him", "portugues": "ele"},
    {"english": "know", "portugues": "saber"},
    {"english": "take", "portugues": "pegar"},
    {"english": "people", "portugues": "pessoas"},
    {"english": "into", "portugues": "dentro"},
    {"english": "your", "portugues": "seu"},
    {"english": "good", "portugues": "bom"},
    {"english": "some", "portugues": "algum"},
    {"english": "could", "portugues": "poderia"},
    {"english": "them", "portugues": "eles/elas"},
    {"english": "see", "portugues": "ver"},
    {"english": "other", "portugues": "outro"},
    {"english": "than", "portugues": "do que"},
    {"english": "then", "portugues": "então"},
    {"english": "now", "portugues": "agora"},
    {"english": "look", "portugues": "olhar"},
    {"english": "only", "portugues": "somente"},
    {"english": "come", "portugues": "vir"},
    {"english": "its", "portugues": "seu"},
    {"english": "over", "portugues": "sobre"},
    {"english": "think", "portugues": "pensar"},
    {"english": "also", "portugues": "também"},
    {"english": "back", "portugues": "voltar"},
    {"english": "after", "portugues": "depois"},
    {"english": "use", "portugues": "usar"},
    {"english": "two", "portugues": "dois"},
    {"english": "how", "portugues": "como"},
    {"english": "our", "portugues": "nosso"},
    {"english": "work", "portugues": "trabalho"},
    {"english": "first", "portugues": "primeiro"},
    {"english": "well", "portugues": "bem"},
    {"english": "way", "portugues": "caminho"},
    {"english": "even", "portugues": "mesmo"},
    {"english": "new", "portugues": "novo"},
    {"english": "want", "portugues": "querer"},
    {"english": "because", "portugues": "porque"},
    {"english": "any", "portugues": "qualquer"},
    {"english": "these", "portugues": "estes/estas"},
    {"english": "give", "portugues": "dar"},
    {"english": "day", "portugues": "dia"}
]

random.shuffle(palavras)

perguntas = []

for i in range(0, 10):
    perguntas.append(palavras[i])

def quiz(lista):
    score = 0
    tempList = []
    count = 1
    for palavra in lista:
        if palavra not in tempList:
            print(f"\nPergunta {count}")
            print(f"Qual a tradução de {palavra['english']}? ")
            tempList.append(palavra)
            resp = input("Sua resposta: ").strip().lower()
            respCorreta = palavra["portugues"].lower()
            count += 1
            if resp == respCorreta:
                print("Voce acertou a resposta!")
                score += 1
            else:
                print(f"Voce errou, a tradução era {respCorreta}")
    print("-" * 40)
    print("\nACABOU!")
    print(f"Sua pontuação foi: {score}")

def main():
    print("Bem vindo ao aplicativo de Linguagem")
    input("Aperte ENTER para começar...")
    quiz(perguntas)

main()