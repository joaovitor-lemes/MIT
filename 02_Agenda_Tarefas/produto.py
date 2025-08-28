''' Criando a Classe Tarefa'''

class Tarefa():

    def __init__(self, titulo:str, descricao:str, prioridade:int, status:str):

        
        if prioridade > 6 or prioridade <0:
            raise ValueError("Digite um valor entre 1 e 5")
        
              
        
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        
        
        
    def __str__ (self) -> str:

        return f"Título: {self.titulo} | Descrição: {self.descricao} | Prioridade: {self.prioridade} | Status: {self.status} "
        
        













