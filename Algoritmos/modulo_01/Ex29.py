#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez
'''
29.	Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%.
Demais tipos não serão considerados.
'''

def Ex29():
    
    def calcInvest():
        
        if tipo==1:
            valor_corrigido = valor*(1.03)
        else:
            valor_corrigido = valor*(1.05)
        print("O valor corrigido é de : R$",valor_corrigido)
            
        
    print('Selecione o tipo de investimento:\n',
          '1- Poupança\n',
          '2- Renda Fixa')
    tipo = int(input())
    valor = float(input("Digite o valor investido: R$"))
    
    calcInvest()
