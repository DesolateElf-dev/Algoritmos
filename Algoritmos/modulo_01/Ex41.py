#EXERCÍCIOS DA AULA 4  
#Eduardo Maciel Sanchez

#41. Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.
#    D1 + D2 = 7 

def Ex41():
    
    print("Possibilidade das faces de 2 dados somarem 7")

    for i in range(1,7):
        for j in range(1,7):
            if (i+j)==7:
                print(i," mais ", j, " soma 7")

