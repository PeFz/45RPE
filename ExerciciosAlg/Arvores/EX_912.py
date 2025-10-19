# Apresente o pseudocódigo de um algoritmo que conta o número de folhas em uma árvore binária que são
# filhas esquerdas dos seus respectivos pais.

def contar_folhas(raiz, filho_esquerdo):
    if raiz is None:
        return 0
    if raiz.esquerda is None and raiz.direita is None:
        if filho_esquerdo:
            return 1
        else:
            return 0
    else:
        return contar_folhas(raiz.filho_esquerdo, True) + contar_folhas(raiz.direita, False)