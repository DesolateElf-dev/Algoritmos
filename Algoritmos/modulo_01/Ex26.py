#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#26. Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.

def Ex26():
    
    def verificaMult():
        if (x>=y):
            if (x%y==0):
                print(x,' é multiplo de ',y)
            else:
                print(x,' não é multiplo de ',y) 
        else:
            if (y%x==0):
                print(y,' é multiplo de ',x)
            else:
                print(y,' não é multiplo de ',x)


    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))

    verificaMult()