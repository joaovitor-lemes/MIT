from funcoes import adicionar_tarefa
from dados import lista

adicionar_tarefa(lista,"Futebol", "Assistir jogo", 3, "pendente")

for i in lista:
    print(i)