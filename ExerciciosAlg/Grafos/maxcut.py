import sys
import os
import networkx as nx


def ler_mc(pasta, nome_arquivo):
    """
    Lê um arquivo .mc e devolve um grafo NetworkX ponderado.

    Formato esperado:
        1ª linha: n m
        Demais:   u v w   (aresta com peso)
    """

    caminho = os.path.join(pasta, nome_arquivo)

    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    G = nx.Graph()

    with open(caminho, "r") as f:
        # Lê n e m
        primeira = f.readline().strip()
        n, m = map(int, primeira.split())

        # Lê as m arestas
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue

            u_str, v_str, w_str = linha.split()
            u = int(u_str)
            v = int(v_str)
            w = float(w_str)

            G.add_edge(u, v, weight=w)

    # Garante que todos os vértices existem
    for v in range(1, n + 1):
        if v not in G:
            G.add_node(v)

    return G


def peso_corte(G, A, B):
    """Soma os pesos das arestas que cruzam A <-> B."""
    total = 0.0
    for u, v, dados in G.edges(data=True):
        w = dados.get("weight", 1.0)
        if (u in A and v in B) or (u in B and v in A):
            total += w
    return total


def sahni_gonzalez_maxcut(G):
    """Heurística de Sahni–Gonzalez para corte máximo."""

    vertices = list(G.nodes())

    # ---------- FASE 1 ----------

    A = set()
    B = set()

    # Primeiro vértice vai para A
    v0 = vertices[0]
    A.add(v0)

    # Constrói a partição inicial
    for v in vertices[1:]:
        wA = sum(G[v][u].get("weight", 1.0) for u in G.neighbors(v) if u in A)
        wB = sum(G[v][u].get("weight", 1.0) for u in G.neighbors(v) if u in B)

        # Colocar no lado oposto ao lado mais "conectado"
        if wA > wB:
            B.add(v)
        else:
            A.add(v)

    # ---------- FASE 2 (Melhoria Local) ----------
    melhorou = True

    while melhorou:
        melhorou = False

        for v in vertices:
            if v in A:
                atual = A
                outro = B
            else:
                atual = B
                outro = A

            w_atual = sum(G[v][u].get("weight", 1.0) for u in G.neighbors(v) if u in atual)
            w_outro = sum(G[v][u].get("weight", 1.0) for u in G.neighbors(v) if u in outro)

            # Ganho ao mover
            delta = w_atual - w_outro

            if delta > 0:
                atual.remove(v)
                outro.add(v)
                melhorou = True

    return A, B


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Uso: python maxcut.py arquivo.mc")
        sys.exit(1)

    nome_arquivo = sys.argv[1]

    pasta = os.path.join(os.getcwd(), "set2")

    G = ler_mc(pasta, nome_arquivo)

    A, B = sahni_gonzalez_maxcut(G)

    valor = peso_corte(G, A, B)

    print(f"Arquivo: {nome_arquivo}")
    print(f"Valor do corte encontrado: {valor}")
    print(f"Tamanho do conjunto A: {len(A)}")
    print(f"Tamanho do conjunto B: {len(B)}")
    print("A:", sorted(A))
    print("B:", sorted(B))
