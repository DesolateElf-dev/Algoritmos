#EXERCÍCIOS DA AULA 6 
#Eduardo Maciel Sanchez

#42. Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99

def Ex42():
    def calcSoma(cima,baixo):
        soma=0
        j = 1
        for i in range(1,cima+1):
            print("+",i,"/",j)
            soma += i/j
            j += 2
        return(soma)
    
    print("Calcula a série 1 + 2/3 + 3/5 + ... + 50/99")
    soma = calcSoma(50,99)
    print("A soma da série é: ",soma)