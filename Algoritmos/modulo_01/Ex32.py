#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#32. Receba um número inteiro. Calcule e mostre o seu fatorial. (N! = 1 * 2 * 3 *...*N)

def Ex31():
    
    def calcFat(numero):
        if numero == 0:
            return(1)
        else:
            resultado = numero*calcFat(numero-1)
            
        return(resultado)
    
    numero = int(input("Digite um número e receba seu fatorial: "))
    fatorial = calcFat(numero)
    print("O fatorial de ",numero," é ", fatorial)