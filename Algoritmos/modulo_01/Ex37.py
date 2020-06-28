#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#37. Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

#def Ex37():
    
n = int(input("Digite o valor de n: ")
        
for i in range(0,10):
    
    if i == 0:
        n1 = i
        print(n1,", ", end="")
        n2 = n1
    else:
        n1 = n1+n2
        print(n1,", ", end="")
        n2 = n1