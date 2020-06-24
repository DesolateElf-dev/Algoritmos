#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez

#27. Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos).
#    Calcule e mostre a velocidade média em km/h.

def Ex27():
    
    def calcVMedia():
        
        velocidade = (((extensao*voltas)/tempo))/(100/6)
        print("A velocidade média durante o circuito foi de :",velocidade,"km/h")


    voltas = int(input("Digite o número de voltas: "))
    extensao = int(input("Digite a extensão de cada volta (metros): "))
    tempo = int(input("Digite o tempo de duração (min): "))

    calcVMedia()