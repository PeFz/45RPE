#bubbleSort
def arrumaLista(a):
    n = len(a)
    trocou = True
    while trocou:
        trocou = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                trocou = True
        n -= 1
    return a

#BuscaBin
def busca_binaria(lista, alvo):
    esq, dir = 0, len(lista) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            return meio
        if lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return -1


