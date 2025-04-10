import os
os.system("clear || cls")

lista_notas = []

for i in range(3):
    nota = float(input(f"digite sua {i + 1}ª nota: "))
    lista_notas.append(nota)


media = sum(lista_notas) / 3



print()
for nota in lista_notas:  #foreach
    
    
    print(f"nota:  {nota}")
 
    
print(f"primeiro número: {lista_notas[0]}")

print(f"media: {media}")     
   


    