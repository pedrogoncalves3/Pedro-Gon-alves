import os 
os.system("clear")
import time 


pedidos = []
carro = []
preco = []
cores = []

def menu_carro():
    print("""
codigo   carro    preço

                 
1    porshe 911Gt3      1.100,000  
2    AMG GT 2023        1.250,000        
3    BMW I8             650.000
4    AUDI TT RS         500.000   
5    CIVIC 2023/2024    300.000     
6    CAMARO 2016        250.000
7    JETTA              205.000       

OBS:VERIFIFICAR AS CORES EM ESTOQUE
      

""")
    
def core():
    print("""

CORES EM ESTOQUE!

CODIGO     COR   ESTOQUE

      
1        AZUL BB     5  
2        PRETO       35
3        VERMELHOR   15         
4        BRANCO      7
      
      
CORES DISPONIVEIS!


""")
    
    
    
nome = input("digite o nome que deseja receber na nota: ")    
    
while True: 
    menu_carro()    
    opcao1 = str(input("digite o codigo do carro: "))    
    
    
    match opcao1:
     case '1':
           carro.append("PORSHE 911GT3")
           preco.append  ( 1100000)
     case '2':
           carro.append("AMG GT 2023")
           preco.append  ( 1250000)   
     case '3':
           carro.append("BMW I8")
           preco.append  ( 650000 ) 
     case '4':
           carro.append("AUDI TT RS")
           preco.append  ( 500000 ) 
     case '5' :
           carro.append("CIVIC 2023/2024")
           preco.append  ( 300000 ) 
     case '6':
           carro.append("CAMARO 2016")
           preco.append   (250000 )    
     case '7':
           carro.append("JETTA")
           preco.append  ( 205000 ) 
     case '0' :
           print("espera para digitar a cor do carro!")
           print(f"carro: {carro}")
           print(f"preço: {preco}")
           time.sleep(2)
           break

os.system("clear")

print()





while True: 
   core()
   opcao2 = int(input("digite o codigo da cor do carro: "))
      
      
      
   match opcao2:
       case 1:
        cores.append("AZUL BB")
       case 2:
        cores.append("PRETO")   
       case 3:
        cores.append("VERMELHO")   
       case 4:
        cores.append("BRANCO")
       case '_' :
        cores.append("CODIGO INVALIDO")     
       case 0 :
           print("aguarde!")
           time.sleep(2)
           break  

print()       



def calcular(precos):
    soma = sum(precos)
    return soma

# Calcula o preço total
preco_total = calcular(preco)

# Mostra os resultados
print(f"\nResumo da Compra para {nome}:")
print(f"Quantidade de carros escolhidos: {len(carro)}")
print(f"Carros: {', '.join(carro)}")
print(f"Preço total: R$ {preco_total:,.2f}")
print(f"cores escolhidas: {cores}")
print(f"quantidade de cores : {len(cores)}")


