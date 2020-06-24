#EXERCÍCIOS DA AULA 5
#Eduardo Maciel Sanchez

#20. Calcula o equações de 2º grau

import math

def Ex19():
    
    def calcEqua():
        delta = (b**2)-(4*a*c)
        if (delta < 0):
            print('Não existem raízes reais.')
        elif (delta==0):
            x1 = -b/(2*a)
            print('A única raíz é ',x1)
        else:
            x1 = (-b+(math.sqrt(delta)))/(2*a)
            x2 = (-b-(math.sqrt(delta)))/(2*a)
            print('As raízes são x1=',x1,' e x2= ',x2)
        
    
    
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    calcEqua()