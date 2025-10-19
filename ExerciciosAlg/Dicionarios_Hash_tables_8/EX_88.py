def hash(i):
    return (3*i + 5) % 11

entradas = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)

for i in entradas:
    print(f"Chave: {i} - Valor: {hash(i)}")