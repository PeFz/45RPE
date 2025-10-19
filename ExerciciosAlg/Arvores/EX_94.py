# Escreva um algoritmo recursivo que conta os nodos de uma árvore binária.

def contar_nodos(arvore):
    if arvore is None:
        return 0
    return 1 + contar_nodos(arvore.esquerda) + contar_nodos(arvore.direita)