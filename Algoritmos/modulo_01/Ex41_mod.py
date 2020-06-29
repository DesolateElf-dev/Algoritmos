#EXERCÍCIOS DA AULA 6 
#Eduardo Maciel Sanchez

#41. Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.
#    D1 + D2 = 7 

def Ex41_mod():   
    
    def calcDado(i,j):
        if (i+j)==7:
            return(True)
        else:
            return(False)    
    
    print("Possibilidade das faces de 2 dados somarem 7")
    for i in range(1,7):
        for j in range(1,7):
            if calcDado(i,j):
                print(i, " mais ", j, "soma 7")