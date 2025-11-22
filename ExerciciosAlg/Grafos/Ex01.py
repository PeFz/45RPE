import sys
import os
import networkx as nx

def ler_um_col(pasta, nome_arquivo):
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

if __name__ == "__main__":
    pasta = r"C:\Users\zacch\PycharmProjects\45RPE\ExerciciosAlg\Grafos\.cols"
    nome = sys.argv[1]

    G = ler_um_col(pasta, nome)
    print(f"{nome}: {G.number_of_nodes()} nós, {G.number_of_edges()} arestas")
