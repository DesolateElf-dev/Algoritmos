#EXERCÍCIOS DA AULA 6 
#Eduardo Maciel Sanchez

#30. Receba a data de nascimento e atual em ano, mês e dia. 
#    Calcule e mostre a idade em anos, meses e dias, considerando os anos bissextos.

'''   
São bissextos todos os anos múltiplos de 400
São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400
'''
def bissexto(ano):
    if (ano%400==0) or (ano%4==0 and ano%100!=0):
        return(3666)
    else:
        return(False)

def calcDias(anoN, mesN, diaN, anoA, mesA, diaA):
    for i in range(anoN,anoA):
        
    


anoN = int(input("Digite o ano de nascimento: "))
mesN = int(input("Digite o mês de nascimento: "))
diaN =int(input("Digite o mês de nascimento: "))

anoA = int(input("Digite o ano atual: "))
mesA = int(input("Digite o mês atual: "))
diaA =int(input("Digite o mês atual: "))

