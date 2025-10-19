# h(k) = 3k % 19.

def hash(k):
    return (3 * k) % 19

valores = [54, 28, 41, 18, 10, 36, 25, 38, 12, 90]

for i in valores:

    print(f"Chave: {i} - Valor: {hash(i)}")
