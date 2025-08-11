#Exercicio 5.2

def VintepimeirosImpars():
    numeros = []
    for numero in range(1,40):
        if numero % 2 != 0:
            numeros.append(numero)
    return numeros

print(VintepimeirosImpars())