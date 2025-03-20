import os
import time
os.system("clear")

soma = 0

for i in range(1, 6):
  numero =   int(input(" digite um números: ")) 
  #soma = soma + numero
  soma += numero   

print(f"a soma dos números e igual a: {soma}")