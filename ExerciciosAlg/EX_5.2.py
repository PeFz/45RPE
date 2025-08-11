# Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Lista com os 20 primeiros números ímpares
impares = []
num = 1
while len(impares) < 20:
    if num % 2 != 0:
        impares.append(num)
    num += 1

# Lista com os 20 primeiros números primos
primos = []
num = 2
while len(primos) < 20:
    if eh_primo(num):
        primos.append(num)
    num += 1

# Exibindo resultados
print("20 primeiros números ímpares:", impares)
print("20 primeiros números primos:", primos)
