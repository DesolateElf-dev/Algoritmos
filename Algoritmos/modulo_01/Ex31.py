#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#31. Calcule e mostre o quadrado dos números entre 10 e 150.

def Ex31():
    
    def calcPotencia(numero):
        
        resultado = numero**2
        
        return(resultado)
    
    print("Calcula o quadrado dos número entre 10 e 150")
    
    for numero in range(10,151):
        quadrado = calcPotencia(numero)
        print("O quadrado de ", numero," é ",quadrado)