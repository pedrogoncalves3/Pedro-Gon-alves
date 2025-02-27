import os
os.system("clear")

print("""
======dias da semana======

                 
1  =  Domingo       
2  =  Segunda               
3  =  Terça             
4  =  Quarta         
5  =  Quinta       
6  =  Sexta        
7  =  Sabado                  

aguardando o dia da semana
      

""")

n1 = str(input("digite aqui o número correspondente ao dia da semana: "))
 
 
os.system("clear")

print("""
======dias da semana======
                 
1  =  Domingo       
2  =  Segunda               
3  =  Terça             
4  =  Quarta         
5  =  Quinta       
6  =  Sexta        
7  =  Sabado                  

      
""")


match n1:
    case '1':
        print("final de semana, aproveite o dia")
    case '2':
        print("segunda")   
    case '3':
        print("terça")   
    case '4':
        print("quarta")
    case '5' :
       print("quinta")
    case '6':
        print("sexta")   
    case '7':
        print("final de semana")
    case _:
        print("invalido")