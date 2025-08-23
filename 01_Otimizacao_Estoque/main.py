from dados import produtos
from funcoes import soma_demanda, soma_preco, listar_produtos, calcular_orcamento, melhor_combinacao, melhor_combinacao_greedy

"""
    Função principal do sistema de otimização de estoque
"""

while True:


    print("===========OPÇÕES================")
    print("1 - Digite seu Orçamento")
    print("2 - Listar os produtos disponíveis")
    print("3 - Sair")
    
    question = input("Escolha uma das opções: ").strip() # esse strip resolveu um bug de quando estava dando enter e o código nao entrava no if

    if question == "1":
        orcamento = float(input("Digite o orçamento disponível: \n"))
        melhor_combinacao_greedy(produtos, orcamento)


    elif question == "2":
        listar_produtos(produtos)

    elif question == "3":
        print("Saindo do Sistema...")
        break

    else:
        print("Digite um valor válido")
 
        
