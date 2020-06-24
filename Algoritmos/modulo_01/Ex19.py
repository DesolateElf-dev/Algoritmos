#EXERCÍCIOS DA AULA 5
#Eduardo Maciel Sanchez

#19. Receba 2 valores reais. Calcule e mostre o maior deles.

def Ex19():
    
    def mostraMaior():
        if (x>y):
            print("O maior é ", x)
        elif (y>x):
            print("O maior é ", y)
        else:
            print("Os valores são iguais.")
    
    
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    mostraMaior()
