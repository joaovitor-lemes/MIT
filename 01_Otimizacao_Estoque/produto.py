
"""Criação da Classe Produto"""

class Produto:

    """Classe criada para representar um item disponível no estoque"""

    def __init__(self, nome:str, preco:float, demanda:float):

        if preco < 0:
            raise ValueError("Digite um preço maior que zero!")
        
        if demanda < 0:
            raise ValueError("A Demanda não pode ser negativa!")
        
        if not isinstance(nome,str) or not nome.strip():
            raise ValueError("O nome não pode estar vazio")
        
        # atributos de instância

        self.nome = nome
        self.preco = preco
        self.demanda = demanda

    def __str__ (self) -> str:

        return f"Nome: {self.nome} (Preço: {self.preco: .2f}, Demanda: {self.demanda})"

       


