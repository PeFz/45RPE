#Exercicio 5.6

lista = [1, -2 , 4, -3, 5, -7, 8, -9, 10, -11, 12, -13]

cont = 0
while cont < 12:
    if lista[cont] < 0:
        lista[cont] = 0
    cont=cont+1


print(lista)
