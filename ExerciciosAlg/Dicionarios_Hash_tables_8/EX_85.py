"""
Suponha que o tamanho da sua tabela hash seja 31, que você use o código hash para strings descrito
abaixo (padrão em várias linguagens), e que você use encadeamento para resolver colisões. Liste cinco
nomes distintos que serão armazenados na mesma posição da tabela, gerando colisões.

O método de Horner é comumente usado para gerar códigos hash para strings. Dado g = 31 (valor padrão
para essa variável), o código hash é dado por u0g
n−1 + u1g
n−2 + · · · + un−2g + un−1, onde ui é o i-ésimo
caractere da string. Abaixo é fornecida uma implementação da função hash usando o método de Horner
para gerar o código hash. Note que a função ord retorna o código Unicode do caractere, permitindo a
soma com outros números.

"""

def hash_function(s, size, g=31):
    hash_value = 0
    n = len(s)
    for i in range(n):
        hash_value = g * hash_value + ord(s[i])
    return hash_value % size


print(hash_function("tim", 31))
print(hash_function("m", 31))
print(hash_function("toaasdasdasdm", 31))
print(hash_function("taam", 31))

size = 31

nomes = ["tam", "kham", "juam", "mam", "m"]

for nome in nomes:
    print(f"{nome:>5} → posição = {hash_function(nome, size)}")
"""
metodo de horner pega as ultimas letras da string e soma com o valor do hash, basicamente ele usa somente as ultimas 
letras para alocar na tabela
"""