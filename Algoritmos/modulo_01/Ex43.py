#EXERCÍCIOS DA AULA 6 
#Eduardo Maciel Sanchez

'''
43.	Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria
sabendo que:
Ana tem 1,10 m e cresce 3 cm ao ano; e
Maria tem 1,5 m e cresce 2 cm ao ano.
'''
#def Ex43():
    
def calcAlt(HAna, HMaria):
    anos = 0
    while HAna < HMaria:
        HAna += 0.3
        HMaria += 0.2
        anos += 1
    return(anos)
Ana = 1.10
Maria = 1.5
anos = calcAlt(Ana,Maria)
print("Em ",anos," anos, Ana será mais alta que Maria")