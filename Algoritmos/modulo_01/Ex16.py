#EXERCÍCIOS DA AULA 5
#Eduardo Maciel Sanchez

#16. Cálculo de salário líquido


def Ex16():
    
    def calcSalario():
        salario_bruto = (horas*val_hora)
        salario_liquido = salario_bruto - (salario_bruto*(desconto/100))
        salario_liquido = salario_liquido+(100*descendentes)
        
        print('O salário à receber é: R$',salario_liquido)


    print("Calculo da média e resultado (Aprovado/Exame/Reprovado)")
    horas = int(input("Horas trabalhadas: "))
    val_hora = int(input("Valor por hora: "))
    desconto = int(input("Percentual de desconto: "))
    descendentes = int(input("Número de descendentes: "))

    calcSalario()