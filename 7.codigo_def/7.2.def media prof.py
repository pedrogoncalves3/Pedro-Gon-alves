import os
os.system("clear")




def calcular(soma):
     return soma / 3


for i in range(3):
     nota = float(input("digite suas notas: "))
     soma += nota 
 

media = calcular(soma)   

print(f"a soma dos números e igual a: {soma}")
print(f"media: {media}")

