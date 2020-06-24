#EXERCÍCIOS DA AULA 5
#Eduardo Maciel Sanchez

#23. Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

def Ex23():
    
    def ordena():
        if (d<=a):
            print(d,", ",a,", ",b,", ",c)
        elif (d>a and d<=b):
            print(a,", ",d,", ",b,", ",c)
        elif (d>b and d<=c):
            print(a,", ",b,", ",d,", ",c)
        elif (d>c):
            print(a,", ",b,", ",c,", ",d)


    a = float(input("Digite o primeiro valor em ordem: "))
    b = float(input("Digite o segundo valor em ordem: "))
    c = float(input("Digite o terceiro valor em ordem: "))
    d = float(input("Digite um quarto valor qualquer: "))
    ordena()
    