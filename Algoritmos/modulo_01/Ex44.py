#EXERCÍCIOS DA AULA 6 
#Eduardo Maciel Sanchez

#44. Receba o número da base e do expoente. Calcule e mostre o valor da potência.

def Ex44():
    
    def calcPot(base,exp):
        resultado = base**exp
        return(resultado)
    
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    potencia = calcPot(base,expoente)
    print("O resultado é: ",potencia)