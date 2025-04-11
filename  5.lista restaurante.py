import os 
os.system("clear")

prato = []
preco = [] 

def menu():
    print("""
==========CARDAPIO==========
codigo \tprato  \tpreço

1 | ° Picanha         | 25.00
2 | ° Lasanha         | 20.00
3 | ° Strogonoff      | 18.00
4 | ° Bife acebolado  | 15.00
5 | ° Pão com ovo     | 5.00
                               
""")


  
while True:
   menu()
   print("Digite 0 para finalizar o pedido e obter o valor total")      
   pedido = str(input("digite o código do prato: "))        
  

  
   match pedido:
    case '1':
        prato.append("picanha:")
        preco.append  (25.00)
    case '2':
        prato.append("lasanha:")
        preco.append  (20.00) 
    case '3':
        prato.append(f"strogonoff:")   
        preco.append  (18.00)
    case '4':
        prato.append(f"bife acebolado: ")
        preco.append  (15.00)
    case '5' :
        prato.append("pão com ovo:")
        preco.append   (5.00)
    case '0' :
       os.system("clear")
       print(f"seu prato foi: {prato}")
       print(f"preço: {preco}")
       
       
       break
        
def calcular(preco):
  soma = sum(preco)   
    
    
    
       
   




   