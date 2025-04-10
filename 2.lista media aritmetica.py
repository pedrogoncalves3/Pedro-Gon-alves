import os
os.system("clear")


notas = []

for i in range(4):
    nota = float(input(f"digite sua {i + 1}ª nota: "))
    notas.append(nota)
    
soma = sum(notas) 
media = soma / 4

if media > 7:
    print(f"voçe foi APROVADO com uma media de {media}")

elif media >= 5:
    print(f"voçe está de RECUPERAÇÂO com uma media de {media}")
    
elif media < 5:
    print(f"voçe foi REPROVADO com uma media de {media}")
 
print() 
print("as notas informadas foram:")

for nota in notas:
    print(f"{nota}")
  
        