#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#37. Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

#def Ex37():
    
n = int(input("Digite o valor de n: "))

for i in range(0,n+1):
    if i == 0:
        