#EXERCÍCIOS DA AULA 4  
#Eduardo Maciel Sanchez

#33. Receba um número. Calcule e mostre a soma da série:
#    1 + 1/2 + 1/3 + ... + 1/N

def Ex33():
    
    print("Resultado da série 1 + 1/2 + 1/3 + ... + 1/N")
    N = int(input("Digite o valor de N: "))

    for i in range(0,N):
        if i == 0:
            sum = 1
        else:
            #print(sum," + 1/",i)
            sum = sum + 1/i

    print("O resultado é:",sum)
