from itertools import combinations

def calcular_orcamento(produtos):
    resultado = {}
    for p in produtos:
        resultado[p.nome] = p.preco * p.demanda
    return print(f"O valor total dos produtos é de {resultado}\n")


def soma_demanda(produtos):
    contador = 0
    for p in produtos:
        contador += p.demanda
    return print(f"A Demanda total é de {contador} unidades\n")


def listar_produtos(list):
    print("=== PRODUTOS EM ESTOQUE ===")
    print("--------------------------")
    print("Nome | Preço | Demanda  ")
    print("--------------------------")

    for p in list:
        print(f"{p.nome} | {p.preco  } | {p.demanda  }")
        print("--------------------------")


def soma_preco(list):
    contador = 0
    for p in list:
        contador += p.preco*p.demanda
    return print(f"O valor total é de R$ {contador} \n")

def melhor_combinacao(produtos, orcamento):
    melhor_valor =0
    melhor_combo = []

    for r in range(1, len(produtos)+1):
        for combo in combinations(produtos,r):
            preco_total = sum(p.preco for p in combo)
            demanda_total = sum(p.demanda for p in combo)

            if preco_total <= orcamento and demanda_total > melhor_valor:
                melhor_valor = demanda_total
                melhor_combo = combo

    print("\n Melhor Combinação encontrada: ")
    for p in melhor_combo:
        print(f"{p.nome} | Preço: {p.preco} | Demanda: {p.demanda}")
    print(f"Demanda Total Atendida: {melhor_valor}")
    print(f"Custo Total: {sum(p.preco for p in melhor_combo)}")


#Algoritmo Greedy

def melhor_combinacao_greedy(produtos, orcamento):

    """
    Seleciona produtos de forma rápida usando abordagem gananciosa:
    escolhe sempre o produto com maior demanda por preço até acabar o orçamento.
    """

    produtos_ordenados = sorted(produtos, key = lambda p:p.demanda/p.preco, reverse = True)

    melhor_combo =[]
    gasto_total = 0
    demanda_total = 0

    for p in produtos_ordenados:
        if gasto_total + p.preco <=orcamento:
            melhor_combo.append(p)
            gasto_total +=p.preco*p.demanda
            demanda_total += p.demanda

    # Exibe resultado
    print("\nCombinação sugerida (greedy):")
    for p in melhor_combo:
        print(f"- {p.nome} | Preço: {p.preco} | Demanda: {p.demanda}")
    print(f"Demanda total atendida: {demanda_total}")
    print(f"Custo total: {gasto_total}")



