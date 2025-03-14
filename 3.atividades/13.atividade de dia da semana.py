import os
os.system("clear")

print("""
      
======MESES DO ANO======

 {1}   |   JANEIRO     |
 {2}   |   FEVEREIRO   | 
 {3}   |   MARÇO       | 
 {4}   |   ABRIL       |
 {5}   |   MAIO        |
 {6}   |   JUNHO       |
 {7}   |   JULHO       | 
 {8}   |   AGOSTO      | 
 {9}   |   SETEMBRO    |  
 {10}  |   OUTUBRO     | 
 {11}  |   NOVEMBRO    | 
 {12}  |   DEZEMBRO    | 


ESSES SÃO OS MESES DO ANO
      

""")

n1 = str(input("digite aqui o número correspondente ao dia do mês: "))
 

match n1:
    case '1':
        resultado = (" janeiro")
    case '2':
        resultado = (" fevereiro")   
    case '3':
        resultado = (" março")   
    case '4':
        resultado = (" abril")
    case '5' :
       resultado = (" maio")
    case '6':
        resultado = (" junho")   
    case '7':
        resultado = (" julho")
    case '8':
        resultado = (" agosto")
    case '9':
        resultado = (" setembro")   
    case '10':
        resultado = (" outubro")   
    case '11':
        resultado = (" novembro")
    case '12' :
       resultado = (" dezembro")
print()

print(f"resultado: {resultado}")      