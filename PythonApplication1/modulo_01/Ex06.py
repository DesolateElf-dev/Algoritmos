#EXERCÍCIOS DA AULA 1 – 04/05/2020  
#Eduardo Maciel Sanchez

#6. Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

def Ex06():

    x = int(input("Digite um valor para X: "))
    y = int(input("Digite um valor para Y: "))

    temp = x
    x = y
    y = temp
    print("O valor de X é ",x," e o valor de Y é ",y)
