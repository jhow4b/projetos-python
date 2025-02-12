def menu():
    print("Burguer King")
    print("1- Combos promocionais")
    print("2- Lanches")
    print("3- Bebidas")
    print("4- Sobremesas")
    print("5- Editar pedido")
    print("6- FINALIZAR COMPRA")

def leiaInt(text):
    while True:
        try:
            resp = int(input(text))
        except(ValueError, TypeError):
            print("OPÇÃO INVALIDA! Digite apenas numeros!")
        except(KeyboardInterrupt):
            print("Usuario finalizou a execução")
            break
        else:
            return resp

def mostrarItens(lista, msg, pos):
    print(msg)
    count = 1
    for i in lista[pos]:
        print(f"{count}- {i['item']}: R${i['preço']:.2f}".replace(".", ","))
        count += 1
    print(f"{count}- Voltar")

def fazerPedido(itens, listNum, carrinho):
    while True:
        choice = leiaInt("Qual sua escolha? ")
        if choice > len(itens) or choice <= 0:
            print("ERRO! Digite um valor valido!")
        elif choice == len(itens):
            break
        else:
            carrinho.append(itens[listNum][choice - 1])
            print("ITEM ADICIONADO NO CARRINHO!")
            return carrinho
        
def mostrarCarrinho(carrinho):
    print("=-"*30)
    soma = 0
    print("Seu Carrinho")
    for i in carrinho:
        print(f"- {i['item']}")
        soma += i["preço"]
    print(f"Valor total: R${soma:.2f}".replace(".", ","))
    print("=-"*30)

def listarItens(carrinho):
    count = 1
    for i in carrinho:
        print(f"{count}- {i['item']} R${i['preço']:.2f}".replace(".", ","))
        count += 1
    print(f"{len(carrinho) + 1}- Voltar")

def editarPedido(carrinho, msg, isDuplicar=True):
    while True:
        item = leiaInt(msg)
        if item == len(carrinho) + 1:
            break
        elif item > len(carrinho) + 1 or item <= 0:
            print("Opção invalida!")
        else:
            if isDuplicar == True:
                temp = carrinho[item - 1]
                carrinho.append(temp)
                temp = []
                mostrarCarrinho(carrinho)
                print("ITEM DUPLICADO!")
                return carrinho
            else:
                carrinho.remove(carrinho[item - 1])
                mostrarCarrinho(carrinho)
                print("ITEM EXCLUIDO")
                return carrinho