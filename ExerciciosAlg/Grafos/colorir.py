import sys          # sys: usado para ler argumentos da linha de comando (sys.argv)
import os           # os: usado para trabalhar com caminhos de arquivo (os.path.join, os.getcwd)
import networkx as nx   # networkx: biblioteca para trabalhar com grafos em Python


def ler_col(pasta, nome_arquivo):
    """
    Lê um arquivo .col e devolve um grafo não-direcionado (nx.Graph).

    Formato típico do .col:
        c ...        -> linha de comentário (ignorar)
        p ...        -> linha com informações do problema (ignorar)
        e u v        -> aresta entre os vértices u e v

    Parâmetros:
        pasta (str)         -> caminho da pasta onde está o arquivo .col
        nome_arquivo (str)  -> nome do arquivo .col (ex: 'le450_5a.col')

    Retorna:
        G (nx.Graph)        -> grafo construído a partir do arquivo
    """

    # Monta o caminho completo do arquivo: pasta + nome do arquivo
    # Ex: "C:/.../Grafos/.cols" + "le450_5a.col"
    caminho = os.path.join(pasta, nome_arquivo)

    # Cria um grafo não direcionado vazio
    G = nx.Graph()

    # Abre o arquivo no modo leitura ("r")
    # "with" garante que o arquivo será fechado automaticamente no final do bloco
    with open(caminho, "r") as f:
        # Percorre cada linha do arquivo
        for linha in f:
            # Remove espaços em branco no início/fim da linha (inclui '\n')
            linha = linha.strip()

            # Se a linha começa com 'c' ou 'p', é comentário/descrição -> ignorar
            if linha.startswith("c") or linha.startswith("p"):
                continue

            # Se a linha começa com 'e', temos uma aresta: "e u v"
            if linha.startswith("e"):
                # Faz o split, espera algo tipo: ["e", "12", "30"]
                _, u, v = linha.split()

                # Adiciona a aresta (u, v) ao grafo
                # int(u), int(v): converte de string para inteiro
                G.add_edge(int(u), int(v))

    # Retorna o grafo construído
    return G


def welsh_powell(G):
    """
    Implementação do algoritmo Welsh–Powell para coloração de grafos.

    Ideia:
        1. Ordenar os vértices por grau (decrescente).
        2. Para cada cor:
            - percorrer a lista de vértices nessa ordem
            - colorir com a cor atual todo vértice que:
                * ainda não tem cor
                * não é vizinho de nenhum vértice que já tenha essa cor
        3. Repetir até todos os vértices estarem coloridos.

    Parâmetros:
        G (nx.Graph) -> grafo a ser colorido

    Retorna:
        coloracao (dict): dicionário {vértice: cor_atribuída}
    """

    # "ordem" é a lista de vértices ordenada por grau decrescente.
    # G.degree(v) devolve o grau do vértice v.
    # reverse=True -> do maior grau para o menor.
    ordem = sorted(G.nodes(), key=lambda v: G.degree(v), reverse=True)

    # cor_atual será um número inteiro que representa a "cor" usada.
    # Começamos na cor 0, depois 1, 2, ...
    cor_atual = 0

    # coloracao guarda, para cada vértice, qual foi a cor nele.
    # Exemplo: {1: 0, 5: 0, 3: 1, 7: 2}
    coloracao = {}

    # Percorremos os vértices na ordem de grau decrescente
    for v in ordem:

        # Se o vértice v ainda não foi colorido, tentamos usar uma nova cor nele.
        if v not in coloracao:

            # Atribuímos a cor atual ao vértice v.
            coloracao[v] = cor_atual

            # Agora tentamos colorir outros vértices também com a mesma cor_atual,
            # desde que não entrem em conflito (não sejam vizinhos de quem já tem essa cor).
            for u in ordem:
                # Só podemos tentar colorir u se ele ainda não tiver cor.
                if u not in coloracao:

                    # Verificamos se algum vizinho de u já tem a cor atual.
                    # G.neighbors(u) devolve os vizinhos de u.
                    # coloracao.get(w) == cor_atual verifica se o vizinho w tem cor_atual.
                    conflito = any(coloracao.get(w) == cor_atual for w in G.neighbors(u))

                    # Se não houver conflito, podemos dar a mesma cor para u.
                    if not conflito:
                        coloracao[u] = cor_atual

            # Depois de tentar usar ao máximo essa cor, passamos para a próxima.
            cor_atual += 1

    # Retornamos o dicionário de coloração.
    return coloracao


if __name__ == "__main__":
    """
    Bloco principal do script.
    É executado somente quando rodamos: python colorir.py arquivo.col

    Exemplo:
        python colorir.py le450_5a.col
    """

    # sys.argv é a lista de argumentos que veio da linha de comando.
    # sys.argv[0] = "colorir.py"
    # sys.argv[1] = "le450_5a.col"  (por exemplo)
    if len(sys.argv) < 2:
        print("Uso: python colorir.py arquivo.col")
        sys.exit(1)

    # Nome do arquivo passado na linha de comando
    nome_arquivo = sys.argv[1]

    # Monta o caminho da pasta .cols dentro da pasta atual do projeto.
    # os.getcwd() -> diretório atual (onde você está rodando o script).
    pasta = os.path.join(os.getcwd(), ".cols")

    # Lê o grafo a partir do arquivo .col escolhido.
    G = ler_col(pasta, nome_arquivo)

    # Aplica o algoritmo de Welsh–Powell para colorir o grafo.
    coloracao = welsh_powell(G)

    # Número total de cores usadas é o máximo índice de cor + 1
    num_cores = max(coloracao.values()) + 1

    # Mostra o total de cores
    print(f"Total de cores usadas: {num_cores}")

    # Agora vamos organizar os vértices por cor,
    # só para imprimir de forma mais amigável.
    cores = {}  # dicionário: cor -> lista de vértices

    for v, c in coloracao.items():
        # Se a cor ainda não tem lista, cria uma lista vazia
        if c not in cores:
            cores[c] = []
        # Adiciona o vértice v na lista da cor c
        cores[c].append(v)

    # Imprime as cores em ordem: 0, 1, 2, ...
    for c in sorted(cores.keys()):
        # Ordena os vértices de cada cor para ficar mais organizado
        lista_vertices = sorted(cores[c])
        # Monta uma string tipo "1 5 12 17"
        lista_str = " ".join(str(v) for v in lista_vertices)
        print(f"Cor {c}: {lista_str}")


