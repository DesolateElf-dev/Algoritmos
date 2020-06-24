#EXERCÍCIOS DA AULA 5
#Eduardo Maciel Sanchez

#17. Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l.
#    Receber o tempo de percurso e a velocidade média.


def Ex17():
    
    def calcLitros(tempo):
        
        tempo = tempo/60
        distancia = velocidade*tempo
        litros = distancia/12
        print("Foram gastos durante a viagem ",litros,"l de combustível")


    tempo = int(input("Tempo de percurso em min: "))
    velocidade = int(input("Velocidade media (km/h): "))

    calcLitros(tempo)