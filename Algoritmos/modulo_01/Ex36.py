#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#36. Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

def Ex36():
    
    def calcFat(N):
        if N == 0:
            return(1)
        else:
            resultado = N * calcFat(N-1)
            return(resultado)
    
    def calcSoma(N):
        if N == 0:
            return(1)
        else:
            resultado = 1/calcFat(N) + calcSoma(N-1)
            return(resultado)
        
        
    N = int(input("Digite o valor de N: "))
    soma = calcSoma(N)
    print("A soma da série é: ",soma)