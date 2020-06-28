#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#34. Calcule e mostre o quadrado dos números entre 10 e 150.

def Ex34():
    
    def calcTab(N,i):
        resultado = N*i
        return(resultado)
    
    print("O exercício 34 calcula a tabuada de N")
    N = int(input("Digite o valor de N: "))
    for i in range(0,11):
        tabuada = calcTab(N,i)
        print(i," x ",N," = ",tabuada)