#Eduardo Maciel Sanchez
#Fatec - Zona Leste
#Algoritmos e Lógica de Programação
#Ricardo Satoshi

from modulo_01.Ex06 import *
from modulo_01.Ex07 import *
from modulo_01.Ex18 import *
from modulo_01.Ex23 import *
from modulo_01.Ex34 import *
from modulo_01.Ex35 import *


##from modulo_01.Ex06 import Ex06

"""Módulo de controle para visualizar os exercícios"""

def main():

    ops = 1

    while(ops!=0):

        ops = int(input("Digite o número de um exercício para executá-lo, ou 0 para finalizar: "))

        if(ops==6):
            Ex06()
        elif(ops==7):
            Ex07()
        elif(ops==18):
            Ex18()
        elif(ops==23):
            Ex23()
        elif(ops==34):
            Ex34()
        elif(ops==35):
            Ex35()
        elif(ops==0):
            print("Programa Finalizado")
        else:
            print("Opção Inválida")

if __name__ == "__main__":
    main()