from lib.functions import *
from time import sleep

orçamento = leiaFloat("Digite o seu orçamento: R$")
total = 0
soma = 0
despesa = {}
listaDespesa = []

while True:
    sleep(2)
    menu()
    resp = leiaInt("Qual sua escolha? ")
    if resp == 1:
        nomeDesp = str(input("Digite o nome do produto: "))
        preço = leiaFloat("Digite o preço do produto: R$")
        soma = preço + total
        if soma <= orçamento:
            total += preço
            soma = 0
            adicionarDespesas(nomeDesp, preço, despesa, listaDespesa)
        else:
            print("ERRO! Ultrapassou o limite do orçamento")

    elif resp == 2:
        print(f"Orçamento total: R${orçamento:.2f}")
        print("Despesas:")
        for i, k in enumerate(listaDespesa):
            print(f"{i + 1}- {k['descricao']}: R${k['valor']:.2f}")
        print(f"TOTAL GASTO: R${total:.2f}")

    elif resp == 3:
        print("FINALIZANDO O PROGRAMA!")
        break
    
    else:
        print("Opção invalida!")