
#EXERCÍCIOS DA AULA 2 – 01/05/2020  
#Eduardo Maciel Sanchez

#18. Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

def Ex18():
    quit = 1
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))

    if (x>=y):
        dif = x-y
        print("A diferença é ", dif)
    else:
        dif = y-x
        print("A diferença é ", dif)