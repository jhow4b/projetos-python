def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except(ValueError, TypeError):
            print("ERRO! DIGITE UM VALOR VALIDO!")
            continue
        except(KeyboardInterrupt):
            print("Usuario optou por encerrar o programa!")
            break
        else:
            return valor

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except(ValueError, TypeError):
            print("ERRO! DIGITE UM VALOR VALIDO!")
            continue
        except(KeyboardInterrupt):
            print("Usuario optou por encerrar o programa!")
            break
        else:
            return valor

def menu():
    print("O que voce gostaria de fazer?")
    print("1. Adicionar despesa")
    print("2. Mostrar detalhes do orçamento")
    print("3. Sair")


def adicionarDespesas(nome, valor, despesa, listaDespesa):
    despesa.clear()
    despesa["descricao"] = nome
    despesa["valor"] = valor
    listaDespesa.append(despesa.copy())
    print(f"Item {despesa['descricao']} adicionado no valor de R${despesa['valor']:.2f}")
    return listaDespesa