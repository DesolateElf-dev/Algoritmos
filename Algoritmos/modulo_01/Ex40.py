#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#40. Receba 2 números inteiros. Verifique e mostre todos os números
#    primos existentes entre eles.

def Ex40():
    def calcPrimo(x,y):
        lista = []
        for i in range(x,y):
            check = 1
            for j in range(2,i//2):
                if i%j==0:
                    check = 0
                    break
            if check==1 and i!=0 and i!=1:
                lista.append(i)
        return(lista)
    
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    if x>=y:
        lista = calcPrimo(y,x)
        print(lista)
    else:
        lista = calcPrimo(x,y)
    print(lista)