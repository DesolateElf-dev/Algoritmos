#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#35.Receba 2 números inteiros, verifique qual o maior entre eles.
#   Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

def Ex35_mod():
    
    def calcSoma(x,y):
        resultado = 0
        if y % 2 != 0:
            y = y+1
        if x % 2 != 0:
            x = x-1
        for i in range(y+1,x,2):
            resultado = resultado+i
        return(resultado)
            
        
        
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    if x >= y:
            soma = calcSoma(x,y)
    else:
        soma = calcSoma(y,x)
    print("A soma é: ",soma)