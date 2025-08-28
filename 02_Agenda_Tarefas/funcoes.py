from dados import lista
from produto import Tarefa


# Criação das funções 

def adicionar_tarefa(list, titulo, descricao, prioridade, status):

    nova_tarefa = Tarefa(titulo, descricao, prioridade, status)
    return lista.append(nova_tarefa)


  