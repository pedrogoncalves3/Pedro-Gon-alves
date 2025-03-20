import os
import time
os.system("clear")


for i in range( 1, 21,2 ):
    print(f" os números impares sao: {i}")
    time.sleep (0.20)  #espera 1 segundo

print("acabou. ")

#outra opção

for i in range( 1, 21,2 ):
   if i % 2 == 1:
    time.sleep (0.20)  #espera 1 segundo

print("acabou. ")