import os
os.system("clear")  

def tranformador(numero):
    if numero % 2 == 0:
     print("e par")
    else:
       print("o número e impar") 

numero = int(input("digite um numero: "))
tranformador(numero)
