#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#37. Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

def Ex37():

    def calcFiboo(n):
        i = 0
        while i<=n:
            if i==0:
                fibo = 0
                fibo1 = fibo
                i+=1
            elif i==1:
                fibo = 1
                fibo2 = fibo1
                fibo1 = fibo
                i+=1
            else:
                fibo = fibo1+fibo2
                fibo2 = fibo1
                fibo1 = fibo
                i+=1
        return(fibo)
            
    n = int(input("Digite o valor de n: "))
    
    for i in range(0,n):
        fibo = calcFibo(i)
        print(fibo,end=" ")