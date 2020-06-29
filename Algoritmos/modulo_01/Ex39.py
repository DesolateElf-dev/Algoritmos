#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez
'''
39. Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
Casa: 	1	2	3	4	...	64
Qdte:	1	2	4	8	...	N
'''
def Ex39():
    
    def calcGraos(n):
        resultado = 0
        for i in range(64):
            resultado += 2**i
        return(resultado)
    
    print("Calcula o resultado da quantidade de grãos")
    soma = calcGraos(64)
    print("Um tabuleiro de xadrez possui ",soma," grãos.")