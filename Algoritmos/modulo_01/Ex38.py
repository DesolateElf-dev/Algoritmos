#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#38. Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor.
#    Obs.: somente valores positivos.

#def Ex38():
    #importações para aleatorização
from random import seed
from random import randint
seed(1)

def mostraMaior(lista):
    for i in range(0,len(lista)):
        if i == 0:
            maior = lista[i]
        elif lista[i]> maior:
            maior = lista[i]   
    return(maior)

def mostraMenor(lista):
    for i in range(0,len(lista)):
        if i == 0:
            menor = lista[i]
        elif lista[i]< menor:
            menor = lista[i]   
    return(menor)

#gera 100 numero aleatórios
lista = []
for i in range(100):
    lista.append(randint(0,1000000))

maior = mostraMaior(lista)
menor = mostraMenor(lista)
print("O maior valor é ",maior," e o menor valor é ",menor)