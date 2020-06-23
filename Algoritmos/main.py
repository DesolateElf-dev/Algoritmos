#Eduardo Maciel Sanchez
#Fatec - Zona Leste
#Algoritmos e Lógica de Programação
#Ricardo Satoshi

from modulo_01.Ex06 import Ex06
from modulo_01.Ex07 import Ex07
from modulo_01.Ex16 import Ex16
from modulo_01.Ex18 import Ex18
from modulo_01.Ex21 import Ex21
from modulo_01.Ex23 import Ex23
from modulo_01.Ex25 import Ex25
from modulo_01.Ex33 import Ex33
from modulo_01.Ex34 import Ex34
from modulo_01.Ex35 import Ex35
from modulo_01.Ex41 import Ex41

"""Módulo de controle para visualizar os exercícios"""

def main():

    ops = 1

    while(ops!=0):

        ops = int(input("Digite o número de um exercício para executá-lo, ou 0 para finalizar: "))

        if(ops==6):
            modulo_01.Ex06()
        elif(ops==7):
            Ex07()
        elif(ops==16):
            Ex16()
        elif(ops==18):
            Ex18()
        elif(ops==21):
            Ex21()
        elif(ops==23):
            Ex23()
        elif(ops==25):
            Ex25()
        elif(ops==33):
            Ex33()
        elif(ops==34):
            Ex34()
        elif(ops==35):
            Ex35()
        elif(ops==41):
            Ex41()
        elif(ops==0):
            print("Programa Finalizado")
        else:
            print("Opção Inválida")

if __name__ == "__main__":
    main()