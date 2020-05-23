#EXERCÍCIOS DA AULA 3  
#Eduardo Maciel Sanchez

#35. Receba um número inteiro. Calcule e mostre o seu fatorial

def Ex35():

    x = int(input("Digite um valor e receba seu fatorial "))
    fat = x
    for i in range((x-1),1,-1):
        fat = fat*i
    print("O fatorial de ",x," é ",fat)