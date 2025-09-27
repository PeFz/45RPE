# Classe que representa cada nó da lista
class No:
    def __init__(self, valor):
        self.valor = valor      # dado armazenado no nó
        self.proximo = None     # referência para o próximo nó


# Classe da lista simplesmente encadeada
class ListaEncadeada:
    def __init__(self):
        self.inicio = None      # ponteiro para o primeiro nó
        self.fim = None         # ponteiro para o último nó
        self.tamanho = 0        # contador de elementos

    # Inserir elemento no início da lista
    def inserir_no_inicio(self, valor):
        novo = No(valor)             # cria um novo nó
        if self.inicio == None:      # se a lista estiver vazia
            self.inicio = novo
            self.fim = novo
        else:                         # se já tiver elementos
            novo.proximo = self.inicio
            self.inicio = novo
        self.tamanho += 1

    # Inserir elemento no final da lista
    def inserir_no_fim(self, valor):
        novo = No(valor)
        if self.inicio == None:      # se estiver vazia
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo  # último nó aponta para o novo
            self.fim = novo          # atualiza o último nó
        self.tamanho += 1

    # Remover elemento do início
    def remover_do_inicio(self):
        if self.inicio == None:      # se estiver vazia
            print("Lista vazia. Nada para remover.")
            return None
        valor_removido = self.inicio.valor
        self.inicio = self.inicio.proximo  # o segundo vira o primeiro
        self.tamanho -= 1
        if self.inicio == None:           # se a lista ficou vazia
            self.fim = None
        return valor_removido

    # Remover elemento do final
    def remover_do_fim(self):
        if self.inicio == None:
            print("Lista vazia. Nada para remover.")
            return None

        if self.inicio == self.fim:      # só tem um nó
            valor_removido = self.inicio.valor
            self.inicio = None
            self.fim = None
        else:
            atual = self.inicio
            while atual.proximo != self.fim:  # percorre até o penúltimo
                atual = atual.proximo
            valor_removido = self.fim.valor
            atual.proximo = None
            self.fim = atual
        self.tamanho -= 1
        return valor_removido

    # Retorna o tamanho da lista
    def size(self):
        return self.tamanho

    # Verifica se a lista está vazia
    def is_empty(self):
        return self.tamanho == 0

    # Exibir os elementos da lista
    def mostrar(self):
        atual = self.inicio
        while atual != None:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")



