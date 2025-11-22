import sys
import os
import networkx as nx


def ler_col(pasta, nome_arquivo):
    """Lê um arquivo .col e retorna o grafo NetworkX."""
    caminho = os.path.join(pasta, nome_arquivo)
    G = nx.Graph()

    with open(caminho, "r") as f:
        for linha in f:
            linha = linha.strip()
            if linha.startswith("c") or linha.startswith("p"):
                continue
            if linha.startswith("e"):
                _, u, v = linha.split()
                G.add_edge(int(u), int(v))

    return G


def conjunto_dominante(G):
    """
    Implementa o algoritmo do PDF para conjunto dominante aproximado.
    """

    C = set(G.nodes())             # vértices ainda não processados
    S = set()                      # conjunto dominante final
    dominado = {v: False for v in G.nodes()}   # marca quem já está dominado

    while C:
        # escolhe vértice com mais vizinhos NÃO dominados
        v = max(C, key=lambda x: sum(not dominado[n] for n in G.neighbors(x)))

        # se ele não é dominado ou tem vizinho não dominado, deve entrar no conjunto dominante
        if not dominado[v] or any(not dominado[n] for n in G.neighbors(v)):
            S.add(v)

            dominado[v] = True
            for n in G.neighbors(v):
                dominado[n] = True

        C.remove(v)

    return sorted(S)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Uso: python dom.py arquivo.col")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    pasta = os.path.join(os.getcwd(), ".cols")

    G = ler_col(pasta, nome_arquivo)
    S = conjunto_dominante(G)

    tamanho = len(S)
    elementos = " ".join(str(v) for v in S)

    print(f"{tamanho} ({elementos})")
