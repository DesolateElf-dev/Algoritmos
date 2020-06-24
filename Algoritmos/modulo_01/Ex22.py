#EXERCÍCIOS DA AULA 5
#Eduardo Maciel Sanchez

#22. Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

def Ex22():
    
    def ordena():
        
        if (x <= y):
            print(x,', ', y)
        else:
            print(y,', ', x)    
    
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    
    ordena()