import os
import time

os.system("clear")

def transformador(numero):
    
    if numero >0:
        print("seu número e um número positivo")
    elif numero <0:
        print("seu número e um número negativo")
    else:
       print("valor neutro!")    


while True:
  try:
   nu1 = float(input("digite um número: "))  
   os.system("clear||cls")
   transformador(nu1)
   break 

  except ValueError:
     os.system("clear")
     print(f"voçe digitou letras e simbolos\ntente novamente!")
     time.sleep(1)



