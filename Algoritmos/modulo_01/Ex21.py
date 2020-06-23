#EXERCÍCIOS DA AULA 5 
#Eduardo Maciel Sanchez

#21. Receba 4 notas bimestrais de um aluno.  
#    Calcule a média aritmética. Mostre a mensagem de acordo com a média:

#    a.	Se a média for >= 6.0          exibir “APROVADO”;
#    b.	Se a média for >= 3.0 e < 6.0  exibir “EXAME”;
#    c.	Se a média for < 3.0           exibir “RETIDO”.

def Ex21():
    
    def calcMedia():
        med = (b1+b2+b3+b4)/4

        print("A média foi: ",med)
        
        if med >= 6:
            print("Aprovado")
        elif med >= 3 and med < 6:
            print("Exame")
        elif med < 3:
            print("Reprovado")

    print("Calculo da média e resultado (Aprovado/Exame/Reprovado)")
    b1 = int(input("Nota 1º Bimestre: "))
    b2 = int(input("Nota 2º Bimestre: "))
    b3 = int(input("Nota 3º Bimestre: "))
    b4 = int(input("Nota 4º Bimestre: "))

    calcMedia()
