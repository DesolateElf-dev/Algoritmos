#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#33. Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

def Ex33_mod():

    def calcSoma(N):
        if N ==0:
            return(0)
        else:
            sum = 1/N + calcSoma(N-1)
            return(sum)


    print("Resultado da série 1 + 1/2 + 1/3 + ... + 1/N")
    N = int(input("Digite o valor de N: "))
    sum = calcSoma(N)
    print("O resultado é:",sum)