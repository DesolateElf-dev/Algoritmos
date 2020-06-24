#EXERCÍCIOS DA AULA 6
#Eduardo Maciel Sanchez
'''
28.	Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
Venda Mensal	   Preço Atual	   Preço Novo
< 500              < 30	           + 10%
>= 500 e < 1000	   >= 30 e < 80	   +15%
>= 1000	           >= 80	       - 5%
Obs.: para outras condições, preço novo será igual ao preço atual.
'''

def Ex28():
    
    def calcAjuste():
        
        if m_venda < 500 and preco <30:
            precoFinal = preco+(preco/10)
        elif m_venda >= 500 and m_venda < 1000 and preco >= 30 and preco < 80:
            precoFinal = preco+((preco/100)*15)
        elif m_venda >= 1000 and preco >= 80:
            precoFinal = preco-((preco/20))
        else:
            precoFinal = preco
            print("Não houve reajuste")
        print("O preço final é R$",precoFinal)
            
        
    preco = float(input("Preço atual do produto: "))
    m_venda = int(input("Média de venda mensal: "))
    
    calcAjuste()
