#EXERCÍCIOS DA AULA 5 
#Eduardo Maciel Sanchez

#25. Receba a hora de início e de final de um jogo (HH,MM), 
#    calcular o tempo do jogo em horas e minutos, sabendo
#    que o tempo máximo é menor que 24 horas e pode   
#    começar num dia e terminar em outro.


def Ex25():

    def subTempo(hora0,min0,hora1,min1):

        #converte os minutos para decimais
        min0 = min0/60
        min1 = min1/60

        hora0 = hora0 + min0
        hora1 = hora1 + min1

        if (hora0<hora1):
            horas = hora1-hora0
        elif (hora0>=hora1):
            horas = ((hora1+24)-hora0)

        #separa minutos de horas
        minutos = horas % 1
        horas = horas - minutos

        #transforma os decimais em minutos novamente
        minutos = minutos*60

        print("O jogo durou ","%.0f" % horas," horas e ","%.0f" % minutos," minutos")
    
    #hora(0 a 23)
    #minuto(0 a 59)

    print("Calcula o tempo de jogo")
    h0 = int(input("Hora de início (0 a 23): "))
    m0 = int(input("Minuto de início (0 a 59): "))
    h1 = int(input("Hora de término (0 a 23): "))
    m1 = int(input("Minuto de término (0 a 59): "))

    subTempo(h0,m0,h1,m1)