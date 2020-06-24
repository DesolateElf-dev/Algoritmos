#EXERCÍCIOS DA AULA 5
#Eduardo Maciel Sanchez

#24. Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

def Ex24():
    
    def ordena():
        if(x==0):
            print('Valor nulo')
        else:
            if (x%2==0):
                if (x%3==0):
                    print(x,' é divisível por 2 e por 3')
                else:
                    print(x,' é divisível por 2 mas não por 3')
            else:
                if (x%3==0):
                    print(x,' é divisível por 3 mas não por 2')
                else:
                    print(x,' não é divisível nem por 2 nem por 3')
    
    
    x = int(input("Digite um valor inteiro: "))
    
    ordena()
        