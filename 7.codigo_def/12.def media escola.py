import os
os.system("clear")

soma = 0

def somar(soma):  
     return soma / 2



for i in range(2):
     nota = float(input("digite as suas notas aqui: "))
     soma += nota


media = somar(soma)

if soma >7:
     resultado = "voçe passou de ano!"
elif soma <6:
     resultado = " voçe está de recuperacão"     



print(f"sua média foi: {media}")
print(f"resultado: {resultado}")

