from lib.interface import *

itens = [
    [ # Combos
        {
            "item": "Whopper, batata e refri", 
            "preço": 30
        },
        {
            "item": "Whopper em dobro", 
            "preço": 25
        },
        {
            "item": "Rodeio duplo com milkshake", 
            "preço": 28
        },
    ],
    [ # Lanches
        {
            "item": "Whopper",
            "preço": 20
        },
        {
            "item": "Rodeio Duplo",
            "preço": 18
        },
        {
            "item": "Whopper de plantas",
            "preço": 23
        },
    ],
    [ # Bebidas
        {
            "item": "Pepsi 1l",
            "preço": 8
        },
        {
            "item": "Pepsi 2l",
            "preço": 15
        },
        {
            "item": "Coca zero lata 300ml",
            "preço": 4
        },
    ],
    [ # Sobremesas
        {
            "item": "Sorvete",
            "preço": 10
        },
        {
            "item": "Milkshake",
            "preço": 15
        },
        {
            "item": "Petit Gateau",
            "preço": 30
        },
    ]
]
carrinho = []
temp = []

while True:
    print("=-"*30)
    if len(carrinho) > 0:
        mostrarCarrinho(carrinho)
    menu()
    print("=-"*30)
    resp = leiaInt("Qual opção voce deseja? ")
    # Combos
    if resp == 1:
        mostrarItens(itens, "OPÇÕES DE COMBOS", 0)
        fazerPedido(itens, 0, carrinho)

    # LANCHES
    elif resp == 2:
        mostrarItens(itens, "OPÇÕES DE LANCHES", 1)
        fazerPedido(itens, 1, carrinho)

    # BEBIDAS
    elif resp == 3:
        mostrarItens(itens, "OPÇÕES DE BEBIDAS", 2)
        fazerPedido(itens, 2, carrinho)

    # SOBREMESAS
    elif resp == 4:
        mostrarItens(itens, "OPÇÕES DE SOBREMESAS", 3)
        fazerPedido(itens, 3, carrinho)

    # EDITAR PEDIDO
    elif resp == 5:
        while True:
            if len(carrinho) > 0:
                mostrarCarrinho(carrinho)
                print("1- Duplicar um pedido")
                print("2- Excluir um pedido")
                print("3- Voltar")
                opc = leiaInt("O que você gostaria de fazer? ")
                if opc == 1:
                    listarItens(carrinho)
                    editarPedido(carrinho, "Qual opção você quer duplicar? ", True)
                elif opc == 2:
                    listarItens(carrinho)
                    editarPedido(carrinho, "Qual opção você quer excluir? ", False)
                elif opc == 3:
                    print("Voltando pro menu...")
                    break
                else:
                    print("Opção inválida!")
            else:
                print("O seu carrinho está vazio!")
                break

    # ENCERRAR
    elif resp == 6:
        print("FINALIZANDO COMPRA")
        break
    else:
        print("Opção invalida, tente novamente")