#EXERCÍCIOS DA AULA 6 
#Eduardo Maciel Sanchez

#45. Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225

#def Ex45():
def calcSerie(divMax):
    resultado = 0
    i,j = 1,1
    for n in range(1,16):
        j = n**2
        print(i," / ",j)
        resultado += i/j
        if i < 0:
            i = (-i)+1
        else:
            i = -(i+1)
    return(resultado)

print("Calcula a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225")
serie = calcSerie(225)
print("A soma é: ",serie)
            
            