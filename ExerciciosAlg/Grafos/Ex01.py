import os
import networkx as nx

def ler_todos_col(pasta):
    grafos = {}

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".col"):
            caminho = os.path.join(pasta, arquivo)

            G = nx.Graph()

            with open(caminho, "r") as f:
                for linha in f:
                    linha = linha.strip()

                    # ignora comentários e linha 'p'
                    if linha.startswith("c") or linha.startswith("p"):
                        continue

                    # linha de aresta: e u v
                    if linha.startswith("e"):
                        _, u, v = linha.split()
                        G.add_edge(int(u), int(v))

            grafos[arquivo] = G

    return grafos


pasta = r"C:\Users\zacch\PycharmProjects\45RPE\ExerciciosAlg\Grafos\.cols"
grafos = ler_todos_col(pasta)

for nome, G in grafos.items():
    print(f"{nome}: {G.number_of_nodes()} nós, {G.number_of_edges()} arestas")