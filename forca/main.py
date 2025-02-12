import random

palavras = ["python", "java", "kotlin", "javascript", "ruby", "swift"]
escolhida = random.choice(palavras)
mostrarLetras = ["_" for _ in escolhida]
tentativas = 8

while tentativas > 0 and "_" in mostrarLetras:
    print("\n" + " ".join(mostrarLetras))
    resp = input("Adivinhe: ").lower()
    if resp in escolhida:
        for index, letra in enumerate(escolhida):
            if letra == resp:
                mostrarLetras[index] = resp
    else:
        print("NAO TEM ESSA LETRA")
        tentativas -= 1
        print(f"Voce tem apenas {tentativas} tentativas")

if "_" not in mostrarLetras:
    print("VOCE VENCEU!")
    print(f"A palavra era {escolhida}")
else:
    print("Voce perdeu!")
    print(f"A palavra era {escolhida}")