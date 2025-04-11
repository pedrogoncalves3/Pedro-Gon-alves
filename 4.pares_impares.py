import os
os.system("clear")

numeros = []

def pares_impares(numeros):
    pares = 0
    impares = 0
    
   
    for i in range(6):    
        n = int(input(f"digite o {i + 1}ª número: " ))
        numeros.append(n)
    
        if n % 2 == 0:
           pares +=1
        else:
           impares += 1   
    return pares,impares

quantidade_pares,quantidade_impares = pares_impares(numeros)

os.system("clear")

for i, n in enumerate(numeros , start =1):
 print(f"{i}ª número: {n}")  
print()
print(f"voçe digitou {quantidade_pares} numeros pares")
print(f"voçe digitou {quantidade_impares} numeros impares")
