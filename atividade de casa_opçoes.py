import os 
os.system("clear")

print("""
codigo   carro    preço

                 
1    porshe 911Gt3      1.100.000  
2    AMG GT 2023        1.250.000        
3    BMW I8             650.000
4    AUDI TT RS         500.000   
5    CIVIC 2023/2024    300.000     
6    CAMARO 2016        250.000
7    JETTA              205.000       

OBS:VERIFIFICAR AS CORES EM ESTOQUE
      

""")

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
opcao1 = str(input("digite o codigo do carro: "))
opcao2 = str(input("digite o codigo da cor do carro: "))

print()

match opcao1:
    case '1':
        print(f"PORSHE 911GT3: 1.100.000")
    case '2':
        print(f"AMG GT 2023: 1.250.000")   
    case '3':
        print(f"BMW I8: 650.000")   
    case '4':
        print(f"AUDI TT RS: 500.000")
    case '5' :
       print("CIVIC 2023/2024: 300.000")
    case '6':
        print(f"CAMARO 2016: 250.000")   
    case '7':
        print(f"JETTA: 205.000")
    case '_' :
      print("OPÇÃO INVALIDA!")


print()


match opcao2:
    case '1':
        print(f"AZUL BB: 1")
    case '2':
        print(f"PRETO: 1")   
    case '3':
        print(f"VERMELHO: 1")   
    case '4':
        print(f"BRANCO: 1")
    case '_' :
       print("CODIGO INVALIDO")       

print()       




