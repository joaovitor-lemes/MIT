# 📦 Projeto 1 – Otimização de Estoque com Algoritmo da Mochila (Knapsack)

## 📖 Descrição

Este projeto implementa um sistema interativo de otimização de estoque, no qual o usuário informa seu orçamento disponível e o programa sugere a melhor combinação de produtos a serem adquiridos.

O problema é inspirado no algoritmo da mochila (Knapsack Problem), amplamente utilizado em otimização, logística e gestão de recursos limitados.

## 🎯 Objetivos do Projeto

* Simular um sistema de compras baseado em orçamento limitado.
  
* Comparar estratégias:
  * Força Bruta (Brute Force): garante a melhor solução absoluta, mas é lento para grandes listas.
  * Greedy (Ganancioso): seleciona produtos mais eficientes (demanda/preço), é rápido, mas pode não ser perfeito.

* Desenvolver habilidades práticas em:

   * Estruturas de dados em Python
   * Estruturas de repetição (for, while)
   * Estruturas condicionais (if/elif/else)
   * Modularização de código (separação em dados.py, funcoes.py e main.py)

## ⚙️ Funcionalidades

* Menu interativo com 3 opções:
  1. Digitar o orçamento disponível
  2. Listar os produtos disponíveis
  3. Sair do sistema

* Implementação do algoritmo de otimização usando Knapsack
* Alternativa com Greedy Algorithm para execução rápida
* Cálculo da demanda total atendida e do custo total

## 🖥️ Exemplo de Execução

~~~~python
============ OPÇÕES ===============
1 - Digite seu Orçamento
2 - Listar os produtos disponíveis
3 - Sair
Escolha uma das opções: 1
Digite o orçamento disponível: 1000
~~~~
### Saída (Algoritmo Greedy)
~~~~python
Combinação sugerida (greedy):
- Lampada | Preço: 10 | Demanda: 10
- Livro | Preço: 10 | Demanda: 9
- Mouse | Preço: 50 | Demanda: 6
- Mesa | Preço: 500 | Demanda: 2
Demanda total atendida: 27
Custo total: 570
~~~~

## 📚 Conceito Teórico – Knapsack Problem

O problema da mochila (Knapsack Problem) é um clássico de otimização combinatória:

  * Temos um conjunto de itens (produtos), cada um com peso/custo e valor/demanda.
  * Queremos maximizar o valor total sem ultrapassar a capacidade (orçamento).

Métodos aplicados:

  * Força Bruta: testa todas as combinações possíveis (garante o ótimo).

  * Greedy: escolhe itens mais “rentáveis” (valor/custo) até não caber mais.



