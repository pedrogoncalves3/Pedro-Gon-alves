import os
import time
os.system("clear")

nu1 = int(input("digite a tabuada que deseja ver: "))
print (f"a tabuada do número: {nu1} ")

for i in range( 1, 11 ):
    print(f"{nu1} x {i} = {nu1 * i}")
    time.sleep (0.20)  #espera 1 segundo
   
    
pergunta = input("deseja algo mais?  ")  

if pergunta == "não":
    print("ok tenha um bom dia")

if pergunta == "sim":
    (input("com oque eu posso te ajudar? "))    